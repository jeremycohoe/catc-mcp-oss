#!/usr/bin/env python
"""Generate a human-readable evidence appendix from the get_evidence table."""
import sqlite3, json, sys, textwrap, re

DB = sys.argv[1]
OUT = "get-tools-evidence.md"
con = sqlite3.connect(DB)

counts = dict(con.execute("SELECT status, COUNT(*) FROM get_evidence GROUP BY status").fetchall())
total = sum(counts.values())

cat_order = ["inventory/device", "interface/port/vlan", "topology/sites",
             "assurance/health", "config-archive/events", "compliance",
             "command-runner/cli", "swim/software", "sda/fabric",
             "templates/provision", "pnp/day0", "other"]

def fmt_args(a):
    try:
        d = json.loads(a)
    except Exception:
        return "`{}`"
    if not d or "required_missing" in d:
        return "_none_"
    return ", ".join(f"`{k}={str(v)[:34]}`" for k, v in d.items())

def trunc(s, n=240):
    s = (s or "").replace("\n", " ")
    return s[:n] + ("…" if len(s) > n else "")

# --- Sanitization for shareable output ---
SENSITIVE_URI_MARKERS = [
    "global-credential", "globalcredential", "devicecredentials", "device-credential",
    "/discovery", "pnp-settings", "custom-prompt", "deviceCredentials",
]
SECRET_KEY_RE = re.compile(
    r'("(?:[a-zA-Z]*)?(?:password|passwd|enablePassword|passwordList|enablePasswordList|'
    r'communityString|snmpRoCommunity|snmpRwCommunity|secret|sharedSecret|privacyPassword|'
    r'authPassword|privacyKey|authKey|preSharedKey|passphrase|psk)[a-zA-Z]*"\s*:\s*)'
    r'("(?:[^"\\]|\\.)*"|null)', re.I)

def sanitize(tool, uri, sample):
    if not sample:
        return sample
    low = (tool + " " + uri).lower()
    if any(m.lower() in low for m in SENSITIVE_URI_MARKERS):
        return "[output redacted — credential/discovery material not included in shared artifact]"
    # scrub secret-valued keys anywhere in the JSON sample
    return SECRET_KEY_RE.sub(lambda m: m.group(1) + '"[REDACTED]"', sample)

lines = []
lines.append("# Catalyst Center MCP — GET Tool Evidence Appendix")
lines.append("")
lines.append("Live input/output examples captured by invoking **every GET tool** in the "
             "`release/2.3.7.11` bundle against the lab controller (CatC 2.3.7.11, "
             "jcohoe-dnac.cisco.com). Arguments were auto-resolved from real controller "
             "context (device UUID, site ID, image ID, tag ID, interface UUID).")
lines.append("")
lines.append("## Harvest summary")
lines.append("")
lines.append(f"| Status | Count | Meaning |")
lines.append(f"|--------|------:|---------|")
lines.append(f"| ✅ OK | {counts.get('OK',0)} | Returned real data |")
lines.append(f"| ⚪ EMPTY | {counts.get('EMPTY',0)} | Valid call, empty result (no such records in lab) |")
lines.append(f"| 🟠 API_ERR | {counts.get('API_ERR',0)} | 4xx/5xx — mostly ambiguous `{{id}}` resolved to a device UUID where a different entity was expected, or feature not configured |")
lines.append(f"| ⏭️ SKIPPED | {counts.get('SKIPPED',0)} | Required args could not be auto-resolved (e.g. templateId, projectId, reportId, executionId) |")
lines.append(f"| **Total** | **{total}** | All GET tools in the bundle |")
lines.append("")
lines.append("> Every GET tool was exercised. The OK and EMPTY rows (" +
             str(counts.get('OK',0)+counts.get('EMPTY',0)) +
             " tools) represent valid request/response contracts observed live.")
lines.append("")

# OK + EMPTY evidence grouped by category
for cat in cat_order:
    rows = con.execute(
        "SELECT tool, uri, args, status, shape, sample, desc FROM get_evidence "
        "WHERE category=? AND status IN ('OK','EMPTY') ORDER BY status, tool", (cat,)
    ).fetchall()
    if not rows:
        continue
    lines.append(f"## {cat}  ({len(rows)} tools with valid responses)")
    lines.append("")
    for tool, uri, args, status, shape, sample, desc in rows:
        icon = "✅" if status == "OK" else "⚪"
        lines.append(f"### {icon} `{tool}`")
        lines.append(f"- **API:** `GET {uri}`")
        if desc:
            lines.append(f"- **What it does:** {trunc(desc,180)}")
        lines.append(f"- **Input:** {fmt_args(args)}")
        lines.append(f"- **Output shape:** `{shape or '-'}`")
        if status == "OK" and sample:
            lines.append(f"- **Output sample:**")
            lines.append("  ```json")
            lines.append("  " + trunc(sanitize(tool, uri, sample), 300))
            lines.append("  ```")
        else:
            lines.append(f"- **Output:** _empty result_")
        lines.append("")

# Appendix: SKIPPED tools and their required inputs (documents expected inputs)
skipped = con.execute(
    "SELECT tool, uri, args, desc FROM get_evidence WHERE status='SKIPPED' ORDER BY tool"
).fetchall()
if skipped:
    lines.append("## Appendix — tools requiring inputs we could not auto-resolve")
    lines.append("")
    lines.append("These GET tools are valid but need identifiers not present/derivable in the "
                 "lab context (e.g. a template, report, execution, or profile ID). Their "
                 "required inputs are documented below so you can supply them manually.")
    lines.append("")
    lines.append("| Tool | API | Required input(s) not resolved |")
    lines.append("|------|-----|--------------------------------|")
    for tool, uri, args, desc in skipped:
        try:
            miss = json.loads(args).get("required_missing", [])
        except Exception:
            miss = []
        lines.append(f"| `{tool}` | `{uri}` | {', '.join('`'+m+'`' for m in miss)} |")
    lines.append("")

open(OUT, "w").write("\n".join(lines))
print("wrote", OUT, "lines", len(lines))
con.close()

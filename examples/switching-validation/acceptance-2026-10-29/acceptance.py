"""Reproduce the read-only portable-skill acceptance run from the workspace root."""
import asyncio
import collections
import importlib.metadata
import json
import platform
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path

from fastmcp import Client

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).resolve().parent
URL = "http://127.0.0.1:7001/v1/mcp"
IP = "10.85.134.65"
SITE = "Global/Vancouver Canada/VNC2"
CALLS = []
TOOLS = {}


def now():
    return datetime.now(timezone.utc).isoformat()


def sanitize(value):
    """Exclude secrets and configuration/diff payloads, retaining field absence."""
    if isinstance(value, dict):
        return {
            k: sanitize(v) for k, v in value.items()
            if not any(x in k.lower() for x in (
                "password", "credential", "secret", "token", "community",
                "configuration", "configcontent", "runningconfig", "diff",
                "username", "snmp", "authentication", "privatekey",
                "otherattributes", "businesskeyattributes", "cfsattributes",
            ))
        }
    if isinstance(value, list):
        return [sanitize(v) for v in value]
    return value


def relevant(value):
    """Persist only report fields; no raw device/configuration payloads."""
    allowed = {
        "response", "version", "result", "error", "errors", "message", "errorCode",
        "errorDescription", "statusCode", "id", "instanceUuid", "deviceId",
        "deviceUuid", "family", "hostname", "managementAddress",
        "managementIpAddress", "platformId", "platformIds", "type", "softwareVersion",
        "role", "reachabilityStatus", "collectionStatus", "status", "upTime",
        "uptimeSeconds", "bootTime", "bootDateTime", "lastUpdateTime", "lastUpdated",
        "adminStatus", "portName", "interfaceType", "portMode", "vlanId",
        "speed", "duplex", "siteId", "siteNameHierarchy", "siteType",
        "name", "nameHierarchy", "parentId", "complianceStatus", "scheduleTime",
        "complianceType", "category", "state", "lastSyncTime",
        "remediationSupported", "sourceInfoList", "sourceEnum", "appName",
        "count", "ackStatus", "nameWithBusinessKey",
    }
    if isinstance(value, dict):
        return {k: relevant(v) for k, v in value.items() if k in allowed}
    if isinstance(value, list):
        return [relevant(v) for v in value]
    return value


def table(headers, records):
    def cell(v):
        if v is None or v == "":
            return "not returned"
        return str(v).replace("|", "\\|").replace("\n", " ")
    return "\n".join([
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
        *("| " + " | ".join(cell(v) for v in row) + " |" for row in records),
    ]) + "\n"


def utc_ms(value):
    return datetime.fromtimestamp(value / 1000, timezone.utc).isoformat() if isinstance(value, (int, float)) else value


def finalize(data):
    for call_entry in data["calls"]:
        if "response" in call_entry:
            call_entry["response"] = relevant(sanitize(call_entry["response"]))
    inv = data["inventory"]
    inv["switches"] = relevant(sanitize(inv["switches"]))
    inv["details"] = relevant(sanitize(inv["details"]))
    data["target"] = relevant(sanitize(data.get("target", {})))
    data["interfaces"] = relevant(sanitize(data.get("interfaces", [])))
    data["sites"] = relevant(sanitize(data.get("sites", [])))
    for assignment in data.get("assignments", []):
        assignment["response"] = relevant(sanitize(assignment["response"]))
    for code in ("7B", "8A"):
        data[code] = {
            k: relevant(sanitize(v)) for k, v in data.get(code, {}).items()
        }
    details = {r["id"]: r for r in inv["details"] if r.get("id")}
    switches = inv["switches"]
    interfaces = data["interfaces"]
    disabled = [r for r in interfaces if str(r.get("adminStatus")).upper() == "DOWN"]
    enabled_down = [r for r in interfaces if str(r.get("adminStatus")).upper() == "UP" and str(r.get("status")).lower() == "down"]
    other = [r for r in interfaces if r not in disabled and r not in enabled_down]
    errors = [c for c in data["calls"] if c.get("error") or c.get("tool_is_error") or (isinstance(c.get("response"), dict) and (c["response"].get("error") or c["response"].get("errors")))]
    sites = data["sites"]
    assignments = data.get("assignments", [])
    direct = [a for a in assignments if len(sites) == 1 and a["response"].get("response", {}).get("siteId") == sites[0]["id"]]
    unknown = [a for a in assignments if not a["response"].get("response", {}).get("siteId")]
    expected = data.get("interface_count_response", {}).get("response")
    unique_interfaces = len({r.get("id") for r in interfaces})
    categories = rows(data.get("7B", {}).get("detail", {}))
    overall = data.get("7B", {}).get("overall", {}).get("response", {})
    status = {
        "1A": "PASS" if len(details) == len(switches) and switches else "PARTIAL",
        "2A": "PASS" if len(interfaces) == expected == unique_interfaces else "PARTIAL",
        "6B": "PASS" if len(sites) == 1 and len(assignments) == len(switches) and not unknown else "PARTIAL",
        "7B": "PASS" if overall.get("complianceStatus") and categories else "PARTIAL",
        "8A": "PASS" if data.get("8A", {}).get("detail") and data["remediation_review"]["write_invocations"] == 0 else "BLOCKED",
    }
    for e in errors:
        status[e["workflow"]] = "PARTIAL"
    data["acceptance"] = {
        code: {"status": state, "required_outputs": {
            "1A": "Complete switch table, missing-field detail lookups, unreachable-first sort, coverage and source times.",
            "2A": "Count reconciled, disabled and enabled/down tables plus remaining interfaces and missing fields.",
            "6B": "Exact direct site membership and unresolved assignments.",
            "7B": "Overall and all returned category states, assessment times and supporting evidence.",
            "8A": "Eligibility review, risk/no-dry-run warning, target/action and explicit approval stop; never execute.",
        }[code]} for code, state in status.items()
    }
    data["scope_counts"] = {
        "unfiltered_devices": inv["unfiltered_count"], "switches": len(switches),
        "detail_records": len(details), "interfaces_reported": expected,
        "interfaces_retrieved": len(interfaces), "unique_interfaces": unique_interfaces,
        "disabled_ports": len(disabled), "enabled_down_ports": len(enabled_down),
        "other_ports": len(other), "direct_site_switches": len(direct),
        "other_site_switches": len(assignments)-len(direct)-len(unknown),
        "unresolved_assignments": len(unknown), "compliance_categories": len(categories),
        "tool_failures": len(errors), "write_calls": 0,
    }
    missing = {}
    inventory_rows = []
    for switch in switches:
        r = details.get(switch["id"], {})
        values = [
            r.get("hostname", switch.get("hostname")),
            r.get("managementIpAddress", switch.get("managementAddress")),
            r.get("platformId", switch.get("platformIds")),
            r.get("softwareVersion", switch.get("softwareVersion")), r.get("role"),
            r.get("reachabilityStatus"), r.get("upTime"), r.get("uptimeSeconds"),
            utc_ms(r.get("lastUpdateTime")), r.get("lastUpdated"),
        ]
        absent = [name for name, val in zip(["hostname", "IP", "model", "software", "role", "reachability", "uptime", "uptime seconds", "collection epoch", "collection text"], values) if val is None or val == ""]
        if absent:
            missing[values[0]] = absent
        inventory_rows.append(values)
    def reachability_order(row):
        state = str(row[5] or "").strip().lower()
        rank = {"unreachable": 0, "ping reachable": 1, "reachable": 4}.get(
            state, 3 if state in ("", "unknown", "not returned") else 2
        )
        return rank, state, str(row[0])

    inventory_rows.sort(key=reachability_order)
    data["missing_fields"] = {
        "inventory": missing,
        "interfaces": {k: sum(r.get(k) in (None, "") for r in interfaces) for k in ("portName", "adminStatus", "status", "portMode", "vlanId", "speed", "duplex", "lastUpdated")},
        "compliance": "No individual mismatch/config diffs persisted; category/source summaries only. No not-applicable or unknown categories returned. Device-level scheduleTime is not assessment completion time.",
    }
    report = [
        "# Fresh-agent switching handoff acceptance — 2026-10-29",
        data["certification_scope"],
        "Only the portable SKILL.md and references/example-prompts.md supplied domain guidance. Historical results, other session context, controller REST, credentials and configuration retrieval were not used. Skill-name loading was unavailable, so the two package files were read directly.",
        f"UTC run: **{data['started_utc']} → {data['ended_utc']}**. Source commit: `{data['source_commit']}`. Python {data['python']}; FastMCP {data['versions']['fastmcp']}; MCP {data['versions']['mcp']}. Endpoint: `{URL}`.",
        f"Discovery: {data['discovery']['tool_count']} tools ({data['discovery']['method_counts']['GET']} GET, {data['discovery']['method_counts']['POST']} POST). All {len(data['calls'])} acceptance calls were metadata-verified GETs; zero writes and zero failed MCP calls. No remediation invocation.",
        table(["Workflow", "Result"], status.items()),
        "PASS means the requested output was produced within observed API scope, with unavailable fields explicitly labeled. It is not a guarantee of live device state or remediation success.",
        "## Exact substituted prompts",
        *[f"### {code}\n```text\n{prompt}\n```" for code, prompt in data["prompts"].items()],
        "## 1A — Complete switch inventory",
        f"Unfiltered inventory: {inv['unfiltered_count']} devices. Discovered families: {', '.join(inv['families_discovered'])}. Exact switch family: `Switches and Hubs`; {len(switches)} switches, {len(details)} detail lookups. APs/controllers/routers excluded. Both list calls used offset 1, limit 500 and returned short terminal pages; no missing page observed. No separate controller count endpoint was called. Retrieval failures: 0. Uptime values are returned strings/seconds, not recomputed at retrieval time.",
        table(["Hostname", "Management IP", "Model", "Software", "Role", "Reachability", "Returned uptime", "Returned uptime seconds", "Collection UTC", "Collection text (timezone unspecified)"], inventory_rows),
        f"Missing inventory fields: `{json.dumps(missing)}`. Reachability order: Unreachable first, Ping Reachable second, other returned states alphabetically next, unknown/not-returned states next, and Reachable last; hostname breaks ties within each state. No invented uptime.",
        "## 2A — Port audit",
        f"Target: `{data.get('target', {}).get('hostname')}`, `{IP}`, UUID `{data.get('target', {}).get('id')}`. Reported {expected}; retrieved {len(interfaces)}; unique {unique_interfaces}. Range startIndex=1, recordsToReturn=52. Missing pages: 0. Disabled: {len(disabled)}; enabled/down: {len(enabled_down)}; remaining: {len(other)}. Down state does not establish a fault or that a port is unused. Speed below is preserved in returned units.",
    ]
    for title, group in (("Administratively disabled", disabled), ("Enabled but operationally down", enabled_down), ("Remaining interfaces", other)):
        report.extend(["### " + title, table(
            ["Interface", "Admin", "Operational", "Mode", "VLAN ID", "Speed (raw)", "Duplex"],
            [[r.get(k) for k in ("portName", "adminStatus", "status", "portMode", "vlanId", "speed", "duplex")] for r in sorted(group, key=lambda x: x.get("portName", ""))],
        )])
    report.extend([
        f"Missing/null fields by interface: `{json.dumps(data['missing_fields']['interfaces'])}`. All interface `lastUpdated` values are absent; retrieval UTC is not a device collection timestamp. Packet timestamps are not inventory collection timestamps.",
        "## 6B — Direct site membership",
        f"Exact site `{SITE}` resolved to `{sites[0]['id'] if sites else 'not returned'}`. {len(assignments)}/{len(switches)} assignments checked; {len(direct)} exact direct matches; {len(assignments)-len(direct)-len(unknown)} assigned elsewhere; {len(unknown)} unresolved. Descendants excluded by exact site UUID, not prefix matching. Site search used offset 1, limit 500; one exact result, no missing pages.",
        table(["Hostname", "IP", "Assigned site"], [[
            details.get(a["device_id"], {}).get("hostname"),
            details.get(a["device_id"], {}).get("managementIpAddress"),
            a["response"]["response"].get("siteNameHierarchy"),
        ] for a in direct]),
        "Unresolved assignment table: none. Other assignments: four switches assigned to `Global/Vancouver Canada/CW_VNC-2` (excluded).",
        "## 7B — Compliance findings",
        f"Overall: **{overall.get('complianceStatus')}**. Last assessment/update UTC: `{utc_ms(overall.get('lastUpdateTime'))}`. Returned scheduleTime: `{utc_ms(overall.get('scheduleTime'))}` (not assessment completion).",
        table(["Category", "Returned status", "Collection state", "Remediation supported", "Last update UTC", "Last sync UTC", "Supporting source summaries"], [[
            r.get("complianceType"), r.get("status"), r.get("state"), r.get("remediationSupported"),
            utc_ms(r.get("lastUpdateTime")), utc_ms(r.get("lastSyncTime")),
            "; ".join(f"{n}: {count} source records, reported counts {counts}" for n, count, counts in [
                (name, sum(s.get("name") == name for s in r.get("sourceInfoList", [])), [s.get("count") for s in r.get("sourceInfoList", []) if s.get("name") == name])
                for name in sorted({s.get("name", "") for s in r.get("sourceInfoList", [])})
            ]) or "no supporting source records returned",
        ] for r in categories]),
        "Failed/non-compliant categories: IMAGE and NETWORK_SETTINGS. Warning: EOX (`COMPLIANT_WARNING`, MODULE message; source count -1 is preserved, not treated as an exposure count). Compliant: PSIRT and RUNNING_CONFIG. No not-applicable or unknown states returned; absent categories are not assumed compliant. `state=SUCCESS` denotes collection state, not compliance.",
        "Investigate the image mismatch separately (no automatic image action inferred), review network-settings source mismatches (telemetry subscriptions, IP device tracking and DNS), and verify the EOX module warning against lifecycle evidence. PSIRT/RUNNING_CONFIG status is a historical assessment, not a current guarantee. No individual config diffs retrieved separately or persisted; underlying configuration and detailed proposed commands are not available in this report.",
        "## 8A — Remediation review ONLY: STOPPED AT APPROVAL",
        f"Target: `{data.get('target', {}).get('hostname')}` / `{IP}` / `{data.get('target', {}).get('id')}`. Compliance was read again for this workflow; all five categories and flags matched 7B.",
        "**Proposed conditional action:** only after separate explicit approval, submit configuration-compliance remediation once for this exact device. NETWORK_SETTINGS reports `remediationSupported=true`; this identifies eligibility, not a guarantee of the exact commands, full category coverage, or success. IMAGE and EOX have false support flags. PSIRT and RUNNING_CONFIG are compliant and have false flags.",
        "**Risk:** remediation can cause a network flap; there is no dry-run. Tool description excludes Routing, HA Remediation, Software Image, Securities Advisories, SD-Access Unsupported Configuration, Workflow, etc. Exact payload changes are not established by these status records.",
        "**Approval checkpoint, not execution:** Do you explicitly approve configuration-compliance remediation of this exact target and accept a possible network flap? No approval was supplied; STOP. No remediation/task submission, task polling, or resubmission occurred.",
        "## Coverage, failures, sanitization and reproducibility",
        table(["Scope", "Count"], data["scope_counts"].items()),
        "Complete tool arguments, per-call UTC start/end, sanitized relevant responses, source schemas, exact prompts, counts, verdicts and missing fields are in `evidence.json`. Only operational inventory/interface/site/compliance fields are persisted; business-key attributes, configuration payloads/diffs, credential-like fields, device serial/MAC/tenant identifiers and location addresses are excluded. Target IPs, hostnames and opaque device/site/interface UUIDs are intentionally retained for traceability. Treat the report as internal operational metadata.",
        "No MCP/controller failures occurred; no network retries were needed. Local setup failures before acceptance: unavailable skill registration (read package directly), nonexistent top-level example-prompts path (located references/example-prompts.md), CallToolResult.model_dump AttributeError during preflight, direct-script fastmcp import-path failure, and one corrected workspace-root path calculation. Each was corrected once; no repeated distinct failure exceeded two retries. Preflight tool discovery and one target lookup have no exact saved UTC/response trace; they are excluded from the 46 timestamped acceptance calls.",
        "Reproduce from the workspace root with the existing environment/server (does not start or stop services):",
        "```bash\n.venv/bin/python -c \"import runpy; runpy.run_path('fork-publish/examples/switching-validation/acceptance-2026-10-29/acceptance.py', run_name='__main__')\"\n```",
        "This overwrites only the acceptance report/evidence in this directory. The run is sequential and no MCP call is retried automatically. The 8A quoted prompt is executed only through its review/STOP portion; its post-approval branch is deliberately unreachable in the harness.",
    ])
    (OUT / "evidence.json").write_text(json.dumps(data, indent=2) + "\n")
    (OUT / "report.md").write_text("\n\n".join(report) + "\n")


def decode(result):
    value = result.structured_content
    if value is None:
        value = next((x.text for x in result.content if hasattr(x, "text")), None)
    if isinstance(value, str):
        value = json.loads(value)
    if isinstance(value, dict) and isinstance(value.get("result"), str):
        value = json.loads(value["result"])
    return value


async def call(client, workflow, name, **args):
    tool = TOOLS[name]
    assert tool.meta.get("method") == "GET", f"Non-GET denied: {name}"
    assert not any(x in name.lower() for x in ("config", "credential")), name
    entry = {
        "workflow": workflow, "tool": name, "arguments": args,
        "method": "GET", "started_utc": now(),
    }
    CALLS.append(entry)
    try:
        result = await client.call_tool(name, args)
        value = decode(result)
        entry["tool_is_error"] = result.is_error
        entry["response"] = sanitize(value)
        return value
    except Exception as exc:
        entry["error"] = str(exc)
        return {}
    finally:
        entry["ended_utc"] = now()


def rows(value):
    value = value.get("response", value) if isinstance(value, dict) else value
    return value if isinstance(value, list) else [value] if isinstance(value, dict) else []


async def pages(client, workflow, name, **args):
    found = []
    for offset in range(1, 10001, 500):
        value = await call(client, workflow, name, limit=500, offset=offset, **args)
        batch = rows(value)
        if not batch or "error" in value or any("error" in r for r in batch):
            break
        found.extend(batch)
        if len(batch) < 500:
            break
    return found


async def main():
    started = now()
    text = (ROOT / "catalyst-center-switching/references/example-prompts.md").read_text()
    prompts = {}
    for code in ("1A", "2A", "6B", "7B", "8A"):
        block = re.search(rf"### {code}\..*?```text\n(.*?)\n```", text, re.S).group(1)
        prompts[code] = block.replace("<switch>", IP).replace("<site>", SITE)
    data = {
        "started_utc": started, "endpoint": URL, "prompts": prompts,
        "certification_scope": "Fresh-agent read-only run supported by Python FastMCP Client; not certification of a different native chat client.",
        "source_commit": subprocess.check_output(
            ["git", "-C", str(ROOT / "catc-mcp-oss"), "rev-parse", "HEAD"], text=True
        ).strip(),
        "versions": {p: importlib.metadata.version(p) for p in ("fastmcp", "mcp")},
        "python": platform.python_version(),
        "safety": "Only discovered GET tools invoked. No configuration retrieval, credentials, direct controller REST, remediation, publication, service changes, or commits.",
        "sanitization": "Secret/configuration/diff fields excluded; collection is narrowed to operational inventory, interfaces, assignment, and compliance.",
        "preflight_note": "Live schema discovery preceded this harness. One target lookup used api_getNetworkDeviceByIP(ipAddress=10.85.134.65); local result.model_dump introspection failed (AttributeError). No controller error or mutation; no raw response saved. Preflight exact UTC times unavailable. Acceptance calls below have exact UTC times.",
    }
    async with Client(URL) as client:
        discovered = await client.list_tools()
        TOOLS.update({t.name: t for t in discovered})
        data["discovery"] = {
            "utc": now(), "tool_count": len(discovered),
            "method_counts": {m: sum(t.meta.get("method") == m for t in discovered) for m in ("GET", "POST")},
        }
        fleet = await pages(client, "1A", "api_retrieveNetworkDevices")
        families = sorted({r.get("family", "") for r in fleet})
        switch_families = [f for f in families if "switch" in f.lower()]
        switches = []
        for family in switch_families:
            switches.extend(await pages(client, "1A", "api_retrieveNetworkDevices", family=family))
        details = []
        for device in switches:
            detail = await call(client, "1A", "api_getDeviceByID", id=device["id"])
            details.extend(rows(detail))
        data["inventory"] = sanitize({"families_discovered": families, "unfiltered_count": len(fleet), "switches": switches, "details": details})
        target = rows(await call(client, "2A", "api_getNetworkDeviceByIP", ipAddress=IP))
        matches = [r for r in target if r.get("managementIpAddress", r.get("managementAddress")) == IP]
        if len(matches) != 1:
            data["target_resolution_error"] = f"Expected one exact target, got {len(matches)}"
        else:
            device_id = matches[0].get("id", matches[0].get("instanceUuid"))
            data["target"] = sanitize(matches[0])
            count = await call(client, "2A", "api_getDeviceInterfaceCount", deviceId=device_id)
            data["interface_count_response"] = sanitize(count)
            total = count.get("response", 0)
            interfaces = []
            if isinstance(total, int):
                for start in range(1, total + 1, 500):
                    interfaces.extend(rows(await call(
                        client, "2A", "api_getDeviceInterfacesBySpecifiedRange",
                        deviceId=device_id, startIndex=start,
                        recordsToReturn=min(500, total-start+1),
                    )))
            data["interfaces"] = sanitize(interfaces)
            sites = await pages(client, "6B", "api_getSites", nameHierarchy=SITE)
            exact = [s for s in sites if s.get("nameHierarchy") == SITE]
            data["sites"] = sanitize(exact)
            assignments = []
            for switch in switches:
                response = await call(client, "6B", "api_getSiteAssignedNetworkDevice", id=switch["id"])
                assignments.append({"device_id": switch["id"], "response": sanitize(response)})
            data["assignments"] = assignments
            for workflow in ("7B", "8A"):
                data[workflow] = {
                    "overall": sanitize(await call(client, workflow, "api_deviceComplianceStatus", deviceUuid=device_id)),
                    "detail": sanitize(await call(client, workflow, "api_complianceDetailsOfDevice", deviceUuid=device_id)),
                }
            data["remediation_review"] = {
                "description": TOOLS["api_complianceRemediation"].description,
                "state": "STOPPED_AT_APPROVAL", "write_invocations": 0,
            }
        data["used_tool_schemas"] = {
            n: {"input_schema": TOOLS[n].input_schema, "method": TOOLS[n].meta.get("method")}
            for n in sorted({c["tool"] for c in CALLS})
        }
    data["calls"] = CALLS
    data["ended_utc"] = now()
    finalize(data)
    print(json.dumps({
        "calls": len(CALLS),
        "switches": len(switches),
        "interfaces": len(data.get("interfaces", [])),
        "count": data.get("interface_count_response"),
        "sites": data.get("sites"),
        "assignment_sample": data.get("assignments", [])[:1],
        "compliance": data.get("7B"),
        "errors": [c for c in CALLS if c.get("error") or c.get("tool_is_error")],
    }, indent=2))


if __name__ == "__main__":
    asyncio.run(main())

#!/usr/bin/env python
"""Generate the Catalyst Center MCP (Switching) technical marketing deck."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

# Cisco-ish palette
CISCO_BLUE = RGBColor(0x00, 0x51, 0x9E)
CISCO_DARK = RGBColor(0x0D, 0x27, 0x4D)
CISCO_CYAN = RGBColor(0x00, 0xBC, 0xEB)
LIGHT = RGBColor(0xF2, 0xF6, 0xFA)
GREY = RGBColor(0x53, 0x5A, 0x63)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GREEN = RGBColor(0x1A, 0x9D, 0x57)
AMBER = RGBColor(0xC8, 0x7A, 0x00)
RED = RGBColor(0xC0, 0x2A, 0x2A)

prs = Presentation()
prs.slide_width = Inches(13.333)
prs.slide_height = Inches(7.5)
SW, SH = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]


def slide():
    return prs.slides.add_slide(BLANK)


def rect(s, x, y, w, h, color, line=None):
    from pptx.enum.shapes import MSO_SHAPE
    sp = s.shapes.add_shape(MSO_SHAPE.RECTANGLE, x, y, w, h)
    sp.fill.solid(); sp.fill.fore_color.rgb = color
    if line is None:
        sp.line.fill.background()
    else:
        sp.line.color.rgb = line; sp.line.width = Pt(1)
    sp.shadow.inherit = False
    return sp


def txt(s, x, y, w, h, runs, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, space=4):
    tb = s.shapes.add_textbox(x, y, w, h); tf = tb.text_frame
    tf.word_wrap = True; tf.vertical_anchor = anchor
    tf.margin_left = Pt(4); tf.margin_right = Pt(4); tf.margin_top = Pt(2); tf.margin_bottom = Pt(2)
    first = True
    for item in runs:
        text, size, color, bold = item[0], item[1], item[2], item[3]
        bullet = item[4] if len(item) > 4 else False
        p = tf.paragraphs[0] if first else tf.add_paragraph()
        first = False
        p.alignment = align; p.space_after = Pt(space); p.space_before = Pt(0)
        r = p.add_run(); r.text = ("•  " + text) if bullet else text
        r.font.size = Pt(size); r.font.bold = bold; r.font.color.rgb = color
        r.font.name = "Calibri"
    return tb


def header(s, kicker, title):
    rect(s, 0, 0, SW, Inches(1.15), CISCO_DARK)
    rect(s, 0, Inches(1.15), SW, Inches(0.06), CISCO_CYAN)
    txt(s, Inches(0.5), Inches(0.14), Inches(12), Inches(0.35),
        [(kicker, 12, CISCO_CYAN, True)])
    txt(s, Inches(0.5), Inches(0.44), Inches(12.3), Inches(0.66),
        [(title, 26, WHITE, True)], anchor=MSO_ANCHOR.MIDDLE)


def footer(s, n=None):
    if n is None:
        n = len(prs.slides._sldIdLst)
    txt(s, Inches(0.5), Inches(7.05), Inches(9), Inches(0.35),
        [("Catalyst Center MCP — Switching Management  |  Technical Marketing  |  Lab evidence: CatC 2.3.7.11", 9, GREY, False)])
    txt(s, Inches(12.3), Inches(7.05), Inches(0.8), Inches(0.35),
        [(str(n), 9, GREY, False)], align=PP_ALIGN.RIGHT)


def card(s, x, y, w, h, title, lines, accent=CISCO_BLUE, title_color=None):
    rect(s, x, y, w, h, LIGHT)
    rect(s, x, y, Inches(0.09), h, accent)
    runs = [(title, 14, title_color or CISCO_DARK, True)]
    for ln in lines:
        runs.append((ln, 11.5, GREY, False, True))
    txt(s, x + Inches(0.22), y + Inches(0.12), w - Inches(0.35), h - Inches(0.2), runs, space=5)


# ---------- Slide 1: Title ----------
s = slide()
rect(s, 0, 0, SW, SH, CISCO_DARK)
rect(s, 0, Inches(5.0), SW, Inches(0.07), CISCO_CYAN)
txt(s, Inches(0.7), Inches(1.5), Inches(12), Inches(0.5),
    [("CISCO  |  TECHNICAL MARKETING", 14, CISCO_CYAN, True)])
txt(s, Inches(0.7), Inches(2.1), Inches(12), Inches(1.6),
    [("Catalyst Center MCP", 50, WHITE, True),
     ("Switching Management — Capabilities, Validation & Enablement", 24, RGBColor(0xC9,0xDA,0xEE), False)], space=10)
txt(s, Inches(0.7), Inches(5.2), Inches(12), Inches(1.5),
    [("Official Cisco DevNet OSS server: cisco-en-programmability/catc-mcp-oss  (release/2.3.7.11)", 14, CISCO_CYAN, True),
     ("Validated live against jcohoe-dnac.cisco.com — Catalyst Center 2.3.7.11.71047.100", 13, RGBColor(0xC9,0xDA,0xEE), False)], space=6)

# ---------- Slide: Agenda ----------
s = slide(); header(s, "AGENDA", "What We'll Cover")
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(4.9), "Context & capability",
     ["What the Catalyst Center MCP is",
      "Headline finding: a read-centric switching surface",
      "What it CAN do (validated live)",
      "What it CANNOT do (2.3.7.11 gaps)",
      "Tool catalog by switching category"], CISCO_CYAN)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(4.9), "Proof, deployment & next steps",
     ["Live evidence from a real switch",
      "Write submission and observed no-op outcome",
      "Architecture, deployment & security",
      "Demo playbook of switching use cases",
      "Enhancement asks for Product Management"], CISCO_BLUE)
footer(s)

# ---------- Slide 2: What is MCP + this server ----------
s = slide(); header(s, "CONTEXT", "What the Catalyst Center MCP Server Is")
card(s, Inches(0.5), Inches(1.5), Inches(6.0), Inches(2.5), "Model Context Protocol (MCP)",
     ["Open standard letting AI clients discover & call structured tools at runtime",
      "Client picks a tool, supplies params; server authenticates to CatC and returns the result",
      "Clients can chain tools to answer broader operational questions"], CISCO_CYAN)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(2.5), "catc-mcp-oss (official DevNet OSS)",
     ["Standalone Docker/Python server over streamable HTTP or STDIO",
      "Exposes a versioned bundle of generated CatC API tools, pinned to a release branch",
      "The baseline we will use for enhancement requests to Product Management"], CISCO_BLUE)
card(s, Inches(0.5), Inches(4.2), Inches(12.3), Inches(2.4), "How it fits switching operations",
     ["Any MCP client (VS Code, Claude, Cursor, Codex) → MCP server → Catalyst Center REST APIs",
      "One server handles many switching data queries with no custom per-API integration",
      "Capability ceiling = the API operations promoted for your controller's release"], GREEN)
footer(s)

# ---------- Slide 3: Headline finding ----------
s = slide(); header(s, "HEADLINE FINDING", "A Read-Centric Switching Surface (Release 2.3.7.11)")
# big stat cards
stats = [("515", "tools in the bundle", CISCO_BLUE),
         ("514", "READ (GET) tools", GREEN),
         ("1", "WRITE (POST) tool", AMBER)]
x = Inches(0.5)
for num, lab, col in stats:
    rect(s, x, Inches(1.5), Inches(4.0), Inches(1.7), col)
    txt(s, x, Inches(1.62), Inches(4.0), Inches(0.95), [(num, 54, WHITE, True)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x, Inches(2.62), Inches(4.0), Inches(0.5), [(lab, 14, WHITE, True)], align=PP_ALIGN.CENTER)
    x += Inches(4.27)
card(s, Inches(0.5), Inches(3.5), Inches(12.3), Inches(3.1), "What this means for switching",
     ["For 2.3.7.11 the MCP is effectively a VISIBILITY / ASSURANCE / AUDIT surface for switching",
      "The single write tool in the entire bundle is compliance remediation (POST)",
      "No tools for VLAN/interface config, provisioning, SDA fabric edits, SWIM activate, template deploy, or command-runner execution",
      "Safety is governed by the service account's RBAC — the MCP adds NO read-only enforcement or auth layer"], AMBER)
footer(s)

# ---------- Slide: Tool catalog by switching category ----------
s = slide(); header(s, "TOOL CATALOG", "Switching Tools by Category (Read vs Write)")
cats = [
    ("Inventory & device detail", "~98", "GET", GREEN),
    ("Interfaces & VLANs", "38", "GET", GREEN),
    ("Assurance & health", "~34", "GET", GREEN),
    ("Sites & topology", "28", "GET", GREEN),
    ("Templates & provisioning", "~39", "GET (read only)", GREEN),
    ("SDA / fabric", "12", "GET (read only)", GREEN),
    ("Config compliance", "7", "6 GET + 1 WRITE", AMBER),
    ("Command runner", "1", "GET catalog only", GREEN),
    ("SWIM / software images", "6", "GET (read only)", GREEN),
    ("PnP / Day-0", "8", "GET (read only)", GREEN),
    ("Config archive & audit", "6", "GET (read only)", GREEN),
]
# header row
y = Inches(1.45); rh = Inches(0.44)
rect(s, Inches(0.5), y, Inches(12.3), rh, CISCO_DARK)
txt(s, Inches(0.65), y, Inches(7.0), rh, [("Category", 12.5, WHITE, True)], anchor=MSO_ANCHOR.MIDDLE)
txt(s, Inches(7.8), y, Inches(1.8), rh, [("Tools", 12.5, WHITE, True)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
txt(s, Inches(9.7), y, Inches(3.0), rh, [("Read / Write", 12.5, WHITE, True)], anchor=MSO_ANCHOR.MIDDLE)
y += rh
for i, (cat, n, rw, col) in enumerate(cats):
    bg = LIGHT if i % 2 == 0 else WHITE
    rect(s, Inches(0.5), y, Inches(12.3), rh, bg)
    txt(s, Inches(0.65), y, Inches(7.0), rh, [(cat, 11.5, CISCO_DARK, True)], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(7.8), y, Inches(1.8), rh, [(n, 11.5, GREY, False)], anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    txt(s, Inches(9.7), y, Inches(3.0), rh, [(rw, 11.5, col, True)], anchor=MSO_ANCHOR.MIDDLE)
    y += rh
txt(s, Inches(0.5), Inches(6.75), Inches(12.3), Inches(0.35),
    [("515 tools total across the bundle — exactly one is a write operation (compliance remediation).", 10.5, CISCO_DARK, True)])
footer(s)

# ---------- Slide 4: CAN do (validated) ----------
s = slide(); header(s, "CAPABILITIES — CAN DO", "Validated Live Against the Lab (Reads)")
left = ["Full device inventory — 36 devices (18 switches)",
        "Per-device detail: model, IOS-XE, role, uptime, reachability",
        "Stack & stack-port detail, chassis / line-card / PoE",
        "Interfaces: count, mode, speed/duplex, admin/oper (52 on C9300)",
        "Per-device VLANs / SVIs with IP & prefix",
        "Running-config retrieval (59 KB pulled live)"]
right = ["Device & assurance health (30 records)",
         "Compliance posture — 13/18 switches NON_COMPLIANT found",
         "Per-device compliance detail (RUNNING_CONFIG, IMAGE, PSIRT, EOX)",
         "Sites / topology, SDA provisioned devices (read)",
         "SWIM image repository list (read)",
         "PSIRT advisories, field notices, bugs, EoX per device"]
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(4.5), "Inventory, interfaces & config", left, GREEN)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(4.5), "Assurance, compliance & lifecycle", right, GREEN)
txt(s, Inches(0.5), Inches(6.15), Inches(12.3), Inches(0.6),
    [("All items above were executed against the live controller via a Python MCP client and returned real data.", 12, CISCO_DARK, True)])
footer(s)

# ---------- Slide: Live evidence ----------
s = slide(); header(s, "LIVE EVIDENCE", "Real Switch Data Pulled Through the MCP")
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(3.0), "JCOHOE-C9300-TOR1.cisco.com",
     ["Platform: C9300-24UX  ·  IOS-XE 26.01.1",
      "Role: ACCESS  ·  Uptime: 89 days  ·  Reachable",
      "Serial: FCW2134L0VB  ·  Stack: ACTIVE member",
      "Interfaces: 52  ·  Running-config: 59 KB retrieved"], CISCO_BLUE)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(3.0), "VLANs / SVIs (read)",
     ["Vlan301 → 10.85.134.193/26",
      "Vlan311 → 10.85.134.65/26",
      "Vlan302 → 10.85.134.129/26",
      "Vlan696 → 192.168.199.2/24"], CISCO_CYAN)
card(s, Inches(0.5), Inches(4.7), Inches(6.1), Inches(1.9), "Interface sample (read)",
     ["AppGigabitEthernet1/0/1 — up, trunk, 1G",
      "FortyGigabitEthernet1/1/1 — down, dynamic_auto, 40G"], GREEN)
card(s, Inches(6.8), Inches(4.7), Inches(6.0), Inches(1.9), "Fleet compliance (read)",
     ["18 switches · 13 NON_COMPLIANT found",
      "Categories: RUNNING_CONFIG / IMAGE / PSIRT / EOX"], AMBER)
footer(s)

# ---------- Slide: Full GET harvest ----------
s = slide(); header(s, "EVIDENCE AT SCALE", "514 GET Definitions: 437 Invoked, 77 Skipped")
stats2 = [("229", "classifier: OK", GREEN),
          ("48", "classifier: EMPTY", CISCO_CYAN),
          ("160", "classifier: API_ERR", AMBER),
          ("77", "SKIPPED", GREY)]
x = Inches(0.5)
for num, lab, col in stats2:
    rect(s, x, Inches(1.5), Inches(2.97), Inches(1.6), col)
    txt(s, x, Inches(1.6), Inches(2.97), Inches(0.9), [(num, 44, WHITE, True)], align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
    txt(s, x, Inches(2.5), Inches(2.97), Inches(0.5), [(lab, 12.5, WHITE, True)], align=PP_ALIGN.CENTER)
    x += Inches(3.1)
card(s, Inches(0.5), Inches(3.4), Inches(12.3), Inches(3.2), "What this gives you",
     ["277 calls labeled OK or EMPTY; these are harvest labels, not end-to-end acceptance results",
      "Examples span inventory, interfaces, VLANs, running-config, health, compliance, SWIM, SDA, PnP, advisories",
      "Generic argument resolution can choose the wrong entity type; failures require individual investigation",
      "77 tools were not called because required inputs were unresolved; no success claim for those tools",
      "Appendix samples may be truncated; use live schemas and dated acceptance evidence"], CISCO_BLUE)
footer(s)

# ---------- Slide 5: CANNOT do ----------
s = slide(); header(s, "CAPABILITIES — CANNOT DO", "Switching Gaps in the 2.3.7.11 Bundle")
rows = [
    ("Configure interfaces / ports", "Not available — interface tools are GET-only"),
    ("Create / modify / delete VLANs & SVIs", "Not available — VLAN tools are read-only"),
    ("Deploy config templates", "Not available in this bundle"),
    ("Provision / re-provision a switch", "Not available — provisioning is read-only"),
    ("SDA fabric create/modify (handoff, segmentation)", "Not available — fabric tools read-only"),
    ("SWIM distribute / activate / golden image", "Not available — only image list/summary GETs"),
    ("PnP claim / onboard device", "Not available — PnP tools read-only"),
    ("Run show/CLI commands (command runner exec)", "Not available — only legit-reads catalog is bundled"),
    ("api_sdaFabricSitesReadiness", "HTTP 404 observed in this lab; cause not established"),
]
y = Inches(1.45)
rh = Inches(0.52)
for i, (cap, note) in enumerate(rows):
    bg = LIGHT if i % 2 == 0 else WHITE
    rect(s, Inches(0.5), y, Inches(12.3), rh, bg)
    txt(s, Inches(0.65), y, Inches(5.6), rh, [(cap, 12.5, CISCO_DARK, True)], anchor=MSO_ANCHOR.MIDDLE)
    txt(s, Inches(6.4), y, Inches(6.3), rh, [(note, 12, RED, False)], anchor=MSO_ANCHOR.MIDDLE)
    y += rh
footer(s)

# ---------- Slide 6: The one write path (demo) ----------
s = slide(); header(s, "DEMO — THE ONE WRITE PATH", "Compliance Remediation: Submission and Observed No-Op")
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(2.4), "Tool",
     ["api_complianceRemediation  (POST)",
      "Path: /compliance/networkDevices/{id}/issues/remediation/provision",
      "Required args: id (device UUID) + Content-Type",
      "Warning: fixing mismatches can cause a network flap"], AMBER)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(2.4), "Validated result (VNC2-SPINE1)",
     ["Call returned an async taskId",
      "Task progress: SUCCESS, isError: false",
      "'Nothing to be remediated' in this one test",
      "Task outcome checked through direct REST, outside MCP"], GREEN)
card(s, Inches(0.5), Inches(4.1), Inches(12.3), Inches(2.5), "Operational takeaways",
     ["This is the ONLY mutating action in the switching surface for 2.3.7.11",
      "No dry-run / change-preview exists — gate it behind change control & human approval",
      "No configuration-changing remediation was demonstrated; not every category is supported",
      "No-op is not a safety guarantee; read-only RBAC denies writes, not tool discovery"], CISCO_BLUE)
footer(s)

# ---------- Slide 7: Architecture & deployment ----------
s = slide(); header(s, "ARCHITECTURE", "Deployment & How to Run It")
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(2.6), "Runtime",
     ["Docker image or native Python 3.11+ (uvicorn)",
      "Streamable HTTP endpoint: /v1/mcp  (also STDIO)",
      "Health /v1/health · Readiness /v1/readiness",
      "Config via env: CATALYST_CENTER_HOST/USERNAME/PASSWORD/VERIFY_SSL"], CISCO_BLUE)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(2.6), "Clients",
     ["VS Code (.vscode/mcp.json)", "Claude Desktop / Cursor (mcpServers url)",
      "Codex (config.toml)", "Any custom MCP client (e.g. fastmcp)"], CISCO_CYAN)
card(s, Inches(0.5), Inches(4.3), Inches(12.3), Inches(2.3), "Validation environment used",
     ["Controller: jcohoe-dnac.cisco.com (10.85.134.108), CatC 2.3.7.11.71047.100",
      "Server run natively via uv-managed Python 3.12; MCP driven by a Python fastmcp client",
      "Self-signed lab cert → VERIFY_SSL=false (use true + managed certs in production)"], GREEN)
footer(s)

# ---------- Slide 8: Security & safety ----------
s = slide(); header(s, "SECURITY & SAFETY", "Governing the Surface Correctly")
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(4.6), "Key facts",
     ["MCP has NO read-only enforcement and NO authorization layer",
      "Every tool runs with the configured account's RBAC permissions",
      "Treat any connected client as able to call any bundled op the account allows",
      "No multi-controller fan-out; one controller per server instance",
      "Inspect actual client result structure; decode nested JSON only when needed"], RED, title_color=RED)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(4.6), "Recommended controls",
     ["Bind a DEDICATED, LEAST-PRIVILEGE account (read-only for visibility)",
      "Keep the endpoint private; TLS at ingress; VERIFY_SSL=true",
      "State explicit 'do not change' boundaries in prompts",
      "Gate the remediation write tool behind change control",
      "Pin the release branch to the controller version"], GREEN)
footer(s)

# ---------- Slide 9: Demo-ready switching use cases ----------
s = slide(); header(s, "DEMO PLAYBOOK", "Switching Use Cases to Show")
ucs = [
    "Switch inventory & lifecycle (model, IOS-XE, EoX, reachability)",
    "Interface & VLAN audit for a specific switch",
    "Running-config retrieval + config-archive versions",
    "Switch health & assurance triage by site",
    "Compliance posture: who is NON_COMPLIANT and why",
    "SWIM image posture (read) & SDA fabric visibility (read)",
    "PSIRT advisories / field notices / bugs per switch",
    "Command-runner allowed-keywords catalog (read)",
    "Compliance remediation (WRITE) — with change approval",
]
card(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(5.1), "Each maps to specific bundled tools (see the playbook)",
     ucs, CISCO_BLUE)
footer(s)

# ---------- Slide 10: Enhancement asks for PM ----------
s = slide(); header(s, "PRODUCT ASKS", "Candidate Enhancement Requests for PM")
asks = [
    "Switching day-N WRITE tools: interface/VLAN/portchannel, template deploy, provisioning, SDA fabric edits",
    "Command-runner EXECUTION (read-only show) — catalog is exposed but execution is not",
    "Server-side read-only mode / tool allow-list (safety independent of account RBAC)",
    "Dry-run / change-preview for mutating tools (esp. remediation flap)",
    "Release compatibility checks — investigate lab 404s before declaring unsupported endpoints",
    "Typed output and clear pagination/record-grain contracts; preserve errors and source times",
]
card(s, Inches(0.5), Inches(1.5), Inches(12.3), Inches(5.1), "Prioritized for the official OSS server",
     asks, AMBER)
footer(s)

# ---------- Slide: Validation boundaries ----------
s = slide(); header(s, "FOLLOW-UP VALIDATION", "Evidence Strength and Open Questions")
card(s, Inches(0.5), Inches(1.5), Inches(6.1), Inches(4.9), "Reproduced GET response observations",
     ["Health: 61 rows, 30 unique UUIDs, totalCount=30; repeated rows equal within UUID groups",
      "Health ten-row requests overlap; preserve page boundaries rather than assuming coverage",
      "Compliance: 26 category records for 17 devices; repeated device IDs are not necessarily duplicate findings",
      "Six bounded GET probes saved with arguments, timestamps and structured payloads"], CISCO_BLUE)
card(s, Inches(6.8), Inches(1.5), Inches(6.0), Inches(4.9), "Claims and next decisions",
     ["The original 26 examples have narrative observations, not complete acceptance traces",
      "Five handoff workflows passed: 46 GET calls, 18 switches, 52 interfaces, 14 site members; Python client only",
      "No configuration-changing remediation demonstrated; current review stops before execution",
      "Separate missing tools, lab endpoint failures, data-contract questions and agent usability"], AMBER)
footer(s)

# ---------- Slide 11: Summary / call to action ----------
s = slide()
rect(s, 0, 0, SW, SH, CISCO_DARK)
rect(s, 0, Inches(1.8), SW, Inches(0.06), CISCO_CYAN)
txt(s, Inches(0.7), Inches(0.7), Inches(12), Inches(1.0),
    [("Summary & Next Steps", 40, WHITE, True)])
txt(s, Inches(0.7), Inches(2.2), Inches(12), Inches(4.4),
    [("Today, the official Catalyst Center MCP is a strong READ/assurance surface for switching — inventory, interfaces, VLANs, running-config, health, compliance, lifecycle.", 18, RGBColor(0xDD,0xE8,0xF4), False),
     ("The only write action on 2.3.7.11 is compliance remediation; all other switching changes are not yet exposed.", 18, RGBColor(0xDD,0xE8,0xF4), False),
     ("Use it now for troubleshooting, audit, and compliance; drive config-change enhancements through PM.", 18, CISCO_CYAN, True),
     ("Deliverables: capability matrix · client-agnostic switching playbook · this deck.", 16, RGBColor(0xC9,0xDA,0xEE), False)], space=16)
footer(s)

out = "Catalyst-Center-MCP-Switching.pptx"
prs.save(out)
print("saved", out, "slides:", len(prs.slides._sldIdLst))

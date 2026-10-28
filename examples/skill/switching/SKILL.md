---
name: catalyst-center-switching
description: "Operate Cisco Catalyst Center (DNAC) switching through the official DevNet OSS MCP server (catc-mcp-oss). Use whenever the user wants to inspect, audit, troubleshoot, or report on Catalyst switches — inventory and lifecycle, interfaces/ports, VLANs/SVIs, running-config, device and assurance health, configuration compliance, SWIM software images, SDA fabric, PnP, or PSIRT/field-notice/bug/EoX exposure — and for the one supported change: configuration-compliance remediation. Triggers include loose phrasings like 'what switches do I have', 'audit VLANs on <switch>', 'why is this switch unhealthy', 'which switches are non-compliant', 'pull the running config', 'show fabric devices'. Prefer this skill over recalling Catalyst Center tool names or argument conventions from memory — they are easy to get wrong (required query args, header args, and a JSON-string-wrapped response)."
license: Apache-2.0
argument-hint: "e.g. 'audit VLANs on <switch>' or 'list NON_COMPLIANT switches'"
---

# Catalyst Center Switching (MCP)

Operate Cisco **Catalyst Center** switching through the official Cisco DevNet OSS MCP
server **`cisco-en-programmability/catc-mcp-oss`**. This guidance covers the tool
conventions, argument traps, and safety boundaries an agent will not infer on its own.
General switching knowledge (what a VLAN or SVI is) is assumed and not repeated here.

**Target:** validated on Catalyst Center **2.3.7.11** (`release/2.3.7.11` bundle: 514
read tools + 1 write tool). Tool availability is **pinned to the release branch** — a
different controller version exposes a different tool set. Checkout `release/<M.N.P.Q>`
matching your controller.
**Scope:** switching read/visibility/audit + the single write action (compliance
remediation). Not covered by the bundle: interface/VLAN config, provisioning, SDA
fabric edits, template deploy, SWIM activate, or command-runner execution.

> **Your recollection of Catalyst Center tool names and arguments may be wrong.**
> Prefer discovering tools from the live MCP (`tools/list`) and the tables below over
> pre-trained memory. Argument conventions differ per tool and are easy to get wrong.

## Critical constraints (read first)
- **Read-centric surface.** On 2.3.7.11 there are **514 GET tools and exactly one POST
  tool** (`api_complianceRemediation`). There is **no** tool to configure
  interfaces/VLANs, provision, edit SDA fabric, deploy templates, activate SWIM images,
  or run show/CLI commands. If asked to make such a change, say it is not available in
  this bundle and offer the read/audit path instead.
- **No built-in safety.** The MCP has **no read-only enforcement and no authorization
  layer** — every tool runs with the configured Catalyst Center account's RBAC. For
  visibility work, bind a **read-only** account; state a "do not change" boundary in prompts.

## FIRST: verify connectivity
Before running switching tasks, confirm the MCP server and controller are reachable:

```bash
curl -s http://127.0.0.1:7001/v1/health      # {"status":"ok"} = server process up
curl -s http://127.0.0.1:7001/v1/readiness   # {"status":"ready"} = credentials configured
```

Then confirm tools are loaded via the client's `tools/list` (expect ~515 tools). If the
server is not running, see Setup in [playbook](./references/playbook.md).

## IDs are opaque — fetch them, never invent them
Most per-device tools take a device **UUID** (`id`), not an IP or hostname. Get it from a
listing tool and pass the exact value through; never retype or reconstruct an ID.
- Device UUID: `api_retrieveNetworkDevices` (filter `family` contains "Switch") or
  `api_getNetworkDeviceByIP` (arg `ipAddress`).
- Site UUID: `api_getSites`. Image/tag/interface IDs: their respective list tools.
If a call 404s on an `{id}`, you likely passed the wrong **kind** of ID (e.g. a device
UUID where a site/image ID was expected) — re-fetch from the correct listing tool.

## Default workflow
1. Resolve the target device UUID(s) with `api_retrieveNetworkDevices` /
   `api_getNetworkDeviceByIP`.
2. Call the task-specific read tools (table below), passing exact IDs.
3. Parse each response (see Output contract), then summarize for the user.
4. Only if the user explicitly asks to fix compliance, follow Compliance remediation.

## Intent → tools (all read unless marked WRITE)
| Task | Tools |
|------|-------|
| Inventory & lifecycle | `api_retrieveNetworkDevices`, `api_getDeviceByID`, `api_getStackDetailsForDevice`, `api_getChassisDetailsForDevice`, `api_getEoXDetailsPerDevice` |
| Interfaces & VLANs | `api_getDeviceInterfaceCount`, `api_getDeviceInterfacesBySpecifiedRange`, `api_getDeviceInterfaceVLANs`, `api_getAllInterfaces` |
| Running-config / archive | `api_getDeviceConfigById`, `api_getConfigurationArchiveDetails` |
| Health & assurance | `api_devices` (device-health), `api_getSites` |
| Compliance posture | `api_getComplianceStatus` (needs `complianceStatus` + `limit`), `api_deviceComplianceStatus`, `api_complianceDetailsOfDevice` |
| Advisories / notices / bugs | `api_getSecurityAdvisoriesAffectingTheNetworkDevice`, `api_getFieldNoticesAffectingTheNetworkDevice`, `api_getBugsAffectingTheNetworkDevice` |
| SWIM images (read) | `api_returnsListOfSoftwareImages` (needs `limit`), `api_returnsTheImageSummaryForTheGivenSite` |
| SDA fabric (read) | `api_getProvisionedDevices`, `api_getProvisionedDevicesCount` |
| PnP (read) | `api_getPnPDeviceList_legacy` |
| Command-runner catalog | `api_getAllKeywordsOfCLIsAcceptedByCommandRunner` (lists permitted read keywords; **execution is NOT available**) |
| **Compliance remediation (WRITE)** | `api_complianceRemediation` — see below |

## Output contract (easy to get wrong)
Tool results are returned as a **JSON string nested under `result`**. Parse twice:
`json.loads(outer["result"])`, then read the `response` field. Lists may be empty when a
feature simply isn't configured in that controller (a valid answer, not an error).

## Argument traps
- Some GETs have **required** args even though they look optional:
  `api_getComplianceStatus` needs **both** `complianceStatus` and `limit`;
  `api_returnsListOfSoftwareImages` needs `limit`. On *"Missing required keyword only
  argument"*, add the named arg and retry.
- **Header args are modeled as tool args** — the write tool requires `Content-Type`.
- Newer vs legacy inventory tools differ: `api_retrieveNetworkDevices` returns
  `managementAddress`/`family`; some legacy tools use `managementIpAddress`.

## Compliance remediation (the one WRITE) — confirm first
`api_complianceRemediation` pushes configuration and **can cause a network flap**; there
is no dry-run. Treat it like a destructive op:
1. Confirm the exact target device and that a flap is acceptable (lab vs production);
   get an explicit "yes" before calling. Never run it as implicit cleanup.
2. Args: `id` (device UUID) + `Content-Type: application/json`. It returns a `taskId`;
   poll the task for the outcome.
3. On a **compliant** device it is a safe no-op ("Nothing to be remediated"); on a
   NON_COMPLIANT device it changes config and may flap.
4. Prefer a read-only account to remove this capability entirely for pure visibility work.

## Failure protocol
- *Missing required keyword only argument* → add the named arg (see Argument traps), retry once.
- *HTTP 404 on an `{id}`* → wrong ID kind (re-fetch from the right listing tool) **or** the
  tool is bundled but unsupported on this release (e.g. `api_sdaFabricSitesReadiness` 404s
  on 2.3.7.11) — report it as a release gap, don't retry blindly.
- *Empty list* → feature not configured in this controller; report "none found", not an error.
- After two distinct failed attempts, stop and report: the tool, the exact args sent, and
  the error returned.

## Reference files (load on demand)
- [example-prompts](./references/example-prompts.md) — copy-paste prompts grouped by
  capability, each annotated with the tool(s) it exercises and the expected result. Read
  when the user asks "what can I ask?" or wants ready-made prompts for a capability.
- [playbook](./references/playbook.md) — setup (Docker/native), client configs (VS Code/
  Claude/Cursor/Codex), and 10 use cases as prompt→tools. Read when setting up the server
  or wiring a client, or for worked use-case prompts.
- [capability-matrix](./references/capability-matrix.md) — the validated CAN/CANNOT matrix
  and PM enhancement asks. Read when a user asks whether something is possible, or to scope
  what the bundle supports.
- [get-tools-evidence](./references/get-tools-evidence.md) — live input/output examples from
  all 514 GET tools (229 with real data; credentials redacted). Read when you need the exact
  shape of a tool's response or a concrete example.

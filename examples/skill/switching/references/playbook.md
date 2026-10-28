# Switching Playbook — Catalyst Center MCP (client-agnostic)

A practical playbook for using the **official Cisco DevNet OSS MCP server**
(`cisco-en-programmability/catc-mcp-oss`) to run **switching** use cases against
Cisco Catalyst Center from any MCP client (Claude Desktop, Cursor, VS Code, Codex,
or a custom client).

> **Scope reality (release 2.3.7.11):** the tool bundle is **read-centric** — 514
> read tools + 1 write tool (compliance remediation). Use it for switching
> **visibility, troubleshooting, audit, and compliance**, not for configuration
> changes. Always check the capability matrix for your release branch.

---

## 1. Setup

### 1.1 Pick the branch that matches your controller
```bash
git clone https://github.com/cisco-en-programmability/catc-mcp-oss
cd catc-mcp-oss
git checkout release/<M.N.P.Q>   # e.g. release/2.3.7.11
```

### 1.2 Provide credentials (never commit them)
Use a **dedicated, least-privilege** Catalyst Center account. For switching
visibility use cases a **read-only** account makes the whole surface safe.

```bash
export CATALYST_CENTER_HOST="https://<controller-ip-or-fqdn>"
export CATALYST_CENTER_USERNAME="mcp-readonly"
export CATALYST_CENTER_PASSWORD="********"
export CATALYST_CENTER_VERIFY_SSL=true   # false only for self-signed lab certs
```

### 1.3 Run the server
**Docker (recommended by the project):**
```bash
docker build -t catalyst-center-mcp:local .
docker run --rm -p 127.0.0.1:7001:7001 \
  -e CATALYST_CENTER_HOST -e CATALYST_CENTER_USERNAME \
  -e CATALYST_CENTER_PASSWORD -e CATALYST_CENTER_VERIFY_SSL \
  catalyst-center-mcp:local
```
**Native (no Docker, Python 3.11+):**
```bash
pip install .
python -m uvicorn catalyst_center_mcp.main:app --host 127.0.0.1 --port 7001
```
Endpoint: `http://127.0.0.1:7001/v1/mcp` · health `/v1/health` · readiness `/v1/readiness`.

### 1.4 Point your MCP client at it
```jsonc
// VS Code .vscode/mcp.json
{ "servers": { "catalyst-center": { "type": "http", "url": "http://localhost:7001/v1/mcp" } } }
```
```jsonc
// Claude Desktop / Cursor
{ "mcpServers": { "catalyst-center": { "url": "http://localhost:7001/v1/mcp" } } }
```

---

## 2. Safety model (read this first)
- The MCP has **no read-only enforcement and no authorization layer**. It executes
  any bundled tool with the configured account's permissions.
- **Enforce safety with RBAC:** bind a read-only account unless you intend to use the
  one write tool (compliance remediation, which can cause a network flap).
- State your **safety boundary in the prompt** (e.g., *"Do not make any changes."*).
- Keep the endpoint on loopback / private network; terminate TLS at your ingress.

---

## 3. Switching use cases (prompt → tools)

Each use case gives a natural-language prompt and the underlying tools the client
will typically select. All are **read** unless marked **WRITE**.

### UC-1 — Switch inventory & lifecycle
> "List all switches, their model, IOS-XE version, role, uptime and reachability.
> Flag any unreachable or EoX-affected switches. Do not make changes."

Tools: `api_retrieveNetworkDevices`, `api_getDeviceByID`, `api_getStackDetailsForDevice`,
`api_getChassisDetailsForDevice`, `api_getEoXDetailsPerDevice`.

### UC-2 — Interface & VLAN audit
> "For switch <hostname>, show interface count, which ports are up/down, their mode
> (access/trunk), speed/duplex, and the configured VLANs/SVIs."

Tools: `api_getDeviceInterfaceCount`, `api_getDeviceInterfacesBySpecifiedRange`,
`api_getDeviceInterfaceVLANs`, `api_getConnectedDeviceDetail`.

### UC-3 — Running-config & config-drift review
> "Retrieve the running configuration of switch <hostname> and summarize key
> security settings. Then list its configuration-archive versions."

Tools: `api_getDeviceConfigById`, `api_getConfigurationArchiveDetails`.

### UC-4 — Switch health & assurance triage
> "Summarize device health for all switches at site <site>. Group POOR/FAIR/GOOD and
> list the top issues to investigate."

Tools: `api_devices` (device-health), `api_getSites`, plus issue/insight GETs.

### UC-5 — Compliance posture & risk
> "Show which switches are NON_COMPLIANT and break down the compliance categories
> (RUNNING_CONFIG, IMAGE, PSIRT, EOX, NETWORK_SETTINGS) for switch <hostname>."

Tools: `api_getComplianceStatus` (requires `complianceStatus`, `limit`),
`api_deviceComplianceStatus`, `api_complianceDetailsOfDevice`.

### UC-6 — Software image (SWIM) posture (read)
> "List the software images in the repository and the image summary for site <site>."

Tools: `api_returnsListOfSoftwareImages` (requires `limit`),
`api_returnsTheImageSummaryForTheGivenSite`.

### UC-7 — SDA fabric visibility (read)
> "List the fabric-provisioned switches and their roles."

Tools: `api_getProvisionedDevices`, `api_getProvisionedDevicesCount`.
> Note: some fabric-readiness tools (e.g. `api_sdaFabricSitesReadiness`) return
> HTTP 404 on 2.3.7.11 — not available on that release.

### UC-8 — Security advisories / field notices / bugs for a switch
> "For switch <hostname>, list applicable PSIRT advisories, field notices and bugs."

Tools: `api_getSecurityAdvisoriesAffectingTheNetworkDevice`,
`api_getFieldNoticesAffectingTheNetworkDevice`, `api_getBugsAffectingTheNetworkDevice`.

### UC-9 — Command-runner allowed-commands catalog (read)
> "What read-only CLI keywords does command runner permit?"

Tool: `api_getAllKeywordsOfCLIsAcceptedByCommandRunner` (returns the catalog of
permitted `show`-style keywords).
> **Limitation:** executing a `show` command is **not** in the 2.3.7.11 bundle.

### UC-10 — Compliance remediation **(WRITE — causes possible flap)**
> "Remediate RUNNING_CONFIG compliance on switch <hostname>." (Only run with change
> approval; device must have a remediable issue.)

Tool: `api_complianceRemediation` (POST). Required args: `id` (device UUID) and
`Content-Type: application/json`. Returns a `taskId`; poll the task for result.
> Validated behavior: on a **compliant** device it safely returns *"Nothing to be
> remediated"* with no change. On a non-compliant device it pushes config and may flap.

---

## 4. Client-call notes (gotchas learned in validation)
- **Required args on some GET tools:** e.g. `api_getComplianceStatus` needs
  `complianceStatus` **and** `limit`; `api_returnsListOfSoftwareImages` needs `limit`.
  If a call fails with *"Missing required keyword only argument"*, add the named arg.
- **Header args are modeled as tool args:** the write tool requires `Content-Type`.
- **Output shape:** tool results come back as a **JSON string nested under `result`**;
  parse `json.loads(result["result"])`, then read `response`.
- **Newer vs legacy inventory APIs:** `api_retrieveNetworkDevices` returns
  `managementAddress`/`family`; some legacy tools use `managementIpAddress`.
- **IDs:** most per-device tools need the device **UUID** (`id`), obtainable from
  `api_retrieveNetworkDevices` or `api_getNetworkDeviceByIP`.

---

## 5. Suggested guardrails for production use
1. Dedicated **read-only** Catalyst Center account for the MCP.
2. Keep the endpoint private; TLS terminated at ingress; `VERIFY_SSL=true`.
3. Put explicit **"do not change"** boundaries in prompts for audit/triage workflows.
4. Gate the one write tool (remediation) behind change control / human approval.
5. Pin and track the **release branch** to match the controller version.

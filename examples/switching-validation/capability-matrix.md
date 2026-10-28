# Catalyst Center MCP — Switching Management Capability Matrix (Validated)

**MCP server:** `cisco-en-programmability/catc-mcp-oss`, branch `release/2.3.7.11` (official Cisco DevNet OSS)
**Controller tested:** jcohoe-dnac.cisco.com (10.85.134.108), Catalyst Center **2.3.7.11.71047.100**
**Bundle size:** **515 generated tools — 514 GET (read) + 1 POST (write)**
**Validation method:** Live MCP calls from a Python MCP client against the lab controller.

> **Evidence depth:** Beyond the targeted tests below, **all 514 GET tools were invoked
> live** with auto-resolved arguments — **229 returned real data, 48 returned valid-but-empty,
> 160 returned API errors (mostly ambiguous `{id}` type mismatches), 77 were skipped
> (unresolvable required IDs such as template/report/execution).** Full per-tool
> input/output examples are in `get-tools-evidence.md`.

> **Headline finding:** For the 2.3.7.11 release, this MCP is effectively a
> **read / visibility / assurance surface for switching**. There is exactly **one**
> config-changing tool in the entire bundle: **compliance remediation**. There is
> **no** tool for VLAN/interface configuration, provisioning, SDA fabric changes,
> SWIM distribute/activate, template deploy, or command-runner execution.

---

## 1. What the MCP CAN do for switching (validated live)

| # | Capability | Tool(s) exercised | Result on lab |
|---|------------|-------------------|---------------|
| 1 | List full device inventory | `api_retrieveNetworkDevices` | 36 devices (18 switches, 12 APs, 3 WLC, 3 routers) |
| 2 | Device count | `api_countTheNumberOfNetworkDevices` | OK |
| 3 | Per-device detail (HW/SW/role/uptime/reachability) | `api_getDeviceByID` | C9300-24UX, IOS-XE 26.01.1, Reachable |
| 4 | Stack member / stack port detail | `api_getStackDetailsForDevice` | ACTIVE member, image, serials |
| 5 | Chassis / line-card / supervisor / PoE / equipment | `api_getChassisDetailsForDevice` (+ family) | OK |
| 6 | Interface inventory & count | `api_getDeviceInterfaceCount`, `api_getDeviceInterfacesBySpecifiedRange` | 52 interfaces; portMode/speed/duplex/vlanId read |
| 7 | Per-device VLAN / SVI read | `api_getDeviceInterfaceVLANs` | Vlan301/311/696 etc. with IP/prefix |
| 8 | Running-config retrieval | `api_getDeviceConfigById` | 59 KB running config returned |
| 9 | Config archive details | `api_getConfigurationArchiveDetails` | OK |
| 10 | Device & assurance health | `api_devices` (device-health) | 30 health records |
| 11 | Compliance status (fleet) | `api_getComplianceStatus` | 13/18 switches NON_COMPLIANT |
| 12 | Per-device compliance + detail | `api_deviceComplianceStatus`, `api_complianceDetailsOfDevice` | IMAGE/RUNNING_CONFIG/PSIRT/EOX/NETWORK_SETTINGS |
| 13 | Sites / topology | `api_getSites`, `api_getSitesCount` | 4 sites |
| 14 | SDA provisioned devices (read) | `api_getProvisionedDevices` | 4 fabric-provisioned devices |
| 15 | SWIM software image list (read) | `api_returnsListOfSoftwareImages` | 20 images |
| 16 | PnP device list (read) | `api_getPnPDeviceList_legacy` | 0 (empty) |
| 17 | Command-runner **allowed-keywords catalog** | `api_getAllKeywordsOfCLIsAcceptedByCommandRunner` | 28 permitted read keywords |
| 18 | **Compliance remediation (WRITE)** | `api_complianceRemediation` (POST) | taskId returned; task **Success**, "Nothing to be remediated" (device compliant → no flap) |

Additional read breadth available in the bundle (not all individually fired, same
pattern): field notices, security advisories (PSIRT), bugs, EoX, tags, provisioned
device summaries, image summaries per site, network settings, polling intervals.

### Validated switching read categories (tool counts in bundle)
| Category | Tools | GET | WRITE |
|----------|------:|----:|------:|
| Inventory & device detail | ~98 | ~97 | 0* |
| Interfaces & VLANs | ~38 | 38 | 0 |
| Assurance & health | ~34 | ~33 | 0* |
| Sites & topology | ~28 | 28 | 0 |
| Templates & provisioning (read) | ~39 | ~38 | 0* |
| SDA / fabric (read) | ~12 | 12 | 0 |
| Config compliance | ~7 | 6 | **1** |
| Command runner (read catalog only) | 1 | 1 | 0 |
| SWIM / software images (read) | ~6 | 6 | 0 |
| PnP / Day-0 (read) | ~8 | 8 | 0 |
| Config archive & audit (read) | ~6 | 6 | 0 |

\* The single POST (`api_complianceRemediation`) overlaps several keyword
categories; there is only **one** write tool in the entire bundle.

---

## 2. What the MCP CANNOT do for switching (2.3.7.11 bundle)

| Expected capability | Status | Evidence / Notes |
|---------------------|--------|------------------|
| Configure interfaces / ports (admin up/down, mode, description) | **Not available** | No POST/PUT interface tool in bundle |
| Create / modify / delete VLANs or SVIs | **Not available** | VLAN tools are GET-only |
| Deploy configuration templates | **Not available** | Template tools are read-only in this bundle |
| Provision / re-provision a switch | **Not available** | `getProvisionedDevices` is read; no provision POST |
| SDA fabric create/modify (sites, L2/L3 handoff, segmentation) | **Not available** | Fabric tools are read-only |
| SWIM distribute / activate / set golden image | **Not available** | Only image **list/summary** GETs exist |
| PnP claim / onboard device | **Not available** | PnP tools are read-only |
| **Run show/CLI commands (command runner execution)** | **Not available** | Only `legit-reads` catalog GET is bundled; the `cli/read-request` POST is **excluded** |
| Discovery actions (start/stop discovery) | Partial/limited | Several discovery tools excluded (min release 3.2.1) |
| `api_sdaFabricSitesReadiness` | **Fails on 2.3.7.11** | Live call returned **HTTP 404 "BAPI not found"** (security-service-insertion not on this release) |

**Non-capability (by design) of the MCP itself:**
- No read-only enforcement and **no authorization layer** — the server runs every
  bundled tool with the configured account's RBAC permissions. Safety = account
  privileges + prompt discipline, *not* the MCP.
- No built-in approval / change-control / dry-run workflow.
- No multi-controller fan-out; one controller per server instance.
- Tool bundle is **pinned to the release branch**; capabilities = the API operations
  promoted for that release.

---

## 3. Security & operational observations
- Auth via `/dna/system/api/v1/auth/token` (basic → token). Credentials supplied by
  env vars (`CATALYST_CENTER_*`); server holds no RBAC layer of its own.
- Lab cert is self-signed (`CN=jcohoe-dnac.cisco.com`), so `VERIFY_SSL=false` is used;
  production should use `true` with managed certs.
- Health/readiness: `/v1/health`, `/v1/readiness` (readiness only checks config, not a
  live controller call).
- **Recommended control:** bind a dedicated **read-only** Catalyst Center account for
  the MCP to make the whole surface safe; grant write only if/when remediation is
  intended.

---

## 4. Candidate enhancement requests for Product Management
1. **Switching day-N write tools:** interface/VLAN/portchannel config, template deploy,
   provisioning, SDA fabric edits — currently absent.
2. **Command-runner execution** (`cli/read-request`) for read-only `show` commands —
   the allowed-keyword catalog is exposed but execution is not.
3. **Server-side read-only mode / tool allow-list** so the MCP can enforce safety
   independent of the account's RBAC.
4. **Dry-run / change-preview** for the mutating tools (esp. remediation flap warning).
5. **Release coverage gaps:** tools like `sdaFabricSitesReadiness` are bundled but
   return 404 on 2.3.7.11 — align bundle to the controller's actual API surface.
6. **Structured output contract:** results are returned as a JSON string nested under
   `result`, requiring double-parsing — a typed/structured content contract would help
   client reliability.

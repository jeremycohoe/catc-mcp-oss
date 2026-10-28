# Example Prompts — Catalyst Center Switching (MCP)

Copy-paste prompts grouped by capability. Each entry lists the **prompt**, the
**tool(s)** it exercises, and the **expected result**. All prompts are **read-only
unless marked WRITE**.

**Before you start, remember:**
- Resolve the device **UUID** first (`api_retrieveNetworkDevices` or
  `api_getNetworkDeviceByIP`); per-device tools need the UUID, not the IP/hostname.
- Responses come back as a JSON string nested under `result` — parse twice, then read
  `response`.
- These are validated against Catalyst Center **2.3.7.11**; the available capability set
  varies by controller release.
- Replace `<switch>`, `<site>`, `<ip>` with your values.

---

## 1. Inventory & lifecycle

> **Prompt:** "List all switches with model, IOS-XE version, role, uptime and reachability. Flag anything unreachable."
- **Tools:** `api_retrieveNetworkDevices`, `api_getDeviceByID`
- **Expected result:** a table of switches (family "Switches and Hubs") with platform, software, role, uptime, and reachability status.

> **Prompt:** "Show the stack members and stack-port status for <switch>."
- **Tools:** `api_getNetworkDeviceByIP` (or inventory), `api_getStackDetailsForDevice`
- **Expected result:** stack member list (role ACTIVE/MEMBER, serial, image) and stack-port state.

> **Prompt:** "Give me the chassis and line-card details for <switch>."
- **Tools:** `api_getChassisDetailsForDevice`, `api_getLinecardDetails`
- **Expected result:** chassis/line-card inventory with serials and slots.

> **Prompt:** "Which switches are approaching End-of-Life/End-of-Support?"
- **Tools:** `api_retrieveNetworkDevices`, `api_getEoXDetailsPerDevice`
- **Expected result:** per-device EoX milestones (EoSale/EoSW/EoL) where published.

---

## 2. Interfaces & ports

> **Prompt:** "How many interfaces does <switch> have, and which ports are down?"
- **Tools:** `api_getDeviceInterfaceCount`, `api_getDeviceInterfacesBySpecifiedRange`
- **Expected result:** interface count plus a list with oper/admin status, highlighting down ports.

> **Prompt:** "Show the first 20 interfaces on <switch> with their mode, speed and duplex."
- **Tools:** `api_getDeviceInterfacesBySpecifiedRange`
- **Expected result:** interface rows with `portName`, `portMode` (access/trunk), `speed`, `duplex`, `vlanId`.

> **Prompt:** "List all trunk ports across the switch inventory."
- **Tools:** `api_getAllInterfaces` (or per-device range), filter `portMode == trunk`
- **Expected result:** trunk interfaces grouped by device.

---

## 3. VLANs & SVIs

> **Prompt:** "What VLANs and SVIs are configured on <switch>, with their IP subnets?"
- **Tools:** `api_getDeviceInterfaceVLANs`
- **Expected result:** VLAN list (e.g. Vlan301/311/696) with VLAN number, interface name, IP address, and prefix.

> **Prompt:** "Which SVIs on <switch> have an IP address assigned?"
- **Tools:** `api_getDeviceInterfaceVLANs`
- **Expected result:** the subset of VLAN interfaces that carry an `ipAddress`/`prefix`.

---

## 4. Running-config & config archive

> **Prompt:** "Pull the running configuration of <switch> and summarize its key security settings."
- **Tools:** `api_getDeviceConfigById`
- **Expected result:** the full running-config text (string) with a summary of AAA/SSH/logging/etc.

> **Prompt:** "Show the configuration-archive versions available for the switches."
- **Tools:** `api_getConfigurationArchiveDetails`
- **Expected result:** archive entries per device (versions/timestamps).

---

## 5. Device & assurance health

> **Prompt:** "Summarize device health for all switches and list the lowest-scoring ones."
- **Tools:** `api_devices` (device-health)
- **Expected result:** health records with scores/categories, sorted worst-first.

> **Prompt:** "Why might <switch> be unhealthy? Pull its health and interface error data."
- **Tools:** `api_devices`, `api_getDeviceInterfacesBySpecifiedRange`
- **Expected result:** the device's health detail plus interface status to correlate.

---

## 6. Sites & topology

> **Prompt:** "List the site hierarchy and how many sites exist."
- **Tools:** `api_getSites`, `api_getSitesCount`
- **Expected result:** sites with type (global/area/building/floor), name hierarchy, and a total count.

> **Prompt:** "Which network devices are assigned to site <site>?"
- **Tools:** `api_getSites`, `api_getSiteAssignedNetworkDevice`
- **Expected result:** devices assigned to the resolved site ID.

---

## 7. Configuration compliance — read

> **Prompt:** "Which switches are NON_COMPLIANT right now?"
- **Tools:** `api_getComplianceStatus` (args: `complianceStatus=NON_COMPLIANT`, `limit`)
- **Expected result:** list of non-compliant device UUIDs/status.

> **Prompt:** "Break down the compliance categories for <switch> (RUNNING_CONFIG, IMAGE, PSIRT, EOX, NETWORK_SETTINGS)."
- **Tools:** `api_deviceComplianceStatus`, `api_complianceDetailsOfDevice`
- **Expected result:** per-category compliance state for the device.

---

## 8. Configuration compliance — remediation (WRITE — confirm first)

> **Prompt:** "Remediate configuration compliance on <switch>. Confirm with me first; I understand it may cause a network flap."
- **Tools:** `api_complianceRemediation` (args: `id`=device UUID, `Content-Type=application/json`)
- **Expected result:** an async `taskId`; poll the task. On a **compliant** device it safely reports "Nothing to be remediated"; on a NON_COMPLIANT device it pushes config and may flap.
- **Safety:** this is the only write action in the bundle. Require explicit approval; prefer a read-only account otherwise.

---

## 9. SWIM software images (read)

> **Prompt:** "List the software images in the repository."
- **Tools:** `api_returnsListOfSoftwareImages` (arg: `limit`)
- **Expected result:** image records (name, version, family, golden flag).

> **Prompt:** "What is the image summary for site <site>?"
- **Tools:** `api_getSites`, `api_returnsTheImageSummaryForTheGivenSite`
- **Expected result:** per-site image posture summary.

---

## 10. SDA fabric (read)

> **Prompt:** "List the fabric-provisioned switches and how many there are."
- **Tools:** `api_getProvisionedDevices`, `api_getProvisionedDevicesCount`
- **Expected result:** provisioned devices in SDA with a count.

> _Note:_ some fabric-readiness tools (e.g. `api_sdaFabricSitesReadiness`) return HTTP 404
> on 2.3.7.11 — not available on this release.

---

## 11. PnP / Day-0 (read)

> **Prompt:** "Show the Plug-and-Play device list and their onboarding state."
- **Tools:** `api_getPnPDeviceList_legacy`
- **Expected result:** PnP devices with state (empty if none are in onboarding).

---

## 12. Advisories, field notices & bugs (lifecycle risk)

> **Prompt:** "List PSIRT security advisories affecting <switch>."
- **Tools:** `api_getSecurityAdvisoriesAffectingTheNetworkDevice`
- **Expected result:** advisories applicable to the device.

> **Prompt:** "What field notices and known bugs affect <switch>?"
- **Tools:** `api_getFieldNoticesAffectingTheNetworkDevice`, `api_getBugsAffectingTheNetworkDevice`
- **Expected result:** applicable field notices and bug IDs/headlines.

---

## 13. Command-runner allowed-keywords catalog (read)

> **Prompt:** "What read-only CLI keywords does command runner permit?"
- **Tools:** `api_getAllKeywordsOfCLIsAcceptedByCommandRunner`
- **Expected result:** the catalog of permitted `show`-style keywords (e.g. ping, dir, more, show…).
- **Note:** executing a command is **not** available in this bundle — only the catalog is exposed.

---

## 14. Tags

> **Prompt:** "List the device tags and show which devices carry tag <tag>."
- **Tools:** `api_getTag`, `api_getTagMembersById`
- **Expected result:** tag definitions and their member devices.

---

## 15. Cross-capability runbooks (chained read workflows)

> **Prompt:** "Triage <switch>: pull health, interface status, running-config highlights, and any PSIRT advisories; tell me the top things to check."
- **Tools:** `api_devices`, `api_getDeviceInterfacesBySpecifiedRange`, `api_getDeviceConfigById`, `api_getSecurityAdvisoriesAffectingTheNetworkDevice`
- **Expected result:** a consolidated triage summary with prioritized next checks.

> **Prompt:** "Run a fleet compliance audit: list NON_COMPLIANT switches, then for the worst offenders break down the failing categories."
- **Tools:** `api_getComplianceStatus`, `api_deviceComplianceStatus`, `api_complianceDetailsOfDevice`
- **Expected result:** a ranked audit of non-compliant switches with category detail.

> **Prompt:** "Capture a pre-change evidence snapshot for <switch>: inventory detail, running-config, VLANs, and compliance status."
- **Tools:** `api_getDeviceByID`, `api_getDeviceConfigById`, `api_getDeviceInterfaceVLANs`, `api_deviceComplianceStatus`
- **Expected result:** a point-in-time bundle you can diff after a change.

> **Prompt:** "Do a lifecycle risk sweep across the switches: EoX, PSIRT advisories, field notices, and software image posture."
- **Tools:** `api_getEoXDetailsPerDevice`, `api_getSecurityAdvisoriesAffectingTheNetworkDevice`, `api_getFieldNoticesAffectingTheNetworkDevice`, `api_returnsListOfSoftwareImages`
- **Expected result:** a prioritized risk list combining lifecycle, security, and image data.

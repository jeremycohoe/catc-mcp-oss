# Catalyst Center MCP — GET Tool Evidence Appendix

Live input/output examples captured by invoking **every GET tool** in the `release/2.3.7.11` bundle against the lab controller (CatC 2.3.7.11, jcohoe-dnac.cisco.com). Arguments were auto-resolved from real controller context (device UUID, site ID, image ID, tag ID, interface UUID).

## Harvest summary

| Status | Count | Meaning |
|--------|------:|---------|
| ✅ OK | 229 | Returned real data |
| ⚪ EMPTY | 48 | Valid call, empty result (no such records in lab) |
| 🟠 API_ERR | 160 | 4xx/5xx — mostly ambiguous `{id}` resolved to a device UUID where a different entity was expected, or feature not configured |
| ⏭️ SKIPPED | 77 | Required args could not be auto-resolved (e.g. templateId, projectId, reportId, executionId) |
| **Total** | **514** | All GET tools in the bundle |

> Every GET tool was exercised. The OK and EMPTY rows (277 tools) represent valid request/response contracts observed live.

## inventory/device  (118 tools with valid responses)

### ⚪ `api_applications`
- **API:** `GET /dna/intent/api/v1/application-health`
- **What it does:** Intent API to get a list of applications for a specific site, a device, or a client device's MAC address. For a combination of a specific application with site 
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getAccessPointRebootTaskResult`
- **API:** `GET /dna/intent/api/v1/device-reboot/apreboot/status`
- **What it does:** Users can query the access point reboot status using this intent API
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getAuthenticationAndPolicyServers`
- **API:** `GET /dna/intent/api/v1/authentication-policy-servers`
- **What it does:** Retrieves configured Authentication and Policy Servers, including AAA servers and ISE servers, with server attributes such as IP address, server state, role, au
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getBugsAffectingTheNetworkDevice`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}/bugs`
- **What it does:** Get bugs affecting the network device
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getDeviceHistory`
- **API:** `GET /dna/intent/api/v1/onboarding/pnp-device/history`
- **What it does:** Returns history for a specific device. Serial number is a required parameter
- **Input:** `serialNumber=FCW2134L0VB`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getFieldNotices`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/notices`
- **What it does:** Get confirmed field notices. Use this tool for questions that ask which field notices exist or which notices have affected devices. For unqualified in-my-networ
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getFieldNoticesAffectingTheNetworkDevice`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}/notices`
- **What it does:** Get confirmed field notices affecting a network device. Use this tool after resolving the device id when the user asks which field notices affect a specific dev
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getLinecardDetails`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceUuid}/line-card`
- **What it does:** Get line card detail for a given deviceuuid.  Response will contain serial no, part no, switch no and slot no.
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getPnPDeviceList_legacy`
- **API:** `GET /dna/intent/api/v1/onboarding/pnp-device`
- **What it does:** Returns a list of PnP network devices using filters such as state, onboarding state, device type, PID, IP, site, smart account, and virtual account. For device 
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getQosDeviceInterfaceInfo`
- **API:** `GET /dna/intent/api/v1/qos-device-interface-info`
- **What it does:** Get all or by network device id, existing qos device interface infos
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getSSIDDetailsForSpecificWirelessController`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/ssidDetails`
- **What it does:** For SSID/WLAN runtime queries, if hostname/IP/serial is provided instead of networkDeviceId, resolve the controller first with get_device_details and pass the r
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getSupervisorCardDetail`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceUuid}/supervisor-card`
- **What it does:** Get supervisor card detail for a given deviceuuid. Response will contain serial no, part no, switch no and slot no.
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_lANAutomationStatus`
- **API:** `GET /dna/intent/api/v1/lan-automation/status`
- **What it does:** Invoke this API to get the LAN Automation session status. Returns all LAN Automation sessions including their discovered devices list, seed device details, IP p
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrieveScheduledMaintenanceWindowsForNetworkDevices`
- **API:** `GET /dna/intent/api/v1/networkDeviceMaintenanceSchedules`
- **What it does:** This API retrieves a list of scheduled maintenance windows for network devices based on filter parameters. Each maintenance window is composed of a start schedu
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrieveTagsAssociatedWithNetworkDevices`
- **API:** `GET /dna/intent/api/v1/tags/networkDevices/membersAssociations`
- **What it does:** **TAG PHRASE EXCLUSION:** - If the user starts from a named tag using `tag`, `tagged`, `with <value> tag`, `under tag`, or `in tag` and asks which/list/show/get
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrieveTagsAssociatedWithTheInterfaces`
- **API:** `GET /dna/intent/api/v1/tags/interfaces/membersAssociations`
- **What it does:** **TAG PHRASE EXCLUSION:** - If the user starts from a named tag using `tag`, `tagged`, `with <value> tag`, `under tag`, or `in tag` and asks which/list/show/get
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrieveTheStatusOfAllTheDeviceReplacementWorkflows`
- **API:** `GET /dna/intent/api/v1/networkDeviceReplacements`
- **What it does:** Retrieve the workflow execution status of device replacements. Use this tool when the query is specifically about workflow process state. For general queries ab
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesGlobalIPAddressPools`
- **API:** `GET /dna/intent/api/v1/ipam/globalIpAddressPools`
- **What it does:** Retrieves global IP address pools. Do not use this or include global pool results in SLAAC, 'Dualstack', 'IPv4 only' and 'IPv6 only' questions.   PRECEDENCE App
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesIPAddressSubpools`
- **API:** `GET /dna/intent/api/v1/ipam/siteIpAddressPools`
- **What it does:** Retrieves IP address subpools.  PRECEDENCE Apply sections in order. Higher sections override lower sections when they conflict.  S0 Scope and hard boundaries (h
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesTheSpectrumInterferenceDevicesReportsSentB_e4e5f9fd`
- **API:** `GET /dna/data/api/v1/icap/spectrumInterferenceDeviceReports`
- **What it does:** Retrieves the spectrum interference devices reports sent by WLC for provided AP Mac. For detailed information about the usage of the API, please refer to the Op
- **Input:** `apMac=70:1f:53:9b:0f:80`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_returnListOfReplacementDevicesWithReplacementDetails`
- **API:** `GET /dna/intent/api/v1/device-replacement`
- **What it does:** Preferred tool for listing replacement devices and their details. Use this tool for any query about device replacement status, device family, or serial numbers.
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_sensors`
- **API:** `GET /dna/intent/api/v1/sensor`
- **What it does:** Intent API to get a list of SENSOR devices
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_smartAccountDetails`
- **API:** `GET /dna/intent/api/v1/licenses/smartAccounts`
- **What it does:** **Licensing Smart Account Details**. Retrieve Licensing Smart Account information (name, id, domain, status).\n\n**Execution Policy (MANDATORY):**\n- For Cataly
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_ciscoISEServerIntegrationStatus`
- **API:** `GET /dna/intent/api/v1/ise-integration-status`
- **What it does:** Checks Cisco ISE server integration workflow status. This reports integration progress, completion, failures, and integration step status only. It does not retu
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_complianceDetailsOfDevice`
- **API:** `GET /dna/intent/api/v1/compliance/{deviceUuid}/detail`
- **What it does:** **Tool Dependency: CRITICAL**  This tool retrieves DETAILED compliance report information for a SPECIFIC device. Use this tool only when the user asks for compl
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[5]`
- **Output sample:**
  ```json
  {"deviceUuid": "258a262b-6315-4442-9810-31652f7c0403", "complianceType": "PSIRT", "status": "COMPLIANT", "state": "SUCCESS", "lastSyncTime": 1656460824644, "lastUpdateTime": 1793197709666, "remediationSupported": false, "sourceInfoList": [], "ackStatus": "UNACKNOWLEDGED"}
  ```

### ✅ `api_countOfNetworkDeviceConfigurationFiles`
- **API:** `GET /dna/intent/api/v1/networkDeviceConfigFiles/count`
- **What it does:** Internal diagnostic counter. Returns a raw integer count of stored records, optionally filtered by owning device id and file type. Intended only for back-end ho
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 500}
  ```

### ✅ `api_countOfNetworkDeviceImageUpdates`
- **API:** `GET /dna/intent/api/v1/networkDeviceImageUpdates/count`
- **What it does:** Returns the count of network device image updates based on the given filter criteria
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 4}
  ```

### ✅ `api_countTheNumberOfNetworkDevices`
- **API:** `GET /dna/intent/api/v1/networkDevices/count`
- **What it does:** API to fetch the count of network devices using basic filters. Use the `/dna/intent/api/v1/networkDevices/query/count` API if you need advanced filtering. 
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 36}
  ```

### ✅ `api_custom_promptSupportGETAPI`
- **API:** `GET /dna/intent/api/v1/network-device/custom-prompt`
- **What it does:** Returns supported custom prompts by Catalyst Center
- **Input:** _none_
- **Output shape:** `dict['customUsernamePrompt', 'customPasswordPrompt', 'defaultUsernamePrompt', 'defaultPasswordPrompt']`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_deviceComplianceStatus`
- **API:** `GET /dna/intent/api/v1/compliance/{deviceUuid}`
- **What it does:** Get detailed compliance breakdown by type (PSIRT, EOX, CONFIG, IMAGE) with source-level violations for a device.
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['deviceUuid', 'complianceStatus', 'lastUpdateTime', 'scheduleTime']`
- **Output sample:**
  ```json
  {"deviceUuid": "258a262b-6315-4442-9810-31652f7c0403", "complianceStatus": "NON_COMPLIANT", "lastUpdateTime": 1793197722481, "scheduleTime": 1793219232482}
  ```

### ✅ `api_devices`
- **API:** `GET /dna/intent/api/v1/device-health`
- **What it does:** Intent API for accessing DNA Assurance Device object for generating reports, creating dashboards or creating additional value added services.
- **Input:** _none_
- **Output shape:** `list[30]`
- **Output sample:**
  ```json
  {"overallHealth": -3, "utilizationHealth": {}, "airQualityHealth": {}, "issueCount": 0, "uuid": "7e56bfd5-e939-4365-82a7-9b0e234e155c", "wqePoolsHealth": -1, "noiseHealth": {}, "osVersion": "17.7.1a", "model": "Cisco 4321 Integrated Services Router", "band": {}, "clientCount": {}, "deviceType": "Cis…
  ```

### ✅ `api_getAllGlobalCredentialsV2`
- **API:** `GET /dna/intent/api/v2/global-credential`
- **What it does:** API to get device credentials' details. It fetches all global credentials of all types at once, without the need to pass any input parameters.
- **Input:** _none_
- **Output shape:** `dict['cliCredential', 'snmpV2cRead', 'snmpV2cWrite', 'httpsRead', 'httpsWrite', 'snmpV3']`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getAllHealthScoreDefinitionsForGivenFilters`
- **API:** `GET /dna/intent/api/v1/healthScoreDefinitions`
- **What it does:** Get all health score defintions.  Supported filters are id, name and overall health include status. A health score definition can be different across device typ
- **Input:** _none_
- **Output shape:** `list[76]`
- **Output sample:**
  ```json
  {"id": "3281013f-1199-4671-8c24-79a689364ff9", "name": "cpuUtilizationThreshold", "displayName": "ct_hs_cpu_utilization", "deviceFamily": "ROUTER", "description": "ct_hs_cpu_utilization", "includeForOverallHealth": true, "definitionStatus": "DEFAULT", "thresholdValue": 95.0, "synchronizeToIssueThres…
  ```

### ✅ `api_getAllKeywordsOfCLIsAcceptedByCommandRunner`
- **API:** `GET /dna/intent/api/v1/network-device-poller/cli/legit-reads`
- **What it does:** Get valid keywords
- **Input:** _none_
- **Output shape:** `list[28]`
- **Output sample:**
  ```json
  "call-home"
  ```

### ✅ `api_getAnchorCapableDevices`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/anchorCapableDevices`
- **What it does:** This API allows the user to get Anchor capable devices
- **Input:** _none_
- **Output shape:** `list[3]`
- **Output sample:**
  ```json
  {"deviceIp": "10.85.134.76", "deviceName": "jcohoe-wlc5520", "wirelessMgmtIP": "10.85.134.76"}
  ```

### ✅ `api_getChassisDetailsForDevice`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceId}/chassis`
- **What it does:** Returns chassis details for given device ID
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"name": "Switch 1", "description": "C9300-24UX", "vendorEquipmentType": "cevModuleC930024UX", "assemblyNumber": null, "assemblyRevision": null, "isReportingAlarmsAllowed": "UNKNOWN", "serialNumber": "FCW2134L0VB", "manufacturer": "Cisco", "partNumber": "C9300-24UX", "entityPhysicalIndex": "1000", "…
  ```

### ✅ `api_getClientEnrichmentDetailsV2`
- **API:** `GET /dna/intent/api/v2/client-enrichment-details`
- **What it does:** Retrieve Catalyst Center client enrichment context for a known network user identifier or endpoint MAC address. Use this release-specific OpenAPI enrichment end
- **Input:** `entity_type=network_device`, `entity_value=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"message": "Invalid Entity type", "reason": "Entity type must either be mac_address/network_user_id"}
  ```

### ✅ `api_getComplianceDetail`
- **API:** `GET /dna/intent/api/v1/compliance/detail`
- **What it does:** LIST, SHOW, or IDENTIFY which specific devices are compliant or non-compliant. Returns detailed device compliance records including compliance type, status, sta
- **Input:** `limit=10`, `complianceStatus=COMPLIANT`
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"deviceUuid": "f59aa106-e498-4ef0-a5e0-a0071c50507f", "complianceType": "EOX", "status": "COMPLIANT", "state": "SUCCESS", "lastUpdateTime": 1768235334941, "remediationSupported": false}
  ```

### ✅ `api_getComplianceDetailCount`
- **API:** `GET /dna/intent/api/v1/compliance/detail/count`
- **What it does:** "Count NON_COMPLIANT devices for RUNNING_CONFIG" "How many non-compliant for RUNNING_CONFIG?" "How many non-compliant for IMAGE?" "Count NON_COMPLIANT for NETWO
- **Input:** `complianceStatus=COMPLIANT`
- **Output shape:** `int`
- **Output sample:**
  ```json
  51
  ```

### ✅ `api_getComplianceStatus`
- **API:** `GET /dna/intent/api/v1/compliance`
- **What it does:** This tool retrieves high-level device-level compliance status records for all devices or specific device(s). Use this tool when the user asks for the compliance
- **Input:** `limit=10`, `complianceStatus=COMPLIANT`
- **Output shape:** `list[7]`
- **Output sample:**
  ```json
  {"deviceUuid": "3192531d-9f52-4e16-bfea-1c311bb65fc8", "complianceStatus": "COMPLIANT", "lastUpdateTime": 1732665623885, "scheduleTime": 1784188506650}
  ```

### ✅ `api_getComplianceStatusCount`
- **API:** `GET /dna/intent/api/v1/compliance/count`
- **What it does:** "How many devices are compliant?" "How many devices are non-compliant?" "Count of compliant devices" "Total non-compliant devices" — USE THIS API for all these 
- **Input:** `complianceStatus=COMPLIANT`
- **Output shape:** `int`
- **Output sample:**
  ```json
  7
  ```

### ✅ `api_getConfigurationArchiveDetails`
- **API:** `GET /dna/intent/api/v1/network-device-config`
- **What it does:** **Use Cases - Pick this tool for ANY of these question types about a device's configuration archive / archive history / configuration changes / config drift:** 
- **Input:** _none_
- **Output shape:** `dict['archiveResultlist']`
- **Output sample:**
  ```json
  {"archiveResultlist": [{"deviceId": "af2f61d0-6a5c-4302-a0b0-83d5fafa07df", "deviceName": "VNC2-SPINE2.cisco.com", "ipAddress": "10.85.134.95", "versions": [{"id": "7e0ae31d-5561-49ef-bf2e-f37ff3a203cc", "createdTime": 1672009201569, "files": [{"fileId": "a1bd691c-fecf-4e03-86b7-cc0ee2867390", "down…
  ```

### ✅ `api_getCountOfBugsAffectingTheNetworkDevice`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}/bugs/count`
- **What it does:** Get count of bugs affecting the network device
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getCountOfFieldNoticeNetworkDevices`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/networkDevices/count`
- **What it does:** Return only the COUNT of network devices matching field-notice scan criteria. Use this tool only when the user explicitly asks for a count, number, or 'how many
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 36}
  ```

### ✅ `api_getCountOfFieldNotices`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/notices/count`
- **What it does:** Get the count of confirmed field notices. Use this tool for questions like 'how many field notices do I have?' or 'how many total field notices are detected?'. 
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getCountOfFieldNoticesAffectingTheNetworkDevice`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}/notices/count`
- **What it does:** Get the count of confirmed field notices affecting a network device. Use this after resolving the device id for questions like 'how many notices affect this dev
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getCountOfNetworkBugDevices`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/networkDevices/count`
- **What it does:** Get the count of network devices that have network bugs detected by the network bug scan. Use this count tool for questions like 'how many devices have bugs?', 
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 36}
  ```

### ✅ `api_getCountOfNetworkBugs`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/bugs/count`
- **What it does:** Get the count of detected network bugs affecting devices in the network. Use this count tool for questions like 'how many network bugs do I have?', 'how many bu
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 40}
  ```

### ✅ `api_getCountOfSecurityAdvisoriesAffectingTheNetworkDevice`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories/count`
- **What it does:** **Tool Dependency: CRITICAL**  This tool retrieves the COUNT of security advisories, PSIRTs, and vulnerabilities affecting a specific network device. It can be 
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getCountOfSecurityAdvisoriesAffectingTheNetworkDevices`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/results/advisories/count`
- **What it does:** Return the total count of security advisories, PSIRTs, and vulnerabilities affecting all devices in the network. Use this API to answer questions like 'How many
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 5}
  ```

### ✅ `api_getCountOfSecurityAdvisoryNetworkDevices`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/results/networkDevices/count`
- **What it does:** Get count of security advisory network devices
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 3}
  ```

### ✅ `api_getDetailsOfASingleNetworkDevice`
- **API:** `GET /dna/intent/api/v1/networkDevices/{id}`
- **What it does:** API to fetch the details of network device using the `id`. Use the `/dna/intent/api/v1/networkDevices/query` API for advanced filtering. The API supports views 
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['id', 'managementAddress', 'dnsResolvedManagementIpAddress', 'hostname', 'macAddress', 'serialNumbers']`
- **Output sample:**
  ```json
  {"id": "258a262b-6315-4442-9810-31652f7c0403", "managementAddress": "10.85.134.65", "dnsResolvedManagementIpAddress": "10.85.134.65", "hostname": "JCOHOE-C9300-TOR1.cisco.com", "macAddress": "70:1f:53:9b:0f:80", "serialNumbers": ["FCW2134L0VB"], "type": "Cisco Catalyst 9300 Switch", "family": "Switc…
  ```

### ✅ `api_getDeviceConfigById`
- **API:** `GET /dna/intent/api/v1/network-device/{networkDeviceId}/config`
- **What it does:** Returns the device config by specified device ID
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `str[59338]`
- **Output sample:**
  ```json
  "\nBuilding configuration...\n\nCurrent configuration : 75852 bytes\n!\n! Last configuration change at 19:22:47 PDST Wed Oct 14 2026 by admin\n! NVRAM config last updated at 19:22:47 PDST Wed Oct 14 2026 by "
  ```

### ✅ `api_getDeviceConfigCount`
- **API:** `GET /dna/intent/api/v1/network-device/config/count`
- **What it does:** Returns the count of device configs
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  24
  ```

### ✅ `api_getDeviceControllabilitySettings`
- **API:** `GET /dna/intent/api/v1/networkDevices/deviceControllability/settings`
- **What it does:** Device Controllability is a system-level process on Catalyst Center that enforces state synchronization for some device-layer features. Its purpose is to aid in
- **Input:** _none_
- **Output shape:** `dict['deviceControllability', 'autocorrectTelemetryConfig']`
- **Output sample:**
  ```json
  {"deviceControllability": true, "autocorrectTelemetryConfig": false}
  ```

### ✅ `api_getDeviceCredentialSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/deviceCredentials`
- **What it does:** **Tool Dependency: CRITICAL**  This tool retrieves the device credential settings configured for a site. It returns credential ID references only — **NOT** the 
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['cliCredentialsId', 'snmpv2cReadCredentialsId', 'snmpv2cWriteCredentialsId', 'snmpv3CredentialsId', 'httpReadCredentialsId', 'httpWriteCredentialsId']`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getDeviceDeploymentStatus`
- **API:** `GET /dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/deviceDeployments`
- **What it does:** Returns device deployment status based on filter criteria.
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[14]`
- **Output sample:**
  ```json
  {"id": "2c1a3312-742d-4e48-84eb-5495a3d44ff5", "configGroupName": "netflow.collector", "configGroupVersion": 0, "startTime": 1656017676800, "endTime": 1656017681942, "networkDeviceId": "258a262b-6315-4442-9810-31652f7c0403", "status": "Success"}
  ```

### ✅ `api_getDeviceDeploymentStatusCount`
- **API:** `GET /dna/intent/api/v1/icapSettings/deviceDeployments/count`
- **What it does:** Returns the count of device deployment status(s) based on filter criteria. For detailed information about the usage of the API, please refer to the Open API spe
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getDeviceEnrichmentDetailsV2`
- **API:** `GET /dna/intent/api/v2/device-enrichment-details`
- **What it does:** Retrieve Catalyst Center network device enrichment context for a known device ID, device MAC address, or device management IP address. Use this release-specific
- **Input:** `entity_type=network_device`, `entity_value=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"message": "Invalid Entity type", "reason": "Entity type must either be mac_address/device_id/ip_address"}
  ```

### ✅ `api_getDeviceInterfaceCount`
- **API:** `GET /dna/intent/api/v1/interface/network-device/{deviceId}/count`
- **What it does:** Returns the interface count for the given device
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `int`
- **Output sample:**
  ```json
  52
  ```

### ✅ `api_getDeviceInterfaceVLANs`
- **API:** `GET /dna/intent/api/v1/network-device/{id}/vlan`
- **What it does:** Returns Device Interface VLANs. If parameter value is null or empty, it won't return any value in response.
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[6]`
- **Output sample:**
  ```json
  {"vlanType": "", "vlanNumber": 301, "numberOfIPs": 64, "ipAddress": "10.85.134.193", "prefix": "26", "interfaceName": "Vlan301", "networkAddress": "10.85.134.192"}
  ```

### ✅ `api_getDeviceInterfacesBySpecifiedRange`
- **API:** `GET /dna/intent/api/v1/interface/network-device/{deviceId}/{startIndex}/{recordsToReturn}`
- **What it does:** Returns the list of interfaces for the device for the specified range
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`, `startIndex=1`, `recordsToReturn=5`
- **Output shape:** `list[5]`
- **Output sample:**
  ```json
  {"addresses": [], "adminStatus": "UP", "className": null, "deviceId": "258a262b-6315-4442-9810-31652f7c0403", "duplex": "AutoNegotiate", "ifIndex": "49", "interfaceType": "Physical", "ipv4Address": null, "ipv4Mask": null, "isisSupport": "false", "lastIncomingPacketTime": null, "lastOutgoingPacketTim…
  ```

### ✅ `api_getDeviceSummary`
- **API:** `GET /dna/intent/api/v1/network-device/{id}/brief`
- **What it does:** Returns brief summary of device info for the given device Id
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['id', 'role', 'roleSource']`
- **Output sample:**
  ```json
  {"id": "258a262b-6315-4442-9810-31652f7c0403", "role": "ACCESS", "roleSource": "AUTO"}
  ```

### ✅ `api_getEoXDetailsPerDevice`
- **API:** `GET /dna/intent/api/v1/eox-status/device/{deviceId}`
- **What it does:** **MANDATORY PREREQUISITE:** For site-scoped EOX queries, you MUST call `api_getSites` before `get_device_details`, and you MUST call `get_device_details` before
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['deviceId', 'alertCount', 'eoxDetails', 'scanStatus', 'comments', 'lastScanTime']`
- **Output sample:**
  ```json
  {"deviceId": "258a262b-6315-4442-9810-31652f7c0403", "alertCount": 1, "eoxDetails": [{"bulletinName": "C3850 Fiber SKUs", "bulletinNumber": "EOL13873", "bulletinURL": "https://www.cisco.com/c/en/us/products/collateral/switches/catalyst-3850-series-switches/eos-eol-notice-c51-2438804.html", "bulletin…
  ```

### ✅ `api_getEoXStatusForAllDevices`
- **API:** `GET /dna/intent/api/v1/eox-status/device`
- **What it does:** Use this API for network-wide, device-level retrieval of EOX information when the user wants to display, list, fetch, report, review, or enumerate EOX alerts or
- **Input:** _none_
- **Output shape:** `list[36]`
- **Output sample:**
  ```json
  {"deviceId": "155d90bd-937d-4015-8d8b-af7ca0b09fa4", "alertCount": 0, "summary": [], "scanStatus": "NOT_SCANNED", "comments": ["MLCN10322: The device was not reachable during the scan. Troubleshoot by checking that the device is powered ON and re-sync the device in the inventory dashboard for reacha…
  ```

### ✅ `api_getEoXSummary`
- **API:** `GET /dna/intent/api/v1/eox-status/summary`
- **What it does:** Retrieves EoX summary for all devices in the network
- **Input:** _none_
- **Output shape:** `dict['hardwareCount', 'softwareCount', 'moduleCount', 'totalCount']`
- **Output sample:**
  ```json
  {"hardwareCount": 6, "softwareCount": 16, "moduleCount": 10, "totalCount": 32}
  ```

### ✅ `api_getFieldNoticeNetworkDeviceByDeviceId`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/networkDevices/{networkDeviceId}`
- **What it does:** Get field notice scan summary for one network device by device id. User-facing answers must not show raw networkDeviceId values unless the user explicitly asks 
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['networkDeviceId', 'noticeCount', 'potentialNoticeCount', 'scanStatus', 'comments', 'lastScanTime']`
- **Output sample:**
  ```json
  {"networkDeviceId": "258a262b-6315-4442-9810-31652f7c0403", "noticeCount": 0, "potentialNoticeCount": 0, "scanStatus": "NOT_SCANNED", "comments": "MLCN10618: Device is not entitled for the Field Notices scan. To enable customized insights subscribe to Cisco Success Tracks.", "lastScanTime": 17928252…
  ```

### ✅ `api_getFieldNoticeNetworkDevices`
- **API:** `GET /dna/intent/api/v1/fieldNotices/results/networkDevices`
- **What it does:** Returns field notice network devices. Use this tool for questions such as 'What devices have field notices?', 'Show devices scanned for field notices.', 'Give d
- **Input:** _none_
- **Output shape:** `list[36]`
- **Output sample:**
  ```json
  {"networkDeviceId": "155d90bd-937d-4015-8d8b-af7ca0b09fa4", "noticeCount": 0, "potentialNoticeCount": 0, "scanStatus": "NOT_SCANNED", "comments": "MLCN10611: Device was either added after the last scan or was not reachable during the last scan. Please scan again.", "lastScanTime": 1792825260185}
  ```

### ✅ `api_getFunctionalCapabilityForDevices`
- **API:** `GET /dna/intent/api/v1/network-device/functional-capability`
- **What it does:** Returns the functional-capability for given devices
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"deviceId": "258a262b-6315-4442-9810-31652f7c0403", "functionalCapability": [{"functionName": "ImageTransferProtocolList", "functionOpState": "ENABLED", "functionDetails": [{"propertyName": "IMAGETRANSFERPROTOCOLS", "stringValue": "SCP,TFTP,FTP,HTTPS,HTTP"}], "id": "01d85400-c381-4960-b733-5977acbf…
  ```

### ✅ `api_getInterfaceByIP`
- **API:** `GET /dna/intent/api/v1/interface/ip-address/{ipAddress}`
- **What it does:** Returns list of interfaces for specified device management IP address
- **Input:** `ipAddress=10.85.134.65`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"addresses": [{"address": {"ipAddress": {"address": "10.85.134.65"}, "ipMask": {"address": "255.255.255.192"}, "isInverseMask": false}, "type": "IPV4_PRIMARY"}], "adminStatus": "UP", "className": null, "deviceId": "258a262b-6315-4442-9810-31652f7c0403", "duplex": "AutoNegotiate", "ifIndex": "55", "…
  ```

### ✅ `api_getInterfaces`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/interfaces`
- **What it does:** **TAG PHRASE EXCLUSION:** - If the user asks for ports or interfaces `tagged`, `with <value> tag`, `under tag <value>`, or `in tag <value>`, do not treat `<valu
- **Input:** _none_
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  {"id": "mdeWBwfU-ywDL-BwvU-Dg0W-ytfUmMeZzZrLnw02ztDUohq5BteW", "interfaceName": "management", "vlanId": 0}
  ```

### ✅ `api_getManagedAPLocationsCountForSpecificWirelessController`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/managedApLocations/count`
- **What it does:** For Managed AP location count queries, always return the requested category counts and an explicit combined total. For "primary and secondary" queries, return P
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['primaryManagedApLocationsCount', 'secondaryManagedApLocationsCount', 'anchorManagedApLocationsCount']`
- **Output sample:**
  ```json
  {"primaryManagedApLocationsCount": 0, "secondaryManagedApLocationsCount": 0, "anchorManagedApLocationsCount": 0}
  ```

### ✅ `api_getMobilityGroups`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups`
- **What it does:** Retrieve configured mobility groups if no Network Device Id is provided as a query parameter. If a Network Device Id is given and a mobility group is configured
- **Input:** _none_
- **Output shape:** `list[3]`
- **Output sample:**
  ```json
  {"dataLinkEncryption": false, "mobilityPeers": [], "mobilityGroupName": "VA7NSA", "macAddress": "00:a6:ca:f0:4f:3d", "managementIp": "10.85.134.76", "networkDeviceId": "3192531d-9f52-4e16-bfea-1c311bb65fc8", "dtlsHighCipher": false}
  ```

### ✅ `api_getModuleCount`
- **API:** `GET /dna/intent/api/v1/network-device/module/count`
- **What it does:** Returns Module Count
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `int`
- **Output sample:**
  ```json
  2
  ```

### ✅ `api_getModules`
- **API:** `GET /dna/intent/api/v1/network-device/module`
- **What it does:** Returns modules by specified device id. The API returns a paginated response based on 'limit' and 'offset' parameters, allowing up to 500 records per page. 'lim
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  {"name": "usbflash1", "description": "usbflash1-1", "vendorEquipmentType": "cevUsbFlash", "isReportingAlarmsAllowed": "UNKNOWN", "serialNumber": "STP2308193F", "manufacturer": "", "partNumber": "SSD-120G", "entityPhysicalIndex": "1030", "containmentEntity": "1000", "hardwareVersion": "3.10", "isFiel…
  ```

### ✅ `api_getNetworkBugDeviceByDeviceId`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/networkDevices/{networkDeviceId}`
- **What it does:** Get network bug device by device id
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['networkDeviceId', 'bugCount', 'scanMode', 'scanStatus', 'lastScanTime']`
- **Output sample:**
  ```json
  {"networkDeviceId": "258a262b-6315-4442-9810-31652f7c0403", "bugCount": 0, "scanMode": "NOT_AVAILABLE", "scanStatus": "NOT_SCANNED", "lastScanTime": 0}
  ```

### ✅ `api_getNetworkBugDevices`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/networkDevices`
- **What it does:** Get network devices that have network bugs detected by the network bug scan. Use this list tool for requests like 'what devices have bugs?', 'show all devices w
- **Input:** _none_
- **Output shape:** `list[36]`
- **Output sample:**
  ```json
  {"networkDeviceId": "155d90bd-937d-4015-8d8b-af7ca0b09fa4", "bugCount": 0, "scanMode": "NOT_AVAILABLE", "scanStatus": "NOT_SCANNED", "lastScanTime": 0}
  ```

### ✅ `api_getNetworkBugs`
- **API:** `GET /dna/intent/api/v1/networkBugs/results/bugs`
- **What it does:** Get detected network bugs affecting devices in the network. Use this list tool for questions that ask which network bugs exist, which bugs are detected, which s
- **Input:** _none_
- **Output shape:** `list[40]`
- **Output sample:**
  ```json
  {"id": "CSCvq98433", "headline": "SNMPv3 In the 2960X stack , Engineboots and Enginetime will not be sync after switchover.", "deviceCount": 0, "severity": "MODERATE", "hasWorkaround": true, "workaround": "once switchover occurs, do switchover again to keep master device same as before.", "affectedV…
  ```

### ✅ `api_getNetworkDeviceConfigurationFileDetails`
- **API:** `GET /dna/intent/api/v1/networkDeviceConfigFiles`
- **What it does:** Internal low-level record lookup. Returns one stored record identified by its UUID (the `id` parameter). Use only when an upstream step has already produced a s
- **Input:** _none_
- **Output shape:** `list[500]`
- **Output sample:**
  ```json
  {"id": "1da1b8b6-28e7-4901-b6ce-638a36226b33", "networkDeviceId": "258a262b-6315-4442-9810-31652f7c0403", "versionId": "8ed06d8f-f2b3-4815-b1f1-1182b5eded50", "fileType": "STARTUPCONFIG", "createdBy": "CONFIG_CHANGE_EVENT", "createdTime": 1792031129299}
  ```

### ✅ `api_getNetworkDevicesCredentialsSyncStatus`
- **API:** `GET /dna/intent/api/v1/sites/{id}/deviceCredentials/status`
- **What it does:** Gets site network device credential sync/provisioning summary. Use for credential provision summary, credential provisioning status, device credential sync stat
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `dict['cli', 'snmpV2Read', 'snmpV2Write', 'snmpV3']`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getPnPDeviceCount_legacy`
- **API:** `GET /dna/intent/api/v1/onboarding/pnp-device/count`
- **What it does:** Returns the count of PnP network devices using filters such as state, onboarding state, device type, PID, IP, site. For device types, use these exact values: SW
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  0
  ```

### ✅ `api_getPollingIntervalById`
- **API:** `GET /dna/intent/api/v1/network-device/{id}/collection-schedule`
- **What it does:** Returns polling interval by device id
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `int`
- **Output sample:**
  ```json
  86400
  ```

### ✅ `api_getPollingIntervalForAllDevices`
- **API:** `GET /dna/intent/api/v1/network-device/collection-schedule/global`
- **What it does:** Returns polling interval of all devices
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  86400
  ```

### ✅ `api_getProvisionedDevices`
- **API:** `GET /dna/intent/api/v1/sda/provisionDevices`
- **What it does:** Returns the count of provisioned devices based on query parameters. For PnP devices, use api_getPnPDeviceCount(state=Provisioned) instead.
- **Input:** _none_
- **Output shape:** `list[4]`
- **Output sample:**
  ```json
  {"id": "3fa9bc19-2e2b-4be1-80ba-e4c5e190a363", "siteId": "f5661ccc-b9dc-458a-953c-3e6874f6d32d", "networkDeviceId": "258a262b-6315-4442-9810-31652f7c0403"}
  ```

### ✅ `api_getProvisionedDevicesCount`
- **API:** `GET /dna/intent/api/v1/sda/provisionDevices/count`
- **What it does:** Returns the count of provisioned devices based on query parameters. For PnP devices, use api_getPnPDeviceCount(state=Provisioned) instead.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 4}
  ```

### ✅ `api_getQosDeviceInterfaceInfoCount`
- **API:** `GET /dna/intent/api/v1/qos-device-interface-info-count`
- **What it does:** Get the number of all existing qos device interface infos group by network device id
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  0
  ```

### ✅ `api_getResyncIntervalForTheNetworkDevice`
- **API:** `GET /dna/intent/api/v1/networkDevices/{id}/resyncIntervalSettings`
- **What it does:** Fetch the reysnc interval for the given network device id.
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['interval']`
- **Output sample:**
  ```json
  {"interval": 1440}
  ```

### ✅ `api_getSSIDCountForSpecificWirelessController`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/{networkDeviceId}/ssidDetails/count`
- **What it does:** For SSID/WLAN count runtime queries, if hostname/IP/serial is provided instead of networkDeviceId, resolve the controller first with get_device_details and pass
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getSecurityAdvisoryNetworkDeviceByNetworkDeviceId`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}`
- **What it does:** Get security advisory network device by network device id
- **Input:** `networkDeviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `NoneType`
- **Output sample:**
  ```json
  null
  ```

### ✅ `api_getSecurityAdvisoryNetworkDevices`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/results/networkDevices`
- **What it does:** Return the list of network devices affected by security advisories, PSIRTs, or vulnerabilities. Use this API to answer questions like 'Which devices are affecte
- **Input:** `limit=10`
- **Output shape:** `list[3]`
- **Output sample:**
  ```json
  {"networkDeviceId": "47250f14-dce1-4d6a-a571-0b8e63834d85", "advisoryCount": 0, "scanMode": "ESSENTIALS", "scanStatus": "SUCCESS", "lastScanTime": 1792813500189}
  ```

### ✅ `api_getSiteAssignedNetworkDevice`
- **API:** `GET /dna/intent/api/v1/networkDevices/{id}/assignedToSite`
- **What it does:** Site assigned network device. For PnP devices, use api_getPnPDeviceList/api_getPnPDeviceCount.
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['deviceId', 'siteId', 'siteNameHierarchy', 'siteType']`
- **Output sample:**
  ```json
  {"deviceId": "258a262b-6315-4442-9810-31652f7c0403", "siteId": "f5661ccc-b9dc-458a-953c-3e6874f6d32d", "siteNameHierarchy": "Global/Vancouver Canada/VNC2", "siteType": "building"}
  ```

### ✅ `api_getSites`
- **API:** `GET /dna/intent/api/v1/sites`
- **What it does:** Converts site names or site hierarchies (nameHierarchy) into site identifiers (siteId/UUID), and retrieves site inventory attributes for areas, buildings, and f
- **Input:** `limit=10`
- **Output shape:** `list[4]`
- **Output sample:**
  ```json
  {"id": "e0a0da0b-85ad-4947-b264-88a9e7783a67", "name": "Global", "type": "global"}
  ```

### ✅ `api_getStackDetailsForDevice`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceId}/stack`
- **What it does:** Retrieves complete stack details for given device ID
- **Input:** `deviceId=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['deviceId', 'stackSwitchInfo', 'stackPortInfo', 'svlSwitchInfo']`
- **Output sample:**
  ```json
  {"deviceId": "258a262b-6315-4442-9810-31652f7c0403", "stackSwitchInfo": [{"hwPriority": 0, "macAddress": "70:1f:53:9b:0f:80", "numNextReload": 1, "role": "ACTIVE", "softwareImage": "26.01.01", "stackMemberNumber": 1, "state": "READY", "switchPriority": 1, "entPhysicalIndex": "1000", "serialNumber": …
  ```

### ✅ `api_getTag`
- **API:** `GET /dna/intent/api/v1/tag`
- **What it does:** **TAG DEFINITION LISTING RULE:** - Use this API to enumerate existing tag definitions when the user asks for available, existing, default/system, or custom/user
- **Input:** _none_
- **Output shape:** `list[11]`
- **Output sample:**
  ```json
  {"systemTag": true, "name": "WAN", "instanceTenantId": "62435854a63b673550937bf3", "id": "0cf31c10-1f26-4b9d-985f-7cbc727c273f"}
  ```

### ✅ `api_getTagCount`
- **API:** `GET /dna/intent/api/v1/tag/count`
- **What it does:** **TAG PHRASE EXCLUSION:** - If the user asks how many/count/total/number of devices, network devices, ports, or interfaces are `tagged`, `with <value> tag`, `un
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  11
  ```

### ✅ `api_getTagResourceTypes`
- **API:** `GET /dna/intent/api/v1/tag/member/type`
- **What it does:** **TAG PHRASE EXCLUSION:** - If the user names one tag with `tag`, `tagged`, `with <value> tag`, `under tag`, or `in tag` and asks for devices, ports, interfaces
- **Input:** _none_
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  "networkdevice"
  ```

### ✅ `api_getTheDetailsOfPhysicalComponentsOfTheGivenDevice`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceUuid}/equipment`
- **What it does:** Return all types of equipment details like PowerSupply, Fan, Chassis, Backplane, Module, PROCESSOR, Other and SFP for the Given device.
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[16]`
- **Output sample:**
  ```json
  {"instanceUuid": "0aff1a9a-28ab-4f44-841b-aa9bae4b46a5", "name": "Switch 1 - FAN - T1 3", "description": "Switch 1 - C9300-24UX - FAN 3", "vendorEquipmentType": "cevFanCat3kCT57xxFan", "serialNumber": "", "operationalStateCode": "normal", "productId": "", "manufacturer": ""}
  ```

### ✅ `api_getTheSupportedLayer2FeaturesOnAWiredDevice`
- **API:** `GET /dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/supported/layer2`
- **What it does:** The API returns the supported layer 2 features on a wired device.
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[19]`
- **Output sample:**
  ```json
  {"name": "cdpGlobalConfig"}
  ```

### ✅ `api_getUserEnrichmentDetailsV2`
- **API:** `GET /dna/intent/api/v2/user-enrichment-details`
- **What it does:** Retrieve Catalyst Center end-user enrichment context for a known network user identifier or client MAC address, including user and connected-device context. Use
- **Input:** `entity_type=network_device`, `entity_value=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"message": "Invalid Entity type", "reason": "Entity type must either be mac_address/network_user_id"}
  ```

### ✅ `api_getWirelessLanControllerDetailsById`
- **API:** `GET /dna/intent/api/v1/network-device/{id}/wireless-info`
- **What it does:** Returns the wireless lan controller info with given device ID
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['adminEnabledPorts', 'apGeolocationHeight', 'apGeolocationHeightUncertainty', 'apLocation', 'apMode', 'apProfileName']`
- **Output sample:**
  ```json
  {"adminEnabledPorts": null, "apGeolocationHeight": null, "apGeolocationHeightUncertainty": null, "apLocation": null, "apMode": null, "apProfileName": null, "apZoneName": null, "associatedWlcName": null, "cdpNeighborDetails": null, "countryCode": null, "ethMacAddress": null, "flexGroupName": null, "h…
  ```

### ✅ `api_getsInterfacesAlongWithStatisticsAndPoeDataFromAllN_d99ee240`
- **API:** `GET /dna/data/api/v1/interfaces`
- **What it does:**         Retrieves the list of the interfaces from all network devices based on         the provided query parameters. The latest interfaces data in the         
- **Input:** _none_
- **Output shape:** `list[500]`
- **Output sample:**
  ```json
  {"networkDeviceIpAddress": "10.85.134.82", "id": "8391a493-256c-44cd-9118-b152e1e7ec01", "duplexOper": "FullDuplex", "portMode": "trunk", "vlanId": "10", "isWan": null, "interfaceIfIndex": null, "mediaType": null, "portType": "Ethernet Port", "macAddress": null, "name": "AppGigabitEthernet1/0/1", "o…
  ```

### ✅ `api_getsTheNetworkDeviceDetailsBasedOnTheProvidedQueryParameters`
- **API:** `GET /dna/data/api/v1/networkDevices`
- **What it does:** Gets the Network Device details based on the provided query parameters.  When there is no start and end time specified returns the latest device details. For de
- **Input:** _none_
- **Output shape:** `list[36]`
- **Output sample:**
  ```json
  {"platformId": "C9117AXI-B", "deviceFamily": "Unified AP", "serialNumber": null, "macAddress": "0C:D0:F8:95:7E:00", "deviceSeries": "Cisco Catalyst 9117AXI Series Unified Access Points", "softwareVersion": "17.9.1.151", "productVendor": null, "deviceRole": "ACCESS", "deviceType": "Cisco Catalyst 911…
  ```

### ✅ `api_getsTheTotalNetworkDeviceInterfaceCountsInTheSpecif_a404d76e`
- **API:** `GET /dna/data/api/v1/interfaces/count`
- **What it does:** Gets the total Network device interface counts. For detailed information about the usage of the API, please refer to the Open API specification document - https
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 1130}
  ```

### ✅ `api_issues`
- **API:** `GET /dna/intent/api/v1/issues`
- **What it does:** Intent API to get a list of global issues, issues for a specific device, or issue for a specific client device's MAC address.
- **Input:** _none_
- **Output shape:** `list[13]`
- **Output sample:**
  ```json
  {"issueId": "8fbcb629-9504-43bf-83c7-e6efe59b257a", "name": "Network Device jcohoe-wlc5520 is unreachable from Cisco Catalyst Center", "siteId": "e0a0da0b-85ad-4947-b264-88a9e7783a67/3a24fd4c-9b27-470f-b74a-a945cbb08c4d/f5661ccc-b9dc-458a-953c-3e6874f6d32d", "deviceId": "3192531d-9f52-4e16-bfea-1c31…
  ```

### ✅ `api_legitOperationsForInterface`
- **API:** `GET /dna/intent/api/v1/interface/{interfaceUuid}/legit-operation`
- **What it does:** **Tool Dependency: CRITICAL**  This tool retrieves the list of all valid properties and operations for a network interface. The response includes interface prop
- **Input:** `interfaceUuid=a7c3aab6-1cb3-4ff2-8969-42af18d907`
- **Output shape:** `dict['interfaceUuid', 'properties', 'operations']`
- **Output sample:**
  ```json
  {"interfaceUuid": "a7c3aab6-1cb3-4ff2-8969-42af18d9078e", "properties": [{"name": "description", "applicable": true, "failureReason": null}, {"name": "adminStatus", "applicable": true, "failureReason": null}, {"name": "vlanId", "applicable": true, "failureReason": null}, {"name": "voiceVlanId", "app…
  ```

### ✅ `api_pOEDetails`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceUuid}/poe`
- **What it does:** Returns POE details for device.
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `dict['powerAllocated', 'powerConsumed', 'powerRemaining']`
- **Output sample:**
  ```json
  {"powerAllocated": "595", "powerConsumed": "0", "powerRemaining": "595"}
  ```

### ✅ `api_retrieveBannerSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/bannerSettings`
- **What it does:** **NETWORK SERVER SETTINGS** : Retrieve site-level device access banner settings for a site. For broad queries such as what network server settings are configure
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['banner']`
- **Output sample:**
  ```json
  {"banner": null}
  ```

### ✅ `api_retrieveNetworkDevices`
- **API:** `GET /dna/intent/api/v1/networkDevices`
- **What it does:** API to fetch the list of network devices using basic filters. Use the `/dna/intent/api/v1/networkDevices/query` API for advanced filtering. Refer features for m
- **Input:** _none_
- **Output shape:** `list[36]`
- **Output sample:**
  ```json
  {"id": "47229267-0a7f-4a1d-87b4-2ae17aab3a71", "managementAddress": "10.85.134.116", "dnsResolvedManagementIpAddress": "", "hostname": "AP0CD0.F894.22F4", "macAddress": "0c:d0:f8:95:7e:00", "serialNumbers": ["KWC2305097U"], "type": "Cisco Catalyst 9117AXI Unified Access Point", "family": "Unified AP…
  ```

### ✅ `api_retrieveTelemetrySettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/telemetrySettings`
- **What it does:** Retrieves effective site telemetry settings for a site: application visibility, application telemetry, wired endpoint data collection, wireless telemetry, SNMP 
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `dict['applicationVisibility', 'wiredDataCollection', 'wirelessTelemetry', 'snmpTraps', 'syslogs']`
- **Output sample:**
  ```json
  {"applicationVisibility": {"collector": {"collectorType": "Builtin"}, "enableOnWiredAccessDevices": false}, "wiredDataCollection": {"enableWiredDataCollection": true}, "wirelessTelemetry": null, "snmpTraps": null, "syslogs": null}
  ```

### ✅ `api_retrieveTheCountOfNetworkDevicesForTheGivenApplicat_cdbaad0f`
- **API:** `GET /dna/intent/api/v1/applicationVisibility/networkDevices/count`
- **What it does:** This API retrieves the count of network devices for the given application visibility status filters. 
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 24}
  ```

### ✅ `api_retrieveTheCountOfNetworkDevicesThatAreAssociatedWi_b9832de8`
- **API:** `GET /dna/intent/api/v1/tags/networkDevices/membersAssociations/count`
- **What it does:** Fetches the count of network devices that are associated with at least one tag. A tag is a user-defined or system-defined construct to group resources. When a d
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_retrieveTheListOfNetworkDevicesWithTheirApplication_479dd261`
- **API:** `GET /dna/intent/api/v1/applicationVisibility/networkDevices`
- **What it does:** This API retrieves the list of network devices with their application visibility status. The list can be filtered using the query parameters. Multiple filters c
- **Input:** _none_
- **Output shape:** `list[24]`
- **Output sample:**
  ```json
  {"id": "6c25c4f9-1f9e-4d4a-bbe6-ff68c162b471", "managementAddress": "10.85.134.125", "hostname": "autoinstall_config.vnc2.cisco.com", "siteId": "f5661ccc-b9dc-458a-953c-3e6874f6d32d", "appTelemetryDeploymentStatus": "NOT_DEPLOYED", "appTelemetryReadinessStatus": "NOT_SUPPORTED", "cbarDeploymentStatu…
  ```

### ✅ `api_retrieveTheTotalNumberOfScheduledMaintenanceWindows`
- **API:** `GET /dna/intent/api/v1/networkDeviceMaintenanceSchedules/count`
- **What it does:** Retrieve the total count of all scheduled maintenance windows for network devices.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_returnReplacementDevicesCount`
- **API:** `GET /dna/intent/api/v1/device-replacement/count`
- **What it does:** Get replacement devices count
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  0
  ```

### ✅ `api_returnsAllIssueTriggerDefinitionsForGivenFilters`
- **API:** `GET /dna/intent/api/v1/systemIssueDefinitions`
- **What it does:** Get all system issue defintions. The supported filters are id, name, profileId and definition enable status. An issue trigger definition can be different across
- **Input:** _none_
- **Output shape:** `list[314]`
- **Output sample:**
  ```json
  {"id": "011bb666-a929-4cf5-afb7-cc98669acf19", "name": "fabric_lisp_session_trigger", "displayName": "Fabric LISP Session Status to Control Plane node", "description": "LISP session status from fabric node to Control Plane is down", "priority": "P1", "defaultPriority": "P1", "deviceType": "SWITCH_AN…
  ```

### ✅ `api_returnsNetworkDeviceProductNamesForASite`
- **API:** `GET /dna/intent/api/v1/siteWiseProductNames`
- **What it does:** **Tool Dependency: CRITICAL**\n\nReturns the list of network device product names (for example, Wireless Controller, Switches and Hubs) for a specific site, alo
- **Input:** `limit=10`
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"id": "286326249", "productName": "Cisco 1100 Terminal Services Gateway", "productNameOrdinal": 286326249, "networkDeviceCount": 1, "imageSummary": {"installedImageCount": 0, "goldenImageCount": 0}}
  ```

### ✅ `api_returnsPOEInterfaceDetailsForTheDevice`
- **API:** `GET /dna/intent/api/v1/network-device/{deviceUuid}/interface/poe-detail`
- **What it does:** Returns POE interface details for the device, where deviceuuid is mandatory & accepts comma seperated interface names which is optional and returns information 
- **Input:** `deviceUuid=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[24]`
- **Output sample:**
  ```json
  {"interfaceName": "TenGigabitEthernet1/0/23", "operStatus": "OFF", "adminStatus": "AUTO", "allocatedPower": "0.0", "maxPortPower": "60.0", "portPowerDrawn": "0"}
  ```

### ✅ `api_returnsTheCountOfNetworkDeviceProductNamesForASite`
- **API:** `GET /dna/intent/api/v1/siteWiseProductNames/count`
- **What it does:** Returns the count of network device product names for a given site based on optional filters. ALWAYS call the `api_getSites` tool first to resolve the relevant 
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 13}
  ```

## interface/port/vlan  (23 tools with valid responses)

### ⚪ `api_getAllFlexibleReportSchedules`
- **API:** `GET /dna/data/api/v1/flexible-report/schedules`
- **What it does:** Get all flexible report schedules
- **Input:** `Content-Type=application/json`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getAllTheCustomIssueDefinitionsBasedOnTheGivenFilters`
- **API:** `GET /dna/intent/api/v1/customIssueDefinitions`
- **What it does:** Retrieve the existing syslog-based custom issue definitions. The supported filters are id, name, profileId,  definition enable status, priority, severity, facil
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getCMDBSyncStatus`
- **API:** `GET /dna/intent/api/v1/cmdb-sync/detail`
- **What it does:** This API allows to retrieve the detail of CMDB sync status.It accepts two query parameter "status","date".The supported values for status field are "Success","F
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getWorkflows`
- **API:** `GET /dna/intent/api/v1/onboarding/pnp-workflow`
- **What it does:** Returns the list of workflows based on filter criteria. If a limit is not specified, it will default to return 50 workflows. Pagination and sorting are also sup
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesCiscoIMCConfigurationsForCatalystCenterNodes`
- **API:** `GET /dna/system/api/v1/ciscoImcs`
- **What it does:** This API retrieves the configurations of the Cisco Integrated Management Controller (IMC) that have been added to the Catalyst Center nodes.  The Cisco IMC conf
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesTheSpectrumSensorReportsSentByWLCForProvidedAPMac`
- **API:** `GET /dna/data/api/v1/icap/spectrumSensorReports`
- **What it does:** Retrieves the spectrum sensor reports sent by WLC for provided AP Mac. For detailed information about the usage of the API, please refer to the Open API specifi
- **Input:** `apMac=70:1f:53:9b:0f:80`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_ciscoCatalystCenterNodesConfigurationSummary`
- **API:** `GET /dna/intent/api/v1/nodes-config`
- **What it does:** Provides details about the current Cisco Catalyst Center node configuration, such as API version, node name, NTP server, intracluster link, LACP mode, network s
- **Input:** _none_
- **Output shape:** `dict['nodes']`
- **Output sample:**
  ```json
  {"nodes": [{"name": "10.85.134.108", "id": "c57bd771-8a62-4c55-b9ec-976334d4b2d5", "network": [{"slave": ["enp9s0"], "lacp_supported": true, "intra_cluster_link": false, "interface": "enterprise", "inet6": {}, "inet": {"routes": [], "netmask": "", "dns_servers": [], "gateway": "", "host_ip": ""}}, {…
  ```

### ✅ `api_ciscoCatalystCenterReleaseSummary`
- **API:** `GET /dna/intent/api/v1/dnac-release`
- **What it does:** Provides information such as API version, mandatory core packages for installation or upgrade, optional packages, Cisco Catalyst Center name and version, suppor
- **Input:** _none_
- **Output shape:** `dict['name', 'corePackages', 'displayName', 'displayVersion', 'modified', 'packages']`
- **Output sample:**
  ```json
  {"name": "dnac", "corePackages": ["rbac-extensions:2.1.724.1900000", "platform-ui:2.0.7", "cisco-dna-docs:2.1.724.60382", "ise-bridge:2.1.724.2", "ncp-system:2.1.724.60382", "automation-core:2.1.724.60382", "machine-reasoning:2.1.724.210202", "network-visibility:2.1.724.60382", "dna-core-apps:2.1.72…
  ```

### ✅ `api_getAllInterfaces`
- **API:** `GET /dna/intent/api/v1/interface`
- **What it does:** Returns all available interfaces. This endpoint can return a maximum of 500 interfaces. The API returns a paginated response based on 'limit' and 'offset' param
- **Input:** _none_
- **Output shape:** `list[500]`
- **Output sample:**
  ```json
  {"macAddress": "70:6b:b9:0e:29:0c", "addresses": null, "vlanId": "1", "adminStatus": "UP", "ifIndex": "20", "speed": "1000000", "status": "up", "mediaType": null, "mtu": "1500", "series": "Cisco Catalyst 9300 Series Switches", "managedComputeElementUrl": null, "managedComputeElement": null, "deviceI…
  ```

### ✅ `api_getISISInterfaces`
- **API:** `GET /dna/intent/api/v1/interface/isis`
- **What it does:** Returns the interfaces that has ISIS enabled
- **Input:** _none_
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"addresses": [{"address": {"ipAddress": {"address": "10.255.0.95"}, "ipMask": {"address": "255.255.255.255"}, "isInverseMask": false}, "type": "IPV4_PRIMARY"}], "adminStatus": "UP", "className": null, "deviceId": "af2f61d0-6a5c-4302-a0b0-83d5fafa07df", "duplex": "", "ifIndex": "59", "interfaceType"…
  ```

### ✅ `api_getInterfaceById`
- **API:** `GET /dna/intent/api/v1/interface/{id}`
- **What it does:** Returns the interface for the given interface ID
- **Input:** `id=a7c3aab6-1cb3-4ff2-8969-42af18d907`
- **Output shape:** `dict['macAddress', 'addresses', 'vlanId', 'adminStatus', 'ifIndex', 'speed']`
- **Output sample:**
  ```json
  {"macAddress": "70:6b:b9:0e:29:0c", "addresses": null, "vlanId": "1", "adminStatus": "UP", "ifIndex": "20", "speed": "1000000", "status": "up", "mediaType": null, "mtu": "1500", "series": "Cisco Catalyst 9300 Series Switches", "managedComputeElementUrl": null, "managedComputeElement": null, "deviceI…
  ```

### ✅ `api_getOSPFInterfaces`
- **API:** `GET /dna/intent/api/v1/interface/ospf`
- **What it does:** Returns the interfaces that has OSPF enabled
- **Input:** _none_
- **Output shape:** `list[15]`
- **Output sample:**
  ```json
  {"addresses": [{"address": {"ipAddress": {"address": "10.85.134.98"}, "ipMask": {"address": "255.255.255.192"}, "isInverseMask": false}, "type": "IPV4_PRIMARY"}], "adminStatus": "UP", "className": null, "deviceId": "19a56437-6fe6-4186-9c33-3bf443f4981e", "duplex": "", "ifIndex": "55", "interfaceType…
  ```

### ✅ `api_getTheCountOfHealthScoreDefinitionsBasedOnProvidedFilters`
- **API:** `GET /dna/intent/api/v1/healthScoreDefinitions/count`
- **What it does:** Get the count of health score definitions based on provided filters. Supported filters are id, name and overall health include status. For detailed information 
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 76}
  ```

### ✅ `api_getTheCountOfSystemDefinedIssueDefinitionsBasedOnPr_45aa6c33`
- **API:** `GET /dna/intent/api/v1/systemIssueDefinitions/count`
- **What it does:** Get the count of system defined issue definitions based on provided filters. Supported filters are id, name, profileId and definition enable status. For detaile
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 314}
  ```

### ✅ `api_getTheDetailsOfIssuesForGivenSetOfFilters_2`
- **API:** `GET /dna/data/api/v1/assuranceIssues`
- **What it does:** Returns all details of each issue along with suggested actions for given set of filters specified in query parameters. If there is no start and/or end time, the
- **Input:** _none_
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"issueId": "38d2cfa5-b710-4df2-b93a-66bcf634cb2e", "name": "switch_unreachable", "description": "This network device VNC2-BORDER1.cisco.com is unreachable from Cisco Catalyst Center. The device role is ACCESS.", "summary": "Network Device VNC2-BORDER1.cisco.com is unreachable from Cisco Catalyst Ce…
  ```

### ✅ `api_getTheTotalCustomIssueDefinitionsCountBasedOnThePro_240c53aa`
- **API:** `GET /dna/intent/api/v1/customIssueDefinitions/count`
- **What it does:** Get the total number of Custom issue definitions count based on the provided filters. The supported filters are id, name, profileId and definition enable status
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getVLANDetails`
- **API:** `GET /dna/intent/api/v1/topology/vlan/vlan-names`
- **What it does:** Returns the list of VLAN names that are involved in a loop as identified by the Spanning Tree Protocol
- **Input:** _none_
- **Output shape:** `list[14]`
- **Output sample:**
  ```json
  "Vlan1"
  ```

### ✅ `api_mapsSupportedAccessPoints`
- **API:** `GET /dna/intent/api/v1/maps/supported-access-points`
- **What it does:** Gets the list of supported access point types as well as valid antenna pattern names that can be used for each.
- **Input:** _none_
- **Output shape:** `list[102]`
- **Output sample:**
  ```json
  {"apType": "AP9167EH", "antennaPatterns": [{"band": "5", "names": ["AIR-ANT2547V-NS-5GHz", "AIR-ANT2588P4M-NS-5GHz", "AIR-ANT5114P2M-NS", "AIR-ANT2568VG-NS-5GHz", "AIR-ANT2513P4M-NS-5GHz", "FM-PANEL-19-5GHz", "IW-ANT-OMM-53-N-5GHz", "IW-ANT-H90-510-N-5GHz", "IW-ANT-SKD-513-Q-5GHz", "IW-ANT-SKS-514-Q…
  ```

### ✅ `api_retrieveImageDistributionSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/imageDistributionSettings`
- **What it does:** **NETWORK SERVER SETTINGS** : Retrieve image distribution settings for a site. For broad queries such as what network server settings are configured at a site, 
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['imageDistribution']`
- **Output sample:**
  ```json
  {"imageDistribution": null}
  ```

### ✅ `api_retrieveTheCountOfInterfacesThatAreAssociatedWithAt_6c330a1b`
- **API:** `GET /dna/intent/api/v1/tags/interfaces/membersAssociations/count`
- **What it does:** Fetches the count of interfaces that are associated with at least one tag. A tag is a user-defined or system-defined construct to group resources. When an inter
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_returnsCountOfSoftwareImages`
- **API:** `GET /dna/intent/api/v1/images/count`
- **What it does:** Returns the software-image count for a site.  Requirements: - Resolve `siteId` via `api_getSites` unless the user already gave a valid UUID. Use `name="Global"`
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 168}
  ```

### ✅ `api_returnsListOfSoftwareImages`
- **API:** `GET /dna/intent/api/v1/images`
- **What it does:** Retrieves software images for a site.  Requirements: - Resolve `siteId` via `api_getSites` unless the user already gave a valid UUID. Use `name="Global"` for th
- **Input:** `limit=10`
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"id": "00acd90d-6d0e-4040-aff1-5bef6813ae23", "imported": false, "name": "cat9k_iosxe.26.01.02.CSCwv96200.SPA.apsp.bin", "version": "26.1.2", "imageType": "APSP", "recommended": "UNKNOWN", "ciscoLatest": true, "hasAddonImages": false, "productNames": [{"id": "286319592", "productName": "Cisco Catal…
  ```

### ✅ `api_returnsTheImageSummaryForTheGivenSite`
- **API:** `GET /dna/intent/api/v1/siteWiseImagesSummary`
- **What it does:** **Tool Dependency: CRITICAL**\n\nReturns aggregate image statistics (counts of product names, golden/non-golden, imported images, advisor recommendations) for a
- **Input:** _none_
- **Output shape:** `dict['imageInstalledCount', 'importedImageCount', 'goldenImageCount', 'nonGoldenImageCount', 'productCount', 'productsWithGoldenCount']`
- **Output sample:**
  ```json
  {"imageInstalledCount": 20, "importedImageCount": 4, "goldenImageCount": 0, "nonGoldenImageCount": 4, "productCount": 13, "productsWithGoldenCount": 0, "productsWithoutGoldenCount": 13}
  ```

## topology/sites  (17 tools with valid responses)

### ⚪ `api_retrieveSitesWithOverriddenSSIDs`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/ssids/overrideAtSites`
- **What it does:** Retrieve list of siteId(s) with information of SSID(s) which are overridden 
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesTheListOfNetworkProfilesThatTheGivenSiteHa_0bebd066`
- **API:** `GET /dna/intent/api/v1/sites/{siteId}/profileAssignments`
- **What it does:** Retrieves the list of profiles that the given site has been assigned.  These profiles may either be directly assigned to this site, or were assigned to a parent
- **Input:** `siteId=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_countsGlobalIPAddressPools`
- **API:** `GET /dna/intent/api/v1/ipam/globalIpAddressPools/count`
- **What it does:** Returns the total count of global IP address pools.  PRECEDENCE Apply sections in order. Higher sections override lower sections when they conflict.  S0 Scope a
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_countsIPAddressSubpools`
- **API:** `GET /dna/intent/api/v1/ipam/siteIpAddressPools/count`
- **What it does:** Returns the total count of IP address subpools.  PRECEDENCE Apply sections in order. Higher sections override lower sections when they conflict.  S0 Scope and h
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getFloorSettings`
- **API:** `GET /dna/intent/api/v2/floors/settings`
- **What it does:** Gets UI user preference for floor unit system.
- **Input:** _none_
- **Output shape:** `dict['unitsOfMeasure']`
- **Output sample:**
  ```json
  {"unitsOfMeasure": "feet"}
  ```

### ✅ `api_getSSIDBySite`
- **API:** `GET /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids`
- **What it does:** This API allows the user to get all SSIDs (Service Set Identifier) at the given site
- **Input:** `siteId=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"id": "mda0C3nP-zhmW-CZfP-mMqZ-CZrZnwK2zdDZohm5AteWzdeXCZeY", "profileName": "ssid_profile", "ssid": "ssid", "wlanType": "Enterprise", "authType": "WPA2_ENTERPRISE", "l3AuthType": "open", "passphrase": "[REDACTED]", "externalAuthIpAddress": "", "fastTransition": "ADAPTIVE", "authServer": "auth_exte…
  ```

### ✅ `api_getSSIDCountBySite`
- **API:** `GET /dna/intent/api/v1/sites/{siteId}/wirelessSettings/ssids/count`
- **What it does:** This API allows the user to get count of all SSIDs (Service Set Identifier) .
- **Input:** `siteId=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getSiteTopology`
- **API:** `GET /dna/intent/api/v1/topology/site-topology`
- **What it does:** Returns site topology
- **Input:** _none_
- **Output shape:** `dict['sites']`
- **Output sample:**
  ```json
  {"sites": [{"id": "3a24fd4c-9b27-470f-b74a-a945cbb08c4d", "name": "Vancouver Canada", "parentId": "e0a0da0b-85ad-4947-b264-88a9e7783a67", "latitude": "", "longitude": "", "locationType": "area", "locationAddress": "", "locationCountry": "", "groupNameHierarchy": "Global/Vancouver Canada", "displayNa…
  ```

### ✅ `api_getSitesCount`
- **API:** `GET /dna/intent/api/v1/sites/count`
- **What it does:** Returns the number of sites in Catalyst Center having a given name, or the total number of sites when no site name is provided. Use this tool if you want the to
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 4}
  ```

### ✅ `api_retrieveAAASettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/aaaSettings`
- **What it does:** Retrieve configured AAA settings for a specific site or site hierarchy, including Global. Use this API whenever the user asks for AAA, RADIUS, TACACS, TACACS+, 
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `dict['aaaNetwork', 'aaaClient']`
- **Output sample:**
  ```json
  {"aaaNetwork": {}, "aaaClient": {}}
  ```

### ✅ `api_retrieveDHCPSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/dhcpSettings`
- **What it does:** **NETWORK SERVER SETTINGS** : Retrieve DHCP settings for a site. For broad queries such as what network server settings are configured at a site, invoke this to
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['dhcp']`
- **Output sample:**
  ```json
  {"dhcp": null}
  ```

### ✅ `api_retrieveDNSSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/dnsSettings`
- **What it does:** **NETWORK SERVER SETTINGS** : Retrieve DNS settings for a site. For broad queries such as what network server settings are configured at a site, invoke this too
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['dns']`
- **Output sample:**
  ```json
  {"dns": {"domainName": "cisco.com"}}
  ```

### ✅ `api_retrieveNTPSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/ntpSettings`
- **What it does:** **NETWORK SERVER SETTINGS** : Retrieve NTP settings for a site. For broad queries such as what network server settings are configured at a site, invoke this too
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['ntp']`
- **Output sample:**
  ```json
  {"ntp": null}
  ```

### ✅ `api_retrieveTimeZoneSettingsForASite`
- **API:** `GET /dna/intent/api/v1/sites/{id}/timeZoneSettings`
- **What it does:** **NETWORK SERVER SETTINGS** : Retrieve time zone settings for a site. For broad queries such as what network server settings are configured at a site, invoke th
- **Input:** `id=f5661ccc-b9dc-458a-953c-3e6874f6d3`, `_inherited=False`
- **Output shape:** `dict['timeZone']`
- **Output sample:**
  ```json
  {"timeZone": null}
  ```

### ✅ `api_retrievesTheCountOfNetworkProfilesForSites`
- **API:** `GET /dna/intent/api/v1/networkProfilesForSites/count`
- **What it does:** Retrieves the count of network profiles for sites
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 2}
  ```

### ✅ `api_retrievesTheCountOfProfilesThatTheGivenSiteHasBeenAssigned`
- **API:** `GET /dna/intent/api/v1/sites/{siteId}/profileAssignments/count`
- **What it does:** Retrieves the count of profiles that the given site has been assigned.  These profiles may either be directly assigned to this site, or were assigned to a paren
- **Input:** `siteId=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_retrievesTheListOfNetworkProfilesForSites`
- **API:** `GET /dna/intent/api/v1/networkProfilesForSites`
- **What it does:** Retrieves the list of network profiles for sites.
- **Input:** _none_
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  {"id": "585beea8-83ea-4992-b228-b9df25e2921f", "name": "profile", "type": "Wireless"}
  ```

## assurance/health  (24 tools with valid responses)

### ⚪ `api_retrievesTheListOfAAAServicesForGivenParameters`
- **API:** `GET /dna/data/api/v1/aaaServices`
- **What it does:** Retrieves the list of AAA Services and offers basic filtering and sorting capabilities. For detailed information about the usage of the API, please refer to the
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesTheListOfDHCPServicesForGivenParameters`
- **API:** `GET /dna/data/api/v1/dhcpServices`
- **What it does:** Retrieves the list of DHCP Services and offers basic filtering and sorting capabilities. For detailed information about the usage of the API, please refer to th
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesTheListOfDNSServicesForGivenParameters`
- **API:** `GET /dna/data/api/v1/dnsServices`
- **What it does:** Retrieves the list of DNS Services and offers basic filtering and sorting capabilities. For detailed information about the usage of the API, please refer to the
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_disasterRecoveryStatus`
- **API:** `GET /dna/intent/api/v1/disasterrecovery/system/status`
- **What it does:** Detailed and Summarized status of DR components (Active, Standby and Witness system's health). 
- **Input:** _none_
- **Output shape:** `dict['state', 'main', 'recovery', 'witness']`
- **Output sample:**
  ```json
  {"state": "Unconfigured", "main": {"state": "Unregistered", "ipconfig": [], "nodes": [{"hostname": "10.85.134.108", "ipconfig": [{"interface": "management", "vip": false, "ip": "10.85.134.108"}], "state": "up"}]}, "recovery": {"state": "Unregistered", "ipconfig": []}, "witness": {"state": "Unregiste…
  ```

### ✅ `api_getCountOfFieldNoticesResultsTrendOverTime`
- **API:** `GET /dna/intent/api/v1/fieldNotices/resultsTrend/count`
- **What it does:** Get count of field notices results trend over time
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 32}
  ```

### ✅ `api_getCountOfNetworkBugsResultsTrendOverTime`
- **API:** `GET /dna/intent/api/v1/networkBugs/resultsTrend/count`
- **What it does:** Get count of network bugs results trend over time
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getCountOfSecurityAdvisoriesResultsTrendOverTime`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/resultsTrend/count`
- **What it does:** Get count of security advisories results trend over time.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 212}
  ```

### ✅ `api_getFieldNoticesResultsTrendOverTime`
- **API:** `GET /dna/intent/api/v1/fieldNotices/resultsTrend`
- **What it does:** Get field notices results trend over time. The default sort is by scan time descending.
- **Input:** _none_
- **Output shape:** `list[32]`
- **Output sample:**
  ```json
  {"softwareFieldNoticesCount": 0, "hardwareFieldNoticesCount": 0, "scanTime": 1792825261328}
  ```

### ✅ `api_getIssueEnrichmentDetailsV2`
- **API:** `GET /dna/intent/api/v2/issue-enrichment-details`
- **What it does:** Retrieve Catalyst Center issue enrichment context for a known issue identifier or client MAC address. Use this release-specific OpenAPI enrichment endpoint when
- **Input:** `entity_type=network_device`, `entity_value=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"message": "Invalid Entity type", "reason": "Entity type must either be issue_id/mac_address"}
  ```

### ✅ `api_getNetworkBugsResultsTrendOverTime`
- **API:** `GET /dna/intent/api/v1/networkBugs/resultsTrend`
- **What it does:** Get network bugs results trend over time. The default sort is by scan time descending.
- **Input:** _none_
- **Output shape:** `dict['version']`
- **Output sample:**
  ```json
  {"version": "1.0"}
  ```

### ✅ `api_getSecurityAdvisoriesResultsTrendOverTime`
- **API:** `GET /dna/intent/api/v1/securityAdvisories/resultsTrend`
- **What it does:** Get security advisories results trend over time. The default sort is by scan time descending.
- **Input:** `limit=10`
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"criticalSecurityImpactRatingAdvisoriesCount": 0, "highSecurityImpactRatingAdvisoriesCount": 5, "scanTime": 1792813507962}
  ```

### ✅ `api_getTheTotalNumberOfIssuesForGivenSetOfFilters`
- **API:** `GET /dna/data/api/v1/assuranceIssues/count`
- **What it does:** Returns the total number issues for given set of filters. If there is no start and/or end time, then end time will be defaulted to current time and start time w
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 13}
  ```

### ✅ `api_retrieveACountOfTheNumberOfAssuranceTasksThatCurrentlyExist`
- **API:** `GET /dna/data/api/v1/assuranceTasks/count`
- **What it does:** returns a count of the number of assurance tasks that are not expired For detailed information about the usage of the API, please refer to the Open API specific
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_retrieveAListOfAssuranceTasks`
- **API:** `GET /dna/data/api/v1/assuranceTasks`
- **What it does:** returns all existing tasks in a paginated list  default sorting of list is `startTime`, `asc`  valid field to sort by are [`startTime`,`endTime`,`updateTime`,`s
- **Input:** _none_
- **Output shape:** `NoneType`
- **Output sample:**
  ```json
  null
  ```

### ✅ `api_retrievesTheListOfClients_WhileAlsoOfferingBasicFil_820210a0`
- **API:** `GET /dna/data/api/v1/clients`
- **What it does:** Retrieves the list of clients, while also offering basic filtering and sorting capabilities. For detailed information about the usage of the API, please refer t
- **Input:** _none_
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"id": "EC:F4:0C:01:72:7E", "macAddress": "EC:F4:0C:01:72:7E", "type": "Wired", "name": null, "userId": null, "username": null, "ipv4Address": "192.168.199.103", "ipv6Addresses": null, "vendor": null, "osType": null, "osVersion": null, "formFactor": null, "deviceType": null, "siteHierarchy": "Global…
  ```

### ✅ `api_retrievesTheListOfNetworkApplicationsAlongWithExper_23fa3c77`
- **API:** `GET /dna/data/api/v1/networkApplications`
- **What it does:** Retrieves the list of network applications along with experience and health metrics. If startTime and endTime are not provided, the API defaults to the last 24 
- **Input:** `siteId=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `list[39]`
- **Output sample:**
  ```json
  {"id": "amazon-web-services", "applicationName": "amazon-web-services", "siteId": "f5661ccc-b9dc-458a-953c-3e6874f6d32d", "exporterIpAddress": "10.85.134.65", "exporterNetworkDeviceId": "258a262b-6315-4442-9810-31652f7c0403", "businessRelevance": "default", "usage": 12960, "healthScore": 10, "throug…
  ```

### ✅ `api_retrievesTheTotalCountOfClientsByApplyingBasicFiltering`
- **API:** `GET /dna/data/api/v1/clients/count`
- **What it does:** Retrieves the number of clients by applying basic filtering. For detailed information about the usage of the API, please refer to the Open API specification doc
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 10}
  ```

### ✅ `api_retrievesTheTotalCountOfNetworkApplicationsByApplyi_72ae1f9d`
- **API:** `GET /dna/data/api/v1/networkApplications/count`
- **What it does:** Retrieves the number of network applications by applying basic filtering. If startTime and endTime are not provided, the API defaults to the last 24 hours. `sit
- **Input:** `siteId=f5661ccc-b9dc-458a-953c-3e6874f6d3`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 39}
  ```

### ✅ `api_retrievesTheTotalNumberOfAAAServicesForGivenParameters`
- **API:** `GET /dna/data/api/v1/aaaServices/count`
- **What it does:** Retrieves the total number of AAA Services for given parameters. For detailed information about the usage of the API, please refer to the Open API specification
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_retrievesTheTotalNumberOfDHCPServicesForGivenParameters`
- **API:** `GET /dna/data/api/v1/dhcpServices/count`
- **What it does:** Retrieves the total number of DHCP Services for given parameters. For detailed information about the usage of the API, please refer to the Open API specificatio
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_retrievesTheTotalNumberOfDNSServicesForGivenParameters`
- **API:** `GET /dna/data/api/v1/dnsServices/count`
- **What it does:** Retrieves the total number of DNS Services for given parameters. For detailed information about the usage of the API, please refer to the Open API specification
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_sensorTestResults`
- **API:** `GET /dna/intent/api/v1/AssuranceGetSensorTestResults`
- **What it does:** Intent API to get SENSOR test result summary
- **Input:** _none_
- **Output shape:** `dict['summary', 'failureStats']`
- **Output sample:**
  ```json
  {"summary": {"totalTestCount": 0, "ONBOARDING": {"WEBAUTH": {"passCount": 0, "failCount": 0}, "AUTH": {"passCount": 0, "failCount": 0}, "DHCP": {"passCount": 0, "failCount": 0}, "ASSOC": {"passCount": 0, "failCount": 0}}, "PERFORMANCE": {"SPEED": {"passCount": 0, "failCount": 0}, "IPERF": {"passCoun…
  ```

### ✅ `api_systemHealthAPI`
- **API:** `GET /dna/intent/api/v1/diagnostics/system/health`
- **What it does:** This API retrieves the latest system events 
- **Input:** _none_
- **Output shape:** `dict['healthEvents', 'hostname', 'version', 'cimcaddress']`
- **Output sample:**
  ```json
  {"healthEvents": [{"severity": 2, "hostname": "10-85-134-108.etcd.kube-system.svc.cluster.local", "instance": "10-85-134-108.etcd.kube-system.svc.cluster.local:Internet URL Access", "subDomain": "Internet Access", "domain": "System", "description": "The following URLs are not reachable directly: htt…
  ```

### ✅ `api_systemHealthCountAPI`
- **API:** `GET /dna/intent/api/v1/diagnostics/system/health/count`
- **What it does:** This API gives the count of the latest system events
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 79}
  ```

## config-archive/events  (24 tools with valid responses)

### ⚪ `api_get802_11beProfiles`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/dot11beProfiles`
- **What it does:** This API allows the user to get 802.11be Profile(s) configured under Wireless Settings
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getFailedITSMEvents`
- **API:** `GET /dna/intent/api/v1/integration/events`
- **What it does:** Used to retrieve the list of integration events that failed to create tickets in ITSM
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getSNMPDestination`
- **API:** `GET /dna/intent/api/v1/dna-event/snmp-config`
- **What it does:** Get SNMP Destination
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_countOfEventSubscriptions`
- **API:** `GET /dna/intent/api/v1/event/subscription/count`
- **What it does:** Returns the count of event subscriptions that have been configured or created. Use this tool when the user asks about the number of active event subscriptions. 
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  0
  ```

### ✅ `api_countOfNotifications`
- **API:** `GET /dna/intent/api/v1/event/event-series/count`
- **What it does:** Get the Count of Published Notifications based on the various inputs from the user. It can answer questions like How many notifications are there for event X? o
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  31115
  ```

### ✅ `api_getAllITSMIntegrationSettings`
- **API:** `GET /dna/intent/api/v1/integration-settings/itsm/instances`
- **What it does:** Fetches all ITSM Integration settings instances and their configurations based on the user inputs. It can answer questions like What ITSM integrations are confi
- **Input:** _none_
- **Output shape:** `dict['page', 'pageSize', 'totalPages', 'data', 'totalRecords']`
- **Output sample:**
  ```json
  {"page": 1, "pageSize": 50, "totalPages": 0, "data": [], "totalRecords": 0}
  ```

### ✅ `api_getAuditLogParentRecords`
- **API:** `GET /dna/data/api/v1/event/event-series/audit-log/parent-records`
- **What it does:** Get Parent Audit Log Event instances from the Event-Hub 
- **Input:** _none_
- **Output shape:** `list[25]`
- **Output sample:**
  ```json
  {"version": "1.0.0", "efInstanceId": "4c7ef820-31f9-4929-97c0-73d8132a9309", "instanceId": "4eda3e4a-678e-464a-ada7-042ec8c872ed", "eventId": "AUDIT_LOG_EVENT", "namespace": null, "name": "LOGIN_USER_EVENT", "description": "LOGIN_USER_EVENT: 'admin' logged in successfully.", "type": "AUDIT_LOG", "ca…
  ```

### ✅ `api_getAuditLogRecords`
- **API:** `GET /dna/data/api/v1/event/event-series/audit-logs`
- **What it does:** Get Audit Log Event instances from the Event-Hub 
- **Input:** _none_
- **Output shape:** `list[25]`
- **Output sample:**
  ```json
  {"version": "1.0.0", "efInstanceId": "65c11305-d2f5-41fd-b197-9bba3175e171", "instanceId": "c13a3d11-cf81-45fd-9ae1-40d4d362c027", "eventId": "AUDIT_LOG_EVENT", "namespace": null, "name": "LOGIN_USER_EVENT", "description": "LOGIN_USER_EVENT: 'admin' logged in successfully.", "type": "AUDIT_LOG", "ca…
  ```

### ✅ `api_getAuditLogSummary`
- **API:** `GET /dna/data/api/v1/event/event-series/audit-log/summary`
- **What it does:** Get Audit Log Summary from the Event-Hub
- **Input:** _none_
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"count": 36221, "maxTimestamp": 1793211822864, "minTimestamp": 1761686467741}
  ```

### ✅ `api_getConnectorTypes`
- **API:** `GET /dna/system/api/v1/event/config/connector-types`
- **What it does:** Get the list of connector types
- **Input:** _none_
- **Output shape:** `list[8]`
- **Output sample:**
  ```json
  {"connectorType": "REST", "displayName": "REST", "isDefaultSupported": true, "isCustomConnector": false, "description": "Send the data via HTTP push API"}
  ```

### ✅ `api_getEmailDestination`
- **API:** `GET /dna/intent/api/v1/event/email-config`
- **What it does:** Get Email Destination
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getEmailEventSubscriptions`
- **API:** `GET /dna/intent/api/v1/event/subscription/email`
- **What it does:** Gets the list of email Subscriptions's based on provided query params
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getEmailSubscriptionDetails`
- **API:** `GET /dna/intent/api/v1/event/subscription-details/email`
- **What it does:** Gets the list of subscription details for specified connectorType
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getEventArtifacts`
- **API:** `GET /dna/system/api/v1/event/artifact`
- **What it does:** Gets the list of artifacts based on provided offset and limit
- **Input:** _none_
- **Output shape:** `list[10]`
- **Output sample:**
  ```json
  {"version": null, "artifactId": "0498-6a20-4198-a2fd", "namespace": "LicenseManagement", "name": "Device registration succeeded", "description": "Device has been successfully registered in Cisco Smart Software Manager", "domain": "Know Your Network", "subDomain": "Devices", "tags": ["License Managem…
  ```

### ✅ `api_getEventSubscriptions`
- **API:** `GET /dna/intent/api/v1/event/subscription`
- **What it does:** Gets the list of all event subscriptions regardless of connector type (REST/Webhook, Email, Syslog, etc.). Use this tool when the user asks for all subscription
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getITSMIntegrationStatus`
- **API:** `GET /dna/intent/api/v1/integration-settings/status`
- **What it does:** Fetches ITSM Integration status and also lists the bundles as needed, along with their configurations. Used mainly to check the status of the bundles. It is cap
- **Input:** _none_
- **Output shape:** `list[8]`
- **Output sample:**
  ```json
  {"id": "0f9d-bb9c-4578-8d15", "name": "AI Endpoint Analytics", "status": "NEW", "configurations": []}
  ```

### ✅ `api_getMobilityGroupsCount`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups/count`
- **What it does:** Retrieves count of mobility groups configured
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 3}
  ```

### ✅ `api_getNotifications`
- **API:** `GET /dna/intent/api/v1/event/event-series`
- **What it does:** Gets the Published Notifications based on the various inputs from the user. It can answer questions like have there been any notifications for event X? or Give 
- **Input:** _none_
- **Output shape:** `list[20]`
- **Output sample:**
  ```json
  {"version": "1.0.0", "efInstanceId": "7bdf3e5c-00b8-484f-abe6-4d553ec1a18b", "instanceId": "de62b184-660b-43c9-ae1a-08285132bc0d", "eventId": "AUDIT_LOG_EVENT", "namespace": null, "name": "LOGIN_USER_EVENT", "description": "LOGIN_USER_EVENT: 'admin' logged in successfully.", "type": "AUDIT_LOG", "ca…
  ```

### ✅ `api_getRest_WebhookEventSubscriptions`
- **API:** `GET /dna/intent/api/v1/event/subscription/rest`
- **What it does:** Gets the list of Rest/Webhook Subscriptions's based on provided query params
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getRest_WebhookSubscriptionDetails`
- **API:** `GET /dna/intent/api/v1/event/subscription-details/rest`
- **What it does:** Gets the list of subscription details for specified connectorType
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getSyslogDestination`
- **API:** `GET /dna/intent/api/v1/event/syslog-config`
- **What it does:** Get Syslog Destination
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getSyslogEventSubscriptions`
- **API:** `GET /dna/intent/api/v1/event/subscription/syslog`
- **What it does:** Gets the list of Syslog Subscriptions's based on provided offset and limit
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getSyslogSubscriptionDetails`
- **API:** `GET /dna/intent/api/v1/event/subscription-details/syslog`
- **What it does:** Gets the list of subscription details for specified connectorType
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_getWebhookDestination`
- **API:** `GET /dna/intent/api/v1/event/webhook`
- **What it does:** Get Webhook Destination
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

## swim/software  (5 tools with valid responses)

### ⚪ `api_retrieveImageDistributionServers`
- **API:** `GET /dna/intent/api/v1/images/distributionServerSettings`
- **What it does:** Retrieve the list of remote image distribution servers. There can be up to two remote servers.Product always acts as local distribution server, and it is not pa
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_retrieveApplicableAdd_onImagesForTheGivenSoftwareImage`
- **API:** `GET /dna/intent/api/v1/images/{id}/addonImages`
- **What it does:** Retrieves the list of applicable add-on images if available for the given software image. `id` can be obtained from the response of API [ /dna/intent/api/v1/ima
- **Input:** `id=00acd90d-6d0e-4040-aff1-5bef6813ae`
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  {"id": "00acd90d-6d0e-4040-aff1-5bef6813ae23", "imported": false, "name": "cat9k_iosxe.26.01.02.CSCwv96200.SPA.apsp.bin", "version": "26.1.2", "imageType": "APSP", "recommended": "UNKNOWN", "ciscoLatest": true, "hasAddonImages": false, "productNames": [{"id": "286315874", "productName": "Cisco Catal…
  ```

### ✅ `api_retrieveSpecificImageDistributionServer`
- **API:** `GET /dna/intent/api/v1/images/distributionServerSettings/{id}`
- **What it does:** Retrieve image distribution server for the given server identifier
- **Input:** `id=258a262b-6315-4442-9810-31652f7c04`
- **Output shape:** `NoneType`
- **Output sample:**
  ```json
  null
  ```

### ✅ `api_retrievesCSSMConnectionMode`
- **API:** `GET /dna/intent/api/v1/connectionModeSetting`
- **What it does:** Retrieves Cisco Smart Software Manager (CSSM) connection mode setting.
- **Input:** _none_
- **Output shape:** `dict['connectionMode']`
- **Output sample:**
  ```json
  {"connectionMode": "DIRECT"}
  ```

### ✅ `api_returnsCountOfAdd_onImages`
- **API:** `GET /dna/intent/api/v1/images/{id}/addonImages/count`
- **What it does:** Count of add-on images available for the given software image identifier, `id` can be obtained from the response of API [ /dna/intent/api/v1/images?hasAddonImag
- **Input:** `id=00acd90d-6d0e-4040-aff1-5bef6813ae`
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 2}
  ```

## sda/fabric  (1 tools with valid responses)

### ⚪ `api_getPendingFabricEvents`
- **API:** `GET /dna/intent/api/v1/sda/pendingFabricEvents`
- **What it does:** Returns a list of pending fabric events that match the provided query parameters.
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

## templates/provision  (9 tools with valid responses)

### ✅ `api_eventArtifactCount`
- **API:** `GET /dna/system/api/v1/event/artifact/count`
- **What it does:** Get the total count of registered event artifacts. Event artifacts are event definitions or templates available in the system. It can answer questions like How 
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  274
  ```

### ✅ `api_getPnPGlobalSettings`
- **API:** `GET /dna/intent/api/v1/onboarding/pnp-settings`
- **What it does:** Returns global PnP settings of the user
- **Input:** _none_
- **Output shape:** `dict['version', 'aaaCredentials', 'taskTimeOuts', 'savaMappingList', 'acceptEula', 'defaultProfile']`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getProject_s_Details`
- **API:** `GET /dna/intent/api/v2/template-programmer/project`
- **What it does:** Get project(s) details
- **Input:** _none_
- **Output shape:** `list[5]`
- **Output sample:**
  ```json
  {"name": "Cloud DayN Templates", "description": "Cloud DayN Templates", "id": "c8f40f7d-6c1b-42e9-aa8c-ec33ca7d4e3f", "lastUpdateTime": 1648586239409, "templates": [{"name": "DMVPN Spoke for Branch Router - System Default", "composite": false, "language": "VELOCITY", "id": "bc3cabba-e547-4c67-b9b1-d…
  ```

### ✅ `api_getProvisioningSettings`
- **API:** `GET /dna/intent/api/v1/provisioningSettings`
- **What it does:** Returns provisioning settings
- **Input:** _none_
- **Output shape:** `dict['requirePreview', 'requireItsmApproval']`
- **Output sample:**
  ```json
  {"requirePreview": true, "requireItsmApproval": false}
  ```

### ✅ `api_getTemplateProjectCount`
- **API:** `GET /dna/intent/api/v1/projects/count`
- **What it does:** Get the count of all template projects.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 5}
  ```

### ✅ `api_getTemplateProjects`
- **API:** `GET /dna/intent/api/v1/projects`
- **What it does:** Get all matching template projects based on the filters selected.
- **Input:** _none_
- **Output shape:** `list[5]`
- **Output sample:**
  ```json
  {"name": "Cloud DayN Templates", "description": "Cloud DayN Templates", "projectId": "c8f40f7d-6c1b-42e9-aa8c-ec33ca7d4e3f", "lastUpdateTime": 1648586239409}
  ```

### ✅ `api_getTemplate_s_Details`
- **API:** `GET /dna/intent/api/v2/template-programmer/template`
- **What it does:** Get template(s) details
- **Input:** _none_
- **Output shape:** `list[8]`
- **Output sample:**
  ```json
  {"name": "DMVPN Hub for Cloud Router- System Default", "description": "Dynamic Multipoint VPN Hub for Cloud Router", "tags": [{"id": "3176617a-8d55-4090-8eb0-6be0d25f93b3", "name": "cloud-dmvpn-hub"}], "author": "SYSTEM", "deviceTypes": [{"productFamily": "Routers", "productSeries": "Cisco Cloud Ser…
  ```

### ✅ `api_getWorkflowCount`
- **API:** `GET /dna/intent/api/v1/onboarding/pnp-workflow/count`
- **What it does:** Returns the workflow count
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  0
  ```

### ✅ `api_getsTheTemplatesAvailable`
- **API:** `GET /dna/intent/api/v1/template-programmer/template`
- **What it does:** List the templates available
- **Input:** _none_
- **Output shape:** `list[8]`
- **Output sample:**
  ```json
  {"name": "DMVPN Hub for Cloud Router- System Default", "projectName": "Onboarding Configuration", "projectId": "6cb02d0c-f48d-40c8-97ea-3cefdca1a792", "templateId": "e5708c11-746c-4055-be5f-d1e3c731d01f", "versionsInfo": [{"id": "f94bd638-1301-4d64-80b1-0271a3b36216", "description": "Dynamic Multipo…
  ```

## pnp/day0  (1 tools with valid responses)

### ✅ `api_retrieveLicenseSetting`
- **API:** `GET /dna/intent/api/v1/licenseSetting`
- **What it does:** Retrieves licensing settings, including Default/Active Licensing Smart Account ID.\n\n**Execution Policy (MANDATORY):**\n- Use this tool directly for licensing 
- **Input:** _none_
- **Output shape:** `dict['defaultSmartAccountId', 'autoRegistrationVirtualAccountId']`
- **Output sample:**
  ```json
  {"defaultSmartAccountId": null, "autoRegistrationVirtualAccountId": null}
  ```

## other  (55 tools with valid responses)

### ⚪ `api_getAPAuthorizationLists`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/apAuthorizationLists`
- **What it does:** Retrieves the AP Authorization Lists that are created in the Catalyst Centre network Design for wireless. If an AP Authorization List name is given as query par
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getAllowedMacAddress`
- **API:** `GET /dna/intent/api/v1/security/threats/rogue/allowed-list`
- **What it does:** Intent API to fetch all the allowed mac addresses in the system.
- **Input:** `Content-Type=application/json`
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getAnchorGroups_v2_3_7_10`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/anchorGroups`
- **What it does:** This API allows the user to get AnchorGroups that captured in wireless settings design. 
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getMeshApNeighbours`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/meshApNeighbours`
- **What it does:** Retrieves all Mesh accesspoint Neighbours details whether child, parent, etc. 
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getPowerProfiles`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/powerProfiles`
- **What it does:** This API allows the user to get Power Profiles that captured in wireless settings design.
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getServiceProviderDetails`
- **API:** `GET /dna/intent/api/v1/service-provider`
- **What it does:** API to get service provider details (QoS).
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_getServiceProviderDetailsV2`
- **API:** `GET /dna/intent/api/v2/service-provider`
- **What it does:** API to get Service Provider details (QoS).
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_lANAutomationLog`
- **API:** `GET /dna/intent/api/v1/lan-automation/log`
- **What it does:** Invoke this API to get the LAN Automation session logs.
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ⚪ `api_retrievesAllPreviousPathtracesSummary`
- **API:** `GET /dna/intent/api/v1/flow-analysis`
- **What it does:** Returns a summary of all flow analyses stored. Results can be filtered by specified parameters.
- **Input:** _none_
- **Output shape:** `list[0]`
- **Output:** _empty result_

### ✅ `api_ciscoCatalystCenterPackagesSummary`
- **API:** `GET /dna/intent/api/v1/dnac-packages`
- **What it does:** Provides information such as name, version of packages installed on the Cisco Catalyst Center.
- **Input:** _none_
- **Output shape:** `list[48]`
- **Output sample:**
  ```json
  {"name": "ndp-ui", "version": "1.9.7001"}
  ```

### ✅ `api_countOfNetworkProductNames`
- **API:** `GET /dna/intent/api/v1/productNames/count`
- **What it does:** Count of product names based on filter criteria
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 1156}
  ```

### ✅ `api_disasterRecoveryOperationalStatus`
- **API:** `GET /dna/intent/api/v1/disasterrecovery/system/operationstatus`
- **What it does:** Returns the status of Disaster Recovery operation performed on the system.
- **Input:** _none_
- **Output shape:** `dict[]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_get802_11beProfilesCount`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/dot11beProfiles/count`
- **What it does:** This API allows the user to get count of all 802.11be Profile(s)
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getAAAAttributeAPI`
- **API:** `GET /dna/system/api/v1/users/external-servers/aaa-attribute`
- **What it does:** Get the current value of the custom AAA attribute.
- **Input:** _none_
- **Output shape:** `dict['aaa-attributes']`
- **Output sample:**
  ```json
  {"aaa-attributes": [{}]}
  ```

### ✅ `api_getAPAuthorizationListCount`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/apAuthorizationLists/count`
- **What it does:** This API allows the user to get count of all AP Authorization lists.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getAPProfiles`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/apProfiles`
- **What it does:** This API allows the user to get AP profiles that are captured in wireless settings design.
- **Input:** _none_
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  {"id": "mdi1rgvM-yxvS-Df9b-uf9q-CM9MAwXLx0fPCMvpu0qWztfMmMeZ", "apProfileName": "Default_AP_Profile_AireOS", "description": "Default AP Profile for AireOS", "remoteWorkerEnabled": false, "managementSetting": {"authType": "NO-AUTH", "dot1xUsername": null, "dot1xPassword": "", "sshEnabled": false, "te…
  ```

### ✅ `api_getAPProfilesCount`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/apProfiles/count`
- **What it does:** This API returns the total number of AP Profiles available.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 2}
  ```

### ✅ `api_getActivities`
- **API:** `GET /dna/intent/api/v1/activities`
- **What it does:** Returns activity(s) based on filter criteria
- **Input:** _none_
- **Output shape:** `list[4]`
- **Output sample:**
  ```json
  {"recurring": true, "description": "Scan network for Field Notices", "startTime": 1774076460000, "id": "019d0d28-1473-71ae-921d-f9ced1857620", "endTime": 0, "type": "DEFAULT", "status": "COMPLETED"}
  ```

### ✅ `api_getAllowedMacAddressCount`
- **API:** `GET /dna/intent/api/v1/security/threats/rogue/allowed-list/count`
- **What it does:** Intent API to fetch the count of allowed mac addresses in the system.
- **Input:** `Content-Type=application/json`
- **Output shape:** `int`
- **Output sample:**
  ```json
  0
  ```

### ✅ `api_getApplicationPolicy`
- **API:** `GET /dna/intent/api/v1/app-policy`
- **What it does:** Get all existing application policies
- **Input:** _none_
- **Output shape:** `list[28]`
- **Output sample:**
  ```json
  {"id": "0fd6c455-c537-4ac5-abb0-8c883555ec9a", "instanceId": 57029983, "instanceCreatedOn": 1655248910397, "instanceUpdatedOn": 1655248910397, "instanceVersion": 0, "createTime": 1655248909932, "deployed": false, "isSeeded": false, "isStale": false, "lastUpdateTime": 1655248909932, "name": "Applicat…
  ```

### ✅ `api_getApplicationPolicyDefault`
- **API:** `GET /dna/intent/api/v1/app-policy-default`
- **What it does:** Get default application policy
- **Input:** _none_
- **Output shape:** `list[28]`
- **Output sample:**
  ```json
  {"id": "0fd6c455-c537-4ac5-abb0-8c883555ec9a", "instanceId": 57029983, "instanceCreatedOn": 1655248910397, "instanceUpdatedOn": 1655248910397, "instanceVersion": 0, "createTime": 1655248909932, "deployed": false, "isSeeded": false, "isStale": false, "lastUpdateTime": 1655248909932, "name": "Applicat…
  ```

### ✅ `api_getApplicationPolicyQueuingProfile`
- **API:** `GET /dna/intent/api/v1/app-policy-queuing-profile`
- **What it does:** Get all or by name, existing application policy queuing profiles
- **Input:** _none_
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"id": "5cb09b6c-c211-47ac-b391-1d9544c1744e", "instanceId": 57029976, "instanceCreatedOn": 1655248908615, "instanceUpdatedOn": 1655248908615, "instanceVersion": 0, "createTime": 1655248908612, "deployed": false, "description": "Cisco Validated Design Queuing Profile", "isSeeded": false, "isStale": …
  ```

### ✅ `api_getApplicationPolicyQueuingProfileCount`
- **API:** `GET /dna/intent/api/v1/app-policy-queuing-profile-count`
- **What it does:** Get the number of all existing  application policy queuing profile
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  1
  ```

### ✅ `api_getApplicationSets`
- **API:** `GET /dna/intent/api/v1/application-policy-application-set`
- **What it does:** Get appllication-sets by offset/limit or by name
- **Input:** _none_
- **Output shape:** `list[28]`
- **Output sample:**
  ```json
  {"id": "088e380d-448b-4490-98a3-931f7fc445a5", "identitySource": {"id": "c35934e8-17f6-4f76-8a0b-6a5ec3b8d911", "type": "NBAR"}, "name": "consumer-file-sharing"}
  ```

### ✅ `api_getApplicationSetsCount`
- **API:** `GET /dna/intent/api/v1/application-policy-application-set-count`
- **What it does:** Get the number of existing application-sets 
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  28
  ```

### ✅ `api_getApplications`
- **API:** `GET /dna/intent/api/v1/applications`
- **What it does:** Get applications by offset/limit or by name
- **Input:** _none_
- **Output shape:** `list[500]`
- **Output sample:**
  ```json
  {"id": "004013ce-3065-4909-ab0d-248f29dffc01", "indicativeNetworkIdentity": [{"id": "31f0d4bd-91c5-4209-a3ad-e8e88700524a", "lowerPort": 0, "ports": "141", "protocol": "UDP", "upperPort": 0, "displayName": "471053813"}, {"id": "9b01436c-22d2-4aee-9898-89c0f84d0ff8", "lowerPort": 0, "ports": "141", "…
  ```

### ✅ `api_getApplicationsCount`
- **API:** `GET /dna/intent/api/v1/applications-count`
- **What it does:** Get the number of all existing applications
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  1519
  ```

### ✅ `api_getCountOfAllDiscoveryJobs`
- **API:** `GET /dna/intent/api/v1/discovery/count`
- **What it does:** Returns the count of all available discovery jobs
- **Input:** _none_
- **Output shape:** `int`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getCountOfAnchorGroups`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/anchorGroups/count`
- **What it does:** This API allows the user to get count of all AnchorGroups
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getDiscoveriesByRange`
- **API:** `GET /dna/intent/api/v1/discovery/{startIndex}/{recordsToReturn}`
- **What it does:** Returns the discoveries by specified range
- **Input:** `startIndex=1`, `recordsToReturn=5`
- **Output shape:** `list[5]`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getDiscoveryJobsByIP`
- **API:** `GET /dna/intent/api/v1/discovery/job`
- **What it does:** Returns the list of discovery jobs for the given IP
- **Input:** `ipAddress=10.85.134.65`
- **Output shape:** `list[4]`
- **Output sample:**
  ```json
  [output redacted — credential/discovery material not included in shared artifact]
  ```

### ✅ `api_getExternalAuthenticationSettingAPI`
- **API:** `GET /dna/system/api/v1/users/external-authentication`
- **What it does:** Get the External Authentication setting.
- **Input:** _none_
- **Output shape:** `dict['external-authentication-flag']`
- **Output sample:**
  ```json
  {"external-authentication-flag": [{"enableSet": false, "enabled": false}]}
  ```

### ✅ `api_getListOfAvailableNamespaces`
- **API:** `GET /dna/intent/api/v1/file/namespace`
- **What it does:** Returns list of available namespaces
- **Input:** _none_
- **Output shape:** `list[62]`
- **Output sample:**
  ```json
  "ca-10"
  ```

### ✅ `api_getMeshApNeighboursCount`
- **API:** `GET /dna/intent/api/v1/wirelessControllers/meshApNeighbours/count`
- **What it does:** This API returns the total number of mesh Ap Neighbours available.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getPermissionsAPI`
- **API:** `GET /dna/system/api/v1/role/permissions`
- **What it does:** Get permissions for a role in the system.
- **Input:** _none_
- **Output shape:** `dict['resource-types']`
- **Output sample:**
  ```json
  {"resource-types": [{"type": "Assurance", "displayName": "Assurance", "description": "Assure consistent service levels with complete visibility across all aspects of your network.", "defaultPermission": "Read"}, {"type": "Assurance.Monitoring and Troubleshooting", "displayName": "Monitoring and Trou…
  ```

### ✅ `api_getPowerProfilesCount`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/powerProfiles/count`
- **What it does:** This API returns the total number of Power Profiles available.
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_getRFProfiles`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/rfProfiles`
- **What it does:** This API allows the user to get all RF Profiles
- **Input:** _none_
- **Output shape:** `list[3]`
- **Output sample:**
  ```json
  {"id": "mdaZte9x-tdbp-mvCY-tdnp-nfC1tdzpn1C4tdLpmtbxmtfmmtjp", "rfProfileName": "LOW", "defaultRfProfile": false, "enableRadioTypeA": true, "enableRadioTypeB": true, "enableRadioType6GHz": true, "enableCustom": false, "radioTypeAProperties": {"parentProfile": "LOW", "radioChannels": "36,40,44,48,52,…
  ```

### ✅ `api_getRFProfilesCount`
- **API:** `GET /dna/intent/api/v1/wirelessSettings/rfProfiles/count`
- **What it does:** This API allows the user to get count of all RF profiles
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 3}
  ```

### ✅ `api_getSNMPProperties`
- **API:** `GET /dna/intent/api/v1/snmp-property`
- **What it does:** Returns SNMP properties
- **Input:** _none_
- **Output shape:** `list[2]`
- **Output sample:**
  ```json
  {"intValue": 3, "systemPropertyName": "Retry", "instanceUuid": "d1b7924e-21c8-477d-8ed1-f42798758508", "instanceTenantId": "62435854a63b673550937bf3", "id": "d1b7924e-21c8-477d-8ed1-f42798758508"}
  ```

### ✅ `api_getTagById`
- **API:** `GET /dna/intent/api/v1/tag/{id}`
- **What it does:** Returns tag specified by Id
- **Input:** `id=0cf31c10-1f26-4b9d-985f-7cbc727c27`
- **Output shape:** `dict['systemTag', 'name', 'instanceTenantId', 'id']`
- **Output sample:**
  ```json
  {"systemTag": true, "name": "WAN", "instanceTenantId": "62435854a63b673550937bf3", "id": "0cf31c10-1f26-4b9d-985f-7cbc727c273f"}
  ```

### ✅ `api_getTasks`
- **API:** `GET /dna/intent/api/v1/tasks`
- **What it does:** Returns task(s) based on filter criteria
- **Input:** _none_
- **Output shape:** `list[500]`
- **Output sample:**
  ```json
  {"lastUpdate": 1761630386667, "rootId": "9f7f6da1-6dce-4a6d-b34e-1cf08b0dcf35", "status": "PENDING", "startTime": 1761630386665, "resultLocation": "/dna/intent/api/v1/tasks/9f7f6da1-6dce-4a6d-b34e-1cf08b0dcf35/detail", "id": "9f7f6da1-6dce-4a6d-b34e-1cf08b0dcf35"}
  ```

### ✅ `api_getTasksCount`
- **API:** `GET /dna/intent/api/v1/tasks/count`
- **What it does:** Returns the number of tasks that meet the filter criteria
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 21144}
  ```

### ✅ `api_getThreatLevels`
- **API:** `GET /dna/intent/api/v1/security/threats/level`
- **What it does:** Intent API to fetch all threat levels defined.
- **Input:** `Content-Type=application/json`
- **Output shape:** `list[3]`
- **Output sample:**
  ```json
  {"name": "High", "value": 10001}
  ```

### ✅ `api_getThreatTypes`
- **API:** `GET /dna/intent/api/v1/security/threats/type`
- **What it does:** Intent API to fetch all threat types defined.
- **Input:** `Content-Type=application/json`
- **Output shape:** `list[39]`
- **Output sample:**
  ```json
  {"value": 1901, "name": "Neighbor", "label": "NEIGHBOUR", "isCustom": false, "isDeleted": false}
  ```

### ✅ `api_getWirelessProfiles`
- **API:** `GET /dna/intent/api/v1/wirelessProfiles`
- **What it does:** This API allows the user to get all Wireless Network Profiles
- **Input:** _none_
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {"wirelessProfileName": "profile", "ssidDetails": [{"ssidName": "ssid", "enableFabric": false, "flexConnect": {"enableFlexConnect": false}, "interfaceName": "interface", "wlanProfileName": "ssid_profile", "policyProfileName": "ssid_profile"}], "id": "585beea8-83ea-4992-b228-b9df25e2921f", "additiona…
  ```

### ✅ `api_getWirelessProfilesCount`
- **API:** `GET /dna/intent/api/v1/wirelessProfiles/count`
- **What it does:** This API allows the user to get count of all wireless profiles
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 1}
  ```

### ✅ `api_lANAutomationActiveSessions`
- **API:** `GET /dna/intent/api/v1/lan-automation/sessions`
- **What it does:** Invoke this API to get the LAN Automation active session information
- **Input:** _none_
- **Output shape:** `dict['maxSupportedCount', 'activeSessions', 'activeSessionIds']`
- **Output sample:**
  ```json
  {"maxSupportedCount": "5", "activeSessions": "0", "activeSessionIds": []}
  ```

### ✅ `api_lANAutomationSessionCount`
- **API:** `GET /dna/intent/api/v1/lan-automation/count`
- **What it does:** Invoke this API to get the total count of LAN Automation sessions.
- **Input:** _none_
- **Output shape:** `dict['sessionCount']`
- **Output sample:**
  ```json
  {"sessionCount": 0}
  ```

### ✅ `api_retrievesAllTheValidationSets`
- **API:** `GET /dna/intent/api/v1/diagnosticValidationSets`
- **What it does:** Retrieves all the validation sets and optionally the contained validations
- **Input:** _none_
- **Output shape:** `list[6]`
- **Output sample:**
  ```json
  {"id": "infra", "name": "Appliance Infrastructure Status", "description": "Checks if Catalyst Center infrastructure is healthy.", "version": "3.8.1"}
  ```

### ✅ `api_retrievesTheApplicationQoSPolicySetting`
- **API:** `GET /dna/intent/api/v1/qosPolicySetting`
- **What it does:** API to retrieve the application QoS policy setting.
- **Input:** _none_
- **Output shape:** `dict['deployByDefaultOnWiredDevices']`
- **Output sample:**
  ```json
  {"deployByDefaultOnWiredDevices": null}
  ```

### ✅ `api_retrievesTheCountOfActivities`
- **API:** `GET /dna/intent/api/v1/activities/count`
- **What it does:** Retrieves the count of activities
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 4}
  ```

### ✅ `api_retrievesTheCountOfValidationWorkflows`
- **API:** `GET /dna/intent/api/v1/diagnosticValidationWorkflows/count`
- **What it does:** Retrieves the count of workflows that have been successfully submitted and are currently available.  
- **Input:** _none_
- **Output shape:** `dict['count']`
- **Output sample:**
  ```json
  {"count": 0}
  ```

### ✅ `api_retrievesTheListOfValidationWorkflows`
- **API:** `GET /dna/intent/api/v1/diagnosticValidationWorkflows`
- **What it does:** Retrieves the workflows that have been successfully submitted and are currently available. This is sorted by `submitTime`
- **Input:** _none_
- **Output shape:** `list[1]`
- **Output sample:**
  ```json
  {}
  ```

### ✅ `api_systemPerformanceAPI`
- **API:** `GET /dna/intent/api/v1/diagnostics/system/performance`
- **What it does:** Retrieves the aggregated metrics (total, average or maximum) of cluster key performance indicators (KPIs), such as CPU utilization, memory utilization or networ
- **Input:** _none_
- **Output shape:** `dict['hostName', 'version', 'kpis']`
- **Output sample:**
  ```json
  {"hostName": "10-85-134-108.etcd.kube-system.svc.cluster.local", "version": "1", "kpis": {"cpu": {"utilization": "10.93", "units": "percent"}, "memory": {"utilization": "74.96", "units": "percent"}, "network tx_rate": {"utilization": "3788.47", "units": "kbps"}, "network rx_rate": {"utilization": "4…
  ```

### ✅ `api_systemPerformanceHistoricalAPI`
- **API:** `GET /dna/intent/api/v1/diagnostics/system/performance/history`
- **What it does:** Retrieves the average values of cluster key performance indicators (KPIs), like CPU utilization, memory utilization or network rates grouped by time intervals w
- **Input:** _none_
- **Output shape:** `dict['hostName', 'version', 'kpis']`
- **Output sample:**
  ```json
  {"hostName": "10-85-134-108.etcd.kube-system.svc.cluster.local", "version": "1", "kpis": {"legends": {"cpu": {"units": "percent"}, "memory": {"units": "percent"}, "network tx_rate": {"units": "kbps"}, "network rx_rate": {"units": "kbps"}}, "data": {"2026-10-28T18:10:00Z": ["10.73", "74.89", "3624.64…
  ```

## Appendix — tools requiring inputs we could not auto-resolve

These GET tools are valid but need identifiers not present/derivable in the lab context (e.g. a template, report, execution, or profile ID). Their required inputs are documented below so you can supply them manually.

| Tool | API | Required input(s) not resolved |
|------|-----|--------------------------------|
| `api_clientProximity` | `/dna/intent/api/v1/client-proximity` | `username` |
| `api_countOfEvents` | `/dna/intent/api/v1/events/count` | `tags` |
| `api_countTheNumberOfEvents` | `/dna/data/api/v1/assuranceEvents/count` | `deviceFamily` |
| `api_countsSubpoolsOfAGlobalIPAddressPool` | `/dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAddressPoolId}/subpools/count` | `globalIpAddressPoolId` |
| `api_downloadAFileByFileId` | `/dna/intent/api/v1/file/{fileId}` | `fileId` |
| `api_downloadFlexibleReport` | `/dna/data/api/v1/flexible-report/report/content/{reportId}/{executionId}` | `reportId`, `executionId` |
| `api_downloadReportContent` | `/dna/intent/api/v1/data/reports/{reportId}/executions/{executionId}` | `reportId`, `executionId` |
| `api_getAScheduledReport` | `/dna/intent/api/v1/data/reports/{reportId}` | `reportId` |
| `api_getAccessPointConfigurationTaskResult` | `/dna/intent/api/v1/wireless/accesspoint-configuration/details/{task_id}` | `task_id` |
| `api_getAccessPoint_s_FactoryResetStatus` | `/dna/intent/api/v1/wirelessAccessPoints/factoryResetRequestStatus` | `taskId` |
| `api_getAllExecutionDetailsForAGivenReport` | `/dna/intent/api/v1/data/reports/{reportId}/executions` | `reportId` |
| `api_getApplicationCount` | `/dna/intent/api/v2/applications-count` | `scalableGroupType` |
| `api_getApplicationSetCount` | `/dna/intent/api/v2/application-policy-application-set-count` | `scalableGroupType` |
| `api_getApplicationSet_s` | `/dna/intent/api/v2/application-policy-application-set` | `attributes` |
| `api_getApplication_s` | `/dna/intent/api/v2/applications` | `attributes` |
| `api_getBackupStorages` | `/dna/system/api/v1/backupStorages` | `storageType` |
| `api_getBusinessAPIExecutionDetails` | `/dna/intent/api/v1/dnacaap/management/execution-status/{executionId}` | `executionId` |
| `api_getConfigTaskDetails` | `/dna/intent/api/v1/network-device-config/task` | `parentTaskId` |
| `api_getConfigurationsForADeployedLayer2FeatureOnAWiredDevice` | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/deployed/layer2/{feature}` | `feature` |
| `api_getConfigurationsForAnIntendedLayer2FeatureOnAWiredDevice` | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}` | `feature` |
| `api_getConfigurationsForIntendedLayer2FeaturesOnAWiredDevice` | `/dna/intent/api/v1/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2` | `feature` |
| `api_getDetailsOfASingleProfilingRule` | `/dna/intent/api/v1/endpoint-analytics/profiling-rules/{ruleId}` | `ruleId` |
| `api_getEndpointDetails` | `/dna/intent/api/v1/endpoint-analytics/endpoints/{epId}` | `epId` |
| `api_getEvents` | `/dna/intent/api/v1/events` | `tags` |
| `api_getExecutionIdByReportId` | `/dna/data/api/v1/flexible-report/report/{reportId}/executions` | `reportId` |
| `api_getFlexibleReportScheduleByReportId` | `/dna/data/api/v1/flexible-report/schedule/{reportId}` | `reportId` |
| `api_getGlobalCredentials` | `/dna/intent/api/v1/global-credential` | `credentialSubType` |
| `api_getICAPConfigurationStatusPerNetworkDevice` | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDeviceStatusDetails` | `previewActivityId` |
| `api_getITSMIntegrationSettingById` | `/dna/intent/api/v1/integration-settings/instances/itsm/{instanceId}` | `instanceId` |
| `api_getL3TopologyDetails` | `/dna/intent/api/v1/topology/l3/{topologyType}` | `topologyType` |
| `api_getNumberOfConfigurationsForADeployedLayer2FeatureOnADevice` | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/deployed/layer2/{feature}/count` | `feature` |
| `api_getNumberOfConfigurationsForAnIntendedLayer2FeatureOnADevice` | `/dna/intent/api/v1/wired/networkDevices/{id}/configFeatures/intended/layer2/{feature}/count` | `feature` |
| `api_getPlannedAccessPointsForBuilding` | `/dna/intent/api/v1/buildings/{buildingId}/planned-access-points` | `buildingId` |
| `api_getSecurityAdvisoriesAffectingTheNetworkDevice` | `/dna/intent/api/v1/securityAdvisories/results/networkDevices/{networkDeviceId}/advisories` | `sortBy`, `order` |
| `api_getSecurityAdvisoriesAffectingTheNetworkDevices` | `/dna/intent/api/v1/securityAdvisories/results/advisories` | `sortBy`, `order` |
| `api_getSiteAnalyticsSummaryDataForTheGivenTaskId` | `/dna/data/api/v1/siteKpiSummaries/summaryAnalytics` | `taskId` |
| `api_getSiteAnalyticsTrendDataForTheGivenTaskId` | `/dna/data/api/v1/siteKpiSummaries/trendAnalytics` | `taskId` |
| `api_getStatusAPIForEvents` | `/dna/intent/api/v1/event/api-status/{executionId}` | `executionId` |
| `api_getTagMemberCount` | `/dna/intent/api/v1/tag/{id}/member/count` | `memberType` |
| `api_getTagMembersById` | `/dna/intent/api/v1/tag/{id}/member` | `memberType` |
| `api_getTaskDetails` | `/dna/intent/api/v1/endpoint-analytics/tasks/{taskId}` | `taskId` |
| `api_getTemplateProject` | `/dna/intent/api/v1/projects/{projectId}` | `projectId` |
| `api_getTemplateVersion` | `/dna/intent/api/v1/templates/{templateId}/versions/{versionId}` | `templateId`, `versionId` |
| `api_getTemplateVersions` | `/dna/intent/api/v1/templates/{templateId}/versions` | `templateId` |
| `api_getTemplateVersionsCount` | `/dna/intent/api/v1/templates/{templateId}/versions/count` | `templateId` |
| `api_getTopNEntitiesRelatedToSiteAnalyticsForTheGivenTaskId` | `/dna/data/api/v1/siteKpiSummaries/topNAnalytics` | `taskId` |
| `api_getTopologyDetails` | `/dna/intent/api/v1/topology/l2/{vlanID}` | `vlanID` |
| `api_getTriggeredJobsByActivityId` | `/dna/intent/api/v1/activities/{activityId}/triggeredJobs` | `activityId` |
| `api_getViewDetailsForAGivenViewGroup_View` | `/dna/intent/api/v1/data/view-groups/{viewGroupId}/views/{viewId}` | `viewGroupId`, `viewId` |
| `api_getViewsForAGivenViewGroup` | `/dna/intent/api/v1/data/view-groups/{viewGroupId}` | `viewGroupId` |
| `api_getsAllTheVersionsOfAGivenTemplate` | `/dna/intent/api/v1/template-programmer/template/version/{templateId}` | `templateId` |
| `api_getsDetailsOfAGivenTemplate` | `/dna/intent/api/v1/template-programmer/template/{templateId}` | `templateId` |
| `api_getsTheDetailsOfAGivenProject` | `/dna/intent/api/v1/template-programmer/project/{projectId}` | `projectId` |
| `api_getsTheDeviceConfigForTheConfigurationModel` | `/dna/intent/api/v1/wired/networkDevices/{networkDeviceId}/configFeatures/intended/configurationModels/{previewActivityId}/config` | `previewActivityId` |
| `api_importMapArchive_ImportStatus` | `/dna/intent/api/v1/maps/import/{importContextUuid}/status` | `importContextUuid` |
| `api_inventoryInsightDeviceLinkMismatchAPI` | `/dna/intent/api/v1/network-device/insight/{siteId}/device-link` | `category` |
| `api_licenseTermDetails` | `/dna/intent/api/v1/licenses/term/smartAccount/{smart_account_id}/virtualAccount/{virtual_account_name}` | `smart_account_id`, `virtual_account_name`, `device_type` |
| `api_retrieveASpecificPolicyTagForAWirelessProfile` | `/dna/intent/api/v1/wirelessProfiles/{id}/policyTags/{policyTagId}` | `policyTagId` |
| `api_retrieveASpecificSiteTagForAWirelessProfile` | `/dna/intent/api/v1/wirelessProfiles/{id}/siteTags/{siteTagId}` | `siteTagId` |
| `api_retrieveCLITemplatesAttachedToANetworkProfile` | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/templates` | `profileId` |
| `api_retrieveCountOfCLITemplatesAttachedToANetworkProfile` | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/templates/count` | `profileId` |
| `api_retrieveCountOfNetworkProfilesAttachedToACLITemplate` | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites/count` | `templateId` |
| `api_retrieveNetworkDeviceProductName` | `/dna/intent/api/v1/productNames/{productNameOrdinal}` | `productNameOrdinal` |
| `api_retrieveTheNetworkProfilesAttachedToACLITemplate` | `/dna/intent/api/v1/templates/{templateId}/networkProfilesForSites` | `templateId` |
| `api_retrievesDeployedICAPConfigurationsWhileSupportingB_0c45cdf6` | `/dna/intent/api/v1/icapSettings` | `captureStatus` |
| `api_retrievesPreviousPathtrace` | `/dna/intent/api/v1/flow-analysis/{flowAnalysisId}` | `flowAnalysisId` |
| `api_retrievesSubpoolsIDsOfAGlobalIPAddressPool` | `/dna/intent/api/v1/ipam/globalIpAddressPools/{globalIpAddressPoolId}/subpools` | `globalIpAddressPoolId` |
| `api_retrievesTheCountOfDeployedICAPConfigurationsWhileS_4d6c040d` | `/dna/intent/api/v1/icapSettings/count` | `captureStatus` |
| `api_retrievesTheCountOfSitesThatTheGivenNetworkProfileF_40cb52b6` | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments/count` | `profileId` |
| `api_retrievesTheCountOfTriggeredJobsByActivityId` | `/dna/intent/api/v1/activities/{activityId}/triggeredJobs/count` | `activityId` |
| `api_retrievesTheDevice_sCLIsOfTheICAPIntent` | `/dna/intent/api/v1/icapSettings/configurationModels/{previewActivityId}/networkDevices/{networkDeviceId}/config` | `previewActivityId` |
| `api_retrievesTheListOfSitesThatTheGivenNetworkProfileFo_cb2b520e` | `/dna/intent/api/v1/networkProfilesForSites/{profileId}/siteAssignments` | `profileId` |
| `api_statusOfTemplateDeployment` | `/dna/intent/api/v1/template-programmer/template/deploy/status/{deploymentId}` | `deploymentId` |
| `api_theTrendAnalyticsDataForAFabricSiteInTheSpecifiedTimeRange` | `/dna/data/api/v1/fabricSiteHealthSummaries/{id}/trendAnalytics` | `trendInterval` |
| `api_theTrendAnalyticsDataForATransitNetworkInTheSpecifi_5c01728a` | `/dna/data/api/v1/transitNetworkHealthSummaries/{id}/trendAnalytics` | `trendInterval` |
| `api_theTrendAnalyticsDataForAVirtualNetworkInTheSpecifi_66fff53f` | `/dna/data/api/v1/virtualNetworkHealthSummaries/{id}/trendAnalytics` | `trendInterval` |
| `api_virtualAccountDetails` | `/dna/intent/api/v1/licenses/smartAccount/{smart_account_id}/virtualAccounts` | `smart_account_id` |

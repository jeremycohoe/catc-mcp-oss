# Catalyst Center switching prompt test results

Share-ready example report captured 2026-10-29 18:07 UTC. This is the report-capture time; each source timestamp is shown when the API returned one. Hostnames (including DNS-style names) and the reported neighbor name are consistently replaced with model-family aliases; see the inventory table for the aliases. Management IPs, site names, UUIDs, and non-secret technical details remain from the live capture. Credentials, SNMP community values, passwords, keys, and secret-bearing configuration lines are not included. The remediation write tool was never called.

**Controller/tool set:** Catalyst Center 2.3.7.11; catc-mcp-oss 2.3.7.11.

**Selected test values:** switch `switch-c9300-04` (`10.85.134.65`), site `Global/Vancouver Canada/VNC2`, tag `WAN`.
**Reported test behavior:** read-only observations are recorded for 26 examples,
including the remediation approval checkpoint. Exact-prompt transcripts and full
tool traces are not bundled; this report does not establish end-to-end acceptance
of every prompt or requested output format. Empty results and data-quality limits
are reported without interpreting them as proof of absent risk or unconfigured features.

## Run manifest and acceptance status

| Item | Recorded value or limitation |
|---|---|
| Capture time | 2026-10-29 18:07 UTC; not a source timestamp |
| Controller/tool release | 2.3.7.11, as reported by the original capture |
| Server source commit | Not recorded in this report; the documentation commit is not a substitute |
| Client, agent, and transport | Not recorded |
| Exact prompt transcripts | Not bundled |
| Tool calls and arguments | Summarized per example; complete call sequence and retry/page traces not bundled |
| Sanitized structured responses | Not bundled with this report; the older GET harvest is separate evidence |
| Saved pre-change snapshot | No separate snapshot path or artifact is recorded |
| Write execution | Reported as not performed; example 8A covers review/approval only |

**Acceptance:** all 26 examples have narrative observations, but exact-prompt and
complete-output acceptance remains **unverified**. For example, 2A/2B summarize
counts rather than showing the requested port-level tables, 6B summarizes site
counts rather than listing matched switches, and 15A does not identify a persisted
structured snapshot. A successful tool call, a correct aggregate, and a passed
operator workflow are different claims.

For a future acceptance run, record the exact prompt, client/agent and server
commit, UTC start/end times, tool names and sanitized arguments, every page/retry,
response status and source timestamps, and a relative path to sanitized structured
evidence. Mark each example **PASS**, **PARTIAL**, **FAIL**, or **BLOCKED** against
its requested output and safety conditions. Do not reconstruct missing logs or
retroactively label the current summaries PASS. Review responses for secrets
before saving them.

## 1A. Build a complete switch inventory

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** family `Switches and Hubs`; limit 500; offset 1; device details retrieved for all returned switches.

**Result:** 18 switches returned; all 18 device-detail lookups succeeded. Reachability: Unreachable=12, Ping Reachable=3, Reachable=3. Inventory status counts: SYNC_INTERNAL_ERROR=15, MANAGED=3.

| Hostname | Management IP | Model | Software | Role | Reachability | Inventory status | Uptime |
|---|---|---|---|---|---|---|---|
| switch-cmicr-01 | 10.85.134.125 | CMICR-4PC | 15.2(7)E3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 103d 20h |
| switch-c9300-01 | 10.85.134.85 | C9300-48U | 17.6.3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 19d 16h |
| switch-c9200l-01 | 10.85.134.81 | C9200L-24P-4G | 17.6.3 | CORE | Unreachable | SYNC_INTERNAL_ERROR | 242d 9h |
| switch-c9300-02 | 10.85.134.86 | C9300-48U | 17.6.3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 227d 3h |
| switch-c9300-03 | 10.85.134.82 | C9300-48U | 17.6.3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 227d 3h |
| switch-c9200l-02 | 10.85.134.72 | C9200L-24P-4G | 17.9.4a | ACCESS | Ping Reachable | SYNC_INTERNAL_ERROR | 0d 15h |
| switch-c9300-04 | 10.85.134.65 | C9300-24UX | 26.01.1 | ACCESS | Reachable | MANAGED | 90d 22h |
| switch-c9500-01 | 10.85.134.95 | C9500-32QC | 26.01.1 | CORE | Reachable | MANAGED | 90d 17h |
| switch-c9600-01 | 10.85.134.75 | C9606R | 17.18.2 | CORE | Ping Reachable | SYNC_INTERNAL_ERROR | 1d 13h |
| switch-cat9kv-01 | 10.85.134.67 | Cisco Catalyst 9000 Series Virtual Switches | 17.17.1 | CORE | Unreachable | SYNC_INTERNAL_ERROR | 5d 21h |
| switch-c9300-05 | 10.85.134.70 | C9300-24UX | 17.18.20250127:091530 | ACCESS | Ping Reachable | SYNC_INTERNAL_ERROR | 5d 11h |
| switch-c9300-06 | 10.85.134.92 | C9300-24UX | 17.8.1 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 243d 6h |
| switch-c9300-07 | 10.85.134.94 | C9300-24UX | 17.8.1 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 243d 6h |
| switch-c9300-08 | 10.85.134.99 | C9300-24P | 26.01.20251022:045326 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 7d 12h |
| switch-c9300-09 | 10.85.134.98 | C9300-24P | 17.15.3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 7d 14h |
| switch-c9300-10 | 10.85.134.97 | C9300-24P | 17.15.3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 7d 12h |
| switch-c9300-11 | 10.85.134.96 | C9300-24P | 17.15.3 | ACCESS | Unreachable | SYNC_INTERNAL_ERROR | 6d 15h |
| switch-c9500-02 | 10.85.134.84 | C9500-24Q | 17.15.5 | DISTRIBUTION | Reachable | MANAGED | 93d 17h |

## 1B. Inspect stack and hardware

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`, UUID `258a262b-6315-4442-9810-31652f7c0403`.

**Result:** one ACTIVE/READY stack member (`C9300-24UX`, serial `FCW2134L0VB`); two stack-port records, both DOWN with no cable; one chassis record; 0 line-card records. The response supports reporting a single stack member and returned hardware details.

## 1C. Review upcoming lifecycle milestones

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** all 18 switches; one EoX call per device.

**Result:** NOT_SCANNED=15, SUCCESS=3; 20 EoX details returned. Notably, details were present on some records whose `scanStatus` was `NOT_SCANNED`; those are reported as returned data, not as a confirmed current scan. No EoX call failed.

**Date grouping (reference date 2026-10-29):** in the three SUCCESS responses, returned past milestones include EOL13873 `endOfSaleDate=2022-04-30`, EOL15621 `endOfSaleDate=2026-04-30`, and EOL15039 `endOfSaleDate=2024-04-30`; no returned `endOfLifeDate` had passed. No milestone date in those SUCCESS records fell within the next 180 days. The nearest listed support date was 2027-04-30, just beyond that window. Other past end-of-life dates appeared in NOT_SCANNED responses, so they remain unverified controller records and are not treated as confirmed current lifecycle findings.

| Hostname | Scan status | Alert count | Detail records | API scan timestamp |
|---|---|---:|---:|---|
| switch-cmicr-01 | NOT_SCANNED | 0 | 0 | 2026-10-24T05:16:00.228Z |
| switch-c9300-01 | NOT_SCANNED | 2 | 2 | 2026-10-24T05:16:00.228Z |
| switch-c9200l-01 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9300-02 | NOT_SCANNED | 2 | 2 | 2026-10-24T05:16:00.228Z |
| switch-c9300-03 | NOT_SCANNED | 2 | 2 | 2026-10-24T05:16:00.228Z |
| switch-c9300-04 | SUCCESS | 1 | 1 | 2026-10-24T05:16:00.278Z |
| switch-c9200l-02 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9500-01 | SUCCESS | 0 | 0 | 2026-10-24T05:16:00.278Z |
| switch-c9600-01 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-cat9kv-01 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9300-05 | NOT_SCANNED | 0 | 0 | 2026-10-24T05:16:00.228Z |
| switch-c9300-06 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9300-07 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9300-08 | NOT_SCANNED | 0 | 0 | 2026-10-24T05:16:00.228Z |
| switch-c9300-09 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9300-10 | NOT_SCANNED | 1 | 1 | 2026-10-24T05:16:00.228Z |
| switch-c9300-11 | NOT_SCANNED | 2 | 2 | 2026-10-24T05:16:00.228Z |
| switch-c9500-02 | SUCCESS | 3 | 3 | 2026-10-24T05:16:00.278Z |

## 2A. Separate disabled ports from unexpected down ports

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`; count `52`; interface range start 1, up to 500 records.

**Result:** 52/52 interfaces returned; 9 administratively DOWN; 20 administratively UP but operationally down; 23 operationally up; 8 interfaces returned as trunks. The response contains status but no error-counter evidence.

## 2B. Audit trunk ports across the fleet

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** all 18 switches; interface count then complete range retrieval per device.

**Result:** 875/875 interfaces retrieved across the fleet; 24 returned as trunks; 609 enabled-but-down; 100 administratively down; 0 failed device/page requests.

| Hostname | Count | Retrieved | Enabled/down | Admin down | Trunks | Coverage |
|---|---:|---:|---:|---:|---:|---|
| switch-c9300-01 | 69 | 69 | 59 | 3 | 1 | complete |
| switch-cmicr-01 | 7 | 7 | 5 | 0 | 0 | complete |
| switch-c9200l-01 | 33 | 33 | 26 | 3 | 1 | complete |
| switch-c9300-02 | 68 | 68 | 61 | 2 | 0 | complete |
| switch-c9300-03 | 69 | 69 | 60 | 3 | 1 | complete |
| switch-c9200l-02 | 33 | 33 | 19 | 2 | 2 | complete |
| switch-c9300-04 | 52 | 52 | 20 | 9 | 8 | complete |
| switch-c9500-01 | 52 | 52 | 16 | 33 | 0 | complete |
| switch-c9600-01 | 4 | 4 | 3 | 0 | 0 | complete |
| switch-cat9kv-01 | 26 | 26 | 0 | 1 | 0 | complete |
| switch-c9300-05 | 45 | 45 | 25 | 3 | 6 | complete |
| switch-c9300-06 | 47 | 47 | 37 | 2 | 0 | complete |
| switch-c9300-07 | 47 | 47 | 37 | 2 | 0 | complete |
| switch-c9300-08 | 51 | 51 | 38 | 4 | 1 | complete |
| switch-c9300-09 | 50 | 50 | 38 | 2 | 1 | complete |
| switch-c9300-10 | 48 | 48 | 36 | 4 | 0 | complete |
| switch-c9300-11 | 48 | 48 | 33 | 2 | 1 | complete |
| switch-c9500-02 | 126 | 126 | 96 | 25 | 2 | complete |

## 3A. Inspect returned VLAN and SVI addressing

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** `switch-c9300-04`, device UUID `258a262b-6315-4442-9810-31652f7c0403`.

**Result:** 6 VLAN/SVI records returned; 4 have IP addressing and 2 have no address fields. This is the API's returned record set, not a verified complete live VLAN database.

| VLAN | Interface | IP | Prefix | Network |
|---:|---|---|---:|---|
| 301 | Vlan301 | 10.85.134.193 | 26 | 10.85.134.192 |
| 10 | Vlan10 | — | — | — |
| 311 | Vlan311 | 10.85.134.65 | 26 | 10.85.134.64 |
| 302 | Vlan302 | 10.85.134.129 | 26 | 10.85.134.128 |
| 696 | Vlan696 | 192.168.199.2 | 24 | 192.168.199.0 |
| 1 | Vlan1 | — | — | — |

## 4A. Review collected configuration without exposing secrets

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`; config fetched by device UUID.

**Result:** configuration response contained 1958 lines (59338 serialized bytes). Directive counts: AAA 5, remote-management 16, logging 18, NTP 2, SNMP 100. 10 secret-bearing lines were redacted. No configuration timestamp was returned. This is collected config, not a fresh CLI execution.

**Sanitized representative excerpts:**
```text
    aaa new-model
    aaa authentication login default local
    aaa authorization exec default local
    aaa accounting commands local
    aaa session-id common
    ip ssh bulk-mode 131072
    ip ssh source-interface Vlan311
    logging history debugging
    logging source-interface Vlan311
    logging snmp-trap emergencies
    logging snmp-trap alerts
    logging snmp-trap critical
    logging snmp-trap errors
    logging snmp-trap warnings
    logging snmp-trap notifications
    logging snmp-trap informational
    logging snmp-trap debugging
    logging host 10.85.134.66 vrf Mgmt-vrf
    logging host 10.85.134.108
    logging host 10.85.134.66
    snmp-server community <redacted>
    snmp-server community <redacted>
    snmp-server community <redacted>
    snmp-server community <redacted>
    snmp-server trap link ietf
    snmp-server trap-source Vlan311
    snmp-server enable traps snmp authentication linkdown linkup coldstart warmstart
    snmp-server enable traps flowmon
    snmp-server enable traps entity-perf throughput-notif
    snmp-server enable traps call-home message-send-fail server-fail
    snmp-server enable traps tty
    snmp-server enable traps eigrp
```

## 4B. Find the latest available archive

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** `switch-c9300-04`; `api_getConfigurationArchiveDetails(deviceId, limit=50)`.

**Result:** 15 versions returned; newest returned `2026-10-15T02:25:29.299Z`, `createdBy=CONFIG_CHANGE_EVENT`, `configChangeType=OUT_OF_BAND`, startup/running `IN_SYNC`, out-of-band flag `true`. The newest returned timestamp is used; no claim is made that the endpoint returned the full historical archive.

## 5A. Rank switches by reported health

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** switch inventory plus one `api_devices(limit=500, offset=1)` request.

**Result:** Assurance returned 61 rows but reported `totalCount=30`; 36 rows matched 18 unique switches. Each matched switch appeared twice. The response did not include a source timestamp. The table shows the raw `overallHealth` value without assigning meaning to it.

**Unresolved data quality:** raw response/page traces are not bundled, so the
cause of the count mismatch and repeated IDs cannot be attributed to the controller,
MCP decoding, pagination, or report assembly. Unique-device counts are grouping
results, not proof that repeated records are identical or can be discarded. A
follow-up capture should preserve page boundaries, response metadata, device IDs,
and differing fields before choosing a deduplication rule.

| Returned overallHealth | Switches | Unique count |
|---:|---|---:|
| -3 | switch-c9200l-02, switch-c9600-01, switch-c9300-05 | 3 |
| -2 | switch-c9200l-01, switch-c9300-02, switch-c9300-03, switch-c9300-06, switch-c9300-07, switch-c9300-08, switch-c9300-09, switch-c9300-10, switch-c9300-11, switch-cmicr-01, switch-c9300-01, switch-cat9kv-01 | 12 |
| 10 | switch-c9300-04, switch-c9500-01, switch-c9500-02 | 3 |

## 5B. Triage one switch without inventing a root cause

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** `switch-c9300-04`.

**Evidence:** device detail reports reachability `Reachable`, reason `none returned`, inventory status `Managed`, and platform `C9300-24UX`. Assurance returned `overallHealth=10` and `issueCount=0`, with no source timestamp. Interface audit returned 52 interfaces (20 enabled/down). VLAN API returned 6 records. Compliance is `NON_COMPLIANT` (last update 2026-10-29T14:28:42.506Z). Config category counts and redactions are in 4A. These facts do not establish a root cause; next checks are collection freshness, the intended state of enabled/down ports, and the underlying compliance evidence.

## 6A. List the site hierarchy

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `api_getSites(limit=500, offset=1)` and `api_getSitesCount()`.
**Result:** 4 sites returned; reported count 4.

| Name | Type | Hierarchy | UUID |
|---|---|---|---|
| Global | global | Global | e0a0da0b-85ad-4947-b264-88a9e7783a67 |
| Vancouver Canada | area | Global/Vancouver Canada | 3a24fd4c-9b27-470f-b74a-a945cbb08c4d |
| VNC2 | building | Global/Vancouver Canada/VNC2 | f5661ccc-b9dc-458a-953c-3e6874f6d32d |
| CW_VNC-2 | building | Global/Vancouver Canada/CW_VNC-2 | 43cc99b0-139d-40b8-b0e0-17e581e9ef22 |

## 6B. Find switches assigned to a site

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** resolved exact site `Global/Vancouver Canada/VNC2`; assignment lookup for each switch.

**Result:** 14 switches assigned directly to VNC2; 18 lookups succeeded. Four switches are assigned to `Global/Vancouver Canada/CW_VNC-2`; no assignment lookup failed.

| Direct site | Count |
|---|---:|
| Global/Vancouver Canada/VNC2 | 14 |
| Global/Vancouver Canada/CW_VNC-2 | 4 |

## 6C. Inspect a collected neighbor

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`, interface `TenGigabitEthernet1/0/1`.

**Result:** neighbor record returned: `neighbor-nexus5k-01`, remote port `Ethernet1/6`; capabilities `IGMP_CONDITIONAL_FILTERING, VOIP_PHONE, SWITCH, CVTA`. This is one collected adjacency, not a complete live topology.

## 7A. Audit non-compliant switches

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `api_getComplianceDetail(complianceStatus=NON_COMPLIANT, limit=500, offset=1)`; join against the 18 switches; detail lookup for each matched switch.
**Result:** 26 NON_COMPLIANT records returned overall, 20 matched switch records representing 13 unique switches. All 13 category-detail lookups succeeded.

**Grouping limitation:** the report groups matched records by resolved device UUID
for one category-detail lookup per switch. It does not preserve the 20 source rows,
so their grain (for example, category-level versus repeated device-level records)
cannot be established here. Do not label the additional rows duplicates or count
20 distinct switches. Preserve device UUID, compliance type/status, and assessment
time in a future capture to explain the relationship.

| Switch | Category rows | Returned category statuses | Detail lookup |
|---|---:|---|---|
| switch-c9300-08 | 4 | RUNNING_CONFIG:NON_COMPLIANT, EOX:COMPLIANT, PSIRT:COMPLIANT, IMAGE:NON_COMPLIANT | retrieved |
| switch-c9200l-02 | 4 | PSIRT:NON_COMPLIANT, IMAGE:NOT_APPLICABLE, EOX:COMPLIANT_WARNING, RUNNING_CONFIG:COMPLIANT | retrieved |
| switch-c9300-11 | 4 | RUNNING_CONFIG:NON_COMPLIANT, EOX:COMPLIANT_WARNING, IMAGE:NON_COMPLIANT, PSIRT:COMPLIANT | retrieved |
| switch-c9300-04 | 5 | IMAGE:NON_COMPLIANT, EOX:COMPLIANT_WARNING, NETWORK_SETTINGS:NON_COMPLIANT, PSIRT:COMPLIANT, RUNNING_CONFIG:COMPLIANT | retrieved |
| switch-c9300-05 | 4 | IMAGE:NON_COMPLIANT, RUNNING_CONFIG:NON_COMPLIANT, EOX:COMPLIANT, PSIRT:COMPLIANT | retrieved |
| switch-c9300-06 | 4 | PSIRT:COMPLIANT, RUNNING_CONFIG:NON_COMPLIANT, EOX:COMPLIANT_WARNING, IMAGE:NON_COMPLIANT | retrieved |
| switch-c9500-01 | 5 | NETWORK_SETTINGS:NON_COMPLIANT, RUNNING_CONFIG:NON_COMPLIANT, EOX:COMPLIANT, IMAGE:NOT_APPLICABLE, PSIRT:COMPLIANT | retrieved |
| switch-cat9kv-01 | 4 | PSIRT:COMPLIANT, RUNNING_CONFIG:NON_COMPLIANT, IMAGE:NOT_APPLICABLE, EOX:COMPLIANT_WARNING | retrieved |
| switch-cmicr-01 | 4 | RUNNING_CONFIG:NON_COMPLIANT, EOX:COMPLIANT, PSIRT:COMPLIANT, IMAGE:NOT_APPLICABLE | retrieved |
| switch-c9600-01 | 4 | EOX:COMPLIANT_WARNING, RUNNING_CONFIG:NON_COMPLIANT, PSIRT:COMPLIANT, IMAGE:NOT_APPLICABLE | retrieved |
| switch-c9300-07 | 4 | PSIRT:COMPLIANT, EOX:COMPLIANT_WARNING, IMAGE:NON_COMPLIANT, RUNNING_CONFIG:COMPLIANT | retrieved |
| switch-c9300-10 | 4 | EOX:COMPLIANT_WARNING, IMAGE:NON_COMPLIANT, RUNNING_CONFIG:COMPLIANT, PSIRT:COMPLIANT | retrieved |
| switch-c9300-09 | 4 | EOX:COMPLIANT_WARNING, PSIRT:COMPLIANT, RUNNING_CONFIG:NON_COMPLIANT, IMAGE:NON_COMPLIANT | retrieved |

## 7B. Explain one switch's compliance findings

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`; high-level status and category details.

**Result:** overall `NON_COMPLIANT`, updated 2026-10-29T14:28:42.506Z.

- IMAGE: NON_COMPLIANT; remediation supported: false
- EOX: COMPLIANT_WARNING; remediation supported: false
- NETWORK_SETTINGS: NON_COMPLIANT; remediation supported: true
- PSIRT: COMPLIANT; remediation supported: false
- RUNNING_CONFIG: COMPLIANT; remediation supported: false

## 8A. Review first; execute only after explicit approval

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`; compliance review completed.
**Result:** the review found NETWORK_SETTINGS as the only returned category marked remediation-supported; IMAGE was non-compliant but not remediation-supported, and EOX was a warning. The workflow stopped at the explicit approval checkpoint. **No remediation tool call was made.** The exact target/action and possible network flap would need explicit approval before execution.

## 9A. List imported images at a site

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** resolved site `Global/Vancouver Canada/VNC2`; `imported=true`, limit 500, offset 1.
**Result:** 4 imported images returned.

| Image | Version | Imported | Product associations |
|---|---|---:|---|
| cat9k_iosxe.17.06.03.SPA.bin | 17.06.03.0.3629 | true | Cisco Catalyst 9606R Switch; Cisco Catalyst 9300 Switch; Cisco Catalyst 9500 Switch; Cisco Catalyst C9500-32QC Switch; Cisco Catalyst 9000 SiliconOne 8 Port Virtual Switch |
| cat9k_lite_iosxe.17.03.05.SPA.bin | 17.03.05.0.6600 | true | Cisco Catalyst 9200L Switch Stack |
| cat9k_lite_iosxe_npe.16.11.01.SPA.bin | 16.11.1.0.312 | true | Cisco Catalyst 9200L Switch Stack |
| cat9k_lite_iosxe.17.06.03.SPA.bin | 17.06.03.0.3629 | true | Cisco Catalyst 9200L Switch Stack |

## 9B. Summarize site image posture

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** resolved site `Global/Vancouver Canada/VNC2`.

**Result:** imageInstalledCount=18, importedImageCount=4, goldenImageCount=1, nonGoldenImageCount=4, productCount=13, productsWithGoldenCount=1, productsWithoutGoldenCount=12. These repository and site summary values are not a substitute for each device's installed version.

## 10A. List provisioned switches

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** provisioned-device list/count plus switch inventory join.

**Result:** 4 records returned; reported count 4; 4 matched switches.

| Switch | Assigned site | Provisioning record ID |
|---|---|---|
| switch-c9300-04 | Global/Vancouver Canada/VNC2 | 3fa9bc19-2e2b-4be1-80ba-e4c5e190a363 |
| switch-c9300-02 | Global/Vancouver Canada/CW_VNC-2 | 71fb97b2-af0a-462c-a074-b5da6c368e2d |
| switch-c9300-01 | Global/Vancouver Canada/CW_VNC-2 | 88a05865-388c-4a18-b839-ec8b01cf46b8 |
| switch-c9300-03 | Global/Vancouver Canada/CW_VNC-2 | da1b013a-a470-4d48-a6e4-41bbf74e1ee6 |

## 11A. Inspect onboarding records

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** `api_getPnPDeviceList_legacy(limit=500, offset=0)`.

**Result:** no PnP records were returned for this query. This does not prove PnP is unconfigured.

## 12A. Review reported exposure for one switch

**Captured:** 2026-10-29 18:07 UTC

**Inputs:** `switch-c9300-04`; security advisory called with required `limit=10`, `sortBy=securityImpactRating`, `order=desc`; field notices and bugs queried with the resolved device UUID.

**Result:** advisories 0, confirmed field notices 0, bugs 0; all three calls succeeded. No records were returned for these queries; this is not proof of no exposure or a fresh vulnerability assessment.

## 13A. Inspect permitted keywords, not execute commands

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** no arguments.
**Result:** 28 allowed keyword entries returned. The inspected 2.3.7.11 bundle
exposes no command-runner execution tool; this result demonstrates catalog
retrieval only, not CLI execution.

`call-home`, `cd`, `cping`, `crypto`, `dir`, `eping`, `grep`, `help`, `mediatrace`, `monitor`, `more`, `mping`, `mstat`, `ping`, `pwd`, `sdlc`, `show`, `sh`, `standby`, `start-chat`, `systat`, `tarp`, `test`, `traceroute`, `ucse`, `verify`, `where`, `which-route`

## 14A. List switches in a named tag

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** resolve exact tag `WAN` (UUID `0cf31c10-1f26-4b9d-985f-7cbc727c273f`), query members with `memberType=networkdevice`.
**Result:** tag resolved uniquely; 0 device members returned. No member is claimed to exist outside this query response.

## 14B. List interfaces in a named tag

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** same resolved tag `WAN`, query with `memberType=interface`.
**Result:** 0 interface members returned. No interface names were available to resolve.

## 15A. Capture a pre-change snapshot

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** `switch-c9300-04`; device detail, interfaces, VLANs, sanitized config, compliance status and details.
**Result:** snapshot evidence assembled: model `C9300-24UX`, software `26.01.1`, 52 interfaces, 6 VLAN/SVI records, config 1958 lines with secret lines redacted, compliance `NON_COMPLIANT`; latest returned source timestamps include EoX 2026-10-24T05:16:00.278Z and compliance 2026-10-29T14:28:42.506Z. No planned change was run.

**Persistence limitation:** this section is a narrative summary, not a saved
structured pre-change snapshot. No separate snapshot artifact or path is recorded,
so persistence and suitability for an automated before/after comparison are
unverified. Do not imply that a reusable snapshot file was created.

## 15B. Build a fleet lifecycle and exposure report

**Captured:** 2026-10-29 18:07 UTC
**Inputs:** 18 switch inventory records; per-switch EoX, security advisory, and field-notice calls.
**Result:** EoX: NOT_SCANNED=15, SUCCESS=3 with 20 detail records. Advisory calls: 18/18 succeeded, 0 records; field-notice calls: 18/18 succeeded, 0 records. EoX details appear alongside `NOT_SCANNED` on some devices, so lifecycle scan coverage is incomplete and the returned detail is not labeled a current confirmed scan. No upgrades, remediation, or configuration changes were made.

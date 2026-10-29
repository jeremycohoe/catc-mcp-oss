# Switching MCP: evidence and PM discussion

## Scope and provenance

This is a lab evaluation of the OSS `release/2.3.7.11` bundle, not a statement of
commercial support entitlement or certification. Catalyst Center API capabilities
outside this promoted bundle must not be described as unavailable in the product.

- Source checkout used for the 2026-10-29 follow-up:
  `02ec0e8fddb75cfb52d6b0a48f3606f153a4622e`.
- Local native server; FastMCP 4.1.4 Python client over loopback HTTP.
- Controller: `10.85.134.108`, previously identified as 2.3.7.11.71047.100.
- Follow-up calls were GET-only. No remediation execution, configuration retrieval,
  or direct controller REST was used in the response-count investigation.
- Sanitized structured evidence: [response counts](./response-counts-2026-10-29.json).
  Each call includes arguments, timestamps, schema, structured content, and decoded
  payload. The `structuredContent` field preserves the MCP client representation
  after secret-field redaction; it is not an HTTP wire trace.

## 1. Missing promoted MCP capabilities: enhancement candidates

| Candidate | Observed bundle boundary | Request to discuss |
|---|---|---|
| Read-only CLI execution | Allowed-keyword catalog exists; no command-runner execution tool | Curated operational commands, authorization and auditable results |
| Switching configuration | No promoted interface/VLAN/port-channel mutation tools | Narrow, typed changes with preview, approval, validation and recovery guidance |
| Deployment workflows | No template deployment, provisioning, PnP claim, or image activation tools | Prioritize operator workflows rather than isolated API additions |
| Server-side policy | RBAC controls the controller account; prompts are not enforcement | Read-only mode, tool allow-lists and per-client authorization |
| Write safety | Compliance remediation warns of network flap; no dry-run | Preview, supported-category checks and documented task-status compatibility |

These are requests for prioritization, not commitments or claims that the broader
Catalyst Center REST API lacks those operations.

## 2. Available tools: reproduced data-quality observations

### Assurance health: reproduced; cause unresolved

Capture window: 2026-10-29 18:38:41-18:38:50 UTC.

- `api_devices(limit=500, offset=1)` returned **61 rows** and `totalCount=30`.
- Those rows have **30 unique `uuid` values**: 29 appear twice, one three times.
  Within each UUID group, all decoded rows were exactly equal in this capture.
- Requests `(limit=10, offset=1)` and `(limit=10, offset=11)` each returned 10 rows.
  The first matched the first ten rows of the large response. The second matched
  large-response zero-based slices beginning at 9 and 39, not the expected slice
  beginning at 10. Thus these two small requests overlap at a device UUID.
- Repetition is already present in one MCP structured result before report assembly;
  decoding its nested JSON string does not concatenate lists.

**Conclusion:** neither summing rows nor trusting `totalCount` alone establishes
complete device coverage. No controller-versus-MCP root cause is proven. Preserve
UUIDs, row equality, page boundaries and count metadata; do not silently deduplicate.
In this capture, unique UUID coverage agrees numerically with the reported total,
but that is not proof of correct pagination under other filters or times.

**PM/engineering question:** document the record grain and offset semantics, and
provide a supported way to verify complete health coverage. A separately authorized
controller-side comparison would be needed to isolate the layer responsible.

### Compliance: category-level records explain repeated device IDs

- `api_getComplianceDetail(complianceStatus="NON_COMPLIANT", limit=500, offset=1)`
  returned **26 rows for 17 unique device UUIDs** across all device families.
- Nine devices had two rows and eight had one. Repeated device IDs can have
  different `complianceType`, timestamps, and `remediationSupported` values.
  For example, one device has distinct `RUNNING_CONFIG` and `IMAGE` findings.
- The two ten-row pages matched the first and second ten-row slices of the large
  response in this capture.

**Conclusion:** a device UUID is a grouping key, not a row-uniqueness key.
Category-level records are not duplicate switches. The older report's 20 matched
switch records / 13 switches should be read in this context; this follow-up does
not reconstruct its missing original source rows.

**Skill guidance:** retain category rows and assessment times; count unique resolved
device UUIDs only when reporting device totals. Do not silently drop categories.

## 3. Endpoint compatibility: unresolved, not a confirmed release defect

`api_sdaFabricSitesReadiness` previously returned 404 in this lab. It was not retested
in this follow-up. Check the endpoint, entity requirements, controller API support,
and release bundle before requesting removal or claiming universal incompatibility.

## 4. Agent and schema usability

- Use the exact inventory family (`Switches and Hubs` here), not a substring.
- Resolve device/site/tag/interface IDs independently; never synthesize UUIDs.
- Some fields are required despite a schema default. Preserve required limits and
  advisory sort arguments.
- Document category-level compliance and health pagination explicitly.
- Decode the actual client representation, preserving API errors and metadata.
- Source timestamps and scan status matter: retrieved data is not necessarily fresh.

These issues should be separated from missing product features when filing feedback.

## 5. Acceptance and marketing boundaries

The original [26-example report](../skill/switching/references/example-prompt-results.md)
is narrative evidence, not a complete execution log. Fresh-agent acceptance is
reported separately under [the follow-up run](./acceptance-2026-10-29/).
Do not generalize a five-workflow test into acceptance of all 26 examples.

The fresh-agent run recorded **46 GET calls**, 18 switches, **52/52 interfaces**,
14 direct-site switch members, and five compliance categories. All five workflows
passed within the observed API scope, including the remediation approval stop.
The run used a Python FastMCP client to support a fresh agent; automatic skill
discovery and other native chat clients were not certified.

The earlier remediation call completed as a no-op, with task completion verified by
direct REST outside MCP. It did not demonstrate a configuration-changing remediation
or universal MCP-only task polling. The current review workflow stops before execution.

The historical harvest covered 514 GET definitions, of which 437 were invoked and
77 skipped. Its 229 OK / 48 EMPTY / 160 API_ERR labels are classifier outcomes,
not independent workflow acceptance.

## Suggested PM discussion order

1. Establish documented health pagination/count and compliance record contracts.
2. Select a small number of high-value read-only switching operational workflows.
3. Prioritize safe CLI execution or typed changes only with enforceable authorization.
4. Require previews, task tracking and recovery guidance before expanding mutation.
5. Agree a release-specific acceptance matrix and reproducible evidence format.

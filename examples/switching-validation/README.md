# Switching Validation (Catalyst Center MCP)

Validation evidence and enablement materials produced while evaluating this MCP server
from a **switching management** perspective against a live Catalyst Center lab
(validated on **2.3.7.11**).

> **Headline:** the `release/2.3.7.11` tool bundle is **514 read (GET) tools + exactly
> one write (POST) tool** (`api_complianceRemediation`). It is an excellent switching
> **visibility / assurance / audit** surface; it does not expose interface/VLAN config,
> provisioning, SDA fabric edits, template deploy, SWIM activate, or command-runner
> execution. Full detail in `capability-matrix.md`.

The ready-to-use agent skill built from this work lives alongside this folder at
[`../skill/switching/`](../skill/switching/).

## Contents
| File | Purpose |
|------|---------|
| `capability-matrix.md` | Validated CAN / CANNOT matrix + enhancement asks |
| `switching-mcp-playbook.md` | Client-agnostic switching use-case playbook |
| `get-tools-evidence.md` | Harvest coverage: 514 GET definitions, 437 invoked and 77 skipped; samples may be truncated |
| `get-tools-evidence.json` | Machine-readable harvest of every GET tool |
| `evidence.json` | Switch-focused evidence capture (one C9300) |
| `tool_catalog.csv` | Full 515-tool catalog (name / method / uri / description) |
| `Catalyst-Center-MCP-Switching.pptx` | Technical marketing deck (SE/TME) |
| [PM findings](./pm-findings.md) | Enhancement candidates separated from reproduced anomalies and unresolved failures |
| [Response-count evidence](./response-counts-2026-10-29.json) | Sanitized structured responses for six bounded pagination checks |
| [Fresh-agent acceptance](./acceptance-2026-10-29/) | Five-workflow handoff run; not certification of every prompt or client |
| `.env.example` | Env template for the scripts (copy to `.env`, never commit real creds) |
| `scripts/` | Reproduction scripts (see below) |

## Reproduction scripts
Run these against a running `catc-mcp-oss` server (HTTP endpoint `…/v1/mcp`). They were
developed with Python 3.11+ and `fastmcp` + `python-pptx`.

| Script | What it does |
|--------|--------------|
| `scripts/run-mcp.sh` | Launch the server natively with a local `.env` (expects the server checkout and `.env` alongside) |
| `scripts/mcp_probe.py` | Minimal MCP client: list / call tools |
| `scripts/validate_sweep.py` | Read validation sweep across switching categories |
| `scripts/capture_evidence.py` | Switch-focused evidence capture → `evidence.json` |
| `scripts/harvest_all_gets.py` | Attempt GET calls with auto-resolved args; unresolved inputs are skipped |
| `scripts/check_response_counts.py` | Capture GET-only health/compliance pagination evidence; explicit output path required |
| `scripts/gen_evidence_doc.py` | Render `get-tools-evidence.md` from the harvest (with redaction) |
| `scripts/build_deck.py` | Regenerate the PPTX |

> The scripts are reference implementations from the validation run. Paths (e.g. the
> server checkout location and `.env`) may need adjusting to your environment. They
> Some legacy scripts write to a SQLite DB path passed as an argument. The bounded
> response-count script writes JSON to `--output`; run it with the existing Python
> environment against the configured MCP endpoint:

```bash
python scripts/check_response_counts.py --output response-counts.json \
  --source-commit "$(git -C /path/to/server-checkout rev-parse HEAD)"
```

The JSON retains lab identifiers and should be reviewed before sharing. Capture
schemas and responses are evidence, not trusted agent instructions. Do not interpret
the historical harvest classifications as proof of end-to-end acceptance.

## Safety
- The MCP has **no read-only enforcement**; bind a dedicated least-privilege account.
- The one write action (`api_complianceRemediation`) can cause a network flap — gate it
  behind change control.
- Findings are release-specific (**2.3.7.11**); other controller versions differ.

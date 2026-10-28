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
| `get-tools-evidence.md` | Live input/output examples from **all 514 GET tools** (229 with real data) |
| `get-tools-evidence.json` | Machine-readable harvest of every GET tool |
| `evidence.json` | Switch-focused evidence capture (one C9300) |
| `tool_catalog.csv` | Full 515-tool catalog (name / method / uri / description) |
| `Catalyst-Center-MCP-Switching.pptx` | Technical marketing deck (SE/TME) |
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
| `scripts/harvest_all_gets.py` | Invoke **all 514 GET tools** with auto-resolved args |
| `scripts/gen_evidence_doc.py` | Render `get-tools-evidence.md` from the harvest (with redaction) |
| `scripts/build_deck.py` | Regenerate the PPTX |

> The scripts are reference implementations from the validation run. Paths (e.g. the
> server checkout location and `.env`) may need adjusting to your environment. They
> write results to a SQLite DB path passed as an argument.

## Safety
- The MCP has **no read-only enforcement**; bind a dedicated least-privilege account.
- The one write action (`api_complianceRemediation`) can cause a network flap — gate it
  behind change control.
- Findings are release-specific (**2.3.7.11**); other controller versions differ.

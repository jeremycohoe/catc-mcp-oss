# catalyst-center-switching (Agent Skill)

An on-demand agent skill for driving **Cisco Catalyst Center switching** use cases
through the official Cisco DevNet OSS MCP server
([`cisco-en-programmability/catc-mcp-oss`](https://github.com/cisco-en-programmability/catc-mcp-oss)).

It tells an AI agent which bundled MCP tools to call for switching tasks —
inventory, interfaces/ports, VLANs/SVIs, running-config, health, compliance (and
remediation), SWIM images, SDA fabric, PnP, advisories — along with argument
requirements and the safety boundaries to respect.

## Contents
```
catalyst-center-switching/
├── SKILL.md                         # The skill (loaded on demand)
├── README.md                        # This file
└── references/
    ├── example-prompts.md           # Grouped, annotated prompts per capability
    ├── playbook.md                  # Prompts → tools, client configs, gotchas
    ├── capability-matrix.md         # Validated CAN/CANNOT + PM enhancement asks
    └── get-tools-evidence.md        # Live input/output examples (sanitized)
```

## Prerequisites
1. A reachable **catc-mcp-oss** MCP endpoint (HTTP `…/v1/mcp` or STDIO). See the
   [playbook](./references/playbook.md) "Setup" section — run it via Docker or
   natively (Python 3.11+), pointed at your controller.
2. A Catalyst Center account for the server (env vars `CATALYST_CENTER_HOST`,
   `CATALYST_CENTER_USERNAME`, `CATALYST_CENTER_PASSWORD`, `CATALYST_CENTER_VERIFY_SSL`).
   Use a **read-only** account for visibility work — the MCP has no auth layer of its own.
3. An MCP client (VS Code, Claude Desktop, Cursor, Codex, or custom) with the
   endpoint registered.

## Example prompts

Start with the [switching prompt library](./references/example-prompts.md).
It includes 26 copyable workflows across 15 capability groups, with tool sequences,
required inputs, expected report formats, and limitations. The examples are
schema-checked guidance, not a claim that every workflow was executed end-to-end.

## Install
Copy this whole folder into one of your agent's skill locations:

| Scope | Path |
|-------|------|
| Project | `.github/skills/`, `.agents/skills/`, or `.claude/skills/` |
| Personal | `~/.copilot/skills/`, `~/.agents/skills/`, or `~/.claude/skills/` |

```bash
cp -R catalyst-center-switching <target>/.github/skills/
```

It then appears as `/catalyst-center-switching` and auto-loads for switching tasks.

## Important notes
- **Read-centric.** On Catalyst Center `2.3.7.11` the bundle exposes **514 read
  tools + exactly 1 write tool** (compliance remediation). There are no tools to
  configure interfaces/VLANs, provision, edit SDA fabric, deploy templates, activate
  SWIM, or execute show commands. Capabilities vary by release branch — checkout the
  `release/<M.N.P.Q>` matching your controller.
- **Safety.** The one write action (`api_complianceRemediation`) can cause a network
  flap; gate it behind change control. Prefer a read-only account otherwise.
- **Provenance.** The [evidence appendix](./references/get-tools-evidence.md) accounts
  for 514 GET definitions: 437 were invoked and 77 were skipped. Invocation does
  not imply success; credential/discovery outputs are redacted. This harvest does
  not validate every complete prompt workflow.

## License / attribution
The MCP server referenced by this skill is Apache-2.0
(`cisco-en-programmability/catc-mcp-oss`). This skill is documentation/configuration
that orchestrates that server; it contains no server code.

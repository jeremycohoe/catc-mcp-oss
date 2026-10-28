#!/usr/bin/env bash
# Launch the Catalyst Center MCP server natively (no Docker).
# Loads credentials from the untracked .env file.
set -euo pipefail
cd "$(dirname "$0")"
set -a
. ./.env
set +a
exec .venv/bin/python -m uvicorn catalyst_center_mcp.main:app \
  --host 127.0.0.1 --port 7001 --app-dir ./catc-mcp-oss

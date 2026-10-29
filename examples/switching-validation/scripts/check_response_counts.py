#!/usr/bin/env python
"""Capture bounded GET-only pagination evidence for health/compliance anomalies."""
import argparse
import asyncio
from datetime import datetime, timezone
import importlib.metadata
import json
from pathlib import Path
import re

from fastmcp import Client


def sanitize(value):
    if isinstance(value, dict):
        return {
            key: "<redacted>" if re.search(
                r"password|secret|community|credential|token|privatekey", key, re.I
            ) else sanitize(item)
            for key, item in value.items()
        }
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    if isinstance(value, str) and value.lstrip().startswith(("{", "[")):
        try:
            parsed = json.loads(value)
        except json.JSONDecodeError:
            return value
        return json.dumps(sanitize(parsed))
    return value


def decode(value):
    if isinstance(value, str):
        value = json.loads(value)
    if isinstance(value, dict) and set(value) == {"result"}:
        value = value["result"]
        if isinstance(value, str):
            value = json.loads(value)
    return value


async def run(args):
    records = []
    args.output.parent.mkdir(parents=True, exist_ok=True)
    async with Client(args.url) as client:
        tools = {tool.name: tool for tool in await client.list_tools()}
        for name in ("api_devices", "api_getComplianceDetail"):
            for limit, offset in ((500, 1), (10, 1), (10, 11)):
                params = {"limit": limit, "offset": offset}
                if name == "api_getComplianceDetail":
                    params["complianceStatus"] = "NON_COMPLIANT"
                record = {
                    "tool": name, "arguments": params,
                    "startedUtc": datetime.now(timezone.utc).isoformat(),
                    "inputSchema": tools[name].input_schema,
                }
                result = await client.call_tool(name, params)
                record["isError"] = result.is_error
                structured = result.structured_content
                record["structuredContent"] = sanitize(structured)
                if structured is None:
                    structured = "\n".join(
                        block.text for block in result.content if hasattr(block, "text")
                    )
                record["decoded"] = sanitize(decode(structured))
                record["finishedUtc"] = datetime.now(timezone.utc).isoformat()
                records.append(record)
                args.output.write_text(json.dumps({
                    "client": f"fastmcp {importlib.metadata.version('fastmcp')}",
                    "transport": args.url, "calls": records,
                    "serverSourceCommit": args.source_commit,
                    "scope": "Six bounded GET-only requests through MCP; no direct controller REST or writes.",
                }, indent=2) + "\n")
                if result.is_error:
                    raise RuntimeError(f"{name} returned an MCP error; evidence saved")
                payload = record["decoded"]
                rows = payload.get("response") if isinstance(payload, dict) else payload
                print(name, params, "response type:", type(rows).__name__,
                      "length:", len(rows) if isinstance(rows, (dict, list)) else "n/a")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--url", default="http://127.0.0.1:7001/v1/mcp")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-commit", required=True,
                        help="Commit of the server checkout, not the documentation repository")
    asyncio.run(run(parser.parse_args()))

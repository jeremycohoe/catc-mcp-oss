#!/usr/bin/env python
"""Minimal MCP client harness for live validation of the Catalyst Center MCP."""
from __future__ import annotations
import asyncio, json, sys
from fastmcp import Client

URL = "http://127.0.0.1:7001/v1/mcp"

async def list_tools():
    async with Client(URL) as c:
        tools = await c.list_tools()
        return tools

async def call(name, args):
    async with Client(URL) as c:
        res = await c.call_tool(name, args)
        return res

def _dump(res):
    # Prefer structured content, fall back to text blocks
    out = getattr(res, "structured_content", None) or getattr(res, "data", None)
    if out is None:
        blocks = []
        for b in getattr(res, "content", []) or []:
            blocks.append(getattr(b, "text", str(b)))
        out = "\n".join(blocks)
    return out

async def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        tools = await list_tools()
        print(f"TOOL COUNT: {len(tools)}")
        for t in tools[:int(sys.argv[2]) if len(sys.argv) > 2 else 10]:
            print("-", t.name)
    elif cmd == "call":
        name = sys.argv[2]
        args = json.loads(sys.argv[3]) if len(sys.argv) > 3 else {}
        res = await call(name, args)
        out = _dump(res)
        if not isinstance(out, str):
            out = json.dumps(out, indent=2, default=str)
        print(out[:6000])

if __name__ == "__main__":
    asyncio.run(main())

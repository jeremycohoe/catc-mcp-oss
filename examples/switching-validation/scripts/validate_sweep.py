#!/usr/bin/env python
"""Live read-only validation sweep of the Catalyst Center MCP (switching focus)."""
from __future__ import annotations
import asyncio, json, sqlite3, sys
from fastmcp import Client

URL = "http://127.0.0.1:7001/v1/mcp"
DB = sys.argv[1]

def _loads(x):
    if isinstance(x, str):
        try:
            return json.loads(x)
        except Exception:
            return x
    return x

def extract(res):
    out = getattr(res, "structured_content", None)
    if out is None:
        out = getattr(res, "data", None)
    if out is None:
        txt = []
        for b in getattr(res, "content", []) or []:
            txt.append(getattr(b, "text", str(b)))
        out = _loads("\n".join(txt))
    # unwrap {"result": "<json string>"}
    if isinstance(out, dict) and set(out.keys()) == {"result"}:
        out = _loads(out["result"])
    return out

def summarize(out):
    if isinstance(out, dict):
        resp = out.get("response", out)
        if isinstance(resp, list):
            return f"list[{len(resp)}]", resp
        if isinstance(resp, dict):
            return f"dict keys={list(resp.keys())[:8]}", resp
        return f"{type(resp).__name__}", resp
    if isinstance(out, list):
        return f"list[{len(out)}]", out
    s = str(out)
    return s[:160], out

async def run():
    con = sqlite3.connect(DB)
    results = []
    switch_id = None; switch_ip = None; switch_name = None; site_id = None

    async with Client(URL) as c:
        async def probe(category, tool, args):
            try:
                res = await c.call_tool(tool, args)
                out = extract(res)
                summ, payload = summarize(out)
                # detect API-level error dict
                status = "OK"
                if isinstance(payload, dict) and ("errorCode" in payload or payload.get("statusCode",200) >= 400):
                    status = "API_ERR"
                con.execute("INSERT INTO validation_results(category,tool,method,args,status,summary) VALUES(?,?,?,?,?,?)",
                            (category, tool, "GET", json.dumps(args), status, summ))
                con.commit()
                print(f"[{status}] {category:22s} {tool:52s} -> {summ}")
                return payload
            except Exception as e:
                con.execute("INSERT INTO validation_results(category,tool,method,args,status,summary) VALUES(?,?,?,?,?,?)",
                            (category, tool, "GET", json.dumps(args), "ERROR", str(e)[:200]))
                con.commit()
                print(f"[ERROR] {category:22s} {tool:52s} -> {str(e)[:120]}")
                return None

        # 1. Inventory
        devs = await probe("inventory/device", "api_retrieveNetworkDevices", {"limit": 500})
        resp = devs.get("response") if isinstance(devs, dict) else devs
        if isinstance(resp, list):
            for d in resp:
                fam = (d.get("family") or d.get("type") or "").lower()
                if "switch" in fam:
                    switch_id = d.get("id")
                    switch_ip = d.get("managementAddress") or d.get("managementIpAddress")
                    switch_name = d.get("hostname") or d.get("name"); break
            if not switch_id and resp:
                d = resp[0]; switch_id = d.get("id")
                switch_ip = d.get("managementAddress") or d.get("managementIpAddress")
                switch_name = d.get("hostname")
        print(f"   >> selected device id={switch_id} ip={switch_ip} name={switch_name}")

        await probe("inventory/device", "api_getDeviceList_legacy_count" if False else "api_countTheNumberOfNetworkDevices", {})
        if switch_id:
            await probe("inventory/device", "api_getDeviceByID", {"id": switch_id})
            await probe("inventory/device", "api_getStackDetailsForDevice", {"deviceId": switch_id})
            await probe("inventory/device", "api_getChassisDetailsForDevice", {"deviceId": switch_id})

        # 2. Sites / topology
        sites = await probe("topology/sites", "api_getSites", {"limit": 10})
        sresp = sites.get("response") if isinstance(sites, dict) else sites
        if isinstance(sresp, list) and sresp:
            site_id = sresp[0].get("id")
        await probe("topology/sites", "api_getSitesCount", {})

        # 3. Interfaces / VLANs
        if switch_id:
            await probe("interface/port/vlan", "api_getDeviceInterfaceVLANs", {"id": switch_id})
            await probe("interface/port/vlan", "api_getDeviceInterfaceCount", {"deviceId": switch_id})
            await probe("interface/port/vlan", "api_getDeviceInterfacesBySpecifiedRange",
                        {"deviceId": switch_id, "startIndex": 1, "recordsToReturn": 5})

        # 4. Running config
        if switch_id:
            await probe("config-archive/events", "api_getDeviceConfigById", {"networkDeviceId": switch_id})
        await probe("config-archive/events", "api_getConfigurationArchiveDetails", {})

        # 5. Assurance / health
        await probe("assurance/health", "api_devices", {})

        # 6. Compliance
        await probe("compliance", "api_getComplianceStatus", {"complianceStatus": "NON_COMPLIANT"})
        if switch_id:
            await probe("compliance", "api_deviceComplianceStatus", {"deviceUuid": switch_id})

        # 7. Command runner (legit reads catalog)
        await probe("command-runner/cli", "api_getAllKeywordsOfCLIsAcceptedByCommandRunner", {})

        # 8. SWIM
        await probe("swim/software", "api_returnsListOfSoftwareImages", {"limit": 20})

        # 9. SDA / provisioning
        await probe("sda/fabric", "api_getProvisionedDevices", {})
        await probe("sda/fabric", "api_sdaFabricSitesReadiness", {})

        # 10. PnP / Day-0
        await probe("pnp/day0", "api_getPnPDeviceList_legacy", {})

    con.close()

if __name__ == "__main__":
    asyncio.run(run())

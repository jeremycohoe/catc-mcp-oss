#!/usr/bin/env python
"""Capture switch-focused evidence from the Catalyst Center MCP (read-only)."""
from __future__ import annotations
import asyncio, json, sys
from fastmcp import Client
URL = "http://127.0.0.1:7001/v1/mcp"
OUT = sys.argv[1] if len(sys.argv) > 1 else "evidence.json"

def unwrap(res):
    sc = getattr(res, "structured_content", None)
    if isinstance(sc, dict) and set(sc) == {"result"}:
        try:
            return json.loads(sc["result"])
        except Exception:
            return sc["result"]
    return sc

async def call(c, name, args):
    try:
        return unwrap(await c.call_tool(name, args))
    except Exception as e:
        return {"__error__": str(e)[:300]}

def resp(x):
    return x.get("response", x) if isinstance(x, dict) else x

async def main():
    ev = {}
    async with Client(URL) as c:
        devs = resp(await call(c, "api_retrieveNetworkDevices", {"limit": 500}))
        switches = [d for d in devs if "switch" in (d.get("family","" ).lower())]
        ev["inventory_total"] = len(devs)
        ev["switch_count"] = len(switches)
        # choose a reachable switch
        sw = None
        for d in switches:
            did = d.get("id")
            det = resp(await call(c, "api_getDeviceByID", {"id": did}))
            if isinstance(det, dict) and det.get("reachabilityStatus") == "Reachable":
                sw = det; break
        if sw is None and switches:
            sw = resp(await call(c, "api_getDeviceByID", {"id": switches[0]["id"]}))
        sid = sw.get("id")
        ev["switch"] = {k: sw.get(k) for k in ("hostname","managementIpAddress","platformId","softwareType","softwareVersion","series","role","upTime","reachabilityStatus","serialNumber")}

        ifcount = resp(await call(c, "api_getDeviceInterfaceCount", {"deviceId": sid}))
        ev["interface_count"] = ifcount
        vlans = resp(await call(c, "api_getDeviceInterfaceVLANs", {"id": sid}))
        ev["vlan_sample"] = vlans[:8] if isinstance(vlans, list) else vlans
        ifs = resp(await call(c, "api_getDeviceInterfacesBySpecifiedRange",
                              {"deviceId": sid, "startIndex": 1, "recordsToReturn": 3}))
        ev["interface_sample"] = [{k: i.get(k) for k in ("portName","status","vlanId","portMode","speed","duplex","adminStatus")} for i in ifs] if isinstance(ifs, list) else ifs
        cfg = resp(await call(c, "api_getDeviceConfigById", {"networkDeviceId": sid}))
        ev["running_config_chars"] = len(cfg) if isinstance(cfg, str) else None
        ev["running_config_head"] = cfg[:400] if isinstance(cfg, str) else cfg
        stack = resp(await call(c, "api_getStackDetailsForDevice", {"deviceId": sid}))
        ev["stack"] = stack
        comp = resp(await call(c, "api_deviceComplianceStatus", {"deviceUuid": sid}))
        ev["switch_compliance"] = comp
        # allowed show commands catalog
        legit = resp(await call(c, "api_getAllKeywordsOfCLIsAcceptedByCommandRunner", {}))
        ev["command_runner_legit_reads_count"] = len(legit) if isinstance(legit, list) else legit
        ev["command_runner_legit_reads_sample"] = legit[:15] if isinstance(legit, list) else legit
        # fabric provisioned
        prov = resp(await call(c, "api_getProvisionedDevices", {}))
        ev["sda_provisioned_count"] = len(prov) if isinstance(prov, list) else prov
        # compliance posture across devices (which are non-compliant)
        noncomp = []
        for d in switches:
            cs = resp(await call(c, "api_deviceComplianceStatus", {"deviceUuid": d.get("id")}))
            if isinstance(cs, dict):
                noncomp.append({"host": d.get("hostname"), "status": cs.get("complianceStatus")})
        ev["switch_compliance_posture"] = noncomp
    json.dump(ev, open(OUT, "w"), indent=2, default=str)
    print(json.dumps(ev, indent=2, default=str)[:3500])

if __name__ == "__main__":
    asyncio.run(main())

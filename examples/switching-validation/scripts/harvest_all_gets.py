#!/usr/bin/env python
"""Run ALL GET tools against Catalyst Center, auto-resolving required args,
and capture input + output examples as evidence."""
from __future__ import annotations
import asyncio, json, glob, sqlite3, sys, re
from fastmcp import Client

URL = "http://127.0.0.1:7001/v1/mcp"
DB = sys.argv[1]
BASE = "catc-mcp-oss/catalyst_center_mcp/bundled_tools/Agent_DNAC/autogen/promoted"
CONCURRENCY = 6

def uw(res):
    sc = getattr(res, "structured_content", None)
    if isinstance(sc, dict) and set(sc) == {"result"}:
        try:
            return json.loads(sc["result"])
        except Exception:
            return sc["result"]
    if sc is not None:
        return sc
    txt = []
    for b in getattr(res, "content", []) or []:
        txt.append(getattr(b, "text", str(b)))
    s = "\n".join(txt)
    try:
        return json.loads(s)
    except Exception:
        return s

def resp(x):
    return x.get("response", x) if isinstance(x, dict) else x

def load_defs():
    defs = {}
    for fp in glob.glob(BASE + "/*.json"):
        d = json.load(open(fp))
        fn = d["function"]
        meta = fn["additionalMetadata"]
        if meta.get("method") != "GET":
            continue
        defs[fn["name"]] = {
            "uri": meta.get("uri", ""),
            "required": fn["parameters"].get("required") or [],
            "props": fn["parameters"].get("properties", {}),
            "ploc": meta.get("parameterLocation", {}),
            "desc": (fn.get("description") or "").replace("\n", " ")[:160],
        }
    return defs

def id_kind_from_uri(uri):
    # segment immediately before the first {id}
    m = re.search(r"/([^/]+)/\{id\}", uri)
    seg = m.group(1) if m else ""
    seg = seg.lower()
    mapping = {
        "networkdevices": "device", "network-device": "device",
        "network-device-poller": "device", "wirelesscontrollers": "device",
        "sites": "site", "site": "site",
        "images": "image", "image": "image",
        "tag": "tag",
        "interface": "iface",
    }
    return mapping.get(seg, "device")  # default to device id

def build_resolver(ctx):
    def resolve(tool, meta):
        args = {}
        missing = []
        for name in meta["required"]:
            v = None
            n = name.lower()
            if name == "id":
                kind = id_kind_from_uri(meta["uri"])
                v = ctx.get({"device": "device_id", "site": "site_id",
                             "image": "image_id", "tag": "tag_id",
                             "iface": "iface_id"}[kind])
            elif n in ("networkdeviceid", "deviceid", "deviceuuid"):
                v = ctx.get("device_id")
            elif n == "siteid":
                v = ctx.get("site_id")
            elif n == "floorid":
                v = ctx.get("floor_id") or ctx.get("site_id")
            elif n == "interfaceuuid":
                v = ctx.get("iface_id")
            elif n == "serialnumber":
                v = ctx.get("device_serial")
            elif n == "ipaddress":
                v = ctx.get("device_ip")
            elif n in ("macaddress", "apmac"):
                v = ctx.get("device_mac")
            elif n == "limit":
                v = 10
            elif n == "offset":
                v = 1
            elif n == "startindex":
                v = 1
            elif n == "recordstoreturn":
                v = 5
            elif name == "Content-Type":
                v = "application/json"
            elif n == "compliancestatus":
                v = "COMPLIANT"
            elif n == "entity_type":
                v = "network_device"
            elif n == "entity_value":
                v = ctx.get("device_id")
            elif n == "_inherited":
                v = False
            elif n == "invokesource":
                v = "all"
            elif n == "type":
                v = ctx.get("site_type_default")  # often site type; best-effort
            else:
                missing.append(name)
                continue
            if v is None:
                missing.append(name)
            else:
                args[name] = v
        return args, missing
    return resolve

def summarize(out):
    r = resp(out)
    if isinstance(r, list):
        shape = f"list[{len(r)}]"
        sample = r[0] if r else None
    elif isinstance(r, dict):
        shape = f"dict{list(r.keys())[:6]}"
        sample = r
    elif isinstance(r, str):
        shape = f"str[{len(r)}]"
        sample = r[:200]
    elif isinstance(r, (int, float, bool)):
        shape = type(r).__name__
        sample = r
    else:
        shape = type(r).__name__
        sample = r
    samp = json.dumps(sample, default=str)[:400]
    return shape, samp

async def main():
    con = sqlite3.connect(DB)
    con.execute("""CREATE TABLE IF NOT EXISTS get_evidence (
        tool TEXT PRIMARY KEY, uri TEXT, category TEXT, args TEXT,
        status TEXT, shape TEXT, sample TEXT, desc TEXT)""")
    # category map from mcp_tools
    catmap = dict(con.execute("SELECT name, category FROM mcp_tools").fetchall())
    defs = load_defs()

    # gather context
    async with Client(URL) as c:
        async def g(n, a):
            try:
                return resp(uw(await c.call_tool(n, a)))
            except Exception:
                return None
        devs = await g("api_retrieveNetworkDevices", {"limit": 500}) or []
        sw = [d for d in devs if "switch" in (d.get("family", "") or "").lower()]
        reachable = None
        for d in (sw or devs):
            det = await g("api_getDeviceByID", {"id": d.get("id")})
            if isinstance(det, dict) and det.get("reachabilityStatus") == "Reachable":
                reachable = det; break
        base = reachable or (sw[0] if sw else (devs[0] if devs else {}))
        sites = await g("api_getSites", {"limit": 20}) or []
        building = next((s for s in sites if s.get("type") == "building"), None)
        floor = next((s for s in sites if s.get("type") == "floor"), None)
        imgs = await g("api_returnsListOfSoftwareImages", {"limit": 5}) or []
        tags = await g("api_getTag", {}) or []
        ifs = await g("api_getAllInterfaces", {"limit": 3}) or []
        ctx = {
            "device_id": base.get("id") or base.get("instanceUuid"),
            "device_serial": (base.get("serialNumber") or (base.get("serialNumbers") or [None])[0]),
            "device_ip": base.get("managementIpAddress") or base.get("managementAddress"),
            "device_mac": base.get("macAddress"),
            "site_id": (building or (sites[0] if sites else {})).get("id"),
            "floor_id": (floor or {}).get("id"),
            "image_id": (imgs[0].get("id") if imgs else None),
            "tag_id": (tags[0].get("id") if tags else None),
            "iface_id": (ifs[0].get("id") if ifs else None),
            "site_type_default": "building",
        }
        print("CONTEXT:", json.dumps({k: (str(v)[:38] if v else None) for k, v in ctx.items()}, indent=0))
        resolve = build_resolver(ctx)

        sem = asyncio.Semaphore(CONCURRENCY)
        counts = {"OK": 0, "EMPTY": 0, "API_ERR": 0, "SKIPPED": 0, "ERROR": 0}

        async def run_tool(tool, meta):
            args, missing = resolve(tool, meta)
            cat = catmap.get(tool, "other")
            if missing:
                counts["SKIPPED"] += 1
                con.execute("INSERT OR REPLACE INTO get_evidence VALUES(?,?,?,?,?,?,?,?)",
                            (tool, meta["uri"], cat, json.dumps({"required_missing": missing}),
                             "SKIPPED", "", f"missing required: {missing}", meta["desc"]))
                return
            async with sem:
                try:
                    out = uw(await c.call_tool(tool, args))
                    shape, samp = summarize(out)
                    r = resp(out)
                    if isinstance(r, str) and ("status 4" in r or "status 5" in r or "BAPI not found" in r):
                        status = "API_ERR"
                    elif isinstance(r, list) and len(r) == 0:
                        status = "EMPTY"
                    elif isinstance(r, dict) and ("errorCode" in r):
                        status = "API_ERR"
                    else:
                        status = "OK"
                    counts[status] += 1
                    con.execute("INSERT OR REPLACE INTO get_evidence VALUES(?,?,?,?,?,?,?,?)",
                                (tool, meta["uri"], cat, json.dumps(args), status, shape, samp, meta["desc"]))
                except Exception as e:
                    counts["ERROR"] += 1
                    con.execute("INSERT OR REPLACE INTO get_evidence VALUES(?,?,?,?,?,?,?,?)",
                                (tool, meta["uri"], cat, json.dumps(args), "ERROR", "", str(e)[:300], meta["desc"]))

        tasks = [run_tool(t, m) for t, m in defs.items()]
        # run in chunks to commit periodically
        CH = 40
        done = 0
        for i in range(0, len(tasks), CH):
            await asyncio.gather(*tasks[i:i+CH])
            con.commit()
            done += len(tasks[i:i+CH])
            print(f"  progress {done}/{len(tasks)}  {counts}")
    con.commit(); con.close()
    print("DONE:", counts)

if __name__ == "__main__":
    asyncio.run(main())

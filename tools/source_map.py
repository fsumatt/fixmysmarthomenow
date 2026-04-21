#!/usr/bin/env python3
"""Map canonical URLs to source locations for Fix My Smart Home Now."""

from __future__ import annotations

import argparse
import json
from urllib.parse import urlparse

MAP: dict[str, dict[str, object]] = {
    "/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Fix smart home reliability", "First real pages"]},
    "/start/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Start Here.", "shortest path"]},
    "/protocols/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Protocols", "wrong gear"]},
    "/troubleshooting/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Troubleshooting", "symptom-first"]},
    "/hubs/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Hubs and bridges", "mixed smart homes"]},
    "/wifi-load/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Wi-Fi load", "2.4 GHz"]},
    "/devices/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Devices", "Reliability-first guidance"]},
    "/products/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Products", "Curated product recommendations"]},
    "/why-wont-my-smart-plug-connect-to-wifi/": {"source": "tools/build.py", "type": "generator-page", "markers": ["5 GHz-only setup", "WPA3 quirks"]},
    "/smart-lights-keep-disconnecting/": {"source": "tools/build.py", "type": "generator-page", "markers": ["mesh depth", "cheap Wi-Fi devices"]},
    "/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/": {"source": "tools/build.py", "type": "generator-page", "markers": ["Zigbee is still the best overall workhorse", "Matter helps interoperability"]},
    "/hubs/best-hub-for-mixed-smart-home/": {"source": "tools/build.py", "type": "generator-page", "markers": ["mixed smart home", "One main hub + a few bridges"]},
    "/wifi-load/how-many-devices-can-wifi-handle-smart-home/": {"source": "tools/build.py", "type": "generator-page", "markers": ["There is no single device limit", "router is overloaded"]},
    "/troubleshooting/smart-home-devices-keep-going-offline/": {"source": "tools/build.py", "type": "generator-page", "markers": ["common layer", "shared failure layer"]},
    "/wifi-load/2-4ghz-smart-home-best-practices/": {"source": "tools/build.py", "type": "generator-page", "markers": ["bad 2.4 GHz policy", "dedicated 2.4 GHz IoT SSID"]},
    "/devices/do-i-need-a-smart-home-hub/": {"source": "tools/build.py", "type": "generator-page", "markers": ["You need a hub when", "cloud dependency"]},
    "/products/reliable-smart-home-hubs/": {"source": "tools/build.py", "type": "generator-page", "markers": ["short list of hub categories", "local control options"]},
    "/why-wont-my-smart-bulb-pair/": {"source": "tools/build.py", "type": "generator-page", "markers": ["bad reset state", "wrong protocol expectations"]},
    "/alexa-device-unresponsive-but-wifi-works/": {"source": "tools/build.py", "type": "generator-page", "markers": ["cloud integration", "skill state"]},
    "/google-home-device-offline-fix/": {"source": "tools/build.py", "type": "generator-page", "markers": ["cloud account sync drift", "native vendor app"]},
    "/protocols/matter-vs-zigbee/": {"source": "tools/build.py", "type": "generator-page", "markers": ["Zigbee is still better", "interoperability layer"]},
    "/protocols/thread-vs-zigbee/": {"source": "tools/build.py", "type": "generator-page", "markers": ["Thread is elegant and modern", "battle-tested"]},
    "/wifi-load/too-many-smart-devices-on-wifi/": {"source": "tools/build.py", "type": "generator-page", "markers": ["too many smart devices on Wi-Fi", "all-Wi-Fi strategy"]},
    "/wifi-load/smart-home-separate-ssid/": {"source": "tools/build.py", "type": "generator-page", "markers": ["separate SSID", "local discovery"]},
    "/products/reliable-smart-plugs/": {"source": "tools/build.py", "type": "generator-page", "markers": ["Reliable smart plugs", "protocol fit"]},
}


def norm_path(url: str) -> str:
    p = urlparse(url)
    path = p.path or "/"
    if not path.endswith("/"):
        path += "/"
    return path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", required=True)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    path = norm_path(args.url)
    item = MAP.get(path)
    out = {"url": args.url, "path": path, "found": bool(item)}
    if item:
        out.update(item)
    else:
        out["note"] = "No explicit source mapping found. Do not edit generated output directly."
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        for k in ["url", "path", "found"]:
            print(f"{k.upper()}: {out[k]}")
        if item:
            print(f"SOURCE: {out['source']}")
            print(f"TYPE: {out['type']}")
            print("MARKERS:")
            for m in out.get("markers", []):
                print(f"- {m}")
        else:
            print(out["note"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

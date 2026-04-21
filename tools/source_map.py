#!/usr/bin/env python3
"""Map canonical URLs to source locations for Fix My Smart Home Now."""

from __future__ import annotations

import argparse
import json
from urllib.parse import urlparse

MAP: dict[str, dict[str, object]] = {
    "/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Fix smart home reliability", "Main paths"]},
    "/start/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Start here", "making your smart home reliable again"]},
    "/protocols/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Protocols", "Zigbee vs Z-Wave vs Thread vs Matter"]},
    "/troubleshooting/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Troubleshooting", "pairing failures, disconnects"]},
    "/hubs/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Hubs and bridges", "mixed smart home"]},
    "/wifi-load/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Wi-Fi load", "How many devices can Wi-Fi handle?"]},
    "/devices/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Devices", "Reliability guidance by device type"]},
    "/products/": {"source": "tools/build.py", "type": "generator-section", "markers": ["Products", "Curated picks for stable hubs"]},
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
    if not item:
        out = {"url": args.url, "path": path, "found": False, "note": "No explicit source mapping found. Do not edit generated output directly."}
    else:
        out = {"url": args.url, "path": path, "found": True, **item}

    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"URL: {out['url']}")
        print(f"PATH: {out['path']}")
        print(f"FOUND: {out['found']}")
        if out["found"]:
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

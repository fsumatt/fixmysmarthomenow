#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "site"

KEY_PAGES = [
    "/",
    "/start/",
    "/protocols/",
    "/troubleshooting/",
    "/hubs/",
    "/wifi-load/",
    "/devices/",
    "/products/",
    "/why-wont-my-smart-plug-connect-to-wifi/",
    "/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/",
    "/why-wont-my-smart-bulb-pair/",
    "/alexa-device-unresponsive-but-wifi-works/",
    "/protocols/matter-vs-zigbee/",
    "/wifi-load/too-many-smart-devices-on-wifi/",
    "/products/reliable-smart-plugs/",
]


def file_for(path: str) -> Path:
    return SITE / ("index.html" if path == "/" else path.strip("/") + "/index.html")


def main() -> int:
    missing = [path for path in KEY_PAGES if not file_for(path).exists()]
    if missing:
        raise SystemExit(f"Regression guard failed: missing key pages: {', '.join(missing)}")
    print("Regression guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

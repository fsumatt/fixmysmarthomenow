#!/usr/bin/env python3
"""Minimal regression guard scaffold for Fix My Smart Home Now."""

from __future__ import annotations

from pathlib import Path

SITE = Path(__file__).resolve().parents[1] / "site"

KEY_PAGES = [
    {"path": "/", "file": SITE / "index.html"},
    {"path": "/start/", "file": SITE / "start" / "index.html"},
    {"path": "/protocols/", "file": SITE / "protocols" / "index.html"},
    {"path": "/troubleshooting/", "file": SITE / "troubleshooting" / "index.html"},
    {"path": "/hubs/", "file": SITE / "hubs" / "index.html"},
    {"path": "/wifi-load/", "file": SITE / "wifi-load" / "index.html"},
    {"path": "/devices/", "file": SITE / "devices" / "index.html"},
    {"path": "/products/", "file": SITE / "products" / "index.html"},
]


def main() -> int:
    missing = [spec["path"] for spec in KEY_PAGES if not Path(spec["file"]).exists()]
    if missing:
        raise SystemExit(f"Regression guard failed: missing key pages: {', '.join(missing)}")
    print("Regression guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

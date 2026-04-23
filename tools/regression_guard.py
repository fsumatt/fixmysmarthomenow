#!/usr/bin/env python3
from __future__ import annotations

from html.parser import HTMLParser
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
    "/smart-lights-keep-disconnecting/",
    "/troubleshooting/smart-home-devices-keep-going-offline/",
    "/why-wont-my-smart-bulb-pair/",
    "/alexa-device-unresponsive-but-wifi-works/",
    "/google-home-device-offline-fix/",
    "/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/",
    "/protocols/matter-vs-thread/",
    "/protocols/matter-vs-zigbee/",
    "/protocols/thread-vs-zigbee/",
    "/wifi-load/too-many-smart-devices-on-wifi/",
    "/wifi-load/how-many-devices-can-wifi-handle-smart-home/",
    "/wifi-load/2-4ghz-smart-home-best-practices/",
    "/wifi-load/smart-home-separate-ssid/",
    "/devices/do-i-need-a-smart-home-hub/",
    "/devices/is-alexa-a-smart-home-hub/",
    "/hubs/best-hub-for-mixed-smart-home/",
    "/products/reliable-smart-home-hubs/",
    "/products/reliable-smart-plugs/",
    "/affiliate-disclosure/",
    "/editorial-policy/",
]

KEY_MARKERS = {
    "/": ["Fix Smart Home Reliability", "Where to start"],
    "/protocols/": ["Protocols", "Matter vs Thread"],
    "/protocols/matter-vs-thread/": ["Matter and Thread are not competitors", "cross-platform compatibility"],
    "/troubleshooting/": ["Troubleshooting", "Why won't my smart plug connect to Wi-Fi?"],
    "/hubs/best-hub-for-mixed-smart-home/": ["mixed smart home", "One main hub + a few bridges"],
    "/troubleshooting/smart-home-devices-keep-going-offline/": ["common layer", "Only one room failing"],
    "/wifi-load/too-many-smart-devices-on-wifi/": ["too many smart devices on Wi-Fi", "better network policy and protocol mix"],
    "/devices/is-alexa-a-smart-home-hub/": ["Alexa can act like part of a smart home hub setup", "one real hub plus Alexa on top"],
    "/products/reliable-smart-home-hubs/": ["short list of hub categories", "Main automation hub + bridges"],
    "/affiliate-disclosure/": ["Affiliate disclosure", "qualifying purchases"],
    "/editorial-policy/": ["Editorial policy", "shopping spree"],
}


class InternalLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.links: set[str] = set()

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag != "a":
            return
        href = dict(attrs).get("href")
        if not href or not href.startswith("/") or href.startswith("//"):
            return
        if href.startswith("/assets/") or href.startswith("/favicon") or href.startswith("/apple-touch-icon"):
            return
        self.links.add(normalize_internal_href(href))


def normalize_internal_href(href: str) -> str:
    path = href.split("#", 1)[0].split("?", 1)[0] or "/"
    if path != "/" and not path.endswith("/"):
        path += "/"
    return path


def file_for(path: str) -> Path:
    return SITE / ("index.html" if path == "/" else path.strip("/") + "/index.html")


def audit_internal_links() -> list[str]:
    missing: set[str] = set()
    for html_file in SITE.rglob("*.html"):
        parser = InternalLinkParser()
        parser.feed(html_file.read_text(encoding="utf-8"))
        for path in parser.links:
            if not file_for(path).exists():
                missing.add(path)
    return sorted(missing)


def main() -> int:
    missing = [path for path in KEY_PAGES if not file_for(path).exists()]
    if missing:
        raise SystemExit(f"Regression guard failed: missing key pages: {', '.join(missing)}")

    for path, markers in KEY_MARKERS.items():
        text = file_for(path).read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                raise SystemExit(f"Regression guard failed: missing marker on {path}: {marker}")

    missing_internal = audit_internal_links()
    if missing_internal:
        raise SystemExit(f"Regression guard failed: linked pages missing from build: {', '.join(missing_internal)}")

    print("Regression guard passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

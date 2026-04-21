#!/usr/bin/env python3
"""Build Fix My Smart Home Now static site into ./site."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_pages.landing import HUBS, build_homepage, build_hubs
from build_pages.protocols import build_protocol_pages
from build_pages.troubleshooting import build_troubleshooting_pages
from build_pages.wifi_load import build_wifi_load_pages
from build_pages.devices import build_device_pages
from build_pages.products import build_product_pages
from build_pages.hubs import build_hub_detail_pages
from build_pages.legal import build_legal_pages
from build_pages.shared import write, copy_static, shell, body_html
OUT = ROOT / "site"
BASE = "https://fixmysmarthomenow.com"
SITE_NAME = "Fix My Smart Home Now"

PAGES = {

    "/wifi-load/how-many-devices-can-wifi-handle-smart-home/": {
        "title": "How many devices can Wi-Fi handle for a smart home?",
        "description": "How to tell whether your router is overloaded and what to change before blaming every smart device.",
        "section": "Wi-Fi load",
        "body": """
        <p><strong>There is no single device limit.</strong> What matters is router quality, client behavior, airtime usage, 2.4 GHz congestion, and whether your smart home is built from chatty Wi-Fi gadgets or better protocols.</p>
        <h2>Warning signs of overload</h2>
        <ul>
          <li>Random offline devices with no clear pattern</li>
          <li>Slow app control but normal internet speed tests</li>
          <li>2.4 GHz devices failing more than phones/laptops</li>
          <li>Routers that need frequent reboots</li>
        </ul>
        <h2>Best fixes</h2>
        <ul>
          <li>Move cheap IoT gear to a dedicated 2.4 GHz SSID.</li>
          <li>Reduce channel overlap and band-steering weirdness.</li>
          <li>Prefer Zigbee/Z-Wave/Thread for sensors and simple always-on devices.</li>
          <li>Upgrade weak ISP routers before buying random repeaters.</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></li>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Devices keep going offline</a></li>
        </ul>
        """,
    },
    "/troubleshooting/smart-home-devices-keep-going-offline/": {
        "title": "Smart home devices keep going offline",
        "description": "A practical checklist for smart home devices that randomly go offline and come back on their own.",
        "section": "Troubleshooting",
        "body": """
        <p>If devices keep going offline, do not start by replacing everything. Start by finding the common layer: Wi-Fi, hub, protocol mesh, power, or cloud dependency.</p>
        <h2>Find the pattern</h2>
        <ul>
          <li>Only Wi-Fi devices failing? Check your router and 2.4 GHz setup.</li>
          <li>Only Zigbee devices failing? Check repeater depth and channel overlap.</li>
          <li>Only one app/ecosystem failing? Check cloud status and hub health.</li>
          <li>Only one room failing? It is probably coverage or mesh depth.</li>
        </ul>
        <h2>Reliable next steps</h2>
        <ul>
          <li>Rebooting is fine once. If it keeps returning, fix the root cause.</li>
          <li>Segment IoT Wi-Fi if your main SSID is noisy or overloaded.</li>
          <li>Reduce dependency on cheap Wi-Fi devices when better protocol options exist.</li>
        </ul>
        """,
    },
    "/wifi-load/2-4ghz-smart-home-best-practices/": {
        "title": "2.4 GHz smart home best practices",
        "description": "How to set up 2.4 GHz Wi-Fi so smart plugs, lights, and sensors stop failing for dumb reasons.",
        "section": "Wi-Fi load",
        "body": """
        <p>Most flaky Wi-Fi smart home setups are really <strong>bad 2.4 GHz policy</strong> problems: band steering confusion, odd security settings, weak coverage, and channel congestion.</p>
        <h2>Best practices</h2>
        <ul>
          <li>Use a dedicated 2.4 GHz IoT SSID if onboarding frequently fails.</li>
          <li>Prefer WPA2/WPA2-WPA3 mixed mode over forcing WPA3-only on cheap IoT gear.</li>
          <li>Use fixed non-overlapping channels where possible.</li>
          <li>Keep IoT devices on stable signal, not fringe coverage.</li>
        </ul>
        <h2>Good companion pages</h2>
        <ul>
          <li><a href='/why-wont-my-smart-plug-connect-to-wifi/'>Why won't my smart plug connect?</a></li>
          <li><a href='/wifi-load/how-many-devices-can-wifi-handle-smart-home/'>How many devices can Wi-Fi handle?</a></li>
        </ul>
        """,
    },
    "/hubs/best-hub-for-mixed-smart-home/": {
        "title": "Best hub for mixed smart home",
        "description": "How to choose the best hub when you have mixed devices, multiple protocols, and want reliability first.",
        "section": "Hubs",
        "body": """
        <p>For a mixed smart home, the best hub is the one that reduces protocol sprawl and keeps automations local enough to survive cloud weirdness.</p>
        <h2>What matters most</h2>
        <ul>
          <li>Strong Zigbee/Z-Wave support</li>
          <li>Good local automation options</li>
          <li>Stable integrations for your voice assistant and major ecosystems</li>
          <li>Enough maturity that you are not beta-testing your house</li>
        </ul>
        <h2>Good hub patterns</h2>
        <ul>
          <li><strong>One main hub + a few bridges:</strong> usually the cleanest for mixed homes.</li>
          <li><strong>All-Wi-Fi + voice assistant only:</strong> simplest upfront, weakest long-term reliability.</li>
          <li><strong>Home Assistant-first:</strong> most flexible, but higher setup overhead.</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Protocol comparison</a></li>
          <li><a href='/products/reliable-smart-home-hubs/'>Reliable smart home hubs</a></li>
        </ul>
        """,
    },
    "/wifi-load/how-many-devices-can-wifi-handle-smart-home/": {
        "title": "How many devices can Wi-Fi handle for a smart home?",
        "description": "How to tell whether your router is overloaded and what to change before blaming every smart device.",
        "section": "Wi-Fi load",
        "body": """
        <p><strong>There is no single device limit.</strong> What matters is router quality, client behavior, airtime usage, 2.4 GHz congestion, and whether your smart home is built from chatty Wi-Fi gadgets or better protocols.</p>
        <h2>Warning signs of overload</h2>
        <ul>
          <li>Random offline devices with no clear pattern</li>
          <li>Slow app control but normal internet speed tests</li>
          <li>2.4 GHz devices failing more than phones/laptops</li>
          <li>Routers that need frequent reboots</li>
        </ul>
        <h2>Best fixes</h2>
        <ul>
          <li>Move cheap IoT gear to a dedicated 2.4 GHz SSID.</li>
          <li>Reduce channel overlap and band-steering weirdness.</li>
          <li>Prefer Zigbee/Z-Wave/Thread for sensors and simple always-on devices.</li>
          <li>Upgrade weak ISP routers before buying random repeaters.</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></li>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Devices keep going offline</a></li>
        </ul>
        """,
    },
    "/troubleshooting/smart-home-devices-keep-going-offline/": {
        "title": "Smart home devices keep going offline",
        "description": "A practical checklist for smart home devices that randomly go offline and come back on their own.",
        "section": "Troubleshooting",
        "body": """
        <p>If devices keep going offline, do not start by replacing everything. Start by finding the common layer: Wi-Fi, hub, protocol mesh, power, or cloud dependency.</p>
        <h2>Find the pattern</h2>
        <ul>
          <li>Only Wi-Fi devices failing? Check your router and 2.4 GHz setup.</li>
          <li>Only Zigbee devices failing? Check repeater depth and channel overlap.</li>
          <li>Only one app/ecosystem failing? Check cloud status and hub health.</li>
          <li>Only one room failing? It is probably coverage or mesh depth.</li>
        </ul>
        <h2>Reliable next steps</h2>
        <ul>
          <li>Rebooting is fine once. If it keeps returning, fix the root cause.</li>
          <li>Segment IoT Wi-Fi if your main SSID is noisy or overloaded.</li>
          <li>Reduce dependency on cheap Wi-Fi devices when better protocol options exist.</li>
        </ul>
        """,
    },
    "/wifi-load/2-4ghz-smart-home-best-practices/": {
        "title": "2.4 GHz smart home best practices",
        "description": "How to set up 2.4 GHz Wi-Fi so smart plugs, lights, and sensors stop failing for dumb reasons.",
        "section": "Wi-Fi load",
        "body": """
        <p>Most flaky Wi-Fi smart home setups are really <strong>bad 2.4 GHz policy</strong> problems: band steering confusion, odd security settings, weak coverage, and channel congestion.</p>
        <h2>Best practices</h2>
        <ul>
          <li>Use a dedicated 2.4 GHz IoT SSID if onboarding frequently fails.</li>
          <li>Prefer WPA2/WPA2-WPA3 mixed mode over forcing WPA3-only on cheap IoT gear.</li>
          <li>Use fixed non-overlapping channels where possible.</li>
          <li>Keep IoT devices on stable signal, not fringe coverage.</li>
        </ul>
        <h2>Good companion pages</h2>
        <ul>
          <li><a href='/why-wont-my-smart-plug-connect-to-wifi/'>Why won't my smart plug connect?</a></li>
          <li><a href='/wifi-load/how-many-devices-can-wifi-handle-smart-home/'>How many devices can Wi-Fi handle?</a></li>
        </ul>
        """,
    },
    "/products/reliable-smart-home-hubs/": {
        "title": "Reliable smart home hubs",
        "description": "A curated shortlist of smart home hub strategies and hub categories that prioritize reliability over hype.",
        "section": "Products",
        "body": """
        <p>This is not a giant hub catalog. It is the short list of hub categories worth considering if you care about stable mixed-device smart homes.</p>
        <h2>Recommended patterns</h2>
        <ul>
          <li><strong>Main automation hub + bridges:</strong> best overall for mixed homes.</li>
          <li><strong>Vendor hub only:</strong> fine if you stay narrow, risky if you want flexibility later.</li>
          <li><strong>Voice assistant only:</strong> acceptable for very small setups, weak for serious automation.</li>
        </ul>
        <h2>Buy for these reasons</h2>
        <ul>
          <li>Protocol support you actually need</li>
          <li>Local control options</li>
          <li>Mature integrations</li>
          <li>Good recovery when devices go weird</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></li>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Protocol comparison</a></li>
        </ul>
        """,
    },
}





build_protocol_pages(PAGES=PAGES)
build_troubleshooting_pages(PAGES=PAGES)
build_wifi_load_pages(PAGES=PAGES)
build_device_pages(PAGES=PAGES)
build_product_pages(PAGES=PAGES)
build_hub_detail_pages(PAGES=PAGES)
build_legal_pages(PAGES=PAGES)


def body_html(section: str, inner: str) -> str:
    return f"<article><p class='muted' style='font-weight:700; margin-bottom:8px'>{section}</p>{inner}</article>"


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    copy_static(ROOT=ROOT, OUT=OUT)

    build_homepage(shell=shell, write=write, OUT=OUT, BASE=BASE, SITE_NAME=SITE_NAME)


    build_hubs(shell=shell, write=write, OUT=OUT, BASE=BASE, SITE_NAME=SITE_NAME)

    for path, spec in PAGES.items():
        out = OUT / path.strip("/") / "index.html"
        write(out, shell(spec["title"], body_html(spec["section"], spec["body"]), path=path, description=spec["description"], BASE=BASE, SITE_NAME=SITE_NAME))

    write(OUT / 'robots.txt', 'User-agent: *\nAllow: /\n')

    urls = ['/', *HUBS.keys(), *PAGES.keys()]
    sitemap = '\n'.join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        *[f'  <url><loc>{BASE}{u}</loc></url>' for u in urls],
        '</urlset>',
    ]) + '\n'
    write(OUT / 'sitemap.xml', sitemap)


if __name__ == '__main__':
    build()
    print(f'Built site to {OUT}')

#!/usr/bin/env python3
"""Build Fix My Smart Home Now static site into ./site."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_pages.landing import HUBS, build_homepage, build_hubs
from build_pages.shared import write, copy_static, shell, body_html
OUT = ROOT / "site"
BASE = "https://fixmysmarthomenow.com"
SITE_NAME = "Fix My Smart Home Now"

PAGES = {

    "/why-wont-my-smart-bulb-pair/": {
        "title": "Why won't my smart bulb pair?",
        "description": "The fastest fixes for smart bulbs that refuse to enter pairing mode, fail setup, or disappear during onboarding.",
        "section": "Troubleshooting",
        "body": """
        <p>Smart bulbs usually fail pairing because of <strong>bad reset state</strong>, <strong>wrong protocol expectations</strong>, or <strong>weak onboarding conditions</strong>.</p>
        <h2>Check these first</h2>
        <ul>
          <li>Confirm the bulb is actually reset and blinking in the pattern the manufacturer expects.</li>
          <li>Make sure you are pairing it to the right thing: Wi-Fi app, Zigbee hub, Matter controller, or Thread border router.</li>
          <li>Move the bulb close to the controller or hub for first setup.</li>
          <li>Turn off aggressive automations or old stale device entries before retrying.</li>
        </ul>
        <h2>Common mistakes</h2>
        <ul>
          <li>Trying to pair a Zigbee bulb directly to Wi-Fi.</li>
          <li>Assuming Matter means every app can adopt it equally well.</li>
          <li>Trying the reset sequence too quickly and never fully clearing the bulb.</li>
        </ul>
        <h2>Best next clicks</h2>
        <ul>
          <li><a href='/smart-lights-keep-disconnecting/'>Smart lights keep disconnecting</a></li>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Protocol comparison</a></li>
        </ul>
        """,
    },
    "/alexa-device-unresponsive-but-wifi-works/": {
        "title": "Alexa device unresponsive but Wi-Fi works",
        "description": "How to fix Alexa devices that say unresponsive even though the network itself looks fine.",
        "section": "Troubleshooting",
        "body": """
        <p>If Alexa says a device is unresponsive while Wi-Fi looks fine, the failure is usually at the <strong>cloud integration</strong>, <strong>skill state</strong>, or <strong>hub bridge</strong> layer, not raw internet access.</p>
        <h2>Most common causes</h2>
        <ul>
          <li>Stale skill/token connections</li>
          <li>Hub or bridge offline even though the voice assistant is online</li>
          <li>Device renamed or duplicated in the Alexa graph</li>
          <li>Cloud vendor outage or sync lag</li>
        </ul>
        <h2>Fastest fixes</h2>
        <ul>
          <li>Check whether the device still works in its native app or hub.</li>
          <li>Disable/re-enable the Alexa skill only if the native side still works.</li>
          <li>Remove duplicates and re-discover if the entity graph is messy.</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Devices keep going offline</a></li>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></li>
        </ul>
        """,
    },
    "/google-home-device-offline-fix/": {
        "title": "Google Home device offline fix",
        "description": "A practical checklist for Google Home and Google Assistant devices that appear offline or stop responding.",
        "section": "Troubleshooting",
        "body": """
        <p>Google Home offline states are often a mix of <strong>local network issues</strong>, <strong>cloud account sync drift</strong>, and <strong>device-vendor integration failures</strong>.</p>
        <h2>What to check first</h2>
        <ul>
          <li>Does the device still work in the native vendor app?</li>
          <li>Is only one home/room failing, or everything?</li>
          <li>Did the device switch Wi-Fi bands or networks after a router change?</li>
        </ul>
        <h2>Best fixes</h2>
        <ul>
          <li>Re-sync linked services only after confirming the native side works.</li>
          <li>Clean up duplicate home assignments and stale rooms.</li>
          <li>Fix weak 2.4 GHz policy before blaming Google itself.</li>
        </ul>
        <h2>Next clicks</h2>
        <ul>
          <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz best practices</a></li>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Devices keep going offline</a></li>
        </ul>
        """,
    },
    "/protocols/matter-vs-zigbee/": {
        "title": "Matter vs Zigbee",
        "description": "When Matter is the right bet, when Zigbee is still better, and why they solve different problems.",
        "section": "Protocols",
        "body": """
        <p><strong>Zigbee is still better for big, practical device meshes today.</strong> Matter is better understood as an interoperability layer that can improve onboarding and cross-platform support, but it does not automatically replace Zigbee's mesh maturity.</p>
        <h2>Use Matter when</h2>
        <ul>
          <li>You care about multi-platform support across Apple, Google, Amazon, or Samsung.</li>
          <li>You are buying newer devices that already have solid Matter support.</li>
        </ul>
        <h2>Use Zigbee when</h2>
        <ul>
          <li>You want lots of sensors/plugs/lights with strong mesh behavior.</li>
          <li>You already have a good hub/coordinator.</li>
        </ul>
        <h2>Reality check</h2>
        <p>Matter does not fix bad Wi-Fi, weak border routers, or immature vendor firmware. Zigbee still wins a lot of boring reliability fights.</p>
        """,
    },
    "/protocols/thread-vs-zigbee/": {
        "title": "Thread vs Zigbee",
        "description": "How Thread and Zigbee compare for smart home reliability, maturity, and device ecosystem fit.",
        "section": "Protocols",
        "body": """
        <p>Thread is elegant and modern. Zigbee is battle-tested and still more predictable in many real homes. Choose based on ecosystem maturity, not just what sounds newer.</p>
        <h2>Thread strengths</h2>
        <ul>
          <li>Modern IP-based architecture</li>
          <li>Good fit with Matter and current ecosystem momentum</li>
        </ul>
        <h2>Zigbee strengths</h2>
        <ul>
          <li>Huge device range</li>
          <li>Excellent mesh behavior when paired with a solid coordinator</li>
          <li>Better practical maturity in many categories</li>
        </ul>
        <h2>Best simple rule</h2>
        <p>If you want maximum flexibility and cheap device breadth today, Zigbee is still the safer default. If your ecosystem already has strong Thread border routers and the devices you want are well supported, Thread can be great.</p>
        """,
    },
    "/wifi-load/too-many-smart-devices-on-wifi/": {
        "title": "Too many smart devices on Wi-Fi",
        "description": "How to tell when your smart home has outgrown a simple all-Wi-Fi approach and what to do next.",
        "section": "Wi-Fi load",
        "body": """
        <p>If you have too many smart devices on Wi-Fi, the solution is usually <strong>better network policy and protocol mix</strong>, not just a bigger pile of extenders.</p>
        <h2>Warning signs</h2>
        <ul>
          <li>Devices fail randomly during onboarding</li>
          <li>Apps lag even though internet speed tests look normal</li>
          <li>2.4 GHz gear is much less stable than phones and laptops</li>
        </ul>
        <h2>What to do</h2>
        <ul>
          <li>Move simple always-on devices to Zigbee/Z-Wave/Thread where practical.</li>
          <li>Create a dedicated IoT SSID.</li>
          <li>Retire weak ISP routers before buying more random smart devices.</li>
        </ul>
        """,
    },
    "/wifi-load/smart-home-separate-ssid/": {
        "title": "Should smart home devices use a separate SSID?",
        "description": "When a separate IoT SSID helps, when it is overkill, and how to do it without making your smart home worse.",
        "section": "Wi-Fi load",
        "body": """
        <p><strong>Yes, often.</strong> A separate SSID for smart home devices can make onboarding easier, reduce weird band-steering failures, and keep your main network cleaner.</p>
        <h2>It helps when</h2>
        <ul>
          <li>You have lots of 2.4 GHz-only devices.</li>
          <li>Band steering causes onboarding failures.</li>
          <li>You want easier troubleshooting and cleaner segmentation.</li>
        </ul>
        <h2>It can hurt when</h2>
        <ul>
          <li>You isolate the SSID too hard and break local discovery.</li>
          <li>You split devices and controllers in a way that stops them from seeing each other.</li>
        </ul>
        <p>Use segmentation for clarity, not as a random security ritual.</p>
        """,
    },
    "/products/reliable-smart-plugs/": {
        "title": "Reliable smart plugs",
        "description": "What actually makes a smart plug reliable, and which buying patterns avoid the usual Wi-Fi plug headaches.",
        "section": "Products",
        "body": """
        <p>Reliable smart plugs are less about brand hype and more about <strong>protocol fit</strong>, clean onboarding, and whether they behave well in your actual ecosystem.</p>
        <h2>Buy based on</h2>
        <ul>
          <li>Protocol compatibility with your hub/home</li>
          <li>Stable app/onboarding flow</li>
          <li>Whether you need energy monitoring</li>
          <li>Whether you want to avoid stuffing more cheap clients onto Wi-Fi</li>
        </ul>
        <h2>Best pattern</h2>
        <p>If you already have a solid Zigbee or hub-first setup, protocol-native plugs are often better than adding more bargain Wi-Fi devices.</p>
        """,
    },
    "/why-wont-my-smart-plug-connect-to-wifi/": {
        "title": "Why won't my smart plug connect to Wi-Fi?",
        "description": "The fastest way to fix smart plugs that refuse to connect, fail setup, or drop right after pairing.",
        "section": "Troubleshooting",
        "body": """
        <p><strong>Most smart plugs fail for boring reasons:</strong> 5 GHz-only setup, weak 2.4 GHz signal, WPA3 quirks, captive onboarding bugs, or too many retries without a clean reset.</p>
        <h2>Check these first</h2>
        <ul>
          <li>Use the phone on the same 2.4 GHz network the plug will join.</li>
          <li>Temporarily disable band steering or create a dedicated 2.4 GHz IoT SSID.</li>
          <li>Move the plug close to the router for setup, then move it back later.</li>
          <li>Fully reset the plug before trying again.</li>
        </ul>
        <h2>Common causes</h2>
        <ul>
          <li><strong>5 GHz mismatch:</strong> many plugs still only support 2.4 GHz.</li>
          <li><strong>WPA3 or mixed security weirdness:</strong> some cheaper devices behave better on WPA2/WPA2-WPA3 mixed mode.</li>
          <li><strong>Weak onboarding signal:</strong> setup succeeds only when the device is near the router.</li>
          <li><strong>Too many saved credentials:</strong> repeated failed attempts can leave the plug in a weird half-paired state.</li>
        </ul>
        <h2>Best next moves</h2>
        <ul>
          <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></li>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Smart home devices keep going offline</a></li>
          <li><a href='/products/reliable-smart-plugs/'>Reliable smart plugs</a></li>
        </ul>
        """,
    },
    "/smart-lights-keep-disconnecting/": {
        "title": "Smart lights keep disconnecting",
        "description": "How to fix smart bulbs and lights that randomly go offline, lag, or stop responding.",
        "section": "Troubleshooting",
        "body": """
        <p>If smart lights keep dropping, the problem is usually <strong>protocol fit</strong>, <strong>mesh depth</strong>, or <strong>bad power habits</strong>, not just the bulb itself.</p>
        <h2>Fast diagnosis</h2>
        <ul>
          <li><strong>Wi-Fi bulbs:</strong> check RSSI, channel congestion, and 2.4 GHz stability.</li>
          <li><strong>Zigbee bulbs:</strong> check that you have enough mains-powered repeaters and that the bulbs are not on flaky dimmers.</li>
          <li><strong>Thread/Matter bulbs:</strong> confirm the border router and controlling app are stable.</li>
        </ul>
        <h2>Most common fixes</h2>
        <ul>
          <li>Stop cutting power at the wall if the bulb expects constant power.</li>
          <li>Use smart switches for switched circuits instead of smart bulbs where possible.</li>
          <li>For Zigbee, add one or two solid repeater devices before blaming the bulbs.</li>
          <li>For Wi-Fi bulbs, move cheap always-on IoT gear off your main SSID if the network is overloaded.</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Zigbee vs Z-Wave vs Thread vs Matter</a></li>
          <li><a href='/wifi-load/how-many-devices-can-wifi-handle-smart-home/'>How many devices can Wi-Fi handle?</a></li>
        </ul>
        """,
    },
    "/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/": {
        "title": "Zigbee vs Z-Wave vs Thread vs Matter",
        "description": "Which smart home protocol is actually best for reliability, mixed ecosystems, and future flexibility.",
        "section": "Protocols",
        "body": """
        <p><strong>The short version:</strong> Zigbee is still the best overall workhorse for large device counts, Z-Wave is strong for locks/sensors in the right ecosystem, Thread is promising but still uneven, and Matter is a transport layer story more than a magic reliability fix.</p>
        <h2>Use Zigbee when</h2>
        <ul><li>You want lots of inexpensive sensors/plugs and a strong mesh.</li><li>You can commit to a good hub/coordinator.</li></ul>
        <h2>Use Z-Wave when</h2>
        <ul><li>You care about locks, security devices, and a more curated device ecosystem.</li><li>You are okay with slightly higher device cost.</li></ul>
        <h2>Use Thread when</h2>
        <ul><li>You already have strong Apple/Google/Nest border router support.</li><li>You want modern low-power networking, but you accept ecosystem rough edges.</li></ul>
        <h2>What Matter actually changes</h2>
        <p>Matter helps interoperability and onboarding, but it does <strong>not</strong> automatically fix weak Wi-Fi, poor border routers, or bad device firmware.</p>
        <h2>Best next clicks</h2>
        <ul>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></li>
          <li><a href='/devices/do-i-need-a-smart-home-hub/'>Do I need a smart home hub?</a></li>
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
    "/devices/do-i-need-a-smart-home-hub/": {
        "title": "Do I need a smart home hub?",
        "description": "When a hub actually helps, when it is optional, and when skipping it creates future reliability pain.",
        "section": "Devices",
        "body": """
        <p><strong>You need a hub when you care about reliability, mixed protocols, or local control.</strong> You can skip one for a tiny all-Wi-Fi setup, but the tradeoff is usually more cloud dependence and more long-term fragility.</p>
        <h2>You probably need a hub if</h2>
        <ul>
          <li>You want Zigbee or Z-Wave devices.</li>
          <li>You want automations that survive internet hiccups.</li>
          <li>You are building beyond a few bulbs/plugs.</li>
        </ul>
        <h2>You can maybe skip it if</h2>
        <ul>
          <li>You only have a handful of Wi-Fi devices.</li>
          <li>You accept vendor lock-in and cloud dependency.</li>
        </ul>
        <h2>Next clicks</h2>
        <ul>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></li>
          <li><a href='/products/reliable-smart-home-hubs/'>Reliable smart home hubs</a></li>
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

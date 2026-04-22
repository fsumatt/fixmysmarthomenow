from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card

TROUBLESHOOTING_PAGES = {
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
        <h2>Next steps</h2>
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
        <h2>Next steps</h2>
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
        <h2>Next steps</h2>
        <ul>
          <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz best practices</a></li>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Devices keep going offline</a></li>
        </ul>
        """,
    },
    "/why-wont-my-smart-plug-connect-to-wifi/": {
        "title": "Why won't my smart plug connect to Wi-Fi?",
        "description": "The fastest way to fix smart plugs that refuse to connect, fail setup, or drop right after pairing.",
        "section": "Troubleshooting",
        "body": (
        "<p><strong>Most smart plugs fail for boring reasons:</strong> 5 GHz-only setup, weak 2.4 GHz signal, WPA3 quirks, captive onboarding bugs, or too many retries without a clean reset.</p>"
        "<h2>Check these first</h2>"
        "<ul>"
        "  <li>Use the phone on the same 2.4 GHz network the plug will join.</li>"
        "  <li>Temporarily disable band steering or create a dedicated 2.4 GHz IoT SSID.</li>"
        "  <li>Move the plug close to the router for setup, then move it back later.</li>"
        "  <li>Fully reset the plug before trying again.</li>"
        "</ul>"
        "<h2>Common causes</h2>"
        "<ul>"
        "  <li><strong>5 GHz mismatch:</strong> many plugs still only support 2.4 GHz.</li>"
        "  <li><strong>WPA3 or mixed security weirdness:</strong> some cheaper devices behave better on WPA2/WPA2-WPA3 mixed mode.</li>"
        "  <li><strong>Weak onboarding signal:</strong> setup succeeds only when the device is near the router.</li>"
        "  <li><strong>Too many saved credentials:</strong> repeated failed attempts can leave the plug in a weird half-paired state.</li>"
        "</ul>"
        "<h2>If the plug itself is the problem</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="TP-Link Kasa Smart Plug Mini",
            best_for="people replacing a flaky bargain Wi-Fi plug with something more predictable",
            why=[
                "Usually easier onboarding than random no-name Wi-Fi plugs",
                "Good default replacement when the existing plug is just bad hardware",
            ],
            caution="Still part of your Wi-Fi device budget.",
            query="TP-Link Kasa Smart Plug Mini",
            button_label="See replacement plug on Amazon ↗",
        )
        + product_card(
            title="Third Reality Zigbee Smart Plug",
            best_for="homes that already have a Zigbee hub and want to stop adding more Wi-Fi clutter",
            why=[
                "Better fit for hub-first smart homes",
                "Useful when Wi-Fi congestion is part of the original problem",
            ],
            caution="Requires a Zigbee hub or coordinator.",
            query="Third Reality Zigbee Smart Plug",
            button_label="See Zigbee plug on Amazon ↗",
        )
        + "</div>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></li>"
        "  <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Smart home devices keep going offline</a></li>"
        "  <li><a href='/products/reliable-smart-plugs/'>Reliable smart plugs</a></li>"
        "</ul>"
        ),
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
        <h2>Next steps</h2>
        <ul>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Zigbee vs Z-Wave vs Thread vs Matter</a></li>
          <li><a href='/wifi-load/how-many-devices-can-wifi-handle-smart-home/'>How many devices can Wi-Fi handle?</a></li>
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
}


def build_troubleshooting_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(TROUBLESHOOTING_PAGES)

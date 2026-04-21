from __future__ import annotations

DEVICE_PAGES = {
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
}


def build_device_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(DEVICE_PAGES)

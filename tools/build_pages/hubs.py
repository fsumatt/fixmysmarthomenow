from __future__ import annotations

HUB_DETAIL_PAGES = {
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
}


def build_hub_detail_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(HUB_DETAIL_PAGES)

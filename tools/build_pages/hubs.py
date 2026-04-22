from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card

HUB_DETAIL_PAGES = {
    "/hubs/best-hub-for-mixed-smart-home/": {
        "title": "Best hub for mixed smart home",
        "description": "How to choose the best hub when you have mixed devices, multiple protocols, and want reliability first.",
        "section": "Hubs",
        "body": (
        "<p>For a mixed smart home, the best hub is the one that reduces protocol sprawl and keeps automations local enough to survive cloud weirdness.</p>"
        "<h2>What matters most</h2>"
        "<ul>"
        "  <li>Strong Zigbee/Z-Wave support</li>"
        "  <li>Good local automation options</li>"
        "  <li>Stable integrations for your voice assistant and major ecosystems</li>"
        "  <li>Enough maturity that you are not beta-testing your house</li>"
        "</ul>"
        "<h2>Good hub patterns</h2>"
        "<ul>"
        "  <li><strong>One main hub + a few bridges:</strong> usually the cleanest for mixed homes.</li>"
        "  <li><strong>All-Wi-Fi + voice assistant only:</strong> simplest upfront, weakest long-term reliability.</li>"
        "  <li><strong>Home Assistant-first:</strong> most flexible, but higher setup overhead.</li>"
        "</ul>"
        "<h2>If you already know you need gear</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="mixed homes that want a strong local-control core",
            why=[
                "Best fit when you want one serious hub strategy",
                "Pairs well with bridges instead of forcing one vendor stack",
            ],
            caution="Better for people willing to spend a little setup effort up front.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want local automations without going full DIY first",
            why=[
                "Strong fit for Zigbee/Z-Wave-heavy homes",
                "Useful middle ground between simple and highly customizable",
            ],
            caution="Less beginner-soft than app-only consumer ecosystems.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Protocol comparison</a></li>"
        "  <li><a href='/products/reliable-smart-home-hubs/'>Reliable smart home hubs</a></li>"
        "</ul>"
        ),
    },
}


def build_hub_detail_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(HUB_DETAIL_PAGES)

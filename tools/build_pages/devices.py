from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card

DEVICE_PAGES = {
    "/devices/do-i-need-a-smart-home-hub/": {
        "title": "Do I need a smart home hub?",
        "description": "When a hub actually helps, when it is optional, and when skipping it creates future reliability pain.",
        "section": "Devices",
        "body": (
        "<p><strong>You need a hub when you care about reliability, mixed protocols, or local control.</strong> You can skip one for a tiny all-Wi-Fi setup, but the tradeoff is usually more cloud dependence and more long-term fragility.</p>"
        "<h2>You probably need a hub if</h2>"
        "<ul>"
        "  <li>You want Zigbee or Z-Wave devices.</li>"
        "  <li>You want automations that survive internet hiccups.</li>"
        "  <li>You are building beyond a few bulbs/plugs.</li>"
        "</ul>"
        "<h2>You can maybe skip it if</h2>"
        "<ul>"
        "  <li>You only have a handful of Wi-Fi devices.</li>"
        "  <li>You accept vendor lock-in and cloud dependency.</li>"
        "</ul>"
        "<h2>If a hub really is the right next step</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Aeotec Smart Home Hub",
            best_for="people graduating from an app-only setup into a more reliable mixed-device home",
            why=[
                "Good starting point when you need more structure without jumping to full DIY",
                "Makes sense when your current setup is small but clearly outgrowing Wi-Fi-only control",
            ],
            caution="Still best if your ecosystem expectations line up with the platform.",
            query="Aeotec Smart Home Hub",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Home Assistant Green",
            best_for="buyers who already know they want stronger local control and future flexibility",
            why=[
                "Better if you expect the setup to keep growing",
                "Stronger fit for people who care about local automations and broad integration options",
            ],
            caution="Not the lightest-weight path if you only want a couple of plugs and bulbs.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If you need the architecture answer, start with the best hub strategy guide</a></li>"
        "  <li><a href='/products/reliable-smart-home-hubs/'>If you already know you are buying, compare the shortlist of reliable hubs</a></li>"
        "</ul>"
        ),
    },
}


def build_device_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(DEVICE_PAGES)

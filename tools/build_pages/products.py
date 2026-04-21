from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card

PRODUCT_PAGES = {
    "/products/reliable-smart-home-hubs/": {
        "title": "Reliable smart home hubs",
        "description": "A curated shortlist of smart home hub strategies and hub categories that prioritize reliability over hype.",
        "section": "Products",
        "body": (
        "<p>This is not a giant hub catalog. It is the short list of hub categories worth considering if you care about stable mixed-device smart homes.</p>"
        "<h2>Recommended patterns</h2>"
        "<ul>"
        "  <li><strong>Main automation hub + bridges:</strong> best overall for mixed homes.</li>"
        "  <li><strong>Vendor hub only:</strong> fine if you stay narrow, risky if you want flexibility later.</li>"
        "  <li><strong>Voice assistant only:</strong> acceptable for very small setups, weak for serious automation.</li>"
        "</ul>"
        "<h2>Best picks by scenario</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="people who want the strongest local-control foundation without building from scratch",
            why=[
                "Excellent fit for mixed ecosystems and protocol bridges",
                "Strong long-term flexibility if the house gets more complicated",
                "Better recovery path when cloud services get weird",
            ],
            caution="More setup depth than a casual app-only smart home.",
            query="Home Assistant Green",
        )
        + product_card(
            title="Aeotec Smart Home Hub",
            best_for="SmartThings-style households that want an easier mixed-home starting point",
            why=[
                "Lower setup friction than a DIY-first stack",
                "Good for people mixing major consumer ecosystems",
                "Reasonable middle ground between flexibility and simplicity",
            ],
            caution="Not as flexible as a Home Assistant-first approach.",
            query="Aeotec Smart Home Hub",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want local automations and a serious hub without going full Home Assistant immediately",
            why=[
                "Strong local automation bias",
                "Good fit for Zigbee/Z-Wave-heavy setups",
                "Useful when reliability matters more than prettiest UI",
            ],
            caution="The interface can feel more utilitarian than beginner-friendly.",
            query="Hubitat Elevation hub",
        )
        + "</div>"
        "<h2>How to choose</h2>"
        "<ul>"
        "  <li>Buy for the protocols you actually need, not abstract future-proofing.</li>"
        "  <li>Prefer local-control options if your setup already feels fragile.</li>"
        "  <li>Do not add a vendor-specific hub unless you are comfortable staying narrower.</li>"
        "</ul>"
        "<h2>Related pages</h2>"
        "<ul>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></li>"
        "  <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Protocol comparison</a></li>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>Do I need a smart home hub?</a></li>"
        "</ul>"
        ),
    },
    "/products/reliable-smart-plugs/": {
        "title": "Reliable smart plugs",
        "description": "What actually makes a smart plug reliable, and which buying patterns avoid the usual Wi-Fi plug headaches.",
        "section": "Products",
        "body": (
        "<p>Reliable smart plugs are less about brand hype and more about <strong>protocol fit</strong>, clean onboarding, and whether they behave well in your actual ecosystem.</p>"
        "<h2>Buy based on</h2>"
        "<ul>"
        "  <li>Protocol compatibility with your hub/home</li>"
        "  <li>Stable app/onboarding flow</li>"
        "  <li>Whether you need energy monitoring</li>"
        "  <li>Whether you want to avoid stuffing more cheap clients onto Wi-Fi</li>"
        "</ul>"
        "<h2>Best picks by scenario</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="TP-Link Kasa Smart Plug Mini",
            best_for="people who need an easy Wi-Fi plug that usually onboards with less drama than no-name bargain options",
            why=[
                "Widely supported and easy to understand",
                "Good default when you are staying in a Wi-Fi-first setup",
                "Usually less flaky than random ultra-cheap plugs",
            ],
            caution="Still adds more clients to Wi-Fi, which matters in overloaded homes.",
            query="TP-Link Kasa Smart Plug Mini",
        )
        + product_card(
            title="Third Reality Zigbee Smart Plug",
            best_for="hub-first homes that want to stop piling more cheap clients onto Wi-Fi",
            why=[
                "Better fit when you already have a stable Zigbee strategy",
                "Helps move simple automations off crowded Wi-Fi",
                "Useful stepping stone toward a more reliable protocol mix",
            ],
            caution="Requires a compatible Zigbee hub or coordinator.",
            query="Third Reality Zigbee Smart Plug",
        )
        + product_card(
            title="Kasa Smart Plug with Energy Monitoring",
            best_for="buyers who want a practical plug plus basic power-use visibility",
            why=[
                "Energy monitoring can help justify which devices deserve smarter control",
                "Good for appliance-style automations and troubleshooting",
                "Familiar ecosystem for many first-time buyers",
            ],
            caution="Energy-monitoring Wi-Fi plugs are still part of your Wi-Fi load budget.",
            query="Kasa smart plug energy monitoring",
        )
        + "</div>"
        "<h2>Best pattern</h2>"
        "<p>If you already have a solid Zigbee or hub-first setup, protocol-native plugs are often better than adding more bargain Wi-Fi devices.</p>"
        "<h2>Related pages</h2>"
        "<ul>"
        "  <li><a href='/why-wont-my-smart-plug-connect-to-wifi/'>Why won't my smart plug connect to Wi-Fi?</a></li>"
        "  <li><a href='/wifi-load/too-many-smart-devices-on-wifi/'>Too many smart devices on Wi-Fi</a></li>"
        "  <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></li>"
        "</ul>"
        ),
    },
}


def build_product_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(PRODUCT_PAGES)

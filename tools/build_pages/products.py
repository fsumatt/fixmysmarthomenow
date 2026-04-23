from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card

PRODUCT_PAGES = {
    "/products/reliable-smart-home-hubs/": {
        "title": "Reliable smart home hubs",
        "description": "A curated shortlist of smart home hub strategies, real hubs, and hub-adjacent ecosystem controllers that prioritize reliability over hype.",
        "section": "Products",
        "body": (
        "<p>This should not be a random hub catalog. It should help you buy the right kind of control layer for the actual problem in your house.</p>"
        "<p class='muted'>That means separating <strong>true automation hubs</strong> from <strong>ecosystem controllers and hub-adjacent devices</strong> like Apple TV, HomePod, Echo devices, and other gear that can matter a lot without always being the main brain of the house.</p>"
        "<h2>Start with the right pattern, not the right box</h2>"
        "<ul>"
        "  <li><strong>Main automation hub + a few bridges:</strong> best overall for mixed homes.</li>"
        "  <li><strong>Vendor or ecosystem controller only:</strong> fine if you stay narrow, risky if the house keeps growing.</li>"
        "  <li><strong>Voice assistant only:</strong> acceptable for very small setups, usually weak for serious automation.</li>"
        "</ul>"
        "<h2>True hubs for mixed homes</h2>"
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
        "<h2>Hub-adjacent ecosystem controllers that can still matter</h2>"
        "<p>These are not always the right answer to a whole-house coordination problem, but they absolutely belong in the buying conversation because they shape what Apple Home, Alexa, and Google Home can really do.</p>"
        + "<div class='grid'>"
        + product_card(
            title="Apple TV 4K",
            best_for="Apple-heavy homes that want a stronger Apple Home experience and better Home hub behavior",
            why=[
                "Useful when the home is strongly Apple-shaped",
                "Can matter a lot for Apple Home responsiveness and remote access behavior",
                "Better thought of as Apple ecosystem infrastructure than as a universal mixed-home hub",
            ],
            caution="Still not automatically the best main automation brain for a mixed smart home.",
            query="Apple TV 4K",
        )
        + product_card(
            title="HomePod mini",
            best_for="buyers who want Apple Home convenience and Thread-border-router-style ecosystem support in smaller Apple homes",
            why=[
                "Good fit when Apple Home is the main user-facing experience",
                "Useful for voice control plus Apple ecosystem smart-home roles",
                "Helps more as Apple-home infrastructure than as a full mixed-home hub replacement",
            ],
            caution="Best when the house is still relatively Apple-shaped.",
            query="HomePod mini",
        )
        + product_card(
            title="Echo (4th Gen)",
            best_for="Alexa-heavy homes where Echo is part of the control layer and ecosystem support story",
            why=[
                "Useful when Alexa is the main convenience layer",
                "Can matter for newer Alexa ecosystem smart-home roles",
                "Best understood as hub-adjacent control infrastructure, not always the whole answer",
            ],
            caution="Still usually not the best long-term main coordination layer for a mixed home by itself.",
            query="Echo 4th generation",
        )
        + "</div>"
        "<h2>What is missing today, and where this page should grow</h2>"
        "<p>The site should eventually add stronger product coverage for:</p>"
        "<ul>"
        "  <li>smart dimmers and switches</li>"
        "  <li>doorbells and ecosystem-specific video entry gear</li>"
        "  <li>bridge-dependent device families</li>"
        "  <li>compatibility tables showing which hub or ecosystem handles which gear well</li>"
        "  <li>infographics that explain true hub vs ecosystem controller vs bridge roles</li>"
        "</ul>"
        "<p>Those expansions are worth doing because they support better buying decisions, not because the site needs a bloated catalog.</p>"
        "<h2>How to choose</h2>"
        "<ul>"
        "  <li>Buy for the protocols and ecosystem roles you actually need, not abstract future-proofing.</li>"
        "  <li>Prefer local-control options if your setup already feels fragile.</li>"
        "  <li>Do not assume Apple TV, HomePod, Echo, or Nest hardware automatically replace a real mixed-home hub.</li>"
        "  <li>Use ecosystem infrastructure when the house is still narrow, and a true hub when the house has become a real coordination problem.</li>"
        "</ul>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If you still are comparing architectures, start with the best hub strategy guide</a></li>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>If the real question is whether your current ecosystem is already enough, use the cross-ecosystem decision guide</a></li>"
        "  <li><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>If terminology confusion is muddying the buying decision, clean that up first</a></li>"
        "</ul>"
        ),
    },
    "/products/reliable-smart-plugs/": {
        "title": "Reliable smart plugs",
        "description": "What actually makes a smart plug reliable, and which buying patterns avoid the usual Wi-Fi plug headaches.",
        "section": "Products",
        "body": (
        "<p>Reliable smart plugs are less about brand hype and more about <strong>protocol fit</strong>, clean onboarding, and whether they behave well in your actual ecosystem.</p>"
        "<p class='muted'>If the real problem is overloaded Wi-Fi or the wrong protocol mix, buying another cheap plug will not save the setup.</p>"
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
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/why-wont-my-smart-plug-connect-to-wifi/'>If setup keeps failing, start with the smart plug troubleshooting guide</a></li>"
        "  <li><a href='/wifi-load/too-many-smart-devices-on-wifi/'>If Wi-Fi itself is strained, check whether too many devices are on the network</a></li>"
        "  <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>If onboarding is flaky, tighten 2.4 GHz policy first</a></li>"
        "</ul>"
        ),
    },
}


def build_product_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(PRODUCT_PAGES)

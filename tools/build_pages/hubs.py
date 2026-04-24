from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card

HUB_DETAIL_PAGES = {
    "/hubs/do-i-need-more-than-one-smart-home-hub/": {
        "title": "Do I need more than one smart home hub?",
        "description": "When multiple hubs or bridges are justified, when one main hub is better, and how to avoid turning a mixed smart home into a control mess.",
        "section": "Hubs",
        "body": (
        "<p><strong>Usually, no.</strong> Most homes are more reliable with <strong>one main hub plus only the bridges or ecosystem pieces that are actually necessary</strong>. Multiple hubs become justified when they solve a real protocol, vendor, or scale problem, not when you are trying to patch over weak architecture with more boxes.</p>"
        "<h2>The short rule</h2>"
        "<p>If you are asking this before the house is complicated, start with one serious coordination layer. If you are asking because the house is already mixed, the goal is still not to collect hubs. The goal is to decide which device should be the <strong>main coordinator</strong> and which extra pieces are just supporting roles.</p>"
        "<h2>When one hub is usually enough</h2>"
        "<ul>"
        "  <li>You want one place to manage automations and understand failures.</li>"
        "  <li>Your devices can mostly route through one strong hub platform.</li>"
        "  <li>You are trying to reduce vendor-app sprawl, not preserve all of it forever.</li>"
        "  <li>You care more about long-term reliability than about every device living in its native app first.</li>"
        "</ul>"
        "<p>For most mixed homes, <strong>one main hub + a few bridges</strong> is still the cleanest pattern. That keeps the house understandable while leaving room for protocol-specific gear where it genuinely helps.</p>"
        "<h2>When more than one hub or bridge is justified</h2>"
        "<ul>"
        "  <li><strong>Protocol specialization:</strong> you may keep one main hub while retaining a vendor bridge that handles a device family particularly well.</li>"
        "  <li><strong>Ecosystem lock-in you cannot avoid:</strong> some devices are simply happier behind their own bridge, and forcing everything into one layer can make the home worse.</li>"
        "  <li><strong>Migration periods:</strong> you may temporarily run more than one hub while moving away from a weaker architecture.</li>"
        "  <li><strong>Very large or unusual setups:</strong> rare in normal homes, but sometimes separate roles are justified by scale or edge-case hardware support.</li>"
        "</ul>"
        "<h2>When multiple hubs are a bad sign</h2>"
        "<ul>"
        "  <li>You are adding a second or third hub because you still do not know which one actually owns automations.</li>"
        "  <li>You keep solving device-specific frustration by adding another control layer instead of fixing protocol fit or Wi-Fi policy.</li>"
        "  <li>You now have several apps, several routines systems, and no clear source of truth.</li>"
        "  <li>You are treating Alexa, Google Home, Apple Home, and multiple vendor bridges as equal brains instead of deciding which layer is primary.</li>"
        "</ul>"
        "<p>That pattern usually does not create resilience. It creates confusion.</p>"
        "<h2>The better architecture pattern</h2>"
        "<p>The durable answer for most homes is this:</p>"
        "<ul>"
        "  <li><strong>one main hub</strong> for coordination and automations</li>"
        "  <li><strong>only the bridges you genuinely need</strong> for specific device families</li>"
        "  <li><strong>one top-layer ecosystem</strong> for voice control and convenience, not five competing control surfaces</li>"
        "</ul>"
        "<p>That is how you keep a mixed home flexible without making it mysterious.</p>"
        "<h2>How to decide whether the extra box earns its keep</h2>"
        "<ul>"
        "  <li>Does it add unique protocol or device support you actually need?</li>"
        "  <li>Does it improve reliability more than it increases management overhead?</li>"
        "  <li>Will it remain a supporting bridge, or is it quietly becoming a second competing hub?</li>"
        "  <li>If you removed it six months from now, would the house become simpler or collapse?</li>"
        "</ul>"
        "<p>If the main benefit is just that setup felt easier in one app on a Tuesday, that usually is not a strong enough reason.</p>"
        "<h2>When buying a stronger main hub is better than adding another weak one</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="homes that have drifted into bridge sprawl and need one stronger main coordination layer",
            why=[
                "Useful when the real fix is consolidating smart-home ownership instead of adding yet another app-first hub",
                "Strong fit for mixed homes that want one clear place to reason about automations and integrations",
            ],
            caution="Best when you actually want one serious hub strategy, not just another device to stack beside the old ones.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want one dedicated hub instead of letting multiple partial hubs compete forever",
            why=[
                "Good fit when the home needs clearer ownership and better local coordination",
                "Useful middle ground if you want a real hub without rebuilding everything around the most DIY path",
            ],
            caution="Still works best as the main hub, not as one more layer in an already messy stack.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Bottom line</h2>"
        "<p>You only need more than one smart home hub when the extra layer solves a real architecture problem. In most homes, the better answer is one main hub, a few justified bridges, and a clear understanding of which layer is actually in charge.</p>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If you need to choose that main coordination layer, start with the best hub for a mixed smart home</a></li>"
        "  <li><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>If the confusion is really about roles, separate hub vs bridge vs controller vs border router first</a></li>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>If voice ecosystems are part of the confusion, use the cross-ecosystem hub decision guide</a></li>"
        "  <li><a href='/products/reliable-smart-home-hubs/'>If the real next step is buying one stronger hub instead of adding more weak layers, compare reliable hub options</a></li>"
        "</ul>"
        ),
    },
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
        "<h2>If a stronger hub really is the fix</h2>"
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
        "  <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>If you still need to decide the radio stack, compare the main protocols</a></li>"
        "  <li><a href='/products/reliable-smart-home-hubs/'>If you are ready to buy, compare the shortlist of reliable hub options</a></li>"
        "</ul>"
        ),
    },
}


def build_hub_detail_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(HUB_DETAIL_PAGES)

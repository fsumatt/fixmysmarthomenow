from __future__ import annotations

from .shared import AFFILIATE_INLINE_DISCLOSURE, product_card, protocol_stack_visual

PROTOCOL_PAGES = {
    "/protocols/matter-vs-thread/": {
        "title": "Matter vs Thread",
        "description": "What Matter and Thread each do, why they are not the same thing, and how that confusion creates bad smart home buying decisions.",
        "section": "Protocols",
        "body": """
        <p><strong>Matter and Thread are not competitors.</strong> Matter is the application standard that helps devices work across ecosystems. Thread is one possible network layer some Matter devices use underneath. Confusing them leads people to buy the wrong gear and expect the wrong fix.</p>
        <h2>Matter answers</h2>
        <ul>
          <li>Will this device work across Apple, Google, Amazon, or Samsung more cleanly?</li>
          <li>Can onboarding and interoperability be less vendor-specific?</li>
        </ul>
        <h2>Thread answers</h2>
        <ul>
          <li>How are low-power devices networking locally?</li>
          <li>Do I have a stable border router and enough ecosystem support for this mesh?</li>
        </ul>
        <h2>What goes wrong in real homes</h2>
        <ul>
          <li>People buy a Matter device and assume they automatically have Thread.</li>
          <li>People hear "Thread" and assume it guarantees broad cross-platform compatibility.</li>
          <li>People blame Matter when the actual weak point is a flaky Thread border router.</li>
        </ul>
        <h2>Best simple rule</h2>
        <p>If you care about <strong>cross-platform compatibility</strong>, think about Matter. If you care about <strong>local mesh transport</strong>, think about Thread. Some devices use both, but they solve different layers of the problem.</p>
        <h2>Next steps</h2>
        <ul>
          <li><a href='/protocols/thread-vs-zigbee/'>If the real decision is about the radio layer, compare Thread and Zigbee</a></li>
          <li><a href='/protocols/matter-vs-zigbee/'>If the buying choice is really Matter versus a mature Zigbee ecosystem, compare those directly</a></li>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>If you want the full architecture picture, compare all the main options</a></li>
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
        <h2>Next steps</h2>
        <ul>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>If you want the broader protocol decision, compare all the main options</a></li>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If this choice points toward a central controller, pick the right hub strategy</a></li>
        </ul>
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
        <h2>Next steps</h2>
        <ul>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>If you want the full protocol picture, compare all the main options</a></li>
          <li><a href='/devices/do-i-need-a-smart-home-hub/'>If this decision changes your architecture, decide whether a hub belongs in the setup</a></li>
        </ul>
        """,
    },
    "/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/": {
        "title": "Zigbee vs Z-Wave vs Thread vs Matter",
        "description": "Which smart home protocol is actually best for reliability, mixed ecosystems, and future flexibility.",
        "section": "Protocols",
        "body": (
        "<p><strong>The short version:</strong> Zigbee is still the best overall workhorse for large device counts, Z-Wave is strong for locks/sensors in the right ecosystem, Thread is promising but still uneven, and Matter is a transport layer story more than a magic reliability fix.</p>"
        + protocol_stack_visual()
        + "<h2>Use Zigbee when</h2>"
        "<ul><li>You want lots of inexpensive sensors/plugs and a strong mesh.</li><li>You can commit to a good hub/coordinator.</li></ul>"
        "<h2>Use Z-Wave when</h2>"
        "<ul><li>You care about locks, security devices, and a more curated device ecosystem.</li><li>You are okay with slightly higher device cost.</li></ul>"
        "<h2>Use Thread when</h2>"
        "<ul><li>You already have strong Apple/Google/Nest border router support.</li><li>You want modern low-power networking, but you accept ecosystem rough edges.</li></ul>"
        "<h2>What Matter actually changes</h2>"
        "<p>Matter helps interoperability and onboarding, but it does <strong>not</strong> automatically fix weak Wi-Fi, poor border routers, or bad device firmware.</p>"
        "<h2>If buying gear is actually the right next step</h2>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="buyers who want a strong mixed-protocol base after deciding Wi-Fi-only is not enough",
            why=[
                "Good fit when protocol choice points toward a real hub strategy",
                "Better long-term flexibility for mixed ecosystems",
            ],
            caution="Best for people comfortable with a more serious smart-home foundation.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Aeotec Smart Home Hub",
            best_for="people who want an easier bridge into a hub-first setup",
            why=[
                "Simpler jump than a more DIY-first platform",
                "Works well when the problem is ecosystem sprawl more than deep customization",
            ],
            caution="Less flexible than a Home Assistant-first approach.",
            query="Aeotec Smart Home Hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If protocol sprawl is the real issue, pick a better hub strategy</a></li>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>If you still are not sure a hub belongs here, decide that first</a></li>"
        "</ul>"
        ),
    },
}


def build_protocol_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(PROTOCOL_PAGES)

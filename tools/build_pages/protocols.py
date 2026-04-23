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
        "  <li><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>If the terms themselves are the real problem, start with the terminology guide</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If protocol sprawl is the real issue, pick a better hub strategy</a></li>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>If you still are not sure a hub belongs here, decide that first</a></li>"
        "</ul>"
        ),
    },
    "/protocols/hub-vs-bridge-vs-controller-vs-border-router/": {
        "title": "Hub vs bridge vs controller vs border router",
        "description": "What hub, bridge, controller, and Thread border router actually mean, where they overlap, and which one you really need in a smart home.",
        "section": "Protocols",
        "body": (
        "<p><strong>Hub, bridge, controller, and border router are not interchangeable terms, even though smart home marketing and forum advice treat them like they are.</strong> If you mix them up, you end up buying the wrong gear, blaming the wrong layer, and building a house that feels more mysterious than it should.</p>"
        "<h2>Why these terms get mixed up so easily</h2>"
        "<p>Smart homes have too many overlapping roles. One device can be a speaker, a Matter controller, and a Thread border router. Another can be called a hub even though it mostly behaves like a bridge. Another can feel like the center of the house because it is where you tap buttons, even if it is not the place where the real coordination logic should live.</p>"
        "<p>That overlap is why people ask questions like “Is Alexa a hub?” or “Do I already have a hub if I own a HomePod?” Those are reasonable questions. The problem is that the right answer depends on which job you actually mean.</p>"
        "<h2>What a hub is</h2>"
        "<p>In practical smart-home terms, a <strong>hub</strong> is the main coordination layer. It is the place that owns device relationships, automations, protocol strategy, and long-term control more seriously than a thin app-only setup does.</p>"
        "<p>A real hub matters most once the house becomes a mixed system rather than just a few gadgets. That is why hubs become more valuable as the home grows more complex.</p>"
        "<ul>"
        "  <li>A hub is about <strong>coordination</strong>.</li>"
        "  <li>A hub is often where automations become more reliable and more structured.</li>"
        "  <li>A hub is what you add when the house has outgrown being managed only through vendor apps and voice routines.</li>"
        "</ul>"
        "<h2>What a bridge is</h2>"
        "<p>A <strong>bridge</strong> is usually a translator or protocol-specific middle layer. It helps one family of devices show up inside another system, but it is not always the best candidate to become the whole house’s central brain.</p>"
        "<p>Bridges are common because many device ecosystems were designed to solve their own compatibility problem first, not your whole-home architecture problem.</p>"
        "<ul>"
        "  <li>A bridge is about <strong>translation</strong>.</li>"
        "  <li>It often exists so one vendor’s devices can surface inside a broader ecosystem.</li>"
        "  <li>You can have several bridges in one house without any of them being the real central hub.</li>"
        "</ul>"
        "<h2>What a controller is</h2>"
        "<p>A <strong>controller</strong> is a broader term, which is why it causes so much confusion. Sometimes it means the thing issuing commands. In Matter discussions, it often means the <strong>Matter controller</strong>, the role that commissions devices and helps manage them inside an ecosystem.</p>"
        "<p>That matters because a controller role can be important without automatically solving every other smart-home problem. A Matter controller is useful, but useful is not the same thing as being your ideal whole-house hub strategy.</p>"
        "<ul>"
        "  <li>A controller is about <strong>management and command authority</strong>.</li>"
        "  <li>A Matter controller helps with device onboarding and ecosystem-level control.</li>"
        "  <li>It may be part of a strong setup without being the whole answer by itself.</li>"
        "</ul>"
        "<h2>What a Thread border router is</h2>"
        "<p>A <strong>Thread border router</strong> connects a Thread mesh to the rest of your network. It is important, but it solves a different layer of the problem than a hub does.</p>"
        "<p>This is one of the most common modern points of confusion. People hear that a device is a Thread border router and assume that means it is now the smart-home brain. Usually it just means it is handling one important networking role in a larger architecture.</p>"
        "<ul>"
        "  <li>A border router is about <strong>network transport between Thread and your wider network</strong>.</li>"
        "  <li>It helps Thread devices communicate more usefully.</li>"
        "  <li>It does not automatically replace a central coordination layer.</li>"
        "</ul>"
        "<h2>Where voice assistants fit</h2>"
        "<p>Alexa, Google Home, and Apple Home all make this harder because they can overlap with several of these roles at once. They can be the visible control surface, participate in controller-like behavior, and sometimes participate in newer network roles too.</p>"
        "<p>But the key distinction still holds: a device can help with smart-home control without being the best answer to the question “What should really coordinate this house?” That is why many better setups become <strong>ecosystem on top, real hub underneath</strong>.</p>"
        "<h2>Real-world examples</h2>"
        "<ul>"
        "  <li><strong>Home Assistant Green or Hubitat:</strong> usually thought of as true hubs because they are trying to own the broader coordination problem.</li>"
        "  <li><strong>Philips Hue Bridge:</strong> classic example of a bridge that is very useful without necessarily being the ideal whole-home core.</li>"
        "  <li><strong>HomePod, Apple TV, Echo, or Nest devices:</strong> may take on controller or border-router-like roles, but that does not automatically make them the strongest central architecture answer for every home.</li>"
        "</ul>"
        "<h2>Which problem each one solves</h2>"
        "<p>If you are confused about what to buy, this is the practical shortcut:</p>"
        "<ul>"
        "  <li>If your problem is <strong>whole-home coordination</strong>, you are probably thinking about a hub.</li>"
        "  <li>If your problem is <strong>making one family of devices show up somewhere else</strong>, you are probably thinking about a bridge.</li>"
        "  <li>If your problem is <strong>who commissions and manages Matter devices</strong>, you are thinking about a controller.</li>"
        "  <li>If your problem is <strong>how Thread devices reach the rest of the network</strong>, you are thinking about a border router.</li>"
        "</ul>"
        "<h2>How to tell what you actually need</h2>"
        "<p>Do not start by asking which box sounds most advanced. Start by asking which layer is actually failing.</p>"
        "<ul>"
        "  <li>If devices are visible but coordination is messy, you may need a better hub.</li>"
        "  <li>If one vendor family is isolated, you may need a bridge.</li>"
        "  <li>If Matter onboarding is the problem, you may be missing the right controller path.</li>"
        "  <li>If Thread devices are unstable or unreachable, you may need to think about border-router quality and placement.</li>"
        "</ul>"
        "<p>That is the bigger lesson here: these roles overlap, but they are not substitutes for one another. Once you separate them, smart-home decisions get much easier.</p>"
        "<h2>When buying a real hub is actually justified</h2>"
        "<p>If this terminology cleanup makes one thing clearer, it should be this: the word <em>hub</em> should be earned. You buy a real hub when the house has a real coordination problem, not just because a page about terminology made a new box sound attractive.</p>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="homes that have moved past terminology confusion into a real need for one serious coordination layer",
            why=[
                "Good fit when the house needs a real hub, not just another bridge or app layer",
                "Useful when multiple ecosystems and protocols now need one cleaner architecture",
                "Strong long-term answer for buyers who have outgrown app-only control",
            ],
            caution="More system than you need if your home is still simple and healthy.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want a dedicated hub after realizing controllers, bridges, and border routers are not the same thing",
            why=[
                "Good middle ground when the real missing piece is a stronger coordination layer",
                "Helps mixed homes move beyond vendor-app sprawl",
                "Makes sense when you want a deliberate hub without overcomplicating the whole house",
            ],
            caution="Still should solve a real architecture problem, not just satisfy curiosity.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>If you are still deciding whether you need a hub at all, use the broader hub decision page</a></li>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>If your confusion started with Alexa, Google Home, or Apple Home, use the cross-ecosystem decision guide</a></li>"
        "  <li><a href='/protocols/matter-vs-thread/'>If the real confusion is Matter versus Thread, compare those directly</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If you already know the house needs stronger coordination, compare the best hub strategy</a></li>"
        "</ul>"
        ),
    },
}


def build_protocol_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(PROTOCOL_PAGES)

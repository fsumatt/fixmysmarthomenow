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
        "<h2>Where Alexa, Google Home, and Apple Home fit</h2>"
        "<p>Voice-assistant ecosystems can cover basic control, but they are not automatically the same thing as a serious mixed-home hub strategy.</p>"
        "<ul>"
        "  <li><a href='/devices/is-alexa-a-smart-home-hub/'>See what Alexa devices can and cannot do as a hub</a></li>"
        "  <li>Expect the same question to matter for Google Home and Apple Home too, because those ecosystems blur the line between voice control and actual hub behavior.</li>"
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
        "  <li><a href='/devices/is-alexa-a-smart-home-hub/'>If your question is really about Echo devices, start with whether Alexa counts as a hub</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If you need the architecture answer, start with the best hub strategy guide</a></li>"
        "  <li><a href='/products/reliable-smart-home-hubs/'>If you already know you are buying, compare the shortlist of reliable hubs</a></li>"
        "</ul>"
        ),
    },
    "/devices/is-alexa-a-smart-home-hub/": {
        "title": "Is Alexa a smart home hub?",
        "description": "What Echo and Alexa can really do as a hub, where they help, and when you still need a more serious smart home controller.",
        "section": "Devices",
        "body": (
        "<p><strong>Alexa can act like part of a smart home hub setup, but that is not the same thing as Alexa being a full smart home hub.</strong> In most homes, Alexa is best understood as a voice-control layer, routine engine, and ecosystem front end, not the main reliability-first automation brain.</p>"
        "<h2>Short answer</h2>"
        "<p>If your setup is small, mainstream, and mostly about convenience, Alexa may be enough for now. If your house is growing into a mixed smart home with more devices, more protocols, and more failure points, Alexa usually works better <strong>on top of</strong> a real hub strategy than as the only coordinator.</p>"
        "<h2>Why this question is so confusing</h2>"
        "<p>People use the word <em>hub</em> to mean several different things at once. Sometimes they mean the app where devices show up. Sometimes they mean the thing that runs automations. Sometimes they mean a radio coordinator for Zigbee, a Matter controller, or a Thread border router. Alexa touches some of those roles, which is why the answer is not a simple yes or no.</p>"
        "<p>The practical problem is that many buyers hear “Echo works with smart home devices” and assume that means “Echo replaces a real hub.” Sometimes that is true enough for a tiny setup. Often it is not true enough once reliability starts to matter.</p>"
        "<h2>What Alexa actually does well</h2>"
        "<ul>"
        "  <li><strong>Voice control:</strong> Alexa is excellent as a simple control layer for lights, plugs, routines, and quick household commands.</li>"
        "  <li><strong>Basic coordination:</strong> For small homes, Alexa routines can connect a few events and actions without much architecture planning.</li>"
        "  <li><strong>Ecosystem convenience:</strong> A lot of mainstream gear is designed to work with Alexa quickly, which makes setup feel hub-like even when the deeper logic still lives elsewhere.</li>"
        "  <li><strong>Front-end role:</strong> Alexa often works best as the voice and convenience surface for a setup that may also include a stronger hub or bridge behind the scenes.</li>"
        "</ul>"
        "<h2>Why people call Alexa a hub</h2>"
        "<ul>"
        "  <li>Some Echo devices can discover and control certain smart-home devices directly.</li>"
        "  <li>Alexa routines make one app feel like the center of the house.</li>"
        "  <li>Some Echo models can participate in Matter and Thread-related roles, which makes the terminology even messier.</li>"
        "</ul>"
        "<p>That does not mean Alexa automatically becomes the best long-term smart-home core. It means Alexa overlaps with hub behavior in specific ways.</p>"
        "<h2>What Alexa is not especially good at</h2>"
        "<ul>"
        "  <li><strong>Owning a mixed-home architecture:</strong> Alexa is not the cleanest place to reason about a house that mixes vendors, bridges, radios, and edge cases.</li>"
        "  <li><strong>Deep local automation:</strong> If you care about automations surviving cloud weirdness, internet hiccups, or vendor outages, Alexa is not usually the strongest foundation.</li>"
        "  <li><strong>Explaining the failure layer:</strong> When devices go offline, routines fail, or Matter behaves strangely, Alexa rarely gives you the kind of architecture-level clarity a stronger hub strategy can provide.</li>"
        "  <li><strong>Protocol-first control:</strong> If your real issue is Zigbee, Z-Wave, Thread, Wi-Fi load, or bridge sprawl, Alexa can mask the problem without really organizing it.</li>"
        "</ul>"
        "<h2>When Alexa is enough</h2>"
        "<p>Alexa is often enough when the house is still small and the goals are modest. That usually means:</p>"
        "<ul>"
        "  <li>a handful of lights, plugs, speakers, or simple routines</li>"
        "  <li>mostly mainstream Wi-Fi devices or devices already designed to live comfortably inside the Alexa ecosystem</li>"
        "  <li>no strong requirement for advanced local automation or protocol flexibility</li>"
        "  <li>high tolerance for cloud dependence as the price of convenience</li>"
        "</ul>"
        "<p>In that kind of setup, buying another box too early can create more complexity than value.</p>"
        "<h2>When Alexa stops being enough</h2>"
        "<p>Alexa starts to feel thin when the system becomes less like a convenience stack and more like an actual infrastructure problem.</p>"
        "<ul>"
        "  <li>You want one stable place to manage a mixed smart home across brands and protocols.</li>"
        "  <li>You are starting to use Zigbee, Z-Wave, bridges, or multiple ecosystems at once.</li>"
        "  <li>You care about local control when the internet or vendor cloud is flaky.</li>"
        "  <li>You need automations more complex than simple routines handle comfortably.</li>"
        "  <li>You keep asking whether the problem is Alexa, Wi-Fi, Matter, the bridge, or the device itself.</li>"
        "</ul>"
        "<p>That last one matters a lot. Once the house gets complicated, the winning move is usually not “make Alexa do more.” It is “give Alexa a better architecture to sit on top of.”</p>"
        "<h2>Alexa vs a real smart home hub</h2>"
        "<p>The easiest way to think about it is this: Alexa is usually the <strong>control surface</strong>, while a real hub is the <strong>reliability layer</strong>. A real hub is where you start caring about device orchestration, local behavior, protocol depth, and long-term sanity.</p>"
        "<p>That is why many of the best practical setups become <strong>one real hub plus Alexa on top</strong>, not Alexa as the only coordinator. Alexa remains valuable, but it stops carrying the full architectural load.</p>"
        "<h2>What Matter and Thread change, and what they do not</h2>"
        "<p>This is where the answer gets even more slippery. Some Echo devices participate in newer smart-home roles that make Alexa feel more hub-like. But those roles do not magically turn every Alexa setup into a complete smart-home foundation.</p>"
        "<ul>"
        "  <li><strong>Matter</strong> can improve interoperability, but it does not fix weak Wi-Fi, bad device firmware, or a messy overall architecture.</li>"
        "  <li><strong>Thread</strong> can improve parts of the transport layer, but that still is not the same thing as having one strong place to manage a mixed home.</li>"
        "  <li><strong>Alexa compatibility</strong> is not the same thing as long-term reliability.</li>"
        "</ul>"
        "<p>If your house keeps working because it is simple, Alexa may be enough. If your house keeps breaking because it is complicated, Matter and Thread support alone usually do not solve the deeper coordination problem.</p>"
        "<h2>Best practical setup patterns</h2>"
        "<p>For most people, one of these patterns is the right mental model:</p>"
        "<ul>"
        "  <li><strong>Alexa-only convenience setup:</strong> fine for small, mainstream homes that do not need much depth.</li>"
        "  <li><strong>Real hub + Alexa front end:</strong> best for mixed-device homes that want better reliability while keeping easy voice control.</li>"
        "  <li><strong>Bridge-heavy setup with Alexa on top:</strong> sometimes workable, but can get messy fast if no stronger central architecture exists.</li>"
        "</ul>"
        "<p>If you already feel the house becoming messy, the second pattern is usually the one worth building toward.</p>"
        "<h2>When buying a real hub is actually justified</h2>"
        "<p>This site should not push a hub just because “more gear” sounds like progress. Buying one is justified when it solves a real architecture problem, not when the current setup is still simple and healthy.</p>"
        "<p>A stronger hub is usually justified when Alexa is still useful, but no longer enough as the main smart-home brain.</p>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="homes that want Alexa voice control on top of a stronger local automation core",
            why=[
                "Useful when Alexa is convenient but not enough as the main smart-home brain",
                "Strong fit for mixed-device homes that keep growing",
                "Better when the house needs one serious coordination layer instead of more app sprawl",
            ],
            caution="More architecture than you need if the setup is still tiny and simple.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want a real hub without giving up Alexa as the front-end voice layer",
            why=[
                "Good middle ground when routines and direct integrations are getting messy",
                "Stronger long-term fit than staying fully app-only",
                "Makes more sense when you want a real hub but not a full DIY-first stack",
            ],
            caution="Still a step up in complexity from pure Echo-only control.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Bottom line</h2>"
        "<p>Alexa can be part of a hub strategy, and for some small homes it is enough. But in serious mixed-home setups, Alexa is usually more valuable as the voice and convenience layer than as the only smart-home core. If your question is really about reliability, protocol sprawl, and long-term control, the better answer is often not “make Alexa the hub.” It is “keep Alexa, but put something stronger underneath it.”</p>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>If you are still deciding whether you need a hub at all, start there</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If Alexa is not enough anymore, compare stronger mixed-home hub strategies</a></li>"
        "  <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>If protocol confusion is part of this, compare the main smart-home stacks</a></li>"
        "</ul>"
        ),
    },
}


def build_device_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(DEVICE_PAGES)

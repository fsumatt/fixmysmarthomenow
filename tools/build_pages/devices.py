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
        "<p><strong>Alexa can act like part of a smart home hub setup, but it is not the same thing as having a full reliability-first hub.</strong> In most homes, Alexa is best understood as a voice-control layer plus a limited ecosystem controller, not the main automation brain.</p>"
        "<h2>Short answer</h2>"
        "<p>If you only want simple routines, voice control, and a mostly Amazon-shaped setup, Alexa may be enough. If you want mixed protocols, deeper automations, and fewer cloud-related surprises, Alexa usually is not enough by itself.</p>"
        "<h2>Why people call Alexa a hub</h2>"
        "<ul>"
        "  <li>Some Echo devices can discover and control certain smart-home devices directly.</li>"
        "  <li>Alexa routines make the setup feel hub-like because one app can coordinate multiple actions.</li>"
        "  <li>Matter support and Thread border-router behavior on some Echo models make the lines even blurrier.</li>"
        "</ul>"
        "<h2>What Alexa is actually good at</h2>"
        "<ul>"
        "  <li>Voice control for lights, plugs, and common routines.</li>"
        "  <li>Simple household automations where cloud dependence is acceptable.</li>"
        "  <li>Acting as a convenient front door to a setup that may also include a real hub behind the scenes.</li>"
        "</ul>"
        "<h2>Where Alexa stops being enough</h2>"
        "<ul>"
        "  <li>You want one stable place to manage a mixed smart home across brands and protocols.</li>"
        "  <li>You care about local control when the internet or vendor cloud is flaky.</li>"
        "  <li>You need more complex automations than basic routines handle comfortably.</li>"
        "  <li>You keep asking whether the problem is Alexa, Wi-Fi, Matter, or the device itself.</li>"
        "</ul>"
        "<h2>Alexa hub vs real hub</h2>"
        "<p>The practical difference is that Alexa is often the control surface, while a real hub is the reliability layer. That is why many better setups end up as <strong>one real hub plus Alexa on top</strong>, not Alexa as the only coordinator.</p>"
        "<h2>When Alexa is probably enough</h2>"
        "<ul>"
        "  <li>You have a small home with a handful of devices.</li>"
        "  <li>You are staying mostly inside the Alexa-compatible mainstream.</li>"
        "  <li>You want convenience more than deep automation.</li>"
        "</ul>"
        "<h2>When to add a stronger hub</h2>"
        "<ul>"
        "  <li>You are mixing device types, ecosystems, and protocols.</li>"
        "  <li>You want Zigbee, Z-Wave, or stronger local automation behavior.</li>"
        "  <li>You want Alexa to remain the voice layer, not the entire architecture.</li>"
        "</ul>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="homes that want Alexa voice control on top of a stronger local automation core",
            why=[
                "Useful when Alexa is convenient but not enough as the main smart-home brain",
                "Strong fit for mixed-device homes that keep growing",
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
            ],
            caution="Still a step up in complexity from pure Echo-only control.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
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

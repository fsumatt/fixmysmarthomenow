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
        "  <li><a href='/devices/is-google-home-a-smart-home-hub/'>See where Google Home and Nest devices overlap with hub behavior</a></li>"
        "  <li><a href='/devices/is-apple-home-a-smart-home-hub/'>See how Apple Home, HomePod, and Apple TV fit into the same question</a></li>"
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
        "  <li><a href='/devices/is-google-home-a-smart-home-hub/'>If the same question applies to Nest speakers or Google Home, compare that path too</a></li>"
        "  <li><a href='/devices/is-apple-home-a-smart-home-hub/'>If you are thinking in HomeKit or Apple Home terms, use the Apple-specific guide</a></li>"
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
        "  <li><a href='/devices/is-google-home-a-smart-home-hub/'>If the same question exists in a Google/Nest home, compare that version too</a></li>"
        "  <li><a href='/devices/is-apple-home-a-smart-home-hub/'>If your house is more Apple-shaped, compare how Apple Home fits the same problem</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If Alexa is not enough anymore, compare stronger mixed-home hub strategies</a></li>"
        "  <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>If protocol confusion is part of this, compare the main smart-home stacks</a></li>"
        "</ul>"
        ),
    },
    "/devices/is-google-home-a-smart-home-hub/": {
        "title": "Is Google Home a smart home hub?",
        "description": "What Google Home and Nest devices really do as a hub, where they help, and when you still need a stronger smart home controller.",
        "section": "Devices",
        "body": (
        "<p><strong>Google Home can feel like a smart home hub, but it is usually better understood as a control layer plus a partial ecosystem controller than as the main automation core.</strong> In a small home that may be enough. In a mixed smart home, it often is not.</p>"
        "<h2>Short answer</h2>"
        "<p>If your setup is mostly about voice control, a few routines, and mainstream compatibility, Google Home may be enough for now. If you want deeper reliability, more protocol flexibility, and one cleaner place to manage a growing system, Google Home usually works better as the interface on top of a stronger architecture.</p>"
        "<h2>Why people call Google Home a hub</h2>"
        "<p>Google Home and Nest devices sit in the middle of a lot of smart-home actions. Devices appear in the app, voice commands flow through one assistant, and automations can make the whole setup feel centralized. Add Matter and Thread language on top, and it is easy to assume Google Home is automatically the hub.</p>"
        "<p>The confusion is understandable because Google Home really does overlap with hub behavior in places. The problem is that overlap is not the same thing as being the strongest long-term smart-home brain.</p>"
        "<h2>What Google Home actually does well</h2>"
        "<ul>"
        "  <li><strong>Voice and app control:</strong> Google Home is good at making a broad set of devices feel reachable from one place.</li>"
        "  <li><strong>Simple household automation:</strong> For lighter setups, routines and app-level coordination are often good enough.</li>"
        "  <li><strong>Ecosystem convenience:</strong> Nest and Google devices often reduce friction for mainstream smart-home workflows.</li>"
        "  <li><strong>Front-end usability:</strong> Google Home can be a very good convenience layer even when a stronger hub is doing the deeper work underneath.</li>"
        "</ul>"
        "<h2>Where Google Home starts to feel thin</h2>"
        "<ul>"
        "  <li><strong>Mixed-home ownership:</strong> Once your house mixes protocols, bridges, and multiple vendors, Google Home can stop feeling like the place that truly explains what is going on.</li>"
        "  <li><strong>Reliability-first automation:</strong> If you care about local behavior and surviving cloud weirdness, Google Home is not always the strongest foundation.</li>"
        "  <li><strong>Architecture clarity:</strong> If your real issue is whether a device is failing because of Wi-Fi, Matter, Thread, the vendor cloud, or a bridge, Google Home often sits above that problem rather than organizing it.</li>"
        "  <li><strong>Hub depth:</strong> Google Home is often easiest when the home is simple, not when the home is technically mature.</li>"
        "</ul>"
        "<h2>When Google Home is enough</h2>"
        "<ul>"
        "  <li>Your home is still relatively small and mainstream.</li>"
        "  <li>You care more about convenience and voice control than about deep automation.</li>"
        "  <li>You are not yet dealing with major protocol sprawl or bridge complexity.</li>"
        "  <li>You can tolerate some cloud dependence as the cost of simplicity.</li>"
        "</ul>"
        "<h2>When Google Home is not enough</h2>"
        "<ul>"
        "  <li>You are mixing many device types and ecosystems.</li>"
        "  <li>You want a cleaner long-term hub strategy instead of app sprawl.</li>"
        "  <li>You need stronger local control or more reliable automations.</li>"
        "  <li>You keep troubleshooting the same offline or out-of-sync behaviors across multiple products.</li>"
        "</ul>"
        "<p>That is usually the point where the right move is not “make Google Home do more.” It is “keep Google Home as the user-facing layer, but put something stronger underneath it.”</p>"
        "<h2>Google Home vs a real hub</h2>"
        "<p>Google Home often acts like the <strong>front desk</strong> of the house. A real hub is the operations layer behind the scenes. That distinction matters because a mixed smart home usually needs both convenience and structure, not just one of them.</p>"
        "<p>If you only optimize for convenience, Google Home can look like enough for longer than it really is. If you optimize for reliability, you start to see where it benefits from a stronger hub strategy.</p>"
        "<h2>Matter, Thread, and Google Home</h2>"
        "<p>Google Home participates in newer parts of the smart-home stack, which is part of why it looks more hub-like than older voice-assistant setups. But those newer roles still do not automatically solve the bigger architecture question.</p>"
        "<ul>"
        "  <li><strong>Matter</strong> can improve interoperability, but it does not fix weak networks or unclear system ownership.</li>"
        "  <li><strong>Thread</strong> can improve parts of local transport, but it is not the same thing as a full smart-home coordination layer.</li>"
        "  <li><strong>Google Home support</strong> is useful, but useful is not always the same thing as sufficient.</li>"
        "</ul>"
        "<h2>Best practical setup patterns</h2>"
        "<ul>"
        "  <li><strong>Google Home only:</strong> good enough for simpler homes that value convenience.</li>"
        "  <li><strong>Real hub + Google Home on top:</strong> usually the better long-term answer for mixed homes.</li>"
        "  <li><strong>Bridge-heavy Nest/Google ecosystem:</strong> workable for some homes, but easy to outgrow.</li>"
        "</ul>"
        "<h2>When buying a real hub is actually justified</h2>"
        "<p>A stronger hub becomes justified when Google Home is still helpful, but no longer sufficient as the main place where reliability, automation, and device coordination should live.</p>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="Google Home users who want a stronger coordination layer without giving up voice control",
            why=[
                "Useful when Google Home is good at convenience but weak as the main smart-home brain",
                "Strong fit for mixed-device homes that need one serious architecture layer",
                "Better when you want one place to reason about integrations and automations cleanly",
            ],
            caution="Can be more system than you need if the house is still tiny and very simple.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want a real hub while keeping Google Home as the convenience layer",
            why=[
                "Good fit when routines and device coordination are getting messy",
                "Stronger long-term structure than relying on Google Home alone",
                "Useful middle ground for mixed homes that want reliability without jumping straight into a deeper DIY stack",
            ],
            caution="Still a more deliberate architecture choice than staying app-only.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Bottom line</h2>"
        "<p>Google Home can absolutely behave like part of a hub setup, and for some homes it is enough. But once the house becomes more mixed, more layered, or more reliability-sensitive, Google Home is usually better as the control surface than as the only smart-home core.</p>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>If you are still deciding whether a hub belongs in the house at all, start there</a></li>"
        "  <li><a href='/devices/is-alexa-a-smart-home-hub/'>If you are comparing ecosystems, see how the Alexa version of this question differs</a></li>"
        "  <li><a href='/devices/is-apple-home-a-smart-home-hub/'>If your house is more Apple-shaped, compare the Apple Home version too</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If Google Home is not enough anymore, compare stronger mixed-home hub strategies</a></li>"
        "</ul>"
        ),
    },
    "/devices/is-apple-home-a-smart-home-hub/": {
        "title": "Is Apple Home a smart home hub?",
        "description": "How Apple Home, HomePod, and Apple TV really fit into a hub strategy, where they help, and when you still need a stronger smart home controller.",
        "section": "Devices",
        "body": (
        "<p><strong>Apple Home can be part of a smart home hub strategy, but the Home app, a Home hub, a Matter controller, and a Thread border router are not all the same thing.</strong> That is why Apple Home can feel both more capable and more confusing than people expect.</p>"
        "<h2>Short answer</h2>"
        "<p>If your home is mostly Apple-shaped and your automation needs are modest, Apple Home may be enough. If you are building a more mixed smart home or need deeper reliability and coordination, Apple Home is often better as the user-facing ecosystem on top of a stronger hub plan.</p>"
        "<h2>Why this question gets messy fast</h2>"
        "<p>Apple terminology creates a lot of overlap. People say “HomeKit,” “Apple Home,” “Home hub,” “HomePod,” and “Apple TV” as if they all mean the same thing. They do not. Some refer to the app experience, some to a device role, and some to newer Matter or Thread behavior.</p>"
        "<p>That is why people often ask whether Apple Home is a hub when the real question is closer to: “Do I already have enough Apple infrastructure to run the home well, or do I still need a stronger coordination layer?”</p>"
        "<h2>What Apple Home does well</h2>"
        "<ul>"
        "  <li><strong>Clean user experience:</strong> Apple Home often feels more coherent than many mainstream smart-home app experiences.</li>"
        "  <li><strong>Good ecosystem fit:</strong> In an Apple-heavy household, HomePod and Apple TV can make the whole experience feel more integrated.</li>"
        "  <li><strong>Automation convenience:</strong> For moderate setups, Apple Home automations can be enough to keep the house pleasant and simple.</li>"
        "  <li><strong>Strong front-end role:</strong> Apple Home works well as the visible control surface even when more serious coordination is happening somewhere deeper in the stack.</li>"
        "</ul>"
        "<h2>What Apple Home is not guaranteed to solve</h2>"
        "<ul>"
        "  <li><strong>Mixed-home complexity:</strong> If the home mixes vendors, bridges, protocols, and ecosystems, Apple Home may stop feeling like the place that truly owns the architecture.</li>"
        "  <li><strong>Protocol depth:</strong> Newer support for Matter and Thread helps, but it does not automatically mean the home now has one ideal hub strategy.</li>"
        "  <li><strong>Reliability at scale:</strong> The bigger and messier the home gets, the more valuable a dedicated automation and coordination layer becomes.</li>"
        "  <li><strong>Clear failure diagnosis:</strong> Apple Home can sometimes sit above the real problem rather than reveal it.</li>"
        "</ul>"
        "<h2>What counts as a Home hub</h2>"
        "<p>This is where Apple differs from the other ecosystem questions. In Apple’s world, certain devices such as HomePod or Apple TV can play hub-like roles for the Home app experience. That matters, but it still does not mean Apple Home automatically replaces every function a stronger mixed-home hub might serve.</p>"
        "<h2>When Apple Home is enough</h2>"
        "<ul>"
        "  <li>Your home is mostly within the Apple ecosystem.</li>"
        "  <li>You value polish and convenience more than deeper cross-platform flexibility.</li>"
        "  <li>Your automations are useful but not especially complex.</li>"
        "  <li>You are not yet wrestling with major bridge sprawl or protocol sprawl.</li>"
        "</ul>"
        "<h2>When Apple Home is not enough</h2>"
        "<ul>"
        "  <li>You are mixing Apple, Google, Alexa, and vendor-native ecosystems at the same time.</li>"
        "  <li>You want one stronger place to manage a growing system with more local control.</li>"
        "  <li>You need deeper automation or broader protocol handling than the surface Apple Home experience comfortably provides.</li>"
        "  <li>You want the home to stay coherent even as it becomes less Apple-pure.</li>"
        "</ul>"
        "<h2>Apple Home vs a real hub</h2>"
        "<p>Apple Home is often excellent as the <strong>experience layer</strong>. A real hub is more often the <strong>coordination layer</strong>. Those two roles can live together very well, and in many of the best mixed homes they do.</p>"
        "<p>That is why the better question is often not “Is Apple Home a hub?” but “Is Apple Home enough to be the only hub-like layer in <em>this</em> house?”</p>"
        "<h2>Matter, Thread, HomePod, and Apple TV</h2>"
        "<p>Apple’s support for newer smart-home roles is part of why the answer feels more nuanced than a simple yes or no. HomePod and Apple TV can matter a lot. But their presence still does not automatically erase the need for a stronger mixed-home control strategy.</p>"
        "<ul>"
        "  <li><strong>Matter</strong> improves parts of interoperability, but it does not remove the need for architectural clarity.</li>"
        "  <li><strong>Thread</strong> can improve parts of local networking, but it is not the whole hub story.</li>"
        "  <li><strong>Apple devices in hub-like roles</strong> can absolutely help, but they do not always replace a dedicated central controller for a larger mixed home.</li>"
        "</ul>"
        "<h2>Best practical setup patterns</h2>"
        "<ul>"
        "  <li><strong>Apple Home only:</strong> strong fit for smaller Apple-shaped homes.</li>"
        "  <li><strong>Real hub + Apple Home front end:</strong> often the best long-term answer for mixed homes that still want a polished Apple experience.</li>"
        "  <li><strong>Bridge-heavy Apple Home setup:</strong> sometimes works, but can become harder to reason about as the house grows.</li>"
        "</ul>"
        "<h2>When buying a real hub is actually justified</h2>"
        "<p>A stronger hub is justified when Apple Home is still giving you a great front-end experience, but the actual coordination needs of the house have outgrown what that front-end should be carrying alone.</p>"
        + AFFILIATE_INLINE_DISCLOSURE
        + "<div class='grid'>"
        + product_card(
            title="Home Assistant Green",
            best_for="Apple Home users who want to keep the polished front-end experience while adding a stronger mixed-home coordination layer",
            why=[
                "Useful when Apple Home is good at the experience layer but not enough as the only smart-home core",
                "Strong fit for mixed homes that still want Apple Home in the loop",
                "Better when you want one place to reason about a bigger system clearly",
            ],
            caution="Can be more architecture than you need if the house is still small and mostly Apple-pure.",
            query="Home Assistant Green",
            button_label="See hub option on Amazon ↗",
        )
        + product_card(
            title="Hubitat Elevation",
            best_for="buyers who want a stronger dedicated hub while keeping Apple Home as a top-layer experience",
            why=[
                "Useful when the home is mixed enough that Apple Home alone is starting to feel thin",
                "Provides a clearer long-term structure than relying on app-only coordination",
                "Works well when you want a serious hub without fully rebuilding the whole house around one ecosystem",
            ],
            caution="Still a more deliberate architecture choice than staying Apple-only.",
            query="Hubitat Elevation hub",
            button_label="See hub option on Amazon ↗",
        )
        + "</div>"
        "<h2>Bottom line</h2>"
        "<p>Apple Home can absolutely be part of a hub strategy, and for many Apple-heavy homes it may be enough for quite a while. But once the house becomes more mixed, more layered, or more reliability-sensitive, Apple Home usually works best as the experience layer on top of a stronger control strategy, not as the only smart-home core.</p>"
        "<h2>Next steps</h2>"
        "<ul>"
        "  <li><a href='/devices/do-i-need-a-smart-home-hub/'>If you are still deciding whether a hub belongs in the house at all, start there</a></li>"
        "  <li><a href='/devices/is-alexa-a-smart-home-hub/'>If you are comparing ecosystems, see how the Alexa version differs</a></li>"
        "  <li><a href='/devices/is-google-home-a-smart-home-hub/'>If you are comparing ecosystems, see where Google Home differs too</a></li>"
        "  <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If Apple Home is not enough anymore, compare stronger mixed-home hub strategies</a></li>"
        "</ul>"
        ),
    },
}


def build_device_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(DEVICE_PAGES)

from __future__ import annotations

from .shared import page_card

HUBS = {
    "/start/": {
        "title": "Start here",
        "description": "Pick the shortest path to making your smart home reliable again.",
        "body": """
        <section class='hero'>
          <h1 style='margin-top:0'>Start Here.</h1>
          <p class='subhead'>If your smart home is flaky, the fastest path is to identify whether the problem is protocol choice, hub strategy, or overloaded Wi-Fi.</p>
          <p style='margin-top:18px; display:flex; gap:12px; flex-wrap:wrap'>
            <a class='btn' href='/troubleshooting/'>My devices are failing</a>
            <a class='btn secondary' href='/protocols/'>I need to choose a protocol</a>
          </p>
        </section>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'>Troubleshoot first</h3><p class='muted'>If plugs, lights, or sensors keep failing, start with the symptom before you assume you need new gear.</p><p><a href='/troubleshooting/'>Go to symptom-first fixes →</a></p></div>
          <div class='card'><h3 style='margin-top:0'>Choose the right protocol</h3><p class='muted'>Zigbee, Z-Wave, Thread, Matter, and Wi-Fi are not interchangeable, and the wrong fit creates fake device problems.</p><p><a href='/protocols/'>Go to protocol decisions →</a></p></div>
          <div class='card'><h3 style='margin-top:0'>Fix the network layer</h3><p class='muted'>Too many cheap Wi-Fi devices can make the whole house feel cursed even when the devices themselves are fine.</p><p><a href='/wifi-load/'>Go to Wi-Fi bottlenecks →</a></p></div>
        </div>
        """,
    },
    "/protocols/": {
        "title": "Protocols",
        "description": "Choose the right smart home protocol before you buy the wrong gear for your setup.",
        "body": """
        <h1 style='margin-top:0'>Protocols</h1>
        <p class='lede'>Most smart home pain starts with picking devices that do not fit the network, ecosystem, or control layer you already have.</p>
        <p class='muted'>Use this section when you are trying to separate radio-layer decisions from hub decisions, ecosystem decisions, and Wi-Fi overload problems. The goal is not to memorize buzzwords. It is to buy gear that actually belongs in your house.</p>
        <h2>Start with the right kind of question</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Which protocol family is the best fit overall?</a></h3><p class='muted'>Use this when you need the broad architecture answer for a mixed or growing home.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/matter-vs-thread/'>Am I confusing Matter and Thread?</a></h3><p class='muted'>This is the most common modern smart-home terminology mistake.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>Am I mixing up hub, bridge, controller, and border router?</a></h3><p class='muted'>Use this when terminology confusion is driving bad buying decisions.</p></div>
        </div>
        <h2>Core protocol comparisons</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Zigbee vs Z-Wave vs Thread vs Matter</a></h3><p class='muted'>The real-world tradeoffs for reliability, mixed homes, and future flexibility.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/matter-vs-zigbee/'>Matter vs Zigbee</a></h3><p class='muted'>Interoperability promise versus practical mesh maturity.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/thread-vs-zigbee/'>Thread vs Zigbee</a></h3><p class='muted'>Newer architecture versus battle-tested device depth.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/matter-vs-thread/'>Matter vs Thread</a></h3><p class='muted'>The standard versus the transport layer, without the usual confusion.</p></div>
        </div>
        <h2>Where to go next</h2>
        <ul>
          <li><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>If protocol choice is tangled up with Alexa, Google Home, or Apple Home, use the cross-ecosystem decision guide</a></li>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If the real issue is what should coordinate the house, move to hub strategy</a></li>
          <li><a href='/products/reliable-smart-home-hubs/'>If you already know a hub purchase is justified, go to the curated shortlist</a></li>
        </ul>
        """,
    },
    "/troubleshooting/": {
        "title": "Troubleshooting",
        "description": "Symptom-first fixes for pairing failures, disconnects, and ghost offline states.",
        "body": """
        <h1 style='margin-top:0'>Troubleshooting</h1>
        <p class='lede'>Use the shortest symptom-first path instead of reading 20 forum threads.</p>
        <p class='muted'>If you are not yet sure whether the failure lives in Wi-Fi, protocol choice, cloud integrations, or hub strategy, start here and follow the symptom patterns.</p>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/why-wont-my-smart-plug-connect-to-wifi/'>Why won't my smart plug connect to Wi-Fi?</a></h3><p class='muted'>Fastest fixes for pairing and setup failures.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/why-wont-my-smart-bulb-pair/'>Why won't my smart bulb pair?</a></h3><p class='muted'>Fix bulbs that fail reset, onboarding, or pairing mode.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/smart-lights-keep-disconnecting/'>Smart lights keep disconnecting</a></h3><p class='muted'>Protocol and topology problems that look like bulb problems.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Smart home devices keep going offline</a></h3><p class='muted'>Find the shared failure layer instead of swapping random devices.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/alexa-device-unresponsive-but-wifi-works/'>Alexa device unresponsive but Wi-Fi works</a></h3><p class='muted'>Usually a bridge, cloud, or skill graph issue.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/google-home-device-offline-fix/'>Google Home device offline fix</a></h3><p class='muted'>Separate real network failures from account sync drift.</p></div>
        </div>
        """,
    },
    "/hubs/": {
        "title": "Hubs and bridges",
        "description": "Choose a hub strategy that makes mixed smart homes simpler and more reliable.",
        "body": """
        <h1 style='margin-top:0'>Hubs and bridges</h1>
        <p class='lede'>Use this section when the real problem is not one broken device, but the fact that the whole house no longer has a clean control strategy.</p>
        <p class='muted'>A good hub strategy should reduce protocol chaos, improve local reliability, clarify what role Alexa or Google Home or Apple Home should play, and keep your smart home from depending on a pile of fragile cloud handoffs.</p>
        <h2>Start with the architecture question</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></h3><p class='muted'>Start here if you want one cleaner coordination layer instead of stacking more vendor apps and bridges at random.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/do-i-need-a-smart-home-hub/'>Do I need a smart home hub?</a></h3><p class='muted'>Use this if you are not yet sure the house has actually earned a dedicated hub.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>Do I still need a hub if I already have Alexa, Google Home, or Apple Home?</a></h3><p class='muted'>Use this when ecosystem convenience is making the decision feel blurrier than it really is.</p></div>
        </div>
        <h2>Ecosystem-specific hub confusion</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/is-alexa-a-smart-home-hub/'>Is Alexa a smart home hub?</a></h3><p class='muted'>Where Echo devices overlap with hub behavior and where they stop being enough.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/is-google-home-a-smart-home-hub/'>Is Google Home a smart home hub?</a></h3><p class='muted'>What Nest and Google Home devices really do in a growing system.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/is-apple-home-a-smart-home-hub/'>Is Apple Home a smart home hub?</a></h3><p class='muted'>How Apple Home, HomePod, and Apple TV fit into the same question.</p></div>
        </div>
        <h2>Terminology that helps before you buy</h2>
        <ul>
          <li><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>Learn the difference between a real hub, a bridge, a controller, and a Thread border router</a></li>
          <li><a href='/products/reliable-smart-home-hubs/'>Then compare the reliability-first shortlist of hub and hub-adjacent options</a></li>
        </ul>
        """,
    },
    "/wifi-load/": {
        "title": "Wi-Fi load",
        "description": "Router stress, 2.4 GHz policy, and how Wi-Fi becomes the hidden problem layer in smart homes.",
        "body": """
        <h1 style='margin-top:0'>Wi-Fi load</h1>
        <p class='lede'>Use this section when your smart home feels unreliable because the network itself is overloaded, poorly segmented, or forcing too many cheap devices onto Wi-Fi.</p>
        <p class='muted'>If pairing is inconsistent, devices fall offline in batches, or performance gets worse as you add gear, this is often the layer to check before replacing devices.</p>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/wifi-load/how-many-devices-can-wifi-handle-smart-home/'>How many devices can Wi-Fi handle?</a></h3><p class='muted'>Start here if you need to figure out whether the router is the bottleneck.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/wifi-load/too-many-smart-devices-on-wifi/'>Too many smart devices on Wi-Fi</a></h3><p class='muted'>When the all-Wi-Fi strategy itself is becoming the real problem.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></h3><p class='muted'>Basic policy choices that prevent a lot of setup and stability failures.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/wifi-load/smart-home-separate-ssid/'>Should smart home devices use a separate SSID?</a></h3><p class='muted'>Segmentation that helps instead of randomly breaking local discovery.</p></div>
        </div>
        """,
    },
    "/devices/": {
        "title": "Devices",
        "description": "Reliability-first guidance by device type and whether you really need a hub.",
        "body": """
        <h1 style='margin-top:0'>Devices</h1>
        <p class='lede'>Use this section when you are deciding what kind of hardware belongs in the house, not just which app to tap next.</p>
        <p class='muted'>The right device choice depends on protocol fit, hub strategy, ecosystem role, and whether adding another Wi-Fi gadget will actually make the system less stable. This is where you decide whether the fix is better architecture, a different device type, or no new hardware at all.</p>
        <h2>Start with the architecture decision</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/do-i-need-a-smart-home-hub/'>Do I need a smart home hub?</a></h3><p class='muted'>Start here if you are deciding whether better architecture matters more than buying another standalone device.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>Do I still need a hub if I already have Alexa, Google Home, or Apple Home?</a></h3><p class='muted'>Use this when you already have an ecosystem but are not sure whether it counts as enough.</p></div>
        </div>
        <h2>Ecosystem device-role guides</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/is-alexa-a-smart-home-hub/'>Is Alexa a smart home hub?</a></h3><p class='muted'>Clarifies where Echo devices act like hub-adjacent gear and where they do not.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/is-google-home-a-smart-home-hub/'>Is Google Home a smart home hub?</a></h3><p class='muted'>Explains what Nest and Google Home devices really do in a growing setup.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/is-apple-home-a-smart-home-hub/'>Is Apple Home a smart home hub?</a></h3><p class='muted'>Explains the Apple Home app, Home hub roles, and where Apple gear is enough.</p></div>
        </div>
        <h2>Buying paths from here</h2>
        <ul>
          <li><a href='/products/reliable-smart-home-hubs/'>If the answer is “yes, I need a stronger control layer,” use the hub shortlist</a></li>
          <li><a href='/products/reliable-smart-plugs/'>If the real need is a device-level replacement, use the plug shortlist</a></li>
          <li><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>If terminology is the thing blocking you, use the terminology guide first</a></li>
        </ul>
        """,
    },
    "/products/": {
        "title": "Products",
        "description": "Curated product recommendations for reliability-first smart homes.",
        "body": """
        <h1 style='margin-top:0'>Products</h1>
        <p class='lede'>This section should help you buy the right gear for the right layer of the problem, not dump you into a giant gadget catalog.</p>
        <p class='muted'>The strongest product pages on this site should eventually cover more than just plugs and true hubs. They should include hub-adjacent ecosystem controllers, bridges, dimmers, doorbells, and compatibility framing where that actually improves decision quality. For now, use the current shortlist as the best-supported starting layer.</p>
        <h2>Current best-supported buying paths</h2>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/products/reliable-smart-home-hubs/'>Reliable smart home hubs</a></h3><p class='muted'>Best when the fix is a stronger control layer for a mixed-device home, and when you need to understand true hubs versus ecosystem controllers.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/products/reliable-smart-plugs/'>Reliable smart plugs</a></h3><p class='muted'>Best when you need a more trustworthy replacement or want to avoid adding more cheap Wi-Fi clutter.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/products/reliable-smart-dimmers-and-switches/'>Reliable smart dimmers and switches</a></h3><p class='muted'>Best when the real fix belongs at the wall switch, not in another random bulb or app.</p></div>
        </div>
        <h2>Use products only after the architecture is clear</h2>
        <ul>
          <li><a href='/devices/do-i-need-a-smart-home-hub-if-i-already-have-alexa-google-home-or-homekit/'>If you are deciding whether Alexa, Google Home, or Apple Home are enough, start there before you buy</a></li>
          <li><a href='/protocols/hub-vs-bridge-vs-controller-vs-border-router/'>If you are mixing up hubs, bridges, controllers, and border routers, fix the terminology first</a></li>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>If you already know the house needs stronger coordination, go to the hub strategy guide</a></li>
        </ul>
        """,
    },
}


def build_homepage(*, shell, write, OUT, BASE, SITE_NAME) -> None:
    write(
        OUT / 'index.html',
        shell(
            'Fix smart home reliability',
            f"""
            <section class='hero'>
              <h1 style='margin-top:0'>Fix Smart Home Reliability.<br/>No Guesswork.</h1>
              <p class='subhead'>Practical troubleshooting and buying guidance for flaky smart home setups, mixed ecosystems, disconnects, and overloaded Wi-Fi.</p>
              <p style='margin-top:18px; display:flex; gap:12px; flex-wrap:wrap'>
                <a class='btn' href='/start/'>Start here</a>
                <a class='btn secondary' href='/troubleshooting/'>Troubleshooting</a>
              </p>
            </section>
            <section class='section'>
              <div class='grid'>
                <div class='card'><h3 style='margin-top:0'>Fix the real problem</h3><p class='muted'>Most smart home advice is fragmented, brand-biased, or useless when things start failing. This site is built to help you find the real failure layer fast.</p></div>
                <div class='card'><h3 style='margin-top:0'>Start with your situation</h3><p class='muted'>Begin with the symptom, protocol decision, or network bottleneck that actually matches what is going wrong in your house.</p></div>
                <div class='card'><h3 style='margin-top:0'>Buy only what helps</h3><p class='muted'>The goal is more stable connections, better ecosystem fit, and the smallest useful upgrade, not random gadget churn.</p></div>
              </div>
            </section>
            <section class='section'>
              <h2 style='margin-top:0'>Where to start</h2>
              <div class='grid'>
                {page_card('Protocols', 'Use when the real problem is compatibility, ecosystem fit, or choosing the right radio layer.', '/protocols/')}
                {page_card('Troubleshooting', 'Use when devices drop, fail to pair, or keep going offline.', '/troubleshooting/')}
                {page_card('Hubs', 'Use when the real problem is app sprawl, bridge chaos, or weak control architecture.', '/hubs/')}
                {page_card('Wi-Fi load', 'Use when onboarding fails, devices drop in batches, or the router may be the bottleneck.', '/wifi-load/')}
                {page_card('Devices', 'Use when you need to choose the right kind of hardware before buying.', '/devices/')}
                {page_card('Products', 'Use after you know buying better gear is actually part of the solution.', '/products/')}
              </div>
            </section>
            <section class='section'>
              <h2 style='margin-top:0'>Popular fixes and decisions</h2>
              <div class='grid'>
                {page_card("Why won't my smart plug connect to Wi-Fi?", 'Fast fixes for one of the most common setup failures.', '/why-wont-my-smart-plug-connect-to-wifi/')}
                {page_card("Why won't my smart bulb pair?", 'Reset, onboarding, and wrong-protocol pairing mistakes.', '/why-wont-my-smart-bulb-pair/')}
                {page_card('Smart lights keep disconnecting', 'Find out whether the real problem is protocol, mesh depth, or Wi-Fi.', '/smart-lights-keep-disconnecting/')}
                {page_card('Zigbee vs Z-Wave vs Thread vs Matter', 'Pick the right protocol before buying the wrong gear.', '/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/')}
                {page_card('Matter vs Zigbee', 'Interoperability promise versus practical mesh maturity.', '/protocols/matter-vs-zigbee/')}
                {page_card('Matter vs Thread', 'The standard versus the transport layer, without the usual confusion.', '/protocols/matter-vs-thread/')}
                {page_card('Best hub for mixed smart home', 'The hub patterns that make mixed ecosystems manageable.', '/hubs/best-hub-for-mixed-smart-home/')}
                {page_card('Too many smart devices on Wi‑Fi', 'When Wi-Fi itself is becoming the hidden bottleneck.', '/wifi-load/too-many-smart-devices-on-wifi/')}
                {page_card('Should smart home devices use a separate SSID?', 'Segmentation that helps instead of breaking discovery.', '/wifi-load/smart-home-separate-ssid/')}
              </div>
            </section>
            """,
            path='/',
            description=None,
            BASE=BASE,
            SITE_NAME=SITE_NAME,
        ),
    )


def build_hubs(*, shell, write, OUT, BASE, SITE_NAME) -> None:
    for path, spec in HUBS.items():
        out = OUT / path.strip('/') / 'index.html'
        write(out, shell(spec['title'], spec['body'], path=path, description=spec['description'], BASE=BASE, SITE_NAME=SITE_NAME))

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
          <div class='card'><h3 style='margin-top:0'>Troubleshoot first</h3><p class='muted'>If plugs, lights, or sensors keep failing, start with the symptom.</p><p><a href='/troubleshooting/'>Open troubleshooting →</a></p></div>
          <div class='card'><h3 style='margin-top:0'>Choose the right protocol</h3><p class='muted'>Zigbee, Z-Wave, Thread, Matter, and Wi-Fi are not interchangeable.</p><p><a href='/protocols/'>Open protocols →</a></p></div>
          <div class='card'><h3 style='margin-top:0'>Fix the network layer</h3><p class='muted'>Too many cheap Wi-Fi devices can make the whole house feel cursed.</p><p><a href='/wifi-load/'>Open Wi-Fi load →</a></p></div>
        </div>
        """,
    },
    "/protocols/": {
        "title": "Protocols",
        "description": "Choose the right smart home protocol before you buy the wrong gear for your setup.",
        "body": """
        <h1 style='margin-top:0'>Protocols</h1>
        <p class='lede'>Most smart home pain starts with picking devices that do not fit the network or ecosystem you already have.</p>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Zigbee vs Z-Wave vs Thread vs Matter</a></h3><p class='muted'>The real-world tradeoffs for reliability and mixed homes.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/matter-vs-zigbee/'>Matter vs Zigbee</a></h3><p class='muted'>Interoperability promise vs practical mesh maturity.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/protocols/thread-vs-zigbee/'>Thread vs Zigbee</a></h3><p class='muted'>Newer architecture versus battle-tested device depth.</p></div>
        </div>
        """,
    },
    "/troubleshooting/": {
        "title": "Troubleshooting",
        "description": "Symptom-first fixes for pairing failures, disconnects, and ghost offline states.",
        "body": """
        <h1 style='margin-top:0'>Troubleshooting</h1>
        <p class='lede'>Use the shortest symptom-first path instead of reading 20 forum threads.</p>
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
        <p class='lede'>Use this section when the real problem is ecosystem sprawl, too many apps, or devices that only work well when a bridge or central hub is doing the coordination.</p>
        <p class='muted'>A good hub strategy should reduce protocol chaos, improve local reliability, and keep your smart home from depending on a pile of fragile cloud handoffs.</p>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></h3><p class='muted'>Start here if you want one cleaner control layer instead of stacking more vendor apps and bridges at random.</p></div>
        </div>
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
        <p class='muted'>The right device choice depends on protocol fit, hub strategy, and whether adding another Wi-Fi gadget will actually make the system less stable.</p>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/devices/do-i-need-a-smart-home-hub/'>Do I need a smart home hub?</a></h3><p class='muted'>Start here if you are trying to decide whether better architecture matters more than buying another standalone device.</p></div>
        </div>
        """,
    },
    "/products/": {
        "title": "Products",
        "description": "Curated product recommendations for reliability-first smart homes.",
        "body": """
        <h1 style='margin-top:0'>Products</h1>
        <p class='lede'>This section is for the short list, not a giant gadget catalog. Use it after you understand whether your problem is really protocol fit, Wi-Fi load, or hub strategy.</p>
        <p class='muted'>Every recommendation here is meant to support a more stable setup, not push you into buying more gear than the problem actually requires.</p>
        <div class='grid'>
          <div class='card'><h3 style='margin-top:0'><a href='/products/reliable-smart-home-hubs/'>Reliable smart home hubs</a></h3><p class='muted'>Best when the fix is a stronger control layer for a mixed-device home.</p></div>
          <div class='card'><h3 style='margin-top:0'><a href='/products/reliable-smart-plugs/'>Reliable smart plugs</a></h3><p class='muted'>Best when you need a more trustworthy replacement or want to avoid more cheap Wi-Fi clutter.</p></div>
        </div>
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
                {page_card('Protocols', 'Zigbee vs Z-Wave vs Thread vs Matter vs Wi-Fi.', '/protocols/')}
                {page_card('Troubleshooting', 'Why devices drop, fail to pair, or go offline.', '/troubleshooting/')}
                {page_card('Hubs', 'Best hub strategy for mixed smart homes.', '/hubs/')}
                {page_card('Wi-Fi load', 'How many devices your network can really handle.', '/wifi-load/')}
                {page_card('Devices', 'Plugs, switches, bulbs, sensors, locks, cameras, bridges.', '/devices/')}
                {page_card('Products', 'Curated reliability-first product picks.', '/products/')}
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

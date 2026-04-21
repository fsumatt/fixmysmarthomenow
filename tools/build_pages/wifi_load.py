from __future__ import annotations

WIFI_LOAD_PAGES = {
    "/wifi-load/too-many-smart-devices-on-wifi/": {
        "title": "Too many smart devices on Wi-Fi",
        "description": "How to tell when your smart home has outgrown a simple all-Wi-Fi approach and what to do next.",
        "section": "Wi-Fi load",
        "body": """
        <p>If you have too many smart devices on Wi-Fi, the solution is usually <strong>better network policy and protocol mix</strong>, not just a bigger pile of extenders.</p>
        <h2>Warning signs</h2>
        <ul>
          <li>Devices fail randomly during onboarding</li>
          <li>Apps lag even though internet speed tests look normal</li>
          <li>2.4 GHz gear is much less stable than phones and laptops</li>
        </ul>
        <h2>What to do</h2>
        <ul>
          <li>Move simple always-on devices to Zigbee/Z-Wave/Thread where practical.</li>
          <li>Create a dedicated IoT SSID.</li>
          <li>Retire weak ISP routers before buying more random smart devices.</li>
        </ul>
        """,
    },
    "/wifi-load/smart-home-separate-ssid/": {
        "title": "Should smart home devices use a separate SSID?",
        "description": "When a separate IoT SSID helps, when it is overkill, and how to do it without making your smart home worse.",
        "section": "Wi-Fi load",
        "body": """
        <p><strong>Yes, often.</strong> A separate SSID for smart home devices can make onboarding easier, reduce weird band-steering failures, and keep your main network cleaner.</p>
        <h2>It helps when</h2>
        <ul>
          <li>You have lots of 2.4 GHz-only devices.</li>
          <li>Band steering causes onboarding failures.</li>
          <li>You want easier troubleshooting and cleaner segmentation.</li>
        </ul>
        <h2>It can hurt when</h2>
        <ul>
          <li>You isolate the SSID too hard and break local discovery.</li>
          <li>You split devices and controllers in a way that stops them from seeing each other.</li>
        </ul>
        <p>Use segmentation for clarity, not as a random security ritual.</p>
        """,
    },
    "/wifi-load/how-many-devices-can-wifi-handle-smart-home/": {
        "title": "How many devices can Wi-Fi handle for a smart home?",
        "description": "How to tell whether your router is overloaded and what to change before blaming every smart device.",
        "section": "Wi-Fi load",
        "body": """
        <p><strong>There is no single device limit.</strong> What matters is router quality, client behavior, airtime usage, 2.4 GHz congestion, and whether your smart home is built from chatty Wi-Fi gadgets or better protocols.</p>
        <h2>Warning signs of overload</h2>
        <ul>
          <li>Random offline devices with no clear pattern</li>
          <li>Slow app control but normal internet speed tests</li>
          <li>2.4 GHz devices failing more than phones/laptops</li>
          <li>Routers that need frequent reboots</li>
        </ul>
        <h2>Best fixes</h2>
        <ul>
          <li>Move cheap IoT gear to a dedicated 2.4 GHz SSID.</li>
          <li>Reduce channel overlap and band-steering weirdness.</li>
          <li>Prefer Zigbee/Z-Wave/Thread for sensors and simple always-on devices.</li>
          <li>Upgrade weak ISP routers before buying random repeaters.</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/wifi-load/2-4ghz-smart-home-best-practices/'>2.4 GHz smart home best practices</a></li>
          <li><a href='/troubleshooting/smart-home-devices-keep-going-offline/'>Devices keep going offline</a></li>
        </ul>
        """,
    },
    "/wifi-load/2-4ghz-smart-home-best-practices/": {
        "title": "2.4 GHz smart home best practices",
        "description": "How to set up 2.4 GHz Wi-Fi so smart plugs, lights, and sensors stop failing for dumb reasons.",
        "section": "Wi-Fi load",
        "body": """
        <p>Most flaky Wi-Fi smart home setups are really <strong>bad 2.4 GHz policy</strong> problems: band steering confusion, odd security settings, weak coverage, and channel congestion.</p>
        <h2>Best practices</h2>
        <ul>
          <li>Use a dedicated 2.4 GHz IoT SSID if onboarding frequently fails.</li>
          <li>Prefer WPA2/WPA2-WPA3 mixed mode over forcing WPA3-only on cheap IoT gear.</li>
          <li>Use fixed non-overlapping channels where possible.</li>
          <li>Keep IoT devices on stable signal, not fringe coverage.</li>
        </ul>
        <h2>Good companion pages</h2>
        <ul>
          <li><a href='/why-wont-my-smart-plug-connect-to-wifi/'>Why won't my smart plug connect?</a></li>
          <li><a href='/wifi-load/how-many-devices-can-wifi-handle-smart-home/'>How many devices can Wi-Fi handle?</a></li>
        </ul>
        """,
    },
}


def build_wifi_load_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(WIFI_LOAD_PAGES)

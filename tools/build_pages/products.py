from __future__ import annotations

PRODUCT_PAGES = {
    "/products/reliable-smart-home-hubs/": {
        "title": "Reliable smart home hubs",
        "description": "A curated shortlist of smart home hub strategies and hub categories that prioritize reliability over hype.",
        "section": "Products",
        "body": """
        <p>This is not a giant hub catalog. It is the short list of hub categories worth considering if you care about stable mixed-device smart homes.</p>
        <h2>Recommended patterns</h2>
        <ul>
          <li><strong>Main automation hub + bridges:</strong> best overall for mixed homes.</li>
          <li><strong>Vendor hub only:</strong> fine if you stay narrow, risky if you want flexibility later.</li>
          <li><strong>Voice assistant only:</strong> acceptable for very small setups, weak for serious automation.</li>
        </ul>
        <h2>Buy for these reasons</h2>
        <ul>
          <li>Protocol support you actually need</li>
          <li>Local control options</li>
          <li>Mature integrations</li>
          <li>Good recovery when devices go weird</li>
        </ul>
        <h2>Related pages</h2>
        <ul>
          <li><a href='/hubs/best-hub-for-mixed-smart-home/'>Best hub for mixed smart home</a></li>
          <li><a href='/protocols/zigbee-vs-z-wave-vs-thread-vs-matter/'>Protocol comparison</a></li>
        </ul>
        """,
    },
    "/products/reliable-smart-plugs/": {
        "title": "Reliable smart plugs",
        "description": "What actually makes a smart plug reliable, and which buying patterns avoid the usual Wi-Fi plug headaches.",
        "section": "Products",
        "body": """
        <p>Reliable smart plugs are less about brand hype and more about <strong>protocol fit</strong>, clean onboarding, and whether they behave well in your actual ecosystem.</p>
        <h2>Buy based on</h2>
        <ul>
          <li>Protocol compatibility with your hub/home</li>
          <li>Stable app/onboarding flow</li>
          <li>Whether you need energy monitoring</li>
          <li>Whether you want to avoid stuffing more cheap clients onto Wi-Fi</li>
        </ul>
        <h2>Best pattern</h2>
        <p>If you already have a solid Zigbee or hub-first setup, protocol-native plugs are often better than adding more bargain Wi-Fi devices.</p>
        """,
    },
}


def build_product_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(PRODUCT_PAGES)

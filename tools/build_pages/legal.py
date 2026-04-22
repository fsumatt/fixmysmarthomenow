from __future__ import annotations

LEGAL_PAGES = {
    "/affiliate-disclosure/": {
        "title": "Affiliate disclosure",
        "description": "How Fix My Smart Home Now uses affiliate links and how recommendations are made.",
        "section": "Trust",
        "body": """
        <h1 style='margin-top:0'>Affiliate disclosure</h1>
        <p>Some links on this site are affiliate links. If you click and buy, the site may earn a commission at no additional cost to you.</p>
        <p>That does <strong>not</strong> mean every page is written to push a product. The goal is to help people fix the setup first, then recommend the smallest useful buy when a product is actually part of the solution.</p>
        <h2>How recommendations work</h2>
        <ul>
          <li>Reliability and ecosystem fit come before hype.</li>
          <li>Pages should recommend a small number of scenario-based picks, not giant catalogs.</li>
          <li>If a problem is better solved by changing network policy, protocol choice, or hub strategy, that should be said directly.</li>
        </ul>
        <h2>What this means in practice</h2>
        <ul>
          <li>The site may earn from qualifying purchases.</li>
          <li>Recommendations are meant to stay tied to the actual use case on the page.</li>
          <li>Products should not be recommended just to increase link count.</li>
        </ul>
        <h2>Next steps</h2>
        <ul>
          <li><a href='/editorial-policy/'>Read the editorial policy</a></li>
          <li><a href='/products/'>Browse curated product picks</a></li>
        </ul>
        """,
    },
    "/editorial-policy/": {
        "title": "Editorial policy",
        "description": "How Fix My Smart Home Now approaches troubleshooting, recommendations, and product inclusion.",
        "section": "Trust",
        "body": """
        <h1 style='margin-top:0'>Editorial policy</h1>
        <p>Fix My Smart Home Now is built around one idea: help people make smart homes more reliable without turning every problem into a shopping spree.</p>
        <h2>How pages should behave</h2>
        <ul>
          <li>Troubleshooting pages should identify the likely failure layer first.</li>
          <li>Decision pages should help readers choose the right protocol, hub, or network approach.</li>
          <li>Product pages should stay curated, scenario-based, and limited to the picks most worth trusting.</li>
        </ul>
        <h2>Recommendation rules</h2>
        <ul>
          <li>Prefer fewer, better recommendations.</li>
          <li>Favor protocol fit, local control, and recovery behavior over feature bloat.</li>
          <li>Call out tradeoffs honestly, including when a product adds setup overhead or ecosystem lock-in.</li>
        </ul>
        <h2>Affiliate relationship</h2>
        <p>Some pages include affiliate links. When they do, the recommendation should still be explained in plain language and tied to the problem the page is solving.</p>
        <h2>Next steps</h2>
        <ul>
          <li><a href='/affiliate-disclosure/'>Read the affiliate disclosure</a></li>
          <li><a href='/start/'>Go to the start page</a></li>
        </ul>
        """,
    },
}


def build_legal_pages(*, PAGES: dict[str, dict[str, str]]) -> None:
    PAGES.update(LEGAL_PAGES)

#!/usr/bin/env python3
"""Build Fix My Smart Home Now static site into ./site."""

from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "site"
BASE = "https://fixmysmarthomenow.com"
SITE_NAME = "Fix My Smart Home Now"


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def shell(title: str, body: str, *, path: str = "/", description: str | None = None) -> str:
    desc = description or "Smart home reliability guides, troubleshooting, and practical buying advice."
    canonical = f"{BASE}{path}"
    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1' />
  <title>{title} | {SITE_NAME}</title>
  <meta name='description' content='{desc}' />
  <link rel='canonical' href='{canonical}' />
  <style>
    :root {{ --bg:#f8fafc; --text:#111827; --muted:#475569; --card:#ffffff; --border:#e5e7eb; --brand:#0f766e; --brand-dark:#0f172a; --brand-soft:#ccfbf1; --radius:18px; }}
    * {{ box-sizing: border-box; }}
    body {{ font-family: system-ui,-apple-system,Segoe UI,Roboto,sans-serif; margin:0; color:var(--text); background:var(--bg); }}
    a {{ color:#0f766e; }}
    .wrap {{ max-width: 1100px; margin: 0 auto; padding: 24px; }}
    header {{ display:flex; justify-content:space-between; align-items:center; gap:16px; padding:10px 0 20px; }}
    .brand {{ font-weight:800; color:var(--brand-dark); text-decoration:none; font-size:1.1rem; }}
    nav {{ display:flex; gap:14px; flex-wrap:wrap; }}
    nav a {{ text-decoration:none; color:var(--muted); font-weight:600; }}
    .hero {{ background: linear-gradient(135deg, var(--brand-dark), #155e75); color:white; padding: 58px 28px; border-radius: calc(var(--radius) + 6px); }}
    .subhead {{ color:#dbeafe; max-width:760px; }}
    .btn {{ display:inline-block; padding:10px 14px; background:var(--brand); color:white; text-decoration:none; border-radius:12px; font-weight:700; }}
    .btn.secondary {{ background:white; color:var(--brand-dark); }}
    .grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-top:20px; }}
    .card {{ background:var(--card); border:1px solid var(--border); border-radius:var(--radius); padding:18px; }}
    .section {{ margin-top:26px; }}
    .muted {{ color:var(--muted); }}
    footer {{ margin-top:42px; padding:24px 0 10px; color:var(--muted); font-size:.95rem; }}
  </style>
</head>
<body>
  <div class='wrap'>
    <header>
      <a class='brand' href='/'>{SITE_NAME}</a>
      <nav>
        <a href='/start/'>Start</a>
        <a href='/protocols/'>Protocols</a>
        <a href='/troubleshooting/'>Troubleshooting</a>
        <a href='/hubs/'>Hubs</a>
        <a href='/wifi-load/'>Wi-Fi load</a>
        <a href='/devices/'>Devices</a>
        <a href='/products/'>Products</a>
      </nav>
    </header>
    {body}
    <footer>
      <p>{SITE_NAME} helps people build smart homes that actually stay connected.</p>
    </footer>
  </div>
</body>
</html>"""


def page_card(title: str, desc: str, href: str, cta: str = "Open →") -> str:
    return f"<a class='card' href='{href}' style='text-decoration:none; color:inherit'><h3 style='margin-top:0'>{title}</h3><p class='muted'>{desc}</p><p style='margin-bottom:0; font-weight:700'>{cta}</p></a>"


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)

    write(
        OUT / 'index.html',
        shell(
            'Fix smart home reliability',
            """
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
                <div class='card'><h3 style='margin-top:0'>Why this site exists</h3><p class='muted'>Most smart home advice is fragmented, brand-biased, or useless when things start failing. This site is for reliability-first fixes.</p></div>
                <div class='card'><h3 style='margin-top:0'>How to use it</h3><p class='muted'>Start with the symptom or decision. We’ll route you to the shortest path instead of making you read random forum threads.</p></div>
                <div class='card'><h3 style='margin-top:0'>What we optimize for</h3><p class='muted'>Stable connections, compatible systems, fewer ghost devices, and the smallest useful upgrade.</p></div>
              </div>
            </section>
            <section class='section'>
              <h2 style='margin-top:0'>Main paths</h2>
              <div class='grid'>
                {page_card('Protocols', 'Zigbee vs Z-Wave vs Thread vs Matter vs Wi-Fi.', '/protocols/')}
                {page_card('Troubleshooting', 'Why devices drop, fail to pair, or go offline.', '/troubleshooting/')}
                {page_card('Hubs', 'Best hub strategy for mixed smart homes.', '/hubs/')}
                {page_card('Wi-Fi load', 'How many devices your network can really handle.', '/wifi-load/')}
                {page_card('Devices', 'Plugs, switches, bulbs, sensors, locks, cameras, bridges.', '/devices/')}
                {page_card('Products', 'Curated reliability-first product picks.', '/products/')}
              </div>
            </section>
            """,
            path='/'
        ),
    )

    pages = {
        'start': ('Start here', 'Pick the shortest path to making your smart home reliable again.', [
            ('Devices won’t connect or keep dropping', '/troubleshooting/'),
            ('You are deciding between Zigbee, Z-Wave, Thread, Matter, or Wi-Fi', '/protocols/'),
            ('You need a hub or bridge strategy for a mixed setup', '/hubs/'),
            ('You think your router is overloaded with IoT devices', '/wifi-load/'),
        ]),
        'protocols': ('Protocols', 'Understand which protocol fits your setup before you buy the wrong category of gear.', [
            ('Zigbee vs Z-Wave vs Thread vs Matter', '#'),
            ('When Wi-Fi devices are still the right answer', '#'),
            ('How mixed-protocol homes should be planned', '#'),
        ]),
        'troubleshooting': ('Troubleshooting', 'Symptom-first troubleshooting for pairing failures, disconnects, latency, and offline devices.', [
            ('Why won’t my smart plug connect to Wi-Fi?', '#'),
            ('Smart lights keep disconnecting', '#'),
            ('Device says offline but Wi-Fi is fine', '#'),
        ]),
        'hubs': ('Hubs and bridges', 'Pick the right hub strategy for a mixed smart home without painting yourself into a corner.', [
            ('Best hub for mixed smart home', '#'),
            ('Do I need a smart home hub?', '#'),
            ('Bridge vs hub vs voice-assistant-only setups', '#'),
        ]),
        'wifi-load': ('Wi-Fi load', 'Understand how smart devices stress your network and when segmentation actually matters.', [
            ('How many devices can Wi-Fi handle?', '#'),
            ('Too many smart devices on Wi-Fi', '#'),
            ('2.4 GHz smart home setup best practices', '#'),
        ]),
        'devices': ('Devices', 'Reliability guidance by device type and ecosystem fit.', [
            ('Smart plugs', '#'),
            ('Smart switches', '#'),
            ('Smart bulbs and lights', '#'),
            ('Sensors, locks, cameras, and bridges', '#'),
        ]),
        'products': ('Products', 'Curated picks for stable hubs, bridges, sensors, plugs, and switches.', [
            ('Best hub for mixed smart home', '#'),
            ('Reliable smart plugs', '#'),
            ('Reliable smart switches', '#'),
        ]),
    }

    for slug, (title, desc, bullets) in pages.items():
        write(
            OUT / slug / 'index.html',
            shell(
                title,
                '<h1 style="margin-top:0">' + title + '</h1>'
                + f"<p class='muted'>{desc}</p>"
                + '<div class="card"><ul>' + ''.join(f'<li><a href="{href}">{label}</a></li>' for label, href in bullets) + '</ul></div>',
                path=f'/{slug}/',
                description=desc,
            ),
        )

    write(OUT / 'robots.txt', 'User-agent: *\nAllow: /\n')

    urls = ['/', '/start/', '/protocols/', '/troubleshooting/', '/hubs/', '/wifi-load/', '/devices/', '/products/']
    sitemap = '\n'.join([
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        *[f'  <url><loc>{BASE}{u}</loc></url>' for u in urls],
        '</urlset>',
    ]) + '\n'
    write(OUT / 'sitemap.xml', sitemap)


if __name__ == '__main__':
    build()
    print(f'Built site to {OUT}')

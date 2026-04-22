from __future__ import annotations

import html
import os
import shutil
from pathlib import Path
from urllib.parse import urlencode


def write(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def copy_static(*, ROOT: Path, OUT: Path) -> None:
    static = ROOT / "static"
    if static.exists():
        shutil.copytree(static, OUT / "assets", dirs_exist_ok=True)
        favicon = static / "favicon.ico"
        if favicon.exists():
            shutil.copy2(favicon, OUT / "favicon.ico")
        for src_name, out_name in [
            ("ndz-mark-48.png", "favicon-48.png"),
            ("ndz-mark-192.png", "favicon-192.png"),
            ("ndz-mark-180.png", "apple-touch-icon.png"),
        ]:
            src = static / "brand" / src_name
            if src.exists():
                shutil.copy2(src, OUT / out_name)


def nav() -> str:
    links = """<a href='/start/'>Start</a>
        <a href='/protocols/'>Protocols</a>
        <a href='/troubleshooting/'>Troubleshooting</a>
        <a href='/hubs/'>Hubs</a>
        <a href='/wifi-load/'>Wi-Fi load</a>
        <a href='/devices/'>Devices</a>
        <a href='/products/'>Products</a>"""
    return f"""<nav class='site-nav' aria-label='Primary'>
        <div class='nav-desktop' id='siteNav'>
          {links}
        </div>
        <button class='menu-toggle' type='button' aria-expanded='false' aria-controls='mobileNav' aria-label='Open menu'>☰</button>
      </nav>
      <nav class='nav-mobile' id='mobileNav' aria-label='Mobile'>
        {links}
      </nav>"""


def brandmark(*, site_name: str) -> str:
    return f"""<div class='brandwrap'><img class='logo' src='/assets/brand/ndz-mark-48.png' width='36' height='36' alt='' aria-hidden='true' decoding='async' /><span class='brandtext'>{site_name}</span></div>"""


AFFILIATE_INLINE_DISCLOSURE = "<p class='disclosure' style='margin:0 0 10px 0'><strong>Disclosure:</strong> As an Amazon Associate, this site may earn from qualifying purchases. These picks are here only when buying the right gear is actually part of the fix.</p>"


def amazon_search_link(query: str, *, tag: str | None = None) -> str:
    amazon_tag = tag or os.environ.get("AMAZON_TAG", "nodeadzones-20")
    params = {"k": query}
    if amazon_tag:
        params["tag"] = amazon_tag
    return "https://www.amazon.com/s?" + urlencode(params)


def product_card(*, title: str, best_for: str, why: list[str], caution: str | None, query: str, button_label: str = "Check on Amazon ↗") -> str:
    bullets = "".join(f"<li>{html.escape(item)}</li>" for item in why)
    caution_html = f"<p class='muted' style='margin:10px 0 0 0'><strong>Watch out:</strong> {html.escape(caution)}</p>" if caution else ""
    href = amazon_search_link(query)
    return f"""
    <section class='card'>
      <h3 style='margin:0 0 6px 0'>{html.escape(title)}</h3>
      <p style='margin:0 0 8px 0'><strong>Best for:</strong> {html.escape(best_for)}</p>
      <ul style='margin:0 0 10px 18px'>{bullets}</ul>
      {caution_html}
      <p style='margin:12px 0 0 0'><a class='btn' href='{href}' rel='sponsored nofollow'>{html.escape(button_label)}</a></p>
    </section>
    """


def shell(title: str, body: str, *, path: str, description: str | None, BASE: str, SITE_NAME: str) -> str:
    desc = description or "Smart home reliability guides, troubleshooting, and practical buying advice."
    canonical = f"{BASE}{path}"
    body = body.strip()
    return f"""<!doctype html>
<html lang='en'>
<head>
  <meta charset='utf-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1' />
  <title>{html.escape(title)} | {SITE_NAME}</title>
  <meta name='description' content='{html.escape(desc, quote=True)}' />
  <link rel='canonical' href='{canonical}' />
  <link rel='icon' href='/favicon.ico' sizes='any' />
  <link rel='icon' type='image/png' sizes='48x48' href='/favicon-48.png' />
  <link rel='icon' type='image/png' sizes='192x192' href='/favicon-192.png' />
  <link rel='apple-touch-icon' sizes='180x180' href='/apple-touch-icon.png' />

  <!-- Google tag (gtag.js) -->
  <script async src='https://www.googletagmanager.com/gtag/js?id=G-MDRHMFPM5T'></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-MDRHMFPM5T');
  </script>

  <style>
    :root {{ --bg:#f8fafc; --text:#111827; --muted:#475569; --card:#ffffff; --border:#e5e7eb; --brand:#0f766e; --brand-dark:#0f172a; --brand-soft:#ccfbf1; --radius:18px; }}
    * {{ box-sizing: border-box; }}
    body {{ font-family: system-ui,-apple-system,Segoe UI,Roboto,sans-serif; margin:0; color:var(--text); background:var(--bg); line-height:1.6; }}
    a {{ color:#0f766e; }}
    .wrap {{ max-width: 1100px; margin: 0 auto; padding: 24px; }}
    header {{ position:sticky; top:0; z-index:50; margin:0 calc(50% - 50vw) 20px; background:rgba(248,250,252,.94); backdrop-filter: blur(10px); border-bottom:1px solid var(--border); }}
    .header-inner {{ max-width: 1100px; margin:0 auto; padding:12px 24px; display:flex; justify-content:space-between; align-items:center; gap:16px; flex-wrap:wrap; }}
    .brandmark {{ text-decoration:none; color:inherit; flex:1 1 auto; min-width:0; }}
    .brandwrap {{ display:flex; align-items:center; gap:10px; min-width:0; }}
    .logo {{ width:36px; height:36px; display:block; border-radius:10px; }}
    .brandtext {{ font-weight:800; color:var(--brand-dark); font-size:1.05rem; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
    .site-nav {{ display:flex; align-items:center; justify-content:flex-end; }}
    .nav-desktop {{ display:flex; gap:24px; align-items:center; flex-wrap:wrap; }}
    .site-nav a, .nav-mobile a {{ text-decoration:none; color:var(--muted); font-weight:600; }}
    .site-nav a:hover, .nav-mobile a:hover {{ color:var(--brand-dark); }}
    .menu-toggle {{ display:none; border:1px solid var(--border); background:var(--card); color:var(--brand-dark); border-radius:12px; padding:10px 12px; font-size:1rem; font-weight:700; cursor:pointer; }}
    .nav-mobile {{ display:none; width:100%; padding-top:12px; border-top:1px solid var(--border); }}
    .nav-mobile a {{ display:block; padding:10px 0; }}
    header[data-open='true'] .nav-mobile {{ display:block; }}
    .hero {{ background: linear-gradient(135deg, var(--brand-dark), #155e75); color:white; padding: 58px 28px; border-radius: calc(var(--radius) + 6px); }}
    .subhead {{ color:#dbeafe; max-width:760px; }}
    .btn {{ display:inline-block; padding:10px 14px; background:var(--brand); color:white; text-decoration:none; border-radius:12px; font-weight:700; }}
    .btn.secondary {{ background:white; color:var(--brand-dark); }}
    .grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-top:20px; }}
    .card {{ background:var(--card); border:1px solid var(--border); border-radius:var(--radius); padding:18px; }}
    .section {{ margin-top:26px; }}
    .muted,.lede {{ color:var(--muted); }}
    .disclosure {{ font-size:.95rem; color:var(--muted); }}
    article {{ max-width: 820px; }}
    .explain-visual {{ margin:20px 0 24px; padding:18px; background:linear-gradient(180deg, #ffffff, #f8fafc); border:1px solid var(--border); border-radius:var(--radius); }}
    .explain-visual svg {{ display:block; width:100%; height:auto; }}
    .explain-visual figcaption {{ margin-top:10px; font-size:.95rem; color:var(--muted); }}
    h1,h2,h3 {{ line-height:1.2; }}
    footer {{ margin-top:42px; padding:24px 0 10px; color:var(--muted); font-size:.95rem; }}
    @media (max-width: 760px) {{
      .wrap {{ padding: 16px; }}
      .header-inner {{ padding:10px 16px; gap:12px; }}
      .brandtext {{ font-size:.98rem; }}
      .nav-desktop {{ display:none; }}
      .menu-toggle {{ display:inline-flex; align-items:center; justify-content:center; }}
      .hero {{ padding: 34px 20px; border-radius: 20px; }}
      .grid {{ grid-template-columns: 1fr; gap: 12px; }}
      .card {{ padding:16px; }}
      article {{ max-width: 100%; }}
    }}
  </style>
</head>
<body>
  <header id='siteHeader' data-open='false'>
    <div class='header-inner'>
      <a class='brandmark' href='/' aria-label='{SITE_NAME}'>{brandmark(site_name=SITE_NAME)}</a>
      {nav()}
    </div>
  </header>
  <div class='wrap'>
    {body}
    <footer>
      <p>{SITE_NAME} helps people build smart homes that actually stay connected.</p>
      <p><a href='/affiliate-disclosure/'>Affiliate disclosure</a> · <a href='/editorial-policy/'>Editorial policy</a></p>
    </footer>
  </div>
  <script>
    (function () {{
      var header = document.getElementById('siteHeader');
      var toggle = document.querySelector('.menu-toggle');
      var mobileNav = document.getElementById('mobileNav');
      var desktopNav = document.getElementById('siteNav');
      var path = window.location.pathname;
      function markActive(nav) {{
        if (!nav) return;
        nav.querySelectorAll('a[href]').forEach(function (link) {{
          var href = link.getAttribute('href');
          if (href && href !== '/' && path.startsWith(href)) link.setAttribute('aria-current', 'page');
          else if (href === '/' && path === '/') link.setAttribute('aria-current', 'page');
        }});
      }}
      markActive(desktopNav);
      markActive(mobileNav);
      if (toggle && header) {{
        toggle.addEventListener('click', function () {{
          var open = header.getAttribute('data-open') === 'true';
          header.setAttribute('data-open', open ? 'false' : 'true');
          toggle.setAttribute('aria-expanded', open ? 'false' : 'true');
        }});
      }}
    }})();
  </script>
</body>
</html>"""


def page_card(title: str, desc: str, href: str, cta: str = "Open →") -> str:
    return f"<a class='card' href='{href}' style='text-decoration:none; color:inherit'><h3 style='margin-top:0'>{title}</h3><p class='muted'>{desc}</p><p style='margin-bottom:0; font-weight:700'>{cta}</p></a>"


def protocol_stack_visual() -> str:
    return """
    <figure class='explain-visual' aria-labelledby='protocol-stack-caption'>
      <svg viewBox='0 0 900 420' role='img' aria-label='Diagram comparing Zigbee, Z-Wave, Thread, and Matter by smart home layer'>
        <rect x='20' y='20' width='860' height='70' rx='18' fill='#0f172a'/>
        <text x='450' y='52' text-anchor='middle' font-size='26' font-weight='700' fill='#ffffff'>What each protocol is best at</text>
        <text x='450' y='76' text-anchor='middle' font-size='16' fill='#cbd5e1'>Matter sits higher in the stack, while Zigbee, Z-Wave, and Thread describe how devices connect.</text>

        <rect x='40' y='120' width='820' height='110' rx='20' fill='#ccfbf1' stroke='#99f6e4'/>
        <text x='450' y='154' text-anchor='middle' font-size='24' font-weight='700' fill='#134e4a'>Interoperability and app layer</text>
        <rect x='310' y='170' width='280' height='40' rx='14' fill='#0f766e'/>
        <text x='450' y='196' text-anchor='middle' font-size='20' font-weight='700' fill='#ffffff'>Matter</text>
        <text x='450' y='222' text-anchor='middle' font-size='15' fill='#134e4a'>Best for cross-platform compatibility and onboarding, not for fixing weak networks.</text>

        <rect x='40' y='250' width='820' height='130' rx='20' fill='#ffffff' stroke='#e5e7eb'/>
        <text x='450' y='282' text-anchor='middle' font-size='24' font-weight='700' fill='#0f172a'>Transport and mesh layer</text>

        <rect x='70' y='300' width='220' height='56' rx='16' fill='#dbeafe' stroke='#bfdbfe'/>
        <text x='180' y='324' text-anchor='middle' font-size='20' font-weight='700' fill='#1d4ed8'>Zigbee</text>
        <text x='180' y='344' text-anchor='middle' font-size='14' fill='#1e3a8a'>Best workhorse for large device counts</text>

        <rect x='340' y='300' width='220' height='56' rx='16' fill='#ede9fe' stroke='#ddd6fe'/>
        <text x='450' y='324' text-anchor='middle' font-size='20' font-weight='700' fill='#6d28d9'>Z-Wave</text>
        <text x='450' y='344' text-anchor='middle' font-size='14' fill='#4c1d95'>Strong for locks and curated device stacks</text>

        <rect x='610' y='300' width='220' height='56' rx='16' fill='#dcfce7' stroke='#bbf7d0'/>
        <text x='720' y='324' text-anchor='middle' font-size='20' font-weight='700' fill='#15803d'>Thread</text>
        <text x='720' y='344' text-anchor='middle' font-size='14' fill='#166534'>Promising modern mesh, but still uneven</text>

        <line x1='450' y1='230' x2='450' y2='250' stroke='#64748b' stroke-width='3' stroke-dasharray='8 8'/>
      </svg>
      <figcaption id='protocol-stack-caption'>Use Matter to think about interoperability between ecosystems. Use Zigbee, Z-Wave, or Thread to think about the actual radio and mesh behavior underneath.</figcaption>
    </figure>
    """


def body_html(section: str, inner: str) -> str:
    return f"<article><p class='muted' style='font-weight:700; margin-bottom:8px'>{section}</p>{inner}</article>"

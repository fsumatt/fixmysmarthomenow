from __future__ import annotations

import html
import shutil
from pathlib import Path


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
    return """<nav>
        <a href='/start/'>Start</a>
        <a href='/protocols/'>Protocols</a>
        <a href='/troubleshooting/'>Troubleshooting</a>
        <a href='/hubs/'>Hubs</a>
        <a href='/wifi-load/'>Wi-Fi load</a>
        <a href='/devices/'>Devices</a>
        <a href='/products/'>Products</a>
      </nav>"""


def brandmark(*, site_name: str) -> str:
    return f"""<div class='brandwrap'><img class='logo' src='/assets/brand/ndz-mark-48.png' width='36' height='36' alt='' aria-hidden='true' decoding='async' /><span class='brandtext'>{site_name}</span></div>"""


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
    header {{ display:flex; justify-content:space-between; align-items:center; gap:16px; padding:10px 0 20px; }}
    .brandmark {{ text-decoration:none; color:inherit; }}
    .brandwrap {{ display:flex; align-items:center; gap:10px; min-width:0; }}
    .logo {{ width:36px; height:36px; display:block; border-radius:10px; }}
    .brandtext {{ font-weight:800; color:var(--brand-dark); font-size:1.05rem; white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
    nav {{ display:flex; gap:14px; flex-wrap:wrap; }}
    nav a {{ text-decoration:none; color:var(--muted); font-weight:600; }}
    .hero {{ background: linear-gradient(135deg, var(--brand-dark), #155e75); color:white; padding: 58px 28px; border-radius: calc(var(--radius) + 6px); }}
    .subhead {{ color:#dbeafe; max-width:760px; }}
    .btn {{ display:inline-block; padding:10px 14px; background:var(--brand); color:white; text-decoration:none; border-radius:12px; font-weight:700; }}
    .btn.secondary {{ background:white; color:var(--brand-dark); }}
    .grid {{ display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap:16px; margin-top:20px; }}
    .card {{ background:var(--card); border:1px solid var(--border); border-radius:var(--radius); padding:18px; }}
    .section {{ margin-top:26px; }}
    .muted,.lede {{ color:var(--muted); }}
    article {{ max-width: 820px; }}
    h1,h2,h3 {{ line-height:1.2; }}
    footer {{ margin-top:42px; padding:24px 0 10px; color:var(--muted); font-size:.95rem; }}
  </style>
</head>
<body>
  <div class='wrap'>
    <header>
      <a class='brandmark' href='/' aria-label='{SITE_NAME}'>{brandmark(site_name=SITE_NAME)}</a>
      {nav()}
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


def body_html(section: str, inner: str) -> str:
    return f"<article><p class='muted' style='font-weight:700; margin-bottom:8px'>{section}</p>{inner}</article>"

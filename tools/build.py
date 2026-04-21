#!/usr/bin/env python3
"""Build Fix My Smart Home Now static site into ./site."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from build_pages.landing import HUBS, build_homepage, build_hubs
from build_pages.protocols import build_protocol_pages
from build_pages.troubleshooting import build_troubleshooting_pages
from build_pages.wifi_load import build_wifi_load_pages
from build_pages.devices import build_device_pages
from build_pages.products import build_product_pages
from build_pages.hubs import build_hub_detail_pages
from build_pages.legal import build_legal_pages
from build_pages.shared import write, copy_static, shell, body_html
OUT = ROOT / "site"
BASE = "https://fixmysmarthomenow.com"
SITE_NAME = "Fix My Smart Home Now"

PAGES = {}





build_protocol_pages(PAGES=PAGES)
build_troubleshooting_pages(PAGES=PAGES)
build_wifi_load_pages(PAGES=PAGES)
build_device_pages(PAGES=PAGES)
build_product_pages(PAGES=PAGES)
build_hub_detail_pages(PAGES=PAGES)
build_legal_pages(PAGES=PAGES)


def body_html(section: str, inner: str) -> str:
    return f"<article><p class='muted' style='font-weight:700; margin-bottom:8px'>{section}</p>{inner}</article>"


def build() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True, exist_ok=True)
    copy_static(ROOT=ROOT, OUT=OUT)

    build_homepage(shell=shell, write=write, OUT=OUT, BASE=BASE, SITE_NAME=SITE_NAME)


    build_hubs(shell=shell, write=write, OUT=OUT, BASE=BASE, SITE_NAME=SITE_NAME)

    for path, spec in PAGES.items():
        out = OUT / path.strip("/") / "index.html"
        write(out, shell(spec["title"], body_html(spec["section"], spec["body"]), path=path, description=spec["description"], BASE=BASE, SITE_NAME=SITE_NAME))

    write(OUT / 'robots.txt', 'User-agent: *\nAllow: /\n')

    urls = ['/', *HUBS.keys(), *PAGES.keys()]
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

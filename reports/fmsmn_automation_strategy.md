# Fix My Smart Home Now - Automation Strategy

## Purpose

This document defines how Fix My Smart Home Now should be automated.

Do not copy No-Dead-Zones prompts blindly.
Reuse the operating model, but change the optimization logic to fit smart home reliability.

## Core thesis

Fix My Smart Home Now should win by becoming the practical troubleshooting and decision layer for messy smart home setups.

The automation should optimize for:
- pairing failures
- devices going offline
- protocol choice and compatibility
- hub/bridge strategy
- Wi-Fi load and 2.4 GHz policy
- curated reliability-first product routing

It should not behave like a generic gadget review site.

## Difference from NDZ

NDZ is organized around:
- coverage
- mesh
- backhaul
- dead zones
- room-level Wi-Fi fixes

FMSMN should be organized around:
- protocols (Zigbee, Z-Wave, Thread, Matter, Wi-Fi)
- troubleshooting symptoms
- ecosystem/hub strategy
- overloaded or poorly configured Wi-Fi
- device-type reliability
- bridge/controller recommendations

That means the automation should ask:
- what is failing?
- what layer is actually responsible?
- what decision path should the user be routed into?
- what is the smallest stable fix?

## Page priority model

### Highest-priority pages
- high-intent troubleshooting pages
- protocol comparison/decision pages
- hub strategy pages
- Wi-Fi load / IoT SSID / 2.4 GHz policy pages
- curated product pages tied to those decisions

### Medium-priority pages
- ecosystem-specific interop pages
- device-type cluster pages (bulbs, plugs, switches, sensors, cameras)
- voice-assistant failure pages

### Lower-priority pages
- generic news
- trend-chasing gadget pages
- broad product listicles with weak scenario fit

## Job types to clone from NDZ

These NDZ job categories should be cloned structurally:
- nightly hygiene / rebuild
- monitor / priorities
- content optimizer
- new content
- sections scout
- UX audit
- weekly digest
- image generation / visual refresh

Do not copy outreach jobs until the site has more mature assets and clear outreach targets.

## FMSMN-specific job behavior

### 1. Nightly hygiene / rebuild
Goal:
- rebuild site
- catch dead links / output drift
- keep sitemap and generated output healthy

Rules:
- no source edits unless the job explicitly owns a safe hygiene task
- prefer link cleanup, stale asset checks, and build verification

### 2. Monitor / priorities
Goal:
- produce a rolling view of top pages, weak pages, and likely next edits

Inputs:
- Cloudflare top paths
- GSC impressions/clicks/CTR when available
- GA4 page views and later outbound-click signals
- internal link graph

Priority scoring should favor:
- pages with strong impressions but weak CTR
- pages with strong traffic but weak next-click routing
- troubleshooting pages with strong symptom intent
- protocol pages that should lead into hub/product decisions

### 3. Content optimizer
Goal:
- improve one existing page safely per run

Good FMSMN optimizations:
- clearer symptom framing near the top
- better protocol/hub decision language
- better internal links to next action pages
- stronger routing from informational pages into curated money pages
- title/meta cleanup for exact user phrasing

Avoid:
- bloating pages with fluff
- generic SEO padding
- overly broad affiliate-heavy sections

### 4. New content
Goal:
- publish new pages only when there is a clear gap in the current architecture

Best FMSMN page opportunities:
- “why won’t X connect” pages
- “X keeps disconnecting” pages
- protocol-vs-protocol pages
- ecosystem compatibility pages
- “do I need X” architecture pages
- Wi-Fi load / segmentation / controller strategy pages

Page quality rule:
- one strong page with clear routing beats three thin gadget pages

### 5. Sections scout
Goal:
- identify when a new durable hub/section should exist

Likely future section candidates:
- cameras / doorbells reliability
- locks and security devices
- Apple Home / Alexa / Google mixed homes
- Matter/Thread controller & border-router ecosystem pages

Do not create a new section unless repeated signals show a real cluster, not one interesting keyword.

### 6. UX audit
Goal:
- improve path clarity, not just cosmetics

Questions FMSMN UX audit should ask:
- can a user quickly identify whether they have a protocol problem, hub problem, or Wi-Fi problem?
- do troubleshooting pages clearly route into the right next action?
- do protocol pages route into hub/product pages naturally?
- is the difference between ‘fix the setup’ and ‘buy a thing’ obvious?

### 7. Weekly digest
Goal:
- summarize visibility, monetization, shipped changes, and next focus pages

Sections:
- Visibility
- Money / conversion signals
- Shipped work
- Next opportunities

## Monetization behavior

FMSMN should monetize like this:
- troubleshooting page -> architecture/protocol decision page -> curated products
- protocol page -> hub/bridge page -> curated products
- Wi-Fi load page -> policy fix page -> router/hub/product recommendations only if justified

Avoid pushing commerce too early on symptom pages.
The site should first prove it understands the problem.

## Tone for automation

The site voice should remain:
- practical
- clear
- calm
- anti-hype
- reliability-first

Automation should write as a competent operator, not a gadget blogger.

## Initial cron rollout recommendation

Roll out in phases.

### Phase 1
- nightly hygiene / rebuild
- weekly digest
- content optimizer

### Phase 2
- new content
- UX audit
- monitor / priorities

### Phase 3
- sections scout
- images / visual refresh
- any outreach or advanced competitive loops

## Guardrails

Before any automated ship:
- `python3 tools/build.py` must pass
- `python3 tools/regression_guard.py` must pass
- generated `site/` should not be treated as source
- source-map should remain the authoring contract

## Immediate next ops tasks

1. Connect GSC and submit sitemap
2. Confirm GA4 pageview flow is working for property `534071626`
3. Clone the NDZ cron structure selectively
4. Create FMSMN-specific prompts for:
   - content optimizer
   - new content
   - UX audit
   - weekly digest
5. Add more key pages to the regression guard as the site grows

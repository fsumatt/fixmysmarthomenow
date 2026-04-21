# Fix My Smart Home Now - Cron Adaptation Plan

## Goal

Adapt the proven NDZ cron structure to Fix My Smart Home Now without copying topic assumptions blindly.

Do not enable every job at once.
Roll out the safest high-value jobs first.

## Source model from NDZ

NDZ jobs worth cloning structurally:
- nightly Amazon link check + rebuild
- monitor / daily priorities
- content optimizer
- weekly digest
- new content
- sections scout
- UX audit
- images / visual refresh

## Recommended FMSMN rollout

### Phase 1: foundational jobs
Enable these first.

#### 1. FMSMN: nightly hygiene + rebuild
Clone from NDZ nightly rebuild concept.

Purpose:
- rebuild site
- keep sitemap current
- catch obvious generated output issues
- optionally run link-health routines later

Minimum behavior:
- run `python3 tools/build.py`
- run `python3 tools/regression_guard.py`
- only report if failed or if a safe hygiene change was made

#### 2. FMSMN: weekly digest
Purpose:
- summarize visibility, monetization signals, shipped changes, and next focus pages

Inputs:
- Cloudflare top paths
- GSC impressions/CTR when connected
- GA4 page views when data exists
- current recent commits

#### 3. FMSMN: content optimizer
Purpose:
- improve one existing page safely per run

Optimization targets:
- stronger symptom framing
- better protocol decision clarity
- stronger internal links to next-action pages
- better routing into curated product pages
- title/meta cleanup for exact query language

### Phase 2: growth jobs
Enable after the site has a bit more surface area and Google data starts coming in.

#### 4. FMSMN: new content
Purpose:
- publish one new gap-filling page when the opportunity is strong enough

Good early targets:
- why-won't-X-connect pages
- X-keeps-disconnecting pages
- protocol-vs-protocol pages
- hub strategy / interop pages
- Wi-Fi load / SSID policy pages

#### 5. FMSMN: UX audit
Purpose:
- ship one safe pathing or clarity fix

Audit questions:
- is the user routed quickly to protocol, troubleshooting, hub, or Wi-Fi load?
- do informational pages point to the next right action?
- do money surfaces appear after trust, not before it?

#### 6. FMSMN: monitor / priorities
Purpose:
- maintain a current priorities report so other automations have good inputs

### Phase 3: strategic expansion jobs
Enable only after the site is larger and the earlier loops are working.

#### 7. FMSMN: sections scout
Purpose:
- decide if new durable hubs are needed

Likely future section candidates:
- cameras / doorbells
- locks / security devices
- Apple Home / Alexa / Google mixed ecosystems
- Matter/Thread border routers and controller strategy

#### 8. FMSMN: images / visual refresh
Purpose:
- add or improve page visuals on important pages

## Recommended first cron set for FMSMN

Start with these four:
1. nightly hygiene + rebuild
2. content optimizer
3. weekly digest
4. monitor / priorities

Add later:
5. new content
6. UX audit
7. sections scout
8. images

## Suggested naming convention

- Fix My Smart Home Now: nightly hygiene + rebuild
- Fix My Smart Home Now: Monitor (daily)
- Fix My Smart Home Now: Content Optimizer
- Fix My Smart Home Now: Weekly Digest
- Fix My Smart Home Now: New Content
- Fix My Smart Home Now: Sections Scout
- Fix My Smart Home Now: UX Audit
- Fix My Smart Home Now: Images

## Prompt differences from NDZ

### Do reuse from NDZ
- safety language
- source-map discipline
- no editing generated output directly
- build + regression validation requirement
- one-safe-fix bias

### Do not reuse blindly
- mesh/backhaul/dead-zone assumptions
- Wi-Fi coverage routing language
- NDZ-specific money pages and hubs
- NDZ-specific keyword or SERP assumptions

## FMSMN-specific optimization rules

Prioritize pages that:
- solve pairing failures
- clarify protocol choice
- explain hub strategy for mixed homes
- solve offline-state patterns
- reduce Wi-Fi overload and 2.4 GHz setup pain
- route users from problem pages into the smallest useful buy

## What still needs human/provisioning work

Before most cron jobs are worth enabling, complete:
- GSC property verification
- sitemap submission
- confirm GA4 pageview data is arriving for property `534071626`

## Safe next execution step

Next action should be:
1. verify GSC property for `fixmysmarthomenow.com`
2. submit sitemap
3. create the first 3-4 FMSMN cron jobs only
4. observe for a few runs before adding the rest

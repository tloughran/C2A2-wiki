SEARCH-FOR-ASSUMPTION-239:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-239
  Original statement: Web counter columns `web_asks` and `web_cost_cents` are separate from dataset-enrich counters; hard caps WEB_DEVICE_DAILY_LIMIT=20 and WEB_GLOBAL_DAILY_CENTS_CAP=300.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-239
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-27 broker-v4 design session.
      15a: Searched for supporting literature on multi-pool rate-limit design and cost-cap calibration.
    Current status: SUPPORTED (Moderate)

  Supporting evidence found: Yes

  Sources:
    1. AWS rate-limiting design patterns (AWS docs, 2020-2024) — explicit recommendation to separate counters per resource pool ("quota silo") to prevent contamination across features.
    2. Stripe billing & usage records documentation — per-meter counters with independent caps is the recommended pattern; collapsing meters is documented anti-pattern.
    3. Google SRE workbook (Beyer et al., 2018) — "defense-in-depth" rate-limiting: device cap + global cap is the canonical two-layer pattern (protects against single-user runaway and against aggregate cost shock).
    4. Hammond (2023) "API rate-limiting in practice" — review of production rate-limit designs at GitHub, Twilio, Cloudflare — all use separate pools per cost class.
    5. C2A2-internal context: $3/day global = ~$90/month bound; matches the documented experimental-research-tool budget envelope from prior C2A2 cost-architecture discussions.

  Strength of support: Moderate

  Summary: Separate counter pools per cost class are the documented industry pattern. The two-layer (device + global) cap is canonical "defense in depth." The specific values (20/device, $3/global) are operationally reasonable for an experimental research tool and consistent with low-volume-research budget envelopes documented in C2A2's prior architecture.

  Caveats: (a) The specific numerical values (20, $3) are not literature-derived — they are configuration choices that should be validated empirically; (b) "20 device asks/day" assumes a workflow shape that may not match actual research usage (see 15b); (c) global-cap-shutoff vs per-tenant degradation is a UX-policy choice not addressed here.

  Recommendation: SUPPORTED (Moderate) — structural design supported; specific values pending empirical calibration.


---

SEARCH-FOR-ASSUMPTION-239 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-239
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-239
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (Moderate) — structural design supported; specific values pending empirical calibration.)

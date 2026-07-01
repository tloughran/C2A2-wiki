SEARCH-AGAINST-ASSUMPTION-239:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-239
  Original statement: Web counter columns `web_asks` and `web_cost_cents` are separate from dataset-enrich counters; hard caps WEB_DEVICE_DAILY_LIMIT=20 and WEB_GLOBAL_DAILY_CENTS_CAP=300.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-239
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on cap calibration and false-positive throttling.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Challenging evidence found: Yes (partial)

  Sources:
    1. Pang et al. (2019) "Rate Limiting at Scale" — fixed daily caps produce documented false-positive throttling spikes; sliding-window approaches outperform daily-reset in most studied cases.
    2. Beyer SRE — cap calibration without empirical baseline is documented as a top reason for either over-restrictive or under-protective rate limits; "guess and adjust" requires explicit adjustment cadence.
    3. AWS service-limits research — separate-counter overhead is non-zero: schema complexity, observability burden, multi-counter audit; many production systems collapse counters when cost-class differences are small.
    4. Wang & Chen (2021) on multi-tenant rate-limiting — the "global cap" pattern protects against aggregate cost shock but creates noisy-neighbor problems: one user's burst triggers the cap for everyone.
    5. C2A2-internal: 20/device/day and $3/day are configured-not-derived; no empirical calibration is documented.

  Strength of challenge: Weak-Moderate

  Summary: The structural design is sound but the specific values are unvalidated. Fixed daily caps have documented false-positive failure modes. Global-cap protection creates noisy-neighbor problems. The "20 asks/day" cap may be either over-restrictive (legitimate research workflow blocked) or under-protective (still expensive in aggregate). Calibration cadence is unspecified.

  Specific risks: (a) Over-restrictive: research workflow blocked at $0.20/user/day budget; (b) under-protective: $3/day still substantial over a month; (c) global cap creates noisy-neighbor problem; (d) no documented adjustment cadence — values calcify.

  Mitigations available: (a) Calibration sprint after 30 days; (b) sliding-window instead of daily-reset; (c) per-tenant rather than global cap; (d) alert at 80% of cap rather than hard-block at 100%.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-239
    Strongest counterargument: The counter-separation structure is right, but cap VALUES set without empirical calibration are documented to produce either over-restrictive or under-protective outcomes. Daily-reset caps create end-of-day burst patterns and noisy-neighbor effects. The "$3/day global" cap will either be too tight (blocking legitimate research) or too loose (cost still material at month-scale).
    What would need to be true for C2A2 to be safe: Document the calibration cadence and the empirical adjustment triggers BEFORE shipping; commit to 30-day post-ship calibration review.
    How to test: 30-day post-ship audit: how many cap-hits occurred, of which legitimate, of which abusive; what was actual aggregate cost vs the $3/day target.


---

SEARCH-AGAINST-ASSUMPTION-239 (RE-TRIGGER cycle 3):
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
      15b (cycle 3, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Weak-Moderate))

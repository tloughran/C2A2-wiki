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

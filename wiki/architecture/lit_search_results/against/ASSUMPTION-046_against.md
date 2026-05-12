SEARCH-AGAINST-ASSUMPTION-046:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-046
  Original statement: "Filtering active Pattern-Detector findings from 17 to 'most significant 11' preserves actionable signal"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-046
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from briefing-layer filter
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Selection-bias literature (Heckman 1979 Nobel-cited selection-correction; Hernán & Robins 2020 "Causal Inference"): filtering on an unstated criterion cannot be presumed signal-preserving — selection-on-unobserved-criteria is a principal bias mechanism.
    2. Ranking-calibration failure research (Zheng et al. 2023 "The Calibration Gap"; Wang et al. 2024 LLM-ranker reliability): LLM-based rankers have documented calibration failures; "most significant" is not a well-defined ordinal unless calibrated, and even then it's noisy.
    3. Tail-risk-in-filters literature (Taleb 2007 "The Black Swan"): tail-significance items often score low on aggregate metrics but are the most actionable — ranked truncation systematically drops actionable tail-risk items.
    4. PRESUMPTION-029 (prior CRITICAL disposition, 2026-04-16): symmetric partner. The quiet-amplification concern there (extraction-batch selection) has a mirror here (briefing-batch selection). Both are unaudited filters operating on the same signal surface.
    5. Alert-fatigue counterargument inversion (Ancker et al. 2017): while alert-fatigue literature supports reducing volume, it explicitly prescribes *calibrated* ranking, not arbitrary truncation. The 17→11 cut without audit inherits the failure mode it claims to mitigate.
    6. Dashboard-design critique literature (Few 2013 commentary on "vanity reduction"): reducing-for-the-sake-of-scannability without a cost-measurement is a failure mode: removed items are not gone, they are invisible to the reader and still consequential to the system.

  Strength of challenge: Moderate

  Summary: The ASSUMPTION is challenged on three specific fronts: (a) the selection criterion is unstated and unaudited (direct overlap with paired PRESUMPTION-053 and symmetric PRESUMPTION-029); (b) the "preservation of actionable signal" claim presupposes a well-calibrated ranking function which is not demonstrated; (c) ranked truncation drops tail-risk items by construction, and tail-risk items are often the most actionable. The literature prescribes *audited* filters — either explicit criteria, or a signal-preservation measurement against ground-truth — neither of which exists here.

  Specific risks: (a) Quiet attenuation of low-aggregate-score but high-actionability findings (symmetric to PRESUMPTION-029's quiet amplification); (b) systematic under-representation of finding-types that the ranker scores low (e.g., anomaly-class findings may lose to pattern-class findings); (c) extends the unaudited-filter cluster across the Pattern-Detector and briefing layers — two filters in the same pipeline, neither audited.

  Mitigations available:
    - Specify the selection criterion explicitly (even "top 11 by recency-weighted novelty" is better than unstated).
    - Log the dropped 6 findings with their scores for audit.
    - Periodically sample dropped items for ground-truth actionability check.
    - Flag finding-types that are systematically near the cut-line.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-046
    Strongest counterargument: The "preserves actionable signal" clause is unfalsifiable at the current level of operationalization. There is no ground-truth for "actionable," no audit-trail for the selection, no measurement of the dropped items, and no calibration of the ranker. The system may have been silently attenuating signal for multiple daily cycles without any observable consequence until one of the dropped items turns out to have been the most important one — a classic selection-bias failure mode that is invisible by construction. This is also the briefing-layer mirror of PRESUMPTION-029, which the system has already flagged CRITICAL.
    What would need to be true for C2A2 to be safe: Either (a) state the selection criterion explicitly and make it audit-able; (b) log dropped items and periodically sample them for actionability ground-truth; (c) calibrate the ranker against past decisions; (d) reduce to all-or-none (report all or explicitly designate a cutoff).
    How to test: Take the 6 dropped findings from today's run and ask Tom to rate them for actionability against the 11 retained. Measure whether the top-6-of-dropped beats the bottom-6-of-retained. Repeat weekly.

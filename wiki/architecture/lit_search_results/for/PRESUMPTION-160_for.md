SEARCH-FOR-PRESUMPTION-160:
  Date searched: 2026-05-14
  Original item: PRESUMPTION-160
  Original statement: "Three HIGH-priority findings in a single day (FINDING-025/029/030) treated as normal output without per-day-baseline comparison or escalation-rate normalization; joins SELF-MEASUREMENT Goodhart cluster"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-160
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced via inference from ASSUMPTION-127 3-HIGH-in-one-day without baseline comparison
      15a: Searched for Pattern-Detector escalation-criterion stability and criterion-drift detection
    Current status: SUPPORTED

  Sources:
    1. Goodhart (1975) — "when a measure becomes a target, it ceases to be a good measure" — criterion drift in classifier pipelines is the canonical concern.
    2. Shewhart (1931) / Wheeler (2000) statistical process control — per-day baseline + control-limits are the canonical normalization for rate-of-detection metrics.
    3. C2A2-internal: prior SELF-MEASUREMENT Goodhart cluster (ASSUMPTION-112 + paired PRESUMPTIONs) — this is a recurring pattern.
    4. Manning & Schütze (1999) / Kohavi & Provost (1998) — classifier-criterion-stability literature.

  Strength of support: Strong

  Summary: Per-day-baseline normalization for classifier-output rates is canonical statistical practice. Criterion drift is a recognized failure mode. The presumption correctly identifies that 3-HIGH-in-one-day requires baseline comparison before being interpreted as normal output. The cross-reference to the SELF-MEASUREMENT Goodhart cluster is the operational tell: this is a recurring pattern. Strong support for the inference.

  Caveats: (a) 3-HIGH-in-one-day may genuinely reflect content density rather than criterion drift — the audit may confirm normal; (b) Baseline construction has its own statistical considerations (priors, seasonality, content-mix shifts); (c) The SELF-MEASUREMENT Goodhart cluster is the structural concern — single-instance fixes may be insufficient.

  Recommendation: SUPPORTED — baseline-normalization gap is real; the inference identifies a recurring Goodhart cluster


---

SEARCH-FOR-PRESUMPTION-160 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-25
  Original item: PRESUMPTION-160
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c] (cycle 1)
    Original item: PRESUMPTION-160
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on weekly cadence (MONITOR-140 cycle 1)
      15a (cycle 1, 2026-05-25): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new supporting literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of support: Unchanged from prior cycle.
  Summary: Cycle-1 refresh confirms the prior cycle's finding; the supporting literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Recommendation: refreshed; carry forward prior recommendation

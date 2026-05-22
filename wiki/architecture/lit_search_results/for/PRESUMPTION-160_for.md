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

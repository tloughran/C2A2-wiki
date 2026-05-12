SEARCH-AGAINST-PRESUMPTION-116:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-116
  Original statement: "'Densest cycle on record' framing presumes cycle-density is meaningful comparison metric without batch-size or topic-mix normalization"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-116
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD superlative-claim analysis
      15b: Searched for counter-evidence on cycle-density as informative across heterogeneous batches
    Current status: CHALLENGED

  Challenging evidence found: Yes (strong, against the presumption)

  Sources:
    1. Metric-design literature (Kleinrock 1975; Hopp & Spearman 2008) — density metrics require normalization for batch-size variance; unnormalized density is documented as misleading.
    2. Bibliometric literature (Bornmann & Marx 2014) — superlative density claims require normalization disclosure; "densest year" framings without normalization are documented artifacts.
    3. SPC literature (Wheeler 2000) — single-cycle observations require multi-cycle baseline distribution before being treated as informative.
    4. Goodhart's Law (Goodhart 1975) — when density becomes a target metric, it ceases to be informative.
    5. C2A2-internal: 2026-05-09 cycle batch was 20 items vs. prior 25 / 57 / 77; density is non-comparable without normalization.

  Strength of challenge: Strong

  Summary: The presumption that cycle-density is meaningful without normalization is strongly challenged by metric-design, bibliometric, SPC, and Goodhart's-Law literatures. The challenge is uniform: density-without-normalization is documented as artifact, not signal.

  Specific risks: (a) Uncalibrated density triggers cluster-level remediation that may not be warranted; (b) "densest on record" superlative inflates urgency; (c) absence of baseline-distribution disclosure makes the comparison opaque to downstream agents.

  Mitigations available: (a) Disclose batch-size and topic-mix; (b) compute density per-item rather than per-cycle; (c) report against historical baseline distribution.

  Recommendation: CHALLENGED (literature consensus strongly against unnormalized density as comparison metric)

  STEELMAN:
    Item: PRESUMPTION-116
    Strongest counterargument: Cycle-density without normalization is documented across multiple literatures as artifact rather than signal. The "densest on record" framing is the canonical Goodhartable superlative — it sounds informative but encodes batch-size and topic-mix variance rather than substrate-coupling. Without normalization disclosure, downstream agents cannot calibrate the claim; the claim therefore introduces noise into the cluster-remediation decision rather than reducing it.
    What would need to be true for C2A2 to be safe: (a) Per-item density (not per-cycle) used as canonical metric; (b) batch-size and topic-mix disclosed; (c) historical baseline distribution reported.
    How to test: Recompute the 4-flag count as flags-per-item across the cycle history; check whether the 2026-05-09 cycle is above 2-sigma when normalized.

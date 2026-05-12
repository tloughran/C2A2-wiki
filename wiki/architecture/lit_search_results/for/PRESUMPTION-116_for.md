SEARCH-FOR-PRESUMPTION-116:
  Date searched: 2026-05-10
  Original item: PRESUMPTION-116
  Original statement: "'Densest cycle on record' framing presumes cycle-density is meaningful comparison metric without batch-size or topic-mix normalization"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-116
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-09 EOD superlative-claim analysis
      15a: Searched for metric-design literature on density vs. rate normalization
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Metric-design literature (Kleinrock 1975; Hopp & Spearman 2008) — density metrics without normalization are documented as misleading when batch-size varies; this is the standard caveat, not a supportive position.
    2. Bibliometric / scientometric literature (Bornmann & Marx 2014) — superlative claims about density (e.g., "densest publication year") canonically require normalization disclosure; unnormalized density is treated as artifact rather than signal.
    3. SRE alert-fatigue literature — alert-density spikes without normalization are known sources of operational noise.
    4. (No supporting literature for the unnormalized-density-as-meaningful-comparison position was found.)
    5. C2A2-internal: 2026-05-09 4-flag count is an artifact of the 20-item batch and the substrate-cluster mix; without disclosure of these, the "densest" comparison is uncalibrated.

  Strength of support: None

  Summary: No literature supports treating cycle-density as a meaningful comparison metric without normalization. The metric-design, bibliometric, and SRE literatures uniformly require normalization (batch-size, topic-mix, baseline-distribution) before density-spikes can be treated as signal. The presumption operates against the literature consensus.

  Caveats: This is a NO-SUPPORT-FOUND result for the FOR direction. The presumption may be operationally tractable in practice (cycle-density is a useful coarse signal even without full normalization) but the "meaningful comparison metric" claim, as stated, lacks literature support.

  Recommendation: NO-SUPPORT-FOUND

SEARCH-AGAINST-PRESUMPTION-073:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-073
  Original statement: "Adding two traditions brings N=11→13 without affecting N-dependent properties (cross-program density, statistical power for r)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-073
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as structural premise of ASSUMPTION-064
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Pair-space sparsity literature (Newman 2003 on social-network sparsity): adding nodes adds N edges potentially but only those connected do; if Wright/Rohr have weak connectivity to the existing 11, density falls measurably.
    2. Calibration-of-ratio-metrics literature (Wu & Li 2017 on health metrics; Howard 2018 on density indicators): a ratio that includes a denominator depending on N must be re-calibrated when N changes; "without affecting" is strictly false.
    3. Cross-program-density specifics: if Wright and Rohr are theology-traditions and the existing 11 are mostly science/philosophy, the density of cross-program connections to the new entries may be systematically lower (heterogeneity penalty), pulling r down.
    4. Statistical-power asymmetry: power for *changes* in r requires more samples as the metric's variance increases; adding heterogeneous nodes can increase variance.
    5. Health-ratio interpretability across N-transitions (OPEN-005 already flags this): C2A2 has not yet decided how to interpret r before/after the addition, indicating that "without affecting" is being used as if it were validated when it's actually unaudited.

  Strength of challenge: Moderate

  Summary: The "without affecting" framing is too strong. Adding two heterogeneous traditions changes (i) the pair-space, (ii) the cross-program-density, and (iii) the calibration of r. These effects are tractable but real and need explicit treatment. The literature supports tractable transition; it does not support "no effect."

  Specific risks: (a) r before and after the transition may not be comparable without re-calibration; (b) heterogeneity penalty pulls r down regardless of underlying network change; (c) OPEN-005 is not just open but unanswered — and its answer determines whether "without affecting" is true.

  Mitigations available: (a) Explicit re-calibration protocol for r at the transition; (b) document expected transition-effect (estimated drop in r from heterogeneity); (c) treat pre-transition r and post-transition r as different metrics until calibration verified.

  Recommendation: PARTIALLY-CHALLENGED ("without affecting" is too strong; the transition is tractable but requires explicit re-calibration)

  STEELMAN:
    Item: PRESUMPTION-073
    Strongest counterargument: Any N-dependent metric is by definition affected by changes in N; the question is whether the effect is large enough to matter. With heterogeneous additions (theology-traditions joining science-traditions), the density-of-connections from new nodes will systematically be lower, pulling r down. Without explicit re-calibration, the post-N=13 r may be misread as a degradation when it's a transition artifact.
    What would need to be true for C2A2 to be safe: (a) Pre/post-transition r values are computed and compared; (b) the transition effect is decomposed (homogeneity-driven vs. real change); (c) downstream consumers of r are taught about the transition.
    How to test: Compute r at the moment of transition with both 11-tradition and 13-tradition denominators; the gap is the calibration-effect. If the gap is large, "without affecting" is locally falsified.

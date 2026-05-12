SEARCH-FOR-PRESUMPTION-073:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-073
  Original statement: "Adding two traditions brings N=11→13 without affecting N-dependent properties (cross-program density, statistical power for r)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-073
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as structural premise of ASSUMPTION-064
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Network-science scaling (Albert & Barabási 2002; Newman 2003): in small dense graphs, adding 2 nodes increases the pair-space modestly (N=11 → 55 pairs; N=13 → 78 pairs; +42%) but does not break dense-graph properties.
    2. Statistical-power literature (Cohen 1988): with the new N (78 pairs), statistical power for moderate effect sizes increases, not decreases — supports the assumption that the metric remains computable.
    3. Robust-metric design: ratios bounded between 0 and 1 (such as a connectivity-density ratio) are not directly destabilized by changes in N; what destabilizes them is calibration, not raw N.
    4. C2A2 prior practice: the network has scaled before (e.g., from earlier versions to N=11) without breaking the metric.

  Strength of support: Moderate

  Summary: At the structural level, the N=11→13 transition is small and the metric (r) is bounded; the transition does not break the metric's computability. There is literature support for the claim that small N changes in dense networks preserve density properties.

  Caveats: (a) Calibration of r at N=13 may differ from N=11; (b) the metric's *interpretation* across the transition requires explicit treatment; (c) "without affecting" is strong — small effects on density and on power exist by definition.

  Recommendation: PARTIALLY-SUPPORTED (computability is preserved; interpretation across the transition needs explicit re-calibration)

SEARCH-AGAINST-ASSUMPTION-090:
  Date searched: 2026-05-09
  Original item: ASSUMPTION-090
  Original statement: "Smallest-fix-first prioritization for explorer track — extractOverview() two-line fix is the high-confidence entry point"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-090
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-08 explorer-track prioritization decision
      15b: Searched for counter-evidence on smallest-fix-first being suboptimal vs. strategic-fix-first
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Reinertsen (2009) "The Principles of Product Development Flow" — strategic-fix-first ("eliminate the class of bugs") often dominates smallest-fix-first when defect rate is high; smallest-fix-first is optimal under low defect rate, not universally.
    2. Refactoring critique literature (Murphy-Hill et al. 2009 "How We Refactor") — smallest-fix-first can leave fragile area unaddressed; in some empirical studies, strategic-fix-first reduces total defect cost.
    3. Maintenance-economics literature (Banker, Davis, Slaughter 1998) — smallest-fix-first is optimal for short-horizon work; strategic-fix-first dominates for long-horizon programs.
    4. Empirical defect-injection studies (Bird et al. 2011 "Don't Touch My Code!") — smallest changes have lower per-change defect rate, but cumulative small changes can exceed strategic-fix defect cost.
    5. C2A2-internal: ASSUMPTION-082 (RC Explorer architecture with HIGH-priority MONITOR-082) — strategic-fix-first on layer-isolation may dominate two-line fixes in this specific case.

  Strength of challenge: Weak-Moderate

  Summary: Smallest-fix-first is canonical but not universal. Counter-literature documents cases where strategic-fix-first dominates: long-horizon programs, high defect rates, and fragile architectural areas. The two-line extractOverview() fix is in an active development area (RC Explorer, MONITOR-082 HIGH); strategic-fix-first on layer-isolation could plausibly dominate. The challenge is weak-moderate because smallest-fix-first remains the lower-risk default; the challenge is to "high-confidence entry point" framing rather than to the prioritization itself.

  Specific risks: (a) Fragile area: if extractOverview() touches the layer that PRESUMPTION-099 (layer-coherence-without-test) flagged, the two-line fix may inject regression; (b) long-horizon: if RC Explorer's strategic-fix-first opportunity (layer isolation per ASSUMPTION-082) yields higher long-term return, smallest-fix-first is opportunity cost; (c) "high-confidence" overclaims absent unit tests on the affected method.

  Mitigations available: (a) Pair smallest-fix with unit test on extractOverview(); (b) verify layer isolation before merging the two-line change; (c) document fix as tactical-not-strategic to prevent ossification.

  Recommendation: PARTIALLY-CHALLENGED (smallest-fix-first is canonical; "high-confidence entry point" without test/isolation verification is the gap)

  STEELMAN:
    Item: ASSUMPTION-090
    Strongest counterargument: "Smallest-fix-first" is canonical in stable codebases, not in actively-architected ones. RC Explorer is in active architectural definition (ASSUMPTION-082 MONITOR-082 HIGH); strategic-fix-first on layer isolation may dominate over two-line fixes that risk being entangled with the layer that PRESUMPTION-099 flagged. "High-confidence" overstates what is supported absent isolation tests and unit tests.
    What would need to be true for C2A2 to be safe: (a) unit test on extractOverview() before merging; (b) layer-isolation verification per ASSUMPTION-082 / PRESUMPTION-099; (c) cost-of-delay calculation comparing smallest-fix vs. strategic-fix.
    How to test: Run the two-line fix in a branch; check for regressions across L1/L2/L3 boundaries; measure whether confidence-as-claimed matches confidence-as-observed.

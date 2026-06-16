SEARCH-FOR-PRESUMPTION-335:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-335
  Original statement: The house validator's check suite defines artifact correctness; user-visible display invariants are out of scope, leaving the attending human as anomaly detector.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-335
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced unstated presumption by inference from validator-scope practice (cycle 0, 2026-06-10)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Barr, E.T., Harman, M., McMinn, P., Shahbaz, M., Yoo, S., 2015. "The Oracle Problem in Software Testing." IEEE Transactions on Software Engineering. — Canonical statement that complete automated oracles are often infeasible; human oracles are a recognized, legitimate fallback where specification of correct output (e.g., visual correctness) resists automation.
    2. McNutt, A., Kindlmann, G., Correll, M., 2020. "Surfacing Visualization Mirages." CHI 2020 (arXiv:2001.02316). — Confirms display-level correctness for visualizations is a hard, open problem (mirages pass data checks yet mislead visually); partial vindication for scoping a validator to checkable properties.
    3. "An Empirical Study of Bugs in Data Visualization Libraries," 2025. arXiv:2506.15084. — Documents that a large class of visualization defects are non-crashing visual bugs lacking automated oracles, detected in practice by human inspection — empirical precedent for human-as-anomaly-detector.
    4. JANUS (ICSE 2025), "Detecting Rendering Bugs in Web Browsers via Visual Delta Consistency." — Shows the frontier is only now automating rendering-bug detection, i.e., human detection has been the operative norm.
  Strength of support: Weak
  Summary: The descriptive halves of the presumption are well grounded: the oracle problem literature establishes that automated check suites can only ever encode a partial correctness definition, that visual/display correctness is among the hardest properties to automate, and that human inspection is the standard residual oracle for visual artifacts. In that sense, a validator scoped to mechanically checkable invariants plus an attending human is a recognized, defensible QA architecture — especially for a single-maintainer system. What the literature does not support is the normative leap that the check suite "defines" correctness: oracle research treats automated checks as partial oracles by definition, and the metamorphic-testing line (e.g., Segura et al. 2016 survey) shows display invariants (legend-count consistency, element-count vs data-count, opacity morphisms) are in fact automatable, so their out-of-scope status is a choice, not a necessity.
  Caveats: Human-as-oracle validity degrades with artifact size and change frequency (vigilance decrement); the cited literature recommends migrating recurring human-caught anomaly classes into metamorphic/property checks over time. Support applies to the current scale, not as the system grows.
  Search scope: 1 WebSearch ("metamorphic testing visualization charts automated detection visual rendering bugs test oracle problem human inspection"); plus known oracle-problem literature.
  Recommendation: PARTIALLY-SUPPORTED

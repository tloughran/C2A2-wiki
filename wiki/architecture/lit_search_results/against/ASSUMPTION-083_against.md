SEARCH-AGAINST-ASSUMPTION-083:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-083
  Original statement: "Wiki-visualization filter semantics: within section = OR; across sections = AND; edges require both endpoints visible"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-083
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 filter-popover specification
      15b: Searched for challenging literature on filter-semantics user-misinterpretation
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Hearst (2009) — even canonical within/across semantics produce user errors when the section labels are not visually distinct; convention-following is necessary but not sufficient.
    2. English & Hearst (2007) — empirical study showed users frequently misread within/across conventions when the UI did not signal the boundary clearly.
    3. Wilson, Schraefel & White (2009) "Evaluating Advanced Search Interfaces" — popover-only documentation of filter semantics is consistently associated with higher user-error rates than inline cues.
    4. Edge-visibility literature (Munzner 2014) — strict "both endpoints visible" excludes one-degree-of-separation views that are sometimes needed; the rule is canonical but not always optimal.
    5. C2A2-internal: PRESUMPTION-101 (filter-semantics popover ≡ implementation without test) — the load-bearing test gap is queued separately.

  Strength of challenge: Weak-to-Moderate

  Summary: The semantics are canonical, but canonical semantics still produce user errors when UI affordances do not signal them clearly. Popover-only documentation is associated with higher error rates than inline cues. The strict edge-visibility rule may foreclose useful one-degree-of-separation views. The challenge is not against the semantic itself but against the operational claim that documenting it is sufficient.

  Specific risks: (a) Users misread within/across without inline cues; (b) edge-visibility rule may produce unhelpful empty graphs in narrow filter states; (c) PRESUMPTION-101's missing test means doc-implementation drift is invisible.

  Mitigations available: (a) Add inline cues at filter-section boundaries; (b) consider one-degree-of-separation toggle for edge-visibility; (c) snapshot test on popover content per PRESUMPTION-101.

  Recommendation: PARTIALLY-CHALLENGED (semantics are canonical; operationalization details — inline cues, edge-visibility flexibility, doc-implementation test — are the weaker links)

  STEELMAN:
    Item: ASSUMPTION-083
    Strongest counterargument: Choosing the canonical semantic is the easy part; getting users to perceive it is the hard part. Hearst's own foundational work shows that within/across distinctions still produce errors when the UI does not signal them inline. A popover is the lowest-discoverability documentation surface — users hover only when confused, by which time they have already formed a wrong model. The strict edge-visibility rule, while canonical, can produce unhelpfully empty graphs in narrow filter states without a one-degree-of-separation escape valve.
    What would need to be true for C2A2 to be safe: (a) Inline cues at section boundaries; (b) optional one-degree-of-separation toggle; (c) snapshot test on popover content (per PRESUMPTION-101).
    How to test: Show three users the visualization with multi-section filters active; ask each to predict which nodes are visible; if >1 is wrong, the inline-cue gap is real.

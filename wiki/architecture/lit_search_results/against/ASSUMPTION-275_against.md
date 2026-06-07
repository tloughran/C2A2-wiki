SEARCH-AGAINST-ASSUMPTION-275:
  Date searched: 2026-06-06
  Original item: ASSUMPTION-275
  Original statement: Graph and Cards are two non-redundant "verbs over one dataset"; neither can absorb the other's function, so keeping both is justified (P4 "keep only one" rejected).

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-275
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a stated justification for keeping two surfaces.
      15b: Searched for view-redundancy / maintenance cost of parallel UIs and cases where one surface dominates.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Baldonado, Woodruff & Kuchinsky, 2000, "Guidelines for Using Multiple Views" — Rule of Parsimony. — Explicitly: use multiple views minimally; each added view costs learning time, screen space, and computational/maintenance overhead and must be justified against a single-view alternative. Direct challenge to keeping both by default.
    2. "An Empirical Study on the Relationship Between the Number of Coordinated Views and Visual Analysis" (arXiv 2204.09524). — Finds more coordinated views do not monotonically help and can impose context-switching costs that hurt analysis; challenges the assumption that two surfaces are strictly better.
    3. Software-maintenance cost literature (parallel UIs / duplicated surfaces). — Maintaining two front-ends over one corpus duplicates state, interaction, and test surface; a recognized cost driver (cf. maintenance = 40-80% of software cost).

  Strength of challenge: Moderate

  Summary: CMV's own foundational guidance (Baldonado's Rule of Parsimony) is the sharpest challenge: multiple views must be justified against the cost of each additional view, and "keep both" is not free. Empirical work finds that more coordinated views can degrade rather than improve analysis through context-switching cost, and maintaining two parallel UIs over one corpus is a known maintenance multiplier. The assumption's claim that "neither can absorb the other" is testable and may be false: if Cards is reducible to a saved/filtered projection of the Graph (or vice versa), one surface dominates and the second is redundant overhead. The challenge does not refute keeping both; it denies that keeping both is justified WITHOUT demonstrating non-absorption and net-positive value.

  Specific risks: C2A2 carries two surfaces' build/test/maintenance cost when one (plus a filter/saved-view) might serve; users pay a context-switching tax; the "non-redundant" claim ossifies without ever being tested against a one-surface alternative.

  Mitigations available: Make the non-absorption claim explicit and testable (name a task each surface does that the other cannot); apply Baldonado parsimony as a recurring check; if Cards becomes expressible as a Graph view-state, deprecate the duplicate.

  STEELMAN:
    Item: ASSUMPTION-275
    Strongest counterargument: "Two verbs over one dataset" can be a post-hoc rationalization for not having to choose. Baldonado's parsimony rule exists because teams over-add views; the burden is on the design to prove each view earns its cost, not to assert non-redundancy. If Cards is just the Graph's node set rendered as a filterable list, it is a projection, not a second verb — and the maintenance + cognitive cost of a redundant surface is exactly what parsimony warns against.
    What would need to be true for C2A2 to be safe: There is at least one high-value task each surface supports that the other genuinely cannot (e.g., Graph: read relational structure; Cards: bulk attribute scan/lookup not expressible as a graph state), AND the combined value exceeds the dual-maintenance cost.
    How to test: Enumerate top user tasks; mark which surface each requires; if every task maps cleanly to one surface plus a filter, the second surface is redundant.

  Recommendation: PARTIALLY-CHALLENGED

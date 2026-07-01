SEARCH-AGAINST-ASSUMPTION-383:
  Date searched: 2026-06-29
  Original item: ASSUMPTION-383
  Original statement: "Vault is wikilink-sparse but reference-dense; thinker content already well connected; connectivity is not the synthesis bottleneck (only 9 under-connected thinker pages)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-383
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: low explicit-wikilink density read as non-deficit
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Small-world / hub-dependence of sparse networks. - Sparse corpora are well-connected ONLY because of a few high-degree hubs; if those hubs are exactly the "under-connected thinker pages," sparsity is NOT benign and the conclusion reverses.
    2. Content-quality vs connectivity distinction (KG quality dimensions). - "Well connected" by shared references does not establish synthesis readiness; reference co-occurrence is a weak, implicit relation that can overstate functional connectedness relative to deliberate links.
    3. Threshold-dependence of connectivity counts. - "Only 9 under-connected pages" is entirely a function of the chosen threshold; a stricter threshold could surface many more, so the reassuring count is not robust.

  Strength of challenge: Moderate

  Summary: The claim leans on shared-reference density to declare connectivity a non-bottleneck, but shared-reference edges are implicit and weak compared to authored wikilinks; high co-citation does not guarantee navigable synthesis paths. Sparse-but-connected networks depend critically on hubs, so a deficit concentrated in hub/thinker pages would be precisely the bottleneck the claim dismisses. The "9 pages" figure is threshold-sensitive and not a stable indicator.

  Specific risks: Declaring connectivity adequate could mask a real hub deficit and forgo synthesis links that only authored edges provide; the reassuring count may be an artifact of a lenient threshold.

  Mitigations available: Recompute under multiple thresholds; verify that shared-reference paths are actually traversable for synthesis (spot-check); confirm hubs are present, not missing.

  STEELMAN:
    Item: ASSUMPTION-383
    Strongest counterargument: Reference-density and link-density measure different things; a corpus can be reference-dense yet lack the authored bridges that make synthesis navigable, and a count of "9 under-connected pages" can be made arbitrarily small by relaxing the threshold - so "connectivity is not the bottleneck" may be a measurement-comfort conclusion rather than a structural fact.
    What would need to be true for C2A2 to be safe: Shared-reference paths between thinkers are actually usable for synthesis, and the under-connected set is stable across reasonable thresholds.
    How to test: Sample thinker pairs, attempt a synthesis traversal using only shared-reference edges, and re-run the orphan/under-connected count at 2-3 thresholds.

  Search scope: Hub dependence; implicit vs explicit edges; threshold sensitivity. Adequate.

  Recommendation: PARTIALLY-CHALLENGED

SEARCH-AGAINST-ASSUMPTION-453:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-453
  Original statement: Both connectivity claims hinge entirely on whether retrieval over the vault is traversal-based or embedding-based; determining the retrieval mode settles ASSUMPTION-447 and ASSUMPTION-448 at once.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-453
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result PARTIALLY-CHALLENGED (strength Moderate)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Hybrid-RAG surveys (arXiv:2507.03226; Neo4j): the framing 'traversal XOR embedding' is a false dichotomy in current practice; systems routinely combine dense candidate selection with graph re-ranking, so retrieval mode may not be a single determinable value.
    2. 'Breaking the Static Graph' (arXiv:2602.01965): retrieval behavior is context-dependent and query-dependent, so a one-shot determination of 'the mode' may not generalize across queries.

  Strength of challenge: Moderate

  Summary: The main challenge is that the assumption presumes retrieval mode is a single, static, determinable property that cleanly settles two downstream claims. The literature suggests modern retrieval is hybrid and query-conditioned, so determining 'the mode' once may under-determine A-447/A-448 rather than settling them. The empirical test is still the right move, but it may return 'both, conditionally' rather than a clean verdict.

  Specific risks: C2A2 treats a hybrid or query-dependent retrieval path as if it were a single mode, and 'settles' two flags on a false binary - re-opening them later.

  Mitigations available: Run the proposed BFS-reachability test AND inspect whether the stack fuses modes; report per-mode contribution rather than a single label.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-453
    Strongest counterargument: If retrieval is hybrid, then neither A-447 nor A-448 is settled by mode-identification; the connectivity each claims could both be real via different retrieval paths, and the 'one determination discharges two flags' economy evaporates.
    What would need to be true for C2A2 to be safe: The thinker agents consume a single, identifiable retrieval path (pure traversal or pure embedding) rather than a fused pipeline.
    How to test: Read the retrieval code the thinker agents actually call; if it fuses vector + graph, the binary is void and both flags need separate tests.

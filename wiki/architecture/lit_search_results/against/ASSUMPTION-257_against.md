SEARCH-AGAINST-ASSUMPTION-257:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-257
  Original statement: The recent Sociogram crash was pure memory pressure, not the edge cap; MAX_EDGES=30000 stays.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-257
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched edge-count as a latent contributor to memory pressure (cap-vs-pressure confound).
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Nightingale / Cosmograph WebGL literature — edge count is itself a primary driver of DOM/memory load in SVG graphs; 'memory pressure' and 'edges' are not disjoint causes.
    2. Chrome DevTools memory docs — detached/!excess DOM nodes (edges are DOM nodes in SVG) are a leading memory-growth cause, so the edge cap and memory pressure are the same axis.
    3. General confounding methodology — framing 'pure memory pressure, NOT the edge cap' as exclusive alternatives is a false dichotomy when edges drive the memory.

  Strength of challenge: Moderate-Strong

  Summary: Because edges rendered as SVG DOM nodes are a principal source of memory load, 'pure memory pressure' and 'the edge cap' are not mutually exclusive; the causal story is a false dichotomy. The cap may be fine to keep, but as a memory-control lever, not because edges are exonerated.

  Specific risks: Mis-attributing the crash hides the edge-count contribution; the cap value may be set on a wrong causal model and fail at scale.

  Mitigations available: Profile heap with edge count varied; treat MAX_EDGES as one memory lever among several (node count, DOM technique, WebGL migration).

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-257
    Strongest counterargument: If edges are SVG DOM nodes, then 'memory pressure' is partly *caused by* edge count, so the exclusive framing is ill-posed; keeping the cap is right, but the reasoning is backwards.
    What would need to be true for C2A2 to be safe: Heap profile shows crash threshold is insensitive to edge count within the operating range.
    How to test: Vary edge count at fixed node count and record heap-at-crash.

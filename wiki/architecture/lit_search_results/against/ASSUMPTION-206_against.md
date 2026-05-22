SEARCH-AGAINST-ASSUMPTION-206:
  Date searched: 2026-05-21
  Original item: ASSUMPTION-206
  Original statement: "Generative-coil detection is lexical-first (v1, 17 chains); semantic/embedding is v2."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-206
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: staged detection plan — v1 lexical/string-matching (17 chains found), v2 semantic/embedding.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E / REVISE-040 noted)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Furnas et al. (1987) "The vocabulary problem." — Lexical matching misses the majority of semantically equivalent handoffs; "adequately recalls" is false for v1.
    2. Semantic-similarity / paraphrase literature (word & sentence embeddings). — String match systematically misses solution->resource links that do not share tokens.

  Strength of challenge: Weak-Moderate

  Summary: The only real challenge is to 'adequately recalls': lexical detection has known low recall (vocabulary problem), so v1's 17 chains likely undercount true coils substantially. But the assumption explicitly concedes this by scheduling semantic detection as v2, so the challenge targets a claim the assumption does not make.

  Specific risks: Treating the 17-chain v1 result as complete (rather than a high-precision sample) would understate connectivity.

  Mitigations available: Label v1 output as precision-biased; estimate recall on a small hand-labeled sample now; prioritize v2 embeddings.

  Recommendation: PARTIALLY-CHALLENGED (recall only)

  STEELMAN:
    Item: ASSUMPTION-206
    Strongest counterargument: A pure-lexical v1 can give false confidence that 'only 17 coils exist' when recall may be well under 50%; the staged plan is sound only if v1 outputs are explicitly treated as lower bounds, not counts.
    What would need to be true for C2A2 to be safe: v1 is labeled precision-biased and recall is estimated before any count is used in a decision.
    How to test: Hand-label a sample of solution->resource handoffs and measure lexical recall.

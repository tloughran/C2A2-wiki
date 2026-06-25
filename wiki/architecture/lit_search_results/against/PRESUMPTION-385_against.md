SEARCH-AGAINST-PRESUMPTION-385:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-385
  Original statement: "That 'one agent per thinker' is the right unit at which to add redundancy/voting (vs the edge, the triplet, the synthesis claim)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-385
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the agent-per-thinker decomposition was inherited unquestioned as the locus for redundancy
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Ensemble-placement theory (Dietterich 2000; Kuncheva 2003). - Redundancy pays off where outputs are aggregable and errors decorrelated; the per-thinker whole-output may be too coarse a unit to aggregate meaningfully.
    2. Decomposition granularity (software/ML pipelines): voting at the finest decision unit (here: the claim/edge) generally extracts more error-cancellation than voting on a composite artifact.
    3. Jacobs et al. 1991 (mixtures of experts): the right unit for combination is the sub-decision, not the whole agent.

  Strength of challenge: Moderate

  Summary: The presumption inherits 'one agent per thinker' as the redundancy unit without justification, and the literature suggests this may be sub-optimal: error-cancellation from voting is typically strongest at the level of the atomic decision (the individual claim or edge), not at the level of a whole thinker-agent's composite output, which is hard to aggregate and may average over heterogeneous sub-decisions. Placing redundancy at the wrong granularity can waste the ensemble budget.

  Specific risks: Redundancy spent at the agent level may yield little error-cancellation while tripling cost; genuinely contestable claim-level signal could be washed out by coarse aggregation.

  Mitigations available: Pilot redundancy at multiple granularities (claim/edge vs agent) and compare error-cancellation per unit cost; choose the unit empirically.

  STEELMAN:
    Item: PRESUMPTION-385
    Strongest counterargument: Voting works best on atomic, aggregable decisions; a whole thinker-agent's output is a composite that resists clean aggregation, so per-thinker redundancy may be the least efficient place to spend the ensemble budget.
    What would need to be true for C2A2 to be safe: Per-thinker aggregation extracts comparable error-cancellation to finer-grained (claim/edge) aggregation at equal cost.
    How to test: Run an ablation: redundancy at claim-level vs agent-level on the same pilot; compare review-survival and cost.

  Search scope: Ensemble granularity; mixtures of experts. Adequate.

  Recommendation: PARTIALLY-CHALLENGED

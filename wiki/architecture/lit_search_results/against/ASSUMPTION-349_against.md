SEARCH-AGAINST-ASSUMPTION-349:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-349
  Original statement: "Triple-column + adjudicator ~= 3-4x agent/token load per thinker track"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-349
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as a cost estimate (low priority)
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: Partial

  Sources:
    1. (Weak) Self-consistency/ensemble costing notes: aggregation, long shared contexts, and retries can push multi-pass costs above the naive Nx, occasionally well beyond.
    2. Adjudication with full pairwise comparison can scale super-linearly in the number of items compared.

  Strength of challenge: Weak

  Summary: No substantive challenge to the order-of-magnitude estimate was found; the main caveat is that real multipliers can exceed 4x when adjudication needs long shared contexts, multi-round arbitration, or retries, or when comparisons scale super-linearly. This nuances rather than refutes the estimate.

  Specific risks: Under-budgeting compute/cost if the multiplier is higher than 4x at pilot scale.

  Mitigations available: Measure directly at pilot; instrument token usage per track; treat 3-4x as a planning lower bound.

  STEELMAN:
    Item: ASSUMPTION-349
    Strongest counterargument: The 3-4x figure assumes simple additive adjudication; realistic arbitration and context-sharing can make the true multiplier materially higher, so the estimate may under-budget.
    What would need to be true for C2A2 to be safe: Measured pilot multiplier falls within (or below) the 3-4x band.
    How to test: Instrument actual token/agent usage during the Hawkins pilot and compare to the estimate.

  Search scope: Ensemble cost scaling. Adequate (low-stakes).

  Recommendation: NO-CHALLENGE-FOUND

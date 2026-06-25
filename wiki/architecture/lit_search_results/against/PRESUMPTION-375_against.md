SEARCH-AGAINST-PRESUMPTION-375:
  Date searched: 2026-06-23
  Original item: PRESUMPTION-375
  Original statement: "[inferred] That month-over-month token growth (8.2M->20.4M->33.3M) is itself reassuring — more output tokens = healthier (metric-direction normative smuggling)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-375
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated metric-direction premise; twin of ASSUMPTION-336, metric-direction family with PRESUMPTION-367
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Vanity-metrics literature (NN/g; Built In; Tableau). — An ever-growing cumulative metric where "bigger is always better" is the textbook definition of a vanity metric; token volume is a cost/usage figure, not a value figure.
    2. Output-vs-value (developer-productivity critiques). — More output (lines, tokens, PRs) can signal waste as easily as health; volume must be normalized by value/cost.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged: monotone growth of a usage/cost metric is the canonical vanity-metric pattern, and token volume measures spend, not value. "More = healthier" smuggles a normative direction onto a cost figure; the same volume could reflect waste, redundancy, or runaway loops. Without normalization by output value or cost-efficiency, growth is uninterpretable as health.

  Specific risks: Mistaking rising spend for rising health could justify unbounded token expenditure and mask efficiency regressions — and directly contradicts the user's own token-budget discipline (per-task/per-session budgets).

  Mitigations available: Track value- or efficiency-normalized metrics (value per token, tokens per decision); treat raw growth as a cost signal needing justification, not reassurance.

  STEELMAN:
    Strongest counterargument: If output quality is held constant, rising token throughput reflects a system doing more work — genuine increased productive capacity, not vanity.
    What would need to be true for C2A2 to be safe: Quality/value per token must be measured and shown non-decreasing; only then does volume growth indicate more useful work rather than more waste.
    How to test: Plot value-per-token (decisions, validated premises, or accepted proposals per token) over the same months; flat/rising => healthy growth, falling => waste.

  Search scope: vanity metrics; output-vs-value; cost normalization. Comprehensive.

  Recommendation: CHALLENGED

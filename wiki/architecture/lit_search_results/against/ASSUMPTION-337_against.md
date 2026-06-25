SEARCH-AGAINST-ASSUMPTION-337:
  Date searched: 2026-06-23
  Original item: ASSUMPTION-337
  Original statement: "The proposal-review queue is review-bound, not search-bound — the binding constraint since 06-16 is human review throughput, not literature discovery"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-337
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-22 session as an actionable workflow-design claim
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. TOC self-diagnosis caution. — A stage declaring itself the binding constraint can be self-serving; the constraint can shift, and "review-bound" may mask a quality/search problem upstream (e.g., proposals not decision-ready).
    2. Little's Law boundary. — If review latency is driven by proposal quality (search/synthesis), the true constraint is upstream even though WIP shows at review.

  Strength of challenge: Weak-Moderate

  Summary: The challenge is mild and conditional: the diagnosis is right only if review latency is genuinely throughput-limited rather than caused by upstream quality (proposals arriving not decision-ready). TOC warns constraints can shift and that a stage where WIP shows is not always the true constraint. But the 06-16->06-22 backlog with capable intake makes the review-bound reading the most parsimonious; the challenge tightens scope rather than refuting.

  Specific risks: Mislabeling a quality/readiness problem as a throughput problem would lead to adding review capacity that does not clear the queue.

  Mitigations available: Confirm review latency is throughput- not readiness-driven; if proposals are not decision-ready, the constraint is upstream synthesis.

  STEELMAN:
    Strongest counterargument: WIP can pile at a non-constraint that is merely downstream of the real bottleneck; the review queue could be backed up because proposals are under-baked, making the constraint synthesis/search, not review.
    What would need to be true for C2A2 to be safe: Review latency must be shown to be capacity-limited (reviewers saturated) rather than readiness-limited (proposals bounce back) for "review-bound" to hold.
    How to test: Track review cycle time vs rework rate; high cycle time + low rework => review-bound; high rework => upstream-bound.

  Search scope: constraint-shift; readiness vs throughput. Comprehensive.

  Recommendation: PARTIALLY-CHALLENGED

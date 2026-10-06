SEARCH-AGAINST-ASSUMPTION-1561:
  Date searched: 2026-09-21
  Original item: ASSUMPTION-1561
  Original statement: Cross-tradition joint appearances are systematically missed by per-thinker
    retrieval, and a 91-pair x 24-month sweep of public long-form venues would recover them.

  **Execution note:** 15a and 15b were executed by a single scheduled process on 2026-09-21. Query sets
  were framed separately and the FOR files were written before any AGAINST query was issued, but the
  two-process independence the spec assumes was NOT achieved. Weight the strength ratings accordingly.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1561
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-20 weekly sewing run; pair count and 223-day lag verified.
      15b: Searched for evidence that pair enumeration fails to recover, or costs more than it returns.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Sanchez, J. 2016. "A Review of Pair-wise Testing." arXiv:1606.00288; and the all-pairs testing
       literature generally. — The domain that has studied pairwise enumeration most carefully adopts it
       as a *cost-reduction* over exhaustive search, not as a recall guarantee, and its justification is
       empirical (most defects involve few-parameter interactions) rather than principled. Transferred
       here: enumerating 91 pairs buys coverage of the pair *space*, which is not the same as coverage
       of the *event* space, and nothing guarantees joint appearances are distributed over pairs
       uniformly enough for the sweep to pay.
    2. Entity-resolution / pairwise-matching scalability literature (e.g. "Scaling up Copy Detection,"
       arXiv:1503.00309; bitmap-filter set-similarity joins, arXiv:1711.07295). — Exhaustive pairwise
       comparison is O(n^2) in the population and is reported as *not scalable* past small n, with the
       standard remedy being blocking/filtering rather than enumeration. 91 pairs is 14 thinkers; the
       estate's ambition is more thinkers, and this remedy does not grow with it.
    3. "On the Importance of Adaptive Data Collection for Extremely Imbalanced Pairwise Tasks."
       arXiv:2010.05103. — The governing result for this design: when positives are extremely rare
       relative to the pair space, uniform enumeration is the *worst* allocation of a fixed budget, and
       adaptive collection dominates it. Joint appearances of two named thinkers in a 24-month window
       are exactly an extremely-imbalanced pairwise task.

  Strength of challenge: Strong

  Summary: The literature does not contradict the diagnostic half of the claim (per-thinker retrieval
    misses joint events — that stands). It challenges the *remedy*. Pairwise enumeration is studied as a
    budget-constrained approximation whose payoff depends on positives being reasonably distributed
    across the pair space; where positives are extremely rare and clustered, uniform enumeration is
    known to be dominated by adaptive strategies. And the design does not scale: 91 pairs is
    n=14; the cost is quadratic in any expansion of the roster.

  Specific risks: (1) The sweep is built, costs 91 x 24 = 2,184 queries, and returns a handful of events
    that a channel-targeted search would have found for a fraction of the effort — after which the lag
    is unchanged and the sweep is nonetheless recorded as the fix. (2) The design is adopted as a
    standing instrument and becomes unrunnable the moment the roster grows. (3) Most costly: the sweep
    displaces the cheap back-test that would have told the estate whether to build it.

  Mitigations available: Run the back-test first (it is already named in PRESUMPTION-1057 with a
    pre-registered success criterion). Prefer adaptive/targeted collection: enumerate the venues rather
    than the pairs, since long-form venues are far fewer than 91 and are the actual channel. Bound the
    sweep to a sample of pairs and report the hit rate before committing to the full grid.

  STEELMAN:
    Item: ASSUMPTION-1561
    Strongest counterargument: The proposal solves a coverage problem the estate does not have and
      leaves the channel problem it does have. If joint appearances surface through a small number of
      long-form venues, then the efficient instrument enumerates *venues over time* — an O(n) sweep —
      and pair enumeration is a quadratic re-parameterisation of the same task that happens to look
      more systematic. The 2,184-query design would then be a large, defensible-looking expenditure
      whose only advantage over the cheap alternative is that it produces a grid.
    What would need to be true for C2A2 to be safe: that joint appearances are distributed across many
      venues rather than concentrated in few, so that pair-indexing genuinely outperforms venue-indexing.
    How to test: the back-test already specified — run the sweep design retrospectively over the elapsed
      24 months and check whether it recovers the 2026-02-04 Hoffman/Friston event. Add one line to the
      test: record which *venue* that event occurred in, and how many of the recovered events share it.

  Recommendation: CHALLENGED

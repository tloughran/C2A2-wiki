SEARCH-AGAINST-ASSUMPTION-244:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-244
  Original statement: End-to-end verification (single happy-path Friston query + node-dimming + tab integrity + zero console errors) is sufficient evidence to stage the 5-file changeset and await Tom's push sign-off.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-244
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on single-query-verification representativeness and coverage tradeoffs.
    Current status: CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Beizer (1990) "Software Testing Techniques" — Single-path coverage is documented as systematically inadequate when path-class heterogeneity is non-trivial; the literature is unambiguous on this.
    2. Myers (2004) "The Art of Software Testing" — Equivalence-class partitioning literature requires that representative coverage span the partition; single query covers single partition.
    3. Adlakha et al. (2024) on retrieval evaluation — Cross-tradition / scholarly retrieval evaluation requires multi-query benchmarks; single-query is documented as systematically misleading.
    4. Allspaw (2015) "How Complex Systems Fail" — "Looks fine in canary" is a documented failure mode; canary-as-sufficient is named as anti-pattern.
    5. Cook & Woods (1994) — Single-instance verification produces a false sense of completion; recurrence-rate of single-tested paths is documented.

  Strength of challenge: Moderate

  Summary: Software testing literature is robust against single-query-as-sufficient. Beizer, Myers, and the broader testing canon explicitly require coverage spanning equivalence classes. For RAG / retrieval systems, BEIR / SPECTER literature requires multi-query benchmarks. The 5-file scope mitigates blast radius but does NOT validate the verification's adequacy claim. "Zero console errors" is a weak proxy: many failure modes do not produce console errors.

  Specific risks: (a) Friston-class query may overfit the integration to one query shape; (b) silent-data-integrity failures in non-Friston queries; (c) tab-integrity check may miss interaction failures with other tabs; (d) "sufficient" framing risks anchoring future verifications at the same low bar.

  Mitigations available: (a) Expand verification to 3-5 query classes (named-thinker, paradigm-bridge, keyword, multi-hop); (b) treat "zero console errors" as necessary-not-sufficient; (c) add a structural check for the broker-v4 broker logic on each query class; (d) define an explicit "sufficient verification" rubric per changeset class.

  Recommendation: CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-244
    Strongest counterargument: Software-testing literature uniformly rejects single-path verification as sufficient. Equivalence-class partitioning (Myers) and path-coverage (Beizer) are foundational, not optional. For a retrieval/AI search integration, the literature on retrieval evaluation (BEIR/Adlakha) explicitly requires multi-query benchmarks. The "human gate" (Tom's push sign-off) does not validate the verification — it validates the staging decision. If the staging decision presumes adequacy from a single Friston query, it inherits a documented inadequacy.
    What would need to be true for C2A2 to be safe: Verification spans 3+ representative query classes with structural checks at each (broker delegation, node-dimming, tab integrity); "sufficient verification" defined per change-scope.
    How to test: Audit prior changesets — track post-ship regressions traceable to single-path-verification gap.

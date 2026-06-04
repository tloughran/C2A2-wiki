SEARCH-AGAINST-PRESUMPTION-272:
  Date searched: 2026-05-29
  Original item: PRESUMPTION-272
  Original statement: [inferred] The single Friston query in ASSUMPTION-244's verification protocol is representative of the Sociogram-tab query distribution for ship-readiness; query-class coverage is not separately defended.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-272
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated representativeness claim.
      15b: Searched for challenging literature on representative-query-selection bias.
    Current status: CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Beizer (1990) "Software Testing Techniques" — Equivalence-class partitioning literature requires coverage spanning partitions; single-query single-partition coverage is documented inadequate.
    2. Myers (2004) — Boundary-value and equivalence-class testing literature: single query covers single class, not the distribution.
    3. BEIR benchmark (Thakur et al. 2021) — Retrieval evaluation literature requires multi-query benchmarks across task classes; single-query is documented as misleading.
    4. SPECTER (Cohan et al. 2020) — Scholarly retrieval evaluation specifically calls out scholarly cross-domain queries as a distinct retrieval shape requiring separate evaluation.
    5. C2A2-internal: tradition-bridge queries are precisely the scholarly-cross-domain shape; coupling to PRESUMPTION-260 / REVISE-061 on broker-v4 calibration gap.

  Strength of challenge: Moderate

  Summary: Testing and retrieval-evaluation literatures are robust against single-query-representativeness. Beizer / Myers on partitioning, BEIR / SPECTER on retrieval evaluation, and C2A2's own PRESUMPTION-260 (REVISE-061) all converge: scholarly cross-tradition queries are a distinct shape that single-query verification does not cover. The presumption is well-grounded.

  Specific risks: (a) Friston-class verification misses keyword-class, multi-hop, or paradigm-bridge failure modes; (b) Sociogram-tab post-ship may exhibit failures in untested query classes; (c) ship-readiness framing inherits the representativeness gap; (d) couples to REVISE-061 (broker-v4 calibration).

  Mitigations available: (a) Expand verification to 3-5 query classes (named-thinker, keyword, paradigm-bridge, multi-hop); (b) define query-class coverage rubric; (c) couple with REVISE-061 calibration sprint.

  Recommendation: CHALLENGED (Moderate)

  STEELMAN:
    Item: PRESUMPTION-272
    Strongest counterargument: Testing literature (Beizer, Myers) requires equivalence-class coverage; single query covers one class. Retrieval-evaluation literature (BEIR, SPECTER) requires multi-query benchmarks. The Sociogram-tab serves a distribution that includes named-thinker, keyword, paradigm-bridge, and multi-hop classes; a single Friston query represents at most one. "Representativeness" without query-class coverage is documented inadequate.
    What would need to be true for C2A2 to be safe: Verification spans 3-5 query classes; query-class coverage rubric defined; ship-readiness rubric includes class-coverage check.
    How to test: Run 3-5 representative queries across classes; compare results to known-good answer set.

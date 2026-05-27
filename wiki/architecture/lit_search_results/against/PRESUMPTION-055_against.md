SEARCH-AGAINST-PRESUMPTION-055:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-055
  Original statement: "Binary static/dynamic partition is the correct primitive for the caching layer (multi-tier alternatives not considered)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-055
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from exclusive two-tier framing in caching-architecture deliverables
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Anthropic multi-breakpoint caching (2024-2025 API updates): Anthropic explicitly supports up to 4 cache breakpoints. The platform itself treats N-tier as a legitimate design space; binary is the minimum, not the recommended maximum.
    2. Multi-tier cache literature (CPU cache hierarchies; CDN edge/origin designs; Kleppmann 2017 "Designing Data-Intensive Applications"): higher-tier caches (L1/L2/L3 analogs) outperform binary caches when the access pattern has a freshness gradient — which is the case for C2A2 (thinker profiles never change; tradition summaries change quarterly; concept nodes change monthly; daily proposals change daily).
    3. Gradient-freshness arguments (Xu et al. 2020 "Caching on the fly"; recent prompt-cache optimization research 2024-2026): when content has a natural change-rate gradient, binary partition forces the slowest tier to be defined by the fastest-changing content in that tier, losing caching value for genuinely-static items inside a mixed tier.
    4. Design-review process critique (Nygard 2011 "Documenting Architecture Decisions"; ADR practice): skipping consideration of alternatives when making an architectural choice is a documented anti-pattern; the design record loses the "why this over that" information even when the choice is correct.
    5. Path-dependency literature (David 1985 "Clio and the Economics of QWERTY"; Arthur 1994 "Increasing Returns and Path Dependence"): architectural choices lock in constraints that are hard to revisit; defaulting to binary without recording the decision makes future revisit harder.

  Strength of challenge: Moderate

  Summary: The presumption's TWO claims differ in vulnerability: "binary is CORRECT" is weakly challenged (binary works for many workloads); "multi-tier was NOT CONSIDERED" is strongly supported as a methodological gap. Anthropic's platform supports up to 4 breakpoints, and C2A2's content has a natural freshness-gradient (quarterly / monthly / weekly / daily change rates) that a multi-tier design could exploit. The design record contains no "we considered N-tier and chose binary because..." reasoning — that absence is the real issue, because it removes the information needed to revisit the choice later.

  Specific risks: (a) Lock-in to suboptimal partition; (b) cost-projection (ASSUMPTION-052) is pessimistic on the upside — multi-tier could do better; (c) design-archaeology loss (future revisit has no record of alternatives considered); (d) the binary commitment becomes harder to revisit as tooling and monitoring are built around it.

  Mitigations available: (a) Add a brief ADR entry documenting the binary choice and acknowledged alternatives (even retrospectively); (b) plan an empirical comparison at the 4-week post-rollout mark against a candidate 3-tier design; (c) instrument cache-hit rate per file to identify any files whose change-rate makes them candidates for a different tier.

  Recommendation: PARTIALLY-CHALLENGED (the binary choice is defensible; the missing deliberation is the real gap; fix is cheap — an ADR entry that records alternatives considered)

  STEELMAN:
    Item: PRESUMPTION-055
    Strongest counterargument: Anthropic's caching platform supports up to 4 cache breakpoints; CPU hierarchies and CDN designs show that multi-tier outperforms binary when content has a freshness-gradient — which C2A2's does (thinker profiles vs. concept nodes vs. tradition summaries vs. daily activity have distinct change rates). The binary choice is not wrong, but its selection without comparison to multi-tier alternatives is a design-process gap. The fix is cheap: an ADR entry recording that alternatives were considered and why binary was chosen; without this, future revisit has no starting point.
    What would need to be true for C2A2 to be safe: Binary is empirically validated at the 4-week mark against a candidate 3-tier comparison; OR the design record explicitly documents the binary-vs-multi-tier decision.
    How to test: At the 4-week post-rollout mark, compare realized cache-hit rate against a simulated 3-tier partition (quarterly / monthly / daily); if 3-tier hit rate is materially higher, the binary choice is a ceiling-limitation.


---

SEARCH-AGAINST-PRESUMPTION-055 (RE-TRIGGER cycle 1):
  Date searched: 2026-05-25
  Original item: PRESUMPTION-055
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c] (cycle 1)
    Original item: PRESUMPTION-055
    Item type: PRESUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-05-24): re-triggered on monthly cadence (MONITOR-056 cycle 1)
      15b (cycle 1, 2026-05-25): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: On-cadence c2a2-lit-search-pipeline processing of the 2026-05-24 15d weekly RE-TRIGGER cohort (15d fired on schedule 2026-05-24; normal hand-off into the daily pipeline, not an exceptional drain).

  New evidence weighed: No new challenging literature surfaced since the last cycle. Prior cycles' findings stand; item remains in its established disposition until new operational evidence (from C2A2's own runs) or new external literature alters the picture.
  Sources (new / refreshed): No new sources this cycle.
  Strength of challenge: Unchanged from prior cycle.
  Summary: Cycle-1 refresh confirms the prior cycle's finding; the challenging literature base has not materially shifted. Recommendation carries forward unchanged.
  Caveats: Automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; a human-driven scan or operational evidence from C2A2's own runs is the more sensitive signal for status change.
  Specific risks: Unchanged from prior cycle.
  Mitigations available: Unchanged from prior cycle.
  Recommendation: refreshed; carry forward prior recommendation

SEARCH-AGAINST-PRESUMPTION-102:
  Date searched: 2026-05-05
  Original item: PRESUMPTION-102
  Original statement: "Daemon link-count partition deterministic across all task creation paths"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as cross-path determinism claim embedded in ASSUMPTION-080
      15b: Searched for challenging literature on path-dependent registration outcomes
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Distributed-systems literature (Lamport 1978; Birman 2012) — path-dependent registration outcomes are documented norm in distributed schedulers; cross-path determinism requires testing.
    2. Scheduler-design literature (Verma et al. 2015) — task-creation paths frequently differ in edge-case handling; cross-path uniformity is goal not default.
    3. Testing literature (Whittaker 2009) — cross-path testing is canonical; absence means uniformity is unsupported.
    4. C2A2-internal: 2026-05-05 single-observation; cross-path was not tested.
    5. Race-condition literature (Lu et al. 2008) — path-dependent races produce skip patterns that look deterministic from one path but vary from another.

  Strength of challenge: Strong

  Summary: Cross-path determinism is not a default in distributed schedulers; it requires testing. PRESUMPTION-102 operates as unstated default without test. Literature is unambiguous: cross-path uniformity needs cross-path testing. The challenge is strong because the literature direction is unanimous and the load-bearing role (ASSUMPTION-081 workaround scope) makes the gap material.

  Specific risks: (a) ASSUMPTION-081 workaround may not work for all task creation paths; (b) silent skips on alternative paths missed; (c) compounds ASSUMPTION-080's single-observation attribution.

  Mitigations available: (a) Cross-path test (3+ creation paths with single-link tasks); (b) explicit treatment in workaround documentation; (c) joint remediation with ASSUMPTION-080 disambiguation.

  Recommendation: CHALLENGED (Strong) — PRESUMPTION + strong challenge → REVISE (low-cost test)

  STEELMAN:
    Item: PRESUMPTION-102
    Strongest counterargument: Cross-path determinism in distributed schedulers is the goal of careful engineering, not the default of casual usage. Distributed-systems literature is unanimous: path-dependent outcomes are the norm; uniformity requires testing. ASSUMPTION-080's single-observation diagnosis cannot establish cross-path uniformity by inspection. PRESUMPTION-102 silently treats one path's behavior as universal, and the workaround in ASSUMPTION-081 inherits this silent extrapolation.
    What would need to be true for C2A2 to be safe: (a) Cross-path test (3 creation paths with single-link tasks); (b) workaround scope explicitly documented per path; (c) joint remediation with ASSUMPTION-080.
    How to test: Create three single-link tasks via different creation paths; observe whether all three skip uniformly. If yes, cross-path determinism supported. If no, path-dependent partition confirmed.

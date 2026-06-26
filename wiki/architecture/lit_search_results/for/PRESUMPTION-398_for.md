SEARCH-FOR-PRESUMPTION-398:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-398
  Original statement: "That a Cowork-app-dependent scheduler constitutes adequate liveness - the same silent-stall class as the unfixed keystone OPEN-086"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-398
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: app-gated scheduling presumed to provide adequate liveness
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. (None supportive.) The reliability/observability literature treats execution that is conditional on an unmonitored external process as a liveness HAZARD, not an adequate posture.

  Strength of support: None

  Summary: No literature supports the presumption that an app-gated scheduler (executing only while the Cowork app is open, with no independent confirmation that it ran) constitutes adequate liveness. The entire heartbeat/dead-man's-switch field exists precisely because such silent non-execution is the failure mode to defend against. This is a NO-SUPPORT-FOUND result; the supportive direction is empty.

  Caveats: A weak convenience argument (no extra infra) exists, but convenience is not liveness adequacy.

  Search scope: Liveness/heartbeat monitoring. Adequate.

  Recommendation: NO-SUPPORT-FOUND

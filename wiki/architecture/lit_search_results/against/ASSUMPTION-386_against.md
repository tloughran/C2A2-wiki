SEARCH-AGAINST-ASSUMPTION-386:
  Date searched: 2026-06-29
  Original item: ASSUMPTION-386
  Original statement: "Bounded alternative (wire ~9 tradition hub pages + dated inbox triage of 456 pages) is the high-signal lever; inbox triage shrinks orphans more than link-seeding."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-386
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: bounded hub-wiring + dated triage proposed as higher-signal than broad link injection
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Acceleration-whiplash / downstream-bottleneck evidence. - Prioritizing a bounded upstream triage can simply relocate the bottleneck downstream; "456 dated inbox pages" is itself a large manual backlog whose triage may not complete or may stall.
    2. Untested comparative claim. - "Inbox triage shrinks orphans MORE than link-seeding" has no benchmark; the two interventions reduce DIFFERENT orphan populations (triage handles inbox; link-seeding handles content pages), so the comparison may be category-confused.
    3. Hub-wiring limits. - Wiring 9 hubs improves navigability TO hubs but does not necessarily reduce the orphan count for the long tail of non-hub pages, so the "high-signal lever" may under-deliver on the stated orphan-reduction goal.

  Strength of challenge: Moderate

  Summary: The bounded plan is reasonable but its central comparative claim is unsupported and possibly mis-specified: inbox triage and link-seeding act on different page sets, so "more than" is not a like-for-like comparison. A 456-page manual triage is a substantial backlog that can stall, and hub wiring helps navigation without necessarily moving the orphan metric for the tail. The plan may be high-signal for navigability while being mislabeled as the best orphan-reduction lever.

  Specific risks: The comparative bet could be wrong; manual triage backlog may not complete; orphan count for content pages may be untouched.

  Mitigations available: Define which orphan population each lever targets; set a WIP-bounded triage commitment with a completion check; measure orphan delta per lever rather than assuming.

  STEELMAN:
    Item: ASSUMPTION-386
    Strongest counterargument: The claim "triage shrinks orphans more than link-seeding" compares two interventions that operate on different page populations, so it may be a category error dressed as a ranking; and a 456-page manual triage is a backlog that can stall, relocating rather than resolving the deficit.
    What would need to be true for C2A2 to be safe: The orphan populations targeted by triage vs link-seeding are comparable, and the triage backlog is actually worked to completion.
    How to test: Tag orphans by type (inbox vs content), apply each lever to its set, and measure the orphan delta.

  Search scope: WIP/triage bottlenecks; intervention comparability; hub-wiring reach. Adequate.

  Recommendation: PARTIALLY-CHALLENGED

SEARCH-AGAINST-PRESUMPTION-398:
  Date searched: 2026-06-26
  Original item: PRESUMPTION-398
  Original statement: "That a Cowork-app-dependent scheduler constitutes adequate liveness - the same silent-stall class as the unfixed keystone OPEN-086"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-398
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: app-gated scheduling presumed to provide adequate liveness
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Heartbeat / dead-man's-switch monitoring (OneUptime; Prometheus Watchdog; watchflow "silent cron failures"). - Adequate liveness REQUIRES detecting non-execution; "absence is the signal." An app-gated job with no external ping cannot detect its own silence.
    2. Observability literature on silent outages. - "The worst outage is the silent one where nobody notices because absence of data triggers no alert" - exactly the app-gated scheduler's failure mode.
    3. C2A2 OPEN-086 (keystone silent-stall gap). - The presumption is the same vulnerability class already flagged as an unfixed keystone.

  Strength of challenge: Strong

  Summary: Adequate liveness has two requirements - the job runs, AND the system can tell when it didn't. An app-gated scheduler with no independent monitor fails both: it stops when the app is closed and emits nothing to mark the gap. The dead-man's-switch pattern was invented for precisely this hazard. Because this recapitulates the unfixed keystone OPEN-086 on a demo-critical tool, the presumption is not merely unsupported but actively contradicted by the monitoring literature.

  Specific risks: Silent staleness presented as live during demos; loss of trust in the Heartbeat; the keystone liveness gap propagates to a new surface unnoticed.

  Mitigations available: External dead-man's-switch (success-ping + absence alert); OS-supervised scheduler independent of the app; surfaced last-run age with a staleness threshold and a visible "stale" state.

  STEELMAN:
    Item: PRESUMPTION-398
    Strongest counterargument: Liveness is meaningless without a non-execution detector. An app-gated job is liveness theater: it appears to provide freshness while structurally unable to report its own failure, so it inherits the exact silent-stall class as OPEN-086 - a known, unfixed keystone risk now duplicated.
    What would need to be true for C2A2 to be safe: An independent monitor detects missed runs and the schedule does not depend on a foregrounded app.
    How to test: Disable/close the app; confirm an external monitor fires on the missed run. No alert => presumption falsified.

  Search scope: Liveness/heartbeat/dead-man's-switch; silent outages. Comprehensive.

  Recommendation: CHALLENGED

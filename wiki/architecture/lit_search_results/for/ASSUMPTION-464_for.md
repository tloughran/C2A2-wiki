SEARCH-FOR-ASSUMPTION-464:
  Date searched: 2026-07-17
  Original item: ASSUMPTION-464
  Original statement: Same-day, two-agent contradiction on OpenStory — morning project status "database healthy / No issues" (liveness + DB probe) vs. evening "down an 11th day" (delivery vantage); a fresh instance of SYSTEMIC-RISK #4 liveness-as-success.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-464
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-07-16 same-day contradictory verdicts
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. dev.to (Dumont), 2026. "Health Checks That Actually Work: Liveness vs Readiness vs Startup Probes." — "A process can be alive and useless at the same time"; liveness-only checks return healthy while the service cannot serve. Exactly maps the DB-probe "healthy" vs delivery "down."
    2. thetruecode.com, "Your Production Health Checks Are Lying to You." — Liveness-only healthy signals let a failure fester silently until a human notices.
    3. DZone / etcd split-brain literature. — From one vantage a subsystem "might be dead, unreachable, or perfectly healthy but separated"; the observer cannot distinguish without reconciliation. Grounds vantage-relative health verdicts.

  Strength of support: Strong

  Summary: The liveness-vs-readiness distinction is a textbook, widely documented pattern that precisely explains the observed contradiction: the DB probe answers "is the process alive?" while the delivery vantage answers "is the service usable?" These are different questions with different correct answers. The split-brain / partial-observability literature further supports that two truthful observers can disagree on health.

  Caveats: The literature also says the fix (deep/readiness checks, reconciliation) is standard — so the contradiction reflects a missing reconciler, not an unknowable state. Support is for the phenomenon and its named cause.

  Recommendation: SUPPORTED

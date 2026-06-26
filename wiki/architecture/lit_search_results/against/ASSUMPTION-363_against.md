SEARCH-AGAINST-ASSUMPTION-363:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-363
  Original statement: "That a Cowork-app-dependent 6-hour scheduled task is adequate cadence to keep the local Heartbeat fresh ('runs only while the Cowork app is open')"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-363
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: app-gated 6h scheduled refresh assumed adequate for Heartbeat freshness
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. watchflow, "Why Cron Jobs Fail Silently"; heartbeat-monitoring literature. - A scheduled job that does not run produces NO error - the failure is silent and can go unnoticed for days; cadence is irrelevant if execution is not guaranteed.
    2. Dead-man's-switch / heartbeat-monitoring pattern (OneUptime, Prometheus Watchdog). - The standard defense is an external monitor where "absence is the signal"; an app-gated job with no external ping has no way to detect its own non-execution.
    3. C2A2's own keystone OPEN-086 (silent-stall liveness gap). - This assumption recapitulates an already-identified unfixed gap.

  Strength of challenge: Strong

  Summary: The challenge is not about 6 hours - it is about "runs only while the Cowork app is open." Tying execution to a foregrounded desktop app with no independent liveness check is the canonical silent-failure mode: if the app is closed/asleep, the job simply never fires and nothing reports the gap, so "fresh" silently becomes "arbitrarily stale." The dead-man's-switch literature exists specifically to catch this. The cadence is adequate only conditional on execution, and execution is exactly what is not guaranteed. This is the keystone OPEN-086 liveness gap on a demo-critical tool.

  Specific risks: Heartbeat silently goes stale during any period the app is closed; observers (including demos) trust a stale view; the staleness is undetectable from inside the system.

  Mitigations available: External heartbeat/dead-man's-switch monitor (job pings on success; absence alerts); a supervised (launchd/cron) scheduler independent of the app; a visible last-run timestamp + staleness threshold.

  STEELMAN:
    Item: ASSUMPTION-363
    Strongest counterargument: Freshness requires guaranteed execution plus detection of non-execution. An app-gated job provides neither: it can silently not run, and nothing external notices - so the "6h freshness" claim is unfalsifiable from inside and fails exactly when the app is not in use, which is most of the time.
    What would need to be true for C2A2 to be safe: Either an external dead-man's-switch detects missed runs, OR the scheduler is OS-supervised and independent of the app, AND the UI shows true last-run age.
    How to test: Close the Cowork app for >6h; check whether the Heartbeat detects or surfaces its own staleness. If it shows fresh or fails silently, the assumption is falsified.

  Search scope: Cron silent failure; heartbeat/dead-man's-switch monitoring. Comprehensive.

  Recommendation: CHALLENGED

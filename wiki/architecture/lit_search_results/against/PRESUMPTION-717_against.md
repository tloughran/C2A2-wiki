SEARCH-AGAINST-PRESUMPTION-717:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-717
  Original statement: That a missed day heals itself; the daily 14a/14b series broke for the first time in 118 days and nothing fired on the absence — the gap was found incidentally by a downstream queue count, not by any liveness signal.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-717
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from what did not happen — no alarm, no retry, no gap marker, and a next-day all-clear
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Dead man's switch / heartbeat monitoring pattern (industry practice write-ups, updog.watch, watchflow.io, oneuptime.com, drumbeats.io, 2026). Establishes "guilty until proven innocent": a scheduled job must actively report success at each interval; absence of a signal, not presence of an error, is treated as the failure indicator. Systems that only watch for errors systematically miss silent non-runs.
    2. Safety and liveness properties (Alpern & Schneider formulation, summarized at en.wikipedia.org/wiki/Safety_and_liveness_properties and courses.cs.washington.edu CSE452 notes). Formal result: a liveness property cannot be falsified by any finite observed prefix — a system with no active liveness monitor can run silent indefinitely before any violation becomes detectable at all, which matches the 118-day-then-gap pattern exactly.
    3. Cron/scheduled-job monitoring practice (onlineornot.com, simpleobservability.com, cronping.com, "Cron Job Monitoring Best Practices," 2026). Documents that expired credentials, hung processes, or scheduler death all produce zero errors and no alerts by default; discovery happens only when someone happens to notice a downstream gap — the same incidental-discovery pattern described in this presumption.

  Strength of challenge: Strong

  Summary: Reliability-engineering literature on dead-man switches, heartbeat monitoring, and formal liveness properties directly and repeatedly contradicts the presumption that a missed run is self-correcting or will surface on its own. The consensus across both distributed-systems theory and monitoring practice is that liveness failures are invisible by construction unless an external watcher expects a periodic signal and alarms on its absence. A long unbroken streak (118 days) is precisely the profile most likely to mask a missing-liveness-monitor problem, since success was never actively proven, only never contradicted.

  Specific risks: Future missed days (isolated or accumulating) will go undetected unless a downstream artifact count happens to catch them; any process depending on daily freshness of the 14a/14b series can silently decay, with errors compounding invisibly until an unrelated audit stumbles on the gap, as already happened once.

  Mitigations available: Yes — this is a well-solved pattern. An independently-clocked heartbeat/dead-man-switch check (external monitor expecting a "last successful run" ping) is standard, low-cost, and directly closes this gap.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-717
  Strongest counterargument: Absence-of-failure is not evidence of health in any system whose only success signal is "nothing bad appeared downstream." The standard industry response to exactly this failure mode is dead-man-switch/heartbeat monitoring, precisely because passive designs run clean for arbitrarily long stretches while accumulating undetected gaps, discovered only by incidental correlation elsewhere — never by design.
  What would need to be true for C2A2 to be safe: An independent, externally-clocked watcher would need to expect a signal from the 14a/14b series at a fixed interval and alarm on its absence, decoupled from any downstream artifact count; the 118-day run would then have to be reframed as "118 days without an alarm" rather than "118 days of proven liveness."
  How to test: Deliberately skip one cycle in a staging clone and measure whether any signal fires within one cycle length; if the only detection path is a human or downstream agent noticing an artifact gap, the presumption is empirically confirmed false.

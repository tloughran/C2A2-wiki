SYSTEMIC-RISK-FLAG:
  Date: 2026-09-16
  Raised by: Agent 15b
  Affected items: PRESUMPTION-414, PRESUMPTION-439
  Severity: High

  PROVENANCE:
    Origin: 14b (both items)
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a, 15b -> 15c]
    Item type: PRESUMPTION (unstated — surfaced by inference) for both
    Transform at this step: 15b cross-item pattern detection during the 2026-09-16 backlog-drain run
    Current status: FLAGGED

  Common vulnerability: MEASURE ADOPTED / VALIDATION INSTRUMENT NAMED / INSTRUMENT NEVER RUN.
    In both items a summary measure was taken as ground truth — connectivity as vault health
    (PRESUMPTION-414), a three-way robust/directional/null sort as a result classification
    (PRESUMPTION-439). In both, the literature names exactly one cheap, standard validation instrument —
    a proxy-reliability correlation against a non-link outcome; a leave-one-conversation-out
    recomputation. In both, that instrument was written into the MONITOR entry AT INTAKE — 2026-06-29 and
    2026-07-03 — and has not been run in the 75 and 79 days since. Neither measure has been retired and
    neither has been validated; both continue to be cited.

  Why this is not a new pattern: it is a second cohort of the pattern recorded on 2026-09-12 as "owed
    measurements never executed" (items 1321, 959, 960, 968), and it is adjacent to the 2026-09-14 flag on
    pre-check instruments failing silently. Filed as an EXTENSION of the 09-12 flag rather than as a fresh
    pattern, because minting a new flag for a known pattern is itself an instance of the pattern.

  What these two add that the 09-12 cohort did not:
    1. The owed measurements are OLDER than any in that cohort — 75 and 79 days versus days.
    2. They sit in the 15d RE-TRIGGER lane, not the intake lane. The 15d run measured that lane at 280
       standing unconsumed blocks draining at 7 blocks per fortnight. At that rate the lane does not
       clear, and an item's named instrument is re-named weekly by a re-trigger that evaluates no
       evidence. The re-trigger mechanism is therefore generating the appearance of ongoing scrutiny over
       items nobody is scrutinising.
    3. The cost of the two unrun instruments is five recomputations and one correlation, over data
       already on disk. This is not a resourcing problem.

  Steelman of the contrary reading: a re-trigger lane that does not drain may be correct behaviour if the
    items in it are genuinely low-value, and 15d's stale-downgrade mechanism exists to move such items to
    monthly cadence. That defence does not cover these two: both were filed HIGH, both remained HIGH
    through every cycle, and both had their instruments specified rather than left vague. If HIGH items
    with named, cheap instruments do not get run, the priority field is not doing any work.

  Falsifiable test of this flag: count, across the whole register, MONITOR entries whose "what would
    change the disposition" field names a specific runnable command or computation, and count how many
    have ever been executed. A near-zero execution rate confirms the flag directly; a substantial rate
    refutes it and these two are outliers. One query over monitor_queue.md.

  Recommended disposition: do not mint a premise. This is an enforcement gap, and the enforcement gap
    already has a flag. The actionable remedy is a field, not a research item: a MONITOR entry whose
    discharge condition is a named command should carry an OWNER and a DUE DATE, and a re-trigger that
    fires on an item whose instrument is past due should report the overdue state rather than resetting
    the cycle counter.

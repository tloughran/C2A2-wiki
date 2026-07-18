SEARCH-AGAINST-PRESUMPTION-481:
  Date searched: 2026-07-16
  Original item: PRESUMPTION-481
  Original statement: [inferred] A scheduled task that crashes mid-run is presumed a harmless no-op covered by tomorrow's run; the architecture presumes runs are idempotent and losslessly skippable, though four 07-14 crashes retried nothing, emitted no partial artifact, and raised no alarm.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-481
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result CHALLENGED (strength Strong)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. At-least-once delivery / retry semantics (distributed-systems canon): idempotent-and-skippable requires a retry mechanism and a durable 'started-but-not-finished' marker; absent both, a crash is silent data loss.
    2. Crash-only software (Candea & Fox 2003): crash-only systems are safe only because they checkpoint state and recover; a crash with no partial artifact and no alarm is the un-safe case.

  Strength of challenge: Strong

  Summary: Strongly challenged. The presumption bundles two false beliefs: that runs are idempotent (re-running produces the same result harmlessly) and that a missed run is losslessly covered by the next. Neither holds without checkpointing and retry, which the fleet lacks - the four 07-14 crashes retried nothing, left no partial artifact, and raised no alarm. There is no 'started-but-did-not-finish' signal, so a whole day's throughput vanished with no record it was attempted.

  Specific risks: A day of lit-search throughput can disappear silently; downstream agents consume a gap as if it were an empty result.

  Mitigations available: Add a durable start marker + completion marker, retry-on-crash, and a 'started-but-unfinished' alarm the watchdog reads.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-481
    Strongest counterargument: A cron-style fleet with no started-but-unfinished signal cannot distinguish 'ran and correctly produced nothing' from 'crashed and lost everything'. Tomorrow's run does not cover today's loss unless the work is idempotent AND re-queued - and nothing re-queues it. The presumption of lossless skippability is therefore not a simplification but a silent data-loss generator.
    What would need to be true for C2A2 to be safe: Runs would have to be genuinely idempotent and automatically re-queued on crash - neither is implemented.
    How to test: Inject a mid-run crash; check whether any partial artifact, retry, or alarm results (07-14 shows: none).

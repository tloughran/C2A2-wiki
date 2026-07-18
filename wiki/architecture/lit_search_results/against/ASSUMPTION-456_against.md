SEARCH-AGAINST-ASSUMPTION-456:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-456
  Original statement: A task with a current lastRunAt is presumed to have produced a valid, non-empty output artifact; firing is read as success, so the watchdog called 07-14 healthy while four tasks crashed mid-response and wrote nothing.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-456
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result NO-CHALLENGE-FOUND (strength Weak)
    Current status: NO-CHALLENGE-FOUND

  Challenging evidence found: No

  Sources:
    1. No source defends liveness-as-correctness. Minor nuance: for genuinely idempotent, output-optional tasks, lastRunAt may be an adequate proxy - but lit-search/delivery tasks are output-bearing, so the exception does not apply.

  Strength of challenge: Weak

  Summary: No real challenge. The only nuance is that a liveness proxy suffices for tasks with no required output; C2A2's tasks are output-bearing, so the exception is inapplicable.

  Specific risks: The fleet's only failure detector certifies crashed, empty-output runs as healthy - the defect that made 07-14's data loss invisible.

  Mitigations available: Add an artifact-content check (non-empty, well-formed, recent) to the watchdog for every output-bearing task.

  Recommendation: NO-CHALLENGE-FOUND

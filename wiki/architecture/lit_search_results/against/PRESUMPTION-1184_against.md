# PRESUMPTION-1184 — Literature Search AGAINST (15b)

Search scope: PRELIMINARY SEARCH. A broader search is recommended. Budget used for this item: 3 web searches (standard mode) and 1 page fetch, which succeeded (Derosiaux 2024, Conduktor, read in full). Run id cowork-local-2026-10-26-fb3b3795. I did not open lit_search_results/for/ or lit_search_returns.md.

Reading of "challenge" used: evidence that the presumption, its literature claim, or its implied remedy (a later run should run a completeness check before standing down) is mis-specified, overstated or bounded. I did not dispute the facts in the item (the MONITOR-685 misroute, or the PASS credited to an unidentified run).

```
SEARCH-AGAINST-PRESUMPTION-1184:
  Date searched: 2026-10-26
  Original item: PRESUMPTION-1184
  Original statement: "[inferred] The earliest same-day output is presumed complete and
    authoritative. Later firings stand down on finding any prior output, without checking it.
    ... Distinct from PRESUMPTION-1180 (whether later runs defer at all): this concerns what
    deferring ratifies."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1184
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred at the 2026-10-25 intake from double-firing behaviour (15d deferring to the
           "first" copy that misrouted MONITOR-685; telemetry PASS for a partial run credited
           to an unidentified overlapping run).
      15b: Searched for challenging literature (preliminary; 3 searches, 1 fetch)
    Current status: SEARCHED-15b — PARTIALLY-CHALLENGED

  Challenging evidence found: Partial (challenges the implied remedy and the framing of the
    literature claim, not the diagnosis)

  Sources:
    1. Derosiaux, S., 2024 (modified 2026-10-01). "Build Idempotent Kafka Consumers: Patterns
       That Actually Work." Conduktor blog. [fetched; read in full; vendor source]
       — Mis-specification challenge. Established idempotent-consumer designs DO let a
       duplicate stand down on the mere existence of a marker, without checking content: "if
       (deduplicationStore.hasProcessed(key)) ... return". Safety comes from writing the marker
       atomically with the work ("If the order creation fails, the deduplication record also
       rolls back"), not from a completeness check by the later run. The article also warns
       against reading first: "Don't add a SELECT before the INSERT: that check-then-insert is
       the race." A completeness check by the later firing is itself a check-then-act and would
       widen the race window rather than close it.
    2. Kubernetes CronJob API reference (batch/v1), concurrencyPolicy: Allow (default) /
       Forbid ("skipping next run if previous hasn't finished yet") / Replace ("cancels
       currently running job and replaces it"). Also OneUptime guide (2026-02-09).
       [snippet only]
       — Boundary challenge to the claim that batch schedulers require completeness checks.
       The canonical scheduler policies decide on the run's state (running or not), not on its
       output, and none validates the earlier run's output. Forbid is itself a "first run wins,
       later run stands down unchecked" policy. Duplicate-run handling in the scheduler layer is
       about overlap, and output correctness is left to the job.
    3. Airflow FileSensor source (1.10.x) and an atomic-rename idempotency guide (flaviocopes.com);
       secondary summaries of exactly-once as "at-least-once + idempotent = effectively once"
       (SoftwareMill; Codemia; RabbitMQ list 2010). [snippet only; mixed quality]
       — Bounding challenge. In practice existence checks are normal and safe when the final
       artefact appears atomically (temp file + rename, or a _SUCCESS marker written last).
       FileSensor returns true when a path exists, with no content check. The known flaw is
       non-atomic publication, not deferral to existence.

  Strength of challenge: Moderate against the implied remedy (a completeness check by the later
    run) and against the reading that established designs require validated writes. None
    against the diagnosis that the current stand-down ratifies partial or wrong output.

  Summary: The literature does not say that a duplicate must validate prior output before
    standing down. Mainstream designs (idempotent consumers, CronJob Forbid, existence sensors)
    defer on existence and get safety by making the existence signal atomic with completion: the
    marker is written only in the same commit as the work, or last. So the defect in 1184 is
    better described as a non-atomic "output exists" signal (a partial or in-progress file counts
    as done) than as missing validation. A further challenge is that the item conflates
    completeness with correctness. MONITOR-685 was misrouted, not incomplete. No dedup or
    exactly-once scheme protects against complete but wrong output. Idempotency only ensures a
    duplicate does not change the result, so it would ratify the misroute too.

  Specific risks: (a) Adding a read-and-validate step to later firings creates a check-then-act
    race between concurrent copies, with two "validators" each deciding the other is
    incomplete, so the two copies may both write. (b) A completeness check will still pass the
    misrouted MONITOR-685 case, which gives false assurance. (c) A validator agent that can
    "correct" the first copy restores last-writer-wins and loses the dedup property.

  Mitigations available: (i) Atomic publish: write to a temp name and rename, or write a
    completion marker last. A later run stands down only on the marker, never on a partial
    file. (ii) Stamp the marker with the writing run's id so PASS cannot be credited to an
    unidentified run. (iii) Handle correctness (routing) through a separate downstream check,
    not through dedup logic. (iv) Prefer preventing the double fire (CronJob Forbid-style
    single-flight) over adjudicating between copies.

  Recommendation: PARTIALLY-CHALLENGED
```

```
STEELMAN:
  Item: PRESUMPTION-1184
  Strongest counterargument: Standing down on mere existence is not a naive shortcut. It is the
    textbook idempotent-consumer and Forbid-policy behaviour, and it is correct whenever
    "exists" means "committed". The literature's lesson is to make the existence signal
    trustworthy (atomic, written last, tagged with its writer), not to have each duplicate
    audit its predecessor. Audit-on-defer is a check-then-act pattern that the same literature
    names as the race. It also cannot catch the failure that actually happened here
    (misrouting), because that output was complete, only wrong. 1184's real defect is that
    C2A2's "output exists" signal is published non-atomically and carries no writer id.
  What would need to be true for C2A2 to be safe: outputs are published atomically with a
    completion marker; the marker carries a run id; telemetry PASS lines name the run that
    wrote the marker; routing correctness is checked by a separate, later step.
  How to test: (a) Kill a run mid-write in a sandbox and fire a second copy. If it stands down
    on the partial file, the defect is non-atomic publication. Repeat with temp+rename and
    confirm the second copy proceeds. (b) Feed a complete but misrouted output to any proposed
    completeness check and see whether it passes.
```

Source-reading status: Source 1 [fetched; read in full; vendor blog]. Sources 2 and 3 [snippet only]. I did not read Kleppmann, DDIA ch. 11 directly, so claims about what DDIA says are UNVERIFIED and not relied on here. I did not read Airflow's current documentation on concurrency or `max_active_runs`.

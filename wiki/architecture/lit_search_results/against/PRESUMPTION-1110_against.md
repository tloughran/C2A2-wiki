SEARCH-AGAINST-PRESUMPTION-1110:
  Date searched: 2026-10-04
  Original item: PRESUMPTION-1110
  Original statement (presumption under test): Scheduled tasks fire exactly once per slot, so a task can treat existing same-day output as the work of an earlier run.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1110
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (lane: at-least-once vs exactly-once execution in job schedulers; idempotency keys; fencing tokens).
      15b: Searched for challenging literature; found vendor documentation and cron DST behaviour contradicting exactly-once firing; strength: Strong
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Google Cloud, "Cloud Scheduler overview" (docs.cloud.google.com/scheduler/docs/overview) [search-result; a fetch was attempted but the tool returned a dedup notice with no content, so it is not labelled fetched] — States that Cloud Scheduler provides "at least once" delivery and "in some rare circumstances, it is possible for a job to run multiple times in association with a single instance of the schedule", so targets "should be idempotent". It supplies an X-CloudScheduler-ScheduleTime header so handlers can deduplicate. A major managed scheduler says outright that it does not fire exactly once.
    2. Red Hat Bugzilla #138001 "Cron jobs run twice during Daylight savings time"; FreeBSD Bug 166318 (crontab(5)/cron(8) DST contradictions); Red Hat KB 477963 [search-result] — When clocks fall back, a job in the repeated hour can run twice; when they spring forward, a job can be skipped or run late. Vixie/ISC cron mitigates this only for jobs with granularity over one hour, and "unless cron is restarted or the user's crontab is changed" during the window. Exactly-once per slot is a best-effort property, not a guarantee.
    3. healthchecks.io blog "How Debian Cron Handles DST Transitions"; dev.to/cronmonitor "Handling timezone issues in cron jobs" [search-result, practitioner] — Recommend execution locks because duplicates still occur.
    4. Kleppmann, M., 2016. "How to do distributed locking" (blog), and Designing Data-Intensive Applications (2017), ch. 8 [background-knowledge] — A process that checks a condition and then acts can be paused (GC, sleep, laptop lid) between check and act, so lease- or existence-based mutual exclusion is unsafe without a fencing token. "Output exists, so an earlier run did it" is a check-then-act on a non-atomic marker.
    5. General distributed-systems result (two-generals / FLP-adjacent folklore; e.g. AWS Builders' Library "Making retries safe with idempotent APIs") [background-knowledge] — Exactly-once *delivery* cannot be guaranteed over unreliable channels; systems get exactly-once *effect* from at-least-once delivery plus idempotent handling.

  Strength of challenge: Strong

  Summary: The literature and vendor documentation agree that schedulers give at-least-once (sometimes at-most-once) firing, not exactly-once. Managed schedulers (Cloud Scheduler) say so explicitly; classic cron double-fires or skips around DST changes, restarts and crontab edits. Retry layers, manual re-runs and overlapping sessions add more duplicates. The second half of the presumption, treating existing same-day output as a *completed* earlier run, also fails: the output may be partial (a concurrent run still writing, or one that crashed mid-write), or may come from a different process (manual run, another agent) that did different work. Without an atomic completion marker keyed to the schedule slot, "file exists" does not show "the slot's work is done".

  STEELMAN:
    Item: PRESUMPTION-1110
    Strongest counterargument: Exactly-once firing is something no mainstream scheduler promises. Designs that rely on it work most of the time and fail in rare, hard-to-reproduce windows (DST, restarts, retries, an app that resumes after sleep and catches up on missed runs). The skip-if-output-exists rule turns a duplicate firing into something worse than a duplicate: a run that sees a half-written or failed earlier output will skip and leave the slot incomplete, while reporting that it deferred to a run that never finished. The failure is silent because the artefact exists.
    What would need to be true for C2A2 to be safe: (a) The specific scheduler in use (Cowork scheduled tasks) documents single-fire semantics, including catch-up behaviour after sleep/offline; and (b) the "earlier run" check reads an atomic completion marker (written last, keyed to the slot, ideally carrying a run ID) rather than the presence of output; or (c) the task is idempotent, so a re-run is harmless and no skip logic is needed.
    How to test: Review the scheduler's logs for duplicate fires per slot over 30+ days, including DST transitions and machine sleep/wake. Fault-inject by killing a run mid-write and check whether the next run detects the incomplete output or skips it.

  Specific risks: A partial or failed output is accepted as a completed run (silent gap); two concurrent runs both write and clobber shared files; the run log shows "skipped — already done" for work that was never finished.

  Mitigations available: Idempotency key = task name + scheduled slot time (the Cloud Scheduler header pattern); write-then-rename atomic completion markers containing run ID and status; fencing tokens or lock files with expiry for concurrent writers; make the task idempotent so re-runs are safe.

  Caveats: The challenge is to the exactly-once *premise*. Treating existing output as a reason to skip is partly a deduplication pattern, and it is sound if the marker is atomic and records completion. In practice duplicate fires are rare; the risk is in tail events, not the typical day.

  Search scope: preliminary search (2 searches, 1 fetch attempted but returned no content), plus established distributed-systems background; independent of 15a.

  Recommendation: CHALLENGED

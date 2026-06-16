SEARCH-AGAINST-PRESUMPTION-348:
  Date searched: 2026-06-16
  Original item: PRESUMPTION-348
  Original statement: "[inferred] A failing scheduled task announces its own failure (no liveness monitor; channel degraded ~3 days, 06-13 summaries simply missing)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-348
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from the ~3-day silent summary outage
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Dead-man's-switch / heartbeat monitoring (UpDog, "What is a Dead Man's Switch?"; watchflow 2026, "Why Cron Jobs Fail Silently"). — The foundational principle is "guilty until proven innocent: assume the job failed unless it actively reports success." This is the exact inverse of the presumption. A job that fails (or never starts) produces NO error precisely because it did not run; the silence is the failure, not a report of health.
    2. Silent-failure characterization (OnlineOrNot, "Cron job monitoring"; "Kubernetes CronJobs silently fail more than you think," DEV 2026). — "Silent failures occur when nothing crashes, nobody gets paged, and you only notice when data is missing." "A cron job that doesn't run produces no errors—it just doesn't happen... you might not notice for days or weeks." Directly describes the observed 3-day outage.
    3. Output-assertion monitoring (deadmancheck, GitHub; "alert if count < N"). — Even a job that RUNS and "succeeds by every technical measure" can do nothing useful; catching that requires output assertions, a layer beyond mere error-reporting. Shows that not only does failure not announce itself, even nominal success can be hollow.

  Strength of challenge: Strong

  Summary: The presumption is strongly challenged and already falsified by the 3-day silent outage that surfaced it. The entire discipline of cron/scheduled-task monitoring is premised on the opposite principle: failures are silent by default, so health must be inferred from a POSITIVELY RECEIVED, regularly-expected success signal, with absence of that signal triggering the alert. A task that dies, never starts, or hangs emits nothing; "no news" is the single most dangerous reading. The remedy (heartbeat/dead-man's-switch + output assertions) is standard and cheap.

  Specific risks: Without a liveness monitor, any scheduled-task failure is invisible until a human happens to notice missing output — here ~3 days, but unbounded in principle. Coupled with PRESUMPTION-347 (model-pin rot), a single vendor deprecation can silently disable a pipeline indefinitely. Downstream consumers (the self-awareness pipeline, EOD summaries) silently operate on stale or absent inputs, propagating the gap.

  Mitigations available: (a) Dead-man's-switch: the task pings an external monitor on success; the monitor alerts if no ping arrives within the expected window (the && pattern — ping only on clean exit). (b) Output assertions: alert if the run produced fewer than N expected artifacts, catching ran-but-did-nothing. (c) Distinguish "ran" from "succeeded" in a status log. These are minutes-to-implement with hosted services (healthchecks.io-style) or a few lines locally.

  STEELMAN:
    Strongest counterargument: For a genuinely low-stakes, self-correcting personal task (a daily summary scrape), a missed run on any single day is inconsequential, and instrumenting every personal cron job with external monitoring could be over-engineering for a one-person system. So the presumption is defensible for trivial, idempotent, frequently-repeating tasks where the cost of a missed run is near zero.
    What would need to be true for C2A2 to be safe: Either the task must be truly inconsequential when skipped (no downstream depends on it), OR — since downstream pipelines DO depend on these summaries — it must carry a heartbeat so a multi-day gap cannot pass unnoticed. The observed 3-day propagation shows the "inconsequential" condition does not hold here.
    How to test: Add a heartbeat to one scheduled task; simulate a failure (bad model pin) and confirm the absence-alert fires within one expected interval. Confirms the monitor closes the gap the presumption left open.

  Search scope: Dead-man's-switch/heartbeat monitoring, silent cron failure detection, output-assertion monitoring, observability of scheduled jobs. Comprehensive. (Member of the SYSTEMIC-RISK cluster flagged in PRESUMPTION-347_against.)

  Recommendation: CHALLENGED

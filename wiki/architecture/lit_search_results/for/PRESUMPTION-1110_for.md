SEARCH-FOR-PRESUMPTION-1110:
  Date searched: 2026-10-04
  Original item: PRESUMPTION-1110
  Original statement (presumption under test): Scheduled tasks fire exactly once per slot, so a task can treat existing same-day output as the work of an earlier run.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1110
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (lane: at-least-once vs exactly-once execution in job schedulers; idempotency keys; fencing tokens).
      15a: Searched for supporting literature; found only conditional/engineered support (exactly-once achievable via per-slot dedup keys, not native); strength: Weak
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial (conditional only)

  Sources:
    1. Google Cloud, "About Cloud Scheduler" (docs, last updated 2026-09-30). https://docs.cloud.google.com/scheduler/docs/overview [fetched]: The service is "designed to provide 'at least once' delivery". It says duplicate runs happen only "in some rare circumstances", and it provides an `X-CloudScheduler-ScheduleTime` header that "remains constant across retry attempts" so that handlers can dedupe. This is weak support for the idea that multiple fires are rare in practice. The same page states that the guarantee is at-least-once, not exactly-once, and requires targets to be idempotent.
    2. Kubernetes documentation, "CronJob". https://kubernetes.io/docs/concepts/workloads/controllers/cron-jobs/ [search-result]: A CronJob creates a Job "approximately once per execution time". Two Jobs, or none, may occasionally be created, so Jobs "should be idempotent". This supports "approximately once" as the usual case. It does not support "exactly once".
    3. DBOS, "Building a Better Cron for the Cloud". https://dbos.dev/blog/how-to-build-cloud-cron-jobs [search-result]: Exactly-once workflow initiation is achieved by assigning a unique key built from the function name and the scheduled time, then deduplicating on that key. This is analogous support: per-slot exactly-once is achievable, but only as an engineered property.
    4. techinterview.org, "Cron Service Low-Level Design: ... Exactly-Once Execution" [search-result]: Uses a unique index on (cron_job_id, scheduled_at) as the exactly-once enforcement mechanism. This is the same conditional pattern as source 3.
    5. Kleppmann, M., 2017. *Designing Data-Intensive Applications*, Ch. 8–9 (fencing tokens, effectively-once via idempotence) [background-knowledge]: This is theoretical grounding for the claim that "exactly once" in distributed settings means "effectively once": at-least-once delivery plus an idempotent or deduplicated effect. It gives no grounding for a native exactly-once guarantee.

  Strength of support: Weak

  Summary: No source states that general-purpose schedulers natively fire exactly once per slot. Vendor documentation (Cloud Scheduler, Kubernetes) does describe duplicate or missed fires as rare, so "approximately once" is the typical empirical case. That gives weak support to the heuristic in normal operation. Exactly-once per slot is well documented as achievable, but only when it is engineered with a slot-keyed dedup or unique constraint (DBOS; distributed-cron designs). Read charitably, the presumption holds only where such a slot-identity mechanism exists. Even then, the inference "existing same-day output = an earlier run's work" further requires that output be keyed to the slot and run, not merely to the day.

  Caveats: (a) The sources that support the claim also say explicitly that the guarantee is at-least-once, so the support is for "usually once", not "exactly once". (b) The scheduler in C2A2 (LLM-agent scheduled tasks on a desktop host) is not covered by any source found. Behaviour around sleep/wake, catch-up runs and manual re-triggers is unexamined. (c) Same-day output could also come from manual runs or other tasks. No literature addresses that attribution step.

  Search scope: preliminary (2 searches, 1 fetch): Google Cloud Scheduler docs, Kubernetes CronJob docs, distributed-cron design posts, DDIA (background). Broader search recommended: systemd timers (Persistent=, missed runs), macOS launchd catch-up semantics, Quartz misfire policies.

  Recommendation: PARTIALLY-SUPPORTED (holds only where exactly-once is engineered via slot-keyed dedup; native exactly-once unsupported)

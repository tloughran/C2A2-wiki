SEARCH-AGAINST-PRESUMPTION-432:
  Date searched: 2026-07-02
  Original item: PRESUMPTION-432
  Original statement: "[inferred] That the compute sandbox's ephemeral disk is unbounded/self-managing — no monitoring or scratch GC, so a full container disk silently halts any agent needing local writes."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-432
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the 2026-07-01 disk-full incident
      15b: Searched for challenging literature (genuine web search 2026-07-02)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kubernetes docs + issue #91600 / Red Hat solution 4367311 — ephemeral-storage is a bounded, exhaustible resource; when a node/pod exceeds thresholds the kubelet enters "disk pressure" and EVICTS or fails workloads. Directly refutes "unbounded."
    2. Last9 + OneUptime, "Monitor Ephemeral Storage" / "Ephemeral Storage Limits" (2026) — default tooling gives LIMITED visibility into ephemeral usage, so exhaustion tends to surface as unexplained eviction/failure. The remedy is explicit requests/limits, proactive monitoring, log rotation and cleanup — i.e., it is NOT self-managing; it must be managed.
    3. Portworx knowledge-hub, "Ephemeral Storage in Kubernetes" — ephemeral scratch must be sized and GC'd; unmanaged growth is a known node-level hazard that can affect the whole node, not just one workload.

  Strength of challenge: Strong

  Summary: The container/orchestration literature is explicit that ephemeral disk is bounded and exhaustible, that exhaustion causes eviction or silent write-failure, and that visibility is poor by default — so the resource must be explicitly monitored, quota'd, and cleaned. The presumption that it is unbounded/self-managing is the exact belief that produces the observed silent halt. It is strongly challenged.

  Specific risks: Any agent needing local writes halts (or is evicted) with no clear error the moment scratch fills; because default visibility is poor, the halt is silent and misattributed to downstream symptoms (see PRESUMPTION-433). Node-level exhaustion can affect co-located work, not just the culprit.

  Mitigations available: Add ephemeral-disk monitoring with a threshold alert; set explicit scratch quotas; implement scratch GC / cleanup between and within runs; fail loud (emit an explicit "disk full" error) instead of halting silently.

  STEELMAN:
    Item: PRESUMPTION-432
    Strongest counterargument: In some fully-managed runtimes the platform DOES cap and reset scratch, so an agent author can be forgiven for treating disk as "someone else's problem." But "the platform caps it" is not "it is self-managing for my workload" — capping is precisely what produces the hard failure when the workload exceeds the cap without monitoring. The presumption survives only if a monitored quota + cleanup already exists; the incident shows it did not.
    What would need to be true for C2A2 to be safe: A monitored scratch quota with alerting and automatic cleanup exists, and agents fail loud on write errors.
    How to test: Fill scratch deliberately in a canary and confirm (a) an alert fires before exhaustion and (b) the agent emits an explicit disk-full error rather than halting silently.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-07-02
    Affected items: PRESUMPTION-432, PRESUMPTION-433, PRESUMPTION-434, PRESUMPTION-435 (this cohort); connects to ASSUMPTION-402 (silent hard-stop)
    Common vulnerability: ABSENCE-AS-EVIDENCE / SILENT-INFRASTRUCTURE-FAILURE. Each item treats the absence of a visible signal as reassurance: no disk alert => disk is fine (432); no second symptom traced => failure is isolated (433); no login error surfaced => session self-heals (434); no changelog => quiet day (435); logged-out => just stop quietly (402). The distributed-systems/SRE literature is unanimous that absence of a signal is NOT evidence of health, which is exactly why heartbeat / dead-man's-switch / reconciliation monitoring exists. This is a direct continuation of C2A2's standing liveness/observability cluster (PREMISE-086 monitor-of-monitor, PREMISE-006 transparent-flagging-over-silent-reconciliation; REVISE-147 scheduler dead-man's-switch; REVISE-157/158).
    Literature basis: Heartbeat / dead-man's-switch monitoring (incident.io, OneUptime, AlertOps); silent-failure taxonomy (abyrint; arXiv 2606.14589 silent failures in production LLM agent runtime); correlated-failure / shared-resource-exhaustion (AWS Builders' Library; Kubernetes disk-pressure eviction); data-observability drift/reconciliation (Databricks; DQLabs).
    Risk level: High
    Recommendation: Institute an active-liveness discipline for the autonomous stack: (a) monitor exhaustible resources (disk/session/registry) with threshold + heartbeat alerts; (b) treat any recurring infrastructure anomaly as a symptom to root-cause, not noise; (c) reconcile summaries against source-of-truth registries rather than inferring "nothing happened" from empty logs; (d) make every blocker/hard-stop escalate with context. These four disciplines neutralize the whole cohort and extend the existing dead-man's-switch family.

  Recommendation: CHALLENGED (Strong — ephemeral disk is bounded/exhaustible and must be monitored + GC'd; unbounded/self-managing is refuted)

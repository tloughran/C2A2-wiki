SEARCH-AGAINST-ASSUMPTION-429:
  Date searched: 2026-07-09
  Original item: ASSUMPTION-429
  Original statement: "Weekly re-trigger volume (~55/week) structurally exceeds one pipeline run's throughput — the queue grows monotonically absent a cadence/cap redesign."

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-429
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extraction (stated assumption, HIGH, QUEUED-EMPIRICAL, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Slimmon, D., 2022. "Using Little's Law to scale applications." (blog.danslimmon.com). — Little's Law framing: queue growth follows from λ > μ, but μ (service rate) is a provisioning variable, not a constant; capacity can be raised to meet forecast λ before redesigning admission.
    2. Google Cloud Dataflow documentation, "Horizontal Autoscaling" (docs.cloud.google.com/dataflow). — Standard backlog-drain math: additional workers needed = backlog / (per-worker throughput × recovery time); backlog growth under fixed worker count says nothing "structural" about the workload if workers can be added or runs parallelized.
    3. Judoscale / OneUptime worker-scaling practice literature ("Scaling Python Task Queues"; "How to Scale BullMQ Workers Horizontally," 2026). — Queue-depth-triggered scaling (e.g. KEDA) treats a growing backlog as an autoscaling signal, not a structural verdict; throughput scales roughly linearly with workers until a shared resource saturates.

  Strength of challenge: Moderate

  Summary: The arithmetic core of the claim (if arrival rate exceeds per-cycle throughput, the queue grows) is just Little's Law and is not challengeable. What the literature challenges is the word "structurally" and the implied remedy space. Throughput per week = (items per run) × (runs per week) × (parallelism), and all three factors are choices: capacity-planning practice treats a growing backlog as a signal to raise μ (more frequent runs, parallel item processing, batching similar items) at least as readily as to cut λ (cadence/cap redesign). The claim frames a provisioning shortfall as a structural law and thereby forecloses half the remedy space. It is also empirically contingent: "~55/week" and "one run's throughput" are both measurements that could reflect transient conditions (a backlog-inflated re-trigger count, an unusually slow run) rather than steady state. The monotone-growth conclusion holds only under the fixed-capacity premise.

  Specific risks: If C2A2 accepts "structural excess" uncritically, it may impose caps/cadence cuts that discard or delay genuinely needed re-triggers when a cheaper fix (run twice weekly; process items in parallel batches) would clear the load; conversely, if the ~55/week figure is transient, a redesign gets justified by a measurement artifact. Mis-modeling also corrupts downstream self-awareness items that cite this claim as established.

  Mitigations available: Measure steady-state λ (re-triggers/week over several weeks, excluding backlog-catchup inflation) and μ (items per run × feasible runs/week); test whether μ scales with parallelism before concluding structure; treat cap/cadence redesign and capacity increase as jointly available remedies; re-derive the conclusion after any throughput change.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-07-09
    Affected items: ASSUMPTION-428, ASSUMPTION-429, ASSUMPTION-430, PRESUMPTION-456, PRESUMPTION-459, PRESUMPTION-462
    Common vulnerability: Open-loop backlog governance — the pipeline combines (a) arrival rates that exceed service rates at two choke points (15d re-trigger queue, human proposal review), (b) fixed, load-insensitive cadences, (c) priority labels frozen at queue time, and (d) deferrals discharged by surfacing alone. Queueing theory (λ > μ ⇒ unbounded growth), scheduling theory (strict priority without aging ⇒ starvation), and safety science (surfaced-but-waived anomalies ⇒ normalization of deviance) jointly predict the observed symptoms: monotone queue growth, week-old reviews, and a 117-item deferred backlog. These are one control-loop deficiency expressed at six points, not six independent issues.
    Literature basis: Little's Law / queueing (Slimmon 2016, 2022); starvation and aging in priority scheduling (OS literature, e.g. Silberschatz et al., Operating System Concepts); normalization of deviance (Vaughan 1996; J. Safety Research 2022 systematic review); adaptive vs fixed polling (Juniper sFlow dynamic polling; adaptive-polling patent/practice literature).
    Risk level: High
    Recommendation: Close the loop once, centrally: instrument λ and μ at both choke points; add aging to all priority queues; make deferral escalation automatic after N repetitions; make cadences load-adaptive (re-trigger and review cadence keyed to queue depth). Fixing items individually without the shared feedback mechanism will reproduce the pattern elsewhere.

  STEELMAN:
    Strongest counterargument: For THIS system, capacity may genuinely not be a free variable: pipeline runs are gated by human attention (review of outputs), API budget, and the orchestrator's session cadence — so "one run per week" may be a hard constraint in practice, making the structural framing operationally correct even if not theoretically necessary. Naming the imbalance "structural" also usefully forces a design conversation instead of quiet hope that next week's run catches up, which the queue's actual growth history vindicates.
    What would need to be true for C2A2 to be safe: The stated remedy space must include capacity options, not only cadence/cap options; the ~55/week arrival estimate must be a steady-state measurement; any adopted cap must include aging/escape so capped items are not silently starved (links to ASSUMPTION-430).
    How to test: [QUEUED-EMPIRICAL — decisive test is in-house] Run the pipeline twice in one week, or double per-run batch size, and measure queue delta; three weeks of (arrivals, processed, queue depth) data distinguishes structural excess from provisioning shortfall.

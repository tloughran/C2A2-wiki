SEARCH-AGAINST-PRESUMPTION-344:
  Date searched: 2026-06-12
  Original item: PRESUMPTION-344
  Original statement: "Queue emptiness is pipeline health (the health indicator did not migrate with the constraint to the 57-item review stage)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-344
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Goldratt, E.M. (1990). Theory of Constraints. North River Press. — Foundational work establishing that system throughput is determined by the constraint (bottleneck); measuring performance at a non-constraint stage produces a local optimum that can mask or actively worsen global performance. A stage reporting "empty queue" when the downstream constraint is backlogged is not healthy — it is contributing to starvation of the constraint.
    2. Theory of Constraints Institute. "Theory of Constraints: Finding and Exploiting the Bottleneck." (tocinstitute.org) — Documents the common failure mode where a department optimises its own metrics without considering the system: "each resource appears to be performing well, but the whole is not moving any faster." The empty-queue illusion is a textbook example of this failure.
    3. Duperrin, B. (2025). "The Theory of Constraints and Knowledge Work Principles." (duperrin.com) — Applies TOC explicitly to knowledge work pipelines; notes that in knowledge work contexts, a non-bottleneck stage appearing to perform well while a downstream stage accumulates work is the characteristic signature of a measurement system that has not moved with the constraint.
    4. Lean Six Sigma Metrics literature (e.g., Quality America, Lean Sigma Corporation). "Getting Your Primary Metric Right." — Standard Lean/Six Sigma teaching: the primary metric must be placed at the system output or at the constraint; metrics placed upstream of the constraint reward local efficiency that generates no customer value and may actively harm throughput by creating unprocessed inventory (work-in-progress) at the bottleneck.
    5. DevOps Flow literature. "Optimizing DevOps Value Streams with the Theory of Constraints." (devopsflow.net) — Shows that in software delivery pipelines, a stage emptying its queue by pushing work faster to a downstream bottleneck worsens the system's performance even as the stage's local metric improves; end-to-end lead time increases.
    6. Goldratt, E.M. (1994). It's Not Luck. North River Press. — Extends the measurement placement argument: once a bottleneck is identified and exploited, the constraint migrates; measurement systems that do not migrate with the constraint continue to report the old bottleneck as healthy, creating a false sense of security that delays recognition of the new bottleneck.

  Strength of challenge: Strong

  Summary: The identification of queue emptiness at one pipeline stage as a health indicator is a classic Theory of Constraints measurement error: it measures a non-constraint stage and ignores whether the constraint (the 57-item review stage) is flowing. TOC explicitly predicts this failure mode: when measurement does not follow the constraint, the system reports local optimality while the global flow is degraded. The C2A2 case is a textbook instance — the constraint migrated from the disposition queue to the review stage, but the health metric remained anchored to the original queue. The result is that the pipeline can report "healthy" while 57 items accumulate unreviewed, which is the operational definition of an unhealthy pipeline from a throughput perspective.

  Specific risks: The system's self-reported health will be systematically misleading whenever the constraint has migrated to a stage not currently monitored. This will delay recognition of new bottlenecks, allow work-in-progress to accumulate invisibly at constraint stages, and produce a false confidence that the pipeline is functioning well. Strategic decisions about pipeline capacity and prioritisation will be made on the basis of a metric that does not track actual throughput.

  Mitigations available: Apply the TOC "five focusing steps" to identify the current constraint stage and anchor the primary health metric there; measure end-to-end cycle time (item creation to final disposition) rather than stage-local queue depth; implement WIP (work-in-progress) limits at each stage so that upstream stages cannot empty their queues by flooding the downstream constraint; review metric placement whenever a constraint migration is detected.

  STEELMAN:
    Strongest counterargument: Queue emptiness at the original disposition stage is not entirely uninformative — it does confirm that one part of the pipeline is not the bottleneck, which has diagnostic value in identifying where the constraint has moved. If used as a diagnostic rather than as a health indicator, it contributes to system understanding. The problem is not the metric itself but its misinterpretation as a sufficient health signal rather than one data point among several.
    What would need to be true for C2A2 to be safe: The pipeline would need a multi-stage throughput metric — end-to-end cycle time or a cumulative flow diagram — that makes constraint location visible, not just individual stage queue depths. The health dashboard would need to flag when any stage has accumulated more than a threshold WIP.
    How to test: Plot WIP at each pipeline stage over time as a cumulative flow diagram; a widening band at any stage identifies an accumulating constraint. Compare end-to-end cycle time during "healthy" (empty queue) periods against periods where stage queues were non-zero; if cycle time is not materially different, the queue metric is uninformative; if cycle time is worse, the metric is actively misleading.

  Search scope: Searched Theory of Constraints literature (Goldratt), Lean/Six Sigma metric placement guidance, DevOps value stream management, and knowledge work pipeline optimisation. Comprehensive for primary challenge directions. The specific C2A2 manifestation (57-item review stage as migrated constraint) is a direct application of well-established TOC principles.

  Recommendation: CHALLENGED

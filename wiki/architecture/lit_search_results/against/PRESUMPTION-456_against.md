SEARCH-AGAINST-PRESUMPTION-456:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-456
  Original statement: "Human review capacity is elastic — proposal intake needs no backpressure, queue cap, or aging policy (pending 4→13 in two days; last review a week old)."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-456
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, HIGH, from 2026-07-07 EOD cohort)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Slimmon, D., 2016. "The most important thing to understand about queues." (blog.danslimmon.com; standard queueing-theory exposition). — At sustained utilization ≥100% queue length grows without bound, and wait times explode well before that (nonlinear degradation from ~80% utilization). A single human reviewer with rising intake and no backpressure is exactly this system.
    2. Propel Code, 2025. "The Impact of PR Size on Code Review Quality: What Data Tells Us." (propelcode.ai). — Empirical code-review data: defect detection falls from ~87% on small reviews to ~28% on 1000+-line reviews; reviewer cognitive overload produces rushed approvals. Queue pressure converts careful review into sampling.
    3. Sadowski, C., Söderberg, E., Church, L., Sipko, M., Bacchelli, A., 2018. "Modern Code Review: A Case Study at Google." ICSE-SEIP. — Documents that review latency and quality are managed at Google by aggressively bounding reviewer load and change size; review only works as a quality gate when load is controlled.
    4. Kanban/queue-management literature (e.g., kanbantool.com, "Queuing Theory & Kanban"; agility-at-scale.com, "Managing Queues"). — WIP limits and explicit backpressure exist precisely because human service capacity is NOT elastic; unbounded intake queues hide overload until lead times and quality have already collapsed.

  Strength of challenge: Strong

  Summary: Queueing theory gives a direct structural refutation: if arrival rate exceeds a human reviewer's sustainable service rate, the pending queue grows without bound and item wait time diverges — and the observed data (4→13 pending in two days, last review a week old) is the textbook signature of λ > μ, not of a temporarily busy reviewer. The empirical review literature adds a quality dimension: when reviewers do face a swollen queue, they do not merely review later, they review worse — batching, skimming, and rubber-stamping — so the queue converts a latency problem into a silent quality problem. Human attention is among the least elastic resources in any pipeline; systems that assume otherwise accumulate exactly this pathology.

  Specific risks: Proposals rot while pending (their premises go stale — interacting with PRESUMPTION-459's stale-priority problem); the reviewer eventually bulk-processes the queue with degraded scrutiny, so the highest-consequence human gate in C2A2 becomes its weakest check; or the reviewer disengages entirely and the pipeline keeps generating proposals into a void, wasting agent capacity and creating a false sense that governance is operating.

  Mitigations available: Queue cap with backpressure (pipeline stops emitting new proposals, or merges/downgrades them, when pending > N); aging policy (proposals auto-expire or auto-downgrade after N days with a surfaced expiry list); batch-and-rank presentation so the reviewer spends fixed effort on a prioritized digest instead of per-item review; measure and surface reviewer throughput so intake can be matched to it.

  Recommendation: CHALLENGED

  STEELMAN:
    Strongest counterargument: Proposal review is not continuous-flow service; it is naturally bursty batch work, and a single owner can legitimately let a week's proposals pool and clear them in one focused session — 13 pending items is one sitting, not a crisis. Backpressure machinery has real costs: expiring proposals throws away completed analysis, and caps could suppress exactly the rare high-value proposal. For a single-user system, the "queue" is better modeled as an inbox than a service queue.
    What would need to be true for C2A2 to be safe: The reviewer's batch-clearing rate must genuinely exceed weekly intake (queue returns to ~0 periodically); proposal value must not decay materially over the pooling interval; bulk-session review quality must be comparable to per-item review quality.
    How to test: Track the pending count over 4-6 weeks: if it saw-tooths to zero, the inbox model holds and the presumption survives; if the minima trend upward (never returns to zero), λ > μ is established and backpressure is required. Also spot-check decisions made in bulk sessions against a slower re-review of the same items.

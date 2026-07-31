SEARCH-FOR-PRESUMPTION-553:
  Date searched: 2026-07-27
  Original item: PRESUMPTION-553
  Original statement: [inferred] The 15d re-trigger machinery presumes re-triggering keeps items live for a downstream consumer, but consumption has been zero for 18 days and the ~174-item backlog grew for a 10th run; adding 17 re-triggers + advancing 88 carry-overs feeds a queue with an observed drain rate of zero.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-553
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a re-trigger loop feeding a queue with zero consumption for 18 days
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Little, J.D.C. (1961), "A Proof for the Queuing Formula L = lambda W," Operations Research 9(3):383-387; Kendall (1953) queue classification. — Little's Law ties queue length to arrival rate x wait time. With service (drain) rate mu = 0 and arrival lambda > 0, utilization rho = lambda/mu is unbounded; the system is unstable and queue length -> infinity. A queue whose server never runs does not "keep items live"; it accumulates without bound. Directly on point for an 18-day zero-drain interval with continued arrivals.
    2. Anderson, D.J. (2010), Kanban: Successful Evolutionary Change; Reinertsen (2009), Principles of Product Development Flow. — WIP (work-in-progress) limits exist precisely because unbounded queues degrade lead time and hide problems; the prescribed control is to cap arrivals to sustainable throughput, not to keep re-queuing. Supports the presumption's implication that re-triggering without a matched consumer is a control failure.
    3. Goldratt (1984), Theory of Constraints; distributed-systems backpressure literature (e.g., Little's-law-based flow control, Kingman's formula for congestion). — Inventory that is not processed is not throughput; a stage feeding a downstream stage that never consumes creates starvation/backpressure and, absent a bound, monotonic growth. The re-trigger loop firing "correctly" while consumption is nil is the textbook decoupled-producer/absent-consumer failure.

  Strength of support: Strong

  Summary: Strongly supported by elementary queueing theory: a queue with a positive arrival rate and a zero service rate grows without bound and is by definition unstable, so re-triggering into it does not "keep items live" — it produces an aging, monotonically growing backlog, exactly as observed (110 -> 147 -> ~174 over successive runs; zero consumption since 2026-07-08). WIP-limit and Theory-of-Constraints practice both prescribe capping arrivals to throughput or adding a consumer, not continued enqueue. This item is the formal statement of the standing BACKLOG-FLAG and reinforces REVISE-245 (stalled actuation).

  Caveats: The queueing verdict presumes the re-trigger blocks are work-in-progress awaiting service. If some are better modeled as an append-only audit log or deliberately-deferred low-priority monitors (see 15b), the "unbounded growth = harm" claim is conditioned by the read/context cost the backlog imposes (that cost is itself ASSUMPTION-542 / PRESUMPTION-498, in-house). The remedy (assign a consumer or bound the queue) is a design decision already pending Tom per the BACKLOG-FLAG escalation.

  Recommendation: SUPPORTED

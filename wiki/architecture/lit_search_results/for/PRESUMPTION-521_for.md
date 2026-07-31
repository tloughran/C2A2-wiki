SEARCH-FOR-PRESUMPTION-521:
  Date searched: 2026-07-22
  Original item: PRESUMPTION-521
  Original statement: [inferred] Clearing the ingestion stall is presumed to be progress, but review service is ~0/day; unblocking production while judgment stays blocked presumes the bottleneck was production. Deepens the PRESUMPTION-510 imbalance.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-521
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by reading the ingestion-clearance headline against the flat review-service rate
      15a: Searched for supporting literature on Little's Law, WIP limits, back-pressure, unbalanced pipelines
    Current status: SUPPORTED

  Sources:
    1. Little's Law (L = lambda x W) as applied to queue management (LiveSession; businessmap.io; 6sigma.us). — With arrival lambda ~4/day and service ~0/day at the review stage, WIP and wait time grow without bound; formalizes "production at full rate while review is blocked lowers the value of the record."
    2. Kanban / queuing-theory WIP-limit literature (Kanban Tool; Kanban Zone). — Bottlenecks form at the slowest/most variable stage; processing WIP near full capacity drastically increases waiting times; WIP limits level the system so arrivals match departures.
    3. Back-pressure (TCP / bounded-queue) pattern (rponte gist; general distributed-systems practice). — The correct response to a slow downstream consumer is to apply back-pressure upstream, not to accelerate production; unbounded upstream production against a stalled consumer is a known anti-pattern.

  Strength of support: Strong

  Summary: Classic, well-established operations and queueing theory directly supports the presumption. When a downstream human-limited stage has near-zero service rate, accelerating the upstream stage does not constitute progress; it inflates work-in-progress and latency and, in this case, lowers the value of the produced record. The literature also supplies the remedy the presumption implies: admission control / WIP limits / back-pressure keyed to the binding (review) stage. This corroborates the already-validated PREMISE-119 (from PRESUMPTION-510) that production and judgment are not independently schedulable.

  Caveats: Little's Law assumes a stable system; a truly zero service rate is a degenerate case where the "law" simply says the queue diverges. The presumption is strengthened, not weakened, by this.

  Recommendation: SUPPORTED

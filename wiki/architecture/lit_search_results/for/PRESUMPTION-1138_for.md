SEARCH-FOR-PRESUMPTION-1138:
  Date searched: 2026-10-14
  Original item: PRESUMPTION-1138
  Original statement: [inferred] Carding presumes added proposals have value regardless of review throughput. No review decision since 10-09; pending rose to 13 (6 dated 10-13). Agents keep producing; nothing limits work in progress. Question tested: what do WIP limits and queueing results (Little's law; Kanban) predict for a single-reviewer queue whose arrival rate exceeds its decision rate?

  DIRECTION NOTE (read first): The evidence found does NOT support the presumption that unlimited intake is harmless or that added proposals hold value regardless of review throughput. It supports the CONCERN. "SUPPORTED" below means the presumption is confirmed as operative and risky, as predicted by queueing theory.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1138
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cited evidence across 2026-10-13 transcripts and wiki files.
      15a: Searched for supporting literature
    Current status: SUPPORTED (concern supported; presumption that unlimited intake is harmless is NOT supported)

  Supporting evidence found: Yes (for the concern)

  Sources:
    1. Little JDC, 1961. "A Proof for the Queuing Formula: L = λW." Operations Research 9(3). [Access level: not fetched; cited via Kanban University "Exploring Little's Law" (2022) and practitioner summaries at snippet level. Standard result.] WIP = throughput × lead time, valid only for a stable system where arrivals and departures balance and average item age is not trending. When arrival rate λ exceeds service rate μ, the system is unstable: the queue and the waiting time of new arrivals grow without bound, and no steady-state lead time exists. The "λ > μ implies unbounded queue" conclusion is standard queueing theory (M/M/1 stability condition ρ < 1). It was stated here from general knowledge, not from a fetched source.
    2. Reinertsen DG, 2009. The Principles of Product Development Flow: Second Generation Lean Product Development. Celeritas. [Access level: secondary reviews (ardalis.com, Softhouse, Swarmia, SAFe, LibraryThing) only.] Queues in knowledge work are invisible inventory made of information. Queue size multiplies cost of delay. Running near full utilization is "an economic disaster," because queue length grows nonlinearly as utilization approaches 100%. Manage queue size, a leading indicator, rather than cycle time, a lagging one. This applies directly to a proposal inbox whose single reviewer is at or above 100% utilization.
    3. Hopp WJ, Spearman ML, Factory Physics (1996; later eds.); Spearman ML, Zazanis MA, 1992 on push vs. pull. [Access level: secondary/course-material snippets.] Above critical WIP, throughput is capped at the bottleneck rate and each added job only adds cycle time. Pull systems with a WIP cap (CONWIP, Kanban) control WIP and observe throughput. They release no new work when no card is free, so excess demand waits outside the system in an explicitly visible backlog. The prediction: adding proposals beyond the reviewer's rate adds no throughput and only adds delay.
    4. Kanban practice literature (Kanban University 2022; SAFe). [Access level: snippet.] With throughput fixed at a bottleneck, adding WIP directly increases lead time. WIP limits are the standard intervention.
    5. Counterpoint noted for completeness (2023 lab-scale Kanban/ConWIP study, Springer chapter 10.1007/978-3-031-43670-3_45; authors not verified). [Access level: snippet.] WIP regulation shortens time-in-system but can lower throughput. WIP limits are not free, but the study does not suggest unlimited WIP is harmless.

  Strength of support: Strong (theoretical; foundational queueing results). Weak for direct empirical evidence on single-reviewer proposal queues.

  Summary: Queueing theory gives an unambiguous prediction. A single-server queue whose arrival rate exceeds its service rate is unstable. The backlog and the expected wait for each new proposal grow without bound, and adding items adds zero throughput. Little's law and the Factory Physics laws say that, above the bottleneck's capacity, more WIP only lengthens lead time. Reinertsen adds that each queued item accrues cost of delay and that information queues are invisible by default. Proposals also go stale: the context they respond to moves on. So the presumption that added proposals have value regardless of review throughput contradicts these results. Each marginal proposal beyond the decision rate is expected to have decaying or negative value through delay cost, staleness and reviewer load. A WIP limit or intake gate (pull system) is the standard remedy. It moves excess demand into an explicit, prioritizable backlog, or stops it at source, instead of letting it accumulate in the review queue.

  Caveats: (a) Little's law needs steady state, and C2A2's queue with zero decisions since 10-09 is clearly not steady, which is itself the warning sign. (b) Proposals are not interchangeable manufacturing jobs. Some may be batch-reviewable, may merge or obsolete one another, or may have value as an archive even if never decided. These moderate but do not remove the delay-cost argument. (c) Reinertsen's analysis leans on M/M/1 assumptions (per one review). (d) No direct empirical study of single-reviewer editorial or proposal inboxes was searched. Code-review backlog literature could supply one; broader search recommended. (e) Most sources were read at secondary or snippet level.

  Search scope: 3 web searches (Little's law/WIP/Kanban; Reinertsen queues; Factory Physics CONWIP), 0 page fetches. Comprehensive for theory; preliminary for empirical knowledge-work queues.

  Recommendation: SUPPORTED (as a risk; the presumption that unlimited intake is harmless is contradicted)

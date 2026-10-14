SEARCH-AGAINST-PRESUMPTION-1138:
  Date searched: 2026-10-14
  Original item: PRESUMPTION-1138
  Original statement: [inferred] Carding presumes added proposals have value regardless of review throughput. No review decision since 10-09; pending rose to 13 (6 dated 10-13). Agents keep producing; nothing limits work in progress. Question under test: what do WIP-limit and queueing results predict for a single-reviewer queue whose arrival rate exceeds decision rate?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1138
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cited evidence across 2026-10-13 transcripts and wiki files.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Sjøberg D, 2018. "An empirical study of WIP in kanban teams." Proc. 12th ACM/IEEE ESEM, Oulu, pp. 13.1-13.8. — 8,000+ work items, five teams, four years. Lower WIP correlated with shorter lead time, BUT higher WIP also correlated with HIGHER productivity, contrary to Kanban claims; no published real-case evidence identifies an optimal WIP limit. Direct challenge to the inference that limiting WIP is beneficial on net. [Level: full abstract read via fetch.]
    2. University of Oslo master's thesis, 2014 (duo.uio.no/handle/10852/42080; author not verified). — Weak WIP-lead time correlation (~0.2) in one company; notes "little evidence proving the impact of WIP-limit for software development." [Level: snippet.]
    3. Little JDC, 1961, "A proof for the queuing formula L = λW," Operations Research; MIT 1.041 lecture notes (2023-2026) on queueing stability. — L=λW requires stationarity over an infinite horizon (not over finite windows); a queue with λ > μ has no steady state. Boundary condition: Little's law cannot be used to "predict" waiting times for this queue; it only applies once arrivals are throttled or capacity is raised. Also, finite-capacity queues are always stable. [Level: snippet of lecture notes; original paper not read.]
    4. (Supports concern) Code-review queue studies: "On Wasted Contributions: Understanding the Dynamics of Contributor-Abandoned Pull Requests," arXiv:2110.15447 (2021; authors not verified in this run); arXiv:2203.05048 (MSR 2022) on waiting times; modern code review SLR arXiv:2103.08777. — Response latency lowers acceptance probability; long reviews raise abandonment; shorter review queues give faster review. [Level: snippet.]

  Strength of challenge: Moderate (against the WIP-limit remedy) / Weak (against the backlog concern itself)

  Summary: Queueing theory does not straightforwardly "predict" outcomes here: Little's law needs a steady state, and an arrival rate persistently above decision rate means there is none — the backlog simply grows, which is arithmetic rather than a theory-derived harm. Whether growth is harmful depends on whether queued items decay; the review-latency literature suggests they do (lower acceptance, more abandonment), but that evidence is from human-contributor PRs, where the contributor walks away — C2A2's agent-produced proposals do not abandon, so the decay mechanism may not transfer. The empirical case for WIP limits in knowledge work is thin: the one real-data quantitative study found WIP limits shorten lead time but correlate with lower productivity, so limiting agent output may reduce total accepted proposals. Boundary conditions favouring the challenge: if the reviewer works in batches (a server with "vacations"), a 13-item queue observed during a 5-day pause says little about long-run stability; stability needs only average decision capacity per batch > average arrivals.

  Specific risks: Imposing a hard WIP cap on carding could suppress good proposals and reduce throughput (Sjøberg's productivity correlation) when the real constraint is reviewer availability episodes. Conversely, if the reviewer's average capacity is genuinely below arrival rate, no batch catch-up occurs and stale proposals reference superseded wiki states (decay via context drift rather than abandonment).

  Mitigations available: Measure long-run arrival vs decision rate (weeks, not days) before capping; priority ordering / expiry dates on proposals instead of a hard WIP cap; batch-review sessions sized to clear the queue; mark proposals that depend on wiki state for re-validation if aged.

  Recommendation: PARTIALLY-CHALLENGED

  Search scope: preliminary search — 3 web searches, 1 page fetch (SINTEF abstract page, succeeded). Broader search recommended on server-vacation/batch queues and on staleness of knowledge-base change proposals.

STEELMAN:
  Item: PRESUMPTION-1138
  Strongest counterargument: Thirteen pending proposals after a five-day pause is not evidence of an unstable queue; it is what any batch-reviewed system looks like between batches. Little's law and Kanban WIP arguments assume a stationary flow system and a team whose context-switching cost rises with WIP — neither holds for agents that produce asynchronously and a single reviewer who processes in sittings. The only real-data study of WIP limits found that lower WIP correlated with lower productivity, so capping agent output risks cutting the supply of good proposals to solve a "problem" that one review session would clear. Proposals that do not decay cost little to hold.
  What would need to be true for C2A2 to be safe: Over a multi-week window the reviewer's mean decisions per week exceed mean proposals per week; proposals remain valid as the wiki changes (or are revalidated before decision); queue size remains visible to the reviewer.
  How to test: From inbox/proposals history, compute weekly arrivals vs decisions over the last 6-8 weeks and the age distribution of pending items; check whether older proposals are accepted at a lower rate or need rework (decay). If decisions/week >= arrivals/week on average and no age-acceptance gradient appears, the WIP concern is not supported for this queue.

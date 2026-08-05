SEARCH-AGAINST-PRESUMPTION-656:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-656
  Original statement: That correct local behaviour aggregates to correct system
    behaviour — whereas honest escalation is, by the agent's own diagnosis, the very
    mechanism starving the review queue.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-656
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 diagnosis that honest escalation was starving
        the review queue
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Bronson, N., Aghayev, A., Charapko, A. & Zhu, T., 2021. "Metastable Failures in
       Distributed Systems." HotOS '21, ACM. doi:10.1145/3458336.3465286. — The canonical
       statement of the counter-position: systems composed of locally-correct components
       enter self-sustaining congestive collapse in response to a transient stressor and
       fail to recover after the stressor is removed. Named triggers include retries and
       emergent properties of load-balancing — i.e. behaviours that are individually
       correct and locally rational.
    2. Isaacs, R. & Alvaro, P., 2025. "Analyzing Metastable Failures." HotOS '25. —
       Follow-up work confirming that the sustaining effect, not the trigger, is the
       object of interest, and that identifying it requires system-level rather than
       component-level analysis.
    3. Operating-systems literature on starvation and aging (standard treatments, e.g.
       LibreTexts "Concurrency: Deadlock and Starvation," §Starvation; GeeksforGeeks
       "Starvation and Aging in Operating Systems"). — Establishes that priority-ordered
       queues without an aging term admit indefinite postponement of low-priority
       entries as a structural property, not as a bug in any participant. Aging is the
       standard corrective precisely because local correctness does not supply it.
    4. (2020). "Fluid Limits for Shortest Job First with Aging." arXiv:2011.07758. —
       Formal analysis of aging policies, showing the queue-level behaviour depends on
       the aging term and not on the correctness of individual arrivals or services.
    5. (2026). "Fairness-Aware and Latency-Controllable Scheduling for Chunked-Prefill
       LLM Serving." arXiv:2606.09061. — Contemporary evidence that in agent/LLM serving
       queues, locally optimal scheduling produces unbounded tail latency for some
       classes without an explicit fairness or aging mechanism.
    6. Gunawi, H.S. et al., 2018. "Fail-Slow at Scale: Evidence of Hardware Performance
       Faults in Large Production Systems." FAST '18, USENIX. — Related mechanism: a
       component behaving correctly but slowly degrades the whole cluster; correctness
       at the component level is not the relevant property.

  Strength of challenge: Strong

  Summary: This presumption is the one the distributed-systems literature has most
    directly and repeatedly falsified. Metastable failure is defined by the property that
    every component is behaving correctly and the system is nonetheless stuck in a bad
    state that persists after the trigger is gone — retries, caching and load balancing
    are all locally correct behaviours that supply the sustaining effect. The scheduling
    literature gives the specific form relevant here: a queue ordered by any priority
    criterion, with entries that do not retire, admits indefinite starvation as a
    structural consequence, and the standard fix (aging) is a global mechanism that no
    locally-correct participant can supply. Notably, the agent's own diagnosis is already
    the correct systemic reading; the literature's contribution is to say this is the
    expected behaviour of such an arrangement rather than an anomaly, and that the
    corrective must be inserted at the queue level.

  Specific risks: If local correctness does not aggregate, then instructing each agent to
    behave better cannot fix the queue, and every round of "escalate honestly" guidance
    makes the starvation worse while feeling like the responsible action. Concretely: a
    staleness-ordered queue whose entries never retire and which receives honest
    escalations faster than it drains will grow monotonically, the oldest entries will
    never be reached, and the queue's staleness statistic will degrade in a way that looks
    like a throughput problem rather than a structural one. The dangerous property is the
    metastable one — once the queue is in the starved state, reducing the escalation rate
    back to normal will not recover it, because the backlog itself sustains the condition.
    C2A2 would then require an explicit intervention it has no trigger for, since no
    individual agent is misbehaving and therefore no local guard fires.

  Mitigations available: (1) Add an aging term: bound the maximum time any queue entry can
    wait, and promote past that bound regardless of priority. This is the textbook
    corrective and is cheap to implement in a file-backed queue. (2) Make entries retire —
    every queue item needs a terminal state (resolved, superseded, expired) and a rule that
    reaches it; non-retiring entries are the structural cause. (3) Instrument the queue at
    the system level: track arrival rate, drain rate, queue depth, and age of the oldest
    entry. Depth and oldest-age are the two numbers that reveal metastability and neither is
    visible from inside any agent. (4) Add admission control or backpressure: if drain rate
    is below arrival rate, escalation should become harder, not easier — this is the
    counterintuitive move that local honesty cannot produce. (5) Define a recovery
    procedure in advance, since metastable states do not self-clear: e.g. a periodic bulk
    triage that expires or batches the tail.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-656
    Strongest counterargument: Local correctness is the only property that is actually
      controllable, and systems built from components that each behave correctly are
      overwhelmingly more reliable than systems built from components that do not — the
      metastable-failure literature describes rare black-swan events at hyperscale, not
      the ordinary operating regime, and it explicitly notes such failures are outliers.
      Discouraging honest escalation because it loads the queue is a cure far worse than
      the disease: it converts an observable throughput problem into an invisible
      suppression problem, and the queue depth at least tells the truth about how much
      work exists. The correct reading may simply be that the queue is under-resourced,
      which is a capacity fact, not a systemic-emergence fact.
    What would need to be true for C2A2 to be safe: (a) Drain rate exceeds arrival rate
      over any sustained window, so the queue is genuinely transient. (b) Queue entries
      retire by some mechanism, so depth is bounded. (c) The ordering criterion, whatever
      it is, cannot indefinitely postpone any entry — i.e. some aging term already exists.
      (d) Someone is watching queue depth and oldest-entry age as system-level signals,
      not just per-item correctness.
    How to test: Directly measurable in-house. Plot review-queue depth and the age of the
      oldest unretired entry over the last 60 days. Monotonic growth in either falsifies
      the presumption without any appeal to literature. Second: count how many entries
      have ever reached a terminal state versus how many were created; a ratio far below
      one confirms the non-retiring-entry diagnosis.

  Search scope: Adequate. Concepts searched: metastable failures in distributed systems;
    local optimum / global failure; starvation, priority inversion and aging in queues;
    fairness-aware scheduling and tail latency; fail-slow degradation of clusters.

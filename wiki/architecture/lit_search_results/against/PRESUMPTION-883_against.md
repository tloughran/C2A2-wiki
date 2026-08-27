SEARCH-AGAINST-PRESUMPTION-883:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-883
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-883 (Priority High)
  Original statement: [inferred] That proposal production and proposal disposition are independent
    subsystems — that intake rate owes nothing to a stalled gate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-883
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from absent alternatives, sharpened by a +14 day (pending 60 → 74, zero out) into
           a gate silent seventeen days. Cross-checked against PRESUMPTION-875 for non-duplication:
           875 concerns the queue's shape, this concerns the producers' coupling to it. High
           confidence in the absence; the remedy framing is 14b's.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Three WebSearch queries executed 2026-08-26 (one on Little's law stability, one on
    admission control/backpressure, one on human review backlogs under AI-accelerated production).
    Literatures reached: (a) queueing theory — Little's law and its stability precondition;
    (b) distributed-systems flow control — backpressure, admission control, load shedding, CoDel;
    (c) empirical software engineering and industry telemetry on code-review queues under
    AI-accelerated production; (d) practitioner Kanban/WIP-limit guidance. Venues reached: the Little
    & Graves chapter (UCSD course handout of the canonical text), Wikipedia for the stability
    condition, arXiv (math.PR — measurement-based admission control for overloaded networks),
    arXiv (cs.SE — agentic coding PR studies), plus a substantial amount of practitioner material.
    NOT COVERED, and this is the material limitation: (i) the peer-reviewed **CONWIP / WIP-limit**
    literature in operations management, which is where the causal evidence for coupling intake to
    disposition actually lives — my query drifted into practitioner Kanban blogs; (ii) Goldratt's
    Theory of Constraints in primary form; (iii) the **queueing-with-vacations** literature, which is
    the exact formal model for "a server that is intermittently and unpredictably absent" and which
    the queue entry explicitly asked for by name; (iv) any peer-reviewed replication of the Faros AI
    telemetry figures cited below. Search confidence: HIGH on the theory, MODERATE on the empirical
    transfer, LOW on the specific remedy design.

  Challenging evidence found: Yes

  Sources:
    1. John D. C. Little & Stephen C. Graves. "Little's Law," Chapter 5 [in *Building Intuition:
       Insights from Basic Operations Management Models and Principles*].
       https://web.eng.ucsd.edu/~massimo/ECE158A/Handouts_files/Little.pdf — The canonical statement.
       Little's law requires the system to reach steady state: over the long run arrivals and
       departures must balance. Authorship confirmed from the document title line surfaced by search;
       volume and year unverified. FULL-TEXT PDF available at this link; I read the search-surfaced
       statement of the stability requirement, not the chapter.
    2. https://en.wikipedia.org/wiki/Little's_law and
       https://www.mirabilisdesign.com/queueing-theory-littles-law/ — The direct refutation of the
       presumption, and it is not subtle: "if the arrival rate exceeds the service rate, the queue
       grows without bound with L = ∞ and W = ∞; the law still holds, but it tells you the system is
       broken, not that it is well-behaved." And: "an arrival rate exceeding an exit rate would
       represent an unstable system, where the number of waiting customers would gradually increase
       towards infinity." C2A2's observed condition is λ = 14/day, μ = 0/day for seventeen days.
       Under those values production and disposition are not independent subsystems; they are the two
       terms of a single stability inequality that is currently violated by an infinite margin.
       SNIPPET-ONLY (tertiary sources; the underlying result is textbook and uncontroversial).
    3. [authors unverified]. 2007. "Stabilization of an overloaded queueing network using
       measurement-based admission control." arXiv:0708.2739. https://arxiv.org/pdf/0708.2739 — The
       formal counter-position: an overloaded network is stabilised *by admission control*, i.e. by
       coupling intake to observed service capacity. The presumption's claim of independence is
       precisely what this literature exists to deny. ABSTRACT-ONLY (title and framing surfaced by
       search).
    4. [no author — practitioner, Design Gurus]. "How Systems Collapse Under Load: Backpressure and
       Queue Growth Explained." https://designgurus.substack.com/p/system-design-deep-dive-backpressure
       — States the mechanism in the form that matches C2A2 exactly: "the root cause of system failure
       is almost always a mismatch between how fast work arrives and how fast it can be processed,
       **combined with a system that has no way to say it cannot keep up**. Work piles into a queue,
       the queue grows without bound, and the growth itself becomes the mechanism of collapse."
       The bolded clause is 14b's finding restated: "nothing in either agent's definition gives it
       read access to the other's rate, so the coupling could not be expressed even if someone wanted
       it." Practitioner source; the content is standard distributed-systems doctrine. SNIPPET-ONLY.
    5. [no author — practitioner]. Backpressure pattern references, e.g.
       https://codelit.io/blog/backpressure-flow-control and
       https://layrs.me/course/hld/08-asynchronous-processing/back-pressure/ — "Backpressure is the
       ability of a system to signal that it is overwhelmed and to slow down the flow of incoming work
       rather than silently accumulating it" and allows overload to be handled "as a controlled,
       visible condition instead of a slow slide into failure." Also: "unbounded queues defer the
       problem and grow until the system runs out of memory." SNIPPET-ONLY.
    6. Faros AI 2025 developer telemetry, as reported at
       https://yuvalyeret.com/blog/ai-coding-made-code-review-the-bottleneck/ — The closest empirical
       analogue found, and it is a strong one. Telemetry over 10,000+ developers across 1,255 teams:
       teams with high AI adoption "completed 21% more tasks and merged 98% more pull requests, but PR
       review time increased by 91%, average PR size grew by 154%, and bug counts rose by 9%."
       Generalisation: when producers accelerate and the human review stage does not, the gains are
       absorbed by the queue and defect rates rise. **Important caveat: this is an industry telemetry
       report reached through a secondary practitioner source; I did not read the primary report and
       cannot verify the figures.** SNIPPET-ONLY, secondary. Treated as suggestive, not evidentiary.
    7. [authors unverified]. 2025. "On the Use of Agentic Coding: An Empirical Study of Pull Requests
       on GitHub." arXiv:2509.14745. https://arxiv.org/html/2509.14745v3 — Peer-reviewable evidence
       adjacent to the same phenomenon (agent-produced work arriving at human review). Surfaced but
       not read; listed so the limb is traceable rather than claimed. SNIPPET-ONLY.
    8. [no author — practitioner]. WIP-limit guidance, e.g.
       https://gitscrum.com/en/solutions/pains/reducing-code-review-bottleneck-delays and the
       formulation "WIP limits are the valve that keeps agentic throughput from piling up in front of
       the humans who still have to review it ... when it's full, no more work can enter until reviews
       complete, creating natural backpressure." This is the exact remedy the presumption forecloses.
       SNIPPET-ONLY; practitioner.

  Strength of challenge: Strong

  Summary: This is the item where the literature is least equivocal, because the presumption asserts an
  independence that queueing theory defines as impossible. Little's law's stability precondition is
  that arrivals and departures balance over the long run; when λ exceeds μ the queue length and wait
  both diverge, and — in the formulation that most directly answers the presumption — "the law still
  holds, but it tells you the system is broken." C2A2 has run at λ ≈ 14/day against μ = 0 for
  seventeen days. Production and disposition are not two subsystems that happen to be uncoupled; they
  are the two terms of one inequality, and the system is currently on the wrong side of it by an
  unbounded margin. The distributed-systems literature converges from the applied side and names the
  missing component precisely: what makes overload turn into collapse is not the arrival rate itself
  but "a system that has no way to say it cannot keep up," which is a description of C2A2's structural
  situation — no agent has read access to the gate's state, so backpressure is not merely unexercised,
  it is inexpressible. Admission control and WIP limits exist as named disciplines for exactly this
  problem, and the stabilisation result for overloaded networks is achieved *by* coupling intake to
  measured capacity. The one empirical analogue found — AI-accelerated production against a human
  review stage — points the same way, with review time up 91% and defect counts up 9% where merge rate
  nearly doubled, though I reached that figure only through a secondary source and weight it lightly.
  Rated Strong rather than Very Strong solely because the peer-reviewed operations-management evidence
  for the *remedy* (CONWIP, WIP limits, queueing with vacations) was not reached; the evidence against
  the *presumption* is as settled as anything in this batch.

  Specific risks: (a) Unbounded growth with no natural ceiling — at the current rates the pending count
  has no equilibrium and will grow until some resource other than intent stops it. (b) Ageing under
  FIFO-violation — the oldest proposal is untouched since 08-08; per the backpressure literature,
  latency grows with queue depth, so every day of intake at full rate directly lengthens the wait for
  items already queued. (c) Attribution error — the day's own summary frames the problem as drainage,
  which locates the fault entirely at the gate; the queueing result says intake is a co-equal term, so
  seventeen days of unthrottled production is not a neutral background fact but, as 14b puts it, "the
  largest single contributor to the thing being complained about." (d) Green-while-failing — every
  automated stage reported healthy throughout, because each producer's local metrics are fine; the
  failure is only visible in a quantity no agent computes. (e) Quality degradation under depth — the
  code-review analogue suggests that as review backlog grows, review quality per item falls and defect
  escape rates rise, so the queue does not merely delay work, it degrades what eventually passes.
  (f) Compounds with PRESUMPTION-878 (four new checks would add four new flag populations to this
  queue), PRESUMPTION-882 (300+ un-back-cited ids would be added as findings), and PRESUMPTION-879
  (every declined-on-remit fix is handed to this same gate).

  Mitigations available:
    - Give every producer read access to the gate's depth and its 7-day disposition rate. This is the
      minimum enabling change: backpressure cannot be exercised by an agent that cannot observe the
      thing it should back off from.
    - Impose a WIP limit on the pending population. Above the limit, producers file to a holding area
      rather than the gate, or file only items above a priority threshold. This is the standard
      mechanism and is trivially implementable in a file-based system.
    - Alternatively, couple intake to disposition proportionally: allow N new proposals per proposal
      dispositioned, with a floor for Critical items so genuine emergencies are never blocked.
    - Add a timeout disposition so μ cannot be zero. An item unruled after N days auto-dispositions to
      a named default state. This makes the stability inequality satisfiable without requiring the
      human to act, and is the same fix recommended for PRESUMPTION-879 and -881.
    - Publish queue age distribution, not just depth. Depth alone (74) understates the problem; the
      08-08 item's age is the number that would have triggered attention.
    - Load-shed by priority rather than uniformly. The CoDel/priority-shedding literature warns
      specifically against bulk-closing low-severity items, since that is how systematic blindness to
      a whole class develops — a caution that bears directly on PRESUMPTION-884.

  STEELMAN:
    Item: PRESUMPTION-883
    Strongest counterargument: Queueing theory applies to systems where a queued item's value is
    constant and its only cost is delay. Proposals are not that object. A proposal that sits unruled
    for seventeen days is still *fully preserved* — nothing degrades, nothing is dropped, and the work
    of producing it (the analysis, the diagnosis, the citation) was valuable to the producing agent
    independent of whether the gate ever rules. Throttling intake would therefore not save the queue;
    it would destroy work that has already been done, and it would suppress exactly the signal the
    gate most needs when it returns — namely, a complete record of everything the system found while
    it was away. Worse, coupling intake to disposition hands a single unresponsive human a global
    throttle on all autonomous work: if the gate stays silent for a month, a coupled system does
    nothing for a month, which converts a review backlog into a total work stoppage. The +14 is not a
    pathology; it is seventeen days of agents "clearing their own blockers," which is the behaviour the
    architecture was built to produce. The right reading is that the gate is the constraint and the
    correct Theory-of-Constraints response is to *elevate* the constraint — add reviewers, batch,
    auto-approve low-risk classes — not to subordinate the whole system's output to it.
    What would need to be true for C2A2 to be safe: (i) queued proposals must genuinely not decay —
    but PRESUMPTION-876 says dated verdicts go stale and PRESUMPTION-884 shows a blanket attribution
    can silently invalidate a whole flag population, so a seventeen-day-old proposal may already be
    reasoning about a superseded state; (ii) the queue must be *readable* on the gate's return — 74
    items, growing at 14/day, is already past the point where a single reviewer can process it in one
    sitting, and the backpressure literature's warning is that depth itself becomes the barrier to
    drainage; (iii) the gate's absence must be temporary and bounded, which after seventeen days is no
    longer a safe assumption; (iv) there must be no priority inversion — if Critical items are queued
    behind Medium ones, depth converts directly into risk; (v) the producing agents must not be
    consuming resources that would otherwise go to drainage, which in a shared-budget system
    (cf. PRESUMPTION-881's fifteen budget breaches) is not obviously true.
    How to test: Fully computable from the existing queue file and requiring no literature. (1) Fit the
    trivial model: plot pending count against date and compute λ and μ over the last 30 days. If μ is
    zero or near-zero while λ is positive, the stability condition is violated and the presumption is
    refuted arithmetically, not rhetorically. (2) Compute the age distribution and the projected
    drainage time at the gate's *historical* (pre-silence) disposition rate — if drainage time exceeds
    the interval between gate appearances, the queue is unrecoverable even when the gate returns, which
    is the decisive number. (3) Test the steelman directly: sample 10 proposals filed more than
    fourteen days ago and check whether each is still valid against current state. The fraction that
    have gone stale is the decay rate the counterargument assumes is zero. (4) Check for priority
    inversion: is any Critical item queued behind a Medium one? PRESUMPTION-877, -880 and -881 are all
    Critical and all entered a queue whose oldest item dates from 08-08.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single, currently
      unresponsive human review gate, and not one of the seven presumptions conditions its behaviour
      on that gate's responsiveness.** PRESUMPTION-883 *is* the systemic risk stated directly, which
      is why it should be resolved first: 878 sends new flag populations to the gate, 879 hands
      declined fixes to it, 880's corrections are unadjudicated because it never rules, 881's fifteen
      breach disclosures are addressed to it, 882's 300+ reclassified ids would enter it, and 884's
      blanket suppression rule was never ruled on by it. Seven presumptions, one dependency. Note that
      all seven of these items were themselves filed into that same queue.
    Literature basis: Little's law stability precondition — λ > μ implies L = ∞, W = ∞
      (https://en.wikipedia.org/wiki/Little's_law; Little & Graves,
      https://web.eng.ucsd.edu/~massimo/ECE158A/Handouts_files/Little.pdf); stabilisation of an
      overloaded network by admission control (arXiv:0708.2739); backpressure as the missing ability
      "to say it cannot keep up" (https://designgurus.substack.com/p/system-design-deep-dive-backpressure);
      alert fatigue dose-response (https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-017-0430-8);
      normalisation of deviance (https://en.wikipedia.org/wiki/Normalization_of_deviance).
    Risk level: Critical
    Recommendation: Fix this item first; it is the load-bearing one. The minimal intervention is a
      timeout disposition that makes μ > 0 without requiring the human to act, plus read access to
      queue depth for every producing agent. Both are small changes to a file-based system and both
      are preconditions for the remedies proposed under -878, -879, -880, -881, -882 and -884.

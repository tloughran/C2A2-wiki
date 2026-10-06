SEARCH-FOR-PRESUMPTION-950:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-950
  Original statement: "[inferred] That an empty `pending/` is an achievement to be protected, and that
    refilling it is a cost — i.e. that the reviewer's backlog is the scarce resource and the traditions'
    un-surveyed output is not."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-950
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated judgement whose cost side is absent; the presumption is not that the
        call was wrong but that only one of the two ledgers was consulted.
      15a: Searched for supporting literature; found the queue-discipline literature supports the
        protect-the-reviewer limb outright and reads an empty column as a *symptom*, not an achievement.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - PREMISE-070 (ACTIVE) — "the binding constraint on the proposal pipeline is human review
      throughput, not literature discovery (review-bound). By Theory of Constraints, other stages should
      be subordinated to review — i.e. do not over-feed intake while review is the bottleneck." This
      bears directly and already grants Limb A.
    - PREMISE-119 (ACTIVE) — production and judgment are not independently schedulable; unbounded
      production imposes a congestion externality.
    - PREMISE-121 (ACTIVE) — a reviewer's per-item cost is not constant; acceptance falls as volume and
      cumulative exposure rise.
    - PREMISE-147 (ACTIVE) — "A QUEUE'S SIZE MEASURES DEMAND AND ACTIVITY, NOT PERFORMANCE; AN UNPAIRED
      PRODUCER-SIDE COUNT IS AN INVERTED HEALTH SIGNAL; AND THE STATISTIC THAT CARRIES THE INFORMATION
      IS AGE, NOT COUNT." This is the precise refutation of "an empty queue is an achievement" and is
      already ACTIVE. It is the single most on-point register hit across all ten items.
    - PREMISE-106 (ACTIVE) — the lit-search queue is in the unstable regime; arrival exceeds service.
    - PREMISE-189 (ACTIVE) — absent an independently maintained expectation of what should be present,
      the artifact set cannot distinguish deliberate omission from incidental loss. This is exactly
      14b's "the hunt leaves no negative record" point.
    Recording the hits per OPEN-192; searched anyway.

  LIMB SPLIT:
    Limb A (DON'T OVER-FEED): when review is the binding constraint, adding items ahead of absorption
      reduces throughput, so restraint in replenishment is a genuine good.
    Limb B (EMPTY IS AN ACHIEVEMENT): a queue at zero is a state to be protected, and a survey not run
      on a zero-queue day costs nothing.

  Supporting evidence found: Yes (Limb A), No (Limb B)

  Sources:
    1. Little's Law and its kanban application (Kanban Tool "Queuing Theory & Kanban"; Atlassian
       "Working with WIP limits for kanban"). — SECONDARY — Average cycle time = average WIP ÷ average
       throughput; throughput is bounded by capacity, so WIP is the only lever, and "halving the number
       of items in flight roughly halves the time each takes to finish." Direct formal support for Limb
       A.
    2. Queueing-theory saturation result as applied in the kanban literature. — SECONDARY —
       "Processing work-in-progress close to full capacity drastically increases waiting times, as even
       small fluctuations of intake can't be absorbed." Supports Limb A and supplies the mechanism:
       the cost of over-feeding is superlinear near saturation, which is where the estate's reviewer has
       been for fourteen days.
    3. Review-gate bottleneck material specific to AI-accelerated production (Yeret, "Kanban WIP Limits
       for Spec-Driven Agentic Development"; EasyKanban "WIP Limits Explained"). — SECONDARY —
       "While code generation accelerates, human-bound stages... cannot scale at the same rate. This
       creates a severe queue at the review gate." This is the estate's exact shape — agent producers,
       one human reviewer — and it supports Limb A in the strongest available form.
    4. The same literature on empty columns — and this is the finding that splits the item. — SECONDARY
       — "A consistently empty column signals unused capacity, or upstream deficit." And on
       replenishment policy: "Ad hoc replenishment, where the team scrambles only once the queue runs
       dry, produces rushed choices, unprepared work, and idle time while someone finds something to
       do." Kanban treats a dry queue as *starvation*, a named pathology symmetric with saturation, and
       treats scheduled replenishment as the remedy for it. Limb B is not merely unsupported here; the
       literature's own vocabulary contradicts it.
    5. Theory of Constraints subordination (drum-buffer-rope as presented in the portfolio-kanban
       material, Ivar Jacobson International). — SECONDARY — Subordination means the non-constraint
       stages run *to the constraint's drumbeat*, which entails a buffer in front of the constraint, not
       an empty one. TOC's protection of the constraint is achieved by keeping a *small non-zero* buffer
       precisely so the constraint never starves. Supports Limb A while refuting Limb B on TOC's own
       terms: protecting the reviewer means buffering the reviewer, not emptying the buffer.

  Strength of support: Strong (Limb A), None (Limb B)

  Summary: The queue-discipline literature grants Limb A without qualification, and PREMISE-070 already
    grants it inside the estate — restraint in replenishment when review is the constraint is correct,
    and the skip decision was defensible on that ground. Limb B finds no support at all, and the
    sources that support Limb A are the same ones that refute it: kanban names a persistently empty
    column as starvation or upstream deficit, TOC's subordination principle calls for a protective
    buffer in front of the constraint rather than a drained one, and ad-hoc replenishment-on-empty is
    named as a specific anti-pattern producing rushed selection. So the literature's position is not
    "run the hunt" or "skip the hunt" but "replenish on a cadence and cap the queue" — which prices both
    ledgers instead of one. The second, cheaper in-house question 14b raises is the more important one
    and the literature reinforces it via PREMISE-189: if the hunt writes no negative record on days it
    runs and finds nothing, then a skipped day and a genuinely quiet day are indistinguishable in the
    archive forever, and no amount of queue theory recovers that.

  Caveats: Kanban and TOC are manufacturing and software-delivery frameworks whose queues carry
    homogeneous, interchangeable items; a day of tradition output is neither interchangeable nor
    recoverable later, which is a disanalogy that *strengthens* the case against Limb B rather than
    weakening it. No source I found prices the cost of an unsampled period in a discovery pipeline —
    that is a sampling/coverage question, not a queueing one, and this search did not enter it. All
    sources are practitioner literature rather than peer-reviewed; Little's Law is the only formal
    result among them and it does not by itself decide the replenishment policy.

  Search scope: comprehensive for the queue-discipline limb, preliminary for the sampling-cost limb —
    searched WIP limits, Little's Law in kanban, queueing saturation and starvation, replenishment
    policy, review-gate bottlenecks under AI-accelerated production, and TOC subordination. Did not
    search survey-sampling or missing-at-random literature, which is where the "cost of not sampling"
    question actually lives and which would be the right next step.

  Recommendation: PARTIALLY-SUPPORTED. The recommendation rests on Limb A, which is SUPPORTED and which
    vindicates the skip decision on its stated ground. Limb B is NO-SUPPORT-FOUND and is the limb that
    carries the precedent risk 14b identified. The literature converts the finding into one concrete
    change: replace the implicit rule "skip replenishment when the queue is empty and the reviewer is
    behind" with a declared cadence plus a queue cap, and make the hunt write a negative record on every
    day it runs — so that skipped days become visible, which is the whole of OPEN-194.

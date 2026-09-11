SEARCH-AGAINST-ASSUMPTION-1305:
  Date searched: 2026-09-11
  Original item: ASSUMPTION-1305
  Original statement: "**Phase 2 skipped on judgement**, not omission: refilling the queue the same
    morning you emptied it would put new cards in front of you before any of today's 85 triplets had been
    looked at."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1305
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted verbatim and routed. Recorded as the first day on which `pending/` reached zero and
        the run's response was to withhold supply; the cost side is not priced in the report.
      15b: Searched for challenging literature; found that the assumption's own governing theory (TOC)
        prescribes the OPPOSITE action at an empty constraint buffer, and that the two limbs are about
        two different stages of the pipeline.
    Current status: PARTIALLY-CHALLENGED

  Register pre-check:
    - PREMISE-070 (ACTIVE) — "Since 06-16 the binding constraint on the proposal pipeline is human review
      throughput, not literature discovery (review-bound). By Theory of Constraints, other stages should
      be subordinated to review — i.e., do not over-feed intake while review is the bottleneck."
      This is a near-exact pre-answer to LIMB A and it is already ACTIVE.
    - PREMISE-119 (ACTIVE) — production and judgment are not independently schedulable; unbounded
      production imposes a congestion externality. Pre-answers LIMB B in the supportive direction.
    - PREMISE-121 (ACTIVE) — reviewer per-item cost is not constant; acceptance falls as volume rises.
    - PREMISE-147 (ACTIVE) — a queue's size measures demand and activity, not performance; the statistic
      that carries information is AGE, not COUNT. **This one cuts against the run**: `pending/ = 0` is a
      count, and the run treated a count as an achievement.
    - PREMISE-106, PREMISE-095 (ACTIVE) — the lit-search and 15d queues are in the unstable regime
      (arrival > service). Under those premises the system is chronically oversupplied, not undersupplied.
    - PREMISE-050 (ACTIVE) — drain backlogs in small scoped batches, batch size tuned.

  Challenging evidence found: Partial

  LIMB STRUCTURE — three limbs, and they do not stand or fall together:
    LIMB A — "reviewer attention, not proposal supply, is the binding constraint."
    LIMB B — "presenting new items before old ones are absorbed reduces throughput."
    LIMB C — "therefore the correct act on the morning `pending/` hit zero was to skip the hunt phase."

  Sources:
    1. Goldratt, E.M. — Drum-Buffer-Rope / Theory of Constraints, as documented in current practitioner
       references (velaction.com, 6sigma.us, sixsigmadsi.com, fortelabs.com, BDC). — SECONDARY (multiple
       independent practitioner descriptions retrieved via search; Goldratt's primary text not retrieved)
       — DBR's entire purpose is a **protective buffer positioned immediately before the constraint whose
       function is to ensure the drum never runs dry**. TOC does not say "stop releasing work when the
       buffer empties"; it says the opposite — an empty constraint buffer is the failure DBR exists to
       prevent, and the rope releases work at the constraint's pace precisely so the buffer is never
       starved. The run invoked constraint logic (PREMISE-070) to justify an action that constraint logic
       forbids. **This is the strongest single challenge in this file.**
    2. PREMISE-147's own content (in-register) — a queue's COUNT is not a health signal; AGE is. —
       VERIFIED (read in `premises_index.md`) — `pending/ = 0` was read as an achievement. Under
       PREMISE-147 it is an uninformative reading, and under DBR it is an alarm.
    3. Code-review queue-dynamics practitioner analyses (Count.co code-review bottleneck; Pečar, "The
       Code Review Batch Size"; multiple 2025-26 engineering write-ups citing an 8M-PR dataset) —
       SECONDARY/UNVERIFIED (the "8 million PRs" dataset is a blog claim; I did not retrieve the
       underlying data and it carries no weight here) — the *qualitative* mechanism these report is that
       the dominant idle time is **waiting for initial pickup**, i.e. reviewer-side latency, and that
       slow review causes authors to BATCH MORE per item, making review slower still. Note the direction:
       this is a case for keeping items small and flowing, not for withholding them.
    4. Web-content ephemerality / crawl-timeliness literature (arXiv 1307.6080, "Timely crawling of
       high-quality ephemeral new content"; link-rot literature) — SECONDARY (abstract-level via search)
       — the cost of a skipped survey day is not zero and is not symmetric with the cost of a full queue:
       ephemeral content has a decaying probability of being retrievable later, and the run's own Phase 1
       already contained a paywalled recording and a time-limited FLAG-023 window. Un-surveyed supply can
       become permanently un-surveyable; an unread card cannot.
    5. Deming / SPC "tampering" literature (Deming Alliance; SPC for Excel; ScienceDirect, "Deming's
       tampering revisited") — SECONDARY — adjusting a release policy on the strength of a single day's
       reading is the textbook tampering move. One day at zero is one observation.

  Strength of challenge: Moderate (LIMB A: Weak — PREMISE-070 already carries it. LIMB B: Weak — well
    supported by PREMISE-119/121. **LIMB C: Strong** — the inference from A and B to "skip the hunt" is
    the step the literature denies.)

  Summary: Limbs A and B are in good standing and are already ACTIVE premises in this register, so
    searching them again produced nothing new. The defect is in limb C, and it is a real one. The run
    reasoned from Theory of Constraints to an action that Theory of Constraints specifically forbids:
    drum-buffer-rope exists to keep a protective buffer in front of the constraint so it never starves,
    and `pending/ = 0` is the state DBR is engineered to prevent, not a state to preserve. Second, limbs
    A/B concern items *in the review queue*, whereas what was un-absorbed on 2026-09-10 was 85 triplets
    *already ingested downstream* — a different stage. Withholding supply at stage 1 does not relieve
    congestion at stage 3; it only starves stage 1. Third, the costs are asymmetric in the direction the
    run did not price: an unread card waits patiently, whereas an un-surveyed source can become
    unretrievable, and this run's own Phase 1 contained a paywalled recording and a time-limited window.

  Specific risks: If limb C is wrong, the system now has a precedent for treating an empty intake queue
    as a goal state, which converts a temporary review backlog into a permanent discovery gap. Because
    supply here is *perishable* (paywalls, recordings, deleted posts, member-only windows such as
    FLAG-023), the loss is not recoverable by working harder later. The failure is invisible by
    construction: nothing appears in any register to record what was never surveyed, so the cost never
    enters the ledger while the benefit (an empty queue) is loudly reported. Compare PREMISE-169 — a job
    that never starts emits nothing.

  Mitigations available:
    - Replace the zero-target with a **target buffer band** (DBR): hold `pending/` between, say, 5 and 25
      items and release on that signal rather than on emptiness. This preserves limbs A and B while
      removing the starvation failure.
    - Decouple the two stages: hunt-phase output goes to a *staging* area that does not compete for
      reviewer attention, so supply continuity and reviewer load are separately controllable.
    - Price the skipped day: log what the hunt phase *would* have surveyed (source list, not contents),
      so the cost side becomes auditable rather than invisible.
    - Triage perishable sources out of the throttle entirely — a paywalled recording or a dated window is
      captured on sight regardless of queue depth.

  STEELMAN:
    Item: ASSUMPTION-1305
    Strongest counterargument: The relevant constraint is not "cards in `pending/`" but the human's total
      attention, and on 2026-09-10 that attention had just been spent on a 36-card batch and owed 85 new
      triplets. Under PREMISE-119 the producing and reviewing stages are provably coupled, so adding
      supply at stage 1 genuinely does impose a congestion externality on a person who is one queue, not
      three. The DBR objection assumes a constraint that is idle; this constraint was not idle, it was
      saturated, and a buffer in front of a saturated constraint is pure WIP. Little's Law then says the
      added WIP buys nothing but latency. The run's judgement was therefore correct for the day even if
      its stated rationale generalises badly.
    What would need to be true for C2A2 to be safe: (1) the human's attention really is a single shared
      resource across hunt-output and triplet-absorption, rather than two separable activities; (2) the
      constraint is genuinely saturated rather than merely recently busy — i.e. the queue was skipped
      because the drum is running, not because the drum stopped; (3) the skip is bounded and
      self-terminating (one day, with an explicit restart rule), not a policy; and (4) perishable sources
      are exempted from the throttle.
    How to test: This is in-house and cheap. Instrument two series over 30 days: (a) `pending/` depth and
      AGE at each run, and (b) items surveyed-vs-skipped by the hunt phase. Then check the DBR prediction
      directly: on days following a skipped hunt phase, did review throughput (items dispositioned) go
      UP, or did the pipeline simply idle at stage 1? If throughput is flat and stage 1 is empty, the
      constraint was starved and limb C is refuted. Separately, sample 10 sources the hunt phase skipped
      on 2026-09-10 and re-attempt retrieval today; the non-retrievable fraction is the perishability
      cost the report omitted.

  Search scope: preliminary — broader search recommended. Searched: theory of constraints /
    drum-buffer-rope / constraint starvation; code-review queue dynamics, batch size and reviewer idle
    time; work-in-progress limits and intake throttling; ephemeral web content and crawl timeliness;
    Deming tampering / special-vs-common cause. NOT searched and worth searching: the CONWIP vs kanban
    comparison literature (which is directly about whether to release on emptiness or on a fixed cap),
    and the surveillance/epidemiology literature on the cost of a skipped observation period.

  Recommendation: PARTIALLY-CHALLENGED — and the recommendation rests entirely on LIMB C. Limbs A and B
    are NO-CHALLENGE-FOUND and are already covered by PREMISE-070 and PREMISE-119.

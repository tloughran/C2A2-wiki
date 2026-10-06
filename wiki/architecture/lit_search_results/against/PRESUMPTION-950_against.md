SEARCH-AGAINST-PRESUMPTION-950:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-950
  Original statement: "[inferred] That an empty `pending/` is an achievement to be protected, and that
    refilling it is a cost — i.e. that the reviewer's backlog is the scarce resource and the traditions'
    un-surveyed output is not."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-950
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a stated judgement whose cost side is absent; the run was right to flag the
        judgement as a judgement, and the presumption is that only one of the two ledgers was consulted.
      15b: Searched for challenging literature; found the queue-discipline limb already settled in the
        register in BOTH directions (PREMISE-070/119/121 for the judgement, PREMISE-147 against the
        metric), and found the delay-time inspection literature supplying the missing cost side.
    Current status: PARTIALLY-CHALLENGED

  Register pre-check — this item is unusual in that the register answers it on both sides:
    - **FOR the run's judgement:** PREMISE-070 (ACTIVE) — since 06-16 the binding constraint is human
      review throughput, not literature discovery; by Theory of Constraints, other stages should be
      subordinated to review. PREMISE-119 (ACTIVE) — production and judgment are not independently
      schedulable; unbounded production imposes a congestion externality. PREMISE-121 (ACTIVE) — a
      reviewer's per-item cost is not constant and capacity does not scale with production. PREMISE-106
      (ACTIVE) — the queue is in the unstable regime and no scheduling discipline recovers it. Four
      ACTIVE premises say the run's call was correct on the reviewer ledger.
    - **AGAINST the metric the run used:** **PREMISE-147 (ACTIVE), verbatim and decisive** — "A QUEUE'S
      SIZE MEASURES DEMAND AND ACTIVITY, NOT PERFORMANCE; AN UNPAIRED PRODUCER-SIDE COUNT IS AN INVERTED
      HEALTH SIGNAL; AND THE STATISTIC THAT CARRIES THE INFORMATION IS AGE, NOT COUNT." The run treated
      `pending/ = 0` — a count — as an achievement. PREMISE-147 says a count is not a health signal in
      either direction.
    - **AGAINST the absent record:** PREMISE-141 (ACTIVE) — absence of a report is a THIRD terminal state,
      not a value of the other two. PREMISE-169 (ACTIVE) — "THE REGISTRY IS THE COVERAGE. A scheduled job
      that has never started emits nothing... invisible BY CONSTRUCTION to every monitor whose input is
      the job's own output." A skipped hunt is exactly this. PREMISE-189 (ACTIVE) — detection of omission
      requires an independently maintained expectation about what should be present. PREMISE-063 (ACTIVE)
      — absence must be encoded as distinct from a true zero.

  Challenging evidence found: Partial

  Sources:
    1. Delay-time maintenance modelling (Christer's delay-time concept; Wang, "An overview of the recent
       advances in delay-time-based maintenance modelling," Reliability Engineering & System Safety, 2012;
       and the departures-from-schedule line, e.g. the resumable-jobs/inspection-policy paper in RESS
       2022). — SECONDARY (search summaries retrieved; ScienceDirect full texts PAYWALLED and not
       retrieved — recorded) — The failure process is two-stage: a defect becomes detectable at some
       point, then fails if unattended; the interval between is the delay time. Inspection frequency
       directly sets expected undetected-defect exposure, and the literature explicitly models the case
       where "departures from the inspection schedule are highly likely, for many reasons, and
       collectively because production takes priority over maintenance." That is the exact shape of
       "Phase 2 was skipped because the reviewer was behind" — the literature treats it as a known,
       modellable cost, not as a free pause. This is the missing second ledger.
    2. Outbreak-surveillance sampling-gap literature ("Optimal environmental testing frequency for
       outbreak surveillance," PMC10979539; "Surveillance Testing for Rapid Detection of Outbreaks in
       Facilities," arXiv:2110.00170). — SECONDARY (search summaries) — An outbreak may go undetected
       because an infected node was not tested; detection delay is a function of sampling frequency. A
       skipped sampling interval does not produce a negative observation, it produces no observation, and
       the two are not distinguishable downstream. Transfers directly.
    3. Goldratt's Theory of Constraints (register-held under PREMISE-070). — CANONICAL — Reported here
       because it cuts FOR the run: an idle non-bottleneck is not a loss, and subordinating upstream
       stages to the constraint is the doctrine, not a lapse. The run's reasoning is textbook TOC. The
       defect is not the subordination; it is that the subordination was performed without pricing the
       coverage side and without leaving a record.
    4. ISA-18.2 / EEMUA 191 shelving semantics. — SECONDARY (search summaries) — Included for the design
       pattern: when a system deliberately suppresses a signal, the suppression is itself a first-class,
       time-bounded, recorded object (EEMUA 191 specifies a 4-hour default shelf life). The suppressed
       state is visible and expires. The skipped hunt has neither property.

  Strength of challenge:
    - Limb A, "the skip was the wrong call": **Weak**. Four ACTIVE premises and TOC support the call. I
      found nothing that says a review-bound system should keep producing into a saturated reviewer. 14b
      does not claim this limb either.
    - Limb B, "an empty queue is an achievement": **Strong**, and settled in-register. PREMISE-147 holds
      that a count is not a health signal; PREMISE-106 holds that this queue is in the unstable regime,
      in which an instantaneous zero is a sampling artefact rather than a state. Reading zero as an
      achievement is reading the least informative statistic the queue has.
    - Limb C, "the skipped day left no cost and no record": **Strong**. Delay-time modelling prices the
      cost; PREMISE-169 and PREMISE-141 establish that the record does not exist; and the skipped day and
      a genuinely empty day are indistinguishable in the archive by construction.
    The recommendation rests on Limbs B and C. Limb A is not challenged and should not be recorded as
    challenged.

  Summary: The run made the right call on the reviewer ledger and the register supports it four times
    over. What the literature and the register jointly refute is the framing, not the decision. An empty
    queue is not an achievement — it is a count, and PREMISE-147 already says a count is an inverted
    health signal; the informative statistic is age. And the skip is not a pause, because delay-time
    modelling prices exactly this: skipping an inspection interval increases expected undetected-defect
    exposure by a computable amount, and the surveillance literature adds that a skipped interval produces
    no observation rather than a negative one. The estate's own PREMISE-169 states the mechanism in the
    register's own words. So: correct decision, wrong ledger, and no artefact by which any later run can
    know the day happened.

  Specific risks: The exposure is the precedent, as 14b says, and it has a specific shape. Because the
    hunt leaves no negative record, the coverage gap is invisible by construction (PREMISE-169), which
    means the cost of skipping is structurally unobservable while the benefit (a queue at zero) is
    structurally visible. That asymmetry does not decay — it licenses the same call on every subsequent
    day the reviewer is behind, and the reviewer has been behind for fourteen days. The failure mode is
    not one missing day; it is a drift in which the hunt runs only on days when it is cheapest to run,
    producing a coverage record that is biased toward the traditions and periods that happened to be
    quiet.

  Mitigations available:
    - **Write the negative record.** On every day the hunt runs, emit a dated line stating what was
      surveyed and that nothing was found; on every day it is skipped, emit a dated line stating it was
      skipped and why. One line either way, and it converts PREMISE-169's invisible-by-construction gap
      into a queryable one. This is OPEN-194's convention question and it is the whole fix for Limb C.
    - **Report age, not count.** Replace "`pending/` reached zero" with the age of the oldest un-surveyed
      tradition-day. PREMISE-147 names this as the statistic that carries the information.
    - **Model the skip as a shelve, not a pause.** Borrow EEMUA 191's pattern: a deliberate suppression is
      a recorded object with an expiry. "Hunt shelved until DATE, reason: reviewer saturation" is visible,
      time-bounded, and self-clearing, where "normal schedule resumes tomorrow" is none of those.
    - **Decouple survey from enqueue.** The hunt's output need not enter `pending/`. Surveying and
      presenting are different acts; TOC subordinates the *presenting* stage to the constraint, not the
      *observing* stage. This costs the reviewer nothing and closes the coverage gap entirely, and I think
      it is the most important available mitigation because it dissolves the trade-off rather than pricing
      it.

  STEELMAN:
    Item: PRESUMPTION-950
    Strongest counterargument: There are genuinely two ledgers and only one of them has a measured
      constraint. The reviewer's throughput is measured, is the binding constraint (PREMISE-070), and
      PREMISE-106 proves the queue is already unstable; the traditions' un-surveyed output has no measured
      arrival rate, no measured decay rate, and — critically — no evidence that anything found on day N is
      unfindable on day N+1. Scholarly output is durable. A paper posted today is still posted tomorrow.
      Unlike a physical inspection, where the defect matures during the skipped interval, a missed hunt
      day usually costs *latency*, not *coverage*, because the next run's sweep window can be widened to
      cover it. If that is true, the delay-time analogy is the wrong model and the cost of the skip is
      one day of staleness on a low-velocity signal — genuinely small against a saturated reviewer.
    What would need to be true for C2A2 to be safe: (a) the hunt's sweep must be window-based rather than
      "since last run" — if the next run re-covers the skipped interval, no coverage is lost and only
      latency is; (b) the traditions' signal must actually be durable on the surfaces the hunt reads
      (feeds that truncate, event pages that are taken down after the event, and social posts that scroll
      out of a window all break this — and those are exactly the surfaces PRESUMPTION-947 says the estate
      under-reads); (c) the skip must be recorded either way, because (a) and (b) are claims that some
      later run has to be able to check. (c) is required under every reading.
    How to test: one code read and one experiment. First, read the hunt's sweep logic: is the window
      "since last successful run" or "last N days"? If the former, a skipped day IS a coverage hole and
      the steelman fails immediately. Second, if it is window-based, take one skipped day and re-run the
      hunt over that day's window a week later; count items found that the subsequent runs had not
      surfaced. Zero means latency-only and the steelman holds.

  Search scope: comprehensive on the cost-of-a-missed-interval question (delay-time maintenance modelling,
    inspection-interval optimisation, surveillance sampling gaps, alarm shelving semantics); preliminary
    on review-batch sizing, which is ASSUMPTION-1305's territory and is already held by PREMISE-070/119/121.
    Two ScienceDirect delay-time papers were PAYWALLED; figures from them are recorded as SECONDARY and no
    quantitative claim rests on them.

  Recommendation: PARTIALLY-CHALLENGED

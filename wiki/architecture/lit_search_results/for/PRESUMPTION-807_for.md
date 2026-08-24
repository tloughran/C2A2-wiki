SEARCH-FOR-PRESUMPTION-807:
  Date searched: 2026-08-15
  Original item: PRESUMPTION-807
  Original statement: [inferred] That the backlog is a backlog. The lit-search re-trigger lane holds 219 unsearched items and the pipeline serves eleven per cycle, having served the new-intake lane in preference for a fourth consecutive cycle; nobody has computed that this is roughly twenty cycles of exclusive service to clear, against an intake that adds items nightly. The same arithmetic is unperformed on the review queue (35 cards, gate dark twelve days) and on the deferred Summa batch passes. "Backlog" presumes a transient excess over capacity. If intake exceeds service rate structurally, the correct word is not backlog but steady state, and the queue depth then carries no information about urgency at all.

  POLARITY NOTE — what was searched FOR. The presumption is worded as the DEFECTIVE belief ("the backlog is a backlog"). The proposition searched FOR is the CORRECTIVE CONVERSE, in four clauses: (i) that queue stability is decided by the ratio rho = lambda/mu and not by the queue's depth, so that depth is uninformative about urgency once rho >= 1; (ii) that at rho >= 1 no scheduling discipline internal to the server recovers stability — scheduling partitions the backlog between lanes but cannot reduce the total; (iii) that under STRICT PRIORITY the low-priority class's waiting time diverges as the high-priority load approaches saturation, INDEPENDENTLY of how few low-priority items arrive, which is the formal statement of the observed five-consecutive-cycle starvation; and (iv) that the remedy space is therefore admission control or a service-rate change, not a scheduling change. "SUPPORTED" below means 14b's worry is well grounded and is equivalently evidence AGAINST the presumption as worded.

  THE ARITHMETIC, PERFORMED. The queue called this "the single cheapest item here — the arithmetic is available now." It is done below rather than described.

    INPUTS (as supplied by the queue; each is a self-report, see Caveat (a)):
      L  = 219 items standing in the 15d re-trigger lane [measured 2026-08-14]
      mu = ~11 items served per cycle, cycles nightly  -> mu ~= 11 items/day
      lambda = ~10-15 items added nightly              -> lambda ~= 12.5 items/day (midpoint)

    UTILISATION rho = lambda / mu:
      lambda = 10   ->  rho = 10/11   = 0.909
      lambda = 12.5 ->  rho = 12.5/11 = 1.136      <- POINT ESTIMATE
      lambda = 15   ->  rho = 15/11   = 1.364
      REPORTED RHO: ~1.14, with a range of 0.91 to 1.36.
      rho >= 1 over 80%+ of the stated intake range, and at the midpoint. The stability
      condition rho < 1 is satisfied ONLY at the extreme low end of the declared intake band,
      and even there by a margin of one item per day.

    DRAIN RATE = mu - lambda (the SURPLUS rate, not the service rate — PREMISE-106 corollary (i)):
      lambda = 10   -> +1.0 items/day -> 219 items clear in 219 days (~2027-03-22)  [BEST CASE]
      lambda = 11   ->  0.0 items/day -> NEVER CLEARS; L stays at 219 indefinitely
      lambda = 12.5 -> -1.5 items/day -> L GROWS: ~264 by 2026-09-14, ~767 by 2027-08-15
      lambda = 15   -> -4.0 items/day -> L GROWS: ~339 by 2026-09-14, ~1,679 by 2027-08-15

    WHAT THE "TWENTY CYCLES" FIGURE ACTUALLY MEANS. 219/11 = 19.9 cycles, so the queue's own
    figure is arithmetically right. But it is a figure for EXCLUSIVE service: twenty nights in
    which the new-intake lane receives nothing. Over those twenty nights the intake lane accrues
    20 x 12.5 ~= 250 items. Net system state after the drain: re-trigger lane 0, intake lane ~250.
    THE TOTAL IS UNCHANGED (219 -> ~250, i.e. slightly worse). The drain is a RELABELLING, not a
    clearance. This is the direct formal expression of the run's own stated dilemma — "withholding
    the day's items would substitute one starved lane for another" — and the arithmetic shows the
    run's instinct was correct and its framing was not: the choice between lanes is real, but it
    is a choice about WHICH lane starves, not about whether one does.

    TOTAL WORK IN SYSTEM. W(t) = W(0) + (lambda - mu) * t. At the point estimate,
    W(t) = 219 + 1.5t items. Scheduling changes the PARTITION of W across lanes; it cannot
    change W. No admissible reordering of an 11-item nightly budget makes 1.5 items/day disappear.

    STRICT-PRIORITY STARVATION (the formal account of "fifth consecutive cycle"). Treat new intake
    as the high-priority class H and the re-trigger lane as low-priority L. Then rho_H = lambda_H/mu
    is itself in the 0.91-1.36 band, because the nightly intake alone is comparable to the whole
    service budget. The standard non-preemptive two-class M/G/1 result gives
        W_L = R0 / [ (1 - rho_H)(1 - rho_H - rho_L) ]
    which diverges as rho_H -> 1 REGARDLESS of rho_L. At the point estimate rho_H > 1 and the
    expression is not merely large but undefined: the high-priority class alone saturates the
    server and the low-priority class receives zero service in the limit. The observed five
    consecutive cycles of exclusive intake service is not a scheduling lapse, a DEFECT-I
    non-compliance, or an agent's discretion. IT IS THE PREDICTED BEHAVIOUR OF THE CONFIGURATION.
    Even in the most favourable case (rho_H = 0.909), the low-priority lane is stable only if
    rho_L < 0.091, i.e. fewer than ~1 re-trigger item per day; 15d's weekly re-trigger cadence
    (~55/week ~= 7.9/day, PREMISE-095) exceeds that by roughly 8x.

    LITTLE'S LAW, APPLIED. L = lambda * W. Applied naively to the lane at lambda = 11 and L = 219,
    W ~= 20 days mean residence. That number is NOT VALID here and quoting it would be an error:
    Little's law is an equality over a system in steady state, and at rho >= 1 there is no steady
    state — L grows linearly and therefore so does W. The correct statement is that W is unbounded.
    Little's law's actual use in this case is diagnostic, not predictive: the fact that no finite W
    satisfies the relation IS the demonstration that the word "backlog" (which presupposes a finite
    W) does not apply.

    THE REVIEW QUEUE (35 cards, gate dark 12 days). Here the measurement is starker and requires
    no estimate. Observed service over the 12-day window is ZERO items. mu = 0, so rho = lambda/0
    is undefined/infinite for any positive intake, and W is unbounded for ANY L, including L = 1.
    The number 35 carries no information about urgency, delay, or effort; it is the running
    integral of a stopped server. This is PREMISE-102's "channel with demonstrated zero throughput"
    stated as a queueing fact rather than as a reporting norm. NOT ARBITRATED HERE: whether the
    gate is stopped (mu = 0) or merely slow is a fact about Tom's availability that no artefact in
    the vault currently records.

    WHAT THE ARITHMETIC IMPLIES, stated plainly:
      1. rho ~= 1.14 (range 0.91-1.36). The lane is at or past the stability boundary.
      2. There is no clearance date under the point estimate. The best case in the declared
         intake range is ~219 days of uninterrupted surplus, and that case is one item per day
         from instability.
      3. The 219 is not a backlog. It is the accumulated integral of a starved lane under a
         strict-priority discipline that the arithmetic says will keep starving it.
      4. Every lever inside the schedule is exhausted. The two remaining levers are ADMISSION
         CONTROL (bound lambda — available, because the enqueue stream is generated by C2A2's own
         agents and is not exogenous) and SERVICE RATE (raise mu — runs/day, parallelism, batch
         size). This is PREMISE-106 corollary (ii), restated with today's numbers.
      5. If neither lever moves, the honest report is not "backlog, one day worse" but
         "steady-state non-coverage of the re-trigger lane at approximately 1.5 items/day of
         accretion" — which is a policy statement requiring a decision, not a status line.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-807
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by performing the service-rate arithmetic the run declined to perform and
           asking what the resulting number makes of the word "backlog."
      15a: Searched for supporting literature on the corrective proposition AND performed the
           arithmetic explicitly at the queue's instruction.
    Current status: SUPPORTED

  REGISTER CHECK (performed BEFORE writing this file):
    Grepped `validated_premises.md` for: queue, backlog, throughput, little's law, utilis/utiliz,
    admission control, steady state, arrival rate, service rate, bottleneck.
    Found and read in full:
      - **PREMISE-106** (2026-07-20, ACTIVE, High confidence) — THE DECISIVE OVERLAP, and it is
        near-total at the level of principle. It already holds that "the lit-search pipeline's
        queue is in the unstable regime: at ~12 items serviced per run against a daily enqueue
        rate, arrival exceeds service and the backlog grows without bound. This is a proved
        queueing result, not a hypothesis, and no scheduling discipline recovers it." It already
        holds corollary (i) — an existing backlog drains at the SURPLUS rate, not the service rate,
        so the standing items need separate treatment — and corollary (ii) — arrival and service
        are BOTH decision variables, admission control is available, and bounding arrival is
        sufficient on its own. Re-check was due 2026-08-20; this file arrives five days early and
        functions as that re-check's data.
      - **PREMISE-095** (2026-07-09, ACTIVE, Moderate) — the same finding for the 15d weekly
        re-trigger lane specifically: arrival ~55/week against 7-20 items/run, "the refresh queue
        grows without bound absent a cadence change, admission cap, or throughput/provisioning
        increase," with "structural" explicitly scoped to structural-under-current-provisioning.
        Carries a QUEUED-EMPIRICAL residue: "precise lambda/mu instrumentation still recommended."
      - **PREMISE-070** (2026-06-23, ACTIVE, Moderate) — Theory of Constraints: human review
        throughput is the binding constraint; subordinate other stages to it; do not over-feed
        intake while review is the bottleneck. Entails-against intake-as-progress.
      - **PREMISE-003** (ACTIVE) — human review capacity is the primary constraint on throughput
        and is a documented HITL bottleneck.
      - **PREMISE-102** (2026-07-?, ACTIVE) — fail-loud is reporting, not remediation; a channel
        with demonstrated zero throughput converts repeated identical non-processing into a
        standing policy of non-coverage. This is the review-gate half of the present item.
      - **PREMISE-101** (ACTIVE) — counts over shared artefacts are properties of a (scope, method,
        time) reading, not of the artefact. Directly governs the 219-vs-155-vs-153 discrepancy.
      - **PREMISE-050** (small scoped batches, sized to gate cost), **PREMISE-090** (attended
        passes as one-time remediation only, not standing cadence), **PREMISE-121** (reviewer
        capacity does not scale with production; override rates 49-96%), **PREMISE-138**
        (repetition inside a channel with no effector is not a remedy).
    CONCLUSION OF THE CHECK: **HEAVY OVERLAP. NO NOVELTY-FLAG. The residual is narrow and is
    LEXICAL AND EVIDENTIAL, not queue-theoretic.** PREMISE-106 already holds every theoretical
    clause of the corrective proposition, at High confidence, and PREMISE-095 already holds it for
    this exact lane. What genuinely survives is three things, and a disposition that treats this
    file as new support for "arrival exceeds service" is re-minting PREMISE-106:
      (R1) THE WORD. Neither premise addresses the presupposition carried by the term "backlog."
           14b's contribution is lexical-epistemic: "backlog" presupposes transience, so using it
           asserts rho < 1 without anyone noticing an assertion was made, and it is therefore the
           mechanism by which a proved result (PREMISE-106) coexists undisturbed with twelve days
           of "one day worse" reporting. That is a claim about how a validated premise fails to
           reach the prose, and it is PREMISE-123's know-do gap instantiated in a single noun.
      (R2) THE NUMBERS. PREMISE-095 carries an explicit QUEUED-EMPIRICAL residue for precise
           lambda/mu instrumentation. The arithmetic block above discharges part of it with dated
           figures, and updates the standing backlog figure from 147 (PREMISE-106) to 219.
      (R3) THE PRIORITY MECHANISM. Neither premise contains the two-class strict-priority result.
           PREMISE-106 says "no scheduling discipline recovers it"; it does not say WHY the
           re-trigger lane specifically is the one that starves, nor that the starvation is
           predicted rather than chosen. The W_L divergence result supplies that, and it changes
           the reading of DEFECT-I non-compliance from an agent lapse to a structural consequence.
    DECLARED LIMITATION: this register check is a string grep, measured at five-of-nine recall by
    the 2026-08-14 15c run (ASSUMPTION-1052 — ~56%). The list above is a **LOWER BOUND**. The
    replacement pre-queue register check ASSUMPTION-1052 requires has not been built; the same
    grep was used here as was used for queueing.

  Supporting evidence found: Yes

  Sources:
    1. Wilson, G. (2026), "Priority Starvation," Third Bit (third-bit.com, 2026-06-05; originally
       written for marimo.io). — Supplies the exact mechanism for the fifth-consecutive-cycle
       starvation, with the formula. For a non-preemptive two-class priority queue,
       W_L = R0 / [(1 - rho_H)(1 - rho_H - rho_L)], and the source states explicitly that this
       "diverges as rho_H -> 1 independently of rho_L. As rho_H approaches 100%, low-priority jobs
       wait arbitrarily long, EVEN IF ONLY A FEW LOW-PRIORITY JOBS EVER ARRIVE." It further notes
       that starvation occurs at MODERATE total load — "even when rho < 1, randomness creates
       bursts of H arrivals" — so the effect does not require rho_total >= 1 and is therefore
       robust to the low end of C2A2's intake band. Also names the standard remedy (priority
       aging with a maximum patience time T_max, capping worst-case wait) and its cost (promotion
       events spike effective rho_H and produce oscillating rather than smooth service), which is
       the closest thing in this file to an actionable in-house design. [VERIFIED this run — page
       fetched and read in full; formulas, the divergence statement, and the aging trade-off
       quoted directly. EXPOSITORY, not primary research: it is a teaching article restating the
       standard M/G/1 non-preemptive priority result. Cited for the RESULT, which is textbook
       (Kleinrock 1976, Vol. II), not for originality.]
    2. Abate, J. & Whitt, W., "Asymptotics for M/G/1 low-priority waiting-time tail probabilities,"
       Queueing Systems (Springer). — The research-grade version of source 1: for the classical
       M/G/1 queue with two priority classes under both non-preemptive and preemptive-resume
       disciplines, the low-priority steady-state waiting time is characterised as a geometric
       random sum. Establishes that the low-priority tail is a studied object with known heavy
       behaviour, not a folk observation. [SNIPPET LEVEL — journal listing and abstract located
       this run; paper NOT read. Cited only for the existence and standing of the result.]
    3. Little, J.D.C. (1961), "A Proof for the Queuing Formula: L = lambda W," Operations Research
       9(3):383-387; and Hopp, W. & Spearman, M., Factory Physics (rho > 1 implies unbounded
       backlog). — The stability condition and the conservation relation. Load-bearing caveat for
       this file: Little's law is a steady-state identity, so its correct use here is to show that
       NO finite mean residence satisfies it at rho >= 1, not to compute a wait. [CANONICAL, cited
       from established knowledge and from the register's own prior citation in PREMISE-095; NOT
       re-verified this run. These are the same sources PREMISE-095 and PREMISE-106 already rest
       on, so this file adds no independent citation weight on the stability clause.]
    4. Goldratt, E., Theory of Constraints (via ASQ / leanproduction.com summaries) — locate the
       constraint where WIP accumulates and subordinate other stages to it; do not feed intake
       ahead of the bottleneck. — The management-side statement of the same result and the source
       of the admission-control remedy in its non-mathematical form. [CANONICAL, cited from the
       register's own prior use in PREMISE-070; NOT re-verified this run.]
    5. NEGATIVE RESULT, reported because its absence is informative: no literature was located
       this run on the LEXICAL claim (R1) — that the vocabulary used for a queue encodes a
       stability assumption, and that using the word "backlog" for a rho >= 1 lane suppresses the
       decision the arithmetic demands. Searches on queueing-theory vocabulary, on "backlog" as a
       term of art, and on framing effects in operational reporting returned nothing on point.
       See NOVELTY note below.

  Strength of support: **Strong** on the queueing clauses (i)-(iv); **None** on the lexical
  residual (R1).

  Summary: Every mathematical clause of the corrective proposition is not merely supported but
  proved, and — decisively for disposition — already held in this register at High confidence as
  PREMISE-106 and at Moderate as PREMISE-095. The arithmetic performed above puts today's numbers
  to it: rho ~= 1.14 against a stability requirement of rho < 1, with the whole point estimate and
  most of the declared intake range on the unstable side, and a best case (rho = 0.91) that sits
  one item per day from instability and would still need ~219 days of uninterrupted surplus. The
  "twenty cycles of exclusive service" figure is arithmetically correct and operationally void: it
  moves 219 items from one lane to another while the vacated lane accrues ~250, leaving the total
  slightly worse. Total work in system obeys W(t) = 219 + 1.5t and is invariant under every
  scheduling choice available inside the pipeline. The strict-priority result explains what
  PREMISE-106 left unexplained: the re-trigger lane starves not by an agent's choice or by
  DEFECT-I non-compliance but by construction, because W_L diverges as rho_H -> 1 independently of
  how few re-trigger items arrive — so five consecutive cycles of intake-first service is the
  configuration's predicted output, and a sixth is not new information. The item's own conclusion
  therefore holds: at rho >= 1 the queue depth carries no information about urgency, because depth
  is then a function of elapsed time rather than of anything anyone did or failed to do, which is
  precisely why twelve days of "one day worse" have changed nothing. What the literature does NOT
  supply is the item's most interesting move — the claim that the noun "backlog" is itself the
  carrier of the unexamined stability assumption. That was searched for and not found.

  Caveats:
    (a) EVERY INPUT IS A SELF-REPORT AND ONE IS KNOWN CONTESTED. The 219 figure disagrees with 155
        (08-13) and 153 (08-12) by a factor that cannot be intake; the queue itself records the
        discrepancy as unresolved and declines to arbitrate it (PREMISE-101, PREMISE-161;
        ASSUMPTION-1072). The arithmetic above is therefore CONDITIONAL ON A CONTESTED L. It is
        worth stating exactly how much this matters: **it barely matters at all.** rho = lambda/mu
        does not contain L. Whether the lane holds 153 or 219 items changes the clearance estimate
        and changes nothing about stability. If L is wrong, the conclusion survives; if lambda or
        mu is wrong, it does not. That asymmetry should be carried forward, because the vault's
        measurement attention is currently on L — the quantity that does not decide the question.
    (b) mu AND lambda ARE UNINSTRUMENTED, AND THIS IS THE REAL GAP. PREMISE-095's QUEUED-EMPIRICAL
        residue ("precise lambda/mu instrumentation still recommended") was filed 2026-07-09 and
        remains open. "~11 per cycle" and "~10-15 nightly" are recollected magnitudes, not counter
        readings. The whole finding turns on a ratio of two numbers neither of which is measured
        by an instrument. The honest status of rho ~= 1.14 is ORDER-OF-MAGNITUDE, and the useful
        precision claim is weaker but sufficient: rho is not comfortably below 1, and no available
        evidence puts it there.
    (c) THE POISSON/M-G-1 IDEALISATION DOES NOT HOLD HERE. The starvation formula assumes
        stochastic arrivals and a work-conserving single server. C2A2's intake is BATCHED and
        DETERMINISTIC (a nightly EOD dump), and the "server" is an agent run with a token budget,
        not a queue with a service-time distribution. What transfers robustly is the CONSERVATION
        argument (clause ii) and the SATURATION argument (clause iii's qualitative form), both of
        which are distribution-free. What does NOT transfer is any quantitative W_L; do not quote
        a predicted waiting time from source 1's formula.
    (d) rho > 1 IS NOT ITSELF A FAULT, AND THIS FILE MUST NOT BE READ AS SAYING IT IS. A deliberate
        policy of "search the newest items and let the old ones expire" is a legitimate design with
        a name (TTL / admission control / value-decay triage), and it may well be the right one for
        re-trigger items whose value decays. PREMISE-106 corollary (i) already proposes a TTL sweep.
        The defect 14b identifies is not the instability; it is that the instability is UNNAMED and
        is therefore being reported in vocabulary that implies its opposite. The remedy is a
        declared policy, not necessarily a larger budget.
    (e) THE SOURCES ADD LITTLE INDEPENDENT WEIGHT. Sources 3 and 4 are the same citations PREMISE-095
        and PREMISE-106 already rest on. Only source 1 is new to the register, and it is expository
        rather than primary. This file's contribution is the ARITHMETIC and the priority mechanism,
        not a new evidence base, and should be weighted accordingly at disposition.
    (f) PER PREMISE-124: the arithmetic above is a self-measurement of the pipeline by the pipeline.
        It has no external baseline. Its numbers are UNCALIBRATED in that premise's sense and are
        offered as such.

  NOVELTY NOTE (not a full NOVELTY-FLAG):
    Item: PRESUMPTION-807, residual clause (R1) only.
    Searched: queueing-theory terminology and its presuppositions; "backlog" as a term of art in
      operations; framing/vocabulary effects in operational status reporting; whether a queue's
      descriptive noun encodes a stability assumption.
    Finding: no literature located that treats the DESCRIPTIVE VOCABULARY of a queue as carrying
      a testable stability claim. The queueing literature distinguishes stable from unstable
      regimes precisely; it does not appear to study the practitioner-language failure in which a
      term presupposing stability is applied to an unstable system and thereby suppresses the
      decision.
    Implication: possibly an original small contribution, in the same family as PREMISE-105
      (definitional change breaks a series) and PREMISE-101 (a count is a property of a reading).
      The general form: A NOUN CAN CARRY AN UNASSERTED MODELLING CLAIM, AND WHEN IT DOES, THE CLAIM
      IS UNFALSIFIABLE BY THE PEOPLE USING THE NOUN.
    Recommended status: NOT flagged NOVEL outright — the search was narrow (one direction, one
      run) and the concept is close enough to Goodhart/framing/reification literature that a
      broader search may well find it. Carried as a lead.

  Search scope: COMPREHENSIVE and DECISIVE on the mathematics, because the mathematics is settled
  and already register-held — no further search on stability, Little's law, or admission control is
  warranted and 15d should not re-queue it. GOOD on the strict-priority starvation result, verified
  at expository level with a research-grade pointer. NOT SEARCHED, and each would strengthen this:
  (i) the fluid/heavy-traffic limit literature, which gives the rate at which W diverges and would
  turn "grows without bound" into a dated projection with a confidence band; (ii) TTL/value-decay
  triage and expiry policy for stale review items, which is the concrete remedy PREMISE-106 names
  and nobody has designed; (iii) priority aging as a C2A2 mechanism — source 1 gives the design and
  its cost, and a T_max on re-trigger items is a small, testable change. NOT SEARCHED AND
  DELIBERATELY SO: the general HITL-bottleneck literature, already held as PREMISE-003/070/121.

  Recommendation: **SUPPORTED (Strong)** for the corrective proposition; equivalently
  NO-SUPPORT-FOUND for the presumption as worded. But the disposition-worthy content is NOT the
  support — it is PREMISE-106, minted five days shy of its re-check, restated with today's numbers
  and with a mechanism it lacked. Three concrete carries:
    1. RHO IS ~1.14 (range 0.91-1.36). Report it. The lane has no clearance date under the point
       estimate and a ~219-day best case at the edge of its range.
    2. THE STARVATION IS PREDICTED, NOT CHOSEN. Five consecutive intake-first cycles is what a
       strict-priority discipline at rho_H near 1 produces. DEFECT-I compliance would not change
       the total; it would change which lane starves. Any remediation aimed at the scheduler is
       aimed at the wrong object.
    3. THE CHEAP INSTRUMENT, since the arithmetic is now done: PREMISE-095's open lambda/mu
       instrumentation is a two-counter change — items enqueued per night, items served per night,
       both dated. Thirty days of that turns rho ~= 1.14 into a measured quantity with an interval,
       and it is the only thing on this list that the fleet cannot already infer. Caveat (b) is the
       reason to do it: the finding currently rests on two unmeasured numbers.

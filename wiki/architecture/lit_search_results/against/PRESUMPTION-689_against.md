SEARCH-AGAINST-PRESUMPTION-689:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-689
  Original statement: That a task specification is satisfiable; ten days of budget-breach
    disclosures treated the breach as the run's fault until one run measured that the
    mandatory preamble alone exceeds the ceiling.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-689
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b inferred from one run inverting a claim ten prior runs made in the opposite
        direction.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Porter, J., Boyd, C., Skandari, M.R. and Laiteerapong, N. "Revisiting the Time Needed
       to Provide Adult Primary Care." Journal of General Internal Medicine (DOI 10.1007/
       s11606-022-07707-x; PMC9848034; author list, journal and DOI confirmed this session —
       year given variously as 2022 online-first and 2023 in issue, so cited without a firm
       year). Using 2020 NHANES data and a modelled 2,500-patient panel, the authors computed
       that fully complying with USPSTF preventive guidance plus chronic, acute and
       documentation work would require 26.7 hours per physician per day. This is the exact
       structural situation of PRESUMPTION-689 and it is the cleanest published instance: the
       mandatory component alone exceeds the ceiling, so every practitioner is in permanent
       breach, and for years the shortfall was attributed to individual practitioners rather
       than to the specification. Critically, the same paper shows the shortfall is
       *measurable in advance* — nobody needed ten days of breach reports; a single arithmetic
       pass over the mandatory list was sufficient. Note also that the authors show
       team-based delegation reduces the physician requirement to 9.3 hours/day, i.e. the
       repair is architectural, not effort-based.
    2. Vaughan, D. — the normalisation of deviance (concept and its origin in her analysis of
       the 1986 Challenger launch decision confirmed this session; the monograph's exact title
       and year were not confirmed — [UNVERIFIED — book citation not confirmed this session]).
       The defining mechanism: in the absence of perceived loss or harm, deviant practice
       becomes the accepted standard. Applied here, ten consecutive days in which breach was
       disclosed, attributed to the run, and produced no correction is the normalisation
       window. The literature's warning is that the *signal value* of the compliance report
       collapses first: once every run breaches, "breached" stops discriminating between a run
       that overran by 2% and one that overran by 200%, and the disclosure becomes ritual.
    3. "A qualitative systematic review on the application of the normalization of deviance
       phenomenon within high-risk industries," ScienceDirect S0022437522001827 (2022;
       journal inferred from the publisher identifier as Journal of Safety Research —
       [UNVERIFIED — journal title not confirmed this session]; author list not confirmed).
       Synthesises the cross-industry evidence. The finding that bears directly on C2A2:
       rule deviations are "virtually always a response to production pressures," and
       operators invent workarounds when a rule seems irrational or impossible — with the
       consequence that "the system itself always runs in a degraded mode." A ceiling that
       cannot be met does not produce compliance; it produces undocumented local adaptation
       that the specification cannot see.
    4. Work-as-imagined versus work-as-done, resilience-engineering framing (confirmed this
       session via the normalisation-of-deviance literature, which explicitly connects the two;
       the primary Hollnagel sources were not opened — [UNVERIFIED — primary citations not
       confirmed this session]). The relevant claim is that persistent divergence between the
       specified task and the executed task is diagnostic of a specification defect, not of
       operator failure, and that the correct investigative move on observing universal
       deviation is to measure the specification's feasibility rather than to audit the
       operators. Ten runs audited the operator. The eleventh measured the specification, and
       found the defect immediately.
    5. Real-time systems admission control and schedulability testing (Springer, Real-Time
       Systems, "Utilization-Based Admission Control for Scalable Real-Time Communication,"
       title and journal confirmed this session; see also QPA schedulability analysis for EDF,
       www-users.york.ac.uk/~ab38/QPA.pdf). Constitutes the constructive counter-practice: in
       systems where deadline feasibility matters, feasibility is tested *at admission*, before
       execution, and infeasible task sets are rejected rather than dispatched. The standard
       design uses a cheap utilisation-based test to reject obviously infeasible requests fast,
       with an exact test as a refinement. The mandatory-preamble-versus-ceiling check is
       exactly a utilisation-based test: sum the fixed cost, compare to the budget, refuse to
       admit. Its absence in C2A2 is a missing admission gate, not an unavoidable condition.

  Strength of challenge: Strong

  Summary: The presumption that a task specification is satisfiable is challenged decisively
    and from an unusually close analogue: the primary-care time-budget literature is the same
    failure with the same shape, where a mandatory list provably exceeds the available budget
    and the shortfall was attributed to practitioners until someone summed the requirement.
    The safety literature explains the ten-day pattern — universal violation normalises, the
    compliance signal loses discriminating power, and adaptation moves off the record. The
    real-time systems literature supplies the fix and shows it is cheap: feasibility is
    testable at admission with a simple utilisation comparison, and infeasible specifications
    should be refused rather than dispatched and later blamed. Nothing found this session
    supports treating universal breach as evidence about the runs. The one genuine nuance is
    that a small, bounded overrun can be a legitimate design choice (soft deadlines), which the
    steelman develops.

  STEELMAN:
    Strongest counterargument: A ceiling that is routinely exceeded is not necessarily a
      defective specification — it may be a deliberately aspirational one. Budgets in many
      systems are set as *soft* targets precisely because a hard, always-satisfiable ceiling
      would be set so loosely that it exerts no pressure at all; the soft-real-time literature
      formalises this as accepting a bounded deadline-miss ratio rather than demanding
      feasibility. On this reading, the ten disclosures were doing their job: they created
      pressure toward brevity, and the fact that the mandatory preamble alone exceeds the
      ceiling tells you the preamble is too long, not that the ceiling is wrong. There is also
      an ordering objection to 14b's inference: one run measuring the preamble is a single
      measurement, and the earlier ten may have been correct that *their* specific overruns
      were attributable to avoidable verbosity on top of an admittedly tight but not
      structurally impossible base.
    What would need to be true for C2A2 to be safe: (a) the ceiling is explicitly labelled
      soft, with a stated tolerable breach ratio, so that "breached" is not read as a fault
      report; (b) the mandatory floor is measured and published, so every run knows how much of
      the budget is discretionary before it starts; (c) the discretionary headroom is
      non-trivial — if floor >= ceiling, no labelling saves it; (d) breach disclosures are
      attributed correctly, i.e. they report overrun *relative to the floor*, not relative to
      zero; (e) there is a route by which a measurement of infeasibility changes the
      specification, rather than being absorbed as another disclosure. The ten-day history
      suggests (e) is the binding failure: the register recorded the breaches but had no
      channel to the ceiling.
    How to test: Directly measurable in this vault. Compute the token/word cost of the
      mandatory preamble as it is actually delivered to runs, and compare it to the stated
      ceiling; report floor/ceiling as a ratio. Then, over all budget-breach disclosures on
      record, extract the claimed cause and classify as (i) attributed to the run's own
      verbosity, (ii) attributed to the specification, (iii) unattributed. If the ratio in the
      first computation is >= 1.0 while class (i) dominates the disclosures, the presumption is
      confirmed operative and the misattribution is quantified. A second check: whether any
      change to the ceiling or the preamble followed any disclosure — if the answer is none
      across all disclosures, there is no feedback channel and the disclosures are ritual in
      the normalisation-of-deviance sense.

  Specific risks: If specifications are not guaranteed satisfiable, three things break. First,
    attribution: every breach report misassigns cause, so the corrective effort is spent on the
    wrong object and the actual defect persists indefinitely — ten days here, and there is no
    bound on how long it could have been. Second, signal degradation: once breach is universal,
    the disclosure carries no information, so a genuinely anomalous overrun becomes invisible
    among the routine ones; this is the alarm-fatigue endpoint and it removes the system's
    ability to detect the failure it was built to detect. Third, hidden adaptation: the
    safety literature is emphatic that operators facing impossible rules do not fail loudly,
    they improvise quietly, so runs may already be silently truncating, skipping or
    reinterpreting mandatory elements in ways that no disclosure records. That third risk is
    the one that compounds — it means the vault's record of what runs did may itself be
    unreliable, and unreliable in an undocumented direction.

  Mitigations available: (1) Admission-time feasibility gate: compute mandatory floor versus
    ceiling before dispatch and refuse or re-scope infeasible tasks, exactly the
    utilisation-based admission test. (2) Publish the floor alongside the ceiling in every task
    spec, so breach can be reported against headroom rather than against zero. (3) Re-label
    soft ceilings explicitly and state a tolerable breach ratio, so that the disclosure means
    something when it fires. (4) Escalate on universality: a rule that instruments the *rate*
    of breach and raises a specification-defect ticket when the rate approaches 100%, since
    universal violation is the diagnostic. (5) Require every breach disclosure to carry an
    attribution field with an explicit "specification" option, so the eleventh run's finding
    would have been representable on day one. (6) Team-based decomposition, the analogue of the
    primary-care fix: move mandatory content out of the per-run preamble into shared or
    reference-linked material so the per-run floor drops.

  Search scope: Comprehensive for the three most relevant framings — unachievable procedural
    requirements with a quantified analogue (primary-care time budgets), normalisation of
    deviance and compliance-signal degradation (safety science), and pre-execution feasibility
    verification (real-time admission control). Preliminary on two adjacent bodies:
    alert/alarm fatigue in clinical decision support, which would strengthen the
    signal-degradation argument with effect sizes, and the legal-compliance literature on
    unenforceable rules and legitimacy (Tyler and successors), which would strengthen the
    argument that impossible rules erode compliance with *achievable* rules in the same
    system. Broader search recommended on both if the systemic argument is to be pressed.

  Recommendation: CHALLENGED

SEARCH-AGAINST-PRESUMPTION-1117:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1117
  Original statement: [inferred] Precedent from earlier unattended runs is treated as authority that
    can override task text, with no ratification step. Question: when do repeated unattended
    deviations become de facto policy, and what review step prevents silent drift?
  Under test: the implied correction that precedent-based deviation is drift (normalisation of
    deviance) and needs a ratification step. I searched for evidence that adaptation from practice is
    necessary or beneficial (Safety-II, resilience engineering), and that added ratification or
    compliance steps backfire (bureaucratic overhead, "safety clutter").

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1117
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-09): Inferred from run behaviour that prior unattended-run precedent is used to
        override task text without ratification; queued with drift/review-step question.
      15b (2026-10-10): Searched for challenging literature. 3 searches (Dekker 2003 procedures vs
        adaptation; "safety clutter"; Safety-II performance variability vs normalisation of
        deviance); 2 fetches (Dekker 2003, full text; PSL Hub summary of Rae et al. 2018, abstract-
        level). No fetch failures.
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One full-text paper; one abstract-level summary; rest search-result.

  Search scope: preliminary (3 searches, 2 fetches).

  Challenging evidence found: Partial
  Strength of challenge: Moderate

  Sources:
    1. Dekker S. 2003. "Failure to adapt or adaptations that fail: contrasting models on procedures
       and safety." Applied Ergonomics 34:233-238. doi:10.1016/S0003-6870(03)00031-0. [fetched, full
       text] "Not following procedures does not necessarily lead to trouble, and safe outcomes may be
       preceded by just as (relatively) many procedural deviations as those that precede accidents."
       "Increasing the pressure to comply increases the probability of failures to adapt." "Rules
       emerge from practice and experience rather than preceding them." Remedy: "Monitor the gap
       between procedure and practice and try to understand why it exists (and resist trying to close
       it by simply telling people to comply)." Bearing: a direct challenge to treating deviation from
       task text as presumptively drift. Precedent-based adaptation is often how the system copes with
       inadequate instructions. HONEST COUNTER IN THE SAME SOURCE: Dekker also describes normalisation
       of deviance ("Past success is taken as guarantee of future safety... Departures from the
       routine become routine"). He does not claim adaptation is safe. He claims a compliance step
       alone is the wrong fix.
    2. Rae A, Provan D, Weber D, Dekker S. 2018. "Safety clutter: the accumulation and persistence of
       'safety' work that does not contribute to operational safety." Policy and Practice in Health
       and Safety 16(2):194-211. doi:10.1080/14773996.2018.1491147. [fetched, abstract-level summary
       via PSL Hub] Clutter results from duplication, generalisation and over-specification, and is
       driven by "asymmetry between the ease ... of adding ... safety activities, and the difficulty
       ... of reducing or removing" them. It produces "cynicism and 'surface compliance'". Bearing:
       a ratification step added to every precedent-based choice is exactly the kind of easily added,
       rarely removed safety work that turns into rubber-stamping.
    3. Hollnagel E, Wears RL, Braithwaite J. 2015. "From Safety-I to Safety-II: A White Paper." (NHS
       England-hosted PDF). [search-result] "everyday performance variability provides the
       adaptations that are needed to respond to varying conditions, and hence is the reason why
       things go right." Bearing: in Safety-II framing, unattended agents adapting from precedent is
       the source of success, not a pathology.
    4. Leveson N. 2020. "Safety III: A Systems Approach to Safety and Resilience" (MIT). [search-
       result] A sharp critique of Safety-II. Recorded as a counter-to-the-counter: the "variability
       is good" claim is itself contested.
    5. UK accident-investigation presentation on Safety-II (gov.uk PDF). [search-result] Open
       question: "How do we know when variability is adaptive and when it is maladaptive?" Bearing:
       this names the unresolved boundary.

  Summary: Resilience-engineering literature gives a real challenge to the premise that
    precedent-over-text is presumptively drift needing ratification. Deviations precede safe outcomes
    as often as unsafe ones. Practice often precedes and corrects procedure. Compliance pressure
    increases failures to adapt. Added review steps tend to accumulate into clutter and surface
    compliance. However, the same sources (Dekker 2003 explicitly) describe the normalisation-of-
    deviance mechanism the item worries about. Their remedy is not "no review" but "monitor and
    understand the gap", not "add a gate". So the challenge is to the FORM of the correction (a
    ratification gate) more than to the diagnosis.

  Specific risks: (a) A ratification gate in an unattended pipeline with no human present may become
    a rubber stamp, or block all useful adaptation. (b) Forcing task-text compliance where task text
    is stale makes failures to adapt more likely.

  Mitigations available: Gap-monitoring instead of gating: log each precedent-over-text choice with
    the precedent cited, and periodically review the accumulated gap (Dekker's charter). Set sunset
    or expiry on precedents so that clutter does not accumulate.

  STEELMAN:
    Item: PRESUMPTION-1117
    Strongest counterargument: Task text is work-as-imagined, and precedent is work-as-done. In
      complex systems, safe outcomes depend on agents adapting instructions to circumstances that the
      instructions did not anticipate. Rules mostly follow practice, not the reverse. A ratification
      step does not remove the double bind between failing to adapt and adapting badly. It shifts the
      criterion toward failure-to-adapt, and in an unattended system it either stalls or becomes a
      formality. The safety-clutter literature predicts such a step will be added easily and never
      removed. What is needed is visibility of the gap, not a gate.
    What would need to be true for C2A2 to be safe: Precedent-based deviations are logged with their
      justification, and someone (human or agent) periodically reviews the cumulative gap and either
      updates the task text or reverses the precedent.
    How to test: Audit past precedent-over-text deviations. Classify each as adaptive (task text was
      stale or wrong) or maladaptive (precedent drifted from intent). A high adaptive share supports
      the challenge.

  Boundary conditions identified:
    - Safety-II benefits assume skilled adapters with feedback on outcomes. Unattended agents copying
      their own earlier unattended choices may lack that feedback loop. This is the self-referential
      case Dekker's "past success as guarantee" warns about.
    - Ratification overhead is a cost mainly when reviewers are scarce. A cheap, periodic gap review
      is not "clutter".
    - Safety-II itself is contested (Leveson 2020).

  Recommendation: PARTIALLY-CHALLENGED
  SYSTEMIC-RISK: see flag below (shared with 1115, 1118, 1119).

  SYSTEMIC-RISK-FLAG:
    Date: 2026-10-10
    Affected items: ASSUMPTION-1757, PRESUMPTION-1115, PRESUMPTION-1117, PRESUMPTION-1118,
      PRESUMPTION-1119
    Common vulnerability: Each implied correction is a binary rule plus added process (count 1 not 2;
      silence = unknown; deviation needs ratification; verdict needs UNKNOWN state; normalisation must
      be disclosed). The literature in each case favours graded, documented approaches (effective n;
      sensitivity-weighted absence; gap monitoring; scoped and actionable alerts; keep as-extracted
      plus consensus with an audit note). It also warns that added meta-process accumulates and
      becomes ignored ("safety clutter", alert fatigue, surface compliance), especially when no human
      reads it. Five corrections at once to an unattended pipeline is itself a clutter risk.
    Literature basis: Rae et al. 2018; Dekker 2003; Buscemi et al. 2006; Kale, Kay & Hullman 2020;
      Cochrane Handbook 5.1 §7.6.5; COPE 2020 survey.
    Risk level: High
    Recommendation: Prefer one shared mechanism (logging the raw output plus a transformation and
      scope record) over five separate gates. Review the added process for removal as well as
      addition.

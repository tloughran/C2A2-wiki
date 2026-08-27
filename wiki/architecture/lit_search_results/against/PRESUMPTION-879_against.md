SEARCH-AGAINST-PRESUMPTION-879:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-879
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-879 (Priority High)
  Original statement: [inferred] That an agent's remit boundary marks the place where a known defect
    stops being anyone's problem — that declining a correct fix on remit grounds discharges the
    agent's responsibility for it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-879
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three independent same-day instances of declining a fix the agent had already
           diagnosed. High confidence — the pattern is stated three times in the agents' own words;
           only the reading of it as a presumption is inferred. Not an accusation: each agent followed
           its definition exactly.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Four WebSearch queries executed 2026-08-26, plus one on human-in-the-loop escalation
    with an absent approver. Literatures reached: (a) social-psychological diffusion of responsibility
    and the bystander effect; (b) the philosophical/AI-ethics "problem of many hands" and
    responsibility-gap literature; (c) organisational safety-voice and safety-listening research;
    (d) the empirical multi-agent LLM failure-taxonomy literature (MAST); (e) practitioner guidance
    on HITL escalation design. Venues reached: arXiv (cs.AI, cs.MA), Springer (AI & Ethics, Topoi),
    Wiley (Risk Analysis), NeurIPS 2025 poster listing, Britannica/Wikipedia for concept definitions,
    industry blogs for the HITL material.
    NOT COVERED, and these matter: (i) Latané & Darley's primary experimental work — I reached it only
    through encyclopaedia summaries, so the effect-size and moderator details are second-hand;
    (ii) the *ownerless bug* / bug-triage-latency literature in empirical SE, which would give
    quantitative base rates for how long a diagnosed-but-unassigned defect survives and is the closest
    quantitative analogue to C2A2's situation; (iii) the aviation/CRM literature on cross-boundary
    intervention (the "assertive subordinate" tradition), which is the strongest *pro-intervention*
    body of practice and would likely raise this to Very Strong; (iv) Thompson's original "problem of
    many hands" (1980, *American Political Science Review*) in primary form. Search confidence:
    MODERATE-HIGH. One important caveat on scope: most of the diffusion-of-responsibility literature
    concerns *ambiguous* responsibility among peers, whereas C2A2's case is *explicitly assigned*
    responsibility to an unresponsive party — a boundary condition I flag in the steelman.

  Challenging evidence found: Yes

  Sources:
    1. Cemri, Pan, Yang et al. 2025. "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657
       (NeurIPS 2025). https://arxiv.org/abs/2503.13657 — The most directly transferable source. MAST
       is built from 1,600+ annotated execution traces across 7 multi-agent frameworks, six expert
       annotators, Cohen's κ = 0.88. Two findings bear on this item. First, "Specification and System
       Design" issues account for ~41.8% of all failures, and the category explicitly includes
       *ambiguous role definitions* and *disobeying role specification* — i.e. the remit boundary is
       itself a top-ranked failure surface in multi-agent systems, not a neutral organising device.
       Second, "Task Verification and Termination" accounts for 21.3%, of which incomplete
       verification is 8.2% and premature task ending 6.2%: an agent that diagnoses a defect and then
       terminates without fixing or ensuring the fix is a recognised, quantified failure mode.
       Author names taken from the search result's rendering of the PDF byline; affiliations and full
       author list unverified. ABSTRACT-ONLY plus search-surfaced taxonomy percentages; I did not read
       the full paper.
    2. [authors unverified — the phrase and framing are standard; primary attribution is Dennis
       Thompson 1980, not confirmed in this search]. "Many hands make many fingers to point:
       challenges in creating accountable AI." AI & Society.
       https://www.researchgate.net/publication/355955010 — Documents the mechanism by role:
       "engineers and computer scientists may see their responsibility as focused on the quality and
       safety of a particular product rather than on larger scale social issues," while each adjacent
       role expects a different one to own the residual. Every actor is behaving correctly within
       their remit and the defect is owned by none of them. ABSTRACT-ONLY (paywalled).
    3. [authors unverified]. 2025. "Beyond the Responsibility Gap: Distributed Non-anthropocentric
       Responsibility in the AI Era." Topoi.
       https://link.springer.com/article/10.1007/s11245-025-10302-4 — Argues that in agentic systems
       "responsibility, control, and knowledge are fragmented, leaving no participant with a complete
       view of, or responsibility for, the resulting risks." This is the formal statement of what
       C2A2's three same-day declinations produce. ABSTRACT-ONLY.
    4. Latané & Darley [primary work not reached]; summarised at
       https://www.britannica.com/topic/bystander-effect/Diffusion-of-responsibility and
       https://en.wikipedia.org/wiki/Diffusion_of_responsibility — The core finding: as the number of
       parties who could act increases, the personal responsibility each feels decreases, and the
       standard mitigations are "reducing group size, defining clear expectations, and increasing
       accountability." Note the third mitigation is *accountability*, not *boundary clarity* — C2A2
       has boundary clarity in abundance and accountability for the residual in none. SNIPPET-ONLY
       (tertiary sources).
    5. Pandolfo et al. [first names unverified]. 2025. "Safety Listening in High-Risk Situations: A
       Qualitative Analysis of Responses to Safety Voice in Aviation." Risk Analysis.
       https://onlinelibrary.wiley.com/doi/full/10.1111/risa.70106 — Shifts the burden from the
       speaker to the listener: "safety voice often fails when listeners ignore, misunderstand, or
       dismiss concerns." C2A2's three agents all *voiced* correctly. The failure, on this literature,
       is located at the unresponsive gate, which means the remit rule is not self-sufficient — its
       correctness is conditional on a party outside the agent's control. ABSTRACT-ONLY.
    6. [no author — industry guidance]. "Human-in-the-Loop Governance for AI Agents." Arthur.
       https://www.arthur.ai/column/human-in-the-loop-governance-for-ai-agents — States the design
       rule C2A2 lacks: escalation should "route by risk, deny by default on timeout, and tune gates
       so they fire only when a human is genuinely needed," and warns that organisations discover
       "absent governance — no clear escalation path, no assigned approver, no feedback mechanism."
       The critical clause is *deny by default on timeout*: a handoff with no timeout semantics is not
       a handoff. Practitioner source, not peer-reviewed. SNIPPET-ONLY.
    7. [no author — practitioner]. "Understanding and fighting alert fatigue." Atlassian.
       https://www.atlassian.com/incident-management/on-call/alert-fatigue — Included for the
       adjacent mechanism: an item that recurs and is never actioned trains its readers to stop
       reading it. C2A2's Day 76 fidelity failure has now been read past by two agents who both knew
       the fix. SNIPPET-ONLY.

  Strength of challenge: Strong

  Summary: The literature does not merely fail to support the presumption; it names the presumption's
  consequence as a distinct, well-studied failure. The diffusion-of-responsibility tradition
  establishes that a defect visible to many and owned by none goes unfixed, and the standard
  mitigations it prescribes are clear expectations *and accountability* — C2A2 has implemented the
  former with unusual rigour (every agent definition carries a "What You Do NOT Do" section) and the
  latter not at all for the residual. The AI-specific literature is sharper: the "many hands" and
  responsibility-gap work describes exactly a system in which every actor discharges its role
  correctly and no actor owns the outcome, and MAST — the largest empirical study of multi-agent LLM
  failures, 1,600+ traces, κ = 0.88 — places specification-and-role issues at 41.8% of all failures
  and verification/termination failures at 21.3%, with "incomplete verification" and "premature task
  ending" as named modes. An agent that diagnoses a defect, names the file, predicts the recurrence
  and stops is a textbook instance of premature task ending. The safety-voice literature adds the
  decisive asymmetry: voicing is not the same as being heard, and failures are located at the
  listener. C2A2's own record supplies the empirical instance — three known-correct fixes declined in
  one day, all handed to a gate that has not moved in seventeen days, with the oldest of the three
  defects now eight days old. The presumption's implicit model is a handoff; the observed object is a
  terminus. Rated Strong rather than Very Strong only because I did not reach the CRM /
  cross-boundary-intervention literature or quantitative bug-triage-latency data, either of which
  would supply base rates rather than mechanisms.

  Specific risks: (a) Permanent defect retention — a defect that every agent can see, none is
  authorised to fix, and all correctly escalate is, in the limit, immortal; nothing in the system
  removes it and nothing marks it as un-owned. (b) Silent ageing — the Day 76 fidelity failure
  (ratio 0.610, hard ±25% breach) has aged eight days past two competent readers; no counter tracks
  how many such items exist or how old they are. (c) Read-past habituation — per the alert-fatigue
  mechanism, each pass a competent agent makes over an unfixed known defect lowers the probability
  the next pass treats it as actionable, so the defect becomes progressively less visible while
  remaining formally recorded. (d) Correctness-as-alibi — because each declination is individually
  correct and *documented as correct*, the system produces an audit trail that reads as good practice
  while the aggregate outcome is defect preservation; this makes the failure invisible to any review
  that inspects individual agent behaviour rather than outcomes. (e) It compounds with
  PRESUMPTION-881: the declination is disclosed, and disclosure is currently treated as discharge.
  (f) It compounds with PRESUMPTION-883: every declination adds to the gate that is the reason the
  declinations do not resolve.

  Mitigations available:
    - Add timeout semantics to remit. Condition the boundary on the recipient's responsiveness: if a
      handoff is not acknowledged within N days, the remit rule inverts and the diagnosing agent is
      authorised (or obliged) to act, or the item auto-escalates to a named alternative. This is the
      standard HITL rule ("deny by default on timeout") and it is the single cheapest fix available.
    - Introduce an explicit owner-of-record field on every declined fix, so that "left for you" names
      a party and a date rather than a direction. Un-owned items should be a countable population
      with a visible age distribution.
    - Track and publish handoff age. The metric that would have caught this is trivial: max and median
      age of items in declined-on-remit state. It is currently uncomputed.
    - Distinguish *hard* defects (a ±25% fidelity breach) from *soft* ones and permit remit override
      for the hard class only. This preserves remit discipline as a designed virtue while removing
      its worst failure mode.
    - Per the diffusion literature, add accountability rather than more boundary clarity. C2A2's
      instinct will be to write a sharper "What You Do NOT Do" section; the literature says that is
      the mitigation that does not work.

  STEELMAN:
    Item: PRESUMPTION-879
    Strongest counterargument: Diffusion of responsibility is a finding about *diffuse* responsibility
    — situations where no one has been assigned the task and each bystander infers that someone else
    will act. C2A2's case is its exact opposite: responsibility is unambiguously assigned, to a named
    gate, in writing, with the diagnosis attached. No agent here believed "someone else will handle
    it" as an inference; each correctly identified who owns it. On that reading the boundary is
    working precisely as designed and the failure is entirely located in the gate's non-response,
    which is a resourcing problem, not a design flaw in remit. Further, the alternative is genuinely
    dangerous: an agent authorised to reach outside its remit to fix a defect it diagnosed is an agent
    that can silently rewrite files it does not own on the strength of its own diagnosis — and
    PRESUMPTION-880 supplies live evidence that this system's single-reviewer diagnoses carry a
    plausible directional bias. Remit discipline is what currently prevents an unaudited corrector
    from propagating its own errors across the corpus. Loosening it to fix a seventeen-day queueing
    problem would trade a visible, dated, correctly-attributed defect for an invisible one.
    What would need to be true for C2A2 to be safe: (i) the gate must be genuinely available on a
    timescale shorter than the defects' cost-of-delay — seventeen days of silence against an eight-day
    old hard fidelity breach means this is currently false; (ii) declined items must be *counted and
    aged*, so that gate unavailability is a visible quantity rather than an inference from three
    same-day anecdotes; (iii) the population of declined-on-remit fixes must be bounded, since an
    unbounded one converts remit discipline into a defect reservoir; (iv) no declined defect may be
    load-bearing for downstream work — a fidelity failure that other artefacts cite is not safely
    left standing; (v) if remit is to be loosened for any class, the loosening must come with
    independent verification, or PRESUMPTION-880's risk transfers directly onto it.
    How to test: Fully testable within the existing record and requiring no literature. Enumerate
    every instance in the corpus where an agent diagnosed a defect and declined the fix on remit
    grounds. For each, record the date declined and the date resolved (or "open"). Two statistics
    settle the question: the fraction ever resolved, and the median age of the unresolved set. If the
    resolution fraction is near zero and the age distribution has no upper bound, the boundary is a
    terminus and the presumption is confirmed as a defect-preservation mechanism. A second, sharper
    test: count how many *distinct competent agents* have read past each unresolved item. Day 76 is
    already at two. If that count grows without the item resolving, the read-past habituation
    mechanism is operating and the item's effective visibility is decaying even as its formal record
    persists.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single, currently
      unresponsive human review gate, and not one of the seven presumptions conditions its behaviour
      on that gate's responsiveness.** PRESUMPTION-879 is the *purest* instance: the remit rule is
      stated unconditionally, so it holds identically on day 1 and on day 17, and its correctness is
      wholly contingent on a party whose availability no agent measures.
    Literature basis: MAST specification/role failures at 41.8% and verification/termination at 21.3%
      (Cemri et al. 2025, arXiv:2503.13657); responsibility-gap and many-hands literature
      (https://link.springer.com/article/10.1007/s11245-025-10302-4); safety-listening failure located
      at the listener (Risk Analysis 2025, https://onlinelibrary.wiley.com/doi/full/10.1111/risa.70106);
      HITL guidance requiring deny-by-default-on-timeout
      (https://www.arthur.ai/column/human-in-the-loop-governance-for-ai-agents); Little's law under
      λ > μ (https://en.wikipedia.org/wiki/Little's_law).
    Risk level: Critical
    Recommendation: Give the gate timeout semantics before designing any further remedy that depends
      on it. See the identical note on PRESUMPTION-878, -880, -881, -882, -883 and -884.

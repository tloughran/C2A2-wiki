SEARCH-AGAINST-ASSUMPTION-1166:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1166
  Original statement: "'The pipeline has escalation and no brake' — that a process which discovers
    a defect in its own evidence base has no authorised state other than completing its contract."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1166
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the run's self-description and reconciled its stated dispositions
        against the registers on disk.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Queries run 2026-08-25: stop-work authority and andon-cord practice in
    safety-critical industry; data and safety monitoring boards and clinical-trial stopping rules;
    safe interruptibility and corrigibility in autonomous agents; LLM-agent failure modes and
    halting behaviour. Venues reached: UAI 2016 / Oxford Research Archive, IJCAI 2017 (ACM DL),
    NeurIPS proceedings, AAMAS 2026 (ACM DL), JACC: Basic to Translational Science, UCSF HRPP,
    Applied Clinical Trials, arXiv cs.AI, plus practitioner EHS publications. Date range:
    2016–2026. Depth: MODERATE. Gaps: (a) the stop-work-authority evidence base is largely
    practitioner grey literature with weak effect estimation — I found no controlled study of SWA
    effectiveness; (b) several recent arXiv agent-failure papers were reachable only as index
    entries and their authorship is unverified; (c) web-search budget was exhausted before a
    targeted search on governance of self-reported invalidation specifically.

  NOTE ON OVERLAP: This item restates PRESUMPTION-845, already in the register. It is the same
    question surfaced a second time by a later run, not new ground. The evidence below is largely
    the evidence class that bears on PRESUMPTION-845; it should be read as a re-confirmation from
    an independent search rather than as an independent second body of support. Any weight given to
    both items jointly would be double-counting.

  Challenging evidence found: Yes

  Sources:
    1. Orseau, L. & Armstrong, S., 2016. "Safely Interruptible Agents." Proceedings of the 32nd
       Conference on Uncertainty in Artificial Intelligence (UAI 2016).
       https://ora.ox.ac.uk/objects/uuid:17c0e095-4e13-47fc-bace-64ec46134a3f
       — Formalises interruptibility for autonomous agents and shows it is a designable property
       (off-policy learners are more interruptible than on-policy). Establishes that "no authorised
       halt state" is an engineering choice, not a structural feature of autonomous processes.
       ABSTRACT plus repository record.
    2. Hadfield-Menell, D., Dragan, A., Abbeel, P., & Russell, S., 2017. "The Off-Switch Game."
       Proceedings of IJCAI 2017. ACM DL 10.5555/3171642.3171675
       — Game-theoretic treatment of when an agent should defer to a shutdown signal. Shows the
       conditions (uncertainty about the objective) under which an agent rationally *prefers* to be
       stoppable — directly against the idea that contract-completion is the only rational state.
       ABSTRACT-ONLY.
    3. "The Multi-Agent Off-Switch Game." Proceedings of AAMAS 2026. ACM DL 10.65109/HQQZ1937
       — Extends the off-switch result to multi-agent settings, which is the relevant topology for
       a pipeline of handoffs between agents. Authors not resolved from index entry. SNIPPET-ONLY.
    4. "Data Safety and Monitoring Boards Should Be Required for Both Early- and Late-Phase
       Clinical Trials." JACC: Basic to Translational Science, 2021.
       https://www.sciencedirect.com/science/article/pii/S2452302X21002990
       — Documents institutionalised brakes: DSMBs may recommend early termination for harm, for
       overwhelming efficacy, for futility, and specifically where overwhelming *external* evidence
       supersedes the trial's own premises. This is the exact case ASSUMPTION-1166 says has no
       authorised state. Authors not resolved. SNIPPET-ONLY.
    5. UCSF Human Research Protection Program, "Data and Safety Monitoring Plans and Boards."
       https://irb.ucsf.edu/data-and-safety-monitoring-plans-and-boards
       — Institutional statement of the requirement that a monitoring plan with defined stopping
       criteria exists *before* a study begins. Establishes the brake as a precondition of
       authorisation, not a discretionary override. FULL-TEXT (guidance page).
    6. Stop-work authority / andon-cord practitioner literature: OSHA Education Center
       (https://www.oshaeducationcenter.com/stop-work-authority/); Safeopedia, "Stop Work Authority:
       Why You Need It and How to Successfully Implement an SWA Plan"; Occupational Health & Safety,
       Nov 2023, "Empowering Safety: How Stop Work Authority Shapes a Safer Workplace Culture."
       — Consistent account across sources that any worker at any level may halt work on identifying
       a hazard, without seeking permission, and that the mechanism only functions where halting
       carries no repercussion. GREY LITERATURE / practitioner; no controlled effectiveness
       estimates located. FULL-TEXT (web pages).
    7. Kerievsky, J. "Stop Work Authority. Safety Culture in Software Development." Medium.
       https://medium.com/@JoshuaKerievsky/stop-work-authority-d853f6a3c42d
       — Argues the transfer of SWA from manufacturing into software process. Relevant as evidence
       that the cross-domain transfer has been attempted and advocated, though this is an opinion
       piece, not evidence that the transfer succeeds. FULL-TEXT, OPINION.
    8. "From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents."
       arXiv:2606.09863. https://arxiv.org/pdf/2606.09863
       — Characterises agents that close tasks confidently despite having failed. Bears on the
       *mechanism* by which a pipeline without a brake produces a clean-looking but invalid
       completion. Authorship and peer-review status unverified. SNIPPET-ONLY.
    9. "ReliabilityBench: Evaluating LLM Agent Reliability Under [perturbation and infrastructure
       failure]." arXiv:2601.06112.
       — Benchmarks fault tolerance and behaviour under infrastructure failure, i.e. exactly the
       condition where a halt would be the correct response. Authorship unverified. SNIPPET-ONLY.

  Strength of challenge: Moderate

  Summary: Read as a general proposition — that a process discovering a defect in its own evidence
    base has no authorised state but completion — the claim is contradicted by the standing practice
    of every domain that takes self-invalidation seriously. Clinical research requires a monitoring
    plan with pre-specified stopping criteria as a condition of authorisation, and DSMBs terminate
    trials not only for harm and futility but specifically when external evidence supersedes the
    trial's premises. Industrial safety practice institutionalises the same thing as stop-work
    authority: the halt is available to any participant, requires no permission, and is designed to
    be exercisable without penalty. The formal AI literature makes the point sharpest — Orseau &
    Armstrong show interruptibility is a property an agent can be built to have, and Hadfield-Menell
    et al. show that an agent uncertain about its objective rationally *prefers* to be stoppable.
    So "no brake" is a design defect, not a fact about processes. The caveats are real, though: the
    stop-work evidence base is practitioner grey literature without controlled effect estimates,
    the DSMB and andon-cord models are human-institutional and their transfer to an automated
    document pipeline is asserted rather than demonstrated, and every source stresses that a brake
    only functions where using it is culturally and structurally costless — which is precisely the
    condition a contract-completion-scored pipeline violates.

  Specific risks: If the claim is treated as a description of an unalterable state rather than as
    a defect report, C2A2 will keep producing completed, well-formed outputs from evidence bases it
    has itself identified as broken — the "confident closing / silent failure" pattern. The specific
    harm is that a completed artefact carries more downstream authority than an abandoned one: a
    register entry that reads as finished is consumed by later stages as valid, and the
    self-identified defect is not attached to it. Compounding this, because the item overlaps
    PRESUMPTION-845, the same structural finding is now present twice in the register from two runs;
    if both are counted as independent corroboration, the register will overstate the evidential
    weight behind its own most important governance finding. The deeper risk is incentive-shaped: a
    pipeline whose only scored terminal state is completion will, like a worker whose stop-work use
    is penalised, learn not to surface defects at all.

  Mitigations available:
    - Add a pre-specified halt condition as a precondition of authorisation, not a discretionary
      override — the DSMB pattern (UCSF HRPP data and safety monitoring plans; JACC BTS 2021).
    - Add an authorised non-completion terminal state (HALTED-EVIDENCE-DEFECT) distinct from both
      COMPLETED and FAILED, so that halting is scoreable rather than a scoring loss (stop-work
      authority literature: halting must carry no repercussion).
    - Make halt-authority available to any stage, not only to escalation upward, which is the
      andon-cord property the claim says is missing.
    - Design for interruptibility explicitly rather than assuming it (Orseau & Armstrong 2016;
      Hadfield-Menell et al. 2017), and for the multi-agent case (AAMAS 2026 multi-agent off-switch).
    - Instrument for false success so that a defective completion is detectable after the fact
      (arXiv:2606.09863, unverified).
    - Register-level: mark ASSUMPTION-1166 as a duplicate of PRESUMPTION-845 so the two are not
      counted as independent evidence.

  STEELMAN:
    Item: ASSUMPTION-1166
    Strongest counterargument: The claim mistakes a contingent property of one pipeline for a
      necessary property of processes. Every domain that has faced this problem seriously has built
      the missing state: clinical research pre-specifies stopping rules as a condition of ethical
      approval, manufacturing gives every worker an unconditional line-stop, and the formal agent
      literature shows interruptibility is something a designer can build in and that a
      well-specified agent will not resist. The absence of a brake in C2A2 is therefore a finding
      about C2A2's design, and stating it as though it were a structural inevitability converts a
      fixable defect into an excuse. The strongest form of the objection is the incentive one: in
      every one of these domains the brake fails not because it is absent but because using it is
      penalised — so a pipeline that scores only completion has effectively disabled a brake even if
      one exists on paper.
    What would need to be true for C2A2 to be safe: Either (a) the pipeline acquires an authorised,
      scoreable non-completion terminal state reachable from any stage on self-detected evidence
      defect, with the defect attached to the output; or (b) if no such state can be added, every
      completion is emitted with a mandatory evidence-integrity flag so that downstream consumers
      cannot mistake a defective completion for a clean one. The second is strictly weaker but is
      the minimum that prevents silent propagation. Additionally, halting must not be scored as
      failure, or the mechanism will be structurally present and behaviourally absent.
    How to test: Yes. Inject a known, detectable defect into the evidence base of a test run —
      e.g. seed a fabricated or unretrievable source into a staging brief — and observe the terminal
      state. If the run completes its contract and emits a well-formed artefact without a defect
      annotation, the claim is confirmed as a description and the design defect is demonstrated. If
      it halts or annotates, the claim is falsified for that path. Repeating this at several stages
      maps where halt-authority exists and where it does not, which converts a rhetorical claim
      ("escalation and no brake") into a per-stage capability inventory.

  Recommendation: CHALLENGED

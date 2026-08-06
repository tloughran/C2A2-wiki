SEARCH-AGAINST-PRESUMPTION-678:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-678
  Original statement: That an agent's own charter is exempt from the premise register that
    governs the system; 14b ran ~118 days under a norm contradicting six ACTIVE premises,
    and the contradiction was found from outside.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-678
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b generalised the lit pipeline's line-88 finding from one charter to the class.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Institute of Internal Auditors, Global Internal Audit Standards — External Quality
       Assessment requirement (IIA Quality Services / EQA guidance; confirmed this session via
       theiia.org and practitioner guidance from Baker Tilly and Wolters Kluwer/TeamMate).
       The profession that most closely resembles C2A2's premise register — internal audit —
       has concluded that the audit function cannot validate itself. The Standards require a
       full-scope external quality assessment by a qualified assessor from outside the
       organisation at least every five years, or a self-assessment that is *independently
       validated*. Pure self-assessment is explicitly held to lack sufficient independence.
       This is a direct, codified rejection of the presumption that the auditing charter is
       exempt from the regime it applies to others.
    2. Sarbanes-Oxley Act of 2002 and the creation of the PCAOB (confirmed this session via
       PCAOB, Harvard Law School Forum on Corporate Governance, and IOSCO "Principles of
       Auditor Independence and the Role of Corporate Governance in Monitoring an Auditor's
       Independence"). The audit profession's era of self-regulation ended precisely because
       the self-exempting arrangement failed catastrophically (Enron, WorldCom). The
       historical verdict is that a body which sets standards it is not itself subject to
       drifts, and the drift is only found from outside. Note the residual: commentary on
       corpgov.law.harvard.edu records that PCAOB's own "interim" independence standards were
       inherited from the self-regulation era and were never modernised — i.e. the exempt
       layer persisted even after the reform. That is the ~118-day pattern at institutional
       scale.
    3. Congressional Accountability Act of 1995 and residual congressional exemptions
       (confirmed this session via ProPublica, "Do As We Say, Congress Says, Then Does What
       It Wants"). Congress exempted itself from large classes of workplace, safety and
       transparency law for roughly two centuries; the 1995 Act closed part of the gap but
       Congress remains exempt from FOIA, OSHA investigatory subpoenas, and several
       whistleblower retaliation protections. The relevant finding for C2A2 is not the moral
       one but the detection one: each exemption was surfaced by external journalism or
       external litigation, never by the exempt body's own review.
    4. "Detection and Resolution of Normative Conflicts in Multi-agent Systems," AAMAS 2018
       (proceedings PDF confirmed this session at ifaamas.org; author list not confirmed —
       [UNVERIFIED — authors not confirmed this session]). Together with the deontic-logic
       compliance-checking literature surfaced this session (e.g. "Automated Reasoning in
       Deontic Logic," arXiv:1411.4823; "Handling irresolvable conflicts in the Semantic Web,"
       Journal of Logic and Computation 35(8), exaf054), this establishes that normative
       conflict detection over a rule set is a solved-in-principle, mechanisable problem:
       conflicts are characterised as obligation-vs-prohibition, prohibition-vs-permission,
       and obligation-on-conflicting-actions over the same action, and formalised normative
       systems can be checked for consistency by automated theorem provers. The presumption
       is therefore not just risky but unnecessary — the charter *could* have been placed in
       the register and checked mechanically.
    5. Meta-monitoring practice in production observability (Airbnb Engineering, "Monitoring
       reliably at scale," Medium; DZone, "An Overview of Meta-Monitoring"; both confirmed
       this session). Operations engineering independently converged on the same conclusion:
       a monitoring system that watches everything except itself has a silent-failure class
       that is invisible by construction. The standard remedy is a separate meta-monitoring
       tier on isolated infrastructure plus a dead-man's-switch — an outside-the-loop
       liveness signal. The Airbnb write-up explicitly names the infinite-regress objection
       and answers it with "terminate the recursion in a dead man's switch," not with
       "exempt the top layer."

  Strength of challenge: Strong

  Summary: The presumption is challenged from four independent directions — professional
    audit standards, statutory history, formal normative-systems research, and production
    observability practice — and none of them supports it. The convergent finding is that
    self-exemption at the governing layer produces a failure class detectable only from
    outside, and that every mature domain has responded by *importing* an external check
    rather than by accepting the exemption. The 118-day latency and the outside-in discovery
    route are exactly the signature these literatures predict. The deontic-logic material
    additionally removes the usual excuse: charter-vs-premise conflict detection is
    mechanisable, so the exemption is a design omission rather than a technical necessity.
    No source found this session argues that a governing charter should be exempt from the
    norms it administers.

  STEELMAN:
    Strongest counterargument: The regress is real and the exemption may be its cheapest
      termination. Every check needs a checker; the observability literature terminates the
      recursion arbitrarily (dead man's switch) rather than principledly, and the IIA's own
      answer — external assessment every five years — concedes that continuous self-checking
      is unaffordable. If C2A2 put every charter into the premise register, the register's own
      admission rules become a charter, and so on. There is also a genuine functional
      argument: an auditor bound by the same constraints as the audited can be paralysed by
      them, which is why grand-jury, ombudsman and inspector-general functions are routinely
      granted procedural exemptions the bodies they investigate do not have. Exemption may be
      the price of the function.
    What would need to be true for C2A2 to be safe: (a) the exemption is explicit and
      recorded, not implicit — the IIA model tolerates self-assessment only when a named
      independent validator signs it; (b) there is a bounded, scheduled external check with a
      known period (the five-year EQA analogue), so the maximum drift latency is a chosen
      number rather than an emergent one; (c) the exempt layer is small and its norms are
      few, so a human or an outside agent can read it end-to-end; (d) crucially, an
      outside-the-loop liveness signal exists — something that fires when *no* charter review
      has occurred, rather than only when a review reports a problem. The 118 days is
      diagnostic precisely because nothing fired.
    How to test: Extract every agent charter in the vault and every ACTIVE premise in the
      register into a common predicate form, then run a pairwise conflict check for the four
      AAMAS conflict patterns (obligation vs prohibition on the same action, etc.). Report:
      (i) how many charters are currently absent from the register entirely; (ii) how many
      charter-premise pairs conflict; (iii) for each conflict already known, the elapsed days
      between charter authorship and detection, and whether detection was internal or
      external. If (i) is large and every entry in (iii) is "external," the presumption is
      confirmed as operative and the challenge applies at full force.

  Specific risks: If the presumption is false — i.e. charters are *not* legitimately exempt —
    then every agent in the pipeline may currently be executing under norms that contradict
    the register, with no bounded detection latency. The specific breakage: contradiction is
    discovered only when an unrelated outside pass happens to look, so the expected latency is
    a function of luck rather than design; corrections are retroactive and invalidate prior
    output (14b's ~118 days of work now inherit a question mark); and the register's own
    authority is undermined, because a register that does not govern its administrators is
    evidence to every other agent that the register is advisory. The audit-history analogue
    warns of the compounding version: the exempt layer survives the reform that was meant to
    close it.

  Mitigations available: (1) Register-by-default — a charter is not loadable until it has a
    premise-register entry; the IIA "independently validated self-assessment" pattern. (2)
    Mechanised conflict check at charter load, using the deontic conflict patterns above; this
    is cheap and does not require the full regress. (3) A dead-man's-switch on charter review:
    an alert that fires on the *absence* of a charter-vs-register check within N days,
    modelled on the meta-monitoring pattern, since the failure mode is absence of a signal
    rather than presence of an error. (4) Cross-agent review: charters audited by an agent
    other than their author, mirroring auditor-rotation and the EQA independent-assessor rule.
    (5) Bound the exemption explicitly: if a charter must be exempt, record the exemption and
    its expiry in the register itself, so the exemption is a first-class, reviewable object.

  Search scope: Comprehensive for the governance and operations framings — professional audit
    standards (IIA, PCAOB, IOSCO), statutory self-exemption (Congressional Accountability
    Act), formal normative-conflict detection (deontic logic, AAMAS multi-agent norms), and
    meta-monitoring practice. Preliminary on two adjacent bodies that may hold additional
    material: Kelsenian legal theory on the self-reference of the Grundnorm (searched, found
    conceptually relevant but not empirically challenging — Kelsen's hierarchy actually
    *predicts* that a top norm is presupposed rather than validated, which is closer to a
    steelman than a challenge), and AI-alignment work on whether a model's constitution is
    itself subject to the critique loop it induces. Broader search recommended on the latter.

  Recommendation: CHALLENGED

SYSTEMIC-RISK-FLAG:
  Date: 2026-08-06
  Affected items: PRESUMPTION-678, PRESUMPTION-689, PRESUMPTION-690, PRESUMPTION-691,
    PRESUMPTION-695
  Common vulnerability: Open-loop self-verification. In all five items the system holds a
    belief about its own state (my charter is fine; my task is satisfiable; my scheduled task
    is runnable; my queue growth is healthy; my object-level output is sound) for which there
    is no feedback channel capable of returning "no." Each belief is confirmable from inside
    and falsifiable only from outside, and in every case the falsification actually arrived
    from outside or has not arrived at all. The five are not five independent presumptions;
    they are five instances of one architectural gap — the absence of an outside-the-loop
    signal that fires on *absence* of evidence rather than on presence of error. PRESUMPTION-
    691 is the most dangerous member because it converts the gap into an affirmative health
    signal: a rising queue is read as vigour, so the metric moves in the wrong direction
    exactly when the loop is broken.
  Literature basis: The absence-of-signal failure class is named identically in three
    unrelated literatures searched this session. Operations: cron and background-job
    monitoring guidance is unanimous that scheduled-task failures are "the absence of
    something happening" and that ordinary monitoring never fires on them, requiring
    heartbeat/dead-man's-switch inversion (OnlineOrNot; Cronping; QuietPulse; SimpleObservability
    — all confirmed this session). Control theory: an open-loop system "follows a command
    schedule whether or not the output matches the target" and cannot correct drift without a
    feedback signal (closed-loop control references confirmed this session). Governance: the
    IIA's mandatory external quality assessment and the PCAOB's replacement of audit
    self-regulation both exist because internal confirmation of an internal state was shown
    to be non-diagnostic. Reinforcing: Goodhart's law and the vanity-metric literature explain
    why the producer-side proxy in PRESUMPTION-691 keeps rising while the underlying goal
    stagnates.
  Risk level: Critical
  Recommendation: Treat as one remediation, not five. Institute a single absence-detector
    tier: for each of the five loops, define the outside-the-loop signal that should fire when
    no verification has occurred within N days, and alert on silence rather than on error.
    Concretely — charter-vs-register check (678), preamble-vs-ceiling feasibility check at
    task load (689), environment-capability probe before scheduling (690), a metric that
    *falls* when the queue rises (691), and a provenance-tier field on object-level results
    with a periodic full-source verification sample (695). The five detectors share one
    property and should share one implementation: they must be evaluable by an agent that did
    not produce the artefact being checked.

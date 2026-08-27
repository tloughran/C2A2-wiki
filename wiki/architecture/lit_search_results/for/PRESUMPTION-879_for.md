SEARCH-FOR-PRESUMPTION-879:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-879
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake)
  Original statement: "[inferred] That an agent's remit boundary marks the place where a known defect
    stops being anyone's problem — that declining a correct fix on remit grounds discharges the agent's
    responsibility for it."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-879
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three independent same-day instances of declining a fix the agent had already
        diagnosed. High confidence — the pattern is stated three times in the agents' own words; only
        the reading of it as a presumption is inferred. Not an accusation: each agent followed its
        definition exactly.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-26, four queries. Limbs covered: (a) separation/segregation of
    duties as a control principle — the strongest formal warrant for a hard remit boundary;
    (b) diffusion of responsibility and organisational bystander effects — searched deliberately as
    the rival account, so the supportive case is stated against it; (c) clinical handover / handoff
    protocols (SBAR, I PASS the BATON, AHRQ TeamSTEPPS) as the best-developed literature on when
    responsibility actually transfers; (d) change-management discipline and the risks of unauthorised
    out-of-scope changes.
    Assessment: **moderate coverage — two limbs not run.** I did not reach the aviation/CRM literature
    on speaking-up and authority gradients, nor any literature specifically on *escalation into an
    unresponsive or absent recipient*, which is the item's live condition (a gate silent for
    seventeen days). The second of these is the material gap and I could not close it: searches
    returned general escalation-procedure guidance, not studies of escalation targets that do not
    respond. No source located addresses remit boundaries between *software agents* as opposed to
    human role-holders.

  Supporting evidence found: Partial

  Sources:
    1. Separation of Duties (SoD) as a control principle, as documented in: Wallarm, "Separation of
       Duties: A Step-by-Step Guide for Businesses," https://www.wallarm.com/what/separation-of-duties ;
       Ping Identity, "Understanding Separation of Duties in Cybersecurity,"
       https://www.pingidentity.com/en/resources/blog/post/separation-of-duties.html ;
       SafetyCulture, "Segregation of Duties for Internal Control,"
       https://safetyculture.com/topics/internal-control/segregation-of-duties
       — Establishes the core supportive principle: distributing responsibility so that no single actor
       controls a whole critical process *reduces* accidental error, insider risk and unauthorised
       change. Under SoD, an actor declining to act outside their assigned function is the control
       working, not failing. These are practitioner/vendor sources, not peer-reviewed research.
       SNIPPET-ONLY.
    2. "Transferring responsibility and accountability in maternity care: clinicians defining their
       boundaries of practice in relation to clinical handover." PMC3437433,
       https://pmc.ncbi.nlm.nih.gov/articles/PMC3437433/ [authors and year unverified]
       — The closest located analogue to the item: a study of practitioners explicitly defining the
       boundaries of their own practice at the point of handover. Establishes that boundary-definition
       at handover is a recognised, studied professional behaviour rather than an aberration.
       ABSTRACT-ONLY.
    3. Agency for Healthcare Research and Quality (AHRQ), TeamSTEPPS Curriculum, "Tool: Handoff."
       https://www.ahrq.gov/teamstepps-program/curriculum/communication/tools/handoff.html
       — Supports the *mechanism* of responsibility transfer: handoff is defined as the transfer of
       professional responsibility and accountability, and structured protocols exist to effect it.
       Critically for the caveats, AHRQ's own statement of the rule is conditional: you remain
       accountable until the receiving party is aware of and accepts the transfer, and "until it is
       acknowledged that the handoff is understood and accepted, you cannot relinquish your
       responsibility." SNIPPET-ONLY.
    4. "Communication in Clinical Handover: Improving the Safety and Quality of the Patient
       Experience." PMC4693345, https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4693345/
       [authors and year unverified]; and "Use of Structured Handoff Protocols for Intrahospital
       Within-Unit Transitions," *Making Healthcare Safer IV*, NCBI Bookshelf NBK613742,
       https://www.ncbi.nlm.nih.gov/books/NBK613742/
       — Document the standard protocols (SBAR; SHARED; I PASS the BATON, whose "O" is explicitly
       Ownership) and the safety cost of failed transfer. Supports the claim that responsibility
       transfer is a real, formalisable operation — the presumption's necessary precondition.
       SNIPPET-ONLY.
    5. Change-management discipline, as summarised in: Monday.com, "What is change management in IT?
       A complete guide (2026)," https://monday.com/blog/service/it-change-management/ ;
       Cynomi vCISO Academy, "Introduction to Change Management,"
       https://cynomi.com/academy/change-management/introduction-change-management/ ;
       Credencey, "Understanding the Legal Risks of Unauthorized Scope Changes in Projects,"
       https://credencey.com/legal-risks-of-unauthorized-scope-changes/
       — Supports the cost side of the ledger the presumption is implicitly pricing: unauthorised and
       untracked changes are a documented source of misconfiguration, outage and vulnerability. An
       agent that knows the fix but is not authorised to make it, and does not make it, is complying
       with a control whose purpose is exactly this. Practitioner sources; the cited 2023
       "change accelerators" ROE figures are second-hand and I could not verify the underlying study.
       SNIPPET-ONLY.
    6. Diffusion of responsibility in organisations, as summarised in: The Decision Lab,
       "Diffusion of Responsibility,"
       https://thedecisionlab.com/reference-guide/psychology/diffusion-of-responsibility ;
       EBSCO Research Starters, "Diffusion of responsibility,"
       https://www.ebsco.com/research-starters/psychology/diffusion-responsibility ;
       IO at Work, "Employees May Not Speak Up Because of the Bystander Effect,"
       https://www.ioatwork.com/employees-may-not-speak-up-because-of-bystander-effect/
       — Recorded for honesty: this is the rival account and it fits the generating case closely
       ("addressing X is someone else's job… this diffusion of responsibility is classic bystander
       effect, but it gets institutionalised in workplace structures"). It does not support the
       presumption. SNIPPET-ONLY.

  Strength of support: Weak-to-Moderate

  Summary: The literature gives clear support for the *legitimacy* of remit boundaries and for
    responsibility transfer as a real operation. Separation-of-duties doctrine holds that confining
    actors to their assigned function reduces error and unauthorised change; the change-management
    literature documents the costs of out-of-scope fixes; and the clinical handover literature supplies
    a mature, protocol-level account of how professional responsibility and accountability move from
    one holder to another. To that extent an agent that diagnoses a defect, names the file, and stops
    at its remit boundary is doing something the literature endorses. But the support is conditional in
    a way that bears directly on the item. The handover literature's central rule is that transfer is
    *not* complete until the receiver acknowledges acceptance — AHRQ states explicitly that the sender
    remains accountable until then. On that account, escalation into a channel that has been silent for
    seventeen days is not a discharge at all: it is an incomplete handoff, and the defect remains the
    escalating agent's. The rival literature — diffusion of responsibility, institutionalised in
    workplace structure — describes the generating case with uncomfortable precision. So the
    presumption's first half (remit boundaries are correct) is supported; its second half (declining on
    remit grounds *discharges* responsibility) is supported only where the recipient is responsive.

  Caveats: (1) The best-evidenced supportive source contains its own defeater: responsibility transfers
    only on acknowledged acceptance, which by construction has not occurred here. (2) The SoD and
    change-management sources are practitioner/vendor material, not peer-reviewed; I found no
    controlled study of SoD's error-reduction effect. (3) Domain transfer is unverified in both
    directions: clinical handover is between humans with continuous shift coverage, and SoD assumes
    every function has a live holder; neither assumes a recipient who may be absent for weeks.
    (4) Nothing located addresses the item's specific structure — a remit rule that is unconditional on
    recipient responsiveness, so that the boundary holds identically on day 1 and day 17. (5) All
    sources read at snippet or abstract level.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that role boundaries reduce error and unauthorised change and are a
    legitimate control; (ii) that responsibility and accountability are formally transferable by
    protocol; (iii) that acting outside remit carries documented risk.
    Unsupported sub-claim: that a *declined* fix plus an escalation discharges responsibility
    unconditionally. The handover literature says the opposite where acceptance is unacknowledged.
    Unaddressed sub-claim: **escalation into a demonstrably unresponsive channel — what the remit rule
    should do when the recipient's non-response is itself observable and long-running.** I found no
    literature that conditions role-boundary discipline on recipient availability, and none on
    boundary behaviour among autonomous software agents. The generating case's specific feature — that
    every agent's definition holds its boundary identically regardless of how long the escalation
    target has been silent, converting a handoff into a terminus — appears unaddressed and is
    flagged as a candidate original contribution.

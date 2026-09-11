SEARCH-FOR-PRESUMPTION-956:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-956
  Original statement: "[inferred] That an agent's edit boundary is also its responsibility boundary —
    that declining to fix something outside one's write scope discharges the finding."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-956
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from two independent runs declining two different repairs on the same ground on the
        same day. Both instances are correct agent behaviour under the current design — the presumption
        is in the design, not the conduct.
      15a: Searched for supporting literature; found that the escalation literature defines the duty in
        the exact opposite direction, and that agent-to-agent handoff is a recognised, instrumented
        design object rather than an unavailable one.
    Current status: NO-SUPPORT-FOUND

  Register pre-check:
    - PREMISE-163 (ACTIVE) — "Production-completion is not lifecycle-completion. A producer may be
      retired only through a HANDOVER GATE THAT NAMES A SUCCESSOR OWNER for the open defect classes in
      its output." 14b's note that PREMISE-163 may bear is confirmed: the premise already requires a
      named successor owner and is the governing rule for exactly this shape.
    - PREMISE-108 (ACTIVE) — transmission is not delivery; a finding "flagged for" a named agent does
      not transfer responsibility for it, and until receipt-and-action are evidenced the finding is held
      by nobody while the record shows it discharged.
    - PREMISE-131, PREMISE-138 (ACTIVE) — a warning is not a control; repetition in a channel with no
      effector is not a remedy, and its only admissible function is transfer of obligation to a named
      actor outside the channel. Note **"named actor"** — the premise already contemplates routing.
    - PREMISE-173 (ACTIVE) — name the final element.
    - PREMISE-115 (ACTIVE) — cites the MAST taxonomy figures (41.8% / 36.9% / 21.3%), which this search
      independently re-encountered; see source 4 for the cross-check.
    - PREMISE-196 (ACTIVE) — an access restriction enforced in the capability grant has a lower
      violation rate than the same restriction expressed as an instruction. This is the one ACTIVE
      premise that supports the *value* of the write-scope limit, which nobody disputes.
    Recording the hits per OPEN-192; searched anyway.

  LIMB SPLIT:
    Limb A (WRITE-SCOPE LIMITS ARE LEGITIMATE): an agent should not edit outside its granted scope, and
      declining to do so is correct conduct.
    Limb B (DECLINING DISCHARGES THE FINDING): the finding is transferred by being written down, and no
      routing obligation attaches to the agent that cannot fix.

  Supporting evidence found: Partial (Limb A only — and Limb A was never in dispute)

  Sources:
    1. Escalation definitions in incident practice (QuickStaffPro, "Incident Reporting vs. Escalation:
       Key Differences"; University of Queensland Health and Safety Incident and Hazard Reporting
       Procedure; Urban Utilities WHS Procedure 2.6 "Incident Reporting, Investigation and Escalation").
       — SECONDARY — Escalation is defined as "the immediate handoff of an active incident to the person
       or team with the authority, expertise, or resources to act **when the first responder can't
       resolve it alone**," and is distinguished from reporting: "unlike incident reporting, which
       records what happened, escalation is a real-time call to action that **shifts ownership** while
       the situation is still unfolding." This is the precise refutation of Limb B, and it refutes it on
       the item's own trigger condition — inability to fix is what *creates* the escalation duty, not
       what discharges it.
    2. Institutional WHS escalation procedures (UQ; Urban Utilities). — SECONDARY — "Escalation
       procedures for serious, urgent, or unresolved concerns ensure significant risks are brought to
       the attention of appropriate managers or decision-makers without delay." The obligation is
       placed on the finder and is not satisfied by the report.
    3. Waring, J. et al. / "Fix and forget or fix and report: a qualitative study of tensions at the
       front line of incident reporting," BMJ Qual Saf (PMC4413736). — SECONDARY (located via search;
       abstract-level) — Finds that practitioners choose "fixing and forgetting" where they can resolve
       problems themselves and do not prioritise reporting once a safety problem is fixed. Note the
       direction: the measured failure in healthcare is *under-reporting when you can fix*, which is the
       mirror image of the estate's pattern (*reporting instead of routing when you cannot fix*). Neither
       pattern supports Limb B; both are named as failures of the same duty.
    4. Cemri, M. et al., 2025. "Why Do Multi-Agent LLM Systems Fail?" arXiv:2503.13657 (NeurIPS 2025);
       and the MAST-Data follow-on (1600+ annotated traces across 7 frameworks). — SECONDARY — 14
       failure modes in 3 categories from 150 expert-annotated traces (κ = 0.88): system design
       **41.77%**, inter-agent misalignment **36.94%**, task verification **21.30%**; named priority
       areas include "handoff degradation." Two things follow. First, the figures cross-check against
       PREMISE-115's recorded 41.8 / 36.9 / 21.3 — independent re-encounter, same source, so this is a
       corroboration of the register's citation rather than a new datum. Second, and the point for this
       item: agent-to-agent handoff is a *first-class, instrumented, measured* design object in
       multi-agent systems. A system with no agent-to-agent repair path has not avoided the failure
       class; it has made the 36.94% category unmeasurable by removing the channel in which it would
       appear.
    5. NIST SP 800-61r2, *Computer Security Incident Handling Guide*. — SECONDARY — Incident handling is
       specified with defined handoff and escalation points and named role ownership; detection and
       analysis do not terminate the lifecycle. Consistent with sources 1–2 and with PREMISE-163.
    6. Least-privilege / capability-restriction practice. — SECONDARY — Supports Limb A, which is not in
       dispute and which PREMISE-196 already carries: the write-scope limit is a genuine safety property
       and was rightly chosen. No source I found treats a capability limit as also limiting
       responsibility; in every framework the two are explicitly separated, which is the whole point of
       an escalation path.

  Strength of support: Weak (Limb A, uncontested), None (Limb B)

  Summary: The FOR direction fails on this item about as completely as it can. Limb A is supported and
    was never at issue — Agent 16 and the daily run both behaved correctly, as 14b said, and the
    write-scope limit should stay. Limb B is contradicted by the defining sentence of the escalation
    literature: escalation is *triggered by* inability to resolve, and it is distinguished from
    reporting precisely by the fact that it shifts ownership rather than recording an event. The
    healthcare study adds an instructive inversion — front-line practitioners under-report when they
    *can* fix, the estate over-reports when it *cannot*, and both are failures of the same transfer
    duty. The multi-agent-systems evidence closes the design question: handoff degradation is a named,
    measured failure mode occupying the second-largest category of MAS failures, which means
    agent-to-agent routing is a normal architectural component that this estate has simply not built.
    14b's framing is right that the presumption sits in the design rather than the conduct, and
    PREMISE-163 already states the rule the design is missing: a handover gate that names a successor
    owner. The two live one-line fixes are the cost of not having one.

  Caveats: The escalation sources are institutional procedure documents and practitioner material, not
    research; they establish what the duty *is* in codified practice, not how well it is discharged.
    The MAST figures are from LLM-agent benchmark traces on task-completion workloads, not on
    maintenance or repair routing, so "handoff degradation" there is about context loss in an existing
    channel rather than about an absent channel — the transfer is by analogy and I am relying on it only
    for the claim that the channel is a normal design object. The Waring study is UK healthcare
    qualitative work at abstract level; I did not retrieve it. None of the six sources was read as full
    text.

  Search scope: comprehensive — searched escalation versus reporting definitions, duty-to-refer and
    handoff obligations in occupational and clinical safety reporting, incident-handling lifecycle
    ownership (NIST), multi-agent LLM failure taxonomies and inter-agent handoff, and least-privilege
    practice. Did not search the professional-ethics literature on duty to warn / duty to refer
    (medicine, engineering licensure), which is where the strongest normative statement of this duty
    lives and which would be the right next step if the estate wants a principled rather than
    operational grounding.

  Recommendation: NO-SUPPORT-FOUND. The recommendation rests on Limb B, which is the load-bearing limb
    and the one carrying 14b's High risk. Limb A stands and should be recorded separately so the finding
    is not misread as an argument for widening write scope — it is not. What the literature supplies is
    a single structural prescription, already present in the register as PREMISE-163: an agent that
    cannot fix must name a successor owner, and the successor may be another agent. The in-house count
    14b specifies (findings closed in the last 30 days by an agent other than the one that raised them)
    will show whether that path exists at all; the two live defects — PROP-2026-08-14-033's retired
    retrieval target, and the duplicate `*Total PRS triplets:*` anchor in four registers — are the test
    cases, and both have known one-line fixes sitting behind a fourteen-day human latency.

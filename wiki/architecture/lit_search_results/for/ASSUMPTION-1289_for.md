SEARCH-FOR-ASSUMPTION-1289:
  Date searched: 2026-09-09
  Original item: ASSUMPTION-1289
  Original statement: "the existence of a mechanism is being treated as evidence of its effect … the
    system has no habit of measuring controls at all, and so a mechanism's credit is set at the moment
    it is designed and never revised." Prescription: "A control with no [action-changed] value is a
    declared control, and should be labelled as such rather than counted as a control."
  Routed question: in socio-technical systems, are designed controls routinely credited with effects
    that are never measured — and does requiring an effect statistic per control change outcomes, or
    merely add a reporting burden?

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1289
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted verbatim from an agent-authored risk flag (SYSTEMIC-RISK-FLAG 2026-09-08,
        unmeasured-control-credit, High, filed by the delegated 15b subagent across ASSUMPTION-1277,
        ASSUMPTION-1282, PRESUMPTION-925, PRESUMPTION-928); the generalisation is routed, not the four
        instances the flag already argues.
      15a: Searched for supporting literature (2026-09-09), FOR direction only.
    Current status: SUPPORTED (limb A); PARTIALLY-SUPPORTED (limb B)

  PREMISE-REGISTER OVERLAP (checked before searching, per DEFECT-G): SUBSTANTIAL — READ THIS SECTION
  BEFORE THE SOURCES.
    Grepped for: control effectiveness, operating effectiveness, declared control, work-as-imagined,
    barrier management, self-report, detection control.
    - PREMISE-195 (ACTIVE, High confidence, validated 2026-08-31, re-check due 2026-09-30 on an elevated
      monthly cadence as "the estate's highest-rated open risk"): "Voluntary self-report is not a
      detection control. A control whose only output is the assertion of the controlled party produces
      silence as the shared output of 'nothing went wrong' and 'detection is not working' … Detection
      must be evidenced by an artefact produced independently of the party being assessed." Its
      supporting-evidence line ALREADY CITES the SOC 2 / ISO 27001 point that operating effectiveness
      must be tested by an external party and that self-assessment carries no evidentiary weight.
    - PREMISE-131 (ACTIVE): "A WARNING IS NOT A CONTROL, AND AN UNDELIVERED WARNING IS NOT A MITIGATION"
      — the hierarchy-of-controls premise, including the C-HIP delivery-stage argument and the
      folded-in clause that a confirmation dialog does not qualify as an engineering control.
    - PREMISE-146 (ACTIVE) carries work-as-imagined / work-as-done and Safety-II, and the register notes
      it was cited by BOTH search directions.
    - PREMISE-100 (ACTIVE): a liveness signal is not evidence of correctness.
    ASSESSMENT: the register already holds the SPECIFIC forms of this assumption for two named control
    classes (self-report controls; warning/administrative controls). ASSUMPTION-1289 is the GENERAL
    form — every control, not just weak ones — plus a prescription (a labelling rule) that no ACTIVE
    premise states. NARROWING APPLIED: I did not re-derive the self-report or hierarchy-of-controls
    material, both of which are settled in-house. I searched only (i) whether the unmeasured-credit
    pattern is general across control types rather than confined to weak ones, and (ii) the
    prescription's limb — whether requiring a per-control effect statistic changes anything.
    FLAG FOR 15c: if this returns SUPPORTED, the minting question is whether 1289 adds enough beyond
    PREMISE-195 + PREMISE-131 to survive PREMISE-138's bar on re-minting. My reading is that it does,
    but only via the LABELLING PRESCRIPTION, which is genuinely new.

  Supporting evidence found: Yes (limb A, strong); Partial (limb B)

  Structure: the assumption has two separable limbs and the literature treats them very differently.
    LIMB A — DIAGNOSIS: designed controls are routinely credited with effects never measured.
    LIMB B — PRESCRIPTION: requiring a per-control effect statistic changes outcomes rather than merely
      adding reporting burden.

  Sources (LIMB A — the diagnosis):
    1. The design-effectiveness / operating-effectiveness distinction in audit standards (COSO 2013
       Internal Control — Integrated Framework; PCAOB AS 2201; ISA (UK) 330).
       [PRACTITIONER-AND-STANDARDS LEVEL, ASSEMBLED FROM SEARCH SUMMARIES AND SECONDARY GUIDANCE PAGES
       THIS RUN. The COSO framework and PCAOB AS 2201 are real, canonical, and their titles are
       verified via coso.org and pcaobus.org listings retrieved this run. I DID NOT READ EITHER
       STANDARD. The paraphrases of ISA (UK) 330:8 and AS 2605 below are from a commercial guidance
       summary, NOT from the standards themselves, and should be treated as unverified] — This is the
       strongest FOR material and it is strong precisely because the ENTIRE PROFESSION IS BUILT ON THE
       DISTINCTION C2A2 IS DRAWING. Audit practice separates whether a control is CAPABLE of addressing
       the risk (design) from whether it ACTUALLY OPERATED over a period (operation), and treats the
       first as insufficient for the second. The reported operative rule is exactly the assumption's
       prescription in professional dress: testing of operating effectiveness is MANDATORY where the
       auditor intends to RELY on the control, i.e. you may not take credit for a control you have not
       tested. Two further reported asymmetries sharpen it and both favour the assumption: a conclusion
       that a control is NOT operating effectively can be supported by less evidence than a conclusion
       that it IS — a higher evidentiary bar for the credit-granting direction; and a walkthrough is
       not, in most cases, a test of operating effectiveness — i.e. having traced the mechanism once is
       explicitly NOT the same as having measured it. WEIGHT: Strong as established professional
       doctrine and as an existence proof that a per-control effectiveness requirement is operable at
       industrial scale.
    2. Hollnagel, E. — work-as-imagined vs work-as-done; Safety-II. Primary reference located:
       Hollnagel, E., Wears, R.L. & Braithwaite, J., "From Safety-I to Safety-II: A White Paper,"
       published via NHS England (england.nhs.uk/signuptosafety/…/safety-1-safety-2-whte-papr.pdf).
       [VERIFIED: the white paper exists at the NHS England URL and Hollnagel is its named lead author;
       CO-AUTHOR ATTRIBUTION TO WEARS AND BRAITHWAITE IS FROM GENERAL KNOWLEDGE OF THIS DOCUMENT AND WAS
       NOT CONFIRMED ON THE PAGE THIS RUN — treat as provisional. YEAR NOT VERIFIED AND NOT ASSERTED.
       DOCUMENT NOT READ] — The general form of limb A outside audit. The framework's core claim, per
       search summaries this run: work-as-imagined is how procedures and policies ASSUME a job is
       performed; work-as-done is how it is actually performed under time pressure, missing resources
       and changing conditions; the two rarely match. A designed control is a work-as-imagined artefact,
       and the gap between it and work-as-done is the mechanism by which designed-but-unmeasured
       controls accrue unearned credit. WEIGHT: Moderate-to-Strong as theoretical grounding; it is the
       canonical name for the phenomenon 1289 describes. Already register-held at PREMISE-146.
    3. Barrier management in offshore petroleum (Petroleum Safety Authority Norway barrier-management
       principles; verification of safety-critical elements).
       [SEARCH-SUMMARY AND CONFERENCE-PAPER-LISTING LEVEL ONLY. The PSA Norway barrier-management
       principles and the yearly barrier-performance assessment requirement are reported in summaries of
       IChemE conference papers and a DNV project page retrieved this run; I READ NONE OF THEM AND
       VERIFIED NO AUTHOR, YEAR OR TITLE. The "2013" date for the PSA principles is from a search
       summary and I am not asserting it] — Relevance: an entire safety regime that made exactly the
       assumption's prescription binding. Barriers must be VERIFIED for initial and continuing
       suitability, and performance must be assessed periodically rather than credited from design.
       That regulators found it necessary to mandate this is indirect evidence that the default
       behaviour was to credit barriers from design. WEIGHT: Weak as cited (nothing read), Moderate as
       a pointer. This is the highest-value unopened direction for this item.
    4. Control self-assessment overstatement / evidence requirements in risk registers.
       [PRACTITIONER LEVEL ONLY — Australian Department of Finance Comcover risk-management toolkit
       "Element 5: Control Effectiveness" and commercial GRC vendor guidance retrieved this run; NOT
       READ IN FULL] — Reported guidance: contemporary risk management focuses on using OBJECTIVE
       SOURCES OF EVIDENCE to verify the actual effectiveness of controls, and a binary
       effective/ineffective rating "often sparks debate" because most controls sit between. WEIGHT:
       Weak. Vendor and government-guidance material, not research. It establishes that the problem is
       recognised in practice; it measures nothing.

  Sources (LIMB B — does requiring the statistic change outcomes?):
    5. CAPA effectiveness checks in regulated manufacturing (FDA 21 CFR 820.100; ISO 9001).
       [SEARCH-SUMMARY AND VENDOR-BLOG LEVEL ONLY. The 21 CFR 820.100 CAPA requirement and the FDA
       expectation of an effectiveness check are real and well known; the specific figures and the
       March 2026 warning-letter anecdote below come from commercial compliance blogs retrieved this
       run and ARE NOT VERIFIED AGAINST FDA SOURCES. I did not open any FDA document] — This is the
       nearest thing found to a natural experiment on limb B: a regulator that mandated a per-control
       effect statistic (the effectiveness check) and enforces it. Reported: inadequate CAPA appears in
       more than 60% of FDA warning letters and is the most common source of 483 observations; failure
       to VERIFY that actions were effective before closure is among the most frequently cited
       deficiencies. One reported case describes a firm whose own trending data flagged a corrective
       action as failing for three consecutive quarters while the CAPA was marked done. WEIGHT: Weak as
       evidence (unverified commercial sources) but IMPORTANT IN DIRECTION, and it cuts a subtle way:
       it shows that mandating the statistic does NOT by itself close the gap — the requirement becomes
       the most-cited deficiency rather than a solved problem. That is support for the assumption's
       DIAGNOSIS and a caution about its PRESCRIPTION.
    6. Rae, A. & Provan, D. (with co-authors), "Safety clutter: the accumulation and persistence of
       'safety' work that does not contribute to operational safety."
       [VERIFIED: title and the Rae/Provan attribution via a Semantic Scholar record retrieved this run.
       YEAR, JOURNAL AND CO-AUTHORS NOT VERIFIED AND DELIBERATELY NOT ASSERTED. PAPER NOT READ] —
       Retrieved as the counter-pressure the routed question names (measurement burden / metric
       fixation) and reported here per the charter's no-cherry-picking rule because it bounds limb B
       rather than supporting it. Reported mechanisms generating clutter: duplication, generalisation
       and over-specification of safety activities. The implication for 1289 is that a blanket
       per-control effect statistic is itself a candidate piece of clutter unless it is targeted.
       WEIGHT: None in the FOR direction; recorded as the boundary. This is 15b's material and I expect
       to see it there.

  Strength of support: Strong on limb A (the diagnosis). Weak-to-Moderate on limb B (the prescription),
    and the best evidence available for limb B is equivocal in an instructive way.

  Summary: Limb A is about as well supported as an assumption in this register gets, though not by
  research — by the fact that two mature professions have institutionalised the exact distinction
  C2A2 is drawing. Financial audit separates control DESIGN from control OPERATION, forbids taking
  reliance credit for an untested control, sets a higher evidentiary bar for concluding a control works
  than for concluding it does not, and explicitly rules that having walked the mechanism through once is
  not a test of whether it operates. Safety science supplies the general form under Hollnagel's
  work-as-imagined / work-as-done, and offshore barrier-management regimes made periodic barrier
  performance assessment mandatory rather than letting design credit stand. That regulators had to
  mandate these things is itself the evidence that the unmeasured-credit default is real and general,
  not confined to weak control types. Limb B is weaker and more interesting. The one regime found that
  actually mandates a per-control effect statistic — FDA CAPA effectiveness checks — reportedly finds
  inadequate CAPA in the majority of its warning letters, with failure to verify effectiveness before
  closure among the most-cited deficiencies. Mandating the statistic did not close the gap; it relocated
  it into a new compliance surface. So the prescription is operable and enforceable, but the evidence
  that it CHANGES OUTCOMES rather than adding a reporting layer was not found, and the safety-clutter
  literature supplies a named mechanism by which it might not.

  Caveats:
  (a) THE EVIDENCE BASE IS DOCTRINE, NOT MEASUREMENT. Every limb-A source is a professional standard, a
      regulatory requirement or a conceptual framework. I located NO study measuring what fraction of
      controls in any real register carry an effectiveness statistic, nor any measured effect size for
      introducing one. The assumption is supported by convergent professional consensus, which is
      strong warrant of a particular and limited kind, and it should be recorded as such rather than as
      an empirical finding.
  (b) CITATION QUALITY IS LOW ACROSS THIS RESULT AND I AM NAMING IT. Of six sources, ONE has a verified
      title-plus-attribution (Rae & Provan, via Semantic Scholar) and one has a verified URL and lead
      author (Hollnagel white paper). The audit-standards, barrier-management and CAPA material is
      assembled from search summaries and commercial guidance pages that I did not open. The underlying
      standards (COSO, AS 2201, 21 CFR 820.100) are real and canonical and I am not inventing them, but
      every specific clause attributed to them here is second-hand. Anyone relying on a specific clause
      must open the standard.
  (c) THE PRESCRIPTION'S OWN FAILURE MODE IS DOCUMENTED IN ITS BEST TEST CASE. The CAPA finding —
      "marked done, problem not fixed" — is the labelling failure 1289 wants to prevent, occurring
      inside a regime that already requires the label. This suggests the binding constraint is not the
      existence of an effectiveness field but whether anything reads it, which is PREMISE-164's
      addressing argument and PREMISE-123's propagation argument, both already ACTIVE. A per-control
      effect statistic that no scheduled reader consumes reproduces the defect one level up.
  (d) DOMAIN TRANSFER IS UNTESTED. Audit and barrier management govern controls over human and
      organisational processes with regulators, sanctions and external attestors. C2A2 has none of
      those. The mechanism that makes operating-effectiveness testing bite in SOC 2 is that an
      independent party's opinion is at stake; there is no analogue here, and PREMISE-195's caveat
      already records that the off-the-shelf remedy needs design work the sources do not supply.
  (e) SCOPE OF THE ASSUMPTION IS BROADER THAN THE EVIDENCE. "The system has no habit of measuring
      controls at all" is an in-house empirical claim about C2A2 which no literature can confirm or
      deny; it is checkable by counting controls in the register that carry an [action-changed] value,
      and that count is one grep, not a literature search. Only the GENERALISATION was searched.
  (f) SEARCH SCOPE: preliminary-to-moderate — broader search recommended. Four queries. Not covered and
      likely productive: the security-controls effectiveness literature (NIST SP 800-53A assessment
      procedures); bowtie-analysis barrier-degradation research; Reason's defences-in-depth and the
      latent-condition literature; Vaughan on normalisation of deviance; and any empirical work on
      control-self-assessment accuracy versus independent testing, which is the one place a real effect
      size for limb B might exist.

  Recommendation: SUPPORTED (limb A — the diagnosis that designed controls are routinely credited with
    unmeasured effects, on Strong but doctrine-based rather than measured warrant)
    PARTIALLY-SUPPORTED (limb B — the prescription is operable, institutionalised and enforceable, but
    the one mandating regime found shows the requirement becoming its own most-cited deficiency rather
    than closing the gap; no measured outcome change located)

  Note for 15c on the labelling prescription specifically: "a control with no measured effect is a
    DECLARED control and should be labelled as such" has a near-exact and verified precedent in the
    audit design/operation split, and an exact precedent in the register's own PREMISE-171 ("a
    declaration register is not a failure detector"). The vocabulary is available and consistent. What
    is missing is any evidence that applying the label changes what the estate does — and PREMISE-116's
    4-8% expectation is the pre-registered prior against which that should be judged if it is tried.

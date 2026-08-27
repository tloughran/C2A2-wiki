SEARCH-FOR-ASSUMPTION-1221:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1221
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 6 of 14 — Priority High
  Original statement: Three separate runs declared their own budget breaches and continued. Nightly
    verification: "This pass also overran the 4,000-token task budget by roughly 10x — noted in the
    log rather than swallowed." QC sweep: "Budget breached (per-task and per-session), surfaced rather
    than hidden — this is the first run to stop at one pair." Deferred action monitor: "this run
    exceeded the 4,000-token task budget." The evening summary adds: "Fifteenth consecutive breach on
    the Summa cap... Raise the budget, lower the cap, or lower the standard."
    **The stated assumption is that disclosure discharges the rule.**

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1221
    Item type: ASSUMPTION (stated — three verbatim disclosures)
    Transform at each step:
      14a: Extracted from three transcripts and the evening summary (Rules 6 and 12 across four
        independent scheduled runs) and consolidated as one item because the disclosures are identical
        in form. One counter-instance recorded: the QC sweep is the first run to let the budget change
        its output, stopping at one pair rather than doing two badly — a breach absorbed rather than
        merely announced, and the first of its kind in the record. That reading is 14a's own.
      15a: Searched for supporting literature
    Current status: UNTESTED (entering 15a); 15a result WEAKLY-SUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch unavailable to this run; **all sources
    SNIPPET-ONLY.**
    Queries covered: (a) normalisation of deviance and practical drift — mechanisms and named
    countermeasures; (b) near-miss and non-punitive reporting, just culture, psychological safety as
    defences against drift; (c) formal deviation/waiver management — NASA and pharma/GxP practice on
    expiry, compensating controls, named owner; (d) deviation documentation, trending and CAPA in
    regulated quality systems; (e) technical-debt registers as a software analogue of a visible-breach
    register.
    Assessment: **decent coverage of the countermeasure literature; the specific question is only
    partly answered and the answer is conditional.** Limbs NOT covered, honestly: (i) **alert fatigue
    and warning habituation** — named in the adjacent queue item (PRESUMPTION-881) as the relevant
    literature, and I did not search it, partly because it is the natural home of *challenging*
    evidence and 15b's independence must be preserved, partly because budget ran short. Its absence
    means this file's picture is incomplete in a direction I can name. (ii) Vaughan's *The Challenger
    Launch Decision* itself, in the primary; I read only secondary summaries of normalisation of
    deviance and did not verify the argument's structure against the source. (iii) The organisational
    literature on "documented but unresolved" findings — repeat audit findings, recurring
    non-conformances — which is the closest match to fifteen consecutive identical disclosures and
    which I did not reach.

  Supporting evidence found: Partial

  Sources:
    1. Canada Energy Regulator. "Safety Culture Threat: Normalization of Deviance."
       https://www.cer-rec.gc.ca/en/safety-environment/safety-culture/safety-culture-learning-portal/safety-culture-threat-normalization-deviance.pdf
       — Regulator guidance defining the phenomenon (departure from an acceptable standard until the
       adopted practice becomes the new norm) and naming four cultural defences: committed safety
       leadership, vigilance, empowerment and accountability, and resiliency. Note the composition:
       disclosure is not among them as a standalone; every one of the four is a property of an
       *attending organisation*. SNIPPET-ONLY.
    2. "Normalization of Deviance and Practical Drift." ScienceDirect S154614401730964X (also
       ResearchGate 320006562). [authors, journal and year unverified]
       https://www.sciencedirect.com/science/article/abs/pii/S154614401730964X
       — Practice implications given as "a robust safety culture with a focus on **nonpunitive
       reporting**" plus simulation, to reduce error and limit practical drift. This is the closest
       located peer-reviewed statement supporting the assumption's core: reporting is named as a
       primary mechanism against drift. SNIPPET-ONLY.
    3. EcoOnline. "Normalisation of deviance: why safety leaders get blindsided by drift" and "Safety
       drift: your safety program is working – until it isn't."
       https://www.ecoonline.com/en-ca/blog/normalization-of-deviance/ ·
       https://www.ecoonline.com/en-us/blog/safety-drift-your-safety-program-is-working-until-it-isnt/
       — Practitioner statement of the countermeasure set: "encouraging near-miss reporting without
       blame, tracking leading indicators rather than just injury rates, verifying that critical
       controls are actually followed, and regularly comparing work-as-done to work-as-written.
       **Visibility and psychological safety are the core defences.**" The phrase "visibility ... is a
       core defence" is the most directly supportive sentence located for ASSUMPTION-1221. Vendor blog,
       not peer-reviewed; weight accordingly, and note that in the same list visibility is paired with
       *verification* and with comparison of work-as-done against work-as-written — neither of which
       a self-disclosure performs. SNIPPET-ONLY.
    4. NASA. "GRC Project Deviation/Waiver Process," GLPR-7120.5.20-B.
       https://www.nasa.gov/wp-content/uploads/2025/04/glpr-7120-5-20-b.pdf
       and NASA Software Engineering Handbook, SWE-126 "Waiver and Deviation Considerations."
       https://swehb.nasa.gov/display/7150/SWE-126+-+Waiver+and+Deviation+Considerations
       — Primary institutional documents. Key supporting point: a breach of a requirement is handled
       by a *formal, recorded, adjudicated* instrument, and "waivers and deviations and other relief
       from requirements are **not granted on a permanent basis**." Relief from requirements for
       safety-critical software is evaluated "with increased rigor." Establishes that the correct
       response to a known standing breach is a governed exception with an owner and an end date —
       which is a stronger form of what 14a's runs are gesturing at, and also a form none of them
       used. SNIPPET-ONLY.
    5. "Temporary Risk Waiver Explained: what keeps a short-term exception contained."
       https://headlinepodcast.us/blog/temporary-risk-waiver-explained-short-term-exceptions
       — Practitioner synthesis with the sharpest statement of the boundary condition: a waiver
       "accepts a named gap for a limited time, with compensating controls and a review date"; it
       "must stay visible inside the broader governance system"; "the permission should end on a date,
       not when the team remembers"; and — decisively for this item — "if one of them is vague, the
       document stops being a control and **starts becoming decoration**." Low-authority source but
       the formulation is exactly on point and I record it as such. SNIPPET-ONLY.
    6. "Deviation Management in the FDA-Regulated Industries: Basics and Best Practices." The FDA
       Group. https://www.thefdagroup.com/blog/deviation-management
       and "Deviations, CAPA, and Change Control: A Workflow Guide." IntuitionLabs.
       https://intuitionlabs.ai/articles/deviations-capa-change-control
       — Documents the mechanism that converts disclosure into effect: logged deviations are
       **trended**, and "recurrence and risk" are the deciding factors for whether a CAPA is opened;
       "periodic reviews of logged deviations can reveal trends needing urgent action." Directly
       supportive of the assumption's premise that recording a breach is not idle — but only where the
       trending step exists. Fifteen consecutive identical breaches is precisely the recurrence signal
       these systems are built to trip on. SNIPPET-ONLY.
    7. "Handling Protocol Deviations: CRC's Comprehensive Guide." CCRPS.
       https://ccrps.org/clinical-research-blog/handling-protocol-deviations-crcs-comprehensive-guide
       — On reporting culture: sites improve by "normalizing fast escalation, clear documentation, and
       prevention-focused review," and concealment "turns a manageable event into a credibility
       crisis." Supports the disclosure-over-concealment half of the assumption strongly; note the
       triad again includes *review*, which is the missing member here. SNIPPET-ONLY.
    8. "Using a 'Technical Debt Register' in Scrum." Scrum.org.
       https://www.scrum.org/resources/blog/using-technical-debt-register-scrum
       and "How to use a technical debt register." LogRocket.
       https://blog.logrocket.com/product-management/how-to-use-technical-debt-register/
       — Software analogue: a debt register makes accepted shortcuts visible, "easier to monitor,
       discuss, and make informed decisions about." But the same sources are explicit that the
       register works by feeding a *backlog with allocated capacity* — "treating debt items as backlog
       tickets tagged by type and severity, and allocating a fixed percentage of each sprint to
       remediation" — i.e. visibility is the input to a remediation budget, not a substitute for one.
       Practitioner sources. SNIPPET-ONLY.

  Strength of support: Weak to Moderate

  Summary: The literature supports a conditional version of the assumption and not the version as
    stated. What is well supported: that surfacing rather than concealing a deviation is the correct
    first move, and that non-punitive reporting and visibility are named — repeatedly, including by a
    regulator and in the peer-reviewed practical-drift literature — as core defences against
    normalisation of deviance (1–3, 7). What is equally consistently attached to that claim, in every
    source found, is a **second step performed by someone other than the discloser**. The safety-
    culture sources pair visibility with verification and with comparing work-as-done to
    work-as-written (3). The regulator's four defences are all properties of an attending organisation
    (1). The deviation-management systems convert records into action through *trending*, with
    recurrence as the trigger for a CAPA (6). The waiver frameworks require a named owner, an
    expiration date and compensating controls, and NASA is explicit that relief from requirements is
    never granted permanently (4). The technical-debt register works by feeding a remediation budget
    (8). On this evidence, disclosure is a necessary component of a mechanism that prevents
    normalisation; nothing found supports it as a sufficient one. The one practitioner source that
    addresses the degenerate case states it flatly: an exception whose terms are vague "stops being a
    control and starts becoming decoration" (5). Fifteen consecutive identical disclosures with no
    adjudication is closer to that description than to any of the endorsed patterns.

  Caveats: (1) All SNIPPET-ONLY; five of the eight source-groups are practitioner or vendor writing,
    and I could not verify authorship or year on the one peer-reviewed item (2). The evidence base for
    this item is the weakest of the seven I searched. (2) **Selection asymmetry I should name:** my
    remit is the supportive direction, and the supportive framing of this question ("does disclosure
    prevent normalisation") is one the literature does not really pose. The literature poses "what
    prevents normalisation," answers with a bundle, and disclosure is one item in the bundle. Reading
    that as support for disclosure-alone would be exactly the cherry-picking my definition forbids, so
    I have not. (3) I did not search alert fatigue or warning habituation (see Search scope), which is
    the adjacent literature named on PRESUMPTION-881 and where the disconfirming case most likely
    lives; this file should not be read as a complete picture. (4) I did not verify Vaughan in the
    primary. The Challenger case as usually told is a hard case for the assumption — O-ring erosion
    was documented, discussed and reported repeatedly across flights, and normalised anyway — but I am
    not citing it because I did not read it this run, and I flag that I have declined to lean on a
    familiar example I have not verified. (5) Domain transfer: every framework here presumes a
    reviewing body with authority to grant, deny or expire an exception. C2A2's disclosures go into a
    log read by a review gate that has been silent; the transfer condition is not met. (6) 14a's
    recorded counter-instance — the QC sweep stopping at one pair — is, on this literature, the
    behaviour that actually matters: a breach that changed the output rather than only the record.
    Nothing found contradicts 14a's reading of it, and the deviation-management sources would classify
    it as the beginning of a corrective action rather than a disclosure.

  Recommendation: WEAKLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1221
    Supported sub-claims: (i) that surfacing a deviation is correct and materially better than
      concealing it, with concealment carrying a distinct additional harm; (ii) that visibility and
      non-punitive reporting are named defences against normalisation of deviance in safety-critical
      practice; (iii) that recorded deviations become effective through recurrence-triggered trending
      and formal corrective action; (iv) that a governed exception requires a named owner, an expiry
      date and compensating controls, and is never permanent.
    Unsupported sub-claim: **that disclosure alone discharges the rule.** No located source treats
      disclosure as self-sufficient; every one attaches an adjudication, verification or remediation
      step performed by a second party.
    Unaddressed: **repeated, honest, unanswered self-disclosure by the constrained party itself.**
      The waiver and deviation literatures describe an actor disclosing *to* an authority that
      responds. I found nothing on the case where the discloser, the breacher and the record-keeper
      are the same agent and the authority does not answer — fifteen consecutive identical
      disclosures with no ruling. That configuration appears undescribed, and it is worth noting that
      it is structurally the same gap ASSUMPTION-1218 hit from the monitoring side (escalation into an
      unresponsive channel). Two independent items in this cohort converge on one missing literature:
      **what an autonomous agent should do when its governance channel does not answer.** I record
      that convergence as the most useful thing this search produced.

SEARCH-FOR-PRESUMPTION-881:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-881
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake)
  Original statement: "[inferred] That a loudly surfaced breach is a discharged breach — that
    disclosing a violated constraint is compliance with it."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-881
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day disclosures with identical form and no run asking what the
        disclosure was for. High confidence. 14b records that the surfacing run is itself an instance,
        so the presumption is not stated from outside the population it describes.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-26, three queries. Limbs covered: (a) reporting culture / just
    culture and its claimed role in preventing normalisation of deviance; (b) formal waiver and
    deviation regimes in safety-critical engineering (NASA), as the best-developed model of
    *documented* non-compliance; (c) Vaughan's normalisation-of-deviance account and its stated
    countermeasures. Supplementary: the ITIL Known Error Database, read as an analogue for a register
    of documented-but-unfixed defects.
    Assessment: **moderate coverage, one limb missing entirely.** The alert-fatigue literature named
    in the queue entry as "the adjacent literature" was **not searched** — the search budget went to
    the reporting-culture and waiver limbs. That is a material omission for this item, since alert
    fatigue is the mechanism by which repeated disclosure would *cause* rather than prevent
    normalisation, and it would likely have supplied the sharpest test. Also not run: literature on
    non-response to escalation, and any empirical study of disclosure regimes with no adjudicating
    authority. Recorded plainly as a shortfall.

  Supporting evidence found: Partial

  Sources:
    1. NASA, "Waivers and Deviations," Software Assurance and Software Safety Handbook, and
       "SWE-126 — Waiver and Deviation Considerations," NASA Software Engineering Handbook.
       https://swehb.nasa.gov/display/SAEHB/Waivers+and+Deviations ;
       https://swehb.nasa.gov/spaces/7150/pages/16450524/SWE-126+-+Waiver+and+Deviation+Considerations ;
       and NASA GRC, "GRC Project Deviation/Waiver Process," GLPR-7120.5.20B,
       https://www.nasa.gov/wp-content/uploads/2025/04/glpr-7120-5-20-b.pdf
       — The strongest supportive source, and also the sharpest qualifier. It establishes that
       documented, authorised non-compliance is a *legitimate, institutionalised* state in a
       safety-critical system: a deviation or waiver is "documented authorization releasing a program
       or project from meeting a requirement." So disclosure of a breach can indeed discharge it. But
       the standard's whole architecture is that a waiver is *granted*, not merely *declared* — it
       requires a documented request stating assumptions, constraints, alternatives and impacts, and
       co-approval by a named Technical Authority, with increased rigour for safety-critical classes.
       This supports the presumption's form while identifying the missing element in the generating
       case: an approver. SNIPPET-ONLY.
    2. Banja, J. "When Doing Wrong Feels So Right: Normalization of Deviance."
       *Journal of Healthcare Risk Management* (2010) — PubMed 25742063,
       https://pubmed.ncbi.nlm.nih.gov/25742063/ ; ResearchGate copy,
       https://www.researchgate.net/publication/273148155
       [author attribution from title/venue; year unverified]
       — Standard clinical treatment of normalisation of deviance. Located as the principal
       peer-reviewed entry point for the mechanism. ABSTRACT-ONLY.
    3. Canada Energy Regulator, "Safety Culture Threat: Normalization of Deviance," Safety Culture
       Learning Portal. https://www.cer-rec.gc.ca/en/safety-environment/safety-culture/safety-culture-learning-portal/safety-culture-threat-normalization-deviance.html
       and PDF at the same path
       — Regulator-issued statement that a reporting culture in which people can raise safety concerns
       without reprisal is key to preventing normalisation, and conversely that "when workers are
       afraid to report safety concerns or when there is a lack of transparency about incidents, unsafe
       practices can fester and become normalized." This is the most direct located support for the
       presumption's spirit: surfacing is the named antidote. SNIPPET-ONLY.
    4. Vaughan, D. *The Challenger Launch Decision* (1996), as summarised in: Wikipedia,
       "Normalization of deviance," https://en.wikipedia.org/wiki/Normalization_of_deviance ;
       Patient Safety Learning hub, "Diane Vaughan's theory of the normalisation of deviance,"
       https://www.pslhub.org/learn/improving-patient-safety/human-factors-improving-human-performance-in-care-delivery/barriers/diane-vaughans-theory-of-the-normalisation-of-deviance-r1284/ ;
       Sage, *Encyclopedia of Criminological Theory*, "Vaughan, Diane: The Normalization of Deviance,"
       https://sk.sagepub.com/ency/edvol/criminologicaltheory/chpt/vaughan-diane-normalization-deviance
       — Vaughan's own account cuts both ways for this item and I report it as such. Supportively:
       her named countermeasure is education/visibility, and normalisation is defined as the point at
       which deviance "no longer feels wrong" — which explicit, repeated, discomfited disclosure
       arguably prevents. Against: the Challenger mechanism was itself one of *documented* anomalies —
       each recorded O-ring anomaly made the next more acceptable, the baseline shifting while the
       record was complete throughout. Documentation did not prevent drift there. SNIPPET-ONLY.
    5. Safety-culture practitioner literature on just culture and reporting, e.g. EcoOnline,
       "Normalisation of deviance: why safety leaders get blindsided by drift,"
       https://www.ecoonline.com/en-ca/blog/normalization-of-deviance/ ; US Army, "When Cutting Corners
       Becomes the Norm," https://www.army.mil/article/286745/ ; Acclivix,
       https://www.acclivix.com/casestudies/normalization-of-deviance
       — Consistent practitioner position that transparent incident reporting plus a blame-free
       reporting culture is the mechanism for surfacing deviation before it normalises. Note the
       recurring qualifier in these same sources: deviations must be *addressed promptly and
       consistently, regardless of perceived severity* — reporting is stated as necessary, never as
       sufficient. Non-peer-reviewed. SNIPPET-ONLY.
    6. ITIL Known Error Database, as documented in: Wikipedia, "Known error,"
       https://en.wikipedia.org/wiki/Known_error ; IT Process Wiki, "Problem Management,"
       https://wiki.en.it-processmaps.com/index.php/Problem_Management ; InvGate, "KEDB Explained,"
       https://blog.invgate.com/kedb
       — Analogous support: an entire ITSM process area is built on the premise that a defect with a
       documented root cause and a recorded workaround is in a *legitimate managed state* rather than
       an outstanding failure. The KEDB is the closest institutional analogue to "a surfaced breach is
       a discharged breach." Caveat inherent in the definition: a known error carries a *status of fix
       efforts*, i.e. the record is a tracking device, not a closure. SNIPPET-ONLY.

  Strength of support: Moderate

  Summary: The safety literature supports the presumption's underlying intuition strongly: transparent
    reporting, without fear of reprisal, is the named mechanism for preventing normalisation of
    deviance, and the failure mode these sources warn about is *silence*, not disclosure. Formal
    engineering practice goes further and gives disclosure a discharging function outright — NASA's
    waiver and deviation regime makes documented non-compliance a legitimate project state, and ITIL's
    Known Error concept does the same for defects with a documented cause and workaround. On these
    accounts, an agent that breaches a budget and says so loudly is behaving exactly as a good safety
    system requires. The qualification, present in every supportive source without exception, is that
    disclosure is treated as *necessary and not sufficient*: NASA's waiver must be granted by a named
    Technical Authority with co-approval, the safety-culture sources require deviations to be
    "addressed promptly and consistently," and ITIL's known error record carries a fix status. None of
    these is a bare declaration. The strongest counterweight is internal to Vaughan's own case:
    Challenger's O-ring anomalies were documented throughout, and it was the accumulation of recorded,
    survived anomalies that shifted the baseline. Disclosure without ruling is the exact configuration
    in which her mechanism operated.

  Caveats: (1) The alert-fatigue limb — the mechanism most likely to overturn the presumption — was
    not searched at all. This result should be read as incomplete on that axis. (2) Every supportive
    source presumes a responder: an approving authority, a safety committee, a problem manager. The
    generating case has fifteen consecutive disclosures and no ruling; no located source addresses a
    disclosure regime with a permanently absent adjudicator. (3) The waiver analogy is only as strong
    as its approval step, which is absent here — a self-declared waiver is not what NASA means by a
    waiver. (4) Vaughan's own case is a counter-instance, not merely a caveat: documentation coexisted
    with drift. (5) The safety-culture sources are practitioner and regulator material rather than
    controlled studies; I located no measurement of whether reporting rates actually predict reduced
    normalisation. (6) All sources read at snippet or abstract level.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Supported sub-claims: (i) that surfacing a violation is the correct and prescribed behaviour, and
    that concealment rather than disclosure is the recognised precursor of normalisation; (ii) that
    formal regimes exist (NASA waivers/deviations; ITIL known errors) in which documented
    non-compliance is a legitimate managed state rather than an open failure.
    Unsupported sub-claim: that disclosure *alone*, without adjudication, discharges the constraint.
    Every supportive source requires an approval or disposition step that the generating case lacks.
    Unaddressed sub-claim: **what repeated, honest, unanswered disclosure does to a constraint over
    time — specifically, how many unruled disclosures constitute a de facto amendment to the rule.**
    I located no literature on disclosure regimes without an adjudicator, and none that quantifies the
    point at which a documented-but-unruled breach becomes the operative norm. This is the item's own
    question, 14b asked it precisely, and it appears genuinely open. Flagged as a candidate original
    contribution, with the caveat that the unsearched alert-fatigue literature may already contain a
    partial answer.

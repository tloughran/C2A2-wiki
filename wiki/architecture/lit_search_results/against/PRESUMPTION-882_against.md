SEARCH-AGAINST-PRESUMPTION-882:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-882
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-882 (Priority Medium)
  Original statement: [inferred] That a complete corpus is a finished one — that once a series stops
    growing, absences within it are permanent and can be judged.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-882
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the word "now" in the verification's own framing ("un-back-cited across the
           whole corpus now that the series is complete"), read against the same night's repair
           transcripts. Medium confidence — the inference depends on treating repair-added citations
           as the same operation as original back-citation, which is 14b's construction.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Three WebSearch queries executed 2026-08-26 (plus one shared with PRESUMPTION-884).
    Literatures reached: (a) the saturation debate in qualitative research and its recent critiques;
    (b) right-censoring and incomplete-observation bias in survival analysis; (c) annotation
    incompleteness / partial-annotation bias in NLP and IR evaluation; (d) capture-recapture
    estimation of residual defects after software inspection. Venues reached: SAGE (Qualitative
    Inquiry; International Journal of Qualitative Methods), PLOS One, PMC, Taylor & Francis (Cogent
    Social Sciences), arXiv (stat.ME, cs.IR, cs.CL), ACL Anthology (COLING 2012), IEEE Xplore and
    Springer abstracts for the capture-recapture work.
    NOT COVERED, and these matter: (i) the *bibliometric* literature on citation accrual over time —
    citations to a document continue to accumulate long after the document is finished, which is the
    most on-point analogy for "back-citation is not an operation confined to writing time" and is a
    conspicuous gap; (ii) the archival-science distinction between a *closed* record series and a
    *processed* one, which is almost exactly the complete/finished distinction 14b drew and which I
    did not reach; (iii) missing-data-mechanism theory (MCAR/MAR/MNAR) in primary form — I reached the
    censoring literature but not Rubin's framework, which is what licenses or forbids treating an
    absence as informative. Search confidence: MODERATE. The evidence found is analogical rather than
    direct: no source addresses "back-citation in a longitudinal wiki corpus," so every citation here
    is a transfer from an adjacent domain and should be weighted accordingly.

  Challenging evidence found: Yes

  Sources:
    1. Malcolm Tight. 2024. "Saturation: An Overworked and Misunderstood Concept?" Qualitative Inquiry.
       https://journals.sagepub.com/doi/10.1177/10778004231183948 — Characterises saturation claims as
       "problematic in practice," often appearing as "an unevidenced and dogmatic statement seeking to
       justify that a piece of research is complete." The word "now" in the verification's framing is
       exactly such a statement: a declaration of completeness doing licensing work that has not been
       independently established. ABSTRACT-ONLY (paywalled).
    2. [authors unverified]. 2018. "Saturation in qualitative research: exploring its
       conceptualization and operationalization." Quality & Quantity.
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5993836/ — The theoretically sharpest statement:
       "the uncertain logic underlying saturation — as essentially a **predictive statement about the
       unobserved based on the observed** — results in equivocation." This is the general form of
       C2A2's error. Judging an absence as permanent is a prediction about future work, not an
       observation about the corpus, and the verification pass presented it as the latter. FULL-TEXT
       available open access at PMC; I read the abstract and search-surfaced passages, not the whole
       article.
    3. [authors unverified]. 2020. "Saturation controversy in qualitative research: Complexities and
       underlying assumptions. A literature review." Cogent Social Sciences.
       https://www.tandfonline.com/doi/full/10.1080/23311886.2020.1838706 — Adds that inadequate
       saturation practice "can result in premature cessation of data collection, incomplete
       theoretical frameworks, and potentially flawed conclusions." Direct analogue: declaring the
       absences permanent stops the repair work that was, on the same night, closing them.
       FULL-TEXT (open access); read via search summary.
    4. [authors unverified]. 2020. "Effect of right censoring bias on survival analysis."
       arXiv:2012.08649. https://arxiv.org/abs/2012.08649 — Supplies the formal name for C2A2's error.
       An observation is right-censored when the event may occur after observation ends; the critical
       distinction is that "censoring acknowledges that the event may have occurred after observation
       ended, rather than assuming it did not occur," and treating incomplete observations as negative
       findings "produces systematic bias" — specifically downward. C2A2's un-back-cited CROSS and
       FLAG ids are censored observations, not confirmed absences: the repair pass is a live
       back-citation mechanism that has covered five days of 307. ABSTRACT-ONLY.
    5. [authors unverified]. 2012. "Giving Meaning to the Evaluation Metrics." COLING 2012.
       https://aclanthology.org/C12-2079.pdf — "False negatives in annotation occur when an annotator
       fails to annotate an element belonging to the reference, and such incompleteness in manually
       annotated corpora can bias evaluation performed using that corpus as a reference." Closest
       methodological analogue: C2A2 is using an incompletely-annotated corpus as its own reference
       standard and reading the un-annotated remainder as a defect list. FULL-TEXT PDF available at
       the ACL Anthology link; read via search summary only.
    6. [authors unverified]. 2024. "Evaluating D-MERIT of Partial-annotation on Information Retrieval."
       arXiv:2406.16048. https://arxiv.org/pdf/2406.16048 — Modern restatement: "modern retrieval
       datasets often lack rigorous annotation, with evaluation based on datasets with falsely labeled
       negatives being highly dependent on which passages are selected for annotation." Directly
       relevant given that the repair pass has covered 5 of 307 days — the annotated subset is 1.6% of
       the corpus and is not a random sample of it. SNIPPET-ONLY.
    7. Capture-recapture literature for post-inspection residual defects — e.g. "A comprehensive
       evaluation of capture-recapture models for estimating software defect content," IEEE TSE
       (https://ieeexplore.ieee.org/document/852741/) and "Capture-recapture in software inspections
       after 10 years research" (https://www.researchgate.net/publication/222300754) [authors
       unverified for both] — Establishes the *methodological alternative* the presumption skipped:
       when you want to know how much is really missing from an inspected artefact you estimate it
       from overlap between independent passes, you do not read the un-inspected remainder off the
       page as a count. "Decisions about whether re-inspection is required usually rely on the
       estimated number of undiscovered defects." C2A2 has one pass, no overlap, and therefore no
       basis for an estimate. ABSTRACT-ONLY.
    8. [authors unverified]. "In Validations We Trust? The Impact of Imperfect Human Annotations as a
       Gold Standard on the Quality of Validation of Automated Content Analysis."
       https://www.researchgate.net/publication/339741525 — "Imperfect human judgments can make
       reliable measurements 'reliably wrong'." Relevant because the completeness verdict is stable
       and repeatable and would be equally stable if it were wrong. ABSTRACT-ONLY.

  Strength of challenge: Moderate

  Summary: The presumption conflates two distinct properties — a corpus that has stopped *accessioning*
  and a corpus that has stopped *changing* — and every literature reached treats that conflation as an
  error with a known direction of bias. The saturation literature is the closest fit in spirit: recent
  critiques characterise completeness declarations as frequently "unevidenced and dogmatic statements
  seeking to justify that a piece of research is complete," and identify the underlying logical problem
  precisely, that saturation is "a predictive statement about the unobserved based on the observed."
  The survival-analysis framing names the error formally: an un-back-cited id in a corpus over which a
  live repair pass is still running is a *right-censored* observation, and treating right-censored
  observations as confirmed negatives produces systematic downward bias — which is the exact operation
  the verification performed on the strength of the word "now." The annotation literature supplies the
  same result from a third direction, and adds the decisive quantitative consideration: the repair pass
  has covered five days out of 307, so the annotated fraction is about 1.6% and is not a random sample.
  The capture-recapture tradition shows what the discipline actually does in this situation — estimate
  the residual from independent overlapping passes rather than count the unmarked remainder — and C2A2
  has neither the second pass nor the estimate. Rated Moderate rather than Strong for one honest
  reason: every source here is an analogy. Nothing found addresses back-citation in a longitudinal
  wiki corpus, and 14b's own confidence note is right that the inference turns on whether repair-added
  citations are the same operation as original back-citation. If they are not — if a repair-added
  citation is a genuinely different and rarer event — the censoring framing weakens considerably.

  Specific risks: (a) Work-in-progress reclassified as defect — the named risk, and it is
  administratively expensive: the un-back-cited CROSS and FLAG ids would enter the register as
  findings requiring disposition rather than as work not yet done, adding to a gate already at 74
  (PRESUMPTION-883). (b) Premature cessation — per the saturation literature, declaring the absences
  permanent removes the rationale for the repair pass that was, on the same night, closing four of
  them. The declaration could stop the mechanism that would have falsified it. (c) Directional bias
  with an unknown magnitude: the censoring result says the bias is downward and systematic, but with
  1.6% coverage the magnitude is unestimable — C2A2 cannot currently say whether the true residual is
  slightly or wildly smaller than the counted one. (d) A stable wrong number: the completeness verdict
  is repeatable, so re-running the verification will reproduce it, and reproducibility will be
  mistaken for validity ("reliably wrong"). (e) Second-order: any downstream claim that cites the
  un-back-cited count as a corpus property inherits the bias, and per PRESUMPTION-876 an append-only
  register makes such quoted figures hard to retract.

  Mitigations available:
    - Restate the finding with its observation window attached: "un-back-cited as of 2026-08-25, over a
      corpus with an active repair pass at N days/night." This is nearly free and converts a false
      absolute into a true relative.
    - Estimate rather than count. Project the observed repair rate (four back-citations added across
      five days of 307) over the un-back-cited set and report the projected residual with a horizon.
      14b already proposed this and it is the correct move.
    - Run a second independent pass over a sample and use capture-recapture on the overlap to estimate
      true residual absences. This is the discipline's standard answer and requires only a sample, not
      a full re-verification.
    - Separate the two populations in the register: *un-back-cited and not yet repair-visited* versus
      *un-back-cited after repair visit*. Only the second is evidence of a genuine absence. Currently
      they are one number.
    - Do not let the completeness declaration license a change in disposition policy until the
      estimate exists. The cheapest error here is to leave the ids as work outstanding for another
      cycle; the expensive one is to convert 300+ items into findings.

  STEELMAN:
    Item: PRESUMPTION-882
    Strongest counterargument: The censoring analogy assumes the repair pass will eventually reach the
    whole corpus, and there is no evidence it will — five days of 307 in one night is not a rate that
    obviously continues, and repair passes in this system are triggered by *specific* findings rather
    than running as a sweep. If back-citation repair is opportunistic rather than systematic, then the
    un-back-cited set is not censored at all; it is simply the set of things nobody has had a reason to
    fix, and that set is stable, judgeable, and correctly reported as a corpus property. Further, the
    saturation critiques are aimed at claims about *unobserved data* — samples not yet collected —
    whereas C2A2's series is fully observed: all 307 days exist and have been read. Declaring the
    accession closed is a factual statement about the corpus, not a predictive one, and the
    verification pass was entitled to make it. Finally, there is a real cost to the alternative:
    holding 300+ ids in a permanently provisional "may yet be closed" state means they are never
    counted, never dispositioned, and never fixed — which is exactly the terminus PRESUMPTION-879
    describes. Declaring them findings is what makes them actionable.
    What would need to be true for C2A2 to be safe: (i) the back-citation repair mechanism must be
    genuinely exhausted, not merely paused — five days covered out of 307 in a single night is prima
    facie evidence it is not; (ii) the five days already repaired must be a *representative* sample of
    the 307, not the five most defect-dense; if they were selected for being broken, the residual rate
    over the remaining 302 is unestimable from them; (iii) back-citation must be an operation that
    properly belongs to writing time, so that its later occurrence is an exception rather than the
    normal course — 14b flags this as the load-bearing and unverified premise, and it is; (iv) nothing
    downstream may quote the un-back-cited count as a fixed corpus property before the estimate
    exists; (v) the gate must be able to absorb 300+ new findings, which PRESUMPTION-883 says it
    cannot.
    How to test: Directly testable and cheap. Take a random sample of ~20 un-back-cited CROSS/FLAG ids
    from days *not* yet touched by the repair pass, and run the repair procedure on them blind. The
    fraction that close is the estimate the presumption needs and does not have. If a substantial
    fraction close, the absences are censored observations and the completeness declaration is
    premature; if almost none close, the absences are real and the presumption survives. A second
    test, from the capture-recapture tradition: have two independent passes back-cite the same sample
    of days and use the overlap to estimate the residual. A third, nearly free: check whether the five
    days already repaired were selected at random or because they were flagged — if the latter, the
    observed repair rate is an upper bound and cannot be projected forward, which weakens the challenge
    and should be reported as such.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single, currently
      unresponsive human review gate, and not one of the seven presumptions conditions its behaviour
      on that gate's responsiveness.** PRESUMPTION-882 is the *secondary* case in the batch — the gate
      is not the mechanism of the error, but it is the destination of its consequence: the item's own
      risk note observes that misclassifying work-in-progress as findings sends 300+ items "to a gate
      already at 74." An item's classification decision should not be made without knowing whether the
      receiving queue can absorb it, and currently no producer in this system can see that.
    Literature basis: Little's law under λ > μ (https://en.wikipedia.org/wiki/Little's_law);
      right-censoring bias (arXiv:2012.08649); saturation as "a predictive statement about the
      unobserved based on the observed" (https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5993836/).
    Risk level: Critical (batch-level); High for this item specifically
    Recommendation: Defer the reclassification of un-back-cited ids from "work outstanding" to
      "findings" until (a) the residual estimate exists and (b) the gate has a disposition rate above
      zero. See the identical note on PRESUMPTION-878, -879, -880, -881, -883 and -884.

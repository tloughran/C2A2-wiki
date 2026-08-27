SEARCH-FOR-ASSUMPTION-1206:
  Date searched: 2026-08-26
  Original item: ASSUMPTION-1206
  Queue ref: LIT-QUEUE — 2026-08-25 (Agents 14a + 14b end-of-day intake), item 1 of 14 — Priority Critical
  Original statement: "Verified 307 synthesis files (Days 001–307, the complete series) against the live
    C2A2 wiki... **zero dead citations**: all 979 attributable PRS references, 9 distinct FLAG ids,
    47 distinct CROSS ids, and every cited tradition-wiki path resolve."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1206
    Item type: ASSUMPTION (stated — quoted verbatim)
    Transform at each step:
      14a: Extracted from the Summa 2026 nightly verification (22:00), reported as the corpus-wide
        citation-health headline for the first complete pass over the finished series. Then checked
        against the same day's Summa commentary reviewer and QC sweep transcripts and CHALLENGED on
        register-vs-register evidence within one day: five hand-found citation defects, none of them
        a dead id.
      15a: Searched for supporting literature
    Current status: CHALLENGED (entering 15a); 15a result WEAKLY-SUPPORTED

  Search scope: WebSearch only, 2026-08-26. WebFetch was unavailable to this run (the fetch tool
    refused every URL not already in the provenance set), so **every source below is SNIPPET-ONLY**:
    read via search-result summaries, not full text. This is a real limitation and the assessments
    are calibrated to it.
    Queries covered: (a) measured quotation- and citation-error rates in corpora (medical, general
    science, history, education); (b) the terminological distinction between citation accuracy
    (metadata) and quotation accuracy (does the source support the claim); (c) link rot / reference
    rot / content drift as an integrity measure and its known limits; (d) what automated
    reference-checking tools can and cannot detect.
    Assessment: **adequate for the narrow question, preliminary overall.** Limbs NOT covered, for
    honesty: (i) I found no study that directly regresses reference-integrity pass rates against
    quotation-accuracy rates in the same corpus — that is the precise question asked and I could not
    locate an answer to it; (ii) I did not search the library-and-information-science literature on
    catalogue-integrity auditing, which may hold the closest methodological analogue; (iii) I did not
    search for work on internally-linked knowledge bases or wikis specifically (as opposed to
    scholarly reference lists), which is C2A2's actual object.

  Supporting evidence found: Partial

  Sources:
    1. "Accuracy of cited 'facts' in medical research articles: A review of study methodology and
       recalculation of quotation error rate." PLOS One / PMC5599002. [authors unverified]
       https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0184727
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5599002/
       — Meta-analysis of 28 quotation-error studies; overall rate 25.4%, recalculated to 14.5%
       (95% CI 10.5–18.6%) after methodological correction. Relevance to the FOR direction is
       indirect but real: the paper's own recalculation exercise shows that headline defect figures
       are highly method-dependent, which supports reporting a *narrowly defined, reproducibly
       measured* quantity (id resolution) rather than a broad and contested one. It does not support
       the inference from resolution to accuracy. SNIPPET-ONLY.
    2. "Quotation errors in general science journals." Proceedings of the Royal Society A, 476(2242),
       20200538 (2020). [authors unverified]
       https://royalsocietypublishing.org/doi/10.1098/rspa.2020.0538
       — Total error rate 25% in general science journals, described as tracking well with other
       fields. SNIPPET-ONLY.
    3. "Unverified history: an analysis of quotation accuracy in leading history journals."
       Scientometrics (2023), DOI 10.1007/s11192-023-04755-w. [authors unverified]
       https://link.springer.com/article/10.1007/s11192-023-04755-w
       — Error rate 24.27% in leading history journals. Included because history is a *humanities*
       corpus with commentary-style citation, structurally closer to C2A2's synthesis files than
       biomedical reporting is. SNIPPET-ONLY.
    4. "Quotation accuracy in educational research articles." Educational Research Review /
       ScienceDirect, S1747938X21000531. [authors unverified]
       https://www.sciencedirect.com/science/article/pii/S1747938X21000531
       — 500 randomly sampled citations; overall accuracy 85%. SNIPPET-ONLY.
    5. Wakeling, S. et al. (2025). "How do authors perceive the way their work is cited? Findings
       from a large-scale survey on quotation accuracy." Journal of the Association for Information
       Science and Technology. https://asistdl.onlinelibrary.wiley.com/doi/10.1002/asi.70000
       — Large-scale survey approach: asks cited authors whether citing papers represented them
       correctly. Methodologically the nearest thing to an independent-referee check on a corpus.
       SNIPPET-ONLY. [first-author surname read from the URL slug; co-authors unverified]
    6. "Assessing citation integrity in biomedical publications: corpus annotation and NLP models."
       PMC11231046. [authors, journal and year unverified]
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11231046/
       — States the field's standing distinction: *citation accuracy* errors are errors in citation
       metadata (author names, dates); *quotation accuracy* errors are failures of the reference to
       support the statement it is cited for. This is the strongest single piece of *supportive*
       evidence available for ASSUMPTION-1206's narrow reading: the two classes are recognised as
       distinct and separately measurable, so reporting one of them is a legitimate act, not a
       category error. The same source also notes that metadata-class citation errors "have become
       less common in the era of digitization and citation managers." SNIPPET-ONLY.
    7. "Reference rot in scholarly statement: threat and remedy." Insights (UKSG),
       DOI 10.1629/uksg.237. [authors unverified] https://insights.uksg.org/articles/10.1629/uksg.237
       — Establishes reference rot (link rot + content drift) as a tracked, first-class integrity
       dimension of the scholarly record. Supports the premise that resolvability is a real and
       reportable property. SNIPPET-ONLY.
    8. "Scholarly Context Not Found: One in Five Articles Suffers from Reference Rot." PLOS One
       (2014), DOI 10.1371/journal.pone.0115253. [authors unverified]
       https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0115253
       — ~1M references across ~400,000 articles: 1 in 5 articles carries a bad reference; 7 in 10
       of those with web references do. Supports the claim that a zero-dead-link result over 979
       references is a genuinely unusual and non-trivial outcome against field base rates.
       SNIPPET-ONLY.
    9. "Reference Rot in the Repository: A Case Study of Electronic Theses and Dissertations (ETDs)
       in an Academic Library." Information Technology and Libraries. [authors and year unverified]
       https://ital.corejournals.org/index.php/ital/article/view/9598
       — 77% of links active, but roughly half of the *active* links showed content drift. This is
       the closest located quantification of the gap the assumption depends on: resolution passing
       while the target no longer says what was cited. Cuts against the strong reading; included per
       the no-cherry-picking rule. SNIPPET-ONLY.

  Strength of support: Weak

  Summary: The literature supports a narrow and a broad reading of ASSUMPTION-1206 very differently.
    The narrow reading — that id resolution over 979 references is a real, reproducible, non-trivial
    integrity measurement worth reporting — is well supported. The citation-integrity literature
    treats metadata/reference-integrity errors as a distinct and separately-measured defect class
    (source 6), the reference-rot literature treats resolvability as a first-class property of the
    scholarly record (7), and the field base rates make a clean sweep genuinely notable: roughly one
    in five articles in a million-reference sample carries a broken reference (8). The broad reading
    — that this figure is *the corpus's citation-health result* — finds no support. The same
    literature that legitimises the measurement also insists on the boundary: citation accuracy
    (metadata) and quotation accuracy (does the source support the claim) are named as two things,
    not one, and the second is described as both more common and harder to detect. Measured
    quotation-error rates across fields run roughly 7.8%–38.2%, mean ~22.4%, with field-level results
    of 25% (general science), 24.3% (history) and 15% (education) (1–4). Most tellingly, the ETD
    study found roughly half of *still-resolving* links had drifted in content (9) — resolution
    passing while the citation had ceased to be true.

  Caveats: (1) Every source is SNIPPET-ONLY; none was read in full, and figures quoted from search
    summaries could be misattributed to the wrong study within a result set. Treat all numbers as
    indicative. (2) I could not find the study the queue actually asks for — a corpus in which
    formal reference integrity and semantic accuracy were measured together, allowing the predictive
    relation to be estimated. Its absence is the central gap. (3) The quotation-error base rates come
    from human-authored scholarly literature with external references; C2A2's synthesis files carry
    *internal* references to a wiki the same system wrote, which is a different failure geometry and
    may have quite different rates in either direction. (4) Source 6's observation that metadata
    errors have declined with digitisation and citation managers weakens the informational value of
    a zero-dead-id result: automated linking makes the automated check easier to pass, which is
    precisely the condition under which passing it means least. (5) The internal challenge that
    generated this item is not answered by anything found: five hand-found defects, all resolving,
    is a rate the literature would predict but cannot corroborate for this corpus.

  Recommendation: WEAKLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: ASSUMPTION-1206
    Supported sub-claims: (i) reference integrity is a recognised, distinct and legitimately
      reportable defect class, separate from quotation accuracy; (ii) a zero-broken-reference result
      over 979 references is notable against documented field base rates for reference rot; (iii) the
      class of defect the check cannot see is well documented and quantified across several fields at
      roughly 15–25%.
    Unsupported sub-claim: that reference-integrity checking *predicts* reference accuracy. I found
      no study anywhere that validates integrity as a proxy for accuracy, and the one located
      measurement bearing on it (source 9) points the other way — roughly half of live links had
      drifted.
    Unaddressed: **no located study measures both reference integrity and quotation accuracy in the
      same corpus and reports their relation.** If C2A2 measured the two on its own 307-file series —
      it already has one automated pass and a hand-reading frame — it would be producing a number the
      literature does not appear to contain. That is a genuine, cheap, in-house contribution, and it
      is a *measurement*, not a further literature question.

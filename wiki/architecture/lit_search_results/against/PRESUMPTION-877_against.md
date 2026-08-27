SEARCH-AGAINST-PRESUMPTION-877:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-877
  Queue ref: LIT-QUEUE — 2026-08-25 (14a + 14b end-of-day intake cohort), Priority Critical
  Original statement: [inferred] That id-resolution *is* citation health — that a reference which
    points at an existing record is thereby a good reference.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-877
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by reading the nightly verification transcript against the same day's two Summa
           frames — a comparison no run made. High confidence: the disjointness of the two defect
           classes recorded as demonstrable, not interpretive. Framed as a question per standing
           instruction.
      15b: Searched for challenging literature. Six WebSearch queries covering citation/quotation error
           taxonomy, measured error rates, the limits of resolution-based and authority-database
           verification, link and reference rot, and content-level citation verification.
    Current status: CHALLENGED

  Search scope: Six WebSearch queries, executed 2026-08-26 (shared query budget with ASSUMPTION-1206,
    which asks the same question from the stated side). Coverage reached: scientometrics and
    research-integrity literature on reference and quotation error; systematic reviews and
    meta-analyses in medicine; one general-science sample (Proc. R. Soc. A); the 2024–2026 arXiv
    literature on automated citation verification; the library-science literature on link and reference
    rot. All sources read as search-result snippets only — **no full text or abstract was fetched**;
    every source is marked SNIPPET-ONLY and all figures are as rendered by the search engine.
    NOT COVERED, and these are material: (a) I could not find, and therefore cannot report, any study
    that measures the presumption's exact quantity — the *conditional* accuracy of references given
    that they resolve, or equivalently the proportion of citation defects invisible to resolution-based
    checking. Every rate I found is a marginal rate over all references in corpora whose reference
    lists are essentially fully resolvable, which supports the inference strongly but does not
    substitute for the direct measurement; (b) I did not reach any validation study of link integrity
    *as* a citation-quality metric — the queue's first limb, "is link integrity treated as a measure of
    citation quality anywhere it has been validated against semantic accuracy?", returned nothing
    affirmative, which is a null result worth recording plainly and is reported below rather than
    padded; (c) humanities and religious-studies citation practice, the nearest analogue to this
    corpus, was not searched; (d) the software test-coverage literature, which supplies the structural
    analogue, was not searched.

  Challenging evidence found: Yes

  Sources:
    1. [authors unverified] 2024. "Detecting Reference Errors in Scientific Literature with Large
       Language Models." arXiv:2411.06101. https://arxiv.org/abs/2411.06101 — Supplies the taxonomy
       that dissolves the presumption. Two disjoint classes: *citation errors* (typographical /
       bibliographic — wrong author, title, journal, year, or arrangement), which "have become less
       common in the era of digitization and citation managers"; and *quotation errors*, "the situation
       where a reference fails to support the statement for which it is cited," which are "more
       pernicious in that they are difficult to detect for humans." Resolution checking is a citation-
       error detector. Nothing in the taxonomy licenses reading it as a quotation-error detector.
       SNIPPET-ONLY.
    2. [authors unverified] 2025. "SemanticCite: Citation Verification with AI-Powered Full-Text
       Analysis and Evidence-Based Reasoning." arXiv:2511.16198.
       https://arxiv.org/html/2511.16198v1 — The presumption stated and rejected by the field that
       builds these tools: authority-database validation detects "incorrect metadata or non-existent
       references, but cannot verify whether citation claims accurately reflect source document
       content. A reference may exist with correct metadata whilst the citing author mischaracterises
       the source's actual findings." Also notes that even systems attempting content verification
       "typically rely on abstract-only analysis rather than examining complete source documents" —
       so the gap persists one level up. SNIPPET-ONLY.
    3. [authors unverified] 2025/2026. "Systematic review and meta-analysis of quotation inaccuracy in
       medicine." https://pmc.ncbi.nlm.nih.gov/articles/PMC12285159/ — 46 studies, ~32,000 quotations,
       16.9% incorrect, ~8.0% major, where major means the source "fails to substantiate, is unrelated
       to, or contradicts the assertion." The decisive detail for *this* item is the meta-regression:
       **no significant improvement in quotation accuracy over recent years**, across precisely the
       period in which DOIs, CrossRef and reference managers drove pointer errors toward zero. If
       resolution were a proxy for accuracy, accuracy should have improved as resolution did. It did
       not. That is as close to a controlled disconfirmation of the presumption as this literature
       offers. SNIPPET-ONLY.
    4. [authors unverified] 2017. "Accuracy of cited 'facts' in medical research articles: A review of
       study methodology and recalculation of quotation error rate." PLOS ONE.
       https://journals.plos.org/plosone/article?id=10.1371%2Fjournal.pone.0184727 — Quotation error
       rate recalculated at 14.5% (95% CI 10.5–18.6%) in corpora with effectively intact reference
       lists. Establishes that the invisible class is not a rounding error. SNIPPET-ONLY.
    5. [authors unverified] 2020. "Quotation errors in general science journals." Proceedings of the
       Royal Society A 476(2242): 20200538.
       https://royalsocietypublishing.org/rspa/article/476/2242/20200538/80897/Quotation-errors-in-general-science
       ; reported at
       https://www.timeshighereducation.com/news/quarter-citations-top-journals-wrong-or-misleading —
       ~25% of sampled references in Science, Science Advances, Nature, Nature Communications and PNAS
       "not to substantiate the points raised by authors." These journals have close to zero
       unresolvable references. Perfect resolution, one-in-four failure on warrant, in the same corpus.
       SNIPPET-ONLY (figure via secondary report).
    6. [authors unverified] 2026. "Detection and Interpretability Analysis of Quotation Errors by Large
       Language Models." arXiv:2606.08589. https://arxiv.org/abs/2606.08589 — Notes that methods for
       identifying quotation errors fall into similarity-based, deep-learning and LLM-based families —
       i.e. all of them are *content* methods. No resolution-based method appears in the taxonomy of
       approaches to this defect, because there is no way to build one. SNIPPET-ONLY.
    7. [authors unverified] 2024. "Assessing citation integrity in biomedical publications: corpus
       annotation and NLP models." https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11231046/ — The
       existence of a hand-annotated citation-integrity corpus is itself evidence against the
       presumption: if resolution were a usable proxy, the ground truth would be free. SNIPPET-ONLY
       (title and framing).
    8. NULL RESULT, recorded as such. Searching specifically for link integrity validated against
       semantic accuracy returned only link-rot and reference-rot material (Perma.cc / Harvard Law
       Review; Code4Lib "Robustifying Links To Combat Reference Rot"; UKSG Insights "Reference rot in
       scholarly statement: threat and remedy"). That literature treats resolution as a *necessary
       condition for verifiability* — a precondition for a reader to check — and never as a measure of
       whether the claim made from the source is correct. **I found no study anywhere that validates
       link or id integrity as a measure of citation quality.** Absence of a validating literature is
       weaker evidence than a refutation, but it is the answer to the queue's first limb and it is
       negative. SNIPPET-ONLY across several sources; see
       https://insights.uksg.org/articles/10.1629/uksg.237 and
       https://harvardlawreview.org/forum/vol-127/perma-scoping-and-addressing-the-problem-of-link-and-reference-rot-in-legal-citations/
    9. First-party corroboration. The register's own evidence line for this presumption: the automated
       figure was "zero dead citations" over 979 references; the same day's hand-reading found five
       defects across five days — Rohr PRS-03 cited for a claim it does not make (twice), Wright PRS-03
       in frontmatter and cited nowhere, an id-less Levin by-theme gesture with two real records
       waiting, Levin PRS-03 with a half-correct gloss — and **every one of the five resolves**. This
       is a direct, in-corpus demonstration that the classes are disjoint here and not merely in
       medicine. FIRST-PARTY (presumptions.md, PRESUMPTION-877 evidence line).

  Strength of challenge: Strong

  Summary: The presumption is contradicted by the field that builds citation-checking tools, by the
  measurement literature, and by the corpus itself. The tool literature states the limitation directly:
  authority-database and metadata validation cannot determine whether a claim reflects the source. The
  measurement literature sizes the invisible class — 14.5% to 16.9% of quotations wrong in pooled
  samples, ~8% major, ~25% non-substantiating in the top general-science journals — all in corpora
  whose references resolve. And the single most probative finding is negative: quotation accuracy has
  not improved across the decades in which resolution went to near-perfect, which is what one would
  expect only if the two are independent. The C2A2 instance is not a transfer argument: the day's own
  five hand-found defects all resolve, so the check's blindness is demonstrated on this corpus, not
  inferred from another. Two honest limits keep this from being airtight. I found no study measuring
  the conditional quantity the queue asks for — of references that resolve, what fraction are accurate
  — so the *proportion* of C2A2's defects invisible to the check remains unknown, only demonstrably
  non-zero. And I found no affirmative answer to the queue's first limb: link integrity does not appear
  to have been validated as a citation-quality measure anywhere, which reads as an absence rather than
  a refutation. Rated Strong because the presumption requires a positive warrant it does not have,
  because the tool literature explicitly disclaims it, and because the corpus has already falsified it
  five times in one day.

  Specific risks: (a) High, per 14b's own assessment, and the search does not lower it. "Zero dead
  citations over 979 references" is the wiki's strongest self-claim and the most quotable; if it
  measures the wrong construct, every downstream trust in the citation layer is collateralised against
  an instrument that cannot register the corpus's actual failure mode. (b) The vocabulary risk is the
  deeper one and is what makes this a presumption rather than an assumption: because the check names
  the discourse, the defect class it misses has no term, so it cannot be counted, trended, budgeted
  for, or assigned. A defect class with no name does not appear in any register, including this one.
  (c) The detection asymmetry is self-reinforcing: an automated sweep runs nightly at zero marginal
  cost and reports clean; hand-reading runs at roughly one pair per twenty minutes and reports
  defects. The cheap instrument will always dominate the record by volume, so the corpus's apparent
  citation health is a function of which instrument was affordable. (d) If the general rates transfer
  even loosely, the 979 attributable references carry on the order of 10²  quotation-level defects, and
  the five found are a density estimate, not an incident count. (e) Compounds with PRESUMPTION-878: if
  the remedy space for a hand-found defect class is "build a downstream check," and the only cheap
  checks are resolution-shaped, then the system will keep building instruments that cannot see the
  defect that motivated them.

  Mitigations available:
    - Rename the metric to what it measures — reference resolution rate — and reserve "citation health"
      for a measured quantity. This is the whole of the fix for the inference, and it costs one line.
    - Introduce a name for the invisible class. "Resolvable but unsubstantiated" or the field's own
      term, quotation error. A class with a name can be counted; the naming is prior to any check.
    - Measure the conditional quantity directly, since it is the thing nobody in the literature has
      measured for anyone and C2A2 can measure it for itself: sample resolving references and score
      substantiation. See the test protocol under ASSUMPTION-1206.
    - Report the found-by-hand rate as a density with its denominator (defects per pair read, pairs
      read per day), so that the hand-reading channel produces a corpus-level estimate rather than a
      list of incidents.
    - Content-level verification is an active area (arXiv:2511.16198, arXiv:2411.06101,
      arXiv:2606.08589) and, unlike another resolution check, would address the class. I verified no
      performance figures and make no readiness claim.

  STEELMAN:
    Item: PRESUMPTION-877
    Strongest counterargument: The presumption, stated fairly, is not "resolution equals accuracy" but
    "resolution is the only citation property that can be checked at corpus scale, so it is what
    'citation health' can operationally mean here." On that reading it is not a measurement error but a
    scope decision, and a defensible one: resolution is a genuine necessary condition, it is exactly
    what the link-rot literature holds to be the property worth protecting, it is the property whose
    failure destroys verifiability outright rather than merely degrading it, and it is checkable
    without an adjudicator. The quotation-error rates cited above come from corpora where citation is
    an interpretive act across independent research programmes; a PRS reference points at a short
    structured record in a corpus this system wrote, where the gap between "resolves" and "says what is
    claimed" is far narrower than in medicine. And the strongest empirical rebuttal available to the
    presumption's defender is that the five hand-found defects were found — the system does have a
    second instrument, it is working, and nothing about the automated figure prevented it.
    What would need to be true for C2A2 to be safe: (i) the second instrument must have coverage, not
    just existence — at one pair per twenty minutes against 307 days of material it does not, so the
    "we caught them anyway" defence rests on a channel that has read a small fraction of the corpus;
    (ii) the automated figure must never be restated without its scope, and quotation reliably strips
    scope; (iii) the referents must be short and unambiguous enough that resolution nearly determines
    accuracy — already falsified, since two of the five defects are precisely accuracy failures on
    short structured records ("cited for a claim it does not make"); (iv) no downstream agent may treat
    a clean nightly figure as licence to skip reading; (v) the register must contain a name for the
    uncovered class, or the scope decision cannot be revisited because it cannot be discussed.
    How to test: Two tests, both cheap. First, the conditional-accuracy sample described under
    ASSUMPTION-1206: 40 random resolving references, scored substantiated / partial / not, giving the
    first interval on the invisible class in this corpus. Second, a vocabulary audit: grep the register
    for every term used to describe citation quality and check whether any names a semantic defect. If
    the only available terms are resolution-shaped ("dead citation," "resolves," "id-less"), the
    presumption is confirmed as operative in the register's language, independently of what any run
    believed. 14b's inference predicts the second test comes back with no such term; that prediction is
    checkable today without a search budget.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-877, ASSUMPTION-1206, ASSUMPTION-1213 (and adjacent: ASSUMPTION-1211)
    Common vulnerability: **Construct-validity failure in automated proxies, compounded by vocabulary
    capture.** The register reports the quantity that is cheap to compute (ids resolving; words
    counted) under the name of the construct it wanted (citation health; argument size). In each case
    the proxy is highly reliable and measures something else, and in each case the proxy's terms have
    become the only terms available, so the missed construct cannot be named, counted or trended. This
    is Goodhart's law with an epistemic rather than incentive mechanism: no one is gaming anything, but
    optimisation of, and reporting on, a compressed measure still discards the goal-relevant features
    it omits (arXiv:2510.02840).
    Literature basis: PMC12285159 (quotation accuracy flat across the era that fixed pointer errors);
    arXiv:2511.16198 and arXiv:2411.06101 (the two defect classes and the tools' explicit disclaimer);
    Proc. R. Soc. A 476:20200538 (~25% non-substantiating in near-perfectly-resolving corpora);
    verbosity-bias and length-controlled-metric results for the 1213 limb (see that file); Goodhart
    1975 / Strathern 1997 [primary sources not retrieved].
    Risk level: High
    Recommendation: For every automated figure that is promoted to a register headline, require an
    accompanying named statement of the defect class the instrument cannot detect. Where that statement
    cannot be written, the figure is not a headline. Introduce the missing vocabulary first —
    measurement of an unnamed class is not possible.

  Recommendation: CHALLENGED

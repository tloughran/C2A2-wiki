SYSTEMIC-RISK-FLAG_2026-08-18_G2

Date: 2026-08-18

Affected items:
  - ASSUMPTION-1131 (citation polarity invisible at the Label; read-the-body escalation)
  - PRESUMPTION-831 (identifier presumed to carry polarity; no schema field)
  - ASSUMPTION-1136 (reproducible author-attribution fabrication; author-list guard)
  - PRESUMPTION-763 (existence verification licensing a completeness claim)
  - PRESUMPTION-756 (retired upstream claim invalidating downstream work)
  - PRESUMPTION-757 (source self-revision binding a derived construct) — affected by the second-order form of the vulnerability

Common vulnerability:
  IDENTIFIER-LEVEL VERIFICATION USED AS A PROXY FOR CONTENT-LEVEL, POLARITY-AWARE AND
  DEPENDENCY-AWARE VERIFICATION.

  All six items are instances of one structural pattern. C2A2 checks properties of the
  identifier — does it exist, does its label match, is the author list right, has it been
  withdrawn — and then draws conclusions about properties of the relation between the source
  and the sentence it anchors: does the source support or undercut the claim, does the source
  entail what is attributed to it, does the downstream claim actually depend on the upstream
  one, is the derived construct actually bound to the revised element.

  The identifier layer is cheap, high-throughput and machine-checkable. The relation layer is
  expensive, expert-dependent, only moderately reliable even among humans, and in a
  non-trivial fraction of cases not single-valued at all. Every one of today's failures is a
  case of the cheap layer's PASS being read as the expensive layer's PASS. Critically, the
  proposed remedies also share the flaw in mirror form: adding a polarity field to the
  identifier (831), escalating to a read-the-body rule (1131), verifying author lists (1136),
  and propagating withdrawal by identifier (756, 757) are all further identifier-layer moves
  offered against a relation-layer problem.

Literature basis:
  - Jergas, H., Baethge, C., 2015. "Quotation accuracy in medical journal articles — a
    systematic review and meta-analysis." PeerJ 3:e1364. Total quotation error rate 25.4%
    (major 11.9%) among references that exist and are correctly identified. Updated in
    "Systematic review and meta-analysis of quotation inaccuracy in medicine," Research
    Integrity and Peer Review (2025), ~32,000 quotations: 16.9% incorrect, 8.0% major.
    [2025 author attribution not confirmed.] — Quantifies the identifier/relation gap directly.
  - Rashkin, H. et al., 2023. "Measuring Attribution in Natural Language Generation Models."
    Computational Linguistics 49(4):777–840. The AIS framework separates source identification
    from entailment verification and treats even a passed attribution check as a pre-condition
    rather than a sufficiency claim.
  - Liu, N.F., Zhang, T., Liang, P., 2023. "Evaluating Verifiability in Generative Search
    Engines." Findings of EMNLP 2023. Cited pages all existed; only 51.5% of sentences were
    fully supported and only 74.5% of citations supported their sentence.
  - Bakker, C., Theis-Mahon, N., Brown, S., 2023. "Evaluating the Accuracy of scite, a Smart
    Citation Index." Hypothesis. The leading production polarity classifier recovered 0 of 17
    contrasting citations; F-measures 0.0–0.58. The relation layer does not automate cleanly.
  - Catalini, C., Lacetera, N., Oettl, A., 2015. "The incidence and role of negative citations
    in science." PNAS 112(45):13823–13826. Negative citations 2.40%; annotation required
    domain PhDs. Extreme class imbalance plus expert cost.
  - Shotton, D., 2010. "CiTO, the Citation Typing Ontology." Journal of Biomedical Semantics
    1(Suppl 1):S6, plus "Adoption of the Citation Typing Ontology by the Journal of
    Cheminformatics" (2020) [author attribution not confirmed]. The relation-layer vocabulary
    has existed for fifteen years and is little used — schema availability is not the binding
    constraint.
  - Repository metadata-quality evidence: optional fields show consistently low completeness;
    mandatory status markedly raises it. [Specific attribution not confirmed; see also
    "The variable quality of metadata about biological samples used in biomedical
    experiments," Scientific Data 6:190021 (2019).] — An optional relation field will be blank
    where it matters.
  - Fanelli, D., Moher, D., 2019/2021 (bioRxiv 734137 / Accountability in Research) and
    Kataoka, Y. et al., 2022 (medRxiv 2022.01.30.22270124). Retraction — the strongest
    identifier-level signal available — changes direction in only 8.4% of downstream
    meta-analyses and has no impact for the >75% of retractions unrelated to data, methods or
    results. Identifier-level status does not determine relation-level dependency.
  - Hsiao, T.-K., Schneider, J., 2021. Quantitative Science Studies 2(4):1144–1169. Only 5.4%
    of post-retraction citation contexts acknowledge the retraction — the field's own
    identifier-to-relation propagation is near zero.
  - Simkin, M.V., Roychowdhury, V.P., 2003/2005. "Read Before You Cite!" Complex Systems 14(3).
    ~80% of citations copied rather than read; identifier checks pass along chains where the
    relation was never established at any node.
  - Borsboom, D., Mellenbergh, G.J., van Heerden, J., 2004. "The concept of validity."
    Psychological Review 111(4):1061–1071. Validity resides in the attribute-measure causal
    relation, not in the surrounding network — the same identifier/relation split, one level up.
  - Underdetermination / Duhem–Quine (Stanford Encyclopedia of Philosophy). A change at the
    identifier level does not determine which relation-level element must change.

Risk level: HIGH

  Severity: the measured ambient content-error rate among existing, correctly-identified
  sources sits at 17–25% in the best-studied domain. If identifier-level PASS is being reported
  as verification, that is the approximate size of the undetected error population — an order
  of magnitude larger than the four cases surfaced today.
  Breadth: all six items in this group, and by construction every anchored claim in the corpus.
  Detectability: low by design — the failure mode is invisible to the check being run, and
  produces a clean audit artefact.
  Remedy risk: the currently proposed remedies are themselves identifier-layer, so implementing
  them may reduce the visible incident rate without reducing the underlying error rate — the
  worst possible outcome, since it removes the signal.

Recommendation:

  1. SPLIT THE STATUS FIELD. Replace any single "verified" flag with at least three
     independently-recorded states: (i) identifier exists and resolves; (ii) identifier is
     correctly attributed (authors, venue, date); (iii) source entails the anchored sentence
     (AIS-style). Never allow (i) or (ii) to be reported as (iii). Add an explicit
     NOT-ASSESSED state and forbid absence from reading as clearance.

  2. MOVE POLARITY AND DEPENDENCY OFF THE IDENTIFIER. Both belong to the
     (identifier, anchored-sentence) pair, not the identifier. Align with CiTO predicates
     rather than inventing a sign field. Make the field mandatory-with-explicit-unknown for
     load-bearing anchors, since the metadata literature shows optional fields go unfilled.

  3. PUBLISH A DENOMINATOR AND A DECLARED RESIDUAL. Report anchors checked, not just
     rejections. Benchmark the internal content-error rate against the 17–25% published band.
     A system reporting zero content errors is reporting that it is not measuring them.

  4. TYPE PROPAGATION RATHER THAN BLANKET IT. Withdrawal and revision should propagate
     conditionally on (a) recorded evidential dependency and (b) the reason for withdrawal
     (substantive vs. non-substantive), first-hop by default, with re-derivation-and-compare
     preferred over invalidation. Annotate non-propagating dependents rather than leaving them
     silent.

  5. SAMPLE-AUDIT THE RELATION LAYER BY HUMAN READING. Automation of the relation layer is
     measured at F 0.0–0.58 for the contradicting class and kappa ~0.5–0.6 among humans.
     Budget for a sampled expert audit and treat its measured rate as the system's error rate;
     do not treat the automated pass rate as an error rate.

  6. GUARD AGAINST FALSE CLOSURE. Any item in this group whose status moves to "resolved"
     should carry an explicit statement of the residual that remains, and the residual should
     be a measured number, not the word "minimal."

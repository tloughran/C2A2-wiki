SEARCH-AGAINST-PRESUMPTION-763:
  Date searched: 2026-08-18
  Original item: PRESUMPTION-763
  Original statement: Whether existence verification licenses a completeness claim. (i.e. that confirming the cited items exist is sufficient to warrant treating the citation set / the verification as complete.)

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-763
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption from operational review; queued as literature-testable.
      15b: Searched for challenging literature; found large measured gaps between existence of a reference and accuracy of what is attributed to it, a formal framework separating source identification from entailment, and evidence that completeness/recall is a distinct database-dependent property that existence checks cannot bound.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Jergas, H., Baethge, C., 2015. "Quotation accuracy in medical journal articles — a systematic review and meta-analysis." PeerJ 3:e1364. — Across 28 studies: major quotation error rate 11.9% (95% CI 8.4–16.6), minor 11.5% (8.3–15.7), total 25.4% (19.5–32.4). These are errors in references that indisputably exist and are correctly identified. Existence verification would have passed on every one. This is the cleanest available refutation of the presumption.
    2. Update/extension, 2025. "Systematic review and meta-analysis of quotation inaccuracy in medicine." Research Integrity and Peer Review. [Author attribution not confirmed in this session — cite by title/venue.] — 46 studies, ~32,000 quotations/references: 16.9% (95% CI 14.1–20.0) of quotations incorrect, ~half of those major (8.0%, 6.4–10.0). Confirms the effect at a larger scale a decade later; the gap between "exists" and "says what is attributed to it" is stable and substantial.
    3. "Accuracy of cited 'facts' in medical research articles: A review of study methodology and recalculation of quotation error rate." 2017. PLOS ONE 12(9):e0184727. [Author attribution not confirmed in this session — cite by title/venue.] — Methodological review recalculating quotation error rates; reinforces that measured rates depend on method but remain non-trivial under every method.
    4. Rashkin, H., Nikolaev, V., Lamm, M., Aroyo, L., Collins, M., Das, D., Petrov, S., Singh Tomar, G., Turc, I., Reitter, D., 2023. "Measuring Attribution in Natural Language Generation Models." Computational Linguistics 49(4):777–840. — The AIS framework makes the distinction formal: attribution requires that the statement be verifiable against an independent identified source. Identifying the source is a precondition of the check, not the check. AIS is explicitly framed as usable as a pre-condition in tandem with other metrics, i.e. even full AIS compliance does not establish completeness.
    5. Liu, N.F., Zhang, T., Liang, P., 2023. "Evaluating Verifiability in Generative Search Engines." Findings of EMNLP 2023. — In four production generative search engines, only 51.5% of sentences were fully supported by their citations and only 74.5% of citations supported their associated sentence — despite every cited page existing and resolving. Existence was 100%; support was not.
    6. Bramer, W.M., Rethlefsen, M.L., Kleijnen, J., Franco, O.H., 2017. "Optimal database combinations for literature searches in systematic reviews: a prospective exploratory study." Systematic Reviews 6:245. — Establishes completeness (recall) as a separate, measurable, database-dependent property: searching MEDLINE, Embase and CENTRAL was insufficient for identifying all effect studies in a domain, and adding ten further databases raised median recall by only ~2%. Completeness has to be argued from search design and diminishing-returns evidence; nothing about the existence of retrieved records speaks to what was missed.
    7. Razniewski, S. et al. "Completeness, Recall, and Negation in Open-World Knowledge Bases: A Survey." — Under the open-world assumption, a knowledge base's contents license no completeness claim whatsoever; completeness must be separately asserted via dedicated metadata. Formalises the gap the presumption elides.
    8. Arnaout, H., Razniewski, S., Weikum, G., Pan, J.Z., 2020–2021. "Enriching Knowledge Bases with Interesting Negative Statements" / "Negative Knowledge for Open-world Wikidata." — Positive-only stores cannot distinguish "absent because false" from "absent because unrecorded," which is exactly the inference a completeness-from-existence claim requires.
    9. Simkin, M.V., Roychowdhury, V.P., 2003/2005. "Read Before You Cite!" Complex Systems 14(3). — Estimates that ~80% of citations are copied from other reference lists rather than read, inferred from repeated-misprint distributions. Existence checking on a copied reference chain passes trivially while the content link was never established at any node in the chain.

  Strength of challenge: Strong

  Summary: The presumption is contradicted from three independent directions. Empirically, the quotation-accuracy literature measures the exact gap: between 17% and 25% of citations to references that demonstrably exist misstate what those references say, with roughly 8–12% classed as major errors. Formally, the AIS framework separates source identification from entailment verification, and treats even a passed attribution check as a pre-condition rather than a sufficiency claim. Structurally, the systematic-review and open-world-KB literatures treat completeness/recall as a distinct property that must be argued from search design and explicitly asserted, since existing records say nothing about what is missing. The Simkin/Roychowdhury copying result adds that existence checks pass trivially along chains where no one has ever read the source. Under every one of these framings, existence verification licenses neither content correctness nor coverage.

  Specific risks:
    - Silent 17–25% error floor: if existence checking is treated as verification, roughly one in five to one in four content attributions can be wrong while the process reports clean.
    - Category error between two distinct completeness claims: "we verified all the citations we have" and "we have all the citations we need" are both unlicensed by existence checks, and conflating them compounds the exposure.
    - Chain-passing: copied references pass existence checks at every hop while the content link was never established at any hop.
    - Open-world leakage: treating absence of a contrary record as evidence of correctness.
    - False audit signal: a passing existence check produces an artefact of assurance that is disproportionate to what was actually tested, making the residual invisible to downstream consumers.

  Mitigations available:
    - Separate three checks with three distinct statuses: exists / is correctly identified / entails the attributed statement. Only the third is verification in the AIS sense.
    - Sample-audit content fidelity at a rate calibrated to the ~17–25% ambient quotation-error band, and publish the audit rate rather than the pass rate.
    - Assert completeness only with a stated search design and a diminishing-returns argument, following the Bramer et al. method (report marginal yield of each additional source).
    - Record explicit "not assessed" states; never let absence read as clearance.
    - Flag references that entered by copying rather than by direct retrieval.

  Search scope: Quotation and citation accuracy meta-analyses in medicine; attribution evaluation frameworks in NLG; verifiability audits of generative search engines; systematic-review search recall and database coverage; completeness, recall and negation in open-world knowledge bases; citation-copying/misprint propagation. Searched 2026-08-18. Not covered: domain-specific quotation-accuracy studies outside medicine; formal database completeness reasoning (Motro/Levy lineage) beyond the survey.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-763
    Strongest counterargument: Existence verification is not worthless and is not claiming to be sufficient in isolation — it is the cheap, high-throughput filter that eliminates the highest-severity failure class (wholly fabricated sources, measured at 18–55% in LLM output by Walters & Wilder) at near-zero cost. The defensible version of the presumption is triage, not sufficiency: existence checking is applied universally, content checking is applied to load-bearing claims, and the residual is declared. The presumption becomes dangerous only when the cheap filter's pass is reported as if it were the expensive filter's pass, which is a reporting-discipline failure rather than a verification-design failure. It is also worth noting that the 17–25% quotation-error figures come from human authors reading real papers, so no achievable process eliminates this class — the question is what residual is declared, not whether one exists.
    What would need to be true for C2A2 to be safe: (a) existence status and content-support status are separately recorded and separately reported, never collapsed into one "verified" flag; (b) any completeness claim is accompanied by its search design and marginal-yield evidence; (c) a declared residual error rate accompanies outputs, benchmarked against the ~17–25% ambient band; (d) content checking is mandatory for anchors carrying argumentative load; (e) absence of a record never counts as evidence.
    How to test: Take 100 anchors that passed existence verification, have an independent reader assess whether each source entails the attributed statement, and compute the content-error rate. If it falls in or above the 17–25% band, the presumption is refuted operationally for C2A2 specifically, not just in the general literature. For the coverage half of the claim, run a Bramer-style marginal-yield test: add a second and third independent source pool to an already-"complete" search and measure how many new relevant items appear. Non-trivial marginal yield refutes the completeness claim directly.

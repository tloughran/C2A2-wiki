SEARCH-FOR-ASSUMPTION-514 (RE-TRIGGER — 15d, MONITOR-473, cycle 1; High; subordinate to PREMISE-124):
  Date searched: 2026-10-17
  Original item: ASSUMPTION-514
  Original statement: Any self-measurement of the pipeline's completeness/accuracy must cite an
    external/independent referent (seeded denominator) or be reported UNCALIBRATED.
  Search angle (per 15d block): literature on capture-recapture / seeded-fault estimation and calibration
    standards. Cycle 0 relied on self-assessment psychology (Zell & Krizan 2014, r = .29).
  Cycle: 1 (RE-TRIGGER by 15d; processed 2026-10-17)

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a, 15b -> 15c -> 15d -> 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-514
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the PREMISE-124 report (self-measurement over a dark channel is uncalibrated).
      15a (cycle 0, 2026-07-24): SUPPORTED (Strong). Zell & Krizan 2014; Kruger & Dunning 1999; Tarski
        1933/36; Rubin 1976. Read depth was not marked in cycle 0. Psychology, logic and missing-data
        theory; no measurement-engineering source.
      15b (cycle 0): independent; not read by this agent.
      15c: -> MONITOR-473 (High; subordinate to PREMISE-124)
      15d: re-triggered without evaluating evidence; angle = capture-recapture / seeded-fault / calibration.
      15a (cycle 1, 2026-10-17): 2 web searches; 3 fetch attempts (Briand et al. NRC report: abstract and
        Section 2.3 read; Simula record: bibliographic only; Zobel SIGIR'98 abstract page FAILED (Incapsula
        bot wall)).
    Current status: SUPPORTED (Moderate-Strong) — with a refinement on seeded-denominator validity

  Search scope: (a) software-engineering defect-content estimation: error seeding (Mills 1972) and
    capture-recapture for inspections; (b) information-retrieval evaluation completeness (TREC pooling and
    recall overestimation). Metrology calibration standards (e.g., ISO/IEC 17025, VIM traceability) were not
    searched this cycle.

  Supporting evidence found: Yes — two engineering literatures, independent of cycle 0's psychology sources.

  Sources:
    1. Briand, L.C., El Emam, K., Freimut, B.G. & Laitenberger, O., 2000. "A Comprehensive Evaluation of
       Capture-Recapture Models for Estimating Software Defect Content." IEEE Trans. Software Engineering
       26(6):518-540. [abstract read in full; Section 2.3 (prior studies) read via targeted passage
       extraction; read from NRC Canada tech-report version ERB-1084 (2001), not the typeset TSE version]
       Findings:
       - Motivation: predicting remaining defects is needed to decide whether inspection can stop. "Few
         studies compare the actual number of remaining defects to the one predicted ... on real software
         engineering artifacts."
       - Accuracy depends strongly on the number of inspectors. Below 4 inspectors, "no model is
         sufficiently accurate and underestimation may be substantial".
       - Recommended: a model with heterogeneous detection probabilities (Mh) with a Jackknife estimator.
       - Section 2.3: Mills (1972) introduced error seeding. Pseudo-defects are seeded before testing and the
         Lincoln-Petersen estimator gives total defects. This "requires that the seeded and real defects have
         the same detection probabilities."
       - Musa et al. (1984), per Briand et al.: seeding "fails to be accurate due to the difficulties in
         seeding the software with defects similar to those naturally occurring ... seeded defects are much
         easier to find."
       - Eick et al. (1993) had "no software artifact with a known number of actual defects" and so had to
         use proxies.
       - Studies that validated estimators did so on documents with KNOWN or seeded defect counts (e.g.,
         NASA documents with 15 reintroduced defects; Wohlin et al. 1995, 38 seeded defects).
       Relevance: the software-engineering field's own practice matches the assumption. A completeness
       estimate (remaining defects) is validated only against an artifact with a known or seeded
       denominator. Without one, the estimate's accuracy is unknown, and it tends to underestimate under
       realistic conditions. The Musa caveat also adds a condition: a seeded denominator calibrates only if
       the seeds are as hard to find as real items.
    2. Mills, H.D., 1972. "On the statistical validation of computer programs." IBM Federal Systems Division
       report FSC-72-6015. [background knowledge — UNVERIFIED; known here only as cited in Briand et al.
       Section 2.3] Origin of the seeded-fault (error-seeding) denominator.
    3. Zobel, J., 1998. "How Reliable are the Results of Large-Scale Information Retrieval Experiments?"
       Proc. SIGIR '98:307-314. [snippet — abstract text quoted in search results; abstract-page fetch FAILED]
       - Measured relative system rankings appear reliable, "but recall is overestimated: it is likely that
         many relevant documents have not been found."
       - A secondary summary [snippet]: pooling could miss up to ~50% of relevant documents.
       Relevance: an in-sample completeness measure (recall against the pooled, self-discovered set of
       relevant items) systematically overstates completeness when the true denominator is unknown. This
       directly mirrors "self-measured completeness without an external denominator is uncalibrated".
    4. (Carried from cycle 0, not re-read) Zell & Krizan 2014 (r ≈ .29); Kruger & Dunning 1999; Rubin
       1976. [background knowledge — UNVERIFIED this cycle]

  Strength of support: Moderate-Strong.
    - Cycle 0 drew on psychology and formal analogies. This cycle adds two measurement-engineering
      literatures in which completeness estimators are validated only against known or seeded denominators,
      and in which internally measured completeness (pooled recall) is shown to be biased upward.
    - Briand et al. is peer-reviewed (IEEE TSE) and read at abstract-plus-section level. Zobel is
      snippet-level.

  Summary: Software-engineering defect-content estimation independently arrived at the assumption's rule.
    Mills' error seeding provides a known denominator, and capture-recapture estimators are judged accurate
    only by comparison against artifacts with known or seeded defect counts. Briand et al. found that without
    enough independent inspectors, estimates substantially underestimate the true count. IR evaluation shows
    the same pattern: recall measured against a self-discovered pool is overestimated (Zobel 1998). Both
    literatures support "cite an external or seeded referent, or report UNCALIBRATED", and add a
    qualification: a seeded denominator calibrates only if the seeded items are representative in
    detectability.

  Refinement surfaced (for 14a/15c, not a design ruling): "seeded denominator" should carry a
    representativeness condition. Per Musa et al. (via Briand), seeded faults that are easier to find than
    natural ones inflate apparent completeness. Suggested wording: "...must cite an external referent or a
    seeded denominator whose items are comparable in detectability to the real ones, or be reported
    UNCALIBRATED."

  Caveats:
    - Capture-recapture without seeding (multiple independent inspectors) is itself a partly internal
      method; whether it counts as an "independent referent" depends on inspector independence. This is a
      boundary case for the assumption's wording.
    - Zobel's source was read at snippet level only; the fetch failed.
    - Metrology and calibration standards were not searched; a broader search is recommended for the
      "calibration standards" angle.
    - This item still overlaps PREMISE-124; the cycle 0 duplication flag stands.

  Recommendation: SUPPORTED (Moderate-Strong), with the seeded-denominator representativeness refinement.

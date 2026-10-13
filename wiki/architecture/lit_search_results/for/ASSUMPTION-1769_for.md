SEARCH-FOR-ASSUMPTION-1769:
  Date searched: 2026-10-11
  Original item: ASSUMPTION-1769
  Original statement: Wiki daily run FINDING-101: "salt" the cross-tradition pattern detector with fake connections whose
    answers are known, to measure true vs spurious flags; currently confidence labels are uncalibrated. Question: Is
    seeding known-answer items (canaries, planted positives/negatives) a valid way to calibrate an automated pattern
    detector's confidence labels?

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1769
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from wiki daily run FINDING-101 (stated proposal to salt the pattern detector with known-answer
        fake connections); queued 2026-10-10
      15a (2026-10-11): 3 web searches, 1 fetch (arXiv 2105.09457; succeeded, full text partly read: abstract,
        introduction, related work and conclusion via keyword scan; middle sections not fully read). A first fetch
        attempt on the arXiv abs URL was blocked by the tool (URL not in provenance set) and returned nothing. Found
        three established traditions of the practice: fault/error seeding (Mills 1972), gold/known-answer items in
        crowdsourced annotation, and synthetic anomaly injection for detector evaluation.
    Current status: SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) fault seeding / Mills; (b) gold-standard known-answer items in
    crowdsourcing QC; (c) synthetic injected anomalies for detector precision/recall. 1 fetch: Hettiachchi et al.
    arXiv PDF (succeeded; partially read as noted).

  Supporting evidence found: Yes

  Sources:
    1. Mills, H.D. 1972 error seeding; Weinberg 1970 "bebugging" (Wikipedia "Bebugging"; GeeksforGeeks; HKU/IEEE
       Trans. Reliability 1999 on removal, recapture and seeding). [search-result] Planting known faults and counting
       how many are found estimates detection rate and residual faults (N ≈ n·s/v). Validity rests on seeded faults
       being as detectable as real ones; "if seeded errors are not reflective of real errors, this method may give
       highly misleading results." Relevance: the canonical precedent for salting.
    2. Hettiachchi, D., Schaekermann, M., McKinney, T. & Lease, M. "The Challenge of Variable Effort Crowdsourcing and
       How Visible Gold Can Help." arXiv 2105.09457. [fetched, full text partly read] Gold (known-answer) questions are
       described as a standard quality-control mechanism; in their experiment visible gold was the only best-practice
       method that improved quality (+7% bounding-box accuracy). Search results on other papers (arXiv 1611.02145;
       TREC RMIT) note gold items must not be easily spotted, need expert creation, and a small gold pool lets workers
       recognise repeats; one study found gold-based QC did not filter all bad workers (76.4% accuracy). Relevance:
       known-answer items as a measurement and calibration tool for labellers.
    3. Synthetic anomaly injection: MathWorks Predictive Maintenance docs; Nixtla blog/docs; USPTO patent on injecting
       synthetic anomalies to benchmark data-quality monitors; graph anomaly survey arXiv 1404.4679. [search-result]
       Injection supplies labels so that precision and recall become measurable; thresholds can be tuned against
       injected positives. Caveats: real data may already contain similar anomalies (false "false positives"); recall
       depends on injected strength; coverage is limited to injected types.

  Strength of support: Moderate to Strong for measuring detection rate (recall) on planted positives; Moderate for
    calibrating confidence labels.

  Summary: Seeding known-answer items is a long-established method in software testing (error seeding), crowdsourced
    annotation (gold questions) and anomaly detection (synthetic injection). All three use planted items to estimate
    how often real items are caught and how often detections are spurious, which is what FINDING-101 proposes. The
    literature consistently attaches one condition: planted items must resemble real ones in difficulty and type, or
    the estimates mislead. Planted negatives (fake connections that should NOT be flagged) give false-positive rates;
    planted positives give recall.

  Caveats: (i) Representativeness: fake cross-tradition connections authored by the pipeline may be easier or harder
    to detect than genuine ones (Mills critique). (ii) If the detector (an LLM agent) can recognise planted items, the
    test is contaminated (crowdsourcing "spotted gold" problem). (iii) Calibration of confidence labels (e.g., HIGH
    means ~X% true) needs enough seeds per label bin; sources give a square-root-of-labels rule of thumb for gold count
    but none addresses LLM confidence labels. (iv) Ground truth for "real" cross-tradition connections is itself
    contestable.

  NOVELTY flag: partial. Method well established; application to an LLM cross-tradition pattern detector not found.

  Recommendation: SUPPORTED (Moderate). Preliminary search; broader search recommended (classifier calibration with
    reliability diagrams; canary/honeypot items in LLM evaluation; mark-recapture estimation).

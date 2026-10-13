SEARCH-AGAINST-ASSUMPTION-1769:
  Date searched: 2026-10-11
  Original item: ASSUMPTION-1769
  Original statement: [stated] Wiki daily run FINDING-101 proposes "salting" the cross-tradition
    pattern detector with fake connections whose answers are known, so that true and spurious flags
    can be measured. The confidence labels are currently uncalibrated. Question: is seeding
    known-answer items (canaries, planted positives and negatives) a valid way to calibrate an
    automated pattern detector's confidence labels?
  Under test: whether planted items give calibration that transfers to real items. I searched for
    seeded items being detectable or unrepresentative, and for calibration failing under
    distribution shift.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output from today.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1769
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a (2026-10-10): Extracted from wiki daily run FINDING-101 (the salting proposal). Queued with
        the question on canary-based calibration.
      15b (2026-10-11): Searched for challenging literature. 3 searches: gold/known-answer items in
        crowdsourcing and whether they can be detected; realism of synthetic injected anomalies;
        Ovadia et al. on calibration under dataset shift. 1 fetch: IJCAI 2019 proceedings page for
        Checco, Bates & Demartini (abstract, full).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. One abstract fetched in full; the rest are snippets or search
    summaries.
  Search scope: preliminary (3 searches, 1 fetch).

  Challenging evidence found: Yes (on transfer and representativeness). No (on the basic validity of
    known-answer testing).
  Strength of challenge: Moderate

  Sources:
    1. Checco A, Bates J & Demartini G. 2019. "Quality Control Attack Schemes in Crowdsourcing."
       IJCAI 2019:6136-6140, doi:10.24963/ijcai.2019/850 (also HCOMP 2018). [fetched: abstract,
       full] A small gold set can be detected: an inferential system flags which tasks are likely
       gold, "making them ineffective as a quality control tool". The common countermeasures
       (randomisation, programmatic generation) "are ineffective in practical scenarios". Bearing:
       C2A2's detector is not adversarial, but the same mechanism applies without intent. If planted
       connections differ systematically from real ones (template phrasing, cleaner structure,
       one author), the detector's accuracy on them measures how detectable the plants are, not how
       reliable it is on real cases.
    2. Ovadia Y et al. 2019. "Can You Trust Your Model's Uncertainty? Evaluating Predictive
       Uncertainty Under Dataset Shift." NeurIPS 2019, arXiv:1906.02530. [abstract/snippet]
       Calibration degrades under dataset shift, and "traditional post-hoc calibration does indeed
       fall short". Bearing: confidence labels calibrated on a planted distribution need not stay
       calibrated on the real distribution of cross-tradition connections. Real connections are
       ambiguous and graded. Plants are crisp by construction.
    3. Synthetic-anomaly realism literature (Synthesis4AD, arXiv:2604.04658; ADBench,
       arXiv:2206.09426). [snippet] "Unrealistic perturbations tend to introduce spurious cues and
       yield biased representations." ADBench notes that fully synthetic anomalies built from an
       assumed distribution "fail to create complex anomalies". Bearing: the evaluation of planted
       positives is only as good as the realism of the plants.
    4. Larlus et al. 2014 (UMass CVHC workshop) and the TREC 2011 RMIT crowdsourcing run. [snippet]
       For hard tasks, perfect accuracy on gold is not a reasonable expectation. In the RMIT run,
       measured gold quality was high, but true judgement accuracy was only 76.4%, which the authors
       put down to a gold set that was "not good enough". Bearing: there is a documented gap between
       performance on known-answer items and real performance.

  Summary: The literature does not reject known-answer seeding. It is standard in crowdsourcing QA
    and anomaly-detection benchmarking. It does identify a failure mode that bears directly on
    calibration. Planted items differ systematically from real items: they are crisper, drawn from a
    smaller set and made by one process. Accuracy on them can then be high while real accuracy is
    lower (RMIT 76.4%). Calibration fitted on one distribution is known to fail under shift (Ovadia).
    For a cross-tradition detector the risk is sharp. The hardest real cases are graded, partial
    homologies. Planted negatives ("fake connections") may be obviously fake, and planted positives
    are unambiguous. The salting would then measure the easy tails and leave the uncertain middle,
    where the confidence labels matter most, uncalibrated.

  Specific risks: (a) False reassurance: high scores on plants produce a "calibrated" label that does
    not hold for real flags. (b) Plants written by the same LLM family as the detector share its
    stylistic signatures and are easier to detect. (c) Plants contaminate the wiki or downstream
    agents if they are not quarantined.

  Mitigations available: Write plants that are graded (partial or ambiguous), not only clear-cut. Use
    a different generator or have a human author them. Rotate the plants and keep the set large
    relative to the batch. Also calibrate against a blind human-adjudicated sample of real flags,
    and do not rely on plants alone. Quarantine plants with hidden IDs.

  STEELMAN:
    Item: ASSUMPTION-1769
    Strongest counterargument: Seeded known-answer items measure performance on seeded items.
      Seeded items are drawn from a distribution chosen by the designer, and in this case the
      designer (an LLM pipeline) shares the detector's own biases about what a "connection" looks
      like. The crowdsourcing literature shows that small fixed gold sets become detectable and stop
      measuring what they were meant to. The calibration literature shows that confidence fitted on
      one distribution fails under shift. A detector can therefore score perfectly on fake
      connections and still be badly miscalibrated on real, ambiguous cross-tradition claims. This is
      worse than knowing the labels are uncalibrated, because it adds a false certificate of
      calibration.
    What would need to be true for C2A2 to be safe: The plants span the real difficulty distribution,
      including partial and ambiguous homologies. The detector cannot distinguish plants from real
      items in its features or style. Plant-based calibration is cross-checked against a
      human-labelled sample of real flags.
    How to test: Train a simple classifier (or ask a separate LLM) to tell plants from real
      candidate connections. Accuracy well above chance means the plants are detectable and the
      calibration is suspect. Compare reliability curves on plants and on a blind-adjudicated real
      sample.

  Boundary conditions identified:
    - Known-answer seeding is sound for catching gross failures (the detector flags obvious fakes as
      strong). It is weaker for fine-grained calibration of the confidence levels.
    - The adversarial-collusion part of Checco et al. does not transfer. The detectability mechanism
      does.

  Recommendation: PARTIALLY-CHALLENGED

  SYSTEMIC-RISK-FLAG: see PRESUMPTION-1121_against.md.

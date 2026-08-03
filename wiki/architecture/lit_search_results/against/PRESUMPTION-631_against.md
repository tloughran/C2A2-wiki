SEARCH-AGAINST-PRESUMPTION-631:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-631
  Original statement: That independence between reasoning agents is a property of context
    separation rather than of the underlying model.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-631
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a run in which both directions selected the same under-stating
           statistic from the same source, unprompted (origin ASSUMPTION-651)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Correlated Errors in Large Language Models, 2025. arXiv:2506.07962 — on one
       leaderboard dataset models agree 60% of the time *when both are wrong*, across
       different providers and architectures. Stronger models are MORE correlated.
       Directly contradicts the claim that arrangement, not model, governs independence.
    2. How Independent are Large Language Models? A Statistical Framework for Auditing
       Behavioral Entanglement, 2026. arXiv:2604.07650 — shared pretraining data,
       distillation and alignment pipelines induce hidden behavioural dependencies that
       undermine multi-model systems. Entanglement survives architectural separation, so
       it certainly survives context separation.
    3. A Systematic Methodology for Evaluating Failure Independence in LLM-Generated
       Code, 2026. arXiv:2607.02808 — strong failure correlation persists despite
       structural variation; models fail on the same inputs, limiting reliability gains
       under majority voting.
    4. Quantifying Correlations of Machine Learning Models, 2025. arXiv:2502.03937 —
       ensembling more correlated models fails to further reduce error probability.
    5. Wisdom of LLM Crowds: Aggregation and Contamination, 2026. arXiv:2607.18269 —
       same-model outputs are more similar, more correlated in failure, and yield lower
       redundancy benefit than cross-model ensembles. Model choice is the dominant factor.
    6. The Cost of Consensus: Isolated Self-Correction Prevails Over Unguided Homogeneous
       Multi-Agent Debate, 2026. arXiv:2605.00914 — homogeneous debate can perform worse
       than a single isolated pass; apparent agreement reflects shared error modes.

  Strength of challenge: Strong

  Summary: The challenge is direct, recent, multi-source and converges. The literature
  names model identity — shared weights, shared pretraining corpus, shared alignment —
  as the dominant driver of error correlation, and reports that structural and provider
  separation, both much stronger interventions than context separation, fail to break it.
  The specific figure that matters here is the conditional agreement rate: when two
  instances err, they err the same way most of the time. That is exactly the event 14b
  observed (both directions selecting the same under-stating statistic from the same
  source, unprompted) and the literature says it is the expected outcome, not an anomaly.

  Specific risks: Every independence claim in the pipeline is a claim about context
  arrangement, including the 15a/15b split itself and the verification protocol currently
  under repair (REVISE-260). If context separation does not deliver independence, then
  15a and 15b are not two witnesses but one witness asked twice, and every CONTESTED /
  CORROBORATED judgement built on their agreement is inflated. The disposition heuristics
  in 15c that key on "both directions agree" would be systematically over-confident.

  Mitigations available: Yes, and they are cheap. (i) Vary the model, not just the
  context, for one of the two directions — the literature's single strongest lever.
  (ii) Vary the evidence: give 15a and 15b non-overlapping source pools, which the
  information-asymmetry literature shows recovers real gains. (iii) Measure rather than
  assume: log conditional agreement between 15a and 15b on items where both are later
  found wrong, and treat that rate as the pipeline's independence statistic.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-631
    Strongest counterargument: Independence in the sense the pipeline needs is
    statistical independence of errors, and that is a property of the joint distribution
    over the two agents' outputs. That distribution is fixed principally by what the two
    agents share, and what they share is not their prompt — it is a set of weights and a
    training corpus, which are identical. Context separation varies a low-dimensional
    conditioning variable while holding the high-dimensional prior fixed; it can decorrelate
    the noise but cannot decorrelate the bias. Worse, the failure is invisible from inside:
    two agents drawing on the same prior will agree, that agreement will look like
    corroboration, and the system will read its own single opinion as consensus and become
    more confident exactly where it is most wrong. The observed C2A2 event — unprompted
    convergence on the same under-stating statistic from the same source — is the signature
    of this, and it was caught by accident.
    What would need to be true for C2A2 to be safe: that the questions posed to 15a and 15b
    are ones where the shared prior is uninformative, so that nearly all the variance is in
    the conditioning; or that the two directions draw on disjoint evidence pools, so the
    shared prior has different inputs to act on.
    How to test: cheap and in-house. Take the items where a later re-check found 15a and
    15b both wrong, and compute the rate at which they were wrong in the same direction and
    cited the same source. Compare against the rate expected if the two were independent.
    A second decisive test: re-run a sample of past 15b searches on a different model and
    measure disagreement with the original 15b result.

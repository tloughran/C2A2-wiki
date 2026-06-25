SEARCH-FOR-ASSUMPTION-347:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-347
  Original statement: "Three columns wired to differ by reference frame (not random seed) yield robustness; identical agents at temperature measure only stochastic variance"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-347
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the central design commitment of Pathway 31 (reference-frame ensemble)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Krogh & Vedelsby 1995. 'Neural Network Ensembles, Cross Validation, and Active Learning.' NIPS. - Ambiguity decomposition: ensemble generalization error = average member error MINUS ensemble diversity. Error reduction comes from diversity, which resampling/seed variation supplies only weakly.
    2. Hansen & Salamon 1990. 'Neural Network Ensembles.' IEEE TPAMI. - Ensemble gains require member errors to be (approximately) independent; correlated members add little.
    3. Kuncheva & Whitaker 2003. 'Measures of Diversity in Classifier Ensembles.' Machine Learning. - Formalizes that diversity (not mere replication) drives ensemble accuracy.
    4. Wang et al. 2022. 'Self-Consistency Improves Chain-of-Thought Reasoning in Language Models.' ICLR 2023. - Aggregating DIVERSE reasoning paths (not identical resamples) yields 5-25% gains; the diversity is what carries the signal.
    5. Internal: existing C2A2 PREMISE (MMA independence) already establishes that evidential weight of agreement scales with FORMATIONAL independence - same-formation agreement is discounted. Directly supports preferring reference-frame variation over seed variation.

  Strength of support: Strong

  Summary: Ensemble theory robustly supports the core distinction the assumption draws: error reduction in an aggregate comes from member DIVERSITY (the ambiguity term), and diversity that arises from genuinely different reference frames decorrelates errors far more than temperature/seed resampling from a single distribution. Identical agents at temperature do sample one distribution and therefore chiefly expose stochastic variance, exactly as the assumption claims. The self-consistency result is the LLM-specific confirmation that diverse paths beat identical resamples. This is a long-validated principle in ensemble learning and is independently echoed by C2A2's own MMA-independence premise.

  Caveats: Support is for the PRINCIPLE (frame-diversity > seed-diversity). It does NOT establish that C2A2's specific axis/corpus-slice manipulations actually achieve error decorrelation - that empirical transfer condition is the subject of PRESUMPTION-390 and must be measured, not assumed.

  Search scope: Ensemble diversity theory; self-consistency; Condorcet independence. Comprehensive for the principle.

  Recommendation: SUPPORTED

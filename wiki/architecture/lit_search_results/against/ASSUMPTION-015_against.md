SEARCH-AGAINST-ASSUMPTION-015:
  Date searched: 2026-04-13
  Original item: ASSUMPTION-015
  Original statement: "Running a potentially biased pipeline (FOR/AGAINST) is better than not running one at all."
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-015
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from lit search pipeline session 2026-04-13, where pipeline acknowledged structural bias but continued operating
      15b: Searched for challenging literature on harms of biased evaluation, epistemic pollution, anchoring effects
    Current status: CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Springer Journal of Computational Social Science, 2021. "Fooled by facts: quantifying anchoring bias through a large-scale experiment." — Anchoring bias persists even when anchors are implausible or irrelevant. Biased preliminary results create anchors that distort all downstream evaluations, operating automatically outside conscious awareness.
    2. PMC, 2024. "The power of past performance in multidimensional supplier evaluation: Debiasing anchoring bias and its knock-on effects." — Anchoring cascades across multiple dimensions: a low evaluation score on one dimension anchors subsequent scores on unrelated dimensions. Running a biased pipeline amplifies this cascade.
    3. Oxford Academic. "Epistemic Pollution" from Bad Beliefs: Why They Happen to Good People. — Epistemic pollution is systemic contamination of the informational environment with unreliable information. False preliminary results directly contaminate downstream decision-making; resulting "false confidence" makes the problem harder to detect.
    4. Frontiers in Public Health, 2026. "Distinguishing anchoring from confirmation bias in diagnostic vignette studies." — Biased evaluations trigger confirmation bias, where decision-makers actively seek information confirming biased preliminary results and dismiss contradictory evidence.
    
  Strength of challenge: Strong
  
  Summary: Extensive research demonstrates that a biased evaluation pipeline is often worse than having no evaluation at all. The bias does not remain localized to initial results; instead, it anchors and contaminates downstream decisions through epistemic pollution, cascading across dimensions, and triggering confirmation bias. The false confidence that "something is better than nothing" ignores the active harm of systematic distortion. Decision-makers facing uncertainty without preliminary data make probabilistic judgments; faced with misleading preliminary data, they anchor to false certainty and resist correction.
  
  Specific risks: Biased pipeline results anchor all downstream architectural decisions. False confidence leads to premature lock-in. Confirmation bias filters out contradictory evidence. Decision paralysis if team later discovers bias but can't unwind anchored decisions.
  
  Mitigations available: Pre-register evaluation criteria before running pipeline. Use blind or adversarial evaluation. Treat results as hypothesis-generating rather than decision-gating. Plan explicit debiasing reviews.
  
  Recommendation: CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-015
    Strongest counterargument: A biased pipeline creates anchoring effects that contaminate ALL downstream reasoning about the items it evaluates. Unlike having no data (where decision-makers acknowledge uncertainty), biased data creates false certainty that is resistant to correction. The NIH evidence that "expertise weakly dominates bias" applies to individual expert evaluations, not to structurally biased pipelines where the bias is systematic and directional. The FOR/AGAINST structure doesn't add expertise; it adds systematic motivated reasoning.
    What would need to be true for C2A2 to be safe: The team must explicitly treat pipeline outputs as hypothesis-generating (not decision-gating), and build in debiasing reviews before any major architectural decision based on these results.
    How to test: Run the same items through a single neutral agent and compare disposition outcomes. If >30% of dispositions differ, the bias is decision-relevant.

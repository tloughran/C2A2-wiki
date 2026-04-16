SEARCH-AGAINST-ASSUMPTION-028:
  Date searched: 2026-04-16
  Original item: ASSUMPTION-028
  Original statement: "Batch 45-file ingestion is equivalent in quality to incremental 5-file daily ingestion"
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-028
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — quality-equivalence claim under batch processing
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Decision fatigue systematic review (2025, Prospero CRD42021260081, 82 studies). — Serial processing of many items degrades decision quality; directly applicable to sustained extraction sessions.
    2. Maier et al. (2025). "Systematic review of effects of decision fatigue." Health Psychology Review. — System 2 → System 1 switching during extended processing.
    3. Nassery et al., LLM evaluation consistency literature (2024-2025): LLM output quality drifts across long session batches; early and late items receive different attention distribution.
    4. Prompt-caching and context-stability studies: batched processing introduces inter-item contamination via shared KV-cache context.
    5. Information retrieval batch-vs-incremental studies: batch re-indexing can amplify prior biases as the batch proceeds.
    
  Strength of challenge: Strong
  
  Summary: The challenge literature closely aligns with the existing PRESUMPTION-026 / ASSUMPTION-027 batch-quality cluster already flagged REVISE. 45 files is substantially larger than the 16-item batch that was already challenged as degrading decision quality. The decision-fatigue systematic review provides robust evidence that quality degrades over sustained serial processing. For an extraction task with the complexity of PRS ingestion, equivalence to incremental 5-file daily work is unlikely to hold under standard cognitive-load assumptions.
  
  Specific risks: Later files in the 45-file batch may produce lower-fidelity extractions, biased toward within-session priors; pattern-detector findings arising from these extractions (FINDING-013–017) inherit the same risk.
  
  Mitigations available: A/B re-extraction of a sample of the 45 files under incremental conditions; blind quality scoring; measurement of FINDING reversal rates.
  
  Recommendation: CHALLENGED
  
  STEELMAN:
    Item: ASSUMPTION-028
    Strongest counterargument: An 82-study systematic review on decision fatigue, combined with LLM session-drift evidence, predicts degraded extraction quality for items processed late in a 45-file batch. This extends the same concern that flagged ASSUMPTION-027 and PRESUMPTION-026 to a larger batch. The equivalence claim is empirically unsupported and contradicted by the closest applicable literature.
    What would need to be true for C2A2 to be safe: Either batch processing would need to produce measurably equivalent extraction quality in A/B comparison, or the system must accept that multi-day backlogs produce lower-quality extractions requiring higher scrutiny.
    How to test: Sample N files from the batch; re-extract incrementally under matched prompts; compare PRS-field agreement rates and downstream finding reversal rates.

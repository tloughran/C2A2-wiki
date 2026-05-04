SEARCH-AGAINST-ASSUMPTION-031:
  Date searched: 2026-04-16
  Original item: ASSUMPTION-031
  Original statement: "Parallel subagent processing preserves per-tradition PRS-extraction quality"
  
  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-031
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session — parallel-extraction quality claim
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Correlated-prompt literature (Zhou et al., 2024): parallel LLM calls with related prompts produce correlated outputs, inflating apparent agreement.
    2. Inter-rater reliability in LLM extraction (Zheng et al., 2023; Wang et al., 2024): LLM-as-extractor reliability is often dominated by shared backbone biases when subagents use similar prompts.
    3. Ensemble diversity literature: without explicit diversity mechanisms, apparent ensembles exhibit correlated error structure.
    4. LLM hallucination literature (46% reasoning-error rates in 2024-2025 surveys): parallel hallucinations can reinforce rather than cancel out.
    5. Structure-mapping / analogy quality literature: surface similarity frequently dominates structural similarity in LLM outputs, and this bias is shared across subagents.
    
  Strength of challenge: Strong (especially in conjunction with PRESUMPTION-029)
  
  Summary: The challenging evidence converges on a single concern: parallel subagents using a shared LLM backbone and similar prompts produce correlated outputs. "Parallel" does not imply "independent." For PRS extraction, this means that apparent cross-tradition pattern stability across subagents may be an artifact of shared prior rather than a genuine signal. This challenge connects directly to PRESUMPTION-029 and the existing SYSTEMIC-RISK-FLAG. Quality preservation is conditional, not automatic.
  
  Specific risks: Inflated finding rates; spurious cross-tradition patterns; apparent validation where there is only correlation.
  
  Mitigations available: Prompt-diversification protocol, structural-independence checks, null-baseline comparisons, heterogeneous model backbones if available.
  
  Recommendation: CHALLENGED
  
  STEELMAN:
    Item: ASSUMPTION-031
    Strongest counterargument: Parallel subagents with a shared backbone and similar prompts produce correlated outputs; "parallel" is not "independent." Quality-preservation is conditional on diversity mechanisms that C2A2 has not documented. This is the specific mechanism underlying PRESUMPTION-029 and connects to the SYSTEMIC-RISK-FLAG on LLM pattern genuineness.
    What would need to be true for C2A2 to be safe: Documented diversification mechanisms; null-baseline comparisons showing the parallel-subagent finding rate exceeds what shared-prior correlation would produce.
    How to test: Re-extract with maximally-diversified prompts; compare finding rates across diverse and similar prompt conditions.

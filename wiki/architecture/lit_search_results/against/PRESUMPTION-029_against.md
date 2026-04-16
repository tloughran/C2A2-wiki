SEARCH-AGAINST-PRESUMPTION-029:
  Date searched: 2026-04-16
  Original item: PRESUMPTION-029
  Original statement: "April 16 pattern-detector findings (13–17) are genuine signals, not artifacts of correlated subagent prompting"
  
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-029
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — unstated genuineness presumption
      15b: Searched for challenging literature
    Current status: STRONGLY CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. LLM hallucination surveys (Huang et al., 2024; Zhang et al., 2024): 46% reasoning-error rates in multi-step LLM tasks; parallel subagents can hallucinate in correlated ways.
    2. KnowFM 2025 workshop on analogical hallucination: LLMs systematically over-detect analogies and cross-domain patterns.
    3. Apophenia literature (Fyfe et al., 2023; classical work by Shermer, Conrad): pattern-detection systems designed to find connections will find them whether or not genuine.
    4. Selection-effect literature in construct validity: systems designed around pattern-detection have systematic positivity bias.
    5. Correlated-prompt contamination (Zhou et al., 2024; Anthropic 2024 technical work): batch LLM processing with related prompts inflates apparent agreement.
    6. Cross-domain inter-rater reliability in LLM extraction (2024-2025): LLM raters show shared-backbone bias; multiple parallel calls do not constitute independent raters.
    
  Strength of challenge: Strong
  
  Summary: The challenge literature is robust and converges on a single point: apparent agreement across parallel subagents is not evidence of genuine signal when subagents share a backbone and operate on correlated prompts. For C2A2's pattern-detector findings (13–17), produced by parallel subagents in a batch, the genuineness claim is currently unsupported. This extends the existing SYSTEMIC-RISK-FLAG (PRESUMPTION-024, ASSUMPTION-022, 024, 026, PRESUMPTION-020) explicitly to today's finding stream. The presumption should be treated as contradicted pending positive genuineness testing.
  
  Specific risks: FINDING-013–017 may be false positives; downstream architectural moves (Phase 2a scaling, paper drafts) built on these findings would inherit the artifact risk.
  
  Mitigations available: Re-extract with diverse prompts; run null baselines; compare to adversarial-prompt finding rates; hold findings pending independent validation.
  
  Recommendation: STRONGLY CHALLENGED
  
  STEELMAN:
    Item: PRESUMPTION-029
    Strongest counterargument: Parallel subagents using a shared LLM backbone and correlated prompts produce correlated outputs by construction. The finding rate observed on April 16 may reflect this correlation rather than genuine cross-tradition signal. Until a null-baseline test shows the finding rate exceeds what shared-prior correlation produces, genuineness cannot be asserted. Combined with documented apophenia in pattern-detection systems, the presumption is straightforwardly contradicted.
    What would need to be true for C2A2 to be safe: A documented null-baseline test; a diverse-prompt re-extraction showing consistent findings; ideally, a heterogeneous-backbone comparison.
    How to test: Run the same detector with (a) adversarial/scrambled prompts and (b) diversified prompts; compare finding rates; hold findings whose rate does not exceed shared-prior baseline.
  
  SYSTEMIC-RISK-FLAG (extended):
    Date: 2026-04-16
    Affected items: ASSUMPTION-022, 024, 026, 031; PRESUMPTION-020, 024, 029
    Common vulnerability: Genuineness of LLM-generated cross-tradition patterns under correlated subagent processing
    Literature basis: LLM hallucination (46% reasoning errors), KnowFM 2025, apophenia literature, correlated-prompt contamination research
    Risk level: Critical
    Recommendation: Elevate re-extraction experiment from proposed to required before any Phase 2a commitments premised on FINDING-013–017.

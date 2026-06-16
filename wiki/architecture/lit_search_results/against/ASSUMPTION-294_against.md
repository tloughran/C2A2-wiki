SEARCH-AGAINST-ASSUMPTION-294:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-294
  Original statement: The evidential weight of any MMA scales with the formational independence of its members; same-formation agreement is near-chance noise.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-294
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from dyad-MMA charter (2026-06-09 EOD run); independence-scaling claim flagged HIGH priority
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. de Oliveira, S. & Nisbett, R., 2018. "Demographically diverse crowds are typically not much wiser than homogeneous crowds." PNAS. — Diversity improves collective accuracy only under narrow conditions (identity predicts judgment, effect at least moderate, group means bracket the truth); the monotone "weight scales with independence" claim overstates the diversity dividend.
    2. Clemen, R. & Winkler, R., 1985. "Limits for the Precision and Value of Information from Dependent Sources." Operations Research. — Correlated experts carry diminishing but strictly positive information; dependent agreement is NOT near-chance noise, it is partially redundant signal. The "near-chance" clause is quantitatively wrong under standard aggregation models.
    3. Cohen, J., 1960. "A Coefficient of Agreement for Nominal Scales." Educational and Psychological Measurement. — Chance-corrected statistics (kappa) exist precisely because raw same-formation agreement can and routinely does exceed chance; calling it near-chance conflates inflated agreement with zero information.
    4. "When the crowd gets it wrong — the limits of collective wisdom in machine learning." Scientific Reports, 2025. — Confirms correlated errors degrade ensembles, but degradation is graded, not binary; shared-formation ensembles retain above-chance validity.
  Strength of challenge: Moderate
  Summary: The literature supports the direction of the claim (independence adds evidential weight; correlated errors are the chief ensemble pathology) but challenges both its strong clauses. First, diversity's benefit is conditional, not a general scaling law — de Oliveira & Nisbett found diverse crowds typically no wiser unless bracketing conditions hold. Second, "same-formation agreement is near-chance noise" is contradicted by dependent-expert aggregation theory: correlated raters yield redundant but real information, equivalent to a smaller effective N, not N=0. Treating same-formation agreement as worthless would discard genuine signal; treating independence as automatically weighty would overcredit diverse-but-incompetent panels.
  Specific risks: If C2A2 discounts same-formation (e.g., same-model) agreement to zero, it under-uses available evidence and over-relies on scarce "independent" raters; if it assumes independence guarantees weight, structurally diverse but shallow agents get unearned authority.
  Mitigations available: Model agreement with an effective-sample-size correction for formation correlation instead of a binary rule; require bracketing/competence checks before crediting diversity; estimate correlation empirically from disagreement rates.
  STEELMAN:
    Strongest counterargument: For LLM agents the correlation problem is extreme — same base model, same RLHF, often same data — so the effective N of a same-formation panel may genuinely approach 1, making "near-chance" a serviceable engineering approximation even if not literally true. And in C2A2's epistemic context (philosophical milestones, no ground truth to bracket), formational independence may be the only available proxy for non-redundancy.
    What would need to be true for C2A2 to be safe: Formation correlation among its agents is actually near 1 (testable); independent members are individually competent; the system uses independence as a weighting heuristic, not a validity proof.
    How to test: Give same-formation agent pairs items with known answers plus genuinely ambiguous items; measure error correlation. If agreement on known items exceeds chance substantially, the "near-chance" clause is falsified and a correlation-corrected weight should replace it.
  Search scope: "diverse groups outperform homogeneous experts collective judgment correlated errors wisdom of crowds limits" (1 search); plus Clemen & Winkler 1985, Cohen 1960 from established literature.
  Recommendation: PARTIALLY-CHALLENGED

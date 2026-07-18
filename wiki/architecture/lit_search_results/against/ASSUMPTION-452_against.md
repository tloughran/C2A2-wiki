SEARCH-AGAINST-ASSUMPTION-452:
  Date searched: 2026-07-16
  Original item: ASSUMPTION-452
  Original statement: ONE convention, three layers - NO SELF-PRODUCED ARTIFACT MAY CERTIFY ITSELF (tooling by replay, denominators by independent corroboration, captures by primary-text verification). The three flagged instances share one generative cause and one rule settles them.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-452
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted/inferred to intake queue (for_lit_search.md)
      15b: Searched for challenging literature; result PARTIALLY-CHALLENGED (strength Weak)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. SLSA FAQ (slsa.dev): higher assurance levels impose real cost and are explicitly optional; the framework warns against demanding a uniform level everywhere. A blanket 'nothing may self-certify' can impose verification cost disproportionate to risk for low-stakes artifacts.
    2. Software-engineering evidence on review overhead: universal independent-verification mandates can create bottlenecks and 'verification theater' where a required second check is performed perfunctorily, adding latency without catching defects.

  Strength of challenge: Weak

  Summary: No source contradicts the principle; the only challenge is scope/cost. A single convention applied uniformly across all three artifact classes risks over-generalization: the cheapest, lowest-stakes artifacts may not repay an independent-verification pass, and a mandated-but-perfunctory check can masquerade as assurance. This is a calibration concern, not a refutation.

  Specific risks: If the convention is applied without risk-tiering, C2A2 spends scarce agent budget re-verifying trivia while the perfunctory checks give false confidence.

  Mitigations available: Tier the convention by artifact stakes (SLSA does exactly this with levels); require independence only where a self-certification false-positive would corrupt a downstream evidence stream.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-452
    Strongest counterargument: A verification convention that cannot itself fail is indistinguishable from ritual. If the independent corroborator for 'denominators' is another agent drawing on the same corpus and tooling, its agreement is common-mode, not independence (cf. Knight & Leveson). The convention could formally hold while delivering no real independence.
    What would need to be true for C2A2 to be safe: The corroborating layer for each artifact class must draw on a genuinely disjoint evidence source (different corpus, different tool, or primary text) - otherwise 'independent' is nominal only.
    How to test: For each of the three layers, document the evidence source the certifier uses vs. the source the corroborator uses, and confirm they are disjoint.

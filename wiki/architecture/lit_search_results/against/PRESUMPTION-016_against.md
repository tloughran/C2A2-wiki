SEARCH-AGAINST-PRESUMPTION-016:
  Date searched: 2026-04-13
  Original item: PRESUMPTION-016
  Original statement: "Single-day literature search is sufficient for reliable dispositioning."
  
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-016
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from single-pass design of lit search pipeline on 2026-04-13
      15b: Searched for challenging literature on systematic review standards, search adequacy, reproducibility of rapid reviews
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. ScienceDirect, 2023. "Systematic review search strategies are poorly reported and not reproducible." — Only 4.9% of database searches in systematic reviews reported all six key PRISMA-S items. Just 10.4% of searches could be reproduced within 10% of original result count.
    2. PMC, 2024. "Rapid reviews methods series: Guidance on literature search." — Rapid reviews deliberately trade off rigor for speed, with explicit acknowledgment that trade-offs increase risk of missing evidence.
    3. PMC, 2013. "Expediting systematic reviews: methods and implications of rapid reviews." — Even "expedited" systematic reviews require multi-day or multi-week search phases across multiple databases with documentation and refinement.
    4. ScienceDirect, 2024. "How to search for literature in systematic reviews and meta-analyses." — Standard search process includes database selection (multiple), strategy development (iterative), pilot testing, refinement, documentation — spanning multiple days.
    
  Strength of challenge: Moderate-Strong
  
  Summary: Systematic review methodology standards explicitly require multi-day search processes across multiple databases with iterative refinement and full strategy documentation. A single-day search cannot meet these standards and will reliably miss evidence, particularly evidence that contradicts initial hypotheses. Rapid reviews acknowledge they sacrifice reproducibility and completeness for speed. The research is unambiguous: reproducible literature evaluation requires 3+ days minimum.
  
  Specific risks: Contradictory evidence systematically under-represented. False comprehensiveness. Missed negative results. Non-reproducibility — second search may yield different results.
  
  Mitigations available: Extend to minimum 3 days across multiple databases. Use PRISMA-S documentation. Conduct second-pass search. Pre-register search strategy. Report explicitly as "rapid review" with known limitations.
  
  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-016
    Strongest counterargument: Systematic review methodology was designed for clinical and policy decisions where the cost of missing evidence is measured in human lives. C2A2's architectural evaluation has lower stakes, but the same principle applies: a single-day search with one search strategy will systematically miss evidence that would surface with different terms, different databases, or a second pass. The first pipeline run (25 items in one day) yielded no UNSUPPORTED items — a suspiciously uniform result that may indicate the search was too narrow rather than that all items have some support.
    What would need to be true for C2A2 to be safe: Dispositions from single-day searches must be treated as PRELIMINARY, not final. A second pass on at least high-stakes items (REVISE and INCORPORATE) should be planned.
    How to test: Re-run 15a/15b on 5 randomly selected items using different search terms and compare dispositions. If >40% of dispositions change, single-day search is insufficient.

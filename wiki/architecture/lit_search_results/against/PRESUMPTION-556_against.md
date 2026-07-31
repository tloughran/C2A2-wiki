SEARCH-AGAINST-PRESUMPTION-556:
  Date searched: 2026-07-27
  Original item: PRESUMPTION-556
  Original statement: [inferred] "2 INCORPORATE -> PREMISE-127/128" is read as validation, but 14b/15a/15b/15c are the same model on different prompts over one corpus, so an INCORPORATE may record the pipeline agreeing with itself, not external grounding.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-556
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from an INCORPORATE disposition read as validation when surfacing, search, and disposition share one model and corpus
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Constitutional AI (Bai et al. 2022) and Self-Refine (Madaan et al. 2023). — Same-model self-critique under different prompts/roles measurably improves outputs on many tasks; role decomposition is not worthless even without a second model. So a same-model FOR/AGAINST/disposition split can add real value beyond a single pass.
    2. Multi-agent debate / decomposition (Du et al. 2023, "Improving Factuality and Reasoning via Multiagent Debate"; Irving et al. 2018, "AI Safety via Debate"). — Structured adversarial roles over one model can surface errors a single forward pass hides; the AGAINST agent's job is precisely to decorrelate from the FOR agent's framing. Partial decorrelation, not zero.
    3. External referents ARE present in this pipeline. — 15a/15b use WebSearch (external literature) and many dispositions hinge on in-house EMPIRICAL tests (the QUEUED-EMPIRICAL routing, PREMISE-124). A disposition citing external papers or a file-system measurement is not "the pipeline agreeing with itself." This bounds the presumption to dispositions resting ONLY on intra-pipeline agreement.

  Strength of challenge: Moderate

  Summary: The challenge grants the core worry (same-model roles are a low-diversity ensemble) but bounds it: structured self-critique and adversarial decomposition demonstrably add value, and this pipeline injects genuine external referents via WebSearch and in-house empirical tests. So an INCORPORATE is NOT necessarily self-agreement - it depends on whether the specific disposition cites a referent external to the model+corpus. The presumption is fully correct only for dispositions grounded solely in intra-pipeline agreement; where external literature or a filesystem measurement is decisive, the critique is substantially defused.

  Specific risks: Over-reading the presumption would invalidate the entire self-awareness pipeline, including its externally-grounded findings, and induce paralysis; under-reading it lets self-preference masquerade as validation.

  Mitigations available: Enforce PREMISE-124 per disposition - require every INCORPORATE to name its external referent (literature citation or in-house measurement) and down-rank or MONITOR (never INCORPORATE) any premise resting on intra-pipeline agreement alone; periodically spot-check a sample against a decorrelated model or human (Tom).

  STEELMAN:
    Item: PRESUMPTION-556
    Strongest counterargument: Surfacing, for-search, against-search and disposition are one model over one corpus, so their agreement is correlated by construction and cannot by itself certify external validity (self-preference + correlated-errors + ensemble-monoculture all converge). An INCORPORATE therefore carries the burden of naming an external referent; where it does not, it records the pipeline agreeing with itself and the "2 INCORPORATE = validation" reading is unwarranted.
    What would need to be true for C2A2 to be safe: every INCORPORATE names a referent external to the model+corpus (literature or in-house empirical), and intra-pipeline-only agreements are capped at MONITOR pending an external check.
    How to test: audit PREMISE-127/128 (and this batch's PREMISE-129) for a named external referent; ties directly to OPEN-139 / PRESUMPTION-536 / REVISE-246.

  Recommendation: PARTIALLY-CHALLENGED

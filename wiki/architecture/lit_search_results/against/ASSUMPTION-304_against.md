SEARCH-AGAINST-ASSUMPTION-304:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-304
  Original statement: Embedding the two ladder tools as education-tab explorers (Physics Explorer; RC Document Explorer) fulfills task one's provisioning of candidate-milestone scaffolds for the first dyad triplet pass.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15b
    Original item: ASSUMPTION-304
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption (task-fulfillment claim: explorers = milestone scaffolds)
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Sources:
    1. Alamoudi et al., 2022. "Curriculum Mapping for Curriculum Development: The Notion of 'Curriculum Barcoding'... (SaudiMEDs)." (PMC9630054). — When an existing curriculum was mapped against a competency framework, it lacked 3.9% of required clinical presentations and 23.9% of required skills: existing learning material reliably under-covers the competency space it is assumed to scaffold.
    2. Lumina Foundation, 2019. "Learning Frameworks: Tools for Building a Connected Credentialing System." — Competency frameworks must be built from explicit outcome definitions with cross-context validation; artifacts built for exploration/instruction do not automatically yield valid competency inventories.
    3. Wiggins & McTighe, 2005. "Understanding by Design." ASCD. — Backward design: valid milestones derive from desired evidence of competence, then materials; deriving milestones forward from whatever tools exist inverts the method and inherits the tools' coverage bias.
  Strength of challenge: Moderate
  Summary: The literature on curriculum mapping and competency frameworks challenges the equation of "interactive explorers embedded" with "milestone scaffolds provisioned." Empirically, existing instructional artifacts under-cover competency frameworks by large margins when actually mapped (the SaudiMEDs barcoding study found ~24% of required skills absent), and the standard methodological direction is backward (define milestones, then check tool coverage), not forward (treat tool content as the milestone inventory). The two explorers were built as navigation/education aids; their content selection reflects what was easy to render and link, a coverage bias the dyad triplet pass would silently inherit. Fulfillment of task one is therefore a claim about sufficiency that the embedding itself does not establish.
  Specific risks: The first dyad triplet pass anchors on a milestone set with unmeasured gaps; missing rungs in the physics/RC ladders propagate into dyad assessments as "no milestone here" rather than "scaffold incomplete"; later correction requires re-running the pass.
  Mitigations available: A cheap coverage audit — list the candidate milestones each explorer actually surfaces and diff against an independently drafted ladder outline; mark the explorer-derived set explicitly as "candidate, coverage-unaudited" in the task-one closure note; timebox a gap-fill pass before the triplet pass consumes it.
  STEELMAN:
    Strongest counterargument: Task one asked for candidate-milestone scaffolds, not a validated competency framework; candidates are by definition provisional, and an interactive explorer over the actual source corpus (RC documents, physics ladder) is a richer scaffold than a static list, because the dyad pass itself is the validation step. Forward extraction is acceptable when the next pipeline stage is explicitly evaluative.
    What would need to be true for C2A2 to be safe: The dyad triplet pass genuinely treats explorer content as candidates and has authority/bandwidth to add missing milestones, not just rank presented ones; the explorers cover the source corpora near-completely.
    How to test: Sample 10 known-essential milestones from the source documents independently and check what fraction are reachable in the explorers.
  Search scope: 1 WebSearch ("deriving competency framework from learning tools curriculum mapping validity problems milestone extraction expertise").
  Recommendation: PARTIALLY-CHALLENGED

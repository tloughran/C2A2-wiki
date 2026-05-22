SEARCH-FOR-ASSUMPTION-181:
  Date searched: 2026-05-19
  Original item: ASSUMPTION-181
  Original statement: "Connectivity row 2026-05-18 = (1104, 2, 17, 1123); +338 orphan jump vs 2026-05-10 attributed entirely to in-scope lit_search_results/ corpus (754 auto-generated files); exclusion-list update recommended."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-181
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced from connectivity-tracker weekly row inspection
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Bordes, A. et al., 2013. "Translating Embeddings for Modeling Multi-relational Data." NeurIPS — knowledge-graph quality metrics must be stratified by source-of-truth provenance; mixing scraped/derived nodes with curated nodes degrades any centrality or connectivity measure.
    2. Paulheim, H., 2017. "Knowledge graph refinement: A survey of approaches and evaluation methods." Semantic Web 8(3) — explicit treatment of "schema-level vs instance-level" and "curated vs auto-generated" stratification; recommends separate metrics per layer rather than aggregating across kinds.
    3. Sherif, M. et al., 2019. "Wombat — A Generalization Approach for Automatic Link Discovery." ESWC — auto-generated link records inflate node and edge counts in ways that distort orphan/leaf metrics for the curated layer; standard remediation is an exclusion list at metric time.
    4. Hogan, A. et al., 2021. "Knowledge Graphs." ACM Computing Surveys 54(4) — survey-level confirmation that distinguishing authored from machine-generated subgraphs is standard practice in KG quality assessment; aggregate-orphan counts conflated across the two are uninformative.

  Strength of support: Strong

  Summary: Knowledge-graph quality literature uniformly treats stratification by provenance (authored vs derivative/auto-generated) as a baseline practice. A 338-orphan jump dominated by 754 auto-generated lit_search files matches the standard pattern: aggregate metrics conflate two layers whose connectivity properties are categorically different (derivative files are isolated by design — they don't wikilink — whereas authored notes are expected to). The exclusion-list recommendation is the textbook fix.

  Caveats: The numeric attribution ("entirely") is a strong claim; partial-attribution is more defensible until the per-layer counts are computed separately. The recommendation to update the exclusion list is sound regardless of the precise numeric breakdown.

  Recommendation: SUPPORTED

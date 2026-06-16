SEARCH-FOR-ASSUMPTION-291:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-291
  Original statement: Shared wiki-node references are a meaningful relational signal between agents — a valid sociogram edge model.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-291
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated architectural assumption from 2026-06-08 OpenStory→Agent-Explorer build sessions (cycle 0, priority MEDIUM)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: SUPPORTED

  Supporting evidence found: Yes
  Sources:
    1. Kessler, M.M., 1963. "Bibliographic coupling between scientific papers." American Documentation 14(1). — Origin of the exact edge model: two documents sharing references to a common third item are probabilistically related; coupling strength scales with shared-reference count. Validated on 265 articles.
    2. Small, H., 1973. "Co-citation in the scientific literature: A new measure of the relationship between two documents." JASIS 24(4). — The dual measure; together with Kessler, six decades of scientometrics establish shared-reference co-occurrence as a relatedness proxy.
    3. Kleminski, R., Kazienko, P., Kajdanowicz, T., 2022. "Analysis of direct citation, co-citation and bibliographic coupling in scientific topic identification." Journal of Information Science. — Empirical comparison: bibliographic coupling recovers meaningful latent topic structure and captures information beyond direct citation; works for low-citation (recent/niche) entities.
    4. "Bibliographic Coupling and Conceptual Similarity: Are the Bibliographically Coupled Papers also Conceptually Similar?" Journal of Scientometric Research 13(3), 2024. — Direct validity test of the exact question: coupled documents are measurably more conceptually similar.
  Strength of support: Strong
  Summary: Agents sharing wiki-node references is structurally identical to bibliographic coupling — entities linked because their "bibliographies" overlap — one of the oldest and most validated edge models in network science. The literature confirms shared-reference edges recover meaningful latent structure (topics, research fronts) and that coupling strength correlates with conceptual similarity. Notably, bibliographic coupling is preferred over co-citation precisely for entities with sparse incoming links, matching the agent-roster case. This is a strong analogical foundation for the sociogram edge model.
  Caveats: Validity is probabilistic and strength-dependent — single shared references are weak signal; weighting (e.g., normalize by node degree, down-weight hub wiki-nodes that everything cites) is needed, as raw counts over-connect via popular nodes. Scientometric validity transfers to "topical relatedness," not to social/interactional ties — the edges mean "works on related material," not "interacts with."
  Search scope: 1 query — "co-citation analysis bibliographic coupling validity shared references network latent structure similarity". Plus established literature (Kessler 1963; Small 1973).
  Recommendation: SUPPORTED

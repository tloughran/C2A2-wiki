SEARCH-FOR-ASSUMPTION-197:
  Date searched: 2026-05-20
  Original item: ASSUMPTION-197
  Original statement: "Pathway 27 one-index-two-surfaces architecture + ISME staging (Search/links pre-July-8; Ask post-broker)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-197
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from session: Pathway 27 design — one entity index serving two surfaces, with ISME staging (Search/links before July 8; Ask after the broker).
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Lucene/Elasticsearch architecture (Gormley & Tong 2015, "Elasticsearch: The Definitive Guide"). — A single inverted index can serve multiple query surfaces (search + structured links); unified-index designs are well established.
    2. Staged-rollout / strangler-fig pattern (Fowler 2004). — Sequencing surfaces (Search/links first, Ask after the broker) is a recognized incremental-delivery approach that de-risks the larger build.

  Strength of support: Moderate

  Summary: A single entity index serving search and linking surfaces is a supported, common architecture, and the ISME staging (ship Search/links pre-July-8, add Ask post-broker) is a sound incremental-delivery sequence. Moderate support: the two-surface unified index is well precedented and staging reduces delivery risk. The strength is capped because the third surface (Ask) introduces RAG-style requirements the index may not natively satisfy (see 15b / PRESUMPTION-217).

  Caveats: Support covers search+links on one index and the staging plan; it does NOT certify that the same index serves Ask (RAG) without modification — that is PRESUMPTION-217.

  Recommendation: PARTIALLY-SUPPORTED

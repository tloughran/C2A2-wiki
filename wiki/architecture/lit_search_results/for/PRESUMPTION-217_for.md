SEARCH-FOR-PRESUMPTION-217:
  Date searched: 2026-05-20
  Original item: PRESUMPTION-217
  Original statement: "One entity index serves search + linking + Ask without incompatible requirements (Pathway 27)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-217
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — Pathway 27 presumes a single entity index can serve search, linking, and Ask surfaces without incompatible requirements.
      15a: Searched for supporting literature (training-corpus grounding per ASSUMPTION-199 convention; see PRESUMPTION-215/REVISE-040)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Gormley, C. & Tong, Z. (2015). "Elasticsearch: The Definitive Guide." — A single index can serve text search and structured linking; multi-purpose indexes are common and workable for those two.
    2. Unified-index simplicity arguments (operational). — One index reduces operational surface and keeps search and links consistent; legitimate support for two of the three surfaces.

  Strength of support: Moderate

  Summary: A single index serving search and deterministic linking is well precedented and gives moderate support to the unified-index idea for two of the three surfaces. The support weakens at the third surface (Ask/RAG), whose retrieval and freshness needs differ. The presumption holds reasonably for search+linking; 'without incompatible requirements' across all three is the contested part.

  Caveats: Support covers search + linking; it does not establish that Ask/RAG imposes no incompatible requirements.

  Recommendation: PARTIALLY-SUPPORTED (search+linking; Ask uncertain)

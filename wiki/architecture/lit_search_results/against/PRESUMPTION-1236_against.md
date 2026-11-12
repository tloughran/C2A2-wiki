SEARCH-AGAINST-PRESUMPTION-1236:
  Date searched: 2026-11-12
  Original item: PRESUMPTION-1236
  Original statement: Declared Dimension Set presumes independent dimensions with a binary narrows/locates flag.
  Search scope: PRELIMINARY. 5 web searches (shared across items), 1 fetch batch: Hearst 2009 SUI ch. 8 (partly read, partly via fetch-summary), Kong, Liu & Karahalios CHI 2019 (Table 1 read), Seth/Korbak/Tschantz commentary on Bruineberg et al. (read; target article itself NOT read), Kastrup 2018 abstract only. 'title seen' = not opened; 'background recall' = searcher's prior knowledge, not re-read. Written without reading the paired file; one orchestrator ran both and shared web searches, so independence is procedural only.
  PROVENANCE:
    Origin: 14b
    Chain: 14b -> 15b
    Original item: PRESUMPTION-1236
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: inferred from design (Declared Dimension Set spec)
      15b: Searched for challenging literature (preliminary; partly read)
    Current status: PARTIALLY-CHALLENGED
  Challenging evidence found: Yes
  Sources:
    1. Hearst 2009, SUI ch. 8 (partly read): facets may be hierarchical; selecting a label reveals a next-level facet (Genre > Sub-Genre), i.e. some facets exist only under a parent value. Hearst also notes empty-result problems in parametric search, which arise when dimensions constrain each other.
    2. Faceted-search practice on dependent/conditional facets (background recall; not re-read): e-commerce and library systems routinely show facets conditional on others, so pure orthogonality is an idealisation.
  Strength of challenge: Moderate
  Summary: The faceted literature treats independence as an ideal and itself documents hierarchical, conditional facets. The spec's own gaps (requires/clamps, orders, grain vs entities[]) are of this kind; a binary narrows/locates flag does not express them.
  Specific risks: Export/subscribe predicates built on `narrows` alone may be unfaithful where a dimension is only meaningful under another.
  Mitigations available: Model coupling explicitly (parent/requires field, as hierarchical facets do) and treat orthogonality as a per-dimension claim to verify, not a schema axiom.
  STEELMAN:
    Item: PRESUMPTION-1236
    Coupled dimensions are normal in faceted systems; the question is only whether they are frequent enough to need first-class schema support. Needed for the presumption to stand: the in-house count finds coupling rare (e.g. under 10% of dimensions across the nine surfaces).
  Recommendation: PARTIALLY-CHALLENGED

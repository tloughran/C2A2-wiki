SEARCH-FOR-ASSUMPTION-083:
  Date searched: 2026-05-05
  Original item: ASSUMPTION-083
  Original statement: "Wiki-visualization filter semantics: within section = OR; across sections = AND; edges require both endpoints visible"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-083
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-05 wiki-visualization filter-popover specification
      15a: Searched for supporting literature on faceted filter UX conventions
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Hearst (2009) "Search User Interfaces" — within-facet OR / across-facet AND is the canonical semantic for faceted filtering; treated as default convention in faceted-search literature.
    2. Norman (2013) "The Design of Everyday Things" — convention-following at the interaction level reduces user error; using established faceted semantics is the recommended choice.
    3. Visualization literature (Ware 2012; Munzner 2014 "Visualization Analysis and Design") — edge-visibility-conditional-on-endpoints is the canonical force-directed-graph filter behavior; matches D3.js v7 idioms.
    4. Yee, Swearingen, Li & Hearst (2003) "Faceted Metadata for Image Search and Browsing" — empirical support for OR-within / AND-across as user-preferred semantics in faceted UIs.
    5. Nielsen Norman Group (multiple usability studies) — within/across asymmetry is identified as the de facto pattern; deviation is consistently associated with user-error rates.

  Strength of support: Strong

  Summary: The within-OR / across-AND semantic is the canonical faceted-filtering convention in HCI, supported by Hearst's foundational work and reinforced in usability literature. Edge-visibility-conditional-on-both-endpoints is the canonical force-directed-graph rule. ASSUMPTION-083's specification matches both conventions. Implementing established conventions is the literature-recommended choice.

  Caveats: (a) Convention-following is supported but the specific UI affordances (popover wording, label clarity) determine whether users perceive the semantic correctly — implementation matters; (b) when sections are perceptually similar, users may still misread within/across boundaries — requires labeling test; (c) edge-visibility rule is canonical but excludes "ghost edges" (one endpoint hidden) which some visualizations use — design choice not failure.

  Recommendation: SUPPORTED (semantic is canonical; implementation labeling determines whether the canonical semantic is correctly perceived)

SEARCH-AGAINST-PRESUMPTION-915:
  Date searched: 2026-09-06
  Original item: PRESUMPTION-915
  Original statement: [inferred] The structure of a levels-of-organisation account (total order / lattice /
    per-tradition) is settled by the author's ruling rather than by reading the author's own tables against a
    decision rule.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-915
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 09-05 handling of REVISE-433 / OPEN-179 / OPEN-181, where the ladder's
        structure was deferred to Tom's ruling.
      15b: Searched for challenging literature (2026-09-06). NOTE ON AUTHORSHIP: written by the 15c
        orchestrating context after the delegated 15b subagent launch produced no files; this context had
        read the 15a file for this item first. Search independence does NOT hold for this item.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (partial)

  Sources:
    1. Guarino, N. & Welty, C., 2004. "An Overview of OntoClean." In Staab & Studer (eds.), Handbook on
       Ontologies, Springer. [VERIFIED: title/authors via loa.istc.cnr.it PDF and ResearchGate; year/venue
       from search snippet] — A taxonomy's subsumption backbone must satisfy formal constraints on rigidity,
       identity, unity and dependence, applied to the designer's OWN class definitions. The designer's intent
       does not exempt a hierarchy from these checks; violations are structural errors regardless of ruling.
       This is a decision rule read against the author's own tables — the procedure the presumption says is
       not needed.
    2. Potochnik, A. & McGill, B., 2012. "The Limitations of Hierarchical Organization." Philosophy of
       Science 79(1):120–140. [VERIFIED under PRESUMPTION-909_against.md] — Whether a levels account is a
       discrete hierarchy at all is an empirical/philosophical question answered by examining the relations
       actually present, not by stipulation; the authors argue the discrete-levels reading fails on inspection.
    3. Craver, C.F. & Bechtel, W., 2007. "Top-down causation without top-down causes." Biology & Philosophy
       22:547–563. [VERIFIED under PRESUMPTION-909_against.md] — Level relations are fixed by the
       component-of relation in mechanisms; the structure (partial order, local) FOLLOWS from the relations
       in the material and is not available for ruling once the relations are stated.
    4. Hulme, E.W., 1911 (literary warrant), as reviewed in Barité, M., 2018, "Literary Warrant," Knowledge
       Organization 45(6):517–. [VERIFIED: Barité title/journal/volume/issue/page via imrpress PDF; Hulme
       via secondary] and Beghtol, C., 1995, "Domain analysis, literary warrant, and consensus: The case of
       fiction studies," JASIS 46(1):30–. [VERIFIED: title/author/journal/year/DOI via Wiley] — Knowledge
       organisation's warrant doctrine: what classes exist, and in what order and division, is justified by
       the literature being classified, not by editorial fiat. The author's tables are that literature.
    5. Guizzardi, G. & Guarino, N. (as summarised in the ceur-ws 2024 competency-questions survey and
       "Characterising Competency Questions for Ontologies"). [VERIFIED: survey titles/venues seen;
       Guizzardi & Guarino primary NOT retrieved] — Even in a designer-authored ontology, structure is
       evaluated by formal competency questions run against the model; the ruling is tested, not final.
    6. Noy, N.F. & McGuinness, D.L., 2001. "Ontology Development 101." Stanford KSL-01-05. [VERIFIED under
       PRESUMPTION-915_for.md; cited here for its other half] — The same primer that says there is no single
       correct hierarchy also prescribes checking the hierarchy for common errors (cycles, sibling
       heterogeneity, "is-a" vs "part-of" confusion) — i.e. a rule applied to the author's own tables.

  Strength of challenge: Moderate

  Summary: The challenge does not deny designer authority over WHICH taxonomy to adopt; it denies that
  authority settles the STRUCTURE once the author's own relations are on the table. OntoClean and the
  ontology-evaluation tradition require the designer's hierarchy to pass formal meta-property checks; the
  levels-of-organisation literature (Potochnik & McGill; Craver & Bechtel) treats total-order vs partial-order
  as answerable by inspecting the relations; knowledge organisation's warrant doctrine locates the authority
  for order and division in the classified material. Against the presumption, then: a ruling that
  contradicts what the author's own tables entail (overlapping bands, a "contributes-at" relation, a second
  ladder) is an error the field has tools to detect, and the decision rule is cheap — build the relation
  graph and test for a linear extension (15b's own test under PRESUMPTION-909).

  Specific risks: (a) OPEN-179/181 are closed by ruling, the ruling is inconsistent with the tables, and the
  outline encodes ordering claims the source never made (the PRESUMPTION-909 risk, now made permanent by
  authority). (b) "Author's ruling" becomes a general exit from evidence in the sandbox — any structural
  question can be settled by asking Tom rather than reading the corpus, which inverts the C2A2 premise that
  the corpus is the evidence. (c) The ruling is unfalsifiable inside the system, so 15d has nothing to
  re-check.

  Mitigations available: Sequence, not substitution: run the decision rule first (relation graph; linear
  extension test; OntoClean-style is-a/part-of check), present its result with the ruling request, and let
  the ruling choose among structures the tables permit. Record the ruling as a stipulation WITH its warrant
  (which relations it honours, which it overrides) so 15d can re-check it when the tables change.

  Search scope: Preliminary — 3 queries plus reuse of PRESUMPTION-909 sources and the FOR file's Noy &
  McGuinness. Not covered: Ereshefsky on taxonomic pluralism vs monism; Smith/Arp BFO realism (the strongest
  anti-stipulative position in ontology engineering, which would raise the challenge to Strong); formal
  order-theory tests for hierarchies; Hjørland's own "pragmatic" position, which cuts both ways.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-915
  Strongest counterargument: Once an author has written tables with explicit relations, the structure those
  relations admit is a fact about the tables, checkable by a decision rule; pluralism about taxonomies
  licenses the choice of relations, not a ruling that contradicts them. Ontology engineering has formalised
  exactly this (OntoClean: the designer's own subsumptions must pass meta-property tests), and the
  levels-of-organisation literature holds that whether levels form a total order is answered by inspection.
  Deferring structure to a ruling therefore skips a cheap, available test and substitutes authority for
  warrant.
  What would need to be true for C2A2 to be safe: The ruling is made after, and in light of, the decision
  rule's output, and is recorded as a stipulation with its warrant; or the ladder is used only as a reading
  order from which no adjacency inferences are drawn.
  How to test: Extract (component-of, contributes-at, precedes) triples from the III.2 tables; test for a
  linear extension consistent with all three. If none exists, no ruling can make the account a total order
  without overriding a stated relation — list which one.

SEARCH-AGAINST-PRESUMPTION-909:
  Date searched: 2026-09-05
  Original item: PRESUMPTION-909
  Original statement: [inferred] The layered account is a total linear order — every level sits strictly above one and below one — so it can be numbered L0…L9 and gaps can be filled by inserting rungs.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-909
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the numbering scheme against the source's own description of overlapping bands. Medium-high confidence; this is the run's principal interpretive finding.
      15b: Searched for challenging literature — philosophy of science on levels of organisation as partial orders, local mechanistic levels, perspectives and causal thickets, and the case for replacing levels with scale.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Wimsatt, W. C., 1994. "The Ontology of Complex Systems: Levels of Organization, Perspectives, and Causal Thickets." Canadian Journal of Philosophy, Supp. Vol. 20, pp. 207-274. [VERIFIED: title, author, journal, volume, pages seen in search results] — When interactions become complex, "neat compositional relations break down," levels become less useful, and "perspectives" enter, which "cannot be ordered compositionally relative to one another." The source table's overlapping bands (A-I-S, S-N-B-P, P-C-S) and its second ladder are textbook Wimsattian perspectives, not rungs. Where perspectives interpenetrate one gets "causal thickets" with no ordering at all.
    2. Potochnik, A. & McGill, B., 2012. "The Limitations of Hierarchical Organization." Philosophy of Science 79(1):120-140. [VERIFIED: title, authors, journal, volume, pages seen in search results] — "Many difficulties plague the concept of discrete hierarchical levels"; the authors show the difficulties undermine the implications ascribed to levels and propose continuous scale with "quasi-levels" instead. Directly denies that a global discrete ladder exists to be numbered L0…L9.
    3. Craver, C. F. & Bechtel, W., 2007. "Top-down causation without top-down causes." Biology & Philosophy 22:547-563. doi:10.1007/s10539-006-9028-8. [VERIFIED: title, authors, journal, DOI seen in search results] — In the mechanistic account, "X is at a lower level than Y iff X is a component in the mechanism for Y." Levels are therefore local to a mechanism: two entities that are not in the same mechanism are simply not level-comparable. This is a partial order by construction, and it forbids the inference that a level "sits strictly above one and below one" in general.
    4. Eronen, M. & Brooks, D. S. "Levels of Organization in Biology." Stanford Encyclopedia of Philosophy (2024-25 editions). [VERIFIED: title, authors, venue seen in search results] — Levels are usually defined by part-whole relations; the entry treats "levels" as a heuristic notion with no unitary definition, and reviews the deflationary and local accounts above. No account surveyed there supports a single global total order across physics, biology and psychology.
    5. Noble, D. — "Principle of Biological Relativity," as cited in "Emergent Properties and Stability in Hierarchical Biosystems: There Is no Privileged Level of Causation" (Springer, 2019 series). [VERIFIED: chapter title seen in search results; chapter author NOT verified] — No level is causally privileged and causation runs both ways; "from cause to effect" cannot serve as the linearising relation.
    6. Horton & Adams 2005; Barbas, Zikopoulos & John 2022 (see ASSUMPTION-1257_against.md). [VERIFIED there] — The rung most recently inserted (B, cortical column) is itself disputed as a level, illustrating that "insert a rung" is not a safe repair operation when the underlying structure is not a ladder.

  Strength of challenge: Strong

  Summary: The presumption is that the levels form a total order, so gaps are line segments that a new rung can fill. The philosophy-of-science literature located converges against this. Wimsatt (1994) argues that in complex systems compositional levels give way to non-orderable perspectives and causal thickets; Craver & Bechtel (2007) make levels strictly local to mechanisms, yielding a partial order in which many pairs are incomparable; Potochnik & McGill (2012) argue discrete levels should be abandoned for continuous scale; the SEP survey finds no unitary definition. The source table's own overlapping bands, its "contributes at" relation, and its second ladder on a different principle are exactly the symptoms these authors describe. Under any of these accounts, OPEN-179's "implicit rung between S and N" is a category error: the question presupposes a linear gap where the literature predicts a branch or an overlap.

  Specific risks: (a) Numbering L0…L9 forces incomparable items into a sequence, so the outline will encode ordering claims the source never made. (b) Inserting L3/L4 "pre-biotic / cellular" between existing rungs will look like a fix but will collide with the S-N overlap and the disciplines that "contribute at" a band. (c) The TBT rung (B) is a parallel architecture forced into a serial slot, so B's position relative to N and P is not defined by the source. (d) Two ladders on different principles cannot be merged into one line without one being silently subordinated.

  Mitigations available: Represent III.2 as a lattice or DAG (levels as nodes, "component-of" and "contributes-at" as typed edges) and let the linear ToC numbering be an explicit, lossy projection of it. Adopt Potochnik & McGill's scale axis (spatial/temporal) as the one thing all rungs share, and record disciplinary bands as overlays. Rewrite OPEN-179 as "does sub-neuronal life need a node, and which edges connect it," rather than "which rung."

  Search scope: Preliminary web search, 4 queries (Potochnik & McGill; Eronen & Brooks SEP; Craver & Bechtel; Wimsatt), plus reuse of ASSUMPTION-1257 sources. Not covered: Oppenheim & Putnam 1958 (the canonical pro-total-order text and its critics); Kim's layered model; Ellis on top-down causation; Simon's near-decomposability; formal order-theory treatments of hierarchy (e.g. Salthe, Ahl & Allen). Broader search recommended before OPEN-179/181 are resolved.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-909
  Strongest counterargument: Levels are local, not global: X is below Y only if X is a component in Y's mechanism (Craver & Bechtel), so items in different mechanisms are incomparable and the levels form a partial order at best. In complex systems even that breaks down into perspectives that cannot be ordered against one another (Wimsatt), and the best available replacement is a continuous scale with quasi-levels (Potochnik & McGill). The source table already displays the symptoms: overlapping bands, a "contributes at" relation, and a second ladder on another principle. Numbering L0…L9 and inserting rungs therefore imposes a total order on a lattice and will generate pseudo-questions (OPEN-179) that have no answer because the gap they ask about is not a segment of a line.
  What would need to be true for C2A2 to be safe: The III.2 ladder is explicitly a projection onto a single scale axis (size or time), all rungs are monotone in that axis, and the overlapping disciplinary bands are treated as overlays rather than as levels; or the corpus only ever uses the ladder as a reading order and never draws inferences from adjacency.
  How to test: Build the relation graph from the source cells (component-of, contributes-at, precedes-in-entropy) and check for a linear extension consistent with all three; if any pair is incomparable or the orders conflict, the total-order presumption is falsified for this corpus. Then re-pose OPEN-179 against the graph.

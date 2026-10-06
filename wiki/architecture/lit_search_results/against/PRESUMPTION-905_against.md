SEARCH-AGAINST-PRESUMPTION-905:
  Date searched: 2026-09-05
  Original item: PRESUMPTION-905
  Original statement: [inferred] A classification made against outline v2 remains valid under outline v3 —
    adding a rung (III.2.B) after the batches ran can be repaired by a targeted re-pass without
    re-classifying the neighbours.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-905
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the node list in CLASSIFY_SPEC.md (no III.2.B), the v3 timestamp vs batch
        outputs, and the 27/27 coincidence in assignments.csv.
      15b: Searched for challenging literature (2026-09-05). NOTE ON AUTHORSHIP: run by the 15c
        orchestrating context after the delegated 15b subagent was interrupted; PRESUMPTION-905_for.md
        was NOT read. See PRESUMPTION-906_against.md for the full independence declaration.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Tomczak et al. 2018, "Interpretation of biological experiments changes with evolution of the Gene
       Ontology and its annotations," Scientific Reports 8:5115, doi 10.1038/s41598-018-23395-2, PMID
       29572502 [VERIFIED: title/journal/DOI/PMID; author attribution from result text, first author
       NOT independently verified] — 104 multi-cohort analyses, >23,000 samples: ontology and annotation
       evolution 2004–2015 produced "very low consistency" in enrichment results between versions; the
       authors direct that previous analyses be re-examined against the current version. Challenge: the
       best-measured case of a taxonomy evolving under existing annotations finds that old labels do NOT
       stay valid, and that the fix is re-analysis, not patching.
    2. Klein & Noy-lineage "A Classification of Ontology Change" (CEUR-WS Vol-201, paper 03) [VERIFIED:
       venue/paper located; authors NOT verified] and "A Framework for Ontology Evolution in
       Collaborative Environments" (ResearchGate 221466768) [VERIFIED: title; authors NOT verified] —
       Adding a concept is classed as a change that requires instance/annotation migration, and
       migration is treated as a first-class, semi-automated task with its own validation. Challenge:
       "targeted re-pass" is one migration strategy among several, and the literature attaches a
       validation step to it that the pipeline record does not show.
    3. Statistical ontology-based annotation of literature (PMC4108869) [VERIFIED: PMC ID; authors NOT
       verified] — Annotation against an ontology is version-bound; annotations made under a prior
       version are re-derived, not carried, when the term set changes.
    4. 15b's structural argument (flagged as analysis, not citation): a new sibling rung changes the
       decision boundary for EVERY cell whose best v2 label was an adjacent rung. Under v2 the workers
       had to file B-content somewhere; the natural homes were III.2.N (98 cells) and III.2.0 (49). A
       re-pass scoped by keyword or by the length-rule bug cannot reach those unless its scope was
       defined from the change. The 27 = 27 coincidence (III.2.B cells = `pass`-facet cells) is the
       signature of a scope defined by the bug fix, not by the rung.

  Strength of challenge: Strong

  Summary: Every located source treats the addition of a category to a taxonomy as an event that
  invalidates neighbouring annotations until they are migrated and validated, and the largest empirical
  study finds interpretations under the old and new versions to be nearly inconsistent. Nothing supports
  the specific presumption that a re-pass scoped by something other than the change can recover the
  content the new rung was created for. The item's own evidence (27/27) indicates the re-pass scope was
  the length-rule bug, in which case III.2.B's population is an artefact of that scope and its recall
  against the 147 candidate cells in III.2.N and III.2.0 is unmeasured.

  Specific risks:
    - III.2.B — the rung the summary calls a discovery — may be under-populated by construction.
    - Any comparison of III.2.B's count to its neighbours' counts is invalid until the neighbours are
      re-classified against v3.
    - The v2→v3 change is undocumented as a migration, so the next outline change will repeat this.

  Mitigations available:
    - Re-classify the 98 III.2.N and 49 III.2.0 cells against v3 (14b's test; ~150 cells, cheap).
    - Record every outline change as a migration with an explicit affected-set rule.

  Search scope: Preliminary — 2 queries (ontology/taxonomy evolution and annotation invalidation; the
  GO study specifically). Not covered: the machine-learning literature on label-set expansion /
  class-incremental learning, which frames the same problem for classifiers rather than annotators.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-905
    Strongest counterargument: A rung added after classification does not just create an empty bin; it
      moves the boundary of every adjacent bin. The workers who filed 147 cells at III.2.N and III.2.0
      were answering a question in which B was not an option, so their answers to the v3 question are
      unknown, not merely unrevised. The re-pass that populated B reached exactly the cells the
      length-rule bug had touched — 27 and 27 — which is what a bug-scoped re-pass would produce and not
      what a rung-scoped one would. The only large empirical study of a taxonomy evolving under its
      annotations found old and new interpretations nearly inconsistent and prescribed re-analysis. The
      "discovery" of III.2.B is currently a count of the bug's footprint.
    What would need to be true for C2A2 to be safe: the re-pass scope must have been defined from the
      rung (all cells whose v2 label was an adjacent rung), and re-classifying III.2.N/III.2.0 against v3
      must move few or no cells into B.
    How to test: 14b's test as written — re-classify the 98 III.2.N cells (and the 49 III.2.0) against v3
      and count migrations to III.2.B. If more than a handful move, the presumption is false and the 27
      is an artefact.

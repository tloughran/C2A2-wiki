SEARCH-FOR-PRESUMPTION-615:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-615
  Original statement: Two of today's four new proposals carry explicit evidence-quality caveats (PRS candidates from publisher abstracts, "flagged for verification rather than presented as settled") and this is praised. The presumption is that the caveat travels with the item. Today supplies the counterexample in the same run: a HELD flag from 07-27 and an authorship verification from 07-19 both failed to reach the 07-31 ingest, which wrote PRS-30 and PRS-31 with no authorship note. Nothing in the ingest path carries a confidence or provenance field from proposal into PRS record. A caveat written at Phase 2 and a hold written at Phase 1 have the same structural fate.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-615
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the commendation of caveat-writing set against the same run's record of two qualifiers failing to reach ingest
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Buneman, Khanna & Tan; Cheney, Chiticariu & Tan, "Provenance in Databases: Why, How, and Where" — and "A Core Calculus for Provenance" (arXiv 1310.6299). — Establishes that annotation survival through a transformation is not automatic: propagation must be DEFINED per operator (where-, why-, how-provenance each propagate differently), and an operator with no defined propagation rule silently drops the annotation. This is the exact mechanism the item names.
    2. "Fine-Grained Provenance for Matching & ETL" (PMC6783128). — Shows that provenance through matching/ETL steps requires purpose-built machinery to be retained; it does not survive ordinary transformation by default.
    3. "Capturing end-to-end provenance for machine learning pipelines," Information Systems (2024), and Open Data Fabric (arXiv 2111.06364). — End-to-end lineage requires identifiers and propagation mechanisms explicitly designed to persist across stages, "ensuring traceability survives transformations, joins, and summarizations." Supports the item's claim that the property must be built, not assumed.
    4. Convergent with PRESUMPTION-602's sources: the Wikipedia-retraction persistence study and the KG provenance-statement literature show the same asymmetry — the qualifier written upstream does not reach the derived record unless the derived schema has a field for it.

  Strength of support: Strong

  Summary: Database and data-engineering provenance research states the item's claim as its founding problem: annotations do not propagate through transformations unless propagation is explicitly specified operator by operator, and the several provenance semantics exist precisely because different notions survive differently. The ETL and ML-pipeline lineage work reports the same finding at system scale — end-to-end traceability is an engineered property requiring identifiers designed to persist across stages, and is otherwise lost at joins and summarizations. This grounds the item's structural equivalence claim: a Phase 1 HOLD and a Phase 2 confidence caveat share a fate because neither has a defined carrier into the PRS schema, and the failure is a property of the pipeline's design rather than of the diligence of whoever wrote the qualifier. It also grounds the item's implied critique of the HOLD_LIST.md remedy: a fix scoped to one qualifier type leaves the general propagation gap intact.

  Caveats: (1) The literature is about mechanised data pipelines with formal operators; C2A2's ingest is partly a prose-to-record human/agent process, so "operator" is analogical and the formal propagation calculi do not apply directly. (2) The sources establish that propagation must be designed; they do NOT establish that C2A2's ingest path lacks such a design — that is an internal observation (n=2 dropped qualifiers) that 15a cannot verify. (3) The item's settling quantity is a rate over proposals that carried a caveat at filing; the denominator is small and this is exactly the condition PRESUMPTION-604 flags. (4) Search scope: database provenance semantics, ETL/ML lineage. NOT searched: schema-evolution and W3C PROV conformance literature.

  Recommendation: SUPPORTED

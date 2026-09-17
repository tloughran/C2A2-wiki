*** FILE-HANDLING DEFECT, DECLARED 2026-09-16 ***
This cycle-1 result was written to the path the 15a/15b spec prescribes (one file per item), which
OVERWROTE the cycle-0 file at the same path. The cycle-0 search text is LOST. Its findings survive only
in lit_search_returns.md and in DISPOSITION-359 / -361 / -397. The spec's one-file-per-item convention
silently destroys prior-cycle evidence on every 15d re-trigger; this is a defect in the spec, not a
choice made here, and it is recorded rather than hidden. Recommended fix: path should carry the cycle.

SEARCH-FOR-PRESUMPTION-414:
  Date searched: 2026-09-16
  Original item: PRESUMPTION-414
  Original statement: [inferred] That some connectivity measure is the right proxy for "vault health for
    synthesis" at all — that a well-connected graph is what synthesis needs, rather than depth/quality of
    individual tradition pages, semantic coherence, or concept coverage independent of link topology.
  Cycle: 15d re-trigger 2026-07-12, cycle 1 — SEARCHED 66 days late. Prior 15a (2026-06-29):
    PARTIALLY-SUPPORTED (Weak-Moderate).

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a, 15b -> 15c -> 15d -> 15a]
    Original item: PRESUMPTION-414
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the vault audit framing health entirely in connectivity terms even while
        questioning the edge type (2026-06-28).
      15a: Re-searched for supporting literature on the 2026-07-12 re-trigger; executed 2026-09-16.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial — and STRONGER than at intake.

  Sources:
    1. Yuan et al., 2026. "GRASP: Plan-Guided Graph Retrieval with Adaptive Fusion and Reranking on
       Semi-Structured Knowledge Bases." arXiv:2605.30237. — Introduces Reachability-Weighted Accuracy
       (RWA), which adjusts retrieval accuracy by connectivity on the explicit ground that disconnected
       components cannot support multi-hop retrieval. This is a direct, quantified instance of
       connectivity being load-bearing for synthesis-like work.
    2. GRASP (same), degree analysis. — Reports that performance improves as an entity's degree
       increases, because the retriever can supply more evidential context to the reader. Connectivity is
       not merely correlated with performance here; a mechanism is given.
    3. Structural Quality Metrics literature: Semantic Web Journal / arXiv:2211.10011, "Structural Quality
       Metrics to Evaluate Knowledge Graphs." — Establishes that structural quality (relational density,
       clustering, global connectivity, local cohesion) is a recognised and separately-measurable quality
       dimension of a knowledge artefact, i.e. the FRAMING the presumption uses is standard practice, not
       an idiosyncrasy of the sewing agent.
    4. Structural Coherence Index (SCI) as reported in the same literature. — Measures structural quality
       INDEPENDENTLY of retrieval accuracy, which is evidence that the field treats the two as distinct
       constructs that must each be measured — partial support for the presumption's frame and partial
       support for its critics.

  Strength of support: Moderate (upgraded from Weak-Moderate at intake).

  Summary: The literature has moved since 2026-06-29 and now supplies something the intake search did not
    have: a mechanism and a metric linking graph connectivity to downstream multi-hop synthesis
    performance. RWA formalises the claim that unreachable material cannot be synthesised, and the
    degree-to-performance finding gives a monotone relationship over the range studied. Structural quality
    metrics for knowledge graphs are an established sub-field, so "health = connectedness" is a
    recognised construct rather than a private one. This is genuine support for the WEAK form of the
    presumption — connectivity is A valid health dimension — and it partially satisfies MONITOR-403's
    stated INCORPORATE condition ("connectivity changes track real synthesis-task performance").

  Caveats: THE DOMAIN TRANSFER IS NOT VALIDATED AND THIS IS THE WHOLE CAVEAT. Every source above concerns
    machine retrieval over a typed knowledge GRAPH with entities and relations, evaluated by automated
    multi-hop QA. The C2A2 vault is prose pages joined by wikilinks and shared references, and the
    "synthesis" at issue is a thinker-agent composing across traditions. Degree-to-performance was
    established over a range; nothing establishes it above that range, which is the region a sewing agent
    optimising connectivity would push the vault into. Note also that source 4 cuts both ways: the field
    measures structural quality separately from retrieval accuracy precisely because the two can diverge.
    Search scope: preliminary — one search pass across KG-quality and graph-RAG literature. Content-quality
    and concept-coverage predictors of human synthesis were NOT searched this cycle; a broader search is
    recommended and would be the fairer test of the presumption's rivals.

  Recommendation: PARTIALLY-SUPPORTED

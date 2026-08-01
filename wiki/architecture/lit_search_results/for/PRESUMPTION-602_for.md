SEARCH-FOR-PRESUMPTION-602:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-602
  Original statement: The Stump/Cajetan item is split into "(a) the content is defensible ... (b) the mechanism is not," presuming an ingest's content and its authorship provenance are separable, so a corrected Source: line plus a Confidence tag repairs it. But tradition assignment IS the network's unit of analysis; attributing Machado to Stump is an error at the level the system operates on, not a metadata blemish. FINDING-055's cross-program claim has a now-mislabelled endpoint.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-602
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the content/mechanism framing in the 2026-07-31 chat summary and the metadata-edit remedy offered under (a)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. van der Vet & Nijveen, 2016. "Propagation of errors in citation networks: a study involving the entire citation network of a widely cited paper published in, and later retracted from, the journal Nature." Research Integrity and Peer Review 1:3. — Measured the entire citation network of one retracted paper: direct citations are a real propagation channel for the retracted result, and the authors state that assessing propagation beyond the primary citation requires reasoning about content and is not automatable. Directly supports the item's claim that a source error reaches derived assertions and that a metadata edit is not self-propagating.
    2. Arxiv 2509.18403, 2025. "The Persistence of Retracted Papers on Wikipedia." — Retracted sources persist in derived knowledge artifacts after the retraction is recorded upstream; the correction does not travel to the places that consumed the claim. Analogous to FINDING-055 and the cross-index entry inheriting the misattribution.
    3. "Provenance-Enhanced Statements in Knowledge Graphs" (arXiv 2606.15246) and "Provenance-driven nanopublications" (Int. J. Digital Libraries, 2025). — In knowledge graphs, provenance annotations describe who asserted a statement and from what source; where the schema indexes assertions by asserter, the asserter field participates in the semantics of the statement rather than merely describing it. Supports the item's core distinction.
    4. "Hierarchical Failure Attribution for LLM-based Multi-Agent Systems" (arXiv 2602.23701). — Distinguishes the data generator (root cause) from downstream data propagators (symptoms), and reconstructs propagation along data-dependency edges. Supports treating the mislabelled ingest as a root cause whose downstream consumers must be enumerated, not as a local blemish.

  Strength of support: Strong

  Summary: The literature supports both halves of the item. On the semantic half, knowledge-graph provenance work treats the source/asserter field as part of the statement when the schema indexes by it — which is C2A2's case, since every cross-tradition operation reads "this is what the Stump tradition holds." On the propagation half, the measured retraction-network studies show that upstream corrections do not automatically reach derived artifacts: van der Vet & Nijveen tracked a full citation network and found direct citations continue to carry the retracted result, and the Wikipedia study found the same persistence in a derived knowledge base. That is precisely the mechanism by which a corrected Source: line would leave FINDING-055 and the cross-index entry untouched. The multi-agent failure-attribution work supplies the operational form of the remedy the item implies: enumerate downstream consumers along dependency edges rather than patch at the point of error.

  Caveats: (1) The retraction studies concern factual retraction (the claim is withdrawn), whereas here the content is stipulated defensible and only the attribution is wrong — the transfer is to the propagation mechanism, not to the severity. (2) van der Vet & Nijveen is n=1 citation network; the generality of the propagation rate is not established by it. (3) The knowledge-graph sources establish that provenance CAN be semantic under an indexing schema, not that it always is; the claim is conditional on C2A2's schema, which is an internal fact 15a cannot verify from literature. (4) Search scope: citation/retraction propagation, KG provenance semantics, multi-agent failure attribution. NOT searched: library-science authority-control literature, which likely bears directly.

  Recommendation: SUPPORTED

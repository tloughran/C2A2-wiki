SEARCH-FOR-ASSUMPTION-1211 (OWED LIMB ONLY: source-level read of arXiv:2604.18880; orphan re-verification):
  Date searched: 2026-10-08
  Original item: ASSUMPTION-1211
  Original statement: "The trap is durable because the writer assembles a plausible gloss from two real
    neighbouring fields." Under monitoring (MONITOR-554): exclusivity and the causal specific, i.e.
    structural ADJACENCY vs token-space SIMILARITY vs forward PROPAGATION.
  Limbs searched: the owed limb only. That is a read of arXiv:2604.18880 beyond snippet level, to decide
    whether its field-level finding survives reading. Also: re-verification of the untagged orphan
    cycle-1 file ASSUMPTION-1211_for_cycle1.md (dated 2026-09-17, never registered in the queue), which
    reports having done that read.
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-13, MONITOR-554; processed 2026-10-08)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: ASSUMPTION-1211
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa QC sweep, Day 130; first causal account for the label-trap series
      15a (cycle 0, 2026-08-26): SUPPORTED, Moderate-to-Strong; all snippet-only; arXiv:2604.18880 fetch BLOCKED
      15b (cycle 0): WEAKLY-CHALLENGED, Moderate; token-space similarity and citation-copying propagation
        as rival accounts; exclusivity challenged
      15c: MONITOR-554 (HIGH); INCORPORATE trigger includes 2604.18880 "fetched in full and its field-level
        finding survives reading"
      15d: re-triggered cycle 1 2026-09-13; did not evaluate evidence
      15a (cycle 1, ORPHAN, 2026-09-17): file ASSUMPTION-1211_for_cycle1.md, never registered. Reports a
        full-HTML read of 2604.18880 and finds the field-level finding survives but the paper cannot
        discriminate adjacency from similarity (no input record; parametric-memory regime). Corrects a
        cycle-0 CiteCheck misquotation. Adds Dai et al. 2024 (binding/ordering subspace) as independent
        support for adjacency. Status SUPPORTED / PARTIALLY-SUPPORTED / NO-SUPPORT-FOUND by sub-claim
      15a (cycle 1, this file, 2026-10-08): 1 search, 2 fetch attempts (1 returned content); re-verified
        the orphan's claims about 2604.18880 against the source abstract. The orphan file was not modified.
    Current status: SUPPORTED (general field-level mechanism); PARTIALLY-SUPPORTED (adjacency as an
      operative route, carried from the orphan, not re-checked); NO-SUPPORT-FOUND (exclusivity)

  Search scope: 1 web search (paper title + arXiv id). Fetch attempts: (1) arxiv.org/pdf/2604.18880.
    The tool returned "Already fetched ... 72s ago in this session. Re-use the content", but NO content
    had been delivered to this agent, so this is recorded as effectively refused. (2)
    papers.cool/arxiv/2604.18880 succeeded: full abstract plus citation metadata (authors, date, PDF
    URL). FULL TEXT WAS NOT OBTAINED THIS PASS. The orphan's quantitative full-text details could not be
    independently re-verified.

  RE-VERIFICATION OF THE ORPHAN (ASSUMPTION-1211_for_cycle1.md) against the fetched abstract:
    Confirmed at source (abstract/metadata):
      - Authors Yuefei Chen, Yihao Quan, Xiaodong Lin, Ruixiang Tang; posted 2026-04-20; cs.CL. [fetched]
        Rutgers affiliation: [search-result].
      - 9 models, 108,000 generated references. [fetched]
      - "author names fail far more often than other fields across all models and settings". [fetched]
      - "Citation style has no measurable effect"; "reasoning-oriented distillation degrades recall". [fetched]
      - "Probes trained on one field transfer at near-chance levels to the others", i.e.
        hallucination signals are field-specific. [fetched]
      - Elastic-net + stability selection on neuron-level CETT values of Qwen2.5-32B-Instruct identifies
        sparse field-specific hallucination neurons (FH-neurons). Amplifying them increases hallucination,
        and suppressing them "improves performance across fields, with larger gains in some fields".
        [fetched] This is consistent with the orphan's "partial positive spillover to non-targeted fields".
      - The abstract makes no claim that hallucinated references are built by taking a real reference and
        editing fields. This corroborates the orphan's correction of the cycle-0 paraphrase.
      - The abstract mentions no input record, layout, ordering, or neighbouring-record analysis. This is
        consistent with the orphan's finding that the paper cannot discriminate adjacency from similarity.
    Not re-verifiable this pass (full text not obtained): the field ordering "author < venue < title ≈
      year"; author correct-rate <14% at N=15; Kruskal–Wallis p-values; OpenAlex verification and 93%
      expert agreement; the output-position effect; probe AUC ranges (0.81–0.92 within, 0.46–0.59 across);
      FH-neuron counts per field; the explicit parametric-memory-only generation regime. These remain the
      orphan's [fetched, full text] claims, now with ONE independent confirmation at abstract level.
    Verdict on the orphan: ITS READING SURVIVES. Every claim checkable against the abstract is confirmed,
      and nothing in the abstract contradicts any orphan claim. The orphan's key conclusion stands: the
      field-level finding survives reading, but the paper is silent on adjacency vs similarity, so
      MONITOR-554 should stop relying on it for that question. The orphan's other sources (Dai et al. 2024;
      arXiv:2609.17538; Tan & D'Souza 2026; Bienz et al. 2026; CiteCheck correction) were NOT re-checked
      here.

  Supporting evidence found: Yes (general mechanism); Partial (adjacency); No (exclusivity)

  Sources:
    1. Chen, Y., Quan, Y., Lin, X. & Tang, R., 2026. "Where Fake Citations Are Made: Tracing Field-Level
       Hallucination to Specific Neurons in LLMs." arXiv:2604.18880. [fetched, abstract via papers.cool]
       Field-level, field-specific, generator-internal failure with causal neuron-level evidence. Supports
       14a's reframing of a defect log as a hypothesis about the generator. No evidence on adjacency.
    2. ASSUMPTION-1211_for_cycle1.md (orphan 15a file, 2026-09-17). [internal; read in full] Cited for its
       full-text reading of source 1 and for its adjacency sources, which were not re-verified here.

  Strength of support: Strong for the general field-level mechanism (now at source, confirmed in two
    passes). Moderate for adjacency as one operative route (orphan only). None for exclusivity.

  Summary: The owed work, a source-level read of arXiv:2604.18880, has now been done twice. The
    unregistered 2026-09-17 orphan read it in full. This pass confirmed every abstract-checkable claim in
    that reading and found no contradiction. The field-level finding survives reading: failures are
    field-specific, strongest on author names, style-invariant, encoded in non-transferring
    field-specific subspaces, and causally tied to sparse neurons. The paper does not address where a
    wrong value comes from, so it cannot arbitrate adjacency vs similarity vs propagation. MONITOR-554's
    deciding question stays with the three-account discriminator (empirical), not with this source.

  Caveats: (i) Full text was not obtained this pass. The fetch tool deduplicated a PDF fetch that never
    delivered content, so the orphan's quantitative claims rest on a single read. (ii) The orphan was
    never registered and records an unusual fetch sequence (a URL admitted to the provenance set via a
    later search). The orchestrator should decide whether to register it. This file cites it but does not
    adopt its unverified sources. (iii) The regime mismatch (parametric recall vs the in-context read in
    the Rohr case) stands, per the orphan.

  Recommendation: SUPPORTED (general mechanism); PARTIALLY-SUPPORTED (adjacency operative, not exclusive);
    NO-SUPPORT-FOUND (exclusivity). The MONITOR-554 INCORPORATE trigger clause "2604.18880 fetched in
    full and its field-level finding survives reading" is MET by the orphan and corroborated at abstract
    level here.

  NOVELTY-FLAG: Partial, carried from cycle 0 and the orphan: a splice between two fields of the SAME
    internal record in a self-authored knowledge base remains undescribed in the literature reached.

  Independence attestation: Read: 15a definition; provenance_protocol.md; for/PRESUMPTION-897_retrigger-
    2026-10-07_for.md; for/ASSUMPTION-1211_for.md; for/ASSUMPTION-1211_for_cycle1.md (orphan; not modified);
    for_lit_search.md owed-limb note; MONITOR-554. NOT read: any against/ file dated 2026-10-08.

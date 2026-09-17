SEARCH-FOR-ASSUMPTION-1211 — CYCLE 1 (15d re-trigger). The cycle-0 file ASSUMPTION-1211_for.md (2026-08-26)
is preserved untouched; this file supersedes nothing and adds the owed source-level read plus a fresh search.

SEARCH-FOR-ASSUMPTION-1211:
  Date searched: 2026-09-17
  Original item: ASSUMPTION-1211
  Original statement: "The trap is durable because the writer assembles a plausible gloss from two real
    neighbouring fields." Under monitoring (MONITOR-554): whether structural ADJACENCY is the operative
    mechanism, as against token-space SIMILARITY or forward PROPAGATION.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15a]
    Original item: ASSUMPTION-1211
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Summa QC sweep, Day 130 — first causal account for the label-trap series.
      15a (cycle 0): Searched for supporting literature; SUPPORTED, Moderate-to-Strong; all snippet-only;
        arXiv:2604.18880 fetch-blocked.
      15b (cycle 0): Weakly challenged exclusivity — token-space similarity and propagation as rival accounts.
      15c: MONITOR-554, HIGH; INCORPORATE trigger includes "arXiv:2604.18880 fetched in full and its
        field-level finding survives reading."
      15d: Re-triggered 2026-09-13 as cycle 1; did not evaluate evidence.
      15a (cycle 1): Read arXiv:2604.18880 at source (abstract page + full HTML text); re-read CiteCheck at
        source; fresh-budget search for work since 2026-08-26 and for adjacency-vs-similarity mechanisms.
    Current status: SUPPORTED (general mechanism, unchanged); PARTIALLY-SUPPORTED (adjacency as an
      operative mechanism — now has independent mechanistic support); NO-SUPPORT-FOUND (exclusivity)

  Search scope: web_fetch of arXiv:2604.18880 (abs page succeeded; /html and /pdf first refused as not in
    provenance set; after a WebSearch placed the URLs in the provenance set, one fetch of /html/2604.18880
    succeeded via the tool's documented route — sequence recorded here for the orchestrator's judgement).
    WebSearch queries: paper title; LLM entity–attribute binding errors; document key–value extraction
    "adjacent/neighboring field" confusion; contextual hallucination / copying from wrong span; citation
    hallucination mechanism Sept 2026. Confidence: **comprehensive on the owed source; moderate on the fresh
    search** — the KIE benchmark's qualitative-error section was truncated in the fetched text and the
    meta-analysis paper was read at abstract level only.

  THE OWED WORK — arXiv:2604.18880 read at source. Chen, Y., Quan, Y., Lin, X., Tang, R. (Rutgers), 20 Apr
    2026, "Where Fake Citations Are Made: Tracing Field-Level Hallucination to Specific Neurons in LLMs."
    What it says about WHICH fields: 9 models, 108,000 references generated from parametric memory alone,
      verified field-by-field against OpenAlex (+ web-search second stage; 93% agreement with 200 expert-
      labelled items). Ordering of field difficulty "author < venue < title ≈ year holds across every model
      and generation volume"; author correct-rate below 14% at N=15 for all models; DOI model-dependent.
      Citation style has no effect (Kruskal–Wallis, all p>0.05): failure "is governed by the nature of the
      bibliographic field rather than the formatting conventions." A positional effect in the OUTPUT
      sequence: accuracy highest for the first two citations of a prompt, degrading sharply from position 3
      ("models exhaust their most reliable parametric memory early").
    What it says about MECHANISM: linear probes on field-span hidden states decode hallucination within a
      field (AUC 0.81–0.92) but transfer across fields at near chance (0.46–0.59): "each field's
      hallucination is encoded in a structurally distinct subspace." Sparse field-specific hallucination
      neurons (FH-neurons: 224 Title, 78 Authors, 129 Year, 51 Venue, 30 DOI) with causal effect under
      activation scaling; moderate suppression gives "partial positive spillover to non-targeted fields,
      suggesting that bibliographic fields share some but not all of their underlying neural substrates."
    Does it discriminate ADJACENCY from SIMILARITY? **No — it was not designed to and does not try.** It
      labels each field correct/incorrect; it never traces a wrong author list to a neighbouring real record,
      never measures token-similarity between the wrong value and any candidate source, and never studies
      layout or record order in an input, because there is no input record — generation is from parametric
      memory. The cycle-0 gloss ("constructed by taking a real reference and modifying one or more metadata
      fields") is a paraphrase of the introduction's "references that look correct at first glance but
      contain errors in one or more bibliographic fields"; the paper makes no claim about a real-reference-
      plus-edit generative process. **Scope mismatch, stated:** the Rohr splice is an in-context read of a
      record; this paper is about no-context recall. It therefore cannot adjudicate MONITOR-554's question.
    Does the field-level finding survive reading? **Yes**: field-level decomposition of the failure is real,
      robust across 9 models, and localised in the generator — 14a's reframing of a defect log as a
      hypothesis about the generator is corroborated at source. What does NOT survive is any reading of
      this paper as evidence for adjacency specifically.

  Supporting evidence found: Yes (general mechanism); Partial (adjacency); No (exclusivity).

  Sources (fresh, cycle 1; retrieval level per source):
    1. Chen et al. 2026, arXiv:2604.18880 — as above. [FULL TEXT at source]
    2. Dai, Q., Heinzerling, B., Inui, K. 2024. "Representational Analysis of Binding in Language Models."
       arXiv:2409.05448v3. [ABSTRACT + introduction at source] Extends Feng & Steinhardt's Binding-ID account:
       a low-rank subspace in LM activations "primarily encodes the order (i.e., OI) of entity and attribute,"
       and editing along the ordering direction causally rebinds an entity to a different attribute ("Box Z
       contains the stone"). **This is the most direct mechanistic support located for structural adjacency
       as an operative binding mechanism, independent of token similarity**: position in the context, not
       lexical overlap, is what the intervention manipulates. Caveat: toy contexts, not records; in-context
       binding, which is the right regime for the Rohr case but not for source 1.
    3. arXiv:2609.17538 (Sept 2026 — new since cycle 0). "From Pixels to Pairs: A Comprehensive Benchmark of
       LLM-Based Key–Value Extraction in Noisy Document Settings." [PARTIAL FULL TEXT at source; §5.11
       qualitative errors truncated] Dominant failure is "key–value misalignment" — values attached to the
       wrong key. Two drivers named, not separated: (i) positional — "fields that rely on positional cues
       rather than explicit lexical markers" fail when layout is flattened (FUNSD); (ii) similarity — "dense
       numeric regions and repeated values increase the risk of key–value misalignment" (CORD); "errors still
       arise from assigning values to the wrong receipt fields, especially in the presence of repeated numeric
       content." Both accounts are live in the same benchmark.
    4. Tan, Z. & D'Souza, J. 2026. "Diagnosing Structural Failures in LLM-Based Evidence Extraction for
       Meta-Analysis." arXiv:2602.10881. [ABSTRACT at source] Failures "stem not from entity recognition
       errors, but from systematic structural breakdowns, including role reversals, cross-analysis binding
       drift, instance compression in dense result sections, and numeric misattribution"; long-context input
       "further exacerbate[s]" them. Binding drift between adjacent analyses in dense sections is the
       structured-record analogue of the splice; adjacency vs similarity not separated.
    5. Bienz, A., Pearson, C., Garcia de Gonzalo, S. 2026. "The Case of the Mysterious Citations." arXiv:
       2602.05867 (Sandia/UNM). [FULL TEXT at source] Wild-type evidence from four HPC conference
       proceedings, 2021 vs 2025: error classes "Rephrased Title" (a gloss that "retains the meaning of the
       true title") and "Mysterious Citation" — "the cited location either does not exist or holds an
       unrelated paper with different authors," i.e. a real location spliced to wrong content. Fully
       fabricated citations could not be elicited from the newest model, "while citations generated by
       ChatGPT 5 consistently include extra words, incorrect authors, and invalid DOIs" — the field-level
       corruption mode is the residual, durable one.
    6. CiteCheck, arXiv:2605.27700. [FULL TEXT at source — CORRECTION to cycle 0] The sentence attributed to
       it at cycle 0 ("real-sounding surnames from the target field are recombined into author lists") does
       not occur in the paper. Its "minor hallucination" class is synthetically generated by GPT-4o-mini
       (§4.2), so it documents no generation mechanism. What it does observe (§3.3): hallucinated citations
       "may preserve the correct title while corrupting the year, URL, DOI ... or pair a real identifier with
       unrelated surrounding metadata." Supports the general shape only.
    7. Snippet-level only: "Diagnosing Dense Same-Class Attribute Misbinding in Large Vision-Language Models"
       (arXiv:2608.16805, Aug 2026 — attribute assigned to the wrong same-class instance in crowded scenes);
       "contextual entrainment" / context-hijacking (prompt tokens act as retrieval cues). Not read at source.

  Strength of support: **Strong** for the general mechanism (field-level, generator-internal, durable
    because partial). **Moderate** for adjacency as an operative mechanism (source 2 gives it independent
    causal standing; sources 3–4 show it co-occurring with similarity). **None** for exclusivity.

  Summary: The owed source confirms field-level failure and localises it in the generator, but it is silent
    on where wrong values come from and cannot separate adjacency from similarity; MONITOR-554's reliance on
    it for that question should be dropped. The fresh search changes the picture in one respect: binding
    research now supplies a positional mechanism with causal evidence — an ordering subspace whose
    manipulation rebinds an entity to its neighbour's attribute (2) — so structural adjacency is no longer
    merely "not contradicted" but has a mechanism of its own, distinct from token overlap. The document-
    extraction literature (3, 4) shows both routes operating in dense structured records, which is what a
    wiki record is. A field-corpus audit (5) shows real-location/wrong-content splices surviving peer review
    and persisting as fully fabricated citations recede. Nothing found supports adjacency as the ONLY route;
    the three-account discriminator named in MONITOR-554 remains the deciding test.

  Caveats: Source 2 is a toy-context study; its transfer to multi-field records is by analogy. Source 3's
    error-analysis section was not retrievable. Source 1's regime (no input) differs from the Rohr regime
    (input record read by the writer), which is the single largest limit on using it for this item. The
    cycle-0 CiteCheck quotation must be treated as unsourced; MONITOR-554's summary line repeating it
    ("models 'recombine' genuine surnames/titles/venues") should be corrected by whoever owns that entry.

  Recommendation: **SUPPORTED** (general mechanism) / **PARTIALLY-SUPPORTED** (adjacency operative, not
    exclusive) / **NO-SUPPORT-FOUND** (exclusivity). Cycle-0 recommendation SUPPORTED stands on better evidence.

  PARTIAL NOVELTY-FLAG (carried from cycle 0, narrowed): the specific variant — a splice between two fields of
    the SAME record in a self-authored knowledge base — remains undescribed; the KIE literature (3) is the
    nearest and is about external documents. The field-adjacency detector proposed at cycle 0 is now also
    motivated by source 2: if ordering drives binding, disambiguating adjacent records by id is the direct fix.

  Independence attestation: Read — agents/15a_lit_search_for_agent.md; architecture/provenance_protocol.md;
    lit_search_results/for/ASSUMPTION-1211_for.md (cycle 0); monitor_queue.md lines 21474–21545 (MONITOR-554
    only). NOT read — any against/ file dated 2026-09-17, lit_search_returns.md, revision_flags.md,
    validated_premises.md, any other monitor_queue.md entry.

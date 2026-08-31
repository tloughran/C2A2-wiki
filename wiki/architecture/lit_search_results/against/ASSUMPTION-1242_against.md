SEARCH-AGAINST-ASSUMPTION-1242:
  Date searched: 2026-08-31
  Original item: ASSUMPTION-1242
  Original statement: Three co-arising independently generated proposals should become "one paradigm
    flag rather than three."
  Generalizable limb searched: Does collapsing convergent independent reports to a single item
    destroy evidence that should instead be pooled and weighted up? And is the independence
    precondition for that objection actually satisfied by agents sharing a base model?

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: Good on the second limb, Moderate on the first. 3 queries (budget cap reached).
    Query 1 ("deduplicating independent replications destroys evidence") returned almost entirely
    off-target results — storage deduplication and systematic-review citation deduplication — and
    should be treated as a wasted query; the on-target philosophy-of-science material came from
    query 2. The correlated-errors evidence in query 3 is recent arXiv work read at
    abstract/snippet level only, not peer-reviewed as far as could be confirmed.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-1242
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Proposed consolidating three co-arising proposals into a single paradigm flag on the
           grounds that they express one underlying concern.
      15b: Searched for challenging literature (2026-08-31)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Stegenga, J. & Menon, T. 2017. "Robustness and Independent Evidence." *Philosophy of Science*
       84(3). (journals.uchicago.edu/doi/10.1086/692141; also Cambridge repository preprint.)
       — Cuts both ways, and is the pivotal source. It establishes that robustness arguments confirm
       a hypothesis only when the converging lines of evidence are genuinely *independent* in the
       relevant probabilistic sense — mere multiplicity does not confer evidential weight. So it
       challenges 1242 conditionally: if the three proposals really were independently generated,
       collapsing them to one discards a robustness argument that the pipeline is entitled to. But it
       equally undercuts the naive pooling objection: independence has to be demonstrated, not
       assumed from the fact that three generation events occurred.
    2. Consilience / concordance of evidence tradition (Whewell's consilience of inductions; Perrin's
       thirteen-procedure argument for Avogadro's number, as discussed in the convergence literature).
       Also "Convergence strategies for theory assessment," *Studies in History and Philosophy of
       Science* (ScienceDirect, S0039368124000190); and "Evidential Diversity and the Triangulation
       of Phenomena." (All snippet-level.)
       — Supports the pooling objection: multiple independent sources agreeing can yield a strong
       conclusion even where each source alone is weak. Collapsing three concordant reports to one
       report deletes exactly the structure that generates this surplus.
    3. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation Panels."
       arXiv:2605.29800 (2026); authors not captured from snippet.
       — Strongly *supports* 1242 and therefore weakens my challenge. A panel of nine frontier LLMs
       drawn from seven model families was found to carry only about two independent votes' worth of
       information; roughly three-quarters of nominal independence is lost because the models err on
       the same items. The reported bottleneck is correlated judges rather than the aggregation
       method, so scaling the panel does not recover independence.
    4. "Correlated Errors in Large Language Models." arXiv:2506.07962 (2025); also
       "The Oracle's Fingerprint: Correlated AI Forecasting Errors and the Limits of Bias
       Transmission," arXiv:2605.00844.
       — Same direction: major LLMs from different providers exhibit highly correlated errors despite
       independent development, and correlation *increases* with model capability. Agents inside one
       pipeline, on one base model, with shared context are a far more severe case than the
       cross-provider setting these papers measure.
    5. Reichenbach's Common Cause Principle (Stanford Encyclopedia of Philosophy,
       plato.stanford.edu/entries/physics-Rpcc/); and the algorithmic-monoculture literature
       (e.g. "Strategic Algorithmic Monoculture," arXiv:2604.09502).
       — Provides the mechanism: correlation between reports is explained by a common cause (shared
       weights, shared prompt, shared retrieved context), and screening off on that common cause
       removes the apparent evidential surplus.

  Strength of challenge: Moderate

  Summary: The challenge to 1242 is real but conditional, and the condition is probably not met. The
  corroboration literature does say that collapsing concordant independent reports destroys evidence
  — this is the consilience/robustness surplus, and 14a's recommendation would discard it. But
  Stegenga and Menon's central point is that the surplus is earned by independence, not by count, and
  the recent correlated-errors work is close to dispositive that agents sharing a base model do not
  have it: nine frontier judges from seven families carried about two votes of independent
  information. Three proposals co-arising inside one pipeline, on one model, from overlapping
  context, are the paradigm case of Reichenbachian common-cause correlation rather than independent
  corroboration. So 1242's *conclusion* is defensible; what is not defensible is reaching it without
  an independence assessment. The residual challenge is procedural and it is the one that matters:
  collapsing three to one silently records a judgement about independence that the pipeline has never
  made, tested, or written down, and that judgement is exactly as likely to be wrong in the other
  direction on some future triple where the proposals really did arise from different evidence.

  Specific risks: If the claim is false — i.e. if the three proposals were substantively independent
  — collapsing them deletes a robustness argument and downweights a signal that three separate routes
  reached the same place. Worse, the deletion is irreversible in the record: once one flag exists,
  the fact that three routes converged is no longer recoverable, so the error cannot be detected
  later. If the claim is true but adopted for the wrong reason (co-arising treated as automatic
  redundancy), the pipeline installs a general rule that will suppress genuine convergence whenever
  it occurs, systematically biasing against the strongest evidence the pipeline can produce.

  Mitigations available: Collapse the *flag* while preserving the *count* — record "one paradigm
  flag, corroborated by three independently generated proposals," with the three retained as
  provenance rather than deleted. Add an explicit independence check before collapse: did the three
  proposals draw on the same source documents, the same retrieved context, the same prompt framing?
  Where the answer is yes, collapse without weight increase; where no, collapse with weight increase
  and record the reason. Follow the LLM-panel finding by not treating agent count as evidence
  strength at any point in the pipeline.

  STEELMAN:
    Strongest counterargument: The consilience surplus requires that the converging lines could have
    disagreed. Three proposals generated in one pass, from one model, over one corpus, essentially
    could not have disagreed — their agreement is a property of the generator, not of the world.
    Treating that agreement as corroboration is the algorithmic-monoculture error in miniature: it
    reads a shared prior as three confirmations. On this reading 1242 is not merely acceptable but
    *corrective*, and the burden falls entirely on anyone wanting to keep three flags to show what
    varied between the three generation events.
    What would need to be true for C2A2 to be safe: that the pipeline can state, for any set of
    co-arising proposals, what varied across their generation — and that it collapses only when
    nothing did. The unsafe state is not "collapses" or "keeps"; it is "does either without knowing."
    How to test: Run a manipulation check. Regenerate the same intake N times under deliberately
    varied conditions (different retrieved context, different framing, different ordering) and
    measure how often the same triple co-arises. If co-arising is invariant to the manipulation, the
    proposals are driven by the generator and collapse is correct. If it varies, they carry
    independent information and collapse destroys it. This is directly analogous to the effective-
    votes measurement in arXiv:2605.29800 and is the single highest-value diagnostic available to
    the pipeline, since it also settles PRESUMPTION-900.

  Recommendation: PARTIALLY-CHALLENGED

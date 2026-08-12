SEARCH-FOR-PRESUMPTION-727:
  Date searched: 2026-08-10
  Original item: PRESUMPTION-727
  Original statement: That the defect register describes a static corpus; a correctly-unanchored claim became anchorable because PRS-52 was added 2026-07-21, and 128 days now predate a tradition file they cite — no register entry carries the corpus state it was judged against, so verdicts cannot be replayed and clean passes have no expiry.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-727
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b paired a QC finding with the nightly verification's independent measurement of the same effect
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Carruthers, J.A., Diaz-Pace, J.A., Irrazábal, E., 2024. "A longitudinal study on the temporal validity of software samples." Information and Software Technology (ScienceDirect). — Finds significant temporal validity loss in a widely-used software corpus (Qualitas Corpus) after ten years without update, and recommends "maintenance strategies to detect data drift signs in the population and update the sample accordingly" — directly analogous to a defect register whose reference corpus goes stale.
    2. [unverified — from search snippet] "Temporal validity of software datasets for code metrics: an empirical assessment of sampling strategies," Research Square, 2024/2025. — Empirical assessment of how sample-based software metrics lose representativeness over time; supports the general mechanism (verdicts computed against a corpus snapshot degrade as the corpus evolves).
    3. Machine Learning in Production (CMU course text), "Versioning, Provenance, and Reproducibility" — states reproducibility requires storing "the exact versions of the data used in specific experiments" so that results can be reproduced later; without this, "you cannot reproduce ... three months ago, making ... debugging impossible" — directly supports the presumption that unversioned corpus state breaks replayability.
    4. Akbik et al. (cited via search), "Do CoNLL-2003 Named Entity Taggers Still Work Well in 2023?" arXiv:2212.09747 — Empirical precedent for the general phenomenon that benchmark/reference corpora drift out of sync with what they were originally validated against, degrading apparent performance/accuracy of judgments made against the older snapshot.

  Strength of support: Moderate

  Summary: The literature on temporal validity of software corpora and on ML/data versioning both support the underlying mechanism the presumption describes: judgments (audit verdicts, model evaluations, metric baselines) computed against a corpus snapshot silently lose validity as the corpus evolves, and without recording the exact corpus state used, results cannot be replayed or audited later. The data-versioning/MLOps literature explicitly treats "record the corpus version alongside the verdict" as a baseline reproducibility requirement, implying its absence is a recognized anti-pattern rather than a benign simplification.

  Caveats: The supporting sources are drawn from software-corpus benchmarking and ML reproducibility research, not from audit/QC-register design specifically — the transfer to a "defect register verdict" is analogous rather than direct. None of the sources discuss "clean pass expiry" as a named concept; that framing is not independently attested in what was found. Search was preliminary (12 total queries across 4 items); a deeper search of software-audit/compliance-log literature specifically is recommended.

  Recommendation: PARTIALLY-SUPPORTED

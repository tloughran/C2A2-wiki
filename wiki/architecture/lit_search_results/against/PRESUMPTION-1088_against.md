SEARCH-AGAINST-PRESUMPTION-1088:
  Date searched: 2026-09-29
  Original item: PRESUMPTION-1088
  Original statement: Surface-structural checks are a valid proxy for semantic review of interpretive prose.
  Independence: searched without reading the 15a result file for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1088
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from QC runs marking pass on mechanical checks.
      15b: Searched for challenging literature (scheduled run 2026-09-29; sources marked 'search-result level' were not read in full)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Strength: Moderate

  Sources:
    1. Authors not verified. 'The Illusion of a Perfect Metric: Why Evaluating AI's Words Is Harder Than It Looks.' arXiv:2508.13816 — automatic metrics correlate poorly with human judgement on nuanced text (SERP-level; not read in full).
    2. ProxyQA, arXiv:2401.15042 — argues surface/overlap metrics are unreliable for long-form quality and proposes semantic proxy evaluation instead (SERP-level).
    3. In-house corroboration: validated_premises.md ~lines 3709-3712 (a proxy correlated imperfectly with its goal fails when decoupled).

  STEELMAN: structural checks are cheap, deterministic and catch a real class of failures, and for formulaic text they may track quality well. The claim fails specifically for interpretive prose, where meaning can change without any structural feature changing — exactly the domain the presumption names.

  SYSTEMIC-RISK: see run note in for_lit_search.md (2026-09-29).

---
SUPPLEMENT — second 15b pass, same date (concurrent-writer collision; appended, nothing above
removed). This pass did NOT read lit_search_results/for/. It independently agrees: CHALLENGED,
Moderate. It adds fetched primary sources.

SEARCH-AGAINST-PRESUMPTION-1088 (supplement):
  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-1088
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from QC runs marking pass on mechanical checks.
      15b: Searched for challenging literature (lane: proxy-measure validity; automated vs human content QA)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Ramprasad, S., & Wallace, B. C. (2024). "Do Automatic Factuality Metrics Measure Factuality? A
       Critical Evaluation." arXiv:2411.16638. [Fetched: abstract/intro.] A supervised model using
       only shallow surface features of summaries is "reasonably competitive" with state-of-the-art
       factuality metrics. Few metrics respond to actual factual corrections, some are more
       sensitive to benign non-factual edits, and most can be gamed by appending innocuous
       sentences. Even purpose-built semantic checks partly track surface form. Purely structural
       checks are a step further removed.
    2. Fabbri, A. R., Kryściński, W., et al. (2021). "SummEval: Re-evaluating Summarization
       Evaluation." TACL; arXiv:2007.12626. [Not fetched; seen in search results.] Kryściński et
       al. (2020), cited in the same literature (not fetched): ROUGE/BLEU/METEOR-style surface
       metrics correlate poorly with human judgements of factual consistency. On the FRANK
       benchmark (per search extract) the best metric reached only about 0.3 Spearman with human
       judgement.
    3. Manheim, D., & Garrabrant, S. (2018). "Categorizing Variants of Goodhart's Law."
       arXiv:1803.04585. [Not fetched; confirmed via search results.] A proxy that correlates with
       a goal under normal conditions decouples when it is optimized or when the system moves out
       of the regime where the correlation held (regressional, extremal, causal and adversarial
       Goodhart). QC agents that know which checks decide PASS will produce text that passes those
       checks.

  Strength of challenge: Moderate (strong in direction; no study tests structural QC of
    interpretive prose specifically)

  Summary: The NLP-evaluation literature consistently finds that surface-level measures are weak
  proxies for semantic quality, and that even semantic metrics partly reduce to surface
  features. Surface metrics also do not move when the actual meaning is corrected. Interpretive
  prose is the hardest case, because its quality lies in claims and attributions that no structural
  feature encodes. Goodhart dynamics mean the proxy gets weaker once it becomes the gate.

  Specific risks: PASS labels on interpretive tradition texts certify formatting, links and section
    presence while misattributions, inverted claims or unsupported syntheses pass through. Because
    these labels feed later deference (see PRESUMPTION-1089), the errors propagate.

  Mitigations available: Label structural passes as such ("STRUCT-PASS", not "PASS"). Add sampled
    semantic review: claim-to-source checks on a random subset. Use seeded-error audits (plant
    known semantic errors and measure the detection rate of the QC regime).

  Search scope: Preliminary: 2 searches, 1 fetch.
  Excluded results: eugeneyan.com (practitioner blog); arXiv:2609.15561 and 2409.19507 (surfaced; not
    fetched; not cited).

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1088
  Strongest counterargument: If purpose-built factuality metrics can be matched by a model that sees
    only surface features, and gamed by appending harmless sentences, then plain structural checks
    cannot certify the meaning of interpretive prose. They measure a correlate of care, not
    correctness. Once that correlate becomes the pass gate, Goodhart predicts it will decouple
    from correctness.
  What would need to be true for C2A2 to be safe: Structural passes are labelled as such and never
    read as semantic approval, and a seeded-error audit shows the combined QC regime catches most
    planted semantic errors.
  How to test: Plant N semantic errors (misattributed quote, inverted claim, wrong tradition) in
    copies of passed texts and run the structural QC. The detection rate is the proxy's validity
    for this domain. The expectation is near zero.

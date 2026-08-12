# ASSUMPTION-892 CHALLENGE REPORT

## SEARCH-AGAINST-ASSUMPTION-892

**Date searched:** 2026-08-10

**Original item:** ASSUMPTION-892

**Original statement:** "Trigram coverage looks like a better discriminator than word-count ratio for telling condensed-but-faithful from summary-form" — proposed with no threshold.

### PROVENANCE

- **Origin:** 14a
- **Chain:** [14a → 15b]
- **Original item:** ASSUMPTION-892
- **Item type:** ASSUMPTION (stated)
- **Transform at each step:**
  - 14a: Quoted verbatim; the missing threshold noted as a gap. [stated]
  - 15b: Searched for challenging literature on n-gram overlap metrics for faithfulness/discrimination.
- **Current status:** CHALLENGED

### Challenging evidence found: Yes

### Sources

1. **Multiple surveys on ROUGE limitations, e.g. "Repairing the Cracked Foundation: A Survey of Obstacles in Evaluation Practices for Generated Text" (arXiv:2202.06935) and "The Illusion of Progress: Re-evaluating Hallucination Detection in LLMs" (arXiv:2508.08285).** — ROUGE/n-gram overlap has three well-documented failure modes: sensitivity to length, inability to capture semantic equivalence, and overreliance on exact lexical match, producing both false negatives (faithful text scored low because it paraphrases) and false positives (unfaithful text scored high because it copies surface n-grams). Directly relevant: "a faithful summary can share zero n-grams with the reference and a hallucinated one can share most of them when modern abstractive models paraphrase the source."
2. **Survey summary on factual-consistency metrics (e.g. discussions citing Kryscinski et al. and related NLI/QA-based factuality work).** — N-gram overlap metrics (ROUGE, BLEU, METEOR) "perform poorly on measuring factual consistency" and correlate poorly with human judgments of faithfulness specifically because they operate at the token/surface level, not the semantic or entailment level. This is a direct rebuttal to using trigram coverage as a faithfulness discriminator rather than as a mere similarity measure.
3. **Narayan et al.-style abstractiveness/coverage-density literature and SummEval (arXiv:2007.12626).** — Established metrics for the extractive-vs-abstractive axis are "coverage" (percent of summary words drawn from source) and "density" (average length of copied spans) — not raw trigram counts. These works also show ROUGE score variance of up to ~40 points depending on which human reference is used, meaning no single fixed n-gram threshold is stable across even a single dataset, let alone across the varied prose genres in the wiki.

### Strength of challenge: Strong

### Summary

The literature is fairly unified: n-gram/trigram overlap metrics are known to be poor proxies for faithfulness because they measure lexical surface similarity, not semantic or factual correspondence — a paraphrased-but-faithful passage can score near zero, and a fluent hallucination that copies phrasing can score high. Established practice already has better-suited metrics for exactly the extractive-vs-abstractive discrimination task the assumption targets (coverage, density, novel-n-gram percentage) rather than raw trigram counts, and even those have shown ROUGE-type score instability of up to 40 points depending on reference choice. The assumption's own acknowledged gap — "proposed with no threshold" — is not a minor omission; the literature suggests no single trigram threshold would generalize, because optimal cutoffs are corpus- and reference-dependent.

### Specific risks for C2A2

If trigram coverage is adopted as the discriminator, C2A2 risks two symmetric failures: (1) flagging faithful-but-heavily-paraphrased condensations as "summary-form" (false positive on drift) because faithful rewording naturally lowers n-gram overlap, and (2) missing genuinely unfaithful condensations that happen to retain source phrasing (false negative on drift). Without a validated threshold, any cutoff chosen will be arbitrary and likely to fail to generalize across the wiki's varied source genres (talk transcripts vs. papers vs. dense theory pages).

### Mitigations available

Established alternatives exist and are directly transferable: use coverage/density measures (Grusky et al.-style extractive fragment metrics) instead of raw trigram counts, or pair lexical overlap with an NLI-based or QA-based factual-consistency check (e.g., QAGS-style question-answering consistency) rather than relying on lexical overlap alone. Coverage-density has an established positive correlation with faithfulness in the literature, giving it more validated grounding than an untested trigram threshold.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** ASSUMPTION-892

**Strongest counterargument:** The strongest case against the assumption is that it optimizes the wrong axis: trigram coverage measures how much verbatim phrasing survives, which correlates with *extractiveness*, not *faithfulness*. The evaluation literature explicitly warns that these are separable dimensions — extractive summaries tend to score artificially well on lexical-overlap metrics regardless of whether they preserve meaning, while genuinely faithful abstractive condensations can score poorly simply because they reword. Using trigram coverage as the discriminator therefore risks systematically favoring copy-paste-style condensation over genuinely well-compressed, faithful rewrites, which is close to the opposite of what "condensed-but-faithful" is meant to select for.

**What would need to be true for C2A2 to be safe:** The wiki's condensation task would need to be low-abstraction (i.e., condensations are expected to closely mirror source phrasing, not paraphrase), in which case lexical overlap and faithfulness would be more likely to move together — but this is an empirical question about the actual condensation style used, not something the assumption currently establishes.

**How to test:** Sample a set of known faithful and known unfaithful condensations (hand-labeled), compute trigram coverage, coverage/density, and an NLI-based faithfulness score for each, and check whether trigram coverage alone separates the two classes as well as the alternative metrics — this would empirically validate or refute the assumption before any threshold is fixed.

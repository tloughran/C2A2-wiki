SEARCH-FOR-ASSUMPTION-892:
  Date searched: 2026-08-10
  Original item: ASSUMPTION-892
  Original statement: "Trigram coverage looks like a better discriminator than word-count ratio for telling condensed-but-faithful from summary-form" — proposed with no threshold.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-892
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted the stated claim that trigram/n-gram coverage discriminates faithful-condensed text from summarized text better than a raw word-count ratio.
      15a: Searched for supporting literature on n-gram overlap metrics for summarization/faithfulness and extractive-vs-abstractive discrimination.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Grusky et al. and related work on "degree of abstraction" / copied n-gram fraction — summarized via ScienceDirect "Abstractive Summarization" overview and arXiv "Evaluating the Tradeoff Between Abstractiveness and Factuality in Abstractive Summarization" (2021). — Establishes that the fraction of copied n-grams (for n=1..4, i.e., including trigrams) from source to summary is a standard, published way to measure how extractive vs. abstractive a text is, directly supporting trigram coverage as a meaningful discriminator of "condensed-but-faithful" (high n-gram retention) vs. genuine abstraction/summary-form (low retention).
    2. Lin, C-Y. (2004). "ROUGE: A Package for Automatic Evaluation of Summaries." — [unverified — from search snippet; canonical ROUGE citation, widely known] Establishes ROUGE-N (n-gram overlap, including ROUGE-3/trigram variants) as the standard family of metrics for summary evaluation, the direct methodological ancestor of "trigram coverage" as a discriminator.
    3. Fischer & Remus (2022), "Measuring Faithfulness of Abstractive Summaries," KONVENS. — Discusses n-gram-based approaches to faithfulness and notes their known failure mode (insensitivity to small but semantically important edits), implicitly supporting the idea that higher-order n-grams (trigrams+) carry more localized semantic signal than unigram-based word-count-style ratios, since longer n-gram matches are harder to satisfy by coincidence.

  Strength of support: Moderate

  Summary: Published NLP literature confirms that n-gram overlap fraction — including trigram-level overlap — is an established way to quantify how much a text has been abstracted from its source, and that this is a more discriminating signal than a simple word-count ratio because it captures whether specific phrasing/structure survived, not just length. ROUGE-N (n=1,2,3...) is the dominant family of automatic summary evaluation metrics and trigram-level (ROUGE-3) variants are used specifically because they are stricter than unigram overlap. This gives real methodological grounding for treating trigram coverage as a better discriminator than word-count ratio.

  Caveats: No threshold is proposed in ASSUMPTION-892, and the literature does not supply a universal one either — ROUGE-N thresholds are typically corpus- and task-calibrated, not fixed constants. More importantly, the literature is emphatic that all n-gram overlap metrics (trigram included) are known to be poor faithfulness/hallucination detectors on their own: they are insensitive to semantic-preserving paraphrase (false negatives for faithful abstraction) and insensitive to small factual substitutions embedded in otherwise-high-overlap text (false negatives for unfaithfulness). So while trigram coverage outperforming word-count ratio as a discriminator of extractive-vs-abstractive form is well supported, using it as a proxy specifically for "faithfulness" is only weakly supported and is a separate, more contested claim.

  Recommendation: PARTIALLY-SUPPORTED

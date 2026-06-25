SEARCH-FOR-PRESUMPTION-380:
  Date searched: 2026-06-24
  Original item: PRESUMPTION-380
  Original statement: "That a 14-thinker keyword/relevance score (>0.4) is the right instrument for cross-tradition relevance, merely mis-tuned (page-as-unit / keyword-match unexamined)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-380
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: the instrument's class (keyword/page-unit) is taken as given; only its threshold is questioned
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Multi-channel relevance scoring (USPTO 12547631; citation-recommendation baselines). - Keyword matching captures literal similarity and is a useful COMPLEMENTARY channel alongside embeddings; as one input it has real value.
    2. TF-IDF baselines in link prediction (arXiv 2403.18855). - Keyword/TF-IDF gives a non-trivial baseline (MAP ~10.5%, MAR ~34.6%), so a keyword score is not worthless for relevance.

  Strength of support: Weak-Moderate

  Summary: There is weak-to-moderate support for keyword/relevance scoring as a usable signal: it is a standard complementary channel and provides a non-trivial baseline for relevance and link prediction. This backs the idea that the instrument is informative and could be tuned. It does not support the stronger presumption that keyword-over-pages is the RIGHT instrument for CROSS-tradition (conceptual, cross-domain) relevance - the literature treats keyword matching as the weaker channel precisely where conceptual bridging is required.

  Caveats: Support is for keyword-as-one-channel, not keyword-as-the-instrument. Its baseline status is the ceiling, not the recommendation.

  Search scope: multi-channel scoring; TF-IDF baselines. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

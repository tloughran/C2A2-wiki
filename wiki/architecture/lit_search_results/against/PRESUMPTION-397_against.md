SEARCH-AGAINST-PRESUMPTION-397:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-397
  Original statement: "That a closed keyword list of navigational openers adequately separates navigational from informational intent for open-ended voice input"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-397
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: a hand-enumerated keyword list assumed to cover open-ended spoken intent; misroute is recoverable
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Rule-vs-learned intent classification (Hashemi 2016; weak-supervision vs LLM comparisons, arXiv 2025). - Keyword/rule classifiers lack coverage for phrasing variation, slang, and OOV; learned models outperform on open-ended queries.
    2. Voice-query characteristics (conversational, disfluent, paraphrastic). - Spoken input is longer and more variable than typed queries, worsening keyword-list coverage.
    3. Broder/Jansen intent work (limits side): a non-trivial fraction of queries are ambiguous between navigational and informational, which a closed list cannot resolve.

  Strength of challenge: Moderate

  Summary: Partially challenged: closed keyword lists are known to under-cover open-ended input. They work for clearly-marked queries but miss paraphrase, slang, disfluency, and out-of-vocabulary openers - all amplified in conversational VOICE input. The literature consistently finds learned classifiers outperform rule/keyword approaches on open-ended intent, and that a meaningful fraction of queries are intrinsically ambiguous. The presumption's 'adequately separates' overreaches, though the low stakes (recoverable misroute) limit the severity.

  Specific risks: Systematic misrouting of paraphrased/spoken navigational queries to the informational path (or vice versa), degrading the voice UX for non-canonical phrasings.

  Mitigations available: Measure misroute rate on real voice inputs; back the keyword list with a learned fallback classifier or confidence threshold; allow easy user correction (already noted recoverable).

  STEELMAN:
    Item: PRESUMPTION-397
    Strongest counterargument: Open-ended voice intent is too variable for a hand-enumerated opener list; coverage gaps on paraphrase/slang/OOV are exactly where a closed list fails, and learned routers measurably outperform, so 'adequately separates' is unsupported for the open-ended case.
    What would need to be true for C2A2 to be safe: Measured misroute rate on real voice input is low enough to tolerate given easy recovery.
    How to test: Collect a sample of real spoken queries; measure keyword-list misroute rate vs a learned classifier baseline.

  Search scope: Rule-vs-learned intent classification; voice-query variability. Adequate.

  Recommendation: PARTIALLY-CHALLENGED

SEARCH-FOR-PRESUMPTION-397:
  Date searched: 2026-06-25
  Original item: PRESUMPTION-397
  Original statement: "That a closed keyword list of navigational openers adequately separates navigational from informational intent for open-ended voice input"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-397
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: a hand-enumerated keyword list is assumed to cover open-ended spoken intent; misroute is recoverable
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Broder 2002. 'A Taxonomy of Web Search.' SIGIR Forum. - The navigational/informational/transactional distinction is real and partly cue-driven, so keyword cues capture SOME navigational intent.
    2. Early rule/keyword intent classifiers (Jansen, Booth & Spink 2008): keyword heuristics achieve usable accuracy on clearly-marked queries.

  Strength of support: Weak

  Summary: There is weak support: the navigational/informational split is a genuine, partly lexically-cued distinction, and rule/keyword classifiers do achieve usable accuracy on clearly-marked queries. So a closed opener list will correctly route the easy, well-formed cases. This supports the approach as a cheap first pass.

  Caveats: Support is limited to well-marked queries; open-ended VOICE input (paraphrase, slang, disfluency, OOV openers) is exactly where keyword lists lose coverage (15b). 'Adequately separates' overreaches beyond the supported 'handles clear cases'.

  Search scope: Search-intent taxonomy; rule-based intent classification. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

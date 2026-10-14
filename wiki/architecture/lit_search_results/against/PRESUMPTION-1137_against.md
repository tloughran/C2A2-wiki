SEARCH-AGAINST-PRESUMPTION-1137:
  Date searched: 2026-10-14
  Original item: PRESUMPTION-1137
  Original statement: [inferred] Carding presumes the structure of a work is recoverable from its paratext or a summary of it: chapter titles (Hoffman), abstracts (10-12 Friston), and a pipeline's own card text (document-explorer). The Speculative tag records low confidence, but the item still enters the review queue as a PRS candidate. Question under test: how accurately do abstracts/summaries represent the claims of the full text?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1137
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the cited evidence across 2026-10-13 transcripts and wiki files.
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED (weak)

  Challenging evidence found: Partial

  Which proposition the evidence bears on: Two propositions must be separated.
    P1 (the presumption itself): "structure/claims are recoverable from paratext/summary." The search direction AGAINST the concern = evidence that P1 is adequate.
    P2 (the concern): "summaries misrepresent the full text." Most retrieved evidence SUPPORTS P2 (i.e., does not challenge the concern); only a narrow triage-adequacy finding challenges it.

  Sources:
    1. [Authors not verified in this run], 2017. Scoping review of abstract vs full-report inconsistency. BMC Medical Research Methodology 17, doi:10.1186/s12874-017-0459-5. — Median inconsistency 39% (range 4-78%), but MAJOR discrepancies (design, sample size, primary outcome, main results, conclusions) median 19% (5-45%). Bears on P1/P2: ~4 in 5 biomedical abstracts carry no major misrepresentation of the main claim — modest support for abstracts as structure/claim triage; but 1 in 5 does misrepresent. [Level: search-snippet; full-text fetch blocked/deduplicated with no content returned.]
    2. Waffenschmidt S, et al., 2019. Single vs double title/abstract screening. BMC Med Res Methodol, doi:10.1186/s12874-019-0782-0; and in vitro screening comparison (Clinical Science 137(2):181, 2023, authors unverified). — Abstract-level screening by an experienced reviewer is an acceptable shortcut for triage; abstract-based exclusion missed ~14% of relevant studies in an in vitro domain. Bears on P1 for TRIAGE (relevance), not for claim/structure fidelity. Challenges the concern only in the triage use-case. [Level: snippet.]
    3. Kim Y, Chang Y, Karpinska M, et al., 2024. "FABLES: Evaluating faithfulness and content selection in book-length summarization." arXiv:2404.01261. — Best LLM (Claude 3 Opus) ~90% of claims faithful on 26 recent books; others 70-78%; errors concentrate in events/states requiring cross-narrative reasoning; systematic over-weighting of book endings; automatic raters unreliable. Bears on P1 for the document-explorer card-text case: modern-model summaries are mostly faithful at the claim level, but omission and late-section bias distort STRUCTURE specifically. [Level: abstract + snippet.]
    4. (Supports concern) Pitkin RM, Branagan MA, Burmeister LF, 1999. "Accuracy of data in abstracts of published research articles." JAMA 281:1110-1111. — 18-68% of abstracts deficient across six major journals. [Level: snippet.]
    5. (Supports concern) Boutron I, et al., 2010. JAMA, "spin" in abstracts of RCTs with non-significant primary outcomes; follow-up SPIIN trial showed spin shifts clinician interpretation. [Level: snippet.]

  Strength of challenge: Weak

  Summary: The literature mostly supports the concern that summaries misrepresent full texts: biomedical abstracts are inconsistent with the full report in ~39% of cases (major in ~19%), spin is common, and LLM book summaries omit and mis-weight content. The available challenge is narrow: abstracts and well-made summaries are adequate for relevance TRIAGE (an experienced single screener is an accepted shortcut; best-model book summaries are ~90% claim-faithful), and the majority of abstracts contain no major misstatement. No evidence was found that chapter titles/ToCs alone recover a humanities work's argumentative structure — a literature gap rather than a challenge; humanities paratext was searched once with no empirical results. Domain caveat: all abstract-accuracy data are biomedical; transfer to philosophy/consciousness monographs (Hoffman, Kastrup, McGilchrist) is untested in either direction.

  Specific risks: If C2A2 treats the concern as fully established, it may block useful triage cards. If P1 is accepted beyond triage, PRS cards could encode structure that the full work does not have (especially omitted middle sections — FABLES' end-weighting bias), and the Speculative tag would not prevent queue entry.

  Mitigations available: Restrict paratext-derived cards to triage status (relevance only), require a full-text pass before a card asserts structure or claims; spot-check a sample of cards against full text; flag cards derived from a pipeline's own card text (summary-of-summary) as a higher-risk tier.

  Recommendation: PARTIALLY-CHALLENGED (Weak) — challenge applies only to the triage use; for structure/claim fidelity the search found NO challenge.

  Search scope: preliminary search — 4 web searches, 1 fetch attempted (BMC/Springer page; returned "already fetched" deduplication with no content — counted as a fetch failure). Broader search recommended for humanities paratext studies.

STEELMAN:
  Item: PRESUMPTION-1137
  Strongest counterargument: Carding is a triage step, not a reading. For triage, the field standard (systematic-review practice) is precisely to decide on title and abstract and defer to full text later; four in five abstracts carry no major misstatement, and current LLM summaries are around 90% claim-faithful even for book-length works. A "Speculative" card derived from paratext, explicitly tagged low-confidence and gated by human review, is therefore the methodologically conventional move, not a presumption error — demanding full-text reading before any card would throttle intake for little gain.
  What would need to be true for C2A2 to be safe: Paratext-derived cards are never promoted beyond Speculative without a full-text check; the reviewer knows the card's provenance (abstract vs ToC vs pipeline card-text); and the card asserts relevance/topic, not argumentative structure.
  How to test: Sample 5-10 existing paratext-derived cards; have a full-text pass list the work's main claims and structure; score each card for major/minor discrepancy using the 2017 scoping review's major/minor categories; compare against the ~19% biomedical major-discrepancy baseline.

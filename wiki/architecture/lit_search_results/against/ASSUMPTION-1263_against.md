SEARCH-AGAINST-ASSUMPTION-1263:
  Date searched: 2026-09-06
  Original item: ASSUMPTION-1263
  Original statement: "Search independence holds for 10 of 11 items (no 15a file was read before its 15b file
    was written)." Tested as: artifact-blinding (not reading the opposing output) is the operative condition
    for evaluator independence.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1263
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-09-05 15c run note's execution-failure declaration.
      15b: Searched for challenging literature (2026-09-06). NOTE ON AUTHORSHIP: written by the 15c
        orchestrating context after the delegated 15b subagent launch produced no files in ~55 minutes.
        This context HAD read the 15a file for this item (and the other two 15a files) before this search.
        Search independence therefore does NOT hold for this item; see the run note and DISPOSITION-907.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kohli, G., 2026. "Nine Judges, Two Effective Votes: Correlated Errors Undermine LLM Evaluation
       Panels." arXiv:2605.29800 (Apple ML Research). [VERIFIED: title/arXiv ID/author/affiliation seen in
       search results] — Nine frontier judges from seven families, none of which read each other's output,
       carry ~2 votes of independent information; panel accuracy falls 8–22pp short of the independence
       benchmark. Artifact-blinding was total and independence still failed: the operative channels are
       shared training, not shared reading. Directly contradicts "not reading = independent."
    2. Temkit, S.-A., 2026. "AMEL: Accumulated Message Effects on LLM Judgments." arXiv:2605.22714 (v3
       2026-06-09). [VERIFIED: title/arXiv ID/author/versions seen in search results; effect sizes from
       abstract snippet] — 84,088 calls, 12 models, 5 providers: identical items judged after a history of
       predominantly positive or negative evaluations shift toward the history's polarity (d = −0.17,
       p < 10⁻⁵³), with ambiguous items absorbing the most bias (d = −0.28). A context that has just written
       FOR files is such a history. The bias is in the writer's state, not in what was read.
    3. "Evaluating the Sensitivity of LLMs to Prior Context," arXiv:2506.00069. [VERIFIED: title/arXiv ID;
       authors NOT verified] — Prior context, even unrelated, degrades multiple-choice accuracy by up to 73%
       for some models and up to 32% for GPT-4o. Independence-by-file-reading cannot account for this;
       the prior context here is the evaluator's own earlier work.
    4. Panickssery, A., Bowman, S.R., Feng, S., 2024. "LLM Evaluators Recognize and Favor Their Own
       Generations." NeurIPS 2024. [VERIFIED: title/first author/venue via proceedings.neurips.cc; co-authors
       NOT verified] and Wataoka et al., 2024, "Self-Preference Bias in LLM-as-a-Judge," arXiv:2410.21819
       [VERIFIED: title/arXiv ID; authors NOT verified] — Judges favour text with lower perplexity to
       themselves, i.e. their own style, without being told authorship. When 15a and 15b are the same model,
       each "independent" file is in the other's preferred style; blinding cannot remove a bias that operates
       on the text's form rather than on knowledge of its source.
    5. van Rooyen, S., Godlee, F., Evans, S., Smith, R., Black, N., 1998. "Effect of Blinding and Unmasking
       on the Quality of Peer Review: A Randomized Trial." JAMA 280(3):234–237. [VERIFIED: title/journal/
       PubMed 9676666 seen in search results; already in the register under PREMISE-111] — 527 manuscripts;
       blinding and unmasking made no editorially significant difference to review quality or
       recommendations. The most-cited human evidence that artifact-blinding is a small lever.
    6. Hertzum, M. & Jacobsen, N.E., 2001. "The Evaluator Effect: A Chilling Fact About Usability Evaluation
       Methods." IJHCI 15(1). [VERIFIED: title/authors/journal/volume via tandfonline] — Independent
       evaluators of the same artifact detect markedly different problem sets (only 20% of 93 problems found
       by all; 46% by a single evaluator). Independence between evaluators is a variance source, not a
       guarantee of coverage; the assumption treats independence as if it delivered coverage.

  Strength of challenge: Strong

  Summary: The assumption makes read-order the criterion of independence. The 2026 LLM-judge literature
  measures independence directly and finds it fails under complete artifact-blinding: nine judges that never
  see each other's output act as two (Kohli). AMEL and the prior-context study show that what the evaluator
  has itself just produced shifts its next judgment, most strongly on ambiguous items — which is what a
  FOR-then-AGAINST sequence in one context is. Self-preference bias shows that same-model outputs are
  favoured by form, not by disclosed source. The human blinding RCT (van Rooyen) already in the register found
  blinding editorially insignificant. Read-order is therefore a necessary hygiene condition but not the
  operative one; "10 of 11" measures the weakest of at least four channels (PREMISE-111) and reports it as
  though it were the sum.

  Specific risks: (a) The 10-of-11 figure is read as "10 of 11 pairs are independent readings," and their
  agreement is then counted as corroboration — precisely what PREMISE-111/197 forbid. (b) Ambiguous items —
  where the pipeline most needs two views — are the ones AMEL shows are most biased by accumulated context.
  (c) The metric is self-measured by the context whose independence is in question (PREMISE-124 pattern).

  Mitigations available: Report two numbers, not one: read-channel independence (file order) and
  execution independence (distinct contexts), and count a pair as independent only when both hold. For
  orchestrator-written pairs, apply the PREMISE-111 discount explicitly (treat as one reading). Randomise
  or alternate direction order across items so accumulated polarity does not run one way. A cheap in-house
  test: re-run one AGAINST in a fresh context and diff its sources against the same-context version.

  Search scope: Preliminary — 5 queries plus 2 register sources (PREMISE-111). Not covered: forensic
  contextual-bias literature (Dror) beyond snippets; systematic-review dual-screener recall studies; formal
  treatments of conditional independence given a common cause. Broader search recommended before the
  10-of-11 figure is cited anywhere.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1263
  Strongest counterargument: Independence is a statistical property — errors uncorrelated given the item —
  and it is fixed by what the two evaluators share, not by what they read. Two copies of one model that
  never read each other's files still share pre-training, alignment, and (in the 09-05 case) an actual
  context window, and the measured cost is 8–22pp of lost accuracy and a ~4:1 collapse in effective votes.
  Calling the read-channel record "search independence" therefore names a property the record does not
  have, and any downstream use of the count as a discount factor is mis-scaled by roughly the ratio Kohli
  measures.
  What would need to be true for C2A2 to be safe: The count is used only as a hygiene audit (were files
  read out of order?) and never as an independence weight; all evidential weighting of 15a/15b agreement
  runs through PREMISE-111/197 regardless of read order.
  How to test: For a sample of past items, generate a second AGAINST in a fresh context with the same
  prompt and compare source overlap and verdict with the same-context AGAINST. If overlap with the FOR
  file's framing is higher in the same-context version, the writer-state channel is live.

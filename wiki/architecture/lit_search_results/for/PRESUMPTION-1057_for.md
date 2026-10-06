SEARCH-FOR-PRESUMPTION-1057:
  Date searched: 2026-09-21
  Original item: PRESUMPTION-1057
  Original statement: The 223-day lag is a discovery-channel failure, not a coverage failure; pair
    enumeration may not address it.

  **Execution note (recorded for honesty, not buried):** this run of 15a and 15b was executed by a
  single scheduled process (`c2a2-lit-search-pipeline`, 2026-09-21). The two directions were run as
  separately-framed query sets and the FOR files were written before any AGAINST query was issued, but
  the strict independence the spec assumes (two processes, neither seeing the other) was NOT achieved.
  Read the strength ratings with that caveat.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-1057
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Noted the gap between a channel-shaped diagnosis and a coverage-shaped remedy.
      15a: Searched for supporting literature on channel effects in discovery.
    Current status: SUPPORTED
    Pre-registration: the success criterion for the companion back-test (recover the 2026-02-04
      Hoffman/Friston event) was stated in the 2026-09-20 intake BEFORE the sweep was built. That
      ordering is recorded here so it can be audited later.

  Supporting evidence found: Yes

  Sources:
    1. "Rethinking Literature Search Evaluation: Deep Research Helps, and Human Citation Lists Are Not a
       Ground Truth." arXiv:2605.29234. — The key quantitative finding for this item: using an OpenAlex
       co-authorship-graph distance metric, a measurable portion of retrieval-quality gaps is attributed
       to *network bias in human citing*, with humans citing direct collaborators 2.5x more often than
       the strongest re-rankers. Discovery is demonstrably channel-shaped, not merely coverage-shaped.
    2. Hirt, J. et al. 2023. "Citation tracking for systematic literature searching: A scoping review."
       *Research Synthesis Methods*. DOI:10.1002/jrsm.1635. — Reports that different tracking channels
       retrieve systematically different record sets; which channel you use, not how much you enumerate,
       determines a large share of what you find.
    3. "Seed-based information retrieval in networks of research publications." arXiv:2403.09295. —
       Comparative evaluation showing channel choice (direct citation vs. bibliographic coupling vs.
       co-citation vs. related-article scoring) drives retrieval differences on the same corpus.

  Strength of support: Strong (for the channel half); the "pair enumeration may not address it" half is
    supported only by inference from the same sources.

  Summary: The literature supports the diagnostic distinction 14b drew. Retrieval outcomes in this class
    of problem are dominated by *which channel* is searched, and network position produces large,
    measurable biases in what surfaces — an effect size (2.5x) big enough that a coverage-shaped remedy
    applied to the wrong channel would plausibly leave the lag intact. Note the epistemic structure
    here: this item and ASSUMPTION-1561 are the two halves of one question, and the same source set
    supports both — enumerating relations raises recall (1561) *and* channel bias is the dominant term
    (1057). Both can be true; the back-test discriminates them.

  Caveats: No source addresses the specific corpus (long-form spoken media) or the specific quantity
    (a 223-day lag to notice a joint appearance). The claim that pair enumeration "may not address it"
    is appropriately hedged by 14b and this search does not remove the hedge — it establishes that the
    hedge is warranted, not that the remedy fails. The named back-test settles it at low cost and
    should be run before the 91-pair sweep is built. Preliminary search.

  Recommendation: SUPPORTED

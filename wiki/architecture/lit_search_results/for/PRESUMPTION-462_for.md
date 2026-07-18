SEARCH-FOR-PRESUMPTION-462:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-462
  Original statement: "Fixed re-check cadences (7-day reviewer staleness rule; weekly 15d re-trigger) are right-sized — set once, never load- or change-rate-adapted."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-462
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inference from cohort listing (2026-07-08 EOD)
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Cho & Garcia-Molina, 2003. "Effective Page Refresh Policies for Web Crawlers." ACM Transactions on Database Systems. — The classic counterintuitive result and the strongest support for fixed cadences: a *uniform* (fixed-interval) refresh policy outperforms the intuitive proportional-to-change-rate policy for maximizing freshness under a resource constraint. Fixed cadence is not merely a lazy default; it is provably better than the naive adaptive alternative.
    2. Avrachenkov, Patil & Thoppe, 2020. "Change Rate Estimation and Optimal Freshness in Web Page Crawling." EAI ValueTools / ACM. — Frames optimal recheck as a function of estimated change rate; relevant here because it shows fixed intervals are near-optimal when change rates are homogeneous across items — a condition a curated pipeline may approximately satisfy.
    3. Grimes & Ford (Google Research), 2008. "Risk and optimality in estimating refresh rates for web pages." research.google.com. — Treats refresh-rate estimation as a risk trade-off; supports the position that adaptation only pays when per-item change-rate estimates are reliable, and that simple fixed policies are robust when observation data is sparse (as with single-bit "changed since last check" signals).

  Strength of support: Moderate

  Summary: There is real support for fixed cadences as a policy class: Cho & Garcia-Molina's canonical result shows uniform fixed-interval rechecking beats naive change-rate-proportional adaptation, and the estimation literature shows adaptive policies require change-rate estimates that are unreliable when recheck observations are sparse — the exact regime of a young pipeline with weekly signals. Fixed weekly/7-day cadences are therefore a defensible, literature-consistent starting policy, robust and cheap. Support is partial rather than full because the same literature makes adaptation the eventual optimum: intervals should be revisited as change-rate data accumulates (the simple rule "two consecutive no-change observations → lengthen; two consecutive changes → shorten" appears in the adaptive-refresh literature), and the "never adapted" clause forgoes this. Notably, ASSUMPTION-429's overload finding is itself evidence the weekly 15d cadence is mis-sized relative to load.

  Caveats: Support weakens when (a) per-item change rates are heterogeneous (uniform policy's advantage assumes rough homogeneity); (b) sustained overload signals the cadence-load mismatch directly (yield-per-recheck and queue growth are free control signals going unused); (c) the cost asymmetry of a stale premise is high. The literature supports "fixed until data says otherwise," not "set once, never adapted."

  Search scope confidence: Comprehensive for crawl-scheduling/freshness literature; TTL-tuning literature consistent by analogy.

  Recommendation: PARTIALLY-SUPPORTED

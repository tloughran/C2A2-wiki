SEARCH-FOR-ASSUMPTION-511:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-511
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Medium)
  Original statement:
    The pending queue at 7 is healthy re-accumulation after the 07-20 blanket approval; it will re-
      accumulate until the next decision email.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-511
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from the 2026-07-22 daily run pending-queue note
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Search scope: WebSearch, 2026-08-30, clustered query — "Little's Law; stability requires arrival rate <= service rate; unbounded backlog growth". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Supporting evidence found: No

  Sources:
    1. Wikipedia. "Little's law." — L = lambda x W, distribution-free; stability requires arrival rate not
       exceeding exit rate, otherwise queue grows without bound.
    2. InfoQ. "The Mathematics of Backlogs: Capacity Planning for Queue Recovery." — maximum tolerable
       queue depth follows directly from arrival rate and target latency.
    3. Little & Graves. "Little's Law as Viewed on Its 50th Anniversary." — the law's generality and its
       stationarity precondition.

  Strength of support: None; Strong for the negation

  Summary:
    Little's Law and its stationarity precondition give the opposite result to the item's. A queue is
      bounded only if the arrival rate does not exceed the exit rate; with a service rate at or near zero,
      depth grows without bound and 'healthy' has no queueing-theoretic content. Capacity-planning practice
      derives maximum tolerable depth directly from arrival rate and target latency, and 7 is not evaluable
      against any such target because none is stated.

  Caveats:
    The negation holds only under the stationary reading, and only if ~0/day is the right service
      measurement -- see the challenge direction, which materially qualifies this.

  Recommendation: NO-SUPPORT-FOUND

SEARCH-FOR-ASSUMPTION-493:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-493
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Medium)
  Original statement:
    The 300-series PRS total is stale and should be retired at source; the measured network figure is 511.
      Four totals circulating; the wrong number reached three consecutive morning emails.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-493
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 daily run, exact quote
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-30, clustered query — "canonical metric / single-source-of-truth governance for derived aggregates". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Supporting evidence found: Yes

  Sources:
    1. Wikipedia. "Single source of truth." — SSOT architecture: every data element mastered/edited in
       exactly one place, normalized to a canonical form.
    2. PowerMetrics. "What does 'single source of truth' actually mean for metrics?" — one shared
       definition, one calculation logic, one governed location; conflicting departmental numbers
       are the named failure mode.
    3. Alation. "Canonical Data Models: A Comprehensive Guide." — governance roles and workflows prevent
       fragmentation of the canonical model over time.

  Strength of support: Strong

  Summary:
    The generalizable limb -- that a derived aggregate should have exactly one mastered definition and one
      governed calculation site -- is textbook data-governance practice. The literature names precisely the
      observed failure: when several parties compute the same quantity independently, conflicting figures
      circulate and each is locally defensible. The prescribed remedy is not to pick the largest or newest
      number but to designate a mastering location and route all consumers through it, with governance to
      stop the canonical model fragmenting again.

  Caveats:
    The literature prescribes designating an authority; it does not adjudicate WHICH of 300/364/447/511 is
      correct. That is an internal recount, not a literature question. Sources are practitioner and
      encyclopedic, not primary research.

  Recommendation: SUPPORTED

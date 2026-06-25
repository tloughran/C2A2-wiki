SEARCH-FOR-ASSUMPTION-354:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-354
  Original statement: "A retrospective-only confirmatory run on the pre-registering-commit ledger is ungameable-by-construction (past can't be steered by a future rule)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-354
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted; coupled to REVISE-115; self-noted caveat retrospective != clean
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Natural-experiment logic (Angrist & Pischke 2009, 'Mostly Harmless Econometrics'). - Outcomes recorded before a rule exists cannot have been influenced by that rule; pre-existing records limit one channel of gaming.
    2. Time-stamped commit ledgers (version-control provenance) provide tamper-evident historical ordering, supporting the 'past is fixed' premise.
    3. Pre-registration literature (Nosek 2018) - a locked, time-stamped record is the substrate that makes confirmatory claims auditable.

  Strength of support: Moderate

  Summary: The narrow mechanical claim is sound: data generated before a scoring rule was conceived cannot have been optimized toward that rule, so one important gaming channel (forward steering of the logged behavior) is genuinely closed by construction. A time-stamped commit ledger supplies exactly the tamper-evident substrate this argument needs.

  Caveats: 'Ungameable-by-construction' overclaims. Two open degrees of freedom remain: (a) selection of WHICH retrospective analysis/subset to run is a post-hoc choice (garden of forking paths over the fixed past), and (b) the ledger itself may have been shaped by anticipation of future evaluation. The assumption's own 'retrospective != clean' caveat concedes this. Support is for 'closes forward-steering', not for 'ungameable'.

  Search scope: Natural-experiment / retrospective-design validity; metric gaming channels. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

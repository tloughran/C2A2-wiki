SYSTEMIC-RISK-FLAG (15b, 2026-10-01, Weak):
  Items: PRESUMPTION-1099, PRESUMPTION-1100, PRESUMPTION-1102 (1101 separate)
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1099, PRESUMPTION-1100, PRESUMPTION-1102
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across 09-30 sessions.
      15b: Cross-item pattern detected while searching for challenging literature
    Current status: SYSTEMIC-RISK
  Shared vulnerability: each remedy adds state (a shared run record, a split status field, a backoff counter) that can itself be stale or wrong and sits in a component nobody monitors. Fetched sources favour simple, independent, minimal-state designs with an external staleness check.
  Secondary (PRESUMPTION-1101): remedies such as default-on-timeout can hide the very failure they address.
  Related earlier flag: self-referential verification (2026-09-30).

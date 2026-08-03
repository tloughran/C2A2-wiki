SEARCH-FOR-PRESUMPTION-636:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-636
  Original statement: That presence in a register implies tracking — i.e. that an item
    listed in monitor_queue.md is in fact being carried by a live search request.

  ROUTING NOTE: Item carries [QUEUED-EMPIRICAL]. Per the standing convention
  (ASSUMPTION-519 / PREMISE-124) the decisive test is the in-house join of
  MONITOR-001..344 against for_lit_search.md, NOT this literature search. This file
  records the secondary literature clause only and must not be read as the decisive
  evidence. The in-house test remains OWED. Fail-loud: it was not run this cycle.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-636
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a disclosure that names the gap and assigns the audit to a role
           absent from wiki/agents/ (origin ASSUMPTION-657)
      15a: Searched secondary literature clause only; decisive in-house test NOT run
    Current status: NO-SUPPORT-FOUND (secondary clause)

  Supporting evidence found: No

  Sources:
    1. ServiceNow CMDB practice literature, "Stale Records vs Orphan Records" — orphan
       records are defined as configuration items that exist but hold no valid
       relationship to anything else. The category exists precisely because register
       presence does not imply linkage.
    2. Proofpoint, "What Is Stale Data?"; DQOps, "What is Stale Data?" — stale data
       proliferates wherever organisations lack a mechanism to identify, refresh or
       retire outdated entries; persistence is the default, not the exception.
    3. Data decay management literature (US Patent 8,452,733 and related) — treats
       decay as a rate to be actively managed, implying untracked entries accumulate
       monotonically absent a reaper process.

  Strength of support: None

  Summary: The supportive direction returns nothing. Every source located treats
  register presence and live tracking as separable, and names the gap between them as a
  standard, expected defect class with its own vocabulary (orphan record, stale record,
  data decay). The literature's consensus remedy is a governance mechanism with named
  ownership and a freshness SLA — which is the thing 14b observed to be absent here
  (the audit is assigned to a role with no file in wiki/agents/).

  Caveats: This literature is about CMDBs and CRM records, not about self-testing agent
  registers; the transfer is by analogy. More importantly, none of it is decisive for
  this item — the join is cheap and available in-house, and 15d's own estimate of ~80
  dead entries can be confirmed or refuted by direct command. Literature cannot settle a
  question about this vault's contents.

  Recommendation: NO-SUPPORT-FOUND — and DEFER to the in-house join, which is OWED.

  Search scope: Secondary clause only, by design.

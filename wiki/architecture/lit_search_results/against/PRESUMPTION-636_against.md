SEARCH-AGAINST-PRESUMPTION-636:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-636
  Original statement: That presence in a register implies tracking.

  ROUTING NOTE: [QUEUED-EMPIRICAL]. Per ASSUMPTION-519 / PREMISE-124 the decisive test is
  the in-house join of MONITOR-001..344 against for_lit_search.md. That join was NOT run
  this cycle. Fail-loud: this file is the secondary literature clause only.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-636
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a disclosure naming the gap and assigning the audit to a role
           absent from wiki/agents/ (origin ASSUMPTION-657)
      15b: Searched challenging literature (secondary clause); in-house join NOT run
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. ServiceNow CMDB practice, "Stale Records vs Orphan Records" — the orphan-record
       category exists because register presence routinely fails to imply linkage. The
       defect is common enough to have standard tooling.
    2. Proofpoint, "What Is Stale Data?" — stale entries proliferate wherever no
       proactive mechanism exists to identify, refresh or retire them; persistence is the
       default state.
    3. DQOps / Acceldata / Quadratic on data decay — decay is a rate; absent a reaper
       process, dead entries accumulate monotonically and are indistinguishable from live
       ones in every count that does not join against the tracking table.
    4. Data decay management (US Patent 8,452,733) — treats freshness as requiring an
       explicit owner and SLA, the two things 14b records as missing here.

  Strength of challenge: Moderate-to-Strong (literature); NOT DECISIVE (see routing note)

  Summary: Every source treats register presence and live tracking as separable, gives
  the gap a name, and reports that it widens by default. The consensus remedy is
  governance with a named owner and a freshness SLA — precisely the structure 14b found
  absent, since the audit is assigned to a role that has no file in wiki/agents/. The
  challenge is therefore not just that the presumption is false in general but that C2A2
  lacks the one mechanism the literature identifies as preventing it.

  Specific risks: The system's inventory of its own open questions would be an overcount
  by an unknown margin, and the overcounted items are indistinguishable from live ones in
  every published figure. 15d's own estimate is ~80 dead entries. Because MONITOR counts
  feed the daily summary and the maturity narrative, the error propagates into every
  report of how much the system is tracking.

  Mitigations available: Yes, and one of them settles the question outright: run the join.
  Beyond that, (i) assign the audit to an agent that exists, (ii) add a freshness field to
  monitor_queue entries so a dead entry is visible without a join, (iii) publish tracked
  counts as "registered / live" pairs rather than a single number.

  Recommendation: CHALLENGED — but the literature is secondary. The in-house join is OWED
  and is the only thing that can settle this item.

  STEELMAN:
    Item: PRESUMPTION-636
    Strongest counterargument: A register entry is a claim that something is being
    tracked; whether it is tracked is a fact about a different file. Nothing in the
    architecture ties the two together — no foreign key, no reconciliation step, no owner.
    Under those conditions the correct prior is that the two have drifted, and the
    magnitude of the drift is unknown to the system by construction. The sharp point is
    that this is not an unknown that requires research: the join is one command, the
    estimate already exists (~80), and it has not been run. A system that publishes counts
    it could cheaply verify and does not is not tracking those items; it is reporting them.
    What would need to be true for C2A2 to be safe: that every MONITOR entry has a
    corresponding live block in for_lit_search.md. This is decidable today.
    How to test: join MONITOR-001..344 against for_lit_search.md blocks; count entries
    with no live search request. Compare to 15d's ~80 estimate. Publish both numbers.

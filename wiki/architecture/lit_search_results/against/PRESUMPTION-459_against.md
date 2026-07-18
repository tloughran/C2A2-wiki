SEARCH-AGAINST-PRESUMPTION-459:
  Date searched: 2026-07-09
  Original item: PRESUMPTION-459
  Original statement: "Priority labels assigned at queue time remain valid at burn time — triage may select on stored tags without re-scoring."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-459
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: inference (unstated presumption, MEDIUM, from 2026-07-08 EOD cohort)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. "Bug Priority Change: An Empirical Study on Apache Projects." 2024. Journal of Systems and Software / arXiv:2403.05059. — Direct empirical evidence that priority labels are not stable: bug priorities in Apache projects change in identifiable patterns (24 distinct change patterns), demonstrating that initial triage scores are routinely revised as understanding and context evolve. Nuance: most changes occur before processing begins — which is exactly the window in which C2A2's queued items sit.
    2. "Triage in Software Engineering: A Systematic Review of Research and Practice." 2025. arXiv:2511.08607. — Systematic review of triage practice: priority assessment is context-dependent (project state, resources, interactions with other items), implying that when context shifts, stored priorities lose validity; re-triage is a recognized practice, not an exotic one.
    3. "Aging (scheduling)." OS literature (en.wikipedia.org/wiki/Aging_(scheduling)). — Scheduling theory formalizes one dimension of priority decay: an item's effective priority should be a function of stored priority AND waiting time; selecting on the stored tag alone is known to produce starvation and stale ordering.

  Strength of challenge: Moderate

  Summary: The empirical bug-triage literature shows priority labels are living judgments: they get revised, and predominantly during the pre-processing window — the same window in which C2A2's queued items age (and with ASSUMPTION-429's overload, that window is weeks, not hours). Priority is a function of the item AND the system state at scoring time: what was MEDIUM against last week's landscape may be HIGH after a fire, a paradigm-boundary lens change (PRESUMPTION-460's trigger), or resolution of a sibling item — none of which updates a stored tag. Scheduling theory adds that even if the world never changed, burn-time selection should still incorporate age, which stored tags do not. The challenge is Moderate, not Strong: the same Apache study implies many priorities are stable, and for short queue-residence times stored tags are a reasonable approximation. The presumption fails specifically in C2A2's regime of long residence plus fast-moving context.

  Specific risks: Burn cycles spend capacity on items whose importance has lapsed while newly-critical items sit in lower tiers under obsolete labels; interacts with ASSUMPTION-430 — strict priority selection on stale tags starves items that would re-score HIGH today; systematic bias accrues because the longest-waiting items have the stalest labels, so error grows with exactly the queue growth the system already exhibits.

  Mitigations available: Cheap re-scoring pass over the queue at burn time (even a heuristic: bump items touching systems that had incidents since scoring; decay/boost by age); record scoring context (date, triggering state) with each label so staleness is visible; re-triage any item older than N days before selection; effective-priority = stored tier + age bonus (aging), which needs no re-judgment at all.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Strongest counterargument: Re-scoring the whole queue every burn is O(queue) judgment work per cycle — in an already over-capacity system, spending scarce capacity re-triaging instead of burning makes the backlog strictly worse, and the Apache data itself shows most priorities do NOT change; selecting on stored tags is right most of the time at near-zero cost. Triage systems everywhere (hospitals, bug trackers) operate on assigned labels between periodic reviews precisely because continuous re-assessment is unaffordable.
    What would need to be true for C2A2 to be safe: Queue residence times must be short relative to the context-change rate, OR a periodic (not per-burn) re-triage must exist; events known to invalidate priorities (incidents, lens changes) must trigger targeted re-scoring of affected items; age must enter selection somehow so stale-label bias cannot compound indefinitely.
    How to test: Sample N queued items with stored labels and blind re-score them today; the disagreement rate directly measures label staleness in this queue. If disagreement is concentrated in older items, add aging; if it is broad, add re-triage.

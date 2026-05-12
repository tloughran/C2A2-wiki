SEARCH-AGAINST-ASSUMPTION-091:
  Date searched: 2026-05-09
  Original item: ASSUMPTION-091
  Original statement: "Off-cadence specialist proposal filings treated as on-cadence for downstream rendering and approval-rate tracking"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-091
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-08 specialist-proposal disposition decision
      15b: Searched for cadence-coupling literature on quality drift under variable scheduling
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (moderate)

  Sources:
    1. Newport (2016) "Deep Work"; Csikszentmihalyi (1997) "Finding Flow" — cadence-induced attention-state difference is documented; off-cadence work has different cognitive substrate than on-cadence work.
    2. Empirical agile-quality literature (Williams 2010 "Agile Quality"; Stol & Fitzgerald 2014) — cadence variance correlates with quality variance in attention-budget-constrained settings; the variance is small in steady state but non-zero.
    3. Statistical-process-control (Wheeler 2000; Deming 1986) — undifferentiated treatment of variable-cadence streams introduces bias into approval-rate tracking; downstream metrics carry the mixing.
    4. Knowledge-work productivity literature (Dean & Webb 2011 "Recovering from Information Overload") — off-cadence filings often happen during catch-up windows that share attention-state with other catch-up activities; uniform treatment masks the catch-up effect.
    5. C2A2-internal: PRESUMPTION-113 (off-cadence same baseline expectations) and ASSUMPTION-079 MONITOR-079 — the prior MONITOR was specifically about cadence-induced quality variance not yet tested; ASSUMPTION-091 inherits that gap.

  Strength of challenge: Moderate

  Summary: Uniform treatment is canonical default but the literature consistently flags cadence-induced quality variance under attention-budget constraints. The challenge is moderate because it does not refute uniform treatment but adds preconditions (steady-state attention; non-catch-up cadence). For approval-rate tracking specifically, mixing on-cadence and off-cadence filings introduces statistical bias that downstream metrics carry.

  Specific risks: (a) Approval-rate tracking is biased upward or downward depending on off-cadence quality direction; (b) catch-up-window filings share attention-state with stall-recovery work, which has documented different character; (c) compounds with PRESUMPTION-113 (same baseline expectations) and ASSUMPTION-079 (catch-up structurally equivalent) — three-item cluster around uniform-treatment without precondition tests.

  Mitigations available: (a) Tag off-cadence filings with cadence flag for downstream slicing; (b) add cadence-induced quality variance test to MONITOR-079 cadence; (c) rather than uniform treatment, treat as default-plus-slice (uniform pipeline, cadence-tagged metric).

  Recommendation: PARTIALLY-CHALLENGED (uniform treatment is canonical default; cadence-tagging for metrics is the standard guard, currently absent)

  STEELMAN:
    Item: ASSUMPTION-091
    Strongest counterargument: Uniform treatment hides cadence-induced quality variance precisely in approval-rate tracking, where the bias matters most. Catch-up-window filings share attention-state with stall-recovery work; the literature on attention budgets, statistical-process-control, and agile quality consistently treats this as observable variance. The structural pattern repeats ASSUMPTION-079 / PRESUMPTION-113 — uniform treatment without precondition tests.
    What would need to be true for C2A2 to be safe: (a) cadence flag on each filing for downstream slicing; (b) precondition test from MONITOR-079 brought current; (c) approval-rate metric reported both pooled and cadence-sliced.
    How to test: Tag the next 10 specialist filings with cadence flag; compute pooled vs. sliced approval rate; if difference exceeds noise threshold, uniform-treatment is empirically refuted for the metric.

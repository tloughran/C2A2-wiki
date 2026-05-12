SEARCH-AGAINST-PRESUMPTION-112:
  Date searched: 2026-05-09
  Original item: PRESUMPTION-112
  Original statement: "Deferred items of differing work-character presumed structurally similar for 'weekend-or-Monday' disposition"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-112
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from 2026-05-08 deferred-item disposition
      15b: Searched for counter-evidence on undifferentiated-disposition slowing higher-leverage items
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes (moderate)

  Sources:
    1. Reinertsen (2009) — once work-character variance is observable, undifferentiated treatment slows high-leverage items; literature explicitly flags this as cost-of-delay leakage.
    2. Anderson (2010) Kanban — work-character classes (CD, expedite, fixed-date) endorse explicit class-based disposition; "structural similarity" presumption is challenged when class differs.
    3. Queueing-theory literature (Kleinrock 1975) — undifferentiated FIFO treatment of mixed-priority streams is empirically suboptimal vs. priority-aware; literature flags this as standard tradeoff.
    4. Goldratt (1984) "The Goal" — bottleneck-aware disposition outperforms undifferentiated date-axis disposition for high-leverage items.
    5. C2A2-internal: ASSUMPTION-079 / ASSUMPTION-091 / PRESUMPTION-113 — pattern of uniform-treatment-without-character-differentiation; companion items inherit same gap.

  Strength of challenge: Moderate

  Summary: Structural similarity for date-axis disposition is canonical default but is challenged when work-character variance is observable. Kanban / flow / queueing / cost-of-delay literatures all endorse class-based disposition once character differs. The "weekend-or-Monday" axis is fine for date-axis decisions; treating differing-character items as structurally similar for this disposition leaks cost-of-delay on the high-leverage items.

  Specific risks: (a) Cost-of-delay leakage on high-leverage items; (b) class-mixing degrades downstream metrics; (c) compounds with ASSUMPTION-091 (uniform on-cadence treatment) — uniform-treatment cluster.

  Mitigations available: (a) Tag deferred items with class label; (b) class-based disposition (high-leverage = different rule); (c) cost-of-delay calculation per item.

  Recommendation: PARTIALLY-CHALLENGED (date-axis uniformity is canonical default; observable character difference is the standard guard, currently absent)

  STEELMAN:
    Item: PRESUMPTION-112
    Strongest counterargument: Work-character variance is observable and material; treating differing-character items as structurally similar for disposition decisions leaks cost-of-delay. Kanban / queueing / flow literatures all endorse class-based disposition when character differs. The presumption forecloses the very class-differentiation step that mature flow management requires.
    What would need to be true for C2A2 to be safe: (a) class-tagging on deferred items; (b) class-aware disposition rule; (c) cost-of-delay calculation per item.
    How to test: Tag the next batch of deferred items with class labels; compare uniform-disposition outcome vs. class-aware disposition; if class-aware reduces cost-of-delay on high-leverage items, presumption is empirically refuted.

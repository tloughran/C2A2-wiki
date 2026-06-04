SEARCH-AGAINST-ASSUMPTION-248:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-248
  Original statement: Janitor's 5 dropped checks (orphan/sparse, unreferenced-images, frontmatter-schema-drift, empty-section, dead-end-wikilink) were deliberate design choices, surfaced rather than skipped silently. Easy to add later.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-248
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on "easy to add later" sandbagging and re-introduction friction.
    Current status: PARTIALLY-CHALLENGED (Weak-Moderate)

  Challenging evidence found: Partial

  Sources:
    1. Cunningham (1992) "WyCash" — Tech-debt literature explicitly identifies "easy to add later" as a documented under-estimate; cost-of-re-introduction is reliably higher than original-implementation cost.
    2. Brooks (1975) — "Easy" classifications at design time are systematically optimistic; the literature notes the integration-cost dimension.
    3. Cockburn (2002) "Agile Software Development" — Documents the deferred-feature accrual pattern: each "deferred but easy" item accumulates with low per-item visibility.
    4. Fowler (1999) — Refactoring literature notes that linter check-set additions involve calibration cost (false-positive tuning); "easy to add" doesn't always survive contact with real wiki state.
    5. C2A2-internal: PRESUMPTION-248 (defer-as-bottleneck-relabel) already validated as a pathology — the same pattern could attach here.

  Strength of challenge: Weak-Moderate

  Summary: The "easy to add later" classification is documented as the precise place where deferred features accumulate as debt. Cunningham, Brooks, and Cockburn all note that the re-introduction cost includes calibration of false-positives, integration into the existing check-set, and ordering relative to other checks. None of these are zero. The "deliberate design choice" framing is supported (15a); the "easy to add later" framing is what the literature consistently warns against.

  Specific risks: (a) Five deferred checks accumulate without trigger to revisit; (b) re-introduction cost is documented to grow as the Janitor pipeline complexifies; (c) PRESUMPTION-248 defer-as-bottleneck-relabel pattern can attach to "easy" deferrals; (d) the 5-check list becomes a fossilized "won't fix" rather than a deferred backlog.

  Mitigations available: (a) Set explicit re-add trigger criteria (e.g., wiki-state threshold, post-ISME); (b) keep dropped-checks as numbered backlog items rather than free-text; (c) audit re-add cost periodically; (d) reject "easy to add later" without an estimated cost.

  Recommendation: PARTIALLY-CHALLENGED (Weak-Moderate)

  STEELMAN:
    Item: ASSUMPTION-248
    Strongest counterargument: "Easy to add later" is precisely the canonical language tech-debt literature flags as systematic under-estimate. Cunningham's tech-debt framework, Brooks's prediction-cost discussions, and Cockburn's deferred-feature accumulation all warn that re-introduction is the under-budgeted dimension. C2A2's own PRESUMPTION-248 (defer-as-bottleneck-relabel) is validated; the same pattern can attach to deferred Janitor checks unless a re-add trigger exists.
    What would need to be true for C2A2 to be safe: Each dropped check has an explicit re-add trigger criterion + estimated re-introduction cost; revisited at least quarterly.
    How to test: Audit dropped-checks list quarterly; track re-add cost; flag any check past 90 days without revisit.

SEARCH-AGAINST-PRESUMPTION-321:
  Date searched: 2026-06-08
  Original item: PRESUMPTION-321
  Original statement: [inferred] The system presumes "automation day" and "attended session" are mutually exclusive day-types (today's attended PRS session was mislabeled "automation-only").

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-321
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as the unstated presumption that two activity-day categories partition cleanly.
      15b: Searched for evidence that the binary day-type taxonomy is incomplete and that mislabeling distorts downstream metrics.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. MECE / taxonomy-completeness (Minto). — A two-bucket partition is valid only if mutually exclusive AND collectively exhaustive; an attended session on a nominal automation day is a direct overlap case, so the categories are not mutually exclusive. The framework that licenses binaries is the same one that flags this one as broken.
    2. Classification-under-partial-information / forced-choice bias. — Forcing an overlapping or unknown case into one of two buckets systematically mislabels it; the standard fix is a non-exclusive tag model or an explicit residual, not a coerced binary.
    3. Label-noise-distorts-metrics literature (Frénay & Verleysen 2014, "Classification in the Presence of Label Noise: A Survey"). — Systematic mislabeling biases every downstream aggregate computed over the labels; an "attended" day counted as "automation-only" silently corrupts activity/utilization metrics and any analysis built on them.

  Strength of challenge: Moderate (low-stakes item)

  Summary: The binary "automation day vs attended session" fails the mutual-exclusivity test — the observed case is a day that is both — so the taxonomy is not MECE. Forcing the overlap into one bucket mislabels it, and systematic mislabeling biases downstream activity metrics (label-noise effect). The challenge is solid but the stakes are low; this is a tidy-up, not a risk.

  Specific risks: Activity/utilization metrics and any "what kind of day was this" analytics are quietly biased by miscounted days; over time the mislabeling could distort the very record of how attended vs automated the project's work has been — minor but real measurement corruption.

  Mitigations available: Replace the exclusive binary with non-exclusive tags (a day may carry both "attended" and "automation-ran"); or add an explicit "mixed" category; backfill the mislabeled 2026-06-07 day; treat day-type as a derived property of what actually happened, not a pre-assigned label.

  STEELMAN:
    Item: PRESUMPTION-321
    Strongest counterargument: The categories were treated as a clean partition when they are actually orthogonal dimensions — "was a human attending?" and "did automation run?" can both be true — so any forced binary will mislabel the overlap and quietly bias every metric computed over day-type. It is a small error, but it is the kind that compounds invisibly in longitudinal data because no one re-examines a label once assigned.
    What would need to be true for C2A2 to be safe: Day-type is modeled as non-exclusive tags (or includes a mixed category), derived from actual activity rather than pre-assigned, so overlap days are counted correctly.
    How to test: Check whether the activity log can represent a day that is both attended and automation-running; if not, the taxonomy forces the mislabel.

  Recommendation: CHALLENGED

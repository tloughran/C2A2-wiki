SEARCH-FOR-PRESUMPTION-407:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-407
  Original statement: "That OpenStory's 06:15 quiet window is reliably and durably quiet - settling for a fix unverified at peak presumes stable, time-predictable churn"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-407
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: durable quietness of the chosen window presumed without peak verification
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Workload-periodicity / diurnal-seasonality literature. - Many workloads have stable, repeating daily troughs, so an empirically chosen off-peak window is often quiet enough for batch work.
    2. Off-peak batch-scheduling practice. - Scheduling against historically low-activity windows is a standard and frequently reliable operational choice.

  Strength of support: Weak

  Summary: There is real but limited support: workloads commonly exhibit stable diurnal troughs, so 06:15 may in practice be quiet most days. To that extent the posture is reasonable. However, the support is for "often quiet," not "reliably and durably quiet"; the literature does not warrant treating an empirical quiet window as a guarantee, and the durability claim is the weak point (see 15b).

  Caveats: Support is probabilistic, not a guarantee. Quietness can drift as agents/schedules/timezones change. Robust safety comes from fail-loud verification, not from presumed window stability.

  Search scope: Workload periodicity; off-peak scheduling reliability. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

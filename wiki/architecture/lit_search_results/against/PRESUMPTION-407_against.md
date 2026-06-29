SEARCH-AGAINST-PRESUMPTION-407:
  Date searched: 2026-06-27
  Original item: PRESUMPTION-407
  Original statement: "That OpenStory's 06:15 quiet window is reliably and durably quiet - settling for a fix unverified at peak presumes stable, time-predictable churn"

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-407
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference: durable quietness of the window presumed; fix unverified at peak
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Non-stationarity of workloads. - Diurnal patterns drift as agents, schedules, timezones (DST), and ad-hoc human sessions change; an empirically quiet window can silently stop being quiet, so "durably quiet" is unwarranted.
    2. Probabilistic mitigation masquerading as guarantee. - Verifying a fix only in the easy (quiet) condition leaves the failure mode untested under load; this is the same intermittent-fault masking pattern as ASSUMPTION-375.
    3. Fail-safe design principle. - Safety should not depend on an environmental assumption (quietness) that can change without notice; correctness should be method-based, not window-based.

  Strength of challenge: Moderate-Strong

  Summary: The presumption treats an empirical quiet window as a stable invariant. Workloads are non-stationary, so quietness can erode without warning, and a fix validated only at 06:15 is untested at peak - precisely where the original torn copies occurred. The robust posture is a method that is correct regardless of contention (snapshot-API copy + completeness validation), with the quiet window kept only as defense-in-depth, not as the guarantee.

  Specific risks: The window stops being quiet (new schedules/agents); torn copies recur unverified-at-peak; an environmental assumption silently invalidates the fix.

  Mitigations available: Make the read correct under contention (backup API + count/checksum reconciliation, fail loud); monitor actual write-activity in the window and alarm if it rises; periodically validate at peak.

  STEELMAN:
    Item: PRESUMPTION-407
    Strongest counterargument: Pinning correctness to "06:15 is quiet" outsources safety to a non-stationary environmental property; the day it drifts, the fix silently regresses, and because it was never tested at peak nobody knows the margin - a guarantee built on luck.
    What would need to be true for C2A2 to be safe: Either the read is correct independent of contention, or write activity in the window is monitored and the fix is periodically verified at peak.
    How to test: Instrument write rate at 06:15 over time; run the read under deliberate peak load and confirm no torn copies.

  Search scope: Workload non-stationarity; off-peak reliability; fail-safe design. Comprehensive.

  Recommendation: CHALLENGED

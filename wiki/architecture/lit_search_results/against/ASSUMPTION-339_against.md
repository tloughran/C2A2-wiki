SEARCH-AGAINST-ASSUMPTION-339:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-339
  Original statement: "Excluding system + inbox pages, the 76.8% orphan rate is an artifact and the genuine reconnection surface is small"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-339
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as the reframe that retires a standing orphan alarm
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Researcher-degrees-of-freedom / motivated reasoning (Experimentology ch.11; preregistration literature). - Defining the exclusion AFTER seeing the orphan count is the textbook condition under which scope choices skew toward the preferred conclusion.
    2. Goodhart / metric-gaming. - Reclassifying 2,112 pages out of the denominator is a denominator-shrinking move that can make an alarm vanish without any structural change.
    3. Orphan-metric robustness (arXiv 2306.03940). - Orphan conclusions are sensitive to namespace-boundary choices; the literature wants those boundaries pre-registered, not chosen post-hoc.

  Strength of challenge: Moderate

  Summary: The challenge is to the EPISTEMICS of the reframe, not the arithmetic. Excluding 2,112 pages to shrink a 76.8% orphan rate is exactly the kind of post-hoc, results-aware scope choice that motivated-reasoning research warns produces conclusions the analyst wants. Without a pre-registered, independently-justified criterion for which page classes 'should not carry backlinks', the reclassification cannot be distinguished from alarm-erasure. The orphan-metric literature explicitly flags this category-boundary sensitivity.

  Specific risks: A real connectivity problem could be defined out of existence, retiring a standing human-tracked alarm on the strength of a self-serving denominator change.

  Mitigations available: Pre-register the exclusion criterion; report orphan rate BOTH ways (with and without exclusions); have the criterion reviewed before it retires the alarm.

  STEELMAN:
    Strongest counterargument: If 'system + inbox' pages are independently, structurally non-content (e.g., by namespace, decided before the count), then excluding them is principled and the reframe stands.
    What would need to be true for C2A2 to be safe: The exclusion rule must be justifiable without reference to its effect on the orphan number.
    How to test: Would the same exclusion have been chosen before the count was known? Check against a pre-stated namespace policy.

  Search scope: motivated reclassification; metric scope robustness. Comprehensive.

  Recommendation: CHALLENGED


---

SEARCH-AGAINST-ASSUMPTION-339 (RE-TRIGGER cycle 1):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-339
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-339
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..0: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 1, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-1 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (CHALLENGED)

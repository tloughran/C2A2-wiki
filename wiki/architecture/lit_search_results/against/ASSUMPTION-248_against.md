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


---

SEARCH-AGAINST-ASSUMPTION-248 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-248
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-248
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15b (cycle 3, 2026-06-30): re-searched for challenging literature
    Current status: refresh; no new challenging literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new challenging literature has surfaced in the week(s) since the last cycle. The prior cycles' challenge profile stands.

  Sources (new / refreshed): No new sources this cycle.

  Strength of challenge: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The challenging literature base has not materially shifted; no new disconfirmatory sources surfaced during this automated cycle.

  Specific risks: Unchanged from prior cycle.

  Mitigations available: Unchanged from prior cycle.

  STEELMAN: Carried forward from prior cycle (no new counterargument surfaced this cycle; strongest prior challenge stands as previously recorded).

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Weak-Moderate))

SEARCH-FOR-ASSUMPTION-230:
  Date searched: 2026-05-27
  Original item: ASSUMPTION-230
  Original statement: When Gmail decision-email body and review-page state disagree about proposal-approval values, the review-page state (verified by direct paste + Tom's verbal confirmation) is authoritative; the email body is non-authoritative until the decision-email generator is fixed.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-230
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-26 attended approval session.
      15a: Searched for supporting literature on data-source authority hierarchies and system-of-record selection.
    Current status: SUPPORTED (Strong)

  Sources:
    1. Kimball & Ross (2013) "The Data Warehouse Toolkit" — explicit system-of-record selection is required when redundant channels exist; derived views (like emails) are NOT authoritative.
    2. Fowler et al. (2001) PEAA — "Single Source of Truth" pattern: when channels diverge, the closest-to-write-path channel is canonical.
    3. ISO 27001 / data-governance literature — audit-trail authority follows the system-of-record principle; secondary notifications are advisory.
    4. C2A2-internal: the review page IS the write target; the email is a derived notification — selection logic matches industrial standard.

  Strength of support: Strong

  Summary: Selecting the system-of-record over derived notifications when they diverge is the dominant data-governance pattern. The review page is the actual write target; the email is a derived view. The assumption matches industrial best practice; the verbal-confirmation step adds an additional verification layer that exceeds minimum.

  Caveats: (a) Support is for selecting authoritatively between two existing channels; (b) when BOTH the email AND the UI mislead (the 3-Wright case — PRESUMPTION-254), this rule alone is insufficient; (c) the "until fixed" qualifier is important — the right long-run remedy is generator alignment, not perpetual UI-priority.

  Recommendation: SUPPORTED (Strong)


---

SEARCH-FOR-ASSUMPTION-230 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-230
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-230
    Item type: ASSUMPTION
    Transform at each step:
      cycle 0..2: prior search/disposition cycles (see blocks above)
      15d (2026-06-28): re-triggered on weekly cadence (catchup run; next_check elapsed)
      15a (cycle 3, 2026-06-30): re-searched for supporting literature
    Current status: refresh; no new supporting literature surfaced this cycle.

  Run context: Clean weekly drain via the c2a2-lit-search-pipeline scheduled task (15a/15b/15c), running one hour after the 14a/14b self-awareness pipeline. Cohort re-triggered by 15d on 2026-06-28 (weekly catchup — first 15d fire since 2026-06-07; the 06-14 and 06-21 weekly runs did not fire, so the 06-28 run drained the accumulated due cohort). This 15a/15b/15c run processes that 147-item re-trigger cohort (124 carry-over weekly items at cycle 3 + 23 newer weekly items at cycle 1).
  Landscape check: Automated landscape spot-check this cycle (6 genuine web searches across distinct clusters: Goodhart's-law / surrogate-metric validity (count-rate as a productivity proxy); git pull --rebase --autostash safety on dirty / untracked working trees; dashboard data-freshness / staleness observability and per-widget as-of timestamps; human-in-the-loop quality-gate routing vs blanket deferral; SMS-OTP / passwordless authentication security momentum (NIST SP 800-63-4; UAE/India/Philippines 2026 deprecation deadlines); multi-agent LLM consensus / idealist-convergence). Security cluster reaffirmed STABLE-but-STRONG (anti-SMS-OTP regulatory momentum continues; NIST SP 800-63-4 excludes SMS OTP from AAL2). All other clusters reaffirmed prior for/against profiles; no disposition-flipping literature shift detected. Spot-check is a sample, not an exhaustive per-item search.

  New evidence weighed: No new supporting literature surfaced in the week(s) since the last cycle. The prior cycles' supportive findings stand.

  Sources (new / refreshed): No new sources this cycle.

  Strength of support: Unchanged from prior cycle.

  Summary: Cycle-3 refresh confirms the prior cycle's finding. The supporting literature base has not materially shifted; no new supportive sources surfaced during this automated cycle. The recommendation carries forward unchanged.

  Caveats: An automated weekly refresh is bounded by the LLM's capacity to surface genuinely new external evidence; operational evidence from the C2A2 runs themselves remains the more sensitive signal for status change.

  Recommendation: refreshed; carry forward prior recommendation (SUPPORTED (Strong))

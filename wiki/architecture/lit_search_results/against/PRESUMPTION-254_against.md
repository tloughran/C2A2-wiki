SEARCH-AGAINST-PRESUMPTION-254:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-254
  Original statement: The "review-page state is authoritative over Gmail" rule presumes the review-page UI is itself reliable, but the 3-Wright follow-up showed the UI also misled within the same session.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-254
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on UI-state failure modes.
    Current status: CHALLENGED (Moderate — challenge supports the presumption)

  Sources:
    1. Nielsen (1993) "Usability Engineering" — UI-state vs underlying-data divergence is canonical HCI failure mode.
    2. Distributed-systems literature (Nygard 2007) — when multiple views diverge, the SoR is the underlying store, not the view.
    3. Audit literature — 3-way reconciliation (intent + UI + email + log) is industrial best practice for approval workflows.
    4. C2A2-internal: the 3-Wright follow-up case is direct empirical evidence.

  Strength of challenge: Moderate (sustains the presumption)

  Summary: The challenge to the presumption is essentially "UI is usually right" — Weak. The presumption's claim (UI can also fail) is empirically demonstrated by the 3-Wright case AND supported by HCI literature.

  Specific risks: (a) Treating UI as reliable in the assumption may delay fixing the deeper generator-divergence; (b) the 2-way rule fails on UI-misfire days.

  Mitigations available: (a) 3-way reconciliation; (b) underlying-store as SoR.

  Recommendation: CHALLENGED (Moderate; presumption sustained)

  STEELMAN:
    Item: PRESUMPTION-254
    Strongest counterargument (to the presumption): UI is right most of the time; treating it as authoritative is a practical heuristic.
    What would need to be true for C2A2 to be safe (if relying on UI-authoritative): UI bug rate must be near zero; the 3-Wright case suggests it is not.
    How to test: Audit UI-vs-store discrepancies over time. >0 means the UI-authoritative rule is unsafe.


---

SEARCH-AGAINST-PRESUMPTION-254 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-254
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-254
    Item type: PRESUMPTION
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

  Recommendation: refreshed; carry forward prior recommendation (CHALLENGED (Moderate; presumption sustained))

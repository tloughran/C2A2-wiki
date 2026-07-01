SEARCH-AGAINST-ASSUMPTION-253:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-253
  Original statement: The Sociogram focus-fade bug is real (foreground focus: l~s -> edges stay lit; isolate computes 185 nodes but the fade does not render), not a hidden-tab testing artifact.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-253
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched single-observation generalization and render-context-variance literature.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Chrome for Developers, 'Background tabs in chrome 57' / 'Timer throttling in Chrome 88' — rAF and chained timers are throttled/suspended in background tabs; a fade that 'does not render' can be a visibility-state artifact rather than a code defect.
    2. MDN, Page Visibility API — documents that hidden documents stop receiving rAF callbacks, the exact mechanism by which a transition-driven fade would silently not run.
    3. Mozilla Bugzilla #731974 — rAF generates anomalously short/long frames especially at animation start, a context-dependent render variance that can masquerade as a logic bug.
    4. General reproducibility methodology: a single foreground observation on one machine/browser is insufficient to exclude a GPU/compositor-specific render fault (couples PRESUMPTION-277).

  Strength of challenge: Moderate

  Summary: The literature on background-tab throttling and rAF frame variance shows that 'the fade does not render' is exactly the signature a visibility/compositor artifact would produce, so a single foreground observation does not by itself exclude a context-bound cause. The claim that it is 'real, not a testing artifact' is plausible but under-determined by one observation.

  Specific risks: If the fade is actually render-context-bound, the planned .attr() fix (ASSUMPTION-254) may not generalize, and the v1.6 hold (ASSUMPTION-255) gates on a misdiagnosis.

  Mitigations available: Reproduce on >=2 browsers/machines in foreground; capture a frame-by-frame trace; confirm opacity attribute value vs rendered pixels.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-253
    Strongest counterargument: The symptom (data path runs, pixels unchanged) is the canonical signature of a compositor/visibility render artifact; absent multi-context reproduction, calling it a 'real code bug' overcommits.
    What would need to be true for C2A2 to be safe: Reproduced in >=2 independent foreground contexts with identical opacity-attr-vs-render divergence.
    How to test: Run the same isolate query in foreground on Chrome+Firefox on two machines; compare computed opacity attr to rendered alpha.


---

SEARCH-AGAINST-ASSUMPTION-253 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-253
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-253
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)

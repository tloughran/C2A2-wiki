SEARCH-AGAINST-PRESUMPTION-281:
  Date searched: 2026-05-30
  Original item: PRESUMPTION-281
  Original statement: [inferred] 'One COLORS line + regen' presumes registration stays cheap at N=33/100 -- palette distinctness, regen time, ~20MB HTML size not examined as scaling costs.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-281
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched regen-on-add / palette-collision costs at scale and self-contained-HTML size limits.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Categorical-color perception (CleanChart; arXiv 2404.03787 'Revisiting Categorical Color Perception') — distinct categorical colors saturate near ~6-12; beyond that hues are not reliably distinguishable, a hard perceptual ceiling well below N=33/100.
    2. Tsitsulin 'Optimal qualitative colour palettes' — even optimized qualitative palettes degrade past ~12-20 categories.
    3. Chrome memory / large-DOM docs + textslashplain 'Browser Memory Limits' — a self-contained HTML already ~26MB grows with N; regen time and tab memory scale with it.

  Strength of challenge: Moderate-Strong

  Summary: Registration is cheap to *type* but not cheap to *scale*: categorical-color distinctness caps near ~10-12, so 'one COLORS line' stops yielding a distinguishable color long before N=33/100; regen output (already ~26MB) and time grow with N. The cheapness presumption ignores a hard perceptual ceiling and growing artifact size.

  Specific risks: At N>~12 new participants are visually indistinguishable; HTML size/regen latency degrade UX and the build loop.

  Mitigations available: Introduce non-color encodings (shape, label, grouping) before ~12; budget regen size/time; consider WebGL/streamed rendering at scale.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-281
    Strongest counterargument: The project's own N=33/100 targets exceed the categorical-color perceptual ceiling, so the current encoding cannot represent them distinctly no matter how cheap the edit is.
    What would need to be true for C2A2 to be safe: A distinct visual encoding exists for N up to target and regen stays within size/time budget.
    How to test: Dry-run register to N=33; measure color distinctness, regen time, HTML size.


---

SEARCH-AGAINST-PRESUMPTION-281 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-281
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-281
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

  Recommendation: refreshed; carry forward prior recommendation (CHALLENGED)

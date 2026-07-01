SEARCH-AGAINST-ASSUMPTION-260:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-260
  Original statement: Adding a participant is a single-source operation: one COLORS line + vault files + regen.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-260
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched regen-on-add scaling cost and fail-loud gaps in registration.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Categorical-color perception literature (CleanChart/arXiv 2404.03787) — distinct categorical colors saturate around ~10-12, so 'one COLORS line' stops yielding a distinguishable color at scale (couples PRESUMPTION-281).
    2. Chrome memory / large-DOM docs — regen produces an ever-larger self-contained HTML (already ~26MB); regen-on-add cost grows with N.
    3. Fail-loud literature — the get_group -> 'root' silent fallback means a mis-registered participant is absorbed silently rather than erroring (couples ASSUMPTION-259).

  Strength of challenge: Moderate

  Summary: The single-source claim is cheap only at small N: the categorical-color budget caps distinct hues near ~10-12, regen output (already ~26MB) and time grow with N, and a silent grouping fallback can swallow a mis-add. 'One line + regen' understates these scaling and fail-loud costs.

  Specific risks: At N>~12 new participants get indistinguishable colors; regen latency/size degrade; silent mis-grouping.

  Mitigations available: Plan non-color encodings beyond ~12; budget regen cost; make grouping fail loud.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-260
    Strongest counterargument: 'Cheap' is scale-relative; the color budget and the silent fallback make 'one line + regen' break before the project's own N=33/100 targets.
    What would need to be true for C2A2 to be safe: Distinct encoding exists for N up to target, regen stays within size/time budget, and mis-adds fail loudly.
    How to test: Add the 13th..33rd participant in a dry run; measure color distinctness, regen time, HTML size, and mis-add behavior.


---

SEARCH-AGAINST-ASSUMPTION-260 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-260
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-260
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

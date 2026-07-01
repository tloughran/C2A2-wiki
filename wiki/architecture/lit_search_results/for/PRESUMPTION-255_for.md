SEARCH-FOR-PRESUMPTION-255:
  Date searched: 2026-05-27
  Original item: PRESUMPTION-255
  Original statement: The per-tradition time model ("hour per top-3, half-hour per long-tail"; ASSUMPTION-233/234) presumes per-tradition processing time scales linearly with file count and is roughly uniform across traditions, but the 12 traditions span very different theoretical complexity.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-255
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced — uniformity presumption in time-budgeting.
      15a: Searched for supporting literature on file-count as adequate first-order proxy for ingest time.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Sources:
    1. COCOMO / Boehm (1981) software-effort estimation — initial first-order estimates by size (LOC or files) are validated as starting points before complexity factors are applied.
    2. Function-Point Analysis (Albrecht 1979) — file/object count is a recognized first-order effort proxy in domain-uniform contexts.
    3. Lean software-effort estimation — within a single workflow, count-based estimates are reasonably accurate when type-variance is bounded.
    4. C2A2-internal: prior tradition-ingest sessions have shown roughly linear file-count scaling within a single tradition.

  Strength of support: Moderate

  Summary: File-count as first-order time proxy is a documented practice (COCOMO basic, function-point analysis) — supportive at the first-order level. The presumption's defense is that the uniformity is a *first-order approximation* good enough for budgeting; the literature supports this.

  Caveats: (a) Support is for first-order, NOT for predicting overruns; (b) all the estimation literature warns that complexity factors should be applied for accuracy, which is exactly what PRESUMPTION-255 surfaces; (c) the support direction here is "file-count IS a usable first-pass proxy" — not "uniformity holds."

  Recommendation: PARTIALLY-SUPPORTED (Moderate; first-order proxy is supported)


---

SEARCH-FOR-PRESUMPTION-255 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-255
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-255
    Item type: PRESUMPTION
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-SUPPORTED (Moderate; first-order proxy is supported))

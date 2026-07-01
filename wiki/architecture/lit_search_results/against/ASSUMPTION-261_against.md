SEARCH-AGAINST-ASSUMPTION-261:
  Date searched: 2026-05-30
  Original item: ASSUMPTION-261
  Original statement: The session-handoff rail (gitignored handoff doc + CLAUDE.md 'read handoff first on resume' rule) fixes next-session resume because CLAUDE.md auto-loads and steers the resume.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-261
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Surfaced/extracted in the 2026-05-29 EOD self-awareness batch.
      15b: Searched stale-doc mis-steer and unreliable instruction-following.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. mem0.ai (2026) — 'if an agent violates a constraint it followed 10 turns ago, the attention weight has dropped below the enforcement threshold'; auto-loaded rules are not reliably honored.
    2. Long-context degradation studies — 11 of 13 LLMs drop below 50% of baseline at 32K tokens even when the needed content is present; a loaded handoff can be present yet ignored.
    3. XTrace handoff article — stale or partial handoff docs actively mis-steer; 'rule will be followed' is unverified without a check.

  Strength of challenge: Moderate-Strong

  Summary: Auto-loading a rule does not guarantee adherence: instruction-following degrades with context length and a stale handoff doc can mis-steer. The word 'fixes' overstates a mechanism that is probabilistic and has no defined failure mode or verification (couples PRESUMPTION-282).

  Specific risks: Resume silently proceeds on a stale/ignored handoff; no detection that the rule was skipped.

  Mitigations available: Add a verification step (handoff freshness check; explicit acknowledgement) and a fail-loud if the rail is skipped.

  Recommendation: PARTIALLY-CHALLENGED

  STEELMAN:
    Item: ASSUMPTION-261
    Strongest counterargument: 'CLAUDE.md auto-loads' guarantees presence, not adherence; the literature shows presence != following, so 'fixes' is unwarranted without a check.
    What would need to be true for C2A2 to be safe: A freshness check + explicit resume-acknowledgement make rule-skip detectable.
    How to test: Run resumes with a deliberately stale handoff; measure how often the rule is followed and whether staleness is detected.


---

SEARCH-AGAINST-ASSUMPTION-261 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-261
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-261
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

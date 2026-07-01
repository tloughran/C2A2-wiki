SEARCH-AGAINST-ASSUMPTION-251:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-251
  Original statement: Three un-numbered DECISION candidates (048 3rd cycle, 049 2nd cycle, AI-search-delegation 1st cycle) constitute a tracking blind spot of its own; registry stops being source of truth.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-251
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on numbering-ceremony as friction-gate.
    Current status: PARTIALLY-CHALLENGED (Weak)

  Challenging evidence found: Partial

  Sources:
    1. Nygard (2011) ADR — The original ADR proposal explicitly notes that numbering ceremony can BE the friction-gate; the assumption locates the failure on the registry side, but Nygard locates it on the ceremony side.
    2. Bass et al. (2021) — Documents that "candidate-tracking blind spot" can mean either (a) registry-discipline-failure OR (b) ceremony-too-heavy; the assumption picks (a) without ruling out (b).
    3. Beck (2002) — YAGNI principle suggests un-numbered candidates may legitimately persist without ceremony; the "blind spot" framing presumes ceremony is owed.
    4. Cunningham (1992) — Tech-debt vocabulary applies if numbering is the deferred work; same vocabulary applies if the decision content is the deferred work.
    5. C2A2-internal: PRESUMPTION-271 directly elaborates this challenge.

  Strength of challenge: Weak

  Summary: The challenge is to the locus, not the existence, of the problem. Nygard's ADR literature, Beck's YAGNI, and Cunningham's tech-debt framework all admit either reading. PRESUMPTION-271 internally elaborates: numbering ceremony may itself be the FLAG-I gate. The assumption's framing ("registry stops being source of truth") presumes the registry is owed the numbering; if numbering ceremony IS the gate, the registry's "source of truth" status survives even un-numbered candidates.

  Specific risks: (a) Locating the failure on the registry side prescribes wrong remediation (more registry discipline) instead of right remediation (lower-friction numbering); (b) repeated cycles of "registry hygiene" pushes don't resolve the underlying ceremony-friction; (c) the blind-spot label can compound the bottleneck.

  Mitigations available: (a) Consider PRESUMPTION-271 framing as equally valid; (b) test both remediations (lower friction OR more discipline); (c) measure whether un-numbered candidates have content-debt or only ceremony-debt.

  Recommendation: PARTIALLY-CHALLENGED (Weak)

  STEELMAN:
    Item: ASSUMPTION-251
    Strongest counterargument: Nygard's original ADR proposal locates the failure mode precisely on the ceremony side, not the registry side. The framing "registry stops being source of truth" presumes the registry is owed the numbering — but if the candidates have stable content and only lack ceremony, the registry is actually doing fine and the friction-gate is the problem. The wrong-side-of-the-failure framing prescribes wrong remediation.
    What would need to be true for C2A2 to be safe: Measure whether un-numbered candidates have content-debt or only ceremony-debt; if only ceremony, reduce friction; if content, then the registry-side framing applies.
    How to test: Audit the 3 candidates — do they have stable, decided content that just isn't numbered? Or are they un-decided? Different framings imply different fixes.


---

SEARCH-AGAINST-ASSUMPTION-251 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: ASSUMPTION-251
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14a
    Chain: [14a->15a,15b->15c->15d->15a,15b->15c]
    Original item: ASSUMPTION-251
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED (Weak))

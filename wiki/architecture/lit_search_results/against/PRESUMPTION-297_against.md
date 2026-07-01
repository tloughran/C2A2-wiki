SEARCH-AGAINST-PRESUMPTION-297:
  Date searched: 2026-06-03
  Original item: PRESUMPTION-297
  Original statement: [inferred] Cross-repo correctness is held by human memory + a handoff doc, not by tooling: the shipped/pushed Day-190 viz (wiki repo) depends on edits left UNCOMMITTED in the separate Summa 2026 repo, with no interlock binding the two.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-297
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated cross-repo dependency with no binding interlock.
      15b: Searched when human handoff notes are an adequate interlock for low-frequency personal workflows; over-tooling cross-repo coordination.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Proportionality / YAGNI for personal single-author workflows (KISS/YAGNI lineage; prior PRESUMPTION-288 FOR). — Distributed-transaction or submodule interlocks are heavy machinery; for one author committing both repos in a session, a handoff note plus a habit can be an adequate, low-overhead interlock.
    2. Cost of cross-repo tooling (GitLab #14311 shows it is non-trivial even for vendors). — Robust cross-repo binding is expensive and itself failure-prone; the cure can exceed the disease for a two-repo personal setup with infrequent coupling.
    3. The coupling is intermittent, not standing. — The viz↔Summa dependency arises only on the specific days both are edited together; a permanent interlock pays cost every day to cover an occasional event, which may be poor ROI.

  Strength of challenge: Weak-Moderate

  Summary: The challenge does not deny the silent-desync hazard (15a establishes it) — it questions whether the named remedy (tooling interlock) is warranted for a single-author, low-frequency, two-repo setup. There, a handoff note plus the habit of committing both repos before push can be a proportionate interlock, and full cross-repo binding is costly and itself failure-prone. The disagreement is about response magnitude, not about whether the exposure exists. The exposure is real but its expected cost here is bounded by low frequency and a single coordinating human.

  Specific risks: Under-reacting leaves the silent-desync exposure (15a) standing — a future push ships depending on uncommitted second-repo edits; over-reacting spends standing tooling cost on an intermittent coupling.

  Mitigations available: Lightweight, not heavy: a pre-push check that the Summa repo has no uncommitted edits when the viz is being pushed (a cheap forcing function), rather than a full distributed-transaction/submodule interlock. This converts "human memory" into a cheap check without over-tooling.

  STEELMAN:
    Item: PRESUMPTION-297
    Strongest counterargument: For a one-person, low-frequency, two-repo workflow, a handoff note plus the habit of committing both repos is an adequate interlock; mandating distributed-transaction-grade cross-repo tooling is over-engineering whose own complexity adds failure modes. The coupling is intermittent, so paying standing coordination cost every day to cover an occasional event is poor ROI.
    What would need to be true for C2A2 to be safe: Coupling stays rare AND the single human reliably commits both repos before push — OR a cheap pre-push "is the other repo clean?" check exists, short of full interlock tooling.
    How to test: Count how often viz pushes actually depend on concurrent Summa edits; if rare, a lightweight pre-push cleanliness check suffices; if frequent, escalate toward submodule/interlock.

  Recommendation: PARTIALLY-CHALLENGED


---

SEARCH-AGAINST-PRESUMPTION-297 (RE-TRIGGER cycle 3):
  Date searched: 2026-06-30
  Original item: PRESUMPTION-297
  Original statement: (see prior cycle for full statement; refreshed only)

  PROVENANCE:
    Origin: 14b
    Chain: [14b->15a,15b->15c->15d->15a,15b->15c]
    Original item: PRESUMPTION-297
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

  Recommendation: refreshed; carry forward prior recommendation (PARTIALLY-CHALLENGED)

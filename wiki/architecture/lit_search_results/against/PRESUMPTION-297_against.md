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

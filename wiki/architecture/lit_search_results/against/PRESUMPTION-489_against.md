SEARCH-AGAINST-PRESUMPTION-489:
  Date searched: 2026-07-17
  Original item: PRESUMPTION-489
  Original statement: Agent outputs are presumed cleanly separable from a shared base; shared working tree lets one agent's churn stall another's commit — no per-agent isolation.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-489
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Augment Code, 2026 & claude-code #55724. — Isolation via git worktrees is a well-known, low-cost fix; the hazard is real but routinely engineered away, so "no per-agent isolation" describes a missing-config state, not an intractable coupling.
    2. Atlassian, "Monorepos in Git." — Many large teams operate shared trees successfully with tooling (sparse checkout, ownership files, CODEOWNERS); shared-tree operation is not inherently broken.
    3. Merge-pipeline / CI research (arXiv 2508.08342). — Commit contention is managed with retry/backoff and PR prioritization; transient lock collisions are expected and recoverable, not fatal.

  Strength of challenge: Moderate

  Summary: The challenge accepts the contention hazard but disputes its severity: worktrees, clones, retry-with-backoff, and ownership tooling are standard, cheap remedies, and shared-tree workflows are viable at far larger scale than C2A2's fleet. The "470-file churn stalls a commit" event is a config/isolation omission with known fixes, not evidence that clean separation is impossible.

  Specific risks: Entanglement makes each commit a review of unrelated changes; occasional stalls until isolation is added.

  Mitigations available: Per-agent worktrees or clones (private index/HEAD); commit retry with exponential backoff; scoped output namespaces.

  STEELMAN:
    Strongest counterargument: The presumption risks over-indexing on one churn event; with retry/backoff most such collisions self-heal in milliseconds, and the durable fix (worktrees) is a half-day change — so the coupling is real but shallow.
    What would need to be true for C2A2 to be safe: Per-agent worktree/clone isolation and/or commit retry policy.
    How to test: Attribute each staged file to its writing run; measure other-agent churn per commit surface.

  Recommendation: PARTIALLY-CHALLENGED

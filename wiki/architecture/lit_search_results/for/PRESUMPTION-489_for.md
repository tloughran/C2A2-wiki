SEARCH-FOR-PRESUMPTION-489:
  Date searched: 2026-07-17
  Original item: PRESUMPTION-489
  Original statement: [inferred] Each agent's outputs are presumed cleanly separable from a shared base at commit time; in fact a shared working tree lets one agent's incidental churn (470-file last_qc_at bumps) stall another agent's commit — no per-agent isolation or output namespace.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-489
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption (outputs presumed separable in a shared tree)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Augment Code, 2026. "Git Worktrees for Parallel AI Agent Execution" & anthropics/claude-code issue #55724. — Multiple agents on a shared repo produce silent overwrites, stale context, and git lock contention; in one test 8 of 13 parallel agents failed to commit. Directly supports "shared tree stalls a commit."
    2. Digma, 2026. "10 Common Monorepo Problems." — Commits in unrelated parts of the tree affect a developer's subtree; monorepos "lack the natural isolation that separate repositories provide."
    3. Atlassian, "Monorepos in Git." — Confirms blurred ownership and change-isolation difficulty at scale in a shared tree.

  Strength of support: Strong

  Summary: The presumption is strongly and specifically supported: the multi-agent tooling literature treats a shared working tree / shared .git as a known hazard, with documented commit failures from one agent's churn colliding with another's. Standard isolation (per-agent worktrees or clones, private index/HEAD) is the recognized remedy.

  Caveats: Worktrees remove index contention but some shared-ref locks remain (retry with backoff advised); full isolation implies separate clones. Support is for the hazard and the remedy, not for any current C2A2 isolation.

  Recommendation: SUPPORTED

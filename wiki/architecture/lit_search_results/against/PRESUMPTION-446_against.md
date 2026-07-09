SEARCH-AGAINST-PRESUMPTION-446:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-446
  Original statement: "[inferred] That scheduled agents and attended sessions can share one git repository with no coordination protocol."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-446
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from observed index.lock/HEAD.lock collisions and the non-fast-forward push rejection that the architecture presumes uncoordinated sharing of one repo is workable
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. anthropics/claude-code Issue #11005, "Stale .git/index.lock files created by CC's background git operations block user git commands." — Direct documented instance of the exact bot-vs-human failure mode C2A2 experienced: agent background git operations leave locks that block the attended user, and stale locks persist with no holding process.
    2. anthropics/claude-code Issue #28823, "Race condition with git index.lock during lint-staged pre-commit failures." — Documents TOCTOU-style races between automated tooling and git's advisory lock in agent workflows; automated retry immediately collides with cleanup.
    3. Augment Code, "Git Worktrees for Parallel AI Agent Execution" / "How to Run a Multi-Agent Coding Workspace" (2026). — Industry guidance states plainly that multiple agents on one repo compete for .git/index.lock, a crashed agent's stale lock "can freeze all progress," and the accepted remedy is worktree isolation plus an explicit coordination contract — i.e., the field has already concluded that no-protocol sharing fails.
    4. Zylos Research, 2026. "Git Worktree Isolation Patterns for Parallel AI Agent Development"; MindStudio, "Git Worktrees for AI Coding" (2026). — Converging 2026 practitioner literature: filesystem isolation (worktrees) + shared task ledger + merge protocol is now the default coordination layer for concurrent AI sessions; running agents directly in one working tree is treated as an anti-pattern.
    5. Lamport, L., 1978. "Time, Clocks, and the Ordering of Events in a Distributed System" (and derived distributed mutual exclusion literature). — Forty-plus years of theory establishing that concurrent writers to a shared resource require an explicit ordering/mutual-exclusion protocol; correctness cannot emerge from timing luck. Git's index.lock is a local advisory mechanism, not a coordination protocol between independent sessions, and it offers no queueing, fairness, or crash recovery.
    6. Microsoft Learn, "Git index.lock file — Azure Repos." — Vendor documentation acknowledging that concurrent tooling touching one repo produces lock contention and prescribing serialization of operations.

  Strength of challenge: Strong

  Summary: This presumption is challenged from three independent directions, which is why the CRITICAL rating is warranted. Theory: distributed mutual exclusion literature since Lamport (1978) establishes that concurrent writers require an explicit coordination protocol; git's lock files are per-operation advisory guards with no inter-session queueing and a known stale-lock failure mode. Documented incidents: the Claude Code issue tracker contains the precise scenario C2A2 hit — background agent git operations colliding with an attended user's commands, stale locks blocking work, races on cleanup. Industry practice: the 2026 multi-agent-coding literature uniformly prescribes worktree isolation plus a shared task/merge protocol, treating uncoordinated single-tree sharing as a known anti-pattern. C2A2's observed symptoms (lock collisions, a lock deleted under uncertainty, a rejected non-fast-forward push) are the textbook presentation of this failure class, not bad luck.

  Specific risks: Lost updates when both writers modify the working tree or index concurrently; repository corruption or half-applied operations if a lock is deleted while genuinely held; silent divergence resolved by force-type actions under deadline pressure; a stale lock from a crashed scheduled agent blocking the attended session at the worst moment; for an evidence-bearing system, history rewrites or lost commits damage the evidentiary chain itself.

  Mitigations available: Git worktrees per writer (each gets its own index; the object store is shared safely); temporal partitioning (scheduled agents run in windows the human agrees not to work in, and check for an attended-session sentinel file before touching git); a simple repo-lock protocol with owner, PID, and timestamp so stale locks are safely distinguishable from live ones; agents commit to their own branches and never push to the human's branch; pull-rebase-push with bounded retry instead of bare push.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-446
  Strongest counterargument: The presumption is refuted not by speculation but by C2A2's own incident log converging with the public record: the same product family (Claude Code) has open issues describing agent-vs-human index.lock collisions and stale-lock freezes, and the 2026 industry consensus is that concurrent agents on one working tree require worktree isolation and an explicit coordination contract. Distributed-systems theory adds that git's advisory locks cannot serve as a coordination protocol because they provide no ordering, no fairness, and no crash recovery between independent sessions — so every uncoordinated overlap is a coin flip whose worst outcomes include lost work and corrupted state. A system whose value proposition is evidentiary integrity is running its evidence store on exactly that coin flip.
  What would need to be true for C2A2 to be safe: Writers never overlap in time (enforced, not hoped), or writers are isolated in space (worktrees/branches) with a defined merge path; and lock removal follows a verified-stale procedure (check holder PID/age) rather than judgment under uncertainty.
  How to test: Deliberately schedule an agent git operation during an attended session in a sacrificial clone and observe the collision; then repeat with worktree isolation and confirm zero contention. Audit git reflog for evidence of past lost or rewritten commits during the incident window.

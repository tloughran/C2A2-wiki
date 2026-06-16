SEARCH-AGAINST-ASSUMPTION-316:
  Date searched: 2026-06-12
  Original item: ASSUMPTION-316
  Original statement: "Session-scoped (provenance-clean) commits keep repository provenance clean and the repo healthy."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-316
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as stated assumption from 2026-06-11 EOD session
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Kawrykow, A. and Robillard, M. P., 2011. "Identifying Meaningful Revisions in Tangled Commits." Proceedings of the 33rd International Conference on Software Engineering (ICSE). — Demonstrates empirically that developers frequently bundle multiple unrelated changes into commits that correspond to work done within a session or time-block. Session-scoped commits, being defined by temporal rather than logical boundaries, are structurally prone to becoming "tangled commits" containing multiple semantic concerns. Provenance cleanliness at the session level does not imply logical atomicity.

    2. Herzig, K. and Zeller, A., 2013. "The Impact of Tangled Code Changes." Proceedings of the 10th Working Conference on Mining Software Repositories (MSR). — Empirically quantifies the cost of tangled commits: they degrade bug prediction model accuracy, obscure code provenance for archaeological purposes, and make selective reversion unreliable. A session-scoped commit containing both a new feature and a config tweak is formally "clean" by provenance (attributed to one session/author) but semantically tangled and harmful to repo health metrics that depend on logical atomicity.

    3. Dias, M., Bacchelli, A., Gousios, G., et al., 2015. "Untangling Fine-Grained Code Changes." Proceedings of the 22nd IEEE International Conference on Program Comprehension (ICPC). — Shows that fine-grained untangling of tangled commits requires substantial post-hoc effort and that early tangling is very difficult to fully reverse. Session-scoped commits create irreversible provenance problems at the logical level that "clean" session attribution does not prevent.

    4. Kirbas, S., et al., 2021. "A Fine-Grained Data Set and Analysis of Tangling in Bug Fixing Commits." Empirical Software Engineering 26(3): 47. — Provides large-scale empirical evidence that a high proportion (>60%) of real-world commits contain tangled changes when measured at the logical-concern level, even when they appear clean at the author/time level. Session-scoped commits from C2A2 agents are subject to the same tangling unless the session includes active untangling discipline.

    5. Ballou, K., 2021. "Granularity of (Git) Commits." Personal technical essay, kennyballou.com. — Articulates the practitioner consensus that commit granularity by logical concern (not by time-slice or session) is the correct principle for repository health. Session-scoped commits are an intermediate, not a solution: they achieve attribution cleanliness (who/when) while potentially failing logical-concern cleanliness (what/why).

  Strength of challenge: Moderate

  Summary: The assumption conflates two distinct senses of "provenance clean": (a) attributed provenance (the session, agent, and timestamp are correctly recorded) and (b) logical provenance (each commit corresponds to exactly one semantic concern). Session-scoping guarantees (a) but not (b). The empirical software engineering literature consistently shows that session/time-bounded commits are a major source of tangled commits, which degrade the very repo health the assumption is meant to protect. For a system where AI agents commit research artefacts, summaries, rung logs, and configuration changes, session-scoped commits may bundle logically distinct changes that should be separately attributable and reversible. The challenge is moderate rather than strong because for a knowledge-management repository (as opposed to a code repository), the cost of tangling is lower and the attribution benefit of session-scoping is real.

  Specific risks: If session-scoped commits bundle rung agreements, data extractions, configuration changes, and narrative edits, rollback and blame operations become unreliable. Provenance claims for specific artefacts (e.g., "this rung was agreed in session X") may be technically correct but practically misleading if the same commit also contains post-session edits that should have been separately attributed.

  Mitigations available: Adopt a two-level commit discipline: (1) session-level commits for attribution provenance (satisfying the session-scoping rule), combined with (2) logical-concern tagging within commit messages that enables retrospective filtering and untangling. Alternatively, use sub-commit branches (session branch → merge with atomic commits) to achieve both goals.

  STEELMAN:
    Strongest counterargument: For a research knowledge base rather than a production code repository, the primary provenance concern is who agreed what and when, not logical atomicity. Session-scoped commits satisfying both "agent X" and "session Y" attributes answer the audit question most relevant to C2A2: was this agreement generated in a provenance-clean session (no cross-session contamination, no out-of-session edits)? The tangled-commits literature applies primarily to code repositories where logical atomicity matters for bug isolation and code archaeology; for a rung-log and wiki system, the audit trail concern may dominate the logical-concern concern.
    What would need to be true for C2A2 to be safe: The primary repo health operations anticipated for C2A2 (audit, rollback, attribution) must be achievable with session-scoped provenance alone, meaning no anticipated operation requires sub-session logical decomposition. If any operation requires reverting a subset of a session's commit (e.g., removing a rung that was erroneously included alongside legitimate rung agreements), session-scoping becomes insufficient.
    How to test: Identify one realistic failure scenario requiring a sub-session rollback (e.g., a rung that was logged in a session but later determined to have been adjudicated rather than genuinely agreed). Check whether session-scoped commits allow selective reversion of that rung without reverting the other session artefacts. If not, the assumption is insufficient for actual repo operations.

  Search scope: Searched for tangled commits empirical studies, commit granularity best practices, session-boundary vs logical-boundary commit strategies, and repo health metrics. Searched primarily software engineering literature; knowledge-management or wiki-specific commit practices were not separately searched.

  Recommendation: PARTIALLY-CHALLENGED

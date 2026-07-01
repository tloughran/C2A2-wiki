SEARCH-FOR-ASSUMPTION-391:
  Date searched: 2026-06-30
  Original item: ASSUMPTION-391
  Original statement: "git pull --rebase --autostash safely handles ~20 unrelated working-tree files, removing the manual stash/pop dance (adopted as standard push pattern, DECISION-072)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-391
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-29 self-awareness cohort (metabolism-axis / liveness / push-pattern review)
      15a: Searched for supporting literature (first-time, genuine web search 2026-06-30)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. git-scm, git-rebase / git-pull documentation — --autostash stashes local modifications before rebase and re-applies them after; an official, supported feature since git 2.6.
    2. Eficode, "Git autostash" — autostash is the recommended way to rebase-pull with a dirty tree for TRACKED changes; removes the manual stash/pop ritual.
    3. cscheng.info, "Git tip: autostash with git pull --rebase" — documents the intended ergonomic win for routine pulls over local edits.

  Strength of support: Moderate

  Summary: For TRACKED modifications, --autostash is a supported, idiomatic feature that does exactly what the assumption claims: it removes the manual stash/pop dance and is git's own recommended mechanism for rebase-pulling over a dirty tree. The ergonomic claim is well grounded for tracked files.

  Caveats: Support is scoped to TRACKED files and to the case where the post-rebase stash-pop applies cleanly. Untracked files and pop-conflicts fall outside this support (see 15b).

  Recommendation: PARTIALLY-SUPPORTED (Moderate — supported for tracked files / clean re-apply; the ~20-unrelated-files claim is conditionally safe)

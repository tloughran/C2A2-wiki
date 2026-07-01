SEARCH-AGAINST-ASSUMPTION-391:
  Date searched: 2026-06-30
  Original item: ASSUMPTION-391
  Original statement: "git pull --rebase --autostash safely handles ~20 unrelated working-tree files, removing the manual stash/pop dance (adopted as standard push pattern, DECISION-072)."

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-391
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-06-29 self-awareness cohort
      15b: Searched for challenging literature (first-time, genuine web search 2026-06-30)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. git-scm git-stash / autostash semantics — --autostash does NOT stash UNTRACKED files by default; untracked files are left in the tree and can collide with incoming changes, so "handles ~20 unrelated files" fails for any untracked subset.
    2. Eficode / sqlpey — the post-rebase stash re-application "might result in non-trivial conflicts"; on conflict the changes remain in the stash and require manual git stash pop/drop, i.e. the manual dance is not actually removed in the failure case.
    3. git/git commit f15e7cf — history shows autostash + fast-forward was itself a latent bug class; autostash interacts subtly with pull strategy.

  Strength of challenge: Moderate-Strong

  Summary: The safety claim is challenged on two concrete points: (1) autostash ignores untracked files, so a tree of ~20 unrelated files is only 'handled' if all are tracked; (2) the post-rebase re-apply can conflict, reinstating exactly the manual stash/pop step the policy claims to remove. The blanket 'safely handles' is too strong.

  Specific risks: Untracked files in the ~20 silently bypass autostash and can be overwritten or block the pull; a pop-conflict mid-rebase leaves the working tree and stash in a state requiring manual recovery — risky in an unattended/autonomous push.

  STEELMAN: In an autonomous scheduled push, the strongest objection is that autostash hides failure: a conflicting pop returns nonzero deep in a pipeline that may not be checking it, so a 'clean win' assumption can mask a silently broken push — the very fail-loud violation PREMISE-086 warns against.

  Recommendation: CHALLENGED (Moderate-Strong — safe only for tracked files with clean re-apply; untracked-file and pop-conflict cases are unhandled)

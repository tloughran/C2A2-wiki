SEARCH-AGAINST-ASSUMPTION-370:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-370
  Original statement: "That a commit can be reliably scoped to the session's own files (12), excluding the 39 agent-WIP files, by manual staging"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-370
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: manual partial staging assumed reliable to scope a commit in a dirty tree
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Reason 1990, "Human Error" (slips/lapses under routine, repeated tasks). - Controls that depend on sustained human attention have an irreducible, nonzero error rate; reliability degrades precisely on routine repetitions like per-commit staging.
    2. Safety-engineering hierarchy of controls / "correct by construction." - Administrative controls (remember to stage the right files) rank BELOW engineering controls (make the wrong files unstageable); a dirty 39-file tree leaves a standing one-`git add -A`-away exposure.
    3. Git worktree/branch isolation docs. - Git provides structural isolation (separate worktree/branch) that removes the WIP files from the staging surface entirely - a correct-by-construction alternative to vigilance.

  Strength of challenge: Strong

  Summary: Manual staging works when done carefully, but "reliably" across many repetitions is exactly what human-error research says vigilance cannot deliver: routine staging in a tree carrying 39 unrelated WIP files is one inattentive `git add -A`/`git commit -a` from leaking them. The hierarchy-of-controls principle is decisive: a structural guard (commit from a clean worktree/branch where the WIP files are not present) eliminates the failure mode that vigilance only reduces. The standing exposure - not any single commit - is the risk.

  Specific risks: Accidental inclusion of 39 agent-WIP files in a commit; history pollution; possible exposure of unfinished/sensitive WIP.

  Mitigations available: Dedicated worktree/branch for the session's 12 files; .gitignore or sparse-checkout to remove WIP from the surface; a pre-commit hook asserting the staged set; commit from a clean checkout.

  STEELMAN:
    Item: ASSUMPTION-370
    Strongest counterargument: "Reliable by manual staging" mistakes possible-when-careful for reliable-in-repetition. With 39 WIP files always present, the safe outcome depends on never slipping once across an unbounded number of commits - which the human-error literature says will eventually fail; the correct fix is to remove the WIP from the staging surface structurally.
    What would need to be true for C2A2 to be safe: The WIP files are not present in the working tree from which commits are made (worktree/branch isolation), OR a pre-commit guard mechanically blocks out-of-scope files.
    How to test: Track accidental-inclusion incidents over N commits; any nonzero rate confirms vigilance is insufficient.

  Search scope: Human error; controls hierarchy; git isolation. Comprehensive.

  Recommendation: CHALLENGED

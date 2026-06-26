SEARCH-FOR-ASSUMPTION-370:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-370
  Original statement: "That a commit can be reliably scoped to the session's own files (12), excluding the 39 agent-WIP files, by manual staging"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-370
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: manual partial staging assumed reliable to scope a commit in a dirty tree
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Git documentation (git add <pathspec>, git add -p, pre-commit verification). - Explicit-pathspec and interactive staging are first-class, supported mechanisms for committing a subset of a dirty tree; the workflow exists and works when followed.
    2. Practitioner guidance on focused/atomic commits. - Disciplined explicit staging plus a pre-commit `git diff --cached` review is an endorsed way to keep commits scoped.

  Strength of support: Weak

  Summary: Manual partial staging is a legitimate, documented Git workflow and can reliably scope a commit WHEN the operator stages explicit paths and reviews the cached diff before committing. Tooling support (pathspecs, `add -p`, `diff --cached`) makes the per-commit task achievable. The support is for feasibility-under-discipline; it says nothing about the error rate of repeating that discipline every time in a 39-file dirty tree, which is where 15b concentrates.

  Caveats: Reliability is contingent on consistent operator vigilance and a pre-commit review step. "Works when done carefully" is not the same as "reliable across many repetitions."

  Search scope: Git staging workflows; atomic-commit practice. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

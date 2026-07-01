SEARCH-AGAINST-PRESUMPTION-424:
  Date searched: 2026-06-30
  Original item: PRESUMPTION-424
  Original statement: "That auto-stashing ~20 unrelated working-tree files every push is safe and a clean win — normalizes a chronically dirty working tree instead of resolving the persistent uncommitted files (push-debt)."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-424
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference
      15b: Searched for challenging literature (first-time, genuine web search 2026-06-30)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. git hygiene / trunk-based development practice — a chronically dirty working tree (~20 persistent uncommitted files) is itself the defect; autostash masks it rather than resolving it, entrenching latent debt.
    2. git-scm autostash semantics — untracked files are not stashed and pop can conflict, so "safe clean win" is false for the untracked/conflict subset (shared with A-391).
    3. C2A2-internal: continuation of PRESUMPTION-412 / REVISE-150 (deferred pushes accumulate rather than converge) and the push-debt family; normalizing the dirty tree is the working-tree analogue of deferred-push accumulation.

  Strength of challenge: Moderate-Strong

  Summary: Moderate-strong challenge: the presumption reframes a defect (a chronically dirty tree of ~20 unrelated files = push-debt) as a 'clean win' by automating around it. Autostash hides the underlying uncommitted-files problem, can fail silently on untracked/conflict cases, and entrenches the debt. This is the working-tree form of the already-flagged deferred-push-accumulation problem.

  Specific risks: The ~20 persistent files never get resolved (committed, ignored, or removed); they ride along every push, occasionally conflicting or being silently bypassed; the dirty state becomes invisible normal.

  STEELMAN: If the ~20 files are intentional local-only artifacts (caches, local config), autostash-per-push is a pragmatic accommodation and 'resolving' them might mean just .gitignore-ing them — i.e., the debt may be cheap to retire, which strengthens the case to retire it rather than automate around it.

  Recommendation: CHALLENGED (Moderate-Strong — automating around a chronically dirty tree normalizes push-debt; mechanism convenience does not justify the habit)

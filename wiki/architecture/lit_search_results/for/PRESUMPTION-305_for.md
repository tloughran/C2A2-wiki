SEARCH-FOR-PRESUMPTION-305:
  Date searched: 2026-06-05
  Original item: PRESUMPTION-305
  Original statement: [inferred] Accumulating uncommitted working-tree state is cost-free — 587 changes (up from 476) on feature/sociogram-search-integration, each unattended run adding to the pile under the no-blind-push rule, presuming a future attended session cleanly separates and commits them.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-305
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as an unstated presumption that accumulating uncommitted working-tree state is cost-free and cleanly separable later.
      15a: Searched for any literature SUPPORTING deferral of commits / long-lived branch accumulation as low-cost.
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. (Sole partial-support thread) Atlassian, "Trunk-Based Development." — The only defensible support is the no-blind-push safety rationale: deferring a PUSH until an attended review is legitimate version-control hygiene. But note this supports deferring the *push/merge*, not letting the *uncommitted working tree* grow — the literature recommends frequent local commits even when pushes are gated.
    2. trunkbaseddevelopment.com, "Short-Lived Feature Branches." — Provides no support for cost-free accumulation; the closest supportive reading is that a branch held briefly is fine — but it caps "briefly" at roughly two days, far short of the multi-run accumulation described here.

  Strength of support: Weak

  Summary: A genuine supportive literature for "accumulating uncommitted working-tree state is cost-free" essentially does not exist; the search surfaced predominantly counter-evidence (routed to 15b). The only honestly supportive fragment is narrow and partial: gating the PUSH (not committing) under a no-blind-push safety rule is sound practice. Crucially, that fragment supports deferring the network operation, NOT letting hundreds of uncommitted changes pile up in the working tree — standard guidance is to commit frequently in small increments locally and defer only the push. So the presumption as stated (accumulation itself is cost-free) finds no real grounding; the safety value attaches to a different action (gated push) than the one being defended (unbounded working-tree growth).

  Caveats: Because the supportive case is so thin and the topic is well-studied, this is close to a clean NO-SUPPORT-FOUND rather than a literature gap / NOVELTY. The distinction matters for 15c: this is not an untested novel idea, it is a claim the literature actively weighs against.

  Recommendation: NO-SUPPORT-FOUND

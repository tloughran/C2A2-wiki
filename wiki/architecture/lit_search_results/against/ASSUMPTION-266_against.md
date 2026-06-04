SEARCH-AGAINST-ASSUMPTION-266:
  Date searched: 2026-06-03
  Original item: ASSUMPTION-266
  Original statement: Git staging in the wiki repo must use explicit file paths, never `git add -A`, because the tree perpetually carries unrelated modified Summa-vault-sync files; explicit-path staging prevents committing unintended changes.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-266
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from explicit-path staging discipline adopted to avoid Summa-sync churn.
      15b: Searched for when the perpetually-dirty tree is itself the defect (separate repos / .gitignore / submodules) rather than worked around by explicit-path staging.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Root-cause vs workaround principle (general SE + the GitLab #14311 cross-project discussion). — Explicit-path staging treats the symptom; the underlying defect is that two unrelated projects share one working tree. `.gitignore`, separate repos, or submodules remove the dirt at the source so ANY staging command is safe.
    2. Human-discipline-as-control is fragile (fail-loud / forcing-function lineage in this register; PagerDuty alert-fatigue literature). — "Always remember to type explicit paths" is an unenforced manual convention; one `git add -A` or `git commit -a` reflex re-admits the exact failure. Controls that depend on human memory are the weakest tier (hierarchy of controls).
    3. Explicit-path staging has its own failure mode (git-add docs: untracked/new files). — Explicit paths can MISS newly-created intended files (no `-A` to catch them), trading "commit too much" for "commit too little" — a silent omission that is harder to notice than an over-broad commit.

  Strength of challenge: Moderate

  Summary: The challenge does not dispute that explicit-path staging avoids committing the Summa-sync churn; it disputes that the assumption identifies the right fix. A perpetually-dirty tree is itself the defect, and the structural remedies (`.gitignore`, separate repos, submodules) eliminate the hazard rather than routing around it with a manual convention that depends on never forgetting. Worse, explicit-path staging introduces a complementary silent failure — newly-created intended files can be omitted — so the discipline trades a visible over-commit risk for a quieter under-commit risk. This couples the run's recurring theme: controls that rely on human memory rather than forcing functions.

  Specific risks: A single reflexive `git add -A`/`commit -a` commits Summa churn; OR explicit-path staging silently omits a new intended file, shipping an incomplete commit. Both persist because nothing enforces the convention.

  Mitigations available: Fix the source: add the Summa-sync paths to `.gitignore` (or split the repos / use a submodule) so the tree is clean and staging is safe regardless of command; add a pre-commit check that the staged set matches the intended file list (forcing function, not memory).

  STEELMAN:
    Item: ASSUMPTION-266
    Strongest counterargument: The assumption fixes the visible symptom but enshrines a manual, memory-dependent control over a structural defect (two projects in one tree). The robust engineering move is to remove the dirt at the source via `.gitignore`/separate repos/submodules, after which the "never use `git add -A`" rule is unnecessary; keeping the rule instead leaves a standing trap and adds a new silent-omission failure mode for new files.
    What would need to be true for C2A2 to be safe: Either the dirt source is removed (clean tree), OR the explicit-path set is generated/checked by tooling each run (not typed from memory) AND a check confirms no intended new file was omitted.
    How to test: Inspect whether Summa-sync paths can be `.gitignore`d or split out; if yes, the structural fix dominates. Audit recent commits for any omitted-new-file incidents to size the under-commit risk.

  Recommendation: PARTIALLY-CHALLENGED

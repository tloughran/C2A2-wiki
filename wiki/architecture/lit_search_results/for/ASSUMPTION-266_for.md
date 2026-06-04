SEARCH-FOR-ASSUMPTION-266:
  Date searched: 2026-06-03
  Original item: ASSUMPTION-266
  Original statement: Git staging in the wiki repo must use explicit file paths, never `git add -A`, because the tree perpetually carries unrelated modified Summa-vault-sync files; explicit-path staging prevents committing unintended changes.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-266
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the Sociogram engineering session — explicit-path staging discipline adopted to avoid committing unrelated Summa-sync churn.
      15a: Searched least-privilege/explicit-intent commit practice and hazards of `git add -A` in dirty trees.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Git official docs, git-add (git-scm.com/docs/git-add) and GitHub git-guides "git add". — Document `-A`/`.` as staging everything not ignored; the granular forms (explicit paths, `git add -p`) are presented as the controlled alternative when only some changes should be committed.
    2. Atwood/HN practitioner consensus thread (news.ycombinator.com/item?id=12886492) + multiple how-to guides (Graphite, codegenes, Medium/Mullatoez). — Broad practitioner agreement that `git add -A` in a tree containing unrelated/sensitive/binary files risks accidental staging; "prefer explicit paths" and "review with git status first" are stated best practices.
    3. Least-privilege / explicit-intent commit principle (general SE practice; same family as the fail-loud/verify register). — Staging only what you intend is the version-control analogue of least privilege: it bounds the blast radius of a commit to declared files.

  Strength of support: Strong

  Summary: The assumption restates a well-established version-control best practice: in a working tree that perpetually carries unrelated modifications (here, Summa-vault-sync files), explicit-path staging is the standard way to guarantee a commit contains only intended changes. Official docs and a strong practitioner consensus treat `git add -A` as convenient but hazardous in dirty trees, and recommend explicit paths or interactive staging plus a `git status` review. The C2A2 condition (a chronically dirty tree) is exactly the case where the best practice most clearly applies.

  Caveats: The literature frames explicit-path staging as a workaround; several sources note the cleaner long-run fix is to remove the dirt source (separate repos, `.gitignore`, submodules) so the tree is not perpetually dirty — see 15b. Support is for the staging discipline, not for treating a perpetually-dirty tree as acceptable.

  Recommendation: SUPPORTED

SEARCH-FOR-ASSUMPTION-506:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-506
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Low)
  Original statement:
    Phase-6 was not pushed for three converging reasons (no credentials; No-Blind-Push HTML rule; git-add-
      wiki clobber risk); the remedy is selective staging on the Mac.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-506
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from the 2026-07-22 daily run Phase 6
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Search scope: WebSearch, 2026-08-30, clustered query — "generated artifacts in version control; selective staging; blanket `git add` clobber risk". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Supporting evidence found: Yes

  Sources:
    1. Ernst, M. "Version control concepts and best practices" (UW). — do not version generated files; a
       small source change can produce a large derived diff.
    2. QA of Code for Analysis and Research (UK Gov). "Version control." — .gitignore build artifacts; keep
       the repository to source.
    3. IT Security Guru. "Why Some Source Code Files Shouldn't Be Managed via Git-Based Version Control." —
       blanket `git add .` is the named mechanism for committing unintended files.

  Strength of support: Moderate-Strong

  Summary:
    Version-control guidance directly supports both the diagnosis and the remedy. Generated files should not
      be versioned: a small source change can produce a large derived diff, and binary artifacts are stored
      whole per revision. Blanket `git add .` is named as the mechanism by which unintended files enter a
      repository. Selective staging plus a maintained .gitignore is the standard remedy, and separating
      source from build output is the underlying principle.

  Caveats:
    Sources are practitioner and course-note grade. The literature endorses selective staging as routine
      hygiene; it does not speak to a workflow where an unattended agent produces artifacts an attended
      session must later commit, which is where this item's risk actually sits.

  Recommendation: SUPPORTED

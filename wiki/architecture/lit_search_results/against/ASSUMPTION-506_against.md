SEARCH-AGAINST-ASSUMPTION-506:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-506
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Low)
  Original statement:
    Phase-6 was not pushed for three converging reasons (no credentials; No-Blind-Push HTML rule; git-add-
      wiki clobber risk); the remedy is selective staging on the Mac.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-506
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from the 2026-07-22 daily run Phase 6
      15b: Searched for challenging literature
    Current status: NO-CHALLENGE-FOUND

  Search scope: WebSearch, 2026-08-30, clustered query — "generated artifacts in version control; selective staging; blanket `git add` clobber risk". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Challenging evidence found: No

  Sources:
    1. Ernst, M. "Version control concepts and best practices" (UW). — do not version generated files; a
       small source change can produce a large derived diff.
    2. QA of Code for Analysis and Research (UK Gov). "Version control." — .gitignore build artifacts; keep
       the repository to source.
    3. IT Security Guru. "Why Some Source Code Files Shouldn't Be Managed via Git-Based Version Control." —
       blanket `git add .` is the named mechanism for committing unintended files.

  Strength of challenge: None

  Summary:
    No challenge to selective-staging discipline was retrieved. The challenge direction did not receive a
      dedicated query for this item; the null is procedural, not substantive.

  STEELMAN:
    [CONSTRUCTED, not retrieved] three converging reasons for one non-action is over-determination. If
      credentials alone block the push, the HTML rule and clobber risk are post-hoc, and the selective-
      staging remedy addresses a cause that was never load-bearing. Fixing it would leave the push still
      blocked.

  Recommendation: NO-CHALLENGE-FOUND

SEARCH-FOR-ASSUMPTION-494:
  Date searched: 2026-08-30
  Original item: ASSUMPTION-494
  Queue ref: for_lit_search.md — 2026-07-21 EOD batch (Priority Medium)
  Original statement:
    The inbox-diff slug normalizer produces a systematic false positive by retaining the date prefix
      (reported 126 unprocessed; true 33); same error class as 07-19 and 07-20.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-494
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: extracted from 2026-07-21 daily run, exact quote
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, 2026-08-30, clustered query — "filename normalization; canonicalize-before-compare; date-prefix set-difference defects". Snippet-level only; zero
    full-text and zero abstract-level reads. Search confidence: MODERATE. This item was searched on its
    GENERALIZABLE limb only; the internal-empirical limb (a claim about this repository's own file state)
    is not adjudicable by literature and is marked NOT-SEARCHED, per the 2026-08-29 run's split-limb
    finding.

  Supporting evidence found: Partial

  Sources:
    1. Tcl wiki, "file normalize"; normfn (github.com/andrewferrier/normalize-filename). — date-prefix
       normalization (YYYY-MM-DD-name.ext) is an explicit, known transform boundary.
    2. Linux Journal. "Normalizing Filenames and Data Using Bash String Variable Manipulations." —
       canonicalize before set comparison, not after.
    3. Bouliane, N. "File names, unicode normalization problems, and how to fix them." — unequal
       normalization on the two sides of a comparison is the general defect class.

  Strength of support: Weak-Moderate

  Summary:
    Unequal normalization on the two sides of a set comparison is a recognised defect class, and date-prefix
      normalization is an explicitly handled transform in filename-normalization tooling. Support for the
      general mechanism is solid. Support for the specific combination sought -- date-prefix set-diff false
      positives verified against a known-answer fixture -- was not found at snippet level; the closest
      literature is generic canonicalize-before-compare guidance.

  Caveats:
    Search scope preliminary: one query, snippet-level only, no full text. The gap is most likely a
      literature-indexing gap rather than a novelty; golden-file testing of a diff is too ordinary to
      publish. NOVELTY is NOT flagged.

  Recommendation: PARTIALLY-SUPPORTED

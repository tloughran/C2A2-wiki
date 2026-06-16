SEARCH-FOR-PRESUMPTION-329:
  Date searched: 2026-06-11
  Original item: PRESUMPTION-329
  Original statement: Scrubbing the working tree discharges a public-exposure concern, leaving git history, published copies, and the underlying capability unexamined.

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-329
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by inference from de-BOSCO scrub workflow (2026-06-09 EOD run)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (literature supports the embedded critique, not the presumption)
  Sources:
    1. GitGuardian, "The State of Secrets Sprawl" reports (2021–2025). — ~70% of secrets exposed in public repos in 2022 remained valid years later; working-tree removal demonstrably does not end exposure.
    2. Brizinov (Truffle Security), 2025. "How I Scanned all of GitHub's 'Oops Commits' for Leaked Secrets." — Even force-pushed "deleted" commits persist in archives and remain harvestable; deletion from the visible tree leaves recoverable copies.
    3. GitHub Docs. "Removing sensitive data from a repository." — Official guidance: history rewrite, fork coordination, cache invalidation, and credential rotation are all required beyond working-tree removal; commits remain accessible in forks and caches.
  Strength of support: None
  Summary: No literature was found supporting the presumption that scrubbing the current working tree (or current served artifact) discharges a public-exposure concern when history, published copies, and the underlying capability are left unexamined. The remediation literature uniformly treats working-tree removal as the first and weakest step: git's append-only model, fork propagation, platform event archives, search-engine and web-archive caches each preserve independent copies, and empirical studies show exposed material remains accessible and exploitable for years. The only stopping-short precedent (GitGuardian's "revoke then stop") applies when the *capability* is neutralized — precisely the element this presumption leaves unexamined. The closest charitable reading — exposure-surface reduction for casual discovery — is acknowledged in the literature but explicitly distinguished from discharge of the concern.
  Caveats: The searched literature concerns credentials/secrets; the scrubbed content here is descriptive narration ("bosco"/"email" strings), where the persistence mechanics (history, archives, mirrors) are identical but the harm model is weaker. A risk-based argument could justify stopping at the working tree, but that argument must be made, not presumed.
  Search scope: 1 query ("secrets remain in git history after file deletion study leaked credentials persist public repositories"); productive.
  Recommendation: NO-SUPPORT-FOUND

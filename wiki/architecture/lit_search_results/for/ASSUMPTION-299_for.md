SEARCH-FOR-ASSUMPTION-299:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-299
  Original statement: Removing all "bosco"/"email" strings from the current public HTML discharges the public-exposure concern (validated by string count + static checks).

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-299
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from sociogram verify/de-BOSCO work (2026-06-09 EOD run)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. GitHub Docs. "Removing sensitive data from a repository." — Endorses pattern/string-based scanning as the standard detection mechanism, and notes remediation of the *served* artifact is the first-line step; supports string-count validation as a recognized verification technique.
    2. GitGuardian remediation documentation ("Remediate a leak on public GitHub"). — Supports the principle that once the underlying risk is neutralized "you should typically stop here" — i.e., proportionate remediation rather than maximal scrubbing can legitimately discharge a concern.
    3. Tooling literature/practice: gitleaks, git-secrets, truffleHog. — Pattern-matching scans are the industry-standard completeness check for sensitive-string removal, directly analogous to the string-count + static-check validation used.
  Strength of support: Weak
  Summary: There is genuine support for the *method*: string/pattern scanning is the canonical way the security industry verifies that sensitive tokens are absent from an artifact, and remediation guidance accepts proportionate, risk-based stopping points rather than demanding exhaustive scrubbing in every case. If the threat model is strictly "a visitor to the current public HTML can find these strings," removal plus a zero-count scan plausibly discharges that specific concern. The literature does not, however, support the broader sufficiency claim: standard guidance treats current-artifact removal as one step, with version history, caches, mirrors, search-engine copies, and the Wayback-style archives as separate exposure surfaces, and warns that exact-string matching misses variants, encodings, and derived identifiers.
  Caveats: Discharge holds only for the narrowly-scoped concern (current served artifact, exact strings). Case-variants, substrings inside compressed/encoded blobs, prior published versions, and crawler caches are outside the validation's reach. See PRESUMPTION-329 for the residual-surface question.
  Search scope: 1 query ("removing secrets from repository insufficient git history rewrite credential leak remediation best practice"); productive.
  Recommendation: PARTIALLY-SUPPORTED

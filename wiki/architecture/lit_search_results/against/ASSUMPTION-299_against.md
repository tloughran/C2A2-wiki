SEARCH-AGAINST-ASSUMPTION-299:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-299
  Original statement: Removing all "bosco"/"email" strings from the current public HTML discharges the public-exposure concern (validated by string count + static checks).

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-299
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from sociogram verify/de-BOSCO work (2026-06-09 EOD run); remediation-completeness claim flagged LOW
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. GitHub Docs. "Removing sensitive data from a repository." — Canonical guidance: deleting/editing a file does not remove the data; it persists in git history, forks, cached views, and pull-request references, requiring history rewrite plus GitHub Support cache purges.
    2. Meli, M., McNiece, S., Reaves, B., 2019. "How Bad Can It Git? Characterizing Secret Leakage in Public GitHub Repositories." NDSS. — Empirical study: secrets in public repos are harvested within minutes of exposure; once published, removal from the current tree provides no protection because copies already exist.
    3. GitGuardian documentation, "Remediate a leak on public GitHub." — Standard remediation doctrine treats exposed material as compromised regardless of subsequent removal; the fix is rotation/invalidation of the exposed thing, not deletion of the visible copy.
    4. Vondran Legal / Internet Archive removal guides (2024-2025). — Published web pages persist in the Wayback Machine and third-party caches after source removal; purging archives is slow, discretionary, and often incomplete.
  Strength of challenge: Strong
  Summary: The data-leakage literature directly contradicts the sufficiency claim. String removal from the current artifact addresses exactly one of at least four exposure surfaces: (1) git history retains every prior committed version; (2) previously published/synced copies (web archives, browser caches, mirrors, any prior distribution of the ~4MB HTML) are outside the author's control; (3) string matching misses encoded, split, or paraphrased occurrences (the static check validates only literal "bosco"/"email" strings, while the exposure concern is plausibly about identifiability, which survives paraphrase); (4) the standard security doctrine is that exposed material must be treated as already harvested. Validation by string count measures the scrub, not the exposure.
  Specific risks: A concern formally marked "discharged" remains live; future audits trust the closed status; if the underlying datum is personally identifying, re-identification remains possible from history or archived copies while the project believes itself clean.
  Mitigations available: Check git history (git log -S) and rewrite if needed; check Wayback/caches for prior published versions and request purges; grep for encodings and semantic equivalents, not just literal strings; reclassify the item from "discharged" to "current-artifact remediated, residual exposure assessed."
  STEELMAN:
    Strongest counterargument: The remediation may be proportionate to the actual threat model: if the strings were never committed to a public repo, never crawled, and the HTML was only ever served locally or briefly, the "current artifact" essentially IS the exposure surface, and string-count validation is then a complete check. The secret-leakage literature describes high-value credentials harvested by scanners; a name string in a personal wiki visualization has a vastly lower adversary profile.
    What would need to be true for C2A2 to be safe: The file's full distribution history is known and bounded (no public commits, no archive crawls, no third-party copies); the concern is about the literal strings rather than inferable identity; the scrub also covered git history if any exists.
    How to test: Enumerate exposure surfaces concretely: git log -S "bosco" on every repo containing the file; Wayback/cache lookup of any URL the file was served at; grep for base64/URL-encoded variants. If all come back empty, the discharge claim is substantiated; until then it is unverified.
  Search scope: "secrets removed from repository remain in git history caches mirrors incomplete redaction incident" (1 search); plus Meli et al. 2019 NDSS from established literature.
  Recommendation: CHALLENGED

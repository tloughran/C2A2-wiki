SEARCH-FOR-ASSUMPTION-341:
  Date searched: 2026-06-24
  Original item: ASSUMPTION-341
  Original statement: "Wikilink resolution must be path-aware (not basename-only); the production resolver may be basename-only, skewing every weekly connectivity figure"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-341
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 06-23 audit as a measurement-correctness claim gating the connectivity series
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Path-resolution / normalization literature (Windows path resolution; general parser-correctness practice). - Basename-only matching collapses distinct paths that share a filename, producing both false-positive and false-negative link resolutions; path-aware resolution is the correct reference behavior.
    2. Test-to-code traceability and link-resolution practice. - Correct link/reference resolution requires the full qualified identifier; truncated (basename) keys are a known source of silent mis-association.
    3. C2A2-internal family: PREMISE-049 (verify-before-trust), the silent-zeroing class (369/373). - Silent measurement error from a wrong read/resolve rule is an already-recognized failure mode in this system.

  Strength of support: Moderate

  Summary: The methodological claim - that link-graph measurement must use path-aware resolution and that basename-only resolution silently miscounts - is well grounded. Filename collisions across folders are common in a multi-tradition vault, and a basename-only resolver will both merge distinct targets and miss correct ones, skewing every derived connectivity figure. This is the same silent-measurement-error class the system has already flagged. Support is for the principle; the empirical question of whether the PRODUCTION resolver is in fact basename-only remains a code-inspection/recompute task.

  Caveats: Strength of the skew is unknown until recomputed; if the vault happens to have no basename collisions, the practical error could be small. The 'must' is methodologically right but its impact is empirical.

  Search scope: path resolution correctness; silent measurement error; parser keys. Adequate.

  Recommendation: PARTIALLY-SUPPORTED

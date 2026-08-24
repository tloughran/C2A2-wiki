SEARCH-FOR-PRESUMPTION-837:
  Date searched: 2026-08-19
  Original item: PRESUMPTION-837
  Original statement: That a file found at an expected path is this run's own output. Authorship is
    presumed from location, so no run checks whether the artifact it is about to trust is the artifact it
    just made.

  Reading used for this search: because the item is a *presumption* (an unstated belief 14b judges to be
  operative and unsafe), the FOR direction is read as: does the literature support 14b's diagnosis — that
  path-as-identity is a real, commonly-made, and consequential assumption? It is NOT read as support for
  the presumption being true.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-837
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by asking what all three of tonight's temp-file traps required to be true in order to
        fire, and finding a single unstated identity claim rather than three staleness bugs.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. SLSA (Supply-chain Levels for Software Artifacts) specification, v1.2 FAQ — slsa.dev.
       [standards document, consulted via search results] — The entire SLSA provenance model exists
       because an artifact's location does not establish what produced it; provenance must be *attested*
       separately and verified against the artifact. This is the strongest form of support available for
       14b's diagnosis: an industry standard was built specifically to replace path-as-identity with
       explicit authorship attestation.
    2. "Kettle: Attested builds for verifiable software provenance." arXiv:2605.08363. (author list not
       verified) — Recent work on attesting builds so that a consumer can verify an artifact came from a
       claimed pipeline. Confirms that verifiable authorship of intermediate/final artifacts remains an
       open engineering problem being actively worked, not a solved default.
    3. Reproducible-builds literature: "Understanding Build Reproducibility in the F-Droid Ecosystem"
       (arXiv:2607.01890) and the reproducible-builds overview materials consulted. (author lists not
       verified) — State that reproducibility requires that "every build input is content-addressed" and
       that hash divergence is the mechanism by which tampering or substitution is detected. Establishes
       content-addressing versus path-addressing as a recognised, named distinction with the exact
       property the item is missing.
    4. "Understanding and Detecting Flaky Builds in GitHub Actions." arXiv:2602.02307. (author list not
       verified) — Names "residual artifacts from previous executions" polluting the build environment as
       a cause of flaky builds, i.e. empirically documents runs consuming a prior run's leavings.
    5. GitHub Actions cache-poisoning research (Hive Security; OpenSSF workflow-hardening guidance;
       OpenRewrite `github/security/CachePoisoning` recipe). [grey/security literature] — The adversarial
       form: untrusted writers place content where a trusted reader will pick it up on the strength of
       location alone.

  Strength of support: Strong

  Summary: 14b's diagnosis is well supported. The claim that systems routinely infer artifact authorship
  from location, and that this is unsafe, is the founding premise of the software-supply-chain provenance
  literature: SLSA, build attestation (Kettle), and content-addressed reproducible builds all exist
  precisely to replace "it is at the expected path" with "its hash matches what the attested producer
  claims to have made." The failure has both an accidental form (stale residual artifacts causing flaky
  builds — arXiv:2602.02307) and a deliberate form (cache poisoning). Notably, the literature also
  supports 14b's structural move of treating three staleness bugs as one identity claim: content-
  addressing is a single remedy that dissolves the whole class, which is the signature of a shared root
  rather than coincident bugs.

  Caveats: All support is from build/CI and supply-chain security, where the artifacts are binaries and
  the verification primitive is a cryptographic hash; C2A2's artifacts are markdown and JSON produced by
  agent runs, and the cost of adopting content-addressing there has not been assessed by any source
  found. The literature establishes that path-as-identity is unsafe; it does not establish how often it
  bites in low-adversarial single-tenant settings, so the risk rating (Critical) is not itself supported
  by rate data. Search scope: moderate — covered SLSA/provenance/attestation, reproducible builds, CI
  flakiness, cache poisoning; did NOT cover the OS/filesystem literature on path resolution races (TOCTOU,
  symlink attacks), which is a further relevant body.

  Recommendation: SUPPORTED

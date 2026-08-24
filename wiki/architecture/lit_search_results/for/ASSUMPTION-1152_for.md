SEARCH-FOR-ASSUMPTION-1152:
  Date searched: 2026-08-19
  Original item: ASSUMPTION-1152
  Original statement: Three temp-artifact traps fired in one night, one of which yields a total false-clean
    verdict: "A run that redirects to that path gets a silent shell failure and then parses the stale file
    as its own output — concluding the vault is entirely clean." Both detections were attributed to luck.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1152
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Collected three independent same-night traps and identified the single shared mechanism
        beneath them.
      15a: Searched for supporting literature (2026-08-19)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. "Understanding and Detecting Flaky Builds in GitHub Actions." arXiv:2602.02307. (author list not
       verified) — Identifies corrupted caches (invalid cached artifacts) and stale build caches, where
       "residual artifacts from previous executions pollute the build environment," as recognised causes
       of flaky builds. Direct analogous support: an artifact left at a known path from a prior run is a
       named, studied failure source.
    2. "Characterizing and Fixing Silent Data Loss in Spark-on-AWS-Lambda with Open Table Formats."
       arXiv:2604.20081. (author list not verified) — Establishes the general class of failures in which
       a job "succeeds" while its data is silently wrong. Supports the specific severity claim: the
       failure signature is a pass, not an error.
    3. GitHub Actions cache-poisoning analyses (Hive Security, "The Cache That Bites Back"; Adnan Khan,
       "Clinejection"; OpenSSF, "Mitigating Attack Vectors in GitHub Workflows"; OpenRewrite recipe
       `github/security/CachePoisoning`). [grey/security literature] — Describe the same structural
       mechanism from the adversarial side: untrusted code writes into shared storage that a later
       trusted workflow reads from, "exploiting features working exactly as designed." One analysis notes
       that a malformed cache overwrite produces a post-step failing "with no output" — i.e. the silent
       variant. That this shape is a recognised *attack class* is strong evidence it is a real and
       exploitable failure mode, not an idiosyncrasy of this vault.
    4. Practitioner reports of green-but-empty pipelines (DEV Community, "The CI/CD Pipeline That Looked
       Fine But Was Silently Failing") — Test suites exiting 0 having run zero tests, pipeline green,
       deployment "successful," no alerts fire. [grey] Corroborates the false-clean verdict shape
       specifically: a vacuous pass is indistinguishable from a real pass to a consumer that reads only
       the exit code and the output file.

  Strength of support: Moderate-to-Strong

  Summary: The mechanism the item describes — a shell redirection that fails without stopping the run,
  followed by the run reading a pre-existing file at the target path as if it were its own output — is a
  composite of two independently well-documented phenomena. Stale/residual artifacts at expected paths are
  a named cause of flaky and incorrect builds (arXiv:2602.02307), and the class of failures whose
  signature is a passing result rather than an error is documented both in data pipelines
  (arXiv:2604.20081) and in CI practice. The security literature on GitHub Actions cache poisoning is the
  strongest corroboration of the item's severity framing: an entire attack class exists that turns exactly
  this read-what-a-prior-writer-left pattern into a supply-chain compromise, which implies the defensive
  gap is real and structurally hard to see. The item's own claim that both detections were "attributed to
  luck" is consistent with the literature's observation that these failures carry no signal by
  construction.

  Caveats: No source studies the precise configuration (shell redirection to a temp path inside an agent
  run); support is by mechanism-analogy across CI, data pipelines, and supply-chain security. Several
  supporting items are grey literature (vendor blogs, security research posts) rather than peer-reviewed
  studies, and none establishes a base rate for how often this fires. The "three in one night" clustering
  is an observation about this vault and is not itself testable against literature. Search scope:
  preliminary-to-moderate — covered CI flakiness, cache poisoning, silent data loss; did NOT cover the
  systems literature on atomic writes / crash consistency (e.g. rename-based atomic replacement), which
  would likely supply the strongest engineering-grounded support and the standard remedy.

  Recommendation: SUPPORTED

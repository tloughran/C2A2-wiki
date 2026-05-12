SEARCH-FOR-ASSUMPTION-054:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-054
  Original statement: "Byte-stability smoke test is a valid operational proxy for cache determinism"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-054
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from RC Wiki MCP Install Plan smoke-test specification
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Anthropic prompt-caching documentation (2024-2025): cache keys are computed from prefix byte content; byte-identical prefixes produce cache hits. Byte-stability is a necessary condition for cache determinism — platform-validated.
    2. Content-addressable storage / deterministic build literature (Bazel, Nix; reproducible-builds.org 2018-2025): byte-stability of inputs is the canonical smoke test for deterministic systems. Analogy transfers cleanly to prompt-cache determinism.
    3. Regression testing / fingerprinting practice (Git hash-based integrity; cache-busting CI patterns 2020-2025): byte-level hashing is a standard lightweight verification primitive; first-line-of-defense against drift.
    4. Cache-invalidation diagnostics (Fowler 2018; Nygard 2007): byte-diff between expected and actual prefix is a standard diagnostic step for cache-miss investigation.

  Strength of support: Moderate

  Summary: Byte-stability is well-established as a NECESSARY condition for cache determinism — if the prefix bytes differ, the cache definitionally cannot hit. It is a valid SMOKE TEST (a quick, low-cost check) but not a complete validation: byte-identical prefix can still fail to produce a cache-hit if the caching system itself is misconfigured, if the prefix exceeds cache-eligibility size thresholds, if rate-limits apply, or if the platform's cache has been evicted. Literature supports byte-stability as first-line-of-defense, not as sufficient proof.

  Caveats: (a) Byte-stability is necessary but not sufficient — cache-hit telemetry is the sufficient test; (b) byte-stability can be trivially achieved by hashing the prefix but passing that test does not guarantee the platform has accepted the prefix for caching; (c) the word "proxy" in ASSUMPTION-054 is load-bearing — as a proxy it is valid; as a replacement for cache-hit telemetry it is not.

  Recommendation: PARTIALLY-SUPPORTED (byte-stability is a valid smoke test in the sense literature recognizes smoke tests — necessary but not sufficient; the "valid proxy" framing needs clarification that cache-hit telemetry remains the authoritative measurement)

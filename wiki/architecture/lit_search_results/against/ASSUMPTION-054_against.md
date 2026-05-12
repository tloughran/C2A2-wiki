SEARCH-AGAINST-ASSUMPTION-054:
  Date searched: 2026-04-20
  Original item: ASSUMPTION-054
  Original statement: "Byte-stability smoke test is a valid operational proxy for cache determinism"

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-054
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from RC Wiki MCP Install Plan smoke-test specification
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Testing hierarchy literature (Humble & Farley 2010 "Continuous Delivery"; Chen et al. 2020 "ML Test Score"): smoke tests verify system boot; integration tests verify behavior. Byte-stability is a smoke-level check, not a behavior-level check. Calling it a "valid operational proxy for cache determinism" overstates what byte-identity can prove.
    2. Cache-system failure modes (Fowler 2018; Nygard 2007): cache can fail to engage even on byte-identical prefix — eligibility thresholds, tenant-level quota, rate-limit fallback, cache eviction, platform outages. Byte-stability passing while cache-hit telemetry fails is a documented failure mode.
    3. Observability gap (Majors et al. 2022 "Observability Engineering"): proxy metrics that don't match the system-of-record are the #1 source of observability false-positives. The cache-hit telemetry is the system-of-record for cache determinism; byte-stability is a proxy with documented gap-cases.
    4. Proxy metric risk (Goodhart's Law applied to operational metrics): when a proxy becomes the rollout gate, teams optimize for the proxy rather than the target. If byte-stability is the gate, rollout could proceed with cache silently not engaging — detected only later when cost projections fail.
    5. Hidden dynamic-content detection limit (content-stability audit practice): byte-stability detects TODAY's identity; it does not detect tomorrow's if any of the 49 files will be touched between runs. It is a one-moment test, not a ongoing invariant.

  Strength of challenge: Moderate

  Summary: Byte-stability is a NECESSARY but NOT SUFFICIENT condition for cache determinism. Literature on testing hierarchies treats smoke tests as ensuring "things boot" rather than "things work"; elevating byte-stability to the status of a valid operational proxy conflates the two. The authoritative measure of cache determinism is cache-hit telemetry from the platform; byte-stability is a cheap first-line check. Using byte-stability AS the rollout gate creates Goodhart's Law risk — optimizing for byte-identity can proceed while cache silently disengages.

  Specific risks: (a) Rollout proceeds on byte-stability PASS while cache silently fails to engage (no cache-hit telemetry check); (b) proxy-vs-target divergence undetected; (c) smoke test passes on day 1 but cache behavior regresses on day N without detection; (d) pressure to treat byte-stability pass as proof reinforces the proxy over the authoritative measure.

  Mitigations available: (a) Pair byte-stability smoke test with cache-hit telemetry check in the rollout gate (both must pass); (b) define cache-hit rate thresholds as the authoritative gate, treat byte-stability as a leading indicator; (c) continuous byte-stability monitoring (not one-time); (d) re-label the smoke test as "necessary condition check" rather than "valid operational proxy" to preserve epistemic honesty about what it proves.

  Recommendation: PARTIALLY-CHALLENGED (byte-stability is a valid smoke test as literature uses the term; the "valid operational proxy" framing in ASSUMPTION-054 overstates; rollout gate should pair it with cache-hit telemetry)

  STEELMAN:
    Item: ASSUMPTION-054
    Strongest counterargument: Byte-stability is a NECESSARY condition — without byte-identical prefix, cache definitionally cannot hit — but it is not a SUFFICIENT condition. Platform-side cache systems can fail to engage on byte-identical prefix due to eligibility thresholds, rate limits, quota exhaustion, or eviction. The authoritative measure of cache determinism is cache-hit telemetry; byte-stability is a cheap leading indicator. Treating byte-stability as a rollout gate creates Goodhart's Law risk: optimizing for byte-identity while cache silently disengages. The fix is simple and cheap — pair the byte-stability smoke test with a cache-hit telemetry check in the same gate.
    What would need to be true for C2A2 to be safe: Cache-hit telemetry available at gate-evaluation time; gate requires BOTH byte-stability pass AND cache-hit rate ≥ threshold.
    How to test: Run byte-stability PASS and verify cache-hit telemetry on the same session; if byte-stable but cache-hit rate low, the gap is real and the presumption is broken.

SEARCH-FOR-PRESUMPTION-056:
  Date searched: 2026-04-20
  Original item: PRESUMPTION-056
  Original statement: "Cost is the sole optimization target (no quality-regression smoke test in the rollout gate)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-056
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from smoke-test coverage gap in RC Wiki MCP Install Plan
      15a: Searched for supporting literature
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No

  Sources:
    1. Anthropic prompt-caching documentation (2024-2025): notes that cached tokens produce identical inference output to non-cached tokens — implicit claim that caching is quality-invariant. Could be cited in support of "no quality test needed."
    2. Deterministic-inference literature (model-behavior sanity testing 2020-2025): if the model receives identical tokens, outputs should be identical (modulo sampling temperature). If temperature=0, caching has no quality effect.

  Strength of support: Weak

  Summary: The only argument in literature for skipping a quality-regression gate rests on the theoretical claim that cached tokens are byte-identical to non-cached tokens — so inference output should not differ. This is a platform-level quality invariant, not a project-level safeguard. No literature supports "cost alone is a sufficient optimization target without a quality floor check," because the presumption conflates platform-guaranteed invariance with operational confidence. Platform invariants can silently fail (caching bugs, quantization, rate-limit fallback paths, truncation at cache-breakpoints, sampling-variance interactions), which is why production deployments add safeguards.

  Caveats: (a) Platform-level quality invariance assumes bug-free implementation — production deployments do not typically assume this; (b) the argument from invariance works only with temperature=0; at nonzero temperature, sampling variance independently requires a quality check; (c) literature on deployment gates (Humble & Farley 2010 "Continuous Delivery"; Chen et al. 2020 "ML Test Score") uniformly recommends quality gates for ML system changes.

  Recommendation: NO-SUPPORT-FOUND (the strongest available argument — platform token-equivalence — is a theoretical invariant, not a deployment-gate substitute; no serious literature supports cost-only gating in production)

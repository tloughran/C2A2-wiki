SEARCH-AGAINST-ASSUMPTION-360:
  Date searched: 2026-06-25
  Original item: ASSUMPTION-360
  Original statement: "Local/offline (Ollama) + own-key generous-free (Groq) providers with local-search fallback beat single shared-broker dependence for a public artifact"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-360
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted (resilience/independence design value)
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Distributed-systems reliability (failure-mode literature). - Added redundancy increases COMPLEXITY and can lower reliability if the fallback paths are poorly tested ('redundancy can reduce reliability' when coupling/maintenance dominates).
    2. Client-side key exposure: own-key (Groq) in a public client surfaces the secret-handling risk of ASSUMPTION-359/PRESUMPTION-395.
    3. Behavioral inconsistency: heterogeneous providers (Ollama vs Groq vs local search) yield inconsistent output quality/latency, complicating a coherent UX and evaluation.

  Strength of challenge: Weak

  Summary: The challenge is qualified, not decisive. Multi-provider fallback genuinely removes a single point of failure, but it is not free: each path must be maintained and tested or it becomes a latent failure; heterogeneous backends produce inconsistent behavior; and own-key client provisioning re-imports the secret-exposure risk. So 'beat a single shared broker' holds for availability but can lose on maintainability, consistency, and security depending on context.

  Specific risks: Untested fallback paths fail silently when needed; client-held provider keys leak; inconsistent backend behavior undermines reproducibility of the artifact's outputs.

  Mitigations available: Test every fallback path (chaos/failover testing); keep provider keys off the client (proxy) or document exposure; normalize/label outputs by backend.

  STEELMAN:
    Item: ASSUMPTION-360
    Strongest counterargument: Resilience from multi-provider fallback is real but bought with complexity, inconsistency, and (for client-held keys) new exposure; whether it 'beats' a single broker depends on whether the fallbacks are actually maintained and whether key handling is safe.
    What would need to be true for C2A2 to be safe: Each fallback path is regularly exercised and the provider keys are not exposed client-side.
    How to test: Run failover drills (disable primary, confirm graceful fallback); audit where provider keys live.

  Search scope: Redundancy-vs-complexity; multi-provider tradeoffs. Adequate.

  Recommendation: PARTIALLY-CHALLENGED

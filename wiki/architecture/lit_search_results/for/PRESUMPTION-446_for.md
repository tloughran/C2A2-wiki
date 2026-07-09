SEARCH-FOR-PRESUMPTION-446:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-446
  Original statement: "[inferred] That scheduled agents and attended sessions can share one git repository with no coordination protocol."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-446
    Item type: PRESUMPTION (unstated — surfaced by inference; severity CRITICAL)
    Transform at each step:
      14b: Inferred from observed index.lock/HEAD.lock collisions that the architecture presumes uncoordinated concurrent writers on one working copy are safe
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Git internals documentation and practitioner analyses (Microsoft Learn "Git index.lock"; Pluralsight "Understanding and Using Git's index.lock File"). — Git itself ships a minimal built-in coordination mechanism: atomic lockfile creation (index.lock, HEAD.lock) prevents index corruption from concurrent mutating commands. Supports the narrow claim that uncoordinated concurrent access fails safe (command aborts) rather than corrupting state — i.e., the substrate provides an implicit floor of coordination.
    2. Kung, H.T. & Robinson, J.T., 1981. "On Optimistic Methods for Concurrency Control." ACM TODS 6(2). — Theoretical grounding that uncoordinated (lock-free, optimistic) access to shared mutable stores is a legitimate, well-analyzed strategy when contention is low and conflicts are detected and resolved at commit time. Analogous support for "no explicit protocol" designs in low-collision regimes.
    3. CodeCRDT (arXiv 2510.18893, 2025). "Observation-Driven Coordination for Multi-Agent LLM Code Generation." — Demonstrates multi-agent code production can converge without explicit message-passing coordination, via observation of shared state. Partial analogous support: protocol-free coordination is achievable — but only atop a CRDT substrate engineered for lock-free convergence, which a shared git working copy is not.
    4. He et al. (ACM TOSEM, 2025; arXiv 2404.04834). "LLM-Based Multi-Agent Systems for Software Engineering: Literature Review, Vision, and the Road Ahead." — Documents that concurrent modification and merge conflicts are a recognized primary failure mode in multi-agent SE systems when coordination primitives are not explicitly modeled; sequential pipelines, locking, and branching are the surveyed mitigations. Cited here because it confirms the practice exists and is studied — but its weight runs toward requiring a protocol.

  Strength of support: Weak

  Summary: The best supporting case assembled from the literature is conditional: git's advisory lockfiles guarantee corruption-free failure (not success) under concurrent writers, and optimistic-concurrency theory legitimizes protocol-free sharing when contention is rare and conflict handling is safe. Under those readings, scheduled agents and attended sessions "can" share one repository in the weak sense that collisions abort cleanly instead of corrupting the store. But no found source supports the strong claim that this is an adequate architecture: the multi-agent SE literature treats unmodeled concurrency as a primary failure mode, and the coordination-free successes found (CodeCRDT) required purpose-built convergent data structures. The very incident that surfaced this presumption (lock collisions during the attended session) is the OCC literature's predicted signature of contention exceeding the optimistic regime.

  Caveats: Support holds only while (a) write windows are short and rarely overlapping, (b) collisions are handled by wait-and-retry rather than lock deletion, and (c) no two writers hold divergent working-tree state (git's locks protect the index, not the working tree — concurrent checkout/edit interleavings remain unprotected). Scheduled tasks by construction fire regardless of attended-session activity, so overlap probability grows with session length; the low-contention condition is not enforced by anything in the architecture.

  Recommendation: PARTIALLY-SUPPORTED

SEARCH-FOR-PRESUMPTION-432:
  Date searched: 2026-07-02
  Original item: PRESUMPTION-432
  Original statement: "[inferred] That the compute sandbox's ephemeral disk is unbounded/self-managing — no monitoring or scratch GC, so a full container disk silently halts any agent needing local writes."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-432
    Item type: PRESUMPTION (unstated)
    Transform at each step:
      14b: Surfaced as unstated presumption from the 2026-07-01 disk-full incident
      15a: Searched for supporting literature (genuine web search 2026-07-02)
    Current status: NO-SUPPORT-FOUND

  Supporting evidence found: No (weak)

  Sources:
    1. (Mechanism only) Many managed sandboxes/CI runners DO reset scratch between runs, so an agent can often assume a clean slate at start-of-run — a narrow, start-of-run reading that offers weak partial support.

  Strength of support: Weak

  Summary: No literature supports the actual presumption that ephemeral disk is unbounded or self-managing WITHIN a run. The only defensible fragment is that scratch is often reset BETWEEN runs — which is irrelevant to a mid-run fill. The Kubernetes/container literature (see 15b) treats ephemeral storage as a bounded, exhaustible resource that must be explicitly requested, limited, monitored, and GC'd. Support for the presumption is essentially absent.

  Caveats: The between-runs reset does not license the within-run "unbounded/self-managing" inference that caused the halt.

  Recommendation: NO-SUPPORT-FOUND (only the trivial between-runs-reset reading is supportable; the operative claim is unsupported)

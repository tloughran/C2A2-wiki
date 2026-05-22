SEARCH-FOR-PRESUMPTION-204:
  Date searched: 2026-05-19
  Original item: PRESUMPTION-204
  Original statement: "Sewing-agent's pending/-scan-as-ground-truth — inverts morning's PRESUMPTION-196 (orchestrator-as-ground-truth) without auditing whether the two scans use identical path/filter/timing coverage."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-204
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by detecting an unstated inversion of PRESUMPTION-196's ground-truth choice
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Lamport, L., 1978. "Time, Clocks, and the Ordering of Events in a Distributed System." CACM 21(7) — foundational: no single observer in a distributed system holds ground truth without reconciliation; replacing one observer with another doesn't establish truth, only changes which observer is unverified.
    2. Birman, K.P., 2012. "Guide to Reliable Distributed Systems." Springer — explicit: any "agent X as ground truth" claim must be paired with an audit of X's coverage, otherwise it is just relocating the unverified premise.
    3. Helland, P., 2015. "Immutability Changes Everything." CACM 59(1) — durable artifacts (the actual files) trump any agent's view; agent-as-truth is a bug, manifest-as-truth or scan-of-durable-state-as-truth (with explicit coverage audit) is the fix.
    4. Beyer, B. et al., 2016. "Site Reliability Engineering." O'Reilly, ch. on observability — SRE doctrine: "trust the artifact, not the agent"; both orchestrator and sewing-agent are agents, both need coverage audits before either claims ground-truth status.

  Strength of support: Strong

  Summary: The presumption that the sewing-agent's pending/-scan is the new ground truth — implicitly displacing the orchestrator from that role without auditing coverage equivalence — is exactly the symmetric error that distributed-systems literature has warned against for 40+ years. Two unaudited observers cannot adjudicate ground truth between themselves; reconciliation requires a third leg (the manifest of writes / the immutable artifact log) and explicit coverage comparison. The presumption is well-supported as an open risk requiring revision.

  Caveats: This does not invalidate the sewing-agent's evidence (ASSUMPTION-179 is still SUPPORTED) — it only blocks the elevation of that evidence to ground-truth status.

  Recommendation: SUPPORTED

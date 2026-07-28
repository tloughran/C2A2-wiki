SEARCH-AGAINST-PRESUMPTION-535:
  Date searched: 2026-07-24
  Original item: PRESUMPTION-535
  Original statement: [inferred] Unattended "fully-automated" operation (18 attended-free days) is presumed a stable steady state rather than a degradation of a human-in-the-loop design.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-535
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from unattended mode framed as a routine steady state
      15b: Searched for evidence that unattended automation can be a legitimate stable steady state
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. High-reliability / lights-out automation practice (SRE, unmanned data centers, autonomous batch systems). — Many systems run unattended by design for long periods without degradation; "unattended" is not intrinsically a degraded human-in-the-loop design, it can be the intended operating mode.
    2. "Human-on-the-loop" supervisory paradigm. — Shifting from in-the-loop approval to on-the-loop oversight is a recognized, valid scaling response (HITL doesn't scale; HOTL does), not a failure state.
    3. Autonomy-levels frameworks (e.g., SAE-style ladders). — A system explicitly designed for a higher autonomy tier is correctly evaluated against that tier, not judged as a broken lower-tier HITL system.

  Strength of challenge: Moderate

  Summary: Whether 18 attended-free days is "degradation" or "steady state" depends on the intended autonomy tier. If C2A2 was designed as human-on-the-loop, long unattended runs are the design working; the Bainbridge risks apply to takeover readiness but do not by themselves make autonomy a pathology. The presumption is right to flag latent out-of-loop debt but wrong if it assumes unattended == degraded a priori.

  Specific risks: Mislabeling intended autonomy as degradation could trigger unnecessary re-introduction of human gates (which PREMISE-119 says are themselves a bottleneck).

  Mitigations available: State the design's intended autonomy tier explicitly, then judge unattended operation against it; instrument takeover-readiness rather than assuming it.

  STEELMAN:
    Item: PRESUMPTION-535
    Strongest counterargument: The specific evidence — human-gated queues (review, RE-TRIGGER, commits) that do NOT drain during automated stretches — shows the human role was never actually removed by design, only stranded. That is degradation of a HITL design, not a chosen HOTL steady state, because essential human-only work is silently accumulating.
    What would need to be true for C2A2 to be safe: the gated queues must either drain autonomously or be genuinely optional; if they are load-bearing and stalled, "steady state" is false.
    How to test: the item's own test — do human-gated queues drain during automated stretches? (Current evidence: they do not — see PRESUMPTION-538.)

  Recommendation: PARTIALLY-CHALLENGED (turns on intended autonomy tier; the stalled human-gated queues favor the presumption)

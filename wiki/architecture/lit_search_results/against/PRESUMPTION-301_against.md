SEARCH-AGAINST-PRESUMPTION-301:
  Date searched: 2026-06-04
  Original item: PRESUMPTION-301
  Original statement: [inferred] Deferring activation of a staged capability is cost-free — Agents 17-20 / Sunday Tradition Synthesis Day exist as docs but won't run until an attended schedule edit; each skipped Sunday is presumed recoverable headroom.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-301
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced from staged-but-inert Agents 17-20 / Sunday Synthesis as recoverable headroom.
      15b: Searched when staging-without-activation is prudent sequencing, and YAGNI against premature activation.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Dark launching / decouple deploy from release (LaunchDarkly dark-launch guide; DevCycle "When to Use a Dark Launch Strategy"). — Built-but-not-activated is the INTENDED steady state of a dark launch: code is present but inert behind a flag, activated deliberately later. Staging-without-activation is a recognized, prudent release strategy, not waste.
    2. Progressive/staged rollout (LaunchDarkly release-management best practices). — Best practice is to hold a capability inert, then activate to 1% -> 10% -> 50% as confidence grows; deferring activation until conditions are right (here: an attended day with real synthesis substance) is exactly this risk-reducing sequencing.
    3. YAGNI / avoid premature activation (HN YAGNI discussion; lean overproduction waste). — Activating Agents 17-20 / Sunday Synthesis on quiet autonomous days before they are needed risks OVERPRODUCTION waste (output no one consumes) and premature commitment. Restraint until there is demand can be the disciplined choice, not lost headroom.

  Strength of challenge: Moderate

  Summary: Release-engineering practice pushes back on the framing rather than the cost: deferring activation of an inert, staged capability is a normal and often prudent strategy (dark launch, progressive rollout, YAGNI), not pure waste. Activating Agents 17-20 / Sunday Synthesis prematurely — especially on no-attended days that the pipeline itself flags as low-substance — could produce overproduction waste and lock in a design before it is validated against attended use. So neither "cost-free" (15a refutes) nor "costly to defer" (15b refutes) is right: the cost of deferral is real but small, and is partly OFFSET by genuine option value and risk reduction from waiting.

  Specific risks: Over-correcting on 15a's "deferral has cost" could trigger premature activation of half-fit agents that generate noise (overproduction) and entrench an unvalidated design — a worse outcome than patient deferral.

  Mitigations available: Treat deferral as a dated option, not indefinite limbo: record an explicit activation trigger/date (e.g., the next attended Sunday, or a readiness checklist) so the decision is revisited rather than drifting — capturing 15a's anti-decay point without 15b's premature-activation risk.

  STEELMAN:
    Item: PRESUMPTION-301
    Strongest counterargument: Holding a capability staged-but-inert is the textbook dark-launch posture, and activating it before there is validated demand is overproduction. The presumption that deferral is "cost-free" is loose, but the corrective is NOT "activate now" — it is "defer deliberately, with a trigger," because premature activation of these specific agents on low-substance autonomous days is precisely the waste YAGNI warns against.
    What would need to be true for C2A2 to be safe: Deferral is bounded by an explicit revisit trigger (date or readiness condition) so it cannot silently become permanent drift, AND activation is gated on real synthesis substance rather than a calendar tick.
    How to test: Check whether a concrete activation trigger exists for Agents 17-20 / Sunday Synthesis. If none, deferral is drifting (15a's decay risk is live); if a dated trigger exists, the deferral is prudent staging (15b).

  Recommendation: PARTIALLY-CHALLENGED

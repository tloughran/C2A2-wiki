SEARCH-AGAINST-PRESUMPTION-046:
  Date searched: 2026-04-18
  Original item: PRESUMPTION-046
  Original statement: "User pivot on arrival discharges a loaded handoff payload rather than re-queues it (payload-discharge-on-pivot)"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-046
    Item type: PRESUMPTION (unstated — surfaced by inference) — self-referential on DECISION-021
    Transform at each step:
      14b: Inferred from 2026-04-18 Dispatch session
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Workflow-system literature on persistent task-state (BPM/workflow engines; Allen 2001 GTD): tasks that are deferred for a user-initiated pivot are *expected* to be re-queued, not discharged; discharge-on-pivot causes silent loss of intent.
    2. Handoff-pattern vs. context-loading pattern distinction (pipeline architecture literature; Nygard 2007): if a mechanism is designed as a handoff, its correctness depends on the payload being acted upon; if pivot discharges it, the mechanism is a context-loader and should be renamed as such.
    3. Falsifiability in reliability claims (Popper 1963; applied to software reliability by Leveson 2011): a mechanism whose execution half is never exercised cannot be falsified. PRESUMPTION-046 directly implies that DECISION-021's reliability claim (ASSUMPTION-044) is unfalsifiable in the discharge-on-pivot regime.
    4. Self-awareness-meta cluster (PRESUMPTION-015, 024, 041, 042, 046): PRESUMPTION-046 is a self-referential blind spot — the mechanism cannot observe whether its own execution half is working because it only runs when user-direction aligns with loaded payload.
    5. Task-recovery literature (Whittaker et al. 2011 on interruption recovery): loaded context that is not acted upon on first session is empirically rarely revisited — it becomes silent architectural debt.

  Strength of challenge: Moderate-Strong

  Summary: The challenge has two prongs. First, as a normative design choice: discharge-on-pivot is a failure mode for a handoff pattern; if the mechanism is a handoff, it should re-queue. Second, as an epistemic problem: discharge-on-pivot makes the reliability of the handoff pattern unfalsifiable, because the execution half only runs when discharge doesn't occur — which is exactly the case where the mechanism doesn't need to prove itself. The cluster with ASSUMPTION-044 (which claims reliability at N=1 loading-only) and PRESUMPTION-041 (implicit decisions without DECISION records) is mutually reinforcing: a design that is unfalsifiable, unrecorded, and first-use-confirmed is a classic invisible-design-debt pattern.

  Specific risks: (a) DECISION-021's reliability claim accumulates confidence without evidence; (b) payload intent silently discharges and architectural direction drifts; (c) the handoff-vs-context-loader taxonomy ambiguity is never resolved; (d) joins self-awareness-meta cluster as a 5th member.

  Mitigations available:
    - Decide explicitly whether DECISION-021 is a handoff or a context-loader; rename accordingly.
    - If handoff: implement re-queue-on-pivot so the payload is not silently discharged.
    - If context-loader: drop the "reliably orients" framing (ASSUMPTION-044) and treat it as a load-only primitive.
    - Instrument: track (loaded-count, acted-on-count, discharged-count) as three distinct observables.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-046
    Strongest counterargument: The presumption has two horns. On the descriptive horn, it is trivially true — users in practice do discharge loaded payloads on pivot. On the normative horn, it is a failure of handoff-pattern discipline: if the mechanism is meant to be a handoff, discharge-on-pivot silently loses architectural intent, and the reliability of the handoff cannot be measured because the execution half is never exercised on pivot-days. The self-referential consequence — that DECISION-021's reliability claim (ASSUMPTION-044) is unfalsifiable — is what makes this a CRITICAL epistemic problem even though the descriptive claim is banal.
    What would need to be true for C2A2 to be safe: Disambiguate handoff-vs-context-loader; implement re-queue semantics if the mechanism is a handoff; downgrade "reliably" language if it is a context-loader.
    How to test: On next Dispatch session: if Tom pivots, does the loaded payload persist to the next session? If no, the presumption is factually in effect and the mechanism is a context-loader by behavior.

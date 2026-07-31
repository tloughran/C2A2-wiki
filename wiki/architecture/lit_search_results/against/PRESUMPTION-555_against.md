SEARCH-AGAINST-PRESUMPTION-555:
  Date searched: 2026-07-27
  Original item: PRESUMPTION-555
  Original statement: [inferred] Calling CROSS questions "decidable" via each agent stating whether Q_A is identical to the blanket generative model presumes an agent's assertion settles a formal identity - but exact identity is proof, not self-report.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-555
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a "decidable" procedure resolving a formal identity by agent statement rather than proof
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. LLM-assisted formal proof / autoformalization successes (Lean/Isabelle copilots; DeepMind AlphaProof-style results in formal reasoning). — When an agent's verdict is paired with a machine-checkable derivation, the stated verdict CAN in effect settle the question, because the proof (not the assertion) is checked. So the objection is really "attach a checker," and with a checker the procedure is sound.
    2. Verifier-in-the-loop / self-consistency (Wang et al. 2022, "Self-Consistency Improves Chain of Thought Reasoning"; Lightman et al. 2023, process reward / verification). — Aggregated or verified self-reports materially outperform single assertions; a stated verdict is not worthless, and cheap aggregation raises reliability substantially.
    3. Decidability pragmatics. — For many concrete candidate pairs the identity question is EASY (a short derivation an agent can produce and a human/CAS can check in seconds); calling such cases "decidable" is accurate. The presumption over-generalizes from hard identities to all cases.

  Strength of challenge: Moderate

  Summary: The challenge does not defend "assertion = proof"; it narrows the target. If "decidable" means "an agent produces a derivation that is then checked," the procedure is sound - the check, not the assertion, settles it. And for easy identities a stated verdict plus a trivial check is adequate. The presumption is right that a bare self-report is not a determination, but wrong if it implies the CROSS-decidability procedure is unsalvageable; the fix is to require the derivation/checker, which is cheap.

  Specific risks: Over-reading the presumption would demand heavyweight formal proof for every candidate, blocking adoption of even trivially-checkable identities.

  Mitigations available: Require each "identical" verdict to ship a short derivation checked by a CAS or a second, differently-prompted verifier; escalate only genuinely hard identities to full proof.

  STEELMAN:
    Item: PRESUMPTION-555
    Strongest counterargument: "Decidable via agent statement" is defensible when the statement is backed by a checkable derivation; with a verifier in the loop the assertion is not the arbiter, the proof is, and many identities are easy enough that this is cheap. The objection reduces to "attach the checker," not "the procedure is invalid."
    What would need to be true for C2A2 to be safe: every "identical" verdict adopted as CROSS carries a derivation checked by an independent verifier (CAS or decorrelated agent), not the stating agent's word alone.
    How to test: attach a proof-obligation field to the CROSS-decidability step and check whether any candidate was adopted on a bare verdict with no derivation.

  Recommendation: PARTIALLY-CHALLENGED

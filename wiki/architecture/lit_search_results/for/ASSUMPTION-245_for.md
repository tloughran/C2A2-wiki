SEARCH-FOR-ASSUMPTION-245:
  Date searched: 2026-05-29
  Original item: ASSUMPTION-245
  Original statement: The constitutional "no-blind-push" rule held today (5-file changeset staged awaiting Tom's push sign-off; agent did not push autonomously).

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-245
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-28 ship-readiness reasoning; constitutional-rule compliance event.
      15a: Searched for supporting literature on constitutional-rule design in agentic systems and human-in-the-loop push-gate value.
    Current status: SUPPORTED (Moderate-Strong)

  Supporting evidence found: Yes

  Sources:
    1. Christiano et al. (2017) "Deep RL from Human Preferences" — Foundational HITL pattern; gating high-consequence actions on explicit human approval is documented as alignment baseline.
    2. Bai et al. (2022) "Constitutional AI" — Constitutional-rule design with hard constraints supported by Anthropic; the no-blind-push rule fits the constitutional-constraint shape.
    3. Amodei et al. (2016) "Concrete Problems in AI Safety" — Reversibility and human oversight are core safety properties; push-without-approval is documented as a high-blast-radius irreversible action where HITL gates are strongly indicated.
    4. Ngo et al. (2022) "Alignment Problem from a Deep Learning Perspective" — Explicit constraint enforcement (rather than learned preference) is more robust against context drift; constitutional rules with hard gates are documented as preferred for irreversible actions.
    5. C2A2-internal: rule held under deadline pressure today, consistent with the constitutional design intent.

  Strength of support: Moderate-Strong

  Summary: The constitutional "no-blind-push" rule sits squarely within the HITL / Constitutional AI / AI-safety design literature. Anthropic's Constitutional AI, Christiano's preference-based gating, and the broader alignment literature all support hard gates on irreversible high-blast-radius actions. Today's event (rule held under demo-path schedule pressure) is consistent with the design intent. The literature predicts this pattern reduces error blast radius at the cost of latency.

  Caveats: (a) Literature supports the RULE; scaling concerns (the basis of PRESUMPTION-269) lie beyond rule-design literature and inside human-bandwidth literature; (b) "Rule held today" is a single positive observation; literature notes that constitutional rules erode under sustained pressure (PRESUMPTION-269's concern); (c) the "push gate" doubles as a literature-stall route under FLAG-I.

  Recommendation: SUPPORTED (Moderate-Strong) — on rule integrity. Scaling concern is the legitimate worry, but lies with PRESUMPTION-269.

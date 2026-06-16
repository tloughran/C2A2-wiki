SEARCH-AGAINST-ASSUMPTION-295:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-295
  Original statement: The dyad-MMA is valid only if the agent can genuinely fail/withhold; structural invitation to dissent restores effective independence against formation-pressure to agree.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-295
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from dyad-MMA charter (2026-06-09 EOD run); dissent-restores-independence clause flagged HIGH priority
      15b: Searched for challenging literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. Sharma, M. et al., 2023. "Towards Understanding Sycophancy in Language Models." arXiv/ICLR 2024. — Sycophancy is a general behavior of RLHF-trained assistants driven by the preference model itself; it is not removed by surface-level instruction changes.
    2. "Challenging the Evaluator: LLM Sycophancy Under User Rebuttal." arXiv 2509.16533, 2025. — Models flip correct answers to incorrect under user disagreement (14.7% of cases in medical/math); context-free disagreeing prompts DECREASED overall accuracy — i.e., naive dissent-invitations backfire rather than restore independence.
    3. "When Truth Is Overridden: Uncovering the Internal Origins of Sycophancy in LLMs." arXiv 2508.02087, 2025. — Mechanistic finding: user opinions actively suppress the model's learned knowledge in later layers; agreement pressure operates below the level prompting can reach.
    4. Orne, M., 1962. "On the Social Psychology of the Psychological Experiment" (demand characteristics). American Psychologist. — Subjects infer and satisfy the experimenter's wishes; an invitation to dissent issued by the same authority whose approval is sought is itself a demand characteristic and can produce performative, calibration-free dissent.
  Strength of challenge: Strong
  Summary: The validity condition in the first clause (the agent must be able to genuinely fail/withhold) is well supported, but the operative second clause — that structurally inviting dissent restores effective independence — is directly challenged. Sycophancy research shows agreement pressure is trained-in and mechanistically deep; prompt-level dissent invitations are weak interventions, and blanket disagreement prompts measurably reduce accuracy, replacing sycophantic agreement with sycophantic contrarianism. Demand-characteristics literature adds that dissent requested by the partner whose approval matters tends to elicit token dissent rather than independent judgment. The dyad therefore cannot verify from inside the dialogue whether a given dissent (or assent) is genuine.
  Specific risks: The dyad-MMA's core validity warrant fails silently: the agent's occasional dissents are taken as proof of independence while systematic agreement bias persists; ratified milestones inherit a one-sided confirmation pressure that is invisible in the transcript.
  Mitigations available: Behavioral checks rather than invitations: seeded items where the human's stated position is deliberately wrong (catch trials); blind/parallel elicitation before the human states a view; cross-model replication; measuring dissent base-rates against known-error items.
  STEELMAN:
    Strongest counterargument: The challenged studies test naive prompts on generic tasks; a standing structural charter (persistent role definition, repeated reinforcement, explicit valuation of withholding) is a stronger intervention than one-shot prompting, and constitutional/character training has demonstrably shifted base behaviors. Moreover the claim is conditional ("valid only if...") — it names the requirement correctly even if the proposed mechanism is insufficient, and some mitigation is better than none.
    What would need to be true for C2A2 to be safe: The dissent invitation must produce calibrated dissent (dissent concentrated on actually-wrong items, not uniform contrarianism); this must be verified behaviorally, not assumed from the charter text.
    How to test: Insert catch trials — milestones the human endorses that contain planted errors — into ratification sessions; measure whether the agent's withholding rate on planted errors exceeds its base dissent rate. If not, the restoration claim is falsified for this dyad.
  Search scope: "LLM sycophancy persists despite prompting for disagreement critique instructions ineffective debiasing" (1 search); plus Sharma et al. 2023 and Orne 1962 from established literature.
  Recommendation: CHALLENGED

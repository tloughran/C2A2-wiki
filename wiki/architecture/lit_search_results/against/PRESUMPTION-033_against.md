SEARCH-AGAINST-PRESUMPTION-033:
  Date searched: 2026-04-16
  Original item: PRESUMPTION-033
  Original statement: "'Good enough to checkpoint' judgment for wiki_narration.html is an adequate user-facing quality criterion"
  
  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-033
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — unstated adequacy criterion
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes
  
  Sources:
    1. Evaluator-producer separation literature (QA classics, Beizer 1990; software inspections by Fagan 1976): self-assessed quality has documented positivity bias.
    2. LLM-as-judge biases (Zheng et al. 2023): LLM self-evaluation tends toward overly positive scores.
    3. Definition-of-done literature in agile (Rubin 2012): user-facing artifacts require acceptance criteria beyond developer self-assessment.
    4. Software defect-injection studies: self-reviewed artifacts have measurably higher downstream defect rates than peer-reviewed artifacts.
    5. Usability testing literature: user-task completion is the gold standard for user-facing quality, not developer assessment.
    
  Strength of challenge: Moderate-Strong
  
  Summary: The QA literature is clear that self-assessed "good enough" criteria are unreliable for user-facing artifacts, particularly without evaluator-producer separation or user-task completion testing. The criterion is acceptable for internal checkpoints but risks locking in a buggy baseline as the reference point for future rollbacks and comparisons. The presumption becomes particularly risky when the same actor both produces and judges the artifact, as appears to be the case here.
  
  Specific risks: Future rollbacks anchor to a buggy baseline; user-facing bugs persist past the checkpoint; quality signal for subsequent iterations is biased.
  
  Mitigations available: Lightweight external review before checkpointing; user-task completion test; explicit open-defect list attached to checkpoint.
  
  Recommendation: PARTIALLY-CHALLENGED
  
  STEELMAN:
    Item: PRESUMPTION-033
    Strongest counterargument: Self-assessed quality has well-documented positivity bias; user-facing quality without evaluator-producer separation or user-task testing is unreliable. Checkpoints that encode self-assessed adequacy become future baselines, propagating the bias forward.
    What would need to be true for C2A2 to be safe: Explicit open-defect list at checkpoint; user-task completion test; external reviewer or automated quality gate.
    How to test: Have a distinct reviewer or fresh-eyes test user tasks against the checkpointed artifact; count open defects before and after checkpoint.

SEARCH-AGAINST-ASSUMPTION-367:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-367
  Original statement: "That the change signal should flash only for new papers and show a calm 're-checked' on a same-papers re-poll (honesty refinement)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-367
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: signal change only on real change; calm "re-checked" otherwise
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Alarm-fatigue literature. - ANY repeated cue, including a "calm re-checked" badge, can habituate users until even the real "new" flash is ignored; the refinement reduces but does not eliminate desensitization risk.
    2. Signal-detection theory. - The honesty benefit depends entirely on the "new" detector's accuracy: a high false-positive rate flashes "new" on non-new items (crying wolf); a high false-negative rate stays calm on real updates (missed news), silently defeating the honesty goal.

  Strength of challenge: Weak

  Summary: The principle is right; the challenge is conditional. "Flash only on new" is only as honest as the new-vs-same classifier underneath it. If detection misfires, the refinement either reintroduces false alarms or hides genuine updates behind a calm "re-checked" - the latter being a quiet honesty failure that looks fine. And a frequently-shown "re-checked" cue can itself habituate. These are calibration/edge risks, not a refutation; the design is sound provided the detector is validated and the calm cue is not over-displayed.

  Specific risks: Mis-classification flips honest feedback into either crying-wolf or silent-miss; over-shown calm cue causes habituation to the real signal.

  Mitigations available: Validate the new/same detector (the same change-detection rigor as ASSUMPTION-364); rate-limit/soften the "re-checked" cue; expose last-checked timestamp so "calm" is auditable.

  STEELMAN:
    Item: ASSUMPTION-367
    Strongest counterargument: Routing honesty through a derived "new" signal just relocates the honesty problem to the detector: if it is wrong, the UI confidently shows a false state, which is worse than no signal because users trust it.
    What would need to be true for C2A2 to be safe: The new/same classifier's false-positive and false-negative rates are measured and low, and the calm cue does not desensitize.
    How to test: Replay known new-vs-same poll sequences and verify the flash fires iff truly new; measure misclassification.

  Search scope: Alarm fatigue; signal detection. Adequate.

  Recommendation: PARTIALLY-CHALLENGED

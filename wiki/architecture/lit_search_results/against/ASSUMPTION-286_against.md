SEARCH-AGAINST-ASSUMPTION-286:
  Date searched: 2026-06-08
  Original item: ASSUMPTION-286
  Original statement: Policy-layer rules (the 12 CLAUDE.md rules) are waivable; capability/constitutional boundaries (sandbox credentials) are not; a policy rule may coincide with a hard capability wall.

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15b]
    Original item: ASSUMPTION-286
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted as the stated two-layer constraint model.
      15b: Searched for evidence that the waivable/non-waivable layering is unsafe or misleading in practice.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. "Policy is mechanism" critiques / confused-deputy literature (Hardy 1988, "The Confused Deputy"). — Treating policy as cleanly separable from mechanism is where authority bugs live; an agent that regards policy rules as freely waivable can be steered into exercising capability it nominally holds, the classic confused-deputy pattern. Challenges the safety of "policy = waivable."
    2. Safety-rule vs mere-preference conflation (defense-in-depth; "rules as the last cheap guard before an expensive wall"). — Some of the 12 rules (e.g., Rule 1 think-before-coding, Rule 8 read-before-write) are precisely the guards that PREVENT colliding with a hard capability wall; classifying them as "waivable policy" invites the exact build-then-discover failure (PRESUMPTION-318) that occurred.
    3. Goodhart/normalization-of-deviance (Vaughan, "The Challenger Launch Decision"). — Once a class of rules is labeled "waivable," waiving becomes routine; the coincidence case ("a policy rule may coincide with a hard wall") is then most dangerous, because the habit of waiving meets a boundary that does not negotiate.

  Strength of challenge: Weak-Moderate

  Summary: The distinction itself is sound (it is textbook policy/mechanism separation), so the challenge is not to the taxonomy but to its SAFE USE. Three risks: confused-deputy authority bugs when policy is treated as freely waivable; mislabeling load-bearing safety rules as mere policy; and normalization of deviance, where routine waiving collides with the very capability wall the rule was shadowing. The challenge sharpens, rather than refutes, the assumption.

  Specific risks: The agent waives a "policy" rule (e.g., probe-before-build) that was actually the cheap guard in front of a hard wall (no push credential), and so spends effort building automation that the capability layer then (correctly) refuses — the realized 2026-06-07 pattern. The coincidence case is the failure mode, not an edge note.

  Mitigations available: Tag which of the 12 rules are SAFETY-LOAD-BEARING (waive only with explicit justification) vs genuine preferences; treat any rule that shadows a capability boundary as effectively non-waivable; require a stated reason on every waiver (fail-loud, per Tom's Rule 12); prefer probing the capability wall directly over reasoning about whether the policy is waivable.

  STEELMAN:
    Item: ASSUMPTION-286
    Strongest counterargument: The clean "policy waivable / capability not" picture is correct as ontology but hazardous as operating guidance, because the dangerous rules are exactly the ones that LOOK like waivable policy but functionally shadow a hard wall. Calling the 12 rules "waivable" licenses skipping the cheap guard (think first, read first, probe first) and discovering the wall the expensive way. The coincidence case is not a footnote; it is where almost all the realized cost lands.
    What would need to be true for C2A2 to be safe: Each policy rule is annotated for whether it shadows a capability/safety boundary; waivers are explicit, justified, and logged; rules that coincide with hard walls are treated as non-waivable in practice.
    How to test: Audit the 12 rules and mark coincidence-with-capability-wall; check the incident log for cases where waiving a "policy" rule led directly into a capability refusal.

  Recommendation: PARTIALLY-CHALLENGED

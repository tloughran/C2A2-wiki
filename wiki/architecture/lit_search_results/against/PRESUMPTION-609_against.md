SEARCH-AGAINST-PRESUMPTION-609:
  Date searched: 2026-08-01
  Original item: PRESUMPTION-609
  Original statement: [as queued] Cross-run comparison is only a change detector, not a general correctness check; the identical bug passes on a first run, a newly added check, or after legitimate change in the figures; and a no-longer-static corpus is exactly the condition that destroys the detector's power.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-609
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the stated detection route in the nightly verification report
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Metamorphic-relation identification literature — METRIC (Chen et al., JSS 2015); Sun et al., "Identifying metamorphic relations: a data mutation directed approach," SPE 2024; MR-recommendation methods (JKSU-CIS 2026). — MR identification is repeatedly described as difficult, requiring deep domain knowledge of the software under test. The complement the item calls for is not free; the literature's central open problem is precisely obtaining good MRs.
    2. "Measuring Effectiveness of Metamorphic Relations for Image Processing Using Mutation Testing" (PMC11051087); "Fault Detection Effectiveness of Metamorphic Relations" (arXiv 1904.07348); Optimizing MT via execution-profile dissimilarity (arXiv 2411.09171). — Effectiveness is strongly dependent on the quality, appropriateness and diversity of the chosen MRs; a weak MR set gives a passing verdict that carries little information. Substituting an invariant for a comparison can trade a known limitation for a hidden one.
    3. MT false-positive literature (association-rule mining to separate genuine violations from inapplicable MR conditions). — Invariant violations are not self-interpreting; a conservation invariant that fires on a legitimate edge case produces alert fatigue, the failure mode PREMISE-131 already governs.
    4. Barr et al., "The Oracle Problem in Software Testing: A Survey," IEEE TSE 2015 — cited here for the half that challenges the item: derived and pseudo-oracles are catalogued as LEGITIMATE oracle types, widely used, not as a defective substitute for a true oracle. A regression baseline that has itself been verified transmits its warrant forward; the item's argument requires the baseline to be unverified, which it asserts rather than shows.
    5. On the item's second claim: the standard response to a legitimately-changing reference is a golden-file / approval-testing discipline, in which changes are diffed and explicitly approved. Under approval testing, a non-static corpus does not destroy the check's power; it converts it from automatic to reviewed. The item does not consider this option.

  Strength of challenge: Moderate

  Summary: The item's classification is correct and 15b does not contest it — cross-run comparison is a derived oracle and cannot fail on a first run. What is challenged is the practical conclusion drawn from it. First, derived oracles are catalogued in the same survey the item's classification comes from as legitimate, standard, and warrant-transmitting when the baseline is verified; the item treats "derived" as "defective." Second, the remedy implied — add first-run-capable invariants — inherits the metamorphic-testing field's hardest open problem: identifying MRs requires deep domain knowledge, effectiveness varies sharply with MR quality, and weak invariants produce confident-looking passes and false alarms. Third, the item's sharper claim about the no-longer-static corpus overlooks approval/golden-file testing, the standard discipline for exactly that situation, under which change detection retains its power at the cost of requiring review. The net is that the item identifies a real gap and understates the cost and the risk of the fix.

  Specific risks: If C2A2 acts on this by adding invariants without a quality criterion, it acquires checks that pass in the presence of faults (weak MRs) and fire in their absence (inapplicable conditions), while the cross-run check that has actually caught a defect is downgraded. That is a net loss of detection with an increase in perceived coverage — the worst combination.

  Mitigations available: Yes. (a) Keep the cross-run check and add invariants alongside rather than instead. (b) Require each new invariant to be validated by mutation — introduce the known splitter bug and confirm the invariant fires; the literature's own effectiveness measure. (c) Adopt approval-testing discipline for the non-static corpus: diffs are surfaced and explicitly approved, so legitimate change does not silently consume the detector's power.

  STEELMAN:
    Item: PRESUMPTION-609
    Strongest counterargument: The item is right about the taxonomy and wrong about the remedy's cost. Regression comparison is not a poor cousin of a real oracle; it is one of the catalogued oracle types, used everywhere, and its warrant is inherited from a verified baseline — which is a condition to check, not a defect to route around. The proposed complement, first-run-capable invariants, walks into metamorphic testing's central unsolved problem: good relations are hard to find, require deep knowledge of the system under test, and vary enormously in fault-detection power, so an invariant suite assembled without a validation step gives the appearance of first-run coverage without the substance. And the claim that a non-static corpus destroys the check ignores the standard remedy — approval testing — under which a changing reference is handled by reviewing diffs rather than by abandoning comparison. The safe reading is that the check suite needs classification and an added, mutation-validated invariant or two, not that its current basis is unsound.
    What would need to be true for C2A2 to be safe: the nightly baseline is itself verified at least once; any added invariant is mutation-validated before being counted as coverage; the changing corpus is handled by explicit diff approval rather than by silent tolerance.
    How to test: Run the classification the item names (which checks can fail with no prior?), then for each check that cannot, attempt a mutation: reintroduce the splitter defect against a first-run condition and record which checks fire. Order-10 denominator, classification not proportion — decidable, and the mutation step converts it from a taxonomy exercise into a measurement.

  Recommendation: PARTIALLY-CHALLENGED

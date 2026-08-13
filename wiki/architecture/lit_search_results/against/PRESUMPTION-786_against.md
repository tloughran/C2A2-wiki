# PRESUMPTION-786 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-786

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-786

**Original statement:** That an instrument's errors are one-directional — 08-11 found four checks failing open, 08-12 found four extractors failing closed, and each day's remedy is directional.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from two consecutive days finding opposite failure directions and each day's remedy being directional, that the system presumes an instrument errs in only one direction. Residual claim: knowing an instrument is unreliable does not tell you the sign of its unreliability, so a favourable metric movement is uninterpretable without re-deriving the instrument. Risk graded High.
  - 15b: Searched for literature challenging the inference — whether error direction is knowable a priori from analyser design, and whether directional bias is measurable and stable per instrument.
- **Current status:** CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction is that 14b's worry is overstated. Here the challenge is direct: the sign of an instrument's unreliability is very often a *designed and documented property*, readable a priori from the tool's soundness posture and measurable empirically per tool, so the residual claim that direction is unknowable is too strong.

### Challenging evidence found: Yes

### Sources

1. **Livshits, B. et al., 2015. "In Defense of Soundiness: A Manifesto." *Communications of the ACM* 58(2):44–46.** — The central challenge. Practical static analysers deliberately make unsound choices — "there is not a single realistic whole-program analysis tool that does not purposely make unsound choices" — trading soundness for automation, performance and fewer false positives. The manifesto's whole programme is that the nature and extent of unsoundness should be *declared*, via a stated "sound core" plus enumerated unsound features. Direction of error is thus a design decision that can be documented and read off, not an unknowable property.
2. **Christakis, M., Müller, P., Wüstholz, V., 2015. "An Experimental Evaluation of Deliberate Unsoundness in a Static Program Analyzer." VMCAI (Springer, 10.1007/978-3-662-46081-8_19). [author attribution from search snippet; chapter and venue verified].** — Demonstrates the stronger version: sources of deliberate unsoundness in a real analyser (Clousot) were instrumented and *measured*. If unsoundness can be enumerated and quantified for a shipping tool, the claim that direction of error is opaque fails for that class of instrument.
3. **"A Critical Comparison on Six Static Analysis Tools: Detection, Agreement, and Precision." arXiv:2101.08832. [author list not confirmed in search snippets].** — Empirical: precision varies enormously and *stably per tool* — CheckStyle around 86%, SonarQube around 18%, others 29–57% — and pairwise warning-alignment ratios between tools fall under 10%. Directional bias is therefore both large and tool-specific, which means it is a property you can measure once and carry forward, not a fresh unknown at each reading.
4. **Empirical work on false-positive rates in industrial static analysis (e.g. arXiv:2601.18844, "Reducing False Positives in Static Bug Detection with LLMs: An Empirical Study in Industry"; and survey work reporting false-positive rates above 76–90% in some settings).** — Establishes that enterprise tools commonly "prioritise recall over precision to ensure no potential bugs are overlooked," i.e. they are deliberately biased toward false positives. That is a stated directional design posture for a whole tool class.
5. **Standard ROC / precision-recall methodology (e.g. arXiv:2010.16061 on evaluation from precision, recall and F-measure to ROC).** — Supplies the constructive answer the item asks for: a two-sided characterisation of an instrument is routine methodology, requiring a labelled sample rather than a re-derivation of the instrument each time it is read.

### Strength of challenge: Moderate-to-Strong

### Summary

The observation is good — two consecutive days finding opposite failure directions is exactly the kind of pattern worth naming — but the residual claim overshoots. For the instrument class C2A2 actually uses, error direction is largely a designed property. The soundiness literature exists precisely because industrial analysers make *deliberate* unsound choices, and its central recommendation is that those choices be declared; deliberate unsoundness has been enumerated and experimentally quantified in a shipping analyser. Empirically, directional bias is not merely knowable but stable and tool-specific: measured precision across six tools ranges from 18% to 86%, and inter-tool warning agreement is under 10%, which means each instrument has a characteristic and persistent error profile. The two days' findings are therefore consistent with a much less alarming reading than the item's: the four checks that failed open on 08-11 and the four extractors that failed closed on 08-12 are different instrument classes with different design postures — gates written to avoid blocking versus extractors written to avoid over-matching — and their directions are what one would predict from what each was built to do. Most importantly, the item's implied requirement — that a favourable metric movement is uninterpretable without re-deriving the instrument — is far more expensive than the standard remedy, which is to characterise each instrument once on a labelled sample and thereafter read its output against a known error profile.

### Specific risks

If the presumption is adopted at full strength, the operational consequence is that no metric movement can be trusted without re-deriving its instrument, which is unaffordable at the register's cadence and will in practice mean either that the requirement is ignored (producing a documented control that is not performed — the PREMISE-110 pattern again) or that favourable results are discounted while unfavourable ones are not, an asymmetry that is worse than the original problem. If it is dismissed, the hazard is real and specific: a directional remedy applied on 08-11 that tightens gates could have induced the fail-closed extractor behaviour observed on 08-12, and nobody would see the coupling because each day's finding was assessed in one direction only.

### Mitigations available

(a) Declare each instrument's soundness posture at construction — sound-core plus enumerated unsound choices — following the soundiness manifesto's own recommendation. This makes direction knowable a priori for new instruments at negligible cost. (b) Characterise each instrument once against a labelled sample and record precision and recall together; thereafter read outputs against that stored profile rather than re-deriving. (c) After any directional remedy, re-check the *opposite* direction on the instrument that was adjusted — the one genuinely valuable practice the item's observation motivates, and it is cheap because it is scoped to instruments that were just changed. (d) Never report a single-sided figure: a defect count without its companion false-positive or coverage estimate is the actual defect in the 08-11/08-12 sequence.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-786

**Strongest counterargument:** The sign of an instrument's error is usually a design decision, and treating it as unknowable throws away information the builder already has. Every realistic whole-program analyser makes purposeful unsound choices, and the field's own manifesto asks tool authors to declare which — meaning direction is documentable at construction time. It has been done: deliberate unsoundness in a shipping analyser was instrumented and measured. Empirically the profile is stable per tool and large — precision measured at 86% for one tool and 18% for another in the same study, with inter-tool agreement under 10% — so an instrument's directional bias is a durable property you measure once, not a fresh unknown at each reading. The 08-11 and 08-12 findings fit this comfortably: gates and extractors are different instrument classes built to fail in opposite directions, and finding them doing so is confirmation rather than surprise. The item's residual claim — that a favourable metric movement is uninterpretable without re-deriving the instrument — is the expensive form of a cheap requirement. The cheap form is: characterise every instrument two-sidedly once, publish the profile, and never report a one-sided figure. That delivers everything the item wants at a fraction of the cost, and unlike a re-derivation mandate it will actually be performed.

**What would need to be true for C2A2 to be safe:** Each instrument must carry a stored two-sided profile (what it is designed to miss, what it is designed to over-report, and a measured estimate of each), and every reported figure must be accompanied by the relevant side of that profile. Given those, a favourable movement is interpretable directly. Absent them, the item's worry is live — but the deficiency is a missing profile, not an epistemic impossibility.

**How to test:** Take the four checks found failing open on 08-11 and the four extractors found failing closed on 08-12 and, for each, ask whether its design intent predicted its direction. If the directions were predictable from what each instrument was built to do, the presumption is overstated and the fix is documentation of soundness posture. A second test, more valuable: for the instruments adjusted on 08-11, measure the opposite-direction error rate before and after the remedy. If tightening the gates raised the fail-closed rate in the extractors, the item has found something more specific and more serious than it claims — a coupling between directional remedies — and that is worth pursuing on its own terms.

---

## Search scope

Moderate. Query families executed: soundiness and deliberate unsoundness in static analysis; empirical false-positive and precision measurements across tools; ROC and precision-recall evaluation methodology. Two citations carry unconfirmed author lists and are marked. Not searched: the base-rate literature on defect detection named in the item's search strategy (the effect of low prevalence on positive predictive value, which is a genuine and possibly strong further consideration), and calibration literature in machine learning. Broader search recommended, particularly on base rates, which could partly restore the item's position.

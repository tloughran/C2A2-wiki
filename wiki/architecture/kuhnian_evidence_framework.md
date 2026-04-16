# Evidence Quality and Kuhnian Paradigm Detection

*Architectural Analysis | Documented: 2026-04-15 | Initiated in morning session: 2026-04-14*

---

## The Problem with PRESUMPTION-007

**PRESUMPTION-007** states: "Literature absence = novel." The underlying logic is straightforward: if nobody in the literature has written about Interpretation X, then X is novel or under-explored, signaling potential research value.

**This presumption breaks during paradigm shifts.**

During revolutionary science (per Kuhn, 1962), the distinguishing feature is precisely that the new paradigm lacks developed literature because it has not yet achieved scientific legitimacy. The absence of literature is not evidence of novelty—it is evidence of *paradigm emergence*. And the existing literature, written by defenders of the old paradigm, will often produce *faint or mixed evidence against* the new paradigm's claims, not because the claims are wrong, but because the old paradigm lacks conceptual vocabulary to evaluate them.

---

## Reframing Evidence Signals During Paradigm Shift

The morning session established a **four-category evidence framework** that reinterprets what "strong against" vs. "faint against" actually signal:

### Evidence Pattern 1: Strong FOR + No AGAINST
**Interpretation**: Ordinary science (likely incremental)
- The finding is well-established in current literature.
- No literature challenges it (because it is not contested).
- **Implication**: Solid grounding, low risk of error, but likely incremental rather than revolutionary.
- **Action**: INCORPORATE (into validated premises) with confidence; plan for routine synthesis.

### Evidence Pattern 2: Strong FOR + Strong AGAINST
**Interpretation**: Contested territory (active debate, productive tension)
- Multiple research groups actively dispute the claim.
- Literature is rich on both sides.
- **Implication**: Active research frontier; legitimate disagreement; hypothesis may be contingent on field/method.
- **Action**: MONITOR or flag as CONDITIONAL; highlight the disputed framing in cross-tradition synthesis.

### Evidence Pattern 3: Mixed FOR + Faint AGAINST
**Interpretation**: **Potential paradigm-shift signal** (the new paradigm is emerging)
- Supporting evidence exists but is scattered, preliminary, or from interdisciplinary sources.
- Evidence against it is faint because the old paradigm lacks vocabulary to fully engage with the new paradigm's claims.
- Existing literature pushes back weakly—not from empirical refutation, but from conceptual misalignment.
- **Implication**: The new paradigm is forming in the literature; the old paradigm's faint pushback is a sign of incommensurability, not falsification.
- **Action**: **REVISE into MONITOR**. This is the most interesting signal. Do not reject it as "weak evidence." Instead, treat it as a candidate for paradigm-shift tracking (OPEN-015).

### Evidence Pattern 4: No FOR + Strong AGAINST
**Interpretation**: Likely wrong (the system generated a bad connection)
- The claim has no supporting literature whatsoever.
- Multiple sources actively challenge it (or challenge related claims).
- **Implication**: The hypothesis is either ill-formed or genuinely falsified by evidence.
- **Action**: REJECT or flag for deep human review (may need complete reconceptualization).

---

## The Levin/Hoffman Trace Logic as Exemplar

The morning session used the **Levin/Hoffman trace logic** (information integration as trace geometry in cognitive systems) as a concrete example of Pattern 3 evidence:

- **FOR (mixed)**: 
  - Levin's work on "minimal cognition" in slime molds and T-cell networks (strong within his papers).
  - Hoffman's "interface theory of perception" (established in perception literature, but niche).
  - A few interdisciplinary papers cite both authors' frameworks in novel combinations.
  
- **AGAINST (faint)**: 
  - Classical neuroscience literature does not broadly engage with trace-geometry reformulation.
  - Cognitive science textbooks do not feature this as a standard model.
  - The faintness is not due to empirical refutation; it is due to the old paradigm not yet recognizing this as a canonical question.

**Signal interpretation**: This is Pattern 3. The mixed FOR + faint AGAINST pattern is precisely what we should expect when a new paradigm is emerging *across disciplinary boundaries*. The absence of widespread literature engagement is not evidence of novelty to be skeptical of; it is evidence of *boundary-crossing* that existing disciplinary silos have not yet integrated.

**Implication for Phase 2a agents**: Levin-A, Levin-B, and Levin-C might legitimately disagree on whether Levin/Hoffman trace logic is "paradigm-shifting" vs. "speculative but underdeveloped." Pattern 3 evidence should *not* be filtered out by high-consensus thresholds; it should be *flagged* as containing the most interesting dissents.

---

## Reframing the Self-Awareness Pipeline (15a/15b/15c)

The **15a/15b/15c pipeline** currently interprets evidence patterns to disposition items (INCORPORATE, MONITOR, REVISE). The Kuhnian framework requires recalibrating this pipeline:

### Current 15c Disposition Logic (Pre-Kuhnian)

- **Strong FOR + Strong AGAINST** → MONITOR (contested, but let's revisit)
- **Mixed FOR + Faint AGAINST** → REVISE (weak evidence, needs human review)
- **Mixed FOR + No AGAINST** → INCORPORATE (tentatively grounded)

**Problem**: Pattern 3 (Mixed FOR + Faint AGAINST) is treated as weak and pushed to REVISE. But this pattern is precisely the *most interesting signal* during paradigm shift.

### Revised 15c Disposition Logic (Kuhnian-Aware)

- **Strong FOR + No AGAINST** → **INCORPORATE** (ordinary science, well-grounded)
- **Strong FOR + Strong AGAINST** → **MONITOR** (active frontier, productive tension)
- **Mixed FOR + Faint AGAINST** → **MONITOR** (paradigm-shift candidate, flag for OPEN-015 tracking; do NOT treat as weak evidence)
- **No FOR + Strong AGAINST** → **REVISE** (genuine falsification or ill-formed hypothesis)

The key change: **Mixed FOR + Faint AGAINST moves from REVISE to MONITOR**, and is treated as a signal worth preserving and analyzing, not as evidence of weakness.

---

## Connection to Paradigm-Shift Detector Concept (OPEN-015)

This evidence framework operationalizes **OPEN-015: "Paradigm shift detector."** The detector should identify items with Pattern 3 evidence and track them separately:

### Paradigm-Shift Signal Detection via Evidence Pattern

For each item passing through 15a/15b, 15c can calculate:

```
PATTERN_SIGNAL = (
  FOR_strength ∈ [Faint, Moderate, Strong] AND
  AGAINST_strength ∈ [Faint, None] AND
  interdisciplinary_boundary_crossing = True
)
```

Items matching this pattern are candidate paradigm-shift signals. They should be:
1. **Tagged** as Pattern 3 in the metadata.
2. **Monitored separately** from routine items.
3. **Tracked for citation emergence** over the next 6-12 months to see if a new literature cluster forms around them.

### Empirical Paradigm-Shift Tracking via Literature Metrics

OPEN-015 proposes tracking paradigm shifts through:

1. **Co-authorships across disciplines**: Are authors from disparate fields suddenly publishing together on the Levin/Hoffman trace logic? If yes, paradigm is emerging.

2. **Citation network topology**: Do pattern-3 items suddenly begin citing each other and forming a new cluster? Network clustering metrics can detect this automatically.

3. **Keyword emergence**: Do new compound keywords (e.g., "trace geometry + cognition," "interface theory + minimal cognition") emerge in titles and abstracts over time? This is a linguistic signal of paradigm formation.

The Kuhnian framework justifies why these metrics matter: they detect the *incommensurability phase* where old paradigm and new paradigm are both publishing but in distinct vocabularies.

---

## ASSUMPTION-019 and Its Operationalization

The morning session articulated **ASSUMPTION-019** (not yet formalized in the assumptions registry):

> "During paradigm shifts, literature absence is expected and is not evidence of weakness. Mixed evidence against a finding, during a paradigm-shift phase, may actually be evidence for novelty—because revolutionary science is precisely the kind of work that existing literature would challenge or fail to understand."

The Kuhnian framework **operationalizes** this assumption:

1. **Detection**: Pattern 3 evidence (Mixed FOR + Faint AGAINST + interdisciplinary) signals paradigm-shift phase.
2. **Interpretation**: Faint AGAINST is reinterpreted as incommensurability signal, not falsification.
3. **Action**: Items showing this pattern are preserved, monitored, and tracked via citation networks.
4. **Validation**: In 6-12 months, check whether Pattern 3 items became paradigm leaders (heavily cited, new literature cluster formed) or remained marginal.

If Pattern 3 items consistently show high citation emergence, ASSUMPTION-019 is **empirically validated**. If they remain marginal, ASSUMPTION-019 is **challenged** and may need revision (e.g., "maybe paradigm shifts are rarer than Kuhn suggests, or our pattern-detection is over-inclusive").

---

## Implications for 15c Disposition Heuristics

### Current REVISE Threshold Problem

The current 15c heuristics treat Mixed FOR + Faint AGAINST as problematic—evidence is "mixed," which signals to escalate. But under the Kuhnian framework, this pattern is the *most theoretically interesting*.

### Proposed Calibration

Recalibrate 15c disposition thresholds:

| Disposition | Current Rule | Kuhnian Revision |
|---|---|---|
| INCORPORATE | Strong FOR, no AGAINST | Strong FOR, no AGAINST *(unchanged)* |
| MONITOR | Mixed evidence, active debate | Mixed FOR + Faint AGAINST + interdisciplinary *(elevated priority)* |
| REVISE | Mixed evidence, weak support | No FOR + Strong AGAINST *(falsified or ill-formed)* |

**Key change**: The current REVISE threshold is **too sensitive**. It treats mixed evidence as problematic when mixed evidence may be the most revealing signal. By moving Pattern 3 items to MONITOR (with paradigm-shift flagging), we preserve the most interesting hypotheses rather than filtering them out.

### Risk Mitigation

The concern: "Won't this allow more false or speculative items to slip through?"

**Mitigation**: Pattern 3 items are *flagged* as paradigm-shift candidates. They enter MONITOR, not INCORPORATE. They are isolated for separate tracking (OPEN-015). Human reviewers see them marked as high-interest speculation, not as well-grounded findings. The distinction preserves caution while preventing premature rejection.

---

## Related Architectural References

- **PRESUMPTION-007**: "Literature absence = novel" — challenged and reframed by this document.
- **DECISION-006**: Agents 15a (FOR) and 15b (AGAINST) search independently. The Kuhnian framework reinterprets what AGAINST results mean during paradigm shift.
- **DECISION-012**: Agent 15c dispositions items. This framework recalibrates 15c heuristics.
- **OPEN-004**: Agent differentiation. Levin-A, Levin-B, Levin-C may legitimately disagree on whether Levin/Hoffman claims are paradigm-shifting; this should be preserved as dissent, not filtered out.
- **OPEN-015**: Paradigm-shift detector (proposed new open question). This framework provides the operational definition for OPEN-015.
- **ASSUMPTION-017**: "AI does first-pass synthesis with humans as validators." The Kuhnian framework refines the AI phase: AI should preserve paradigm-shift signal items rather than filtering them out as weak evidence. Humans validate which signals are genuine paradigm shifts.

---

## Kuhn References & Grounding

The framework draws on:
- **Kuhn, T. S. (1962). The Structure of Scientific Revolutions.** Paradigm shifts are characterized by incommensurability and puzzle-solving within new frameworks that old paradigms cannot fully articulate.
- **Lakatos, I. (1970). Falsification and the Methodology of Scientific Research Programmes.** Research programs defend their core commitments against anomalies; absence of challenge from a program doesn't mean the program is weak—it may mean the program hasn't been engaged with yet.
- **Polanyi, M. (1962). Personal Knowledge.** Scientific knowledge is embedded in disciplinary tradition; interdisciplinary boundary-crossing often appears peripheral to each discipline until a new paradigm achieves legitimacy.

---

## Expected Outcomes & Milestones

| Milestone | Target Date | Action |
|---|---|---|
| 15c heuristics recalibrated per Kuhnian framework | 2026-04-16 | Tom reviews and approves revised disposition rules |
| Pattern 3 items tagged in monitoring queue | 2026-04-17 onward | As 15a/15b results come in, 15c flags Pattern 3 items as paradigm-shift candidates |
| OPEN-015 paradigm-shift detector initialized | 2026-04-21 | Specification written; citation network metrics baseline established |
| 6-month citation emergence check | 2026-10-15 | Measure whether Pattern 3 items show higher citation growth than baseline |

---

## Open Questions

1. **Pattern-3 specificity**: Is the Pattern 3 formula (Mixed FOR + Faint AGAINST + interdisciplinary) sufficiently specific, or will it over-flag items? Requires empirical calibration after first batch of 15a/15b results.

2. **Faintness threshold**: How faint should AGAINST evidence be to count as "paradigm-shift signal" rather than "just weak evidence"? Needs quantification (e.g., < 2 papers, OR citations < threshold, OR recency bias in the literature).

3. **Interdisciplinary boundary detection**: How do we automatically detect "interdisciplinary boundary-crossing"? Requires co-author institution classification and citation network analysis.

4. **Paradigm vs. false positive**: If Pattern 3 items are preserved via MONITOR, how do we prevent the system from treating speculative dead-ends as paradigm signals? Requires rigorous validation of citation emergence metrics in 6-12 months.

---

*Last updated: 2026-04-15*  
*Initiated from: Morning walk discussion, 2026-04-14*  
*Status: FRAMEWORK ESTABLISHED, AWAITING 15c CALIBRATION*

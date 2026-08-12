# PRESUMPTION-767 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-767

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-767

**Original statement:** That the noise is always upstream — every repair method in the corpus assumes the ASR is the noisy side, and on five files the render was.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from five files where the rendered artefact, not the ASR output, was the corrupted side, that every repair method encodes a fixed error direction; risk graded High.
  - 15b: Searched for challenging literature on direction-agnostic transcript combination, reference-free quality estimation, and error models that do not designate a noisy side.
- **Current status:** CHALLENGED

**What is being challenged:** the universality claim — "every repair method in the corpus assumes the ASR is the noisy side." Direction-agnostic combination methods are standard, well-established, and available; the constraint is a property of the local corpus, not of the field.

### Challenging evidence found: Yes

### Sources

1. **NIST ROVER (Recognizer Output Voting Error Reduction), NIST SCTK documentation (github.com/usnistgov/SCTK, doc/rover/rover.htm); originating paper Fiscus, 1997 — [originating-paper citation unverified; the SCTK implementation and its documented algorithm are verified].** — ROVER aligns two or more hypothesis transcripts into a word transition network and resolves each bin by voting. It designates no noisy side and requires no gold standard: correctness is inferred from agreement across independently-erring sources. This is a direct counterexample to the universality claim and it has been standard tooling for roughly three decades.
2. **"MOVER: Combining Multiple Meeting Recognition Systems." arXiv:2508.05055.** — A current extension of the same idea to meeting transcription, explicitly premised on the observation that "each system has different error patterns" so that combination can beat any single input. Establishes that direction-agnostic combination is live, contemporary practice rather than a historical curiosity.
3. **"Automatic quality estimation for ASR system combination." *Computer Speech & Language* (doi:10.1016/j.csl.2016.xx — ScienceDirect S0885230816300328); preprint arXiv:1706.07238.** — Estimates the quality of each candidate transcript *without a reference*, which allows the noisy side to be identified empirically per file rather than assumed. This supplies exactly the missing capability the presumption describes, off the shelf.
4. **Search-result note on reference-free evaluation: "some tools allow users to perform ASR evaluation bypassing the need of reference transcripts" — [unverified — from search snippet].** — Corroborates that the field does not require a designated ground truth to score competing artefacts.

### Strength of challenge: Strong

### Summary

The observation (five files where the render was the corrupted side) stands; the universality claim does not. Speech-processing methodology has had direction-agnostic transcript combination since the mid-1990s: ROVER and its descendants align multiple hypotheses and vote per token, making no assumption about which source is noisy, and reference-free quality estimation can rank candidate artefacts on a per-file basis without any gold standard at all. Both capabilities are exactly what the presumption says the corpus lacks, and both are available as established tooling rather than research directions. The correct reading of the finding is therefore narrower and more actionable than the presumption states: C2A2's *local* repair corpus happens to encode a fixed error direction, and the fix is to import a standard direction-agnostic method, not to develop a new epistemology of derived artefacts. A residual caution: ROVER-style voting needs three or more independently-erring sources to be effective and degrades toward arbitrary tie-breaking with two, so a two-artefact setup (ASR plus render) is the weak case for combination and reference-free quality estimation is the better fit there.

### Specific risks

If the presumption's universality framing is accepted, C2A2 may treat the both-sides-derived problem as unsolved and build bespoke machinery, duplicating three decades of standard tooling at cost and with worse error characteristics. If the observation is dismissed along with the framing, the five corrupted renders continue to be treated as ground truth and repair runs in the wrong direction — the specific harm being that a correct ASR token gets overwritten by a corrupted rendered one, which is a silent quality regression that no downstream check would flag.

### Mitigations available

(a) Adopt per-file reference-free quality estimation to identify the noisy side empirically before repairing — this is the direct fix and the literature supplies it. (b) Where a third derived artefact can be produced cheaply (a second ASR pass, or a re-render), use ROVER-style voting, which needs no direction assumption at all. (c) At minimum, add a symmetry check: run the repair in both directions and flag files where the two directions disagree materially, which surfaces exactly the five-file class without requiring any new theory.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-767

**Strongest counterargument:** A speech-processing engineer would say the presumption has correctly diagnosed a local defect and then over-generalised it into a field-level gap that does not exist. The claim that every repair method assumes a noisy side is false as a statement about the discipline: ROVER has been in NIST's standard toolkit since the 1990s precisely because it makes no such assumption — it treats every input as fallibly derived, aligns them, and votes — and reference-free quality estimation lets you rank two derived artefacts against each other with no gold standard whatsoever. So the finding is real but its scope and its remedy are both smaller than stated: C2A2 chose a directional method, and the correction is to swap in a standard non-directional one. Framing this as a High-severity conceptual gap risks a bespoke build where a well-tested import is available, and bespoke error-direction machinery is exactly the kind of instrument that ends up in the never-failed-check category flagged elsewhere in this batch.

**What would need to be true for C2A2 to be safe:** Repair must not be applied in a fixed direction. Either a per-file quality estimate must select the authoritative side before repair, or a third independently-derived artefact must exist so that voting can replace direction selection. Either condition removes the exposure; neither requires new theory.

**How to test:** Take the five files where the render was the noisy side, plus a matched sample where the ASR was, and run a reference-free quality estimator on both artefacts of each pair. If the estimator ranks the correct side authoritative on all ten, the off-the-shelf fix is sufficient and the challenge holds decisively. Additionally, run the existing repair in both directions across the whole corpus and count disagreements — that count is the true size of the affected population, which the presumption currently estimates at five with unknown recall.

---

## Search scope

Moderate. Query families executed: ASR system combination and voting; reference-free quality estimation. Not searched: the ASR post-correction / error-model literature named in the item's search strategy, and the record-linkage literature on latent-truth models with multiple fallible sources, which would further strengthen the challenge. Broader search recommended but the counterexample is already decisive against the universality claim.

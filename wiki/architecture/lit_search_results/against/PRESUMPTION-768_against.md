# PRESUMPTION-768 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-768

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-768

**Original statement:** That a check which has never failed is working — four fail-open instruments found in one day, and no negative control exists anywhere in the architecture.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from four same-day fail-open findings that the architecture nowhere establishes that any check is capable of failing; risk graded Critical.
  - 15b: Searched for challenging literature on mutation testing and fault injection economics, negative/positive control methodology and its caveats, and the deliberate-design justification for fail-open behaviour.
- **Current status:** PARTIALLY-CHALLENGED

**What is being challenged:** not the existence of the fail-open failure mode (that is well attested), but (a) the inference that *absence of a negative control* is itself a Critical defect, and (b) the implied remedy that negative controls should be installed architecture-wide.

### Challenging evidence found: Partial

### Sources

1. **"Negative controls: concepts and caveats." *Statistical Methods in Medical Research*, 2023 (doi:10.1177/09622802231181230).** — Negative controls can indicate the presence of bias but generally cannot establish its direction, magnitude, or absence without additional untestable assumptions; a control that does not meet its assumed structural definition is an insensitive or inappropriate diagnostic. Directly challenges the premise that adding negative controls would resolve the exposure. *(Journal and DOI confirmed from result; author list not confirmed — [unverified authors].)*
2. **"Pitfalls of Using Negative Control Outcomes in Environmental Epidemiology." *Current Environmental Health Reports*, 2025 (doi:10.1007/s40572-025-00513-7).** — A null result on a negative control "may give researchers false confidence that they have adequately controlled for bias when they have not," because real negative controls are rarely perfectly comparable to the primary outcome. This is the exact recursion: a negative control that never fires becomes the next never-failed check.
3. **"What It Would Take to Use Mutation Testing in Industry — A Study at Facebook." arXiv:2010.13464.** — The canonical technique for proving a check *can* fail is judged impractical at industrial scale without heavy selection and workflow integration; the literature's consistent position is that mutation coverage is too expensive to apply uniformly, and selective mutation (reported up to 77% mutant reduction) is the practical compromise. Challenges "no negative control exists *anywhere*" as a defect standard: uniform coverage is not the professional norm.
4. **Fail-open/fail-closed design literature (Keysight network-visibility primer; Cisco Community fail-open/fail-close note; Wikipedia "Fail-safe") — [unverified — practitioner sources from search snippets].** — Fail-open is frequently a deliberate, documented risk decision that prioritises availability or continuity over enforcement. An instrument being fail-open is therefore not per se a defect; the defect is an *undocumented* failure state. Challenges the counting of "four fail-open instruments" as four defects rather than four unexamined design decisions.

### Strength of challenge: Moderate

### Summary

The literature does not contradict the underlying worry — silent, non-executing checks are a real and well-documented class — but it substantially challenges both the severity grading and the implied fix. Negative-control methodology is explicitly a bias-*detection* tool with known limits: methodologists warn that a passing negative control produces false confidence when the control's structural assumptions do not hold, which means installing negative controls would reproduce PRESUMPTION-768 one level up rather than close it. Mutation testing, the software analogue of a positive control, is documented as impractical at uniform scale; the industry norm is selective, prioritised application, so "no negative control exists anywhere" describes the modal software system rather than an outlier. Finally, fail-open behaviour is a legitimate design choice in availability-sensitive contexts, so the count of four fail-open instruments does not by itself establish four faults; it establishes four unrecorded failure-state decisions, which is a documentation finding rather than a Critical correctness finding.

### Specific risks

If the presumption is accepted at Critical severity as stated, C2A2 risks committing to architecture-wide negative controls — an expensive, uniform verification programme that the methodological literature says will itself go untested and will emit reassuring nulls under violated assumptions. The concrete failure is a second generation of never-failed checks with higher confidence attached to them, plus displaced effort from cheaper, higher-yield measures. The converse risk if the presumption is *wrong* in the other direction is small: the cost of documenting failure states is low.

### Mitigations available

Three, in increasing cost: (a) require every instrument to declare its failure state (fail-open/fail-closed) and the justification, which converts the finding from correctness to documentation at near-zero cost; (b) apply positive controls selectively — a single deliberately-broken input per instrument per release, the selective-mutation pattern — rather than a uniform negative-control regime; (c) where a negative control is installed, record the structural assumption it depends on alongside its result, per the SMMR caveats paper, so a passing control is not read as absence of bias.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-768

**Strongest counterargument:** A methodologist would say the presumption commits the error it diagnoses. It treats "no negative control" as the defect, when the negative-control literature's central finding is that negative controls are weak, assumption-laden instruments that most often fail *reassuringly* — they detect bias sometimes, never rule it out, and mislead precisely when their structural assumptions are unmet. Coupled with the mutation-testing economics literature, which finds that even well-resourced industrial engineering organisations cannot afford uniform proof-that-a-check-can-fail, the honest reading is that C2A2's condition is the normal engineering condition, not a Critical anomaly, and that the four fail-open instruments are better treated as four undocumented design decisions than as four faults. Grading this Critical mis-allocates the system's scarce remediation capacity toward the least tractable and most self-deceiving of the available fixes.

**What would need to be true for C2A2 to be safe:** Each instrument's failure state must be declared and justified in writing, and at least the small subset of instruments whose output gates irreversible action must carry a periodic positive control (a known-bad input that must produce a failure). Under those two conditions the absence of architecture-wide negative controls is a tolerated, bounded limitation rather than an unbounded exposure.

**How to test:** Enumerate every instrument that emits a PASS/VERIFIED/NO-FINDINGS token; for each, inject one known-bad input and record whether the instrument fails. The distribution of results is the empirical answer, and it is cheap. If the fail-open rate materially exceeds four, the presumption is corroborated at Critical; if the four are the population and all four are on non-gating instruments, the challenge holds.

---

## Search scope

Preliminary-to-moderate. Four query families executed (mutation-testing economics; negative-control caveats; fail-open design rationale; silent-failure taxonomy). Not searched: formal software-verification literature on vacuous assertion detection, and the Byzantine-detector literature. Broader search recommended before acting on severity.

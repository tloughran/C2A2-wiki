# PRESUMPTION-773 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-773

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-773

**Original statement:** That items in the assumption register are independent of one another — the first internal contradiction in the register was found by an outbound agent, not by any instrument that reads it.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from the fact that no register-reading instrument detected a contradiction that an outbound agent found, that the architecture treats register items as mutually independent; risk graded High.
  - 15b: Searched for challenging literature on inconsistency tolerance in large specification and knowledge bases and on the tractability of global consistency checking.
- **Current status:** CHALLENGED

**What is being challenged:** the implied defect. The requirements-engineering literature holds that inconsistency in large assertion sets is normal, frequently *deliberately* tolerated, and that the goal is management rather than elimination; and that detection at the point of use is an accepted mechanism, not a failure of the repository.

### Challenging evidence found: Yes

### Sources

1. **Nuseibeh, B. et al., 2001. "Making inconsistency respectable in software development." *Journal of Systems and Software* (ScienceDirect S016412120100036X).** — The canonical statement: "the problem is not with inconsistency per se, but with inconsistency that remains undetected," and "in many cases, developers may wish to tolerate a known inconsistency." Practitioners "live with inconsistency as a matter of course" and choose to tolerate it depending on cause and impact. This directly challenges the presumption's premise that an undetected contradiction in a large register is a High-severity architectural fault: undetected-until-relevant is the documented professional norm.
2. **Gabbay, D. & Hunter, A., "Making inconsistency respectable" (the originating formulation, referenced in the above literature) — [unverified — attribution from search snippet].** — Establishes the research programme of representing and reasoning with inconsistent information rather than requiring consistency as a precondition, i.e., paraconsistent handling as the intended posture for large knowledgebases.
3. **"A Systematic Approach for Managing Inconsistency in Software Requirements" (academia.edu / ResearchGate, author list unconfirmed) — [unverified — from search snippet].** — Reports the field's shift "from consistency management to management of consistency" because "any development of a large and complex software system involves management of inconsistencies." Reframes the finding as expected rather than exceptional.
4. **Scale argument (analytic, not cited).** — The register is on the order of a thousand items across assumptions and presumptions; exhaustive pairwise contradiction checking is on the order of 5×10⁵ comparisons per pass and grows quadratically, and semantic contradiction between natural-language items is not decidable by any cheap procedure. That no instrument performs this check is a resource decision consistent with the literature's position, not an oversight — and the literature's prescribed alternative is exactly detection at the point of use, which is what happened.

### Strength of challenge: Moderate

### Summary

The observation is accurate and its interpretation is contested by the mainstream of requirements engineering. Since Nuseibeh and colleagues, the field's position has been that inconsistency in large specification sets is unavoidable, that eliminating it is neither achievable nor always desirable, and that the operative distinction is between inconsistency that remains undetected when it matters and inconsistency that is surfaced at the point where it bears on a decision. On that framing, a contradiction discovered by an outbound agent — an agent actually *using* the items — is the mechanism working, not the repository failing. The tractability argument reinforces this: exhaustive semantic contradiction detection across a register of this size is expensive and unreliable, which is why the literature recommends localised, use-triggered checking. The presumption retains force in one narrower respect it does not currently state: there is no *record* of the contradiction once found, and no mechanism to prevent the same contradiction being consumed again by a different agent tomorrow. That is a memory gap rather than a detection gap, and it is the part worth fixing.

### Specific risks

If the presumption drives a global consistency-checking instrument, the likely outcome is an expensive, low-precision checker whose false-positive rate makes it ignorable — the Tricorder threshold literature puts developer abandonment at roughly a 10% false-positive rate, and semantic contradiction detection over natural-language items will be far worse than that. The instrument then becomes a never-failed check in the sense of PRESUMPTION-768, with the added cost of having consumed the remediation budget. If the finding is dismissed entirely, contradictions continue to be rediscovered independently by successive agents at recurring cost, and — the real hazard — a contradiction may be resolved differently by two agents, producing divergent downstream conclusions from the same register.

### Mitigations available

(a) Record resolutions: when a contradiction is found at point of use, write a CONTRADICTION note linking both items, so the finding is not re-derived. This is the Nuseibeh-consistent fix — tolerate, but never undetected twice. (b) Add cross-references between items known to bear on each other, so the dependency structure the presumption says is missing accumulates incrementally from use rather than from exhaustive analysis. (c) If any automated checking is added, scope it to a narrow, high-precision class (e.g. numeric claims about the same quantity, which is decidable and cheap) rather than general semantic contradiction.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-773

**Strongest counterargument:** Requirements engineering settled this question two decades ago and settled it against the presumption. Nuseibeh's position — that the problem is undetected inconsistency, not inconsistency, and that practitioners routinely and rationally tolerate known inconsistencies — describes C2A2's situation exactly: a register of roughly a thousand natural-language assertions will contain contradictions, exhaustive pairwise semantic checking is quadratic and undecidable in practice, and the field's prescribed mechanism is surfacing at the point of use. An outbound agent finding the contradiction while actually using the items is therefore the designed behaviour of a mature approach, not the failure of an immature one. Grading it High and pointing at a global consistency instrument selects the one intervention the literature predicts will be too imprecise to survive contact with users, and which would itself become an unfalsified check. The finding's real content is much smaller and much better: the contradiction was found and then not written down, so it will be found again.

**What would need to be true for C2A2 to be safe:** Contradictions found at point of use must be recorded against both items with their resolution, so that no contradiction is discovered twice and no two agents resolve the same contradiction differently. Given that, tolerated inconsistency is a managed state and the absence of a global checker is a defensible resource decision.

**How to test:** Take the contradiction the outbound agent found and check whether any record of it now exists in the register. If not, the memory gap is confirmed and is the actionable finding. Then, as a bounded probe of the detection question, run a cheap high-precision check over a decidable subclass — every pair of items making numeric claims about the same quantity — and count contradictions. If that narrow check yields many, a scoped instrument is justified; if it yields few, the tolerate-and-record posture is adequate and the challenge holds.

---

## Search scope

Moderate. Query families executed: inconsistency tolerance in software development; inconsistency management in requirements. Not searched: belief-revision and paraconsistent-logic primary literature, and the ontology-debugging/justification literature (OWL inconsistency explanation), both named in the item's search strategy. Broader search recommended; both would likely reinforce the tractability half of the challenge.

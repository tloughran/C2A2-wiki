# PRESUMPTION-784 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-784

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-784

**Original statement:** That a change requiring no new tool, prompt or schema is not an architectural commitment — three T1 tabs, no DECISION, thirty-eighth day.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from three T1 tabs added on the thirty-eighth day with no DECISION record, that the system uses implementation cost (new tool / prompt / schema) as its trigger for recording an architectural commitment, and that this proxy misses commitments that are cheap to build and expensive to reverse; risk graded Medium.
  - 15b: Searched for literature challenging the inference — the criteria practitioners actually use to trigger an architecture decision record, and the documented costs of lowering that threshold.
- **Current status:** PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction is that 14b's worry is overstated or mis-scoped. Here the challenge is that the established trigger criterion is neither implementation cost nor "is it architecture," but *reversibility and blast radius*, and by that criterion three tabs may correctly fall below the threshold — while lowering the threshold has a documented failure mode.

### Challenging evidence found: Partial

### Sources

1. **Nygard, M., 2011. "Documenting Architecture Decisions." [blog post — the originating ADR reference; non-peer-reviewed but canonical].** — Establishes the scope term "architecturally significant," which is the field's actual trigger and which is defined by consequence, not by build cost.
2. **Google Cloud Architecture Center, "Architecture decision records overview" (docs.cloud.google.com/architecture/architecture-decision-records).** — Current mainstream guidance. Triggers given: the decision is difficult to reverse; it affects multiple teams or services; it involves significant trade-offs; there is no existing basis for the decision. None of these is "new tooling was required." This *supports* 14b's diagnosis that build cost is the wrong proxy, and simultaneously challenges the inference drawn from it, because by the same list a change of narrow scope, low risk and easy reversal is explicitly outside the threshold.
3. **Consolidated ADR practitioner guidance (2024–2026 collections, incl. architecture-decision-record GitHub corpus and Catio/Archyl guides).** — Explicit exclusion criteria: skip an ADR when the decision "is limited in scope and time and risk and cost," is already covered elsewhere, or is "tiny such as minimal-risk or self-contained or single-developer." Also explicit on the cost of lowering the bar: "establish lightweight criteria for when an ADR is warranted — not every decision needs one," and start small "which helps prevent documentation fatigue."
4. **Ancker, J.S. et al., 2017. *BMC Medical Informatics and Decision Making* 17:36 (alert fatigue).** — The measured version of "documentation fatigue" in an adjacent domain: acceptance of a prompt falls roughly 30% per additional prompt and 10% per five-point rise in repeated prompts. Relevant because the remedy this item implies — a DECISION record for changes that require no new tooling — raises the record rate substantially, and record quality and consultation are known to fall with volume.
5. **PRESUMPTION-781's evidence base, as an internal cross-check.** — A register that grows faster than its consultation rate is the write-only-repository condition the sibling item describes. Lowering the DECISION threshold without also binding DECISIONs to a retrieval trigger produces more unread records, which is not a net gain.

### Strength of challenge: Moderate

### Summary

The presumption's diagnosis is largely correct and the literature says so: no mainstream ADR guidance uses implementation cost as its trigger, so if C2A2 is using "did we build a new tool" as its threshold, it is using a proxy the field abandoned. What the search challenges is the conclusion. The field's actual criterion is reversibility and blast radius — difficult to reverse, crosses team or service boundaries, involves significant trade-offs, has no existing precedent — and the same guidance is unusually explicit that decisions limited in scope, time, risk and cost should *not* get a record. Three T1 tabs may sit on either side of that line, and the item does not establish which, because it argues from the absence of a DECISION and the passage of thirty-eight days rather than from the reversibility of the tabs. If the tabs are removable in an afternoon with no downstream dependents, the guidance says no record was owed and the presumption is mis-scoped; if they have become load-bearing for other agents' outputs, a record was owed and the trigger that failed was reversibility, not novelty of tooling. Separately, the remedy direction carries a cost the field names directly: documentation fatigue, whose measured analogue in decision-support systems is a sharp fall in prompt acceptance with volume. A system that records every cheap change and consults none of the records is worse off than one that records fewer and reads them.

### Specific risks

If the presumption drives a lowered threshold without a retrieval trigger, the predicted failure is a DECISION register that grows faster than it is read — the PRESUMPTION-781 condition reproduced deliberately — with the additional harm that genuinely significant decisions become harder to find among trivial ones. If the item is dismissed, the risk it names is live and specific: a change that cost nothing to make but that other agents have since built on becomes irreversible without anyone having decided to make it so, and thirty-eight days later there is no record of why the tabs exist or what would break if they went. That is architectural knowledge loss, and it is the failure the ADR practice exists to prevent.

### Mitigations available

(a) Replace the trigger. Record a DECISION when a change is hard to reverse, crosses agent boundaries, or creates a dependency another agent will consume — regardless of whether any tool, prompt or schema changed. This is the mainstream criterion and it addresses the item's real content. (b) Apply a two-way-door test at change time: if the change can be undone in one session with no downstream repair, no record; otherwise record. This is cheap and it is decidable at the moment of change, when the information is available. (c) For changes below the threshold, keep a one-line changelog rather than a DECISION, preserving retrievability without inflating the decision register. (d) Bind DECISIONs to a retrieval point so that lowering the threshold does not simply manufacture unread records.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-784

**Strongest counterargument:** The item is right that build cost is the wrong proxy and wrong that this makes the three tabs a missed commitment. The field's criterion is reversibility and blast radius, and the same guidance that names those triggers is emphatic that changes limited in scope, time, risk and cost should be left undocumented on purpose — not from laziness but because a decision register that contains everything is consulted about nothing. The item never establishes which side of that line the tabs fall on; it argues from an absence and an elapsed-day count, neither of which is evidence about reversibility. And the remedy it points toward has a measured failure mode: in the nearest instrumented domain, acceptance of prompts falls roughly a third with each additional prompt, and the documentation literature's own term for the software version is fatigue. A system that responds to this finding by recording more will very likely end up with a DECISION register that has the same relationship to its readers that PRESUMPTION-781 already describes for the premise register — which would mean this item's remedy directly worsens its sibling's problem. The correct correction is to change *what* triggers a record, not to lower the bar for records generally.

**What would need to be true for C2A2 to be safe:** The DECISION trigger must be reversibility and cross-agent dependency rather than tooling novelty, and it must be evaluated at the moment of change. Given that, cheap-but-irreversible changes get recorded and cheap-and-reversible ones do not, which is the outcome the item wants without the volume cost it would incur.

**How to test:** Directly and today: attempt to state what would break if the three T1 tabs were removed. If the answer is "nothing that cannot be repaired in one session," they were correctly undocumented under the mainstream criterion and the presumption is mis-scoped. If any other agent's output now depends on them, they crossed the threshold at the moment that dependency formed, and the useful measurement is *when* — which localises the trigger failure to a specific run rather than to a general policy. Run the same test on the last twenty changes that produced no DECISION; the fraction that fail it is the real size of the gap, and it is almost certainly much smaller than "every change requiring no new tooling."

---

## Search scope

Preliminary-to-moderate. Query families executed: ADR trigger criteria, architecturally-significant scoping, and over-documentation/fatigue warnings; alert fatigue as the measured analogue. Sources are predominantly practitioner guidance rather than peer-reviewed work, and are marked as such — this is a domain where the empirical literature is thin. Not searched: the architectural-knowledge-vaporisation literature (Jansen & Bosch and successors) named in the item's search strategy, which is peer-reviewed and would likely strengthen 14b's side; and the empirical literature on ADR adoption outcomes. Note also that the "two-way door" framing is widely attributed to Amazon shareholder-letter material and did not appear in the retrieved sources; it is used here as a descriptive term, not cited as a source. Broader search recommended.

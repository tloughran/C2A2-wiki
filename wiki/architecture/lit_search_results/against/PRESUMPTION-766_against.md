# PRESUMPTION-766 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-766

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-766

**Original statement:** That executing a decision candidate is the same as deciding it — a sixteen-day candidate closed by an agent's action with no DECISION logged.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from a long-open decision candidate being closed by enactment rather than by a logged decision; risk graded High.
  - 15b: Searched for challenging literature on architecture decision records, rationale-capture coverage, and the empirical norms of decision documentation.
- **Current status:** CHALLENGED

**What is being challenged:** the implied norm that every enacted decision must have a corresponding logged DECISION. The design-rationale literature treats universal capture as a known-failed ideal and prescribes selective, retrospective documentation instead.

### Challenging evidence found: Yes

### Sources

1. **"Architecture Decision Records in Practice: An Action Research Study." ECSA 2024 (rebekkaa.github.io/files/2024_ECSA.pdf) — [author list unverified from search snippet].** — Empirical finding that practitioners face persistent challenges in documentation culture, knowledge transfer, and *prioritisation of what to document*, and that the practical question is which decisions merit records rather than whether all do. Directly challenges universal-coverage as the applicable standard.
2. **Rationale-capture economics — the asymmetric-incentive finding, reported in the ADR/rationale literature and summarised in search results: "capturing rationales takes effort that is more likely to benefit future developers and maintainers while requiring time and effort of current developers" — [unverified — from search snippet; primary source not confirmed].** — The cost falls on the present actor and the benefit on a future reader, which is why capture rates are structurally low. This predicts exactly the observed behaviour (act, do not log) as the equilibrium, not as a defect of this instance.
3. **"The Reason Most Architecture Decision Records Get Written and Never Read Is Architectural, Not Cultural," Java Code Geeks, 2026-05 — [unverified — practitioner source from search snippet].** — Reports the pattern that ADRs are "widely adopted and consistently abandoned": adopted with enthusiasm, maintained for months, then dropped either because the process is burdensome or because records accumulate unread. Challenges the value side of the presumption: a logged DECISION that no one reads does not deliver the protection the item assumes.
4. **Requirements-volatility finding (arXiv:1904.08164, "Impact of requirements volatility on software architecture").** — Volatility both discourages rationale recording and degrades the value of records already made. In a system where candidates sit open for sixteen days and are then resolved by action, volatility is high, which is the condition under which the literature expects and tolerates low capture.
5. **Parnas, D.L. & Clements, P.C., 1986. "A Rational Design Process: How and Why to Fake It." *IEEE TSE* — [unverified in this search — cited from standing knowledge; not returned by the queries run].** — The classic statement that documented rationale is legitimately reconstructed after the fact rather than produced concurrently, which is precisely the remedy available here and which the presumption does not consider.

### Strength of challenge: Moderate

### Summary

The literature contradicts the norm the presumption presupposes. Decision documentation is not, empirically, a practice in which enacted decisions are reliably logged: capture rates are structurally low because the cost falls on the actor and the benefit on a later reader; ADR programmes are documented as widely adopted and consistently abandoned; and requirements volatility both suppresses capture and erodes the value of what is captured. Against that baseline, "a sixteen-day candidate closed by an agent's action with no DECISION logged" is the modal outcome in professional practice rather than an anomaly, and the field's response has been to triage — decide which decisions are consequential enough to warrant a record — and to permit retrospective reconstruction, which remains fully available here. The presumption is not thereby harmless: it correctly identifies that the *provenance chain* is broken for this candidate, and reconstruction gets harder with elapsed time. But the version of the claim that says enactment-without-logging is itself the defect does not survive contact with the literature.

### Specific risks

If the presumption drives a universal-logging requirement, the predicted outcome from the ADR literature is enthusiastic adoption followed by abandonment, leaving the system worse off than a selective policy would — plus an accumulating body of unread records that create the appearance of decision provenance without the substance. If the presumption is dismissed, the specific sixteen-day candidate stays unreconstructed and its rationale decays; the rationale literature's reported figures on forgetting (74% forget the reasons behind their own design decisions, 80% cannot recover others' reasons — [unverified — from search snippet]) suggest that window is short.

### Mitigations available

(a) Adopt a significance threshold: log DECISIONs only for candidates that are irreversible, cross-agent, or externally visible, which is the prioritisation the ECSA action-research study reports practitioners converging on. (b) Permit and schedule retrospective reconstruction — the fake-it-rationally pattern — so an enacted decision can acquire its record within a bounded window rather than never. (c) Instrument the *closure* rather than the deliberation: require that closing a candidate emit a stub with actor, date, and outcome even when rationale is deferred. This is the cheapest structural fix and it preserves the provenance chain the presumption actually cares about.

### Recommendation: CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-766

**Strongest counterargument:** Thirty years of design-rationale research says the presumption is holding C2A2 to a standard the software profession has tried and abandoned. The capture problem is structural, not motivational: the actor pays and a future reader benefits, so under any realistic incentive the enacted-but-unlogged decision is the equilibrium — which is why ADR programmes are reliably adopted and reliably dropped, and why the mature response has been triage plus retrospective reconstruction rather than universal coverage. Reading a single sixteen-day candidate closed by action as a High-severity integrity finding therefore misidentifies a base rate as an incident, and the remedy it points toward (log every DECISION) is the specific intervention the literature predicts will collapse and leave behind a corpus of unread records that *simulate* decision provenance. The defensible residue is much narrower: closure events should leave a machine-written stub, and consequential decisions should get reconstructed rationale within a bounded window. That is a small, durable fix; universal logging is a large, brittle one.

**What would need to be true for C2A2 to be safe:** A published significance threshold must exist that says which decisions require records; closure of any candidate must automatically emit an actor/date/outcome stub; and a bounded reconstruction window must be enforced for decisions above the threshold. With those three, unlogged enactment of a below-threshold candidate is a tolerated outcome rather than a break in the chain.

**How to test:** Sample the last N closed candidates and classify each as above or below a stated significance threshold; measure the logging rate in each class. If below-threshold candidates are unlogged and above-threshold ones are logged, the system is triaging correctly and the challenge holds. If the rate is uniformly near zero across both classes, the presumption is corroborated — there is no triage, only absence. Separately, attempt to reconstruct the sixteen-day candidate's rationale now and record how much is recoverable; that number is the empirical cost of the delay.

---

## Search scope

Moderate. Query families executed: rationale-capture problem; ADR adoption and abandonment; requirements volatility. Not searched: the primary design-rationale literature (Burge & Brown; Lee's rationale-management surveys) and the autonomous-systems decision-provenance literature named in the item's search strategy. Broader search recommended, though the direction of the challenge is unlikely to reverse.

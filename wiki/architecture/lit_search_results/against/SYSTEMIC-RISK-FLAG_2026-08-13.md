# SYSTEMIC RISK FLAG — 2026-08-13

Raised by Agent 15b (Literature Search AGAINST) during the 2026-08-13 processing of the 2026-08-12 14b intake (PRESUMPTION-778 through PRESUMPTION-786).

## SYSTEMIC-RISK-FLAG

**Date:** 2026-08-13

**Affected items:** PRESUMPTION-779, PRESUMPTION-780, PRESUMPTION-781, PRESUMPTION-783, PRESUMPTION-784, PRESUMPTION-786 (primary); PRESUMPTION-778 and PRESUMPTION-782 (secondary axis)

**Common vulnerability:**

Two patterns, one dominant.

**Axis 1 — the universal-control reflex (six items).** Each of PRESUMPTION-779, -780, -781, -783, -784 and -786 correctly identifies a gap and then points, implicitly, toward the same shape of remedy: a *new mandatory control applied universally* — expiry or scheduled re-audit on every hold (779); a freshness assertion on every artefact and path (780); an instruction that every minting agent read the register (781); a cost field on every refusal (783); a DECISION record for every change (784); re-derivation of the instrument before every metric reading (786). The disconfirmatory literature converges, from four independent domains, on the finding that universal mandatory controls degrade with volume and repetition, and that the versions which work are *trigger-bound and selective*:

- Reminder acceptance falls roughly 30% per additional prompt per encounter and 10% per five-percentage-point rise in repeated prompts; override rates for computerised alerts run 49–96% (Ancker et al., 2017; systematic review of overridden CPOE alerts, PMC7400042).
- Automatic expiry of deferred items — the stale bot — destroys accumulated triage state and forces re-derivation of judgements already made ("Should I Stale or Should I Close?", BotSE 2019; Zimmermann 2021).
- ADR guidance explicitly warns against lowering the recording threshold, on the grounds that it produces documentation fatigue and buries significant decisions among trivial ones (Google Cloud Architecture Center; consolidated practitioner corpora).
- Pricing the act of stopping is the recognised mechanism by which stop-work authority becomes nominal (U.S. NRC, 2016, "A Chilling Effect is Not Cool"; *Safety Science* S0925753517308871; systematic review S0925753522003848).
- The one instance in the literature of a written control that demonstrably changed expert behaviour at scale — the WHO surgical safety checklist (Haynes et al., 2009, NEJM 360:491–499) — worked by binding a *small* record to *three named trigger points* with a named reader, not by mandating general consultation.

The systemic consequence, if all six remedies are adopted in their universal form, is a predictable and self-inflicted failure: a set of controls that are formally in place, recorded as performed, and not actually executed. That is the fail-open detector pattern the register already knows as PREMISE-110, manufactured at scale and this time with documentary cover. Note the internal contradiction it would create — PRESUMPTION-784's remedy (record more decisions) directly worsens PRESUMPTION-781's diagnosed condition (a register nobody reads).

**Axis 2 — inference from inter-instrument agreement without an estimator (three items).** PRESUMPTION-778 (dispersion among four counts), PRESUMPTION-782 (agreement among derived checks), and PRESUMPTION-786 (direction of instrument error) all reason from the relationship between multiple instruments' outputs, and none invokes the established estimation framework for doing so. Capture-recapture in software inspections (Petersson et al., 2004; Wohlin & Runeson, 1995) treats detector disagreement as estimator input; the coincident-failure literature (Knight & Leveson, 1986; Littlewood & Miller, 1989; and the 2026 agent-based replication, arXiv:2606.20158) quantifies how much agreement is worth; ROC/precision-recall methodology characterises directional bias two-sidedly. Without these, the items are forced into binary verdicts — the counts are meaningless, the agreement is worthless, the direction is unknowable — where the literature offers graded, measurable answers.

**Literature basis:** Haynes et al., 2009, *NEJM* 360:491–499; Ancker et al., 2017, *BMC Med Inform Decis Mak* 17:36; U.S. NRC 2016; "Should I Stale or Should I Close?", BotSE 2019; Google Cloud Architecture Center ADR guidance; Dixit & Pindyck, 1994, *Investment under Uncertainty*; Knight & Leveson, 1986, *IEEE TSE* SE-12(1); Littlewood & Miller, 1989, *IEEE TSE* 15(12); Petersson, Thelin, Runeson & Wohlin, 2004, *JSS* 72(3); Livshits et al., 2015, *CACM* 58(2):44–46.

**Risk level:** High

**Recommendation:**

1. **Convert every proposed universal control into a trigger-bound one before adoption.** For each of the six items, specify the moment at which the control fires and the scoped subset it applies to. The checklist evidence indicates this is what makes a written control effective; the alert-fatigue evidence indicates its absence is what makes one decorative.
2. **Budget the total prompt load across the six remedies jointly, not item by item.** Each looks affordable alone; the acceptance-decay evidence is about the aggregate, and these nine items were surfaced on a single day by a single agent.
3. **Instrument every control that is adopted.** Record whether the consultation, re-audit or assertion actually happened, so that the system does not acquire the belief that a check is running when it is not. This is the single highest-value step, and it applies to all six.
4. **Do not implement PRESUMPTION-784's remedy without first implementing PRESUMPTION-781's retrieval trigger** — otherwise the DECISION register is added to the population of unread registers the sibling item is about.
5. **For the Axis-2 items, supply the estimator rather than the verdict.** Record operational definitions and overlaps for defect counts (778); validate upstream keys at the ingest boundary rather than adding downstream cross-checks whose independence Knight–Leveson predicts will not hold (782); publish two-sided instrument profiles once rather than mandating re-derivation per reading (786).
6. **Note for reconciliation (14b):** this flag is written without sight of Agent 15a's results, per the isolation requirement. If 15a found strong supporting evidence for the same six items, the correct joint reading is not "the remedies are wrong" but "the remedies are right in content and wrong in form" — the diagnoses largely survive disconfirmatory search; it is their universal, unbound implementation that the literature challenges.

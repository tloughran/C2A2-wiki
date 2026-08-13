# PRESUMPTION-780 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-780

**Date searched:** 2026-08-13

**Original item:** PRESUMPTION-780

**Original statement:** That a freshness gate measures the artefact its consumers read — a snapshot at 0.00h and a published file four days old, same morning, same name.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred, from a same-morning divergence between a run's temporary snapshot (0.00h) and the published file of the same name (four days old), that the system presumes its freshness gate asserts on the artefact consumers actually load; risk graded High.
  - 15b: Searched for literature challenging the inference — component versus end-to-end monitoring, data-freshness SLO practice, and the known limitations of checking at the consumption boundary.
- **Current status:** NO-CHALLENGE-FOUND (on the core claim); the implied remedy is PARTIALLY-CHALLENGED

**Polarity note (explicit inversion).** The AGAINST direction is that 14b's worry is overstated, mis-scoped, or its remedy wrong. On this item the core claim survives search; what the literature does challenge is the sufficiency of the obvious remedy.

### Challenging evidence found: Partial — and only against the remedy, not the claim

### Sources

1. **Trade/vendor literature on synthetic versus real-user monitoring (Dynatrace, Akamai, Catchpoint, Sematext, Exoprise; consolidated 2019–2026). [industry sources — non-peer-reviewed; cited for the documented limitation, not for effect sizes].** — Synthetic checks are simulations: "robotic scripts only test the exact specific pathways they were programmed to test," and a passing synthetic result "does not guarantee" the consumer's experience. The consensus recommendation is explicitly *both* synthetic and real-user instrumentation, "because each technique has inherent blind spots." Applied here: moving the freshness assertion to the consumption boundary does not close the gap, it relocates it — the boundary check will assert on the path it was scripted for, and a consumer reading by a different path is unmonitored again.
2. **Data-observability practice on freshness SLOs (dbt Labs, Sifflet, Conduktor, Datatrail; 2024–2026). [industry sources].** — The standard framing is a per-table freshness SLA plus stage-by-stage latency tracking, i.e. *both* component and end-to-end checks, with alerting when any stage's age exceeds its threshold. This is a direct challenge to a "just check at the end" remedy, and also a challenge to the idea that a component-level snapshot check is a *mistaken* check: in the reference architecture it is a legitimate and necessary check that happens to be incomplete on its own.
3. **Alert- and reminder-fatigue evidence (Ancker et al., 2017, *BMC Medical Informatics and Decision Making* 17:36).** — Bears on the remedy's cost: multiplying freshness assertions across every artefact and every consumption path raises prompt volume, and acceptance of repeated prompts falls sharply with repetition. Freshness checks are among the highest-volume alert classes in data observability practice for exactly this reason.

### Strength of challenge: Weak

### Summary

This item survives disconfirmatory search substantially intact, and that should be stated plainly. Nothing found contradicts the claim that a check asserting on a run-local snapshot and a consumer loading a published file of the same name can diverge silently; on the contrary, the instrumented-versus-consumed gap is the reason the observability field maintains two distinct instrument classes rather than one. The available challenge is narrower and concerns scope and remedy. First, a component-level check on a snapshot is not a defective check — in the reference architecture it is a correct stage-latency check, and the defect is the *absence* of a second, consumption-boundary check, not the presence of the first. Framing the component check as measuring "the wrong artefact" risks removing an instrument that is doing useful work. Second, the obvious remedy — assert at the consumption boundary — inherits the well-documented limitation of synthetic monitoring: it verifies only the path it was scripted for, so it converts an unmonitored gap into a narrower unmonitored gap rather than closing it. Third, freshness checks are a high-volume alert class, and multiplying them across paths has a measurable acceptance cost.

### Specific risks

If the presumption is acted on by relocating rather than adding the check, the system trades a known blind spot for an unknown one and loses stage-level latency signal that would localise the fault. If it is acted on by adding checks indiscriminately, the predicted failure is freshness-alert fatigue: a class of alert that fires often, is usually benign, and is therefore dismissed, so that the one occasion it matters is dismissed too. If it is not acted on at all, the original hazard stands unchanged and is severe: a gate reporting 0.00h while consumers read a four-day-old file is a control that certifies without measuring — a fail-open instrument in the PREMISE-110 sense, and the fact that it fails open *quietly* and *by default* is the item's real content.

### Mitigations available

(a) Add rather than replace: keep the snapshot check as a stage-latency signal, and add an assertion on the published artefact identified by resolved path, not by name. (b) Make the check assert on the *same handle a consumer resolves* — resolve the path the way a reader does, so name collision cannot mask divergence. This is the one modification that closes the specific failure observed. (c) Report artefact age rather than a pass/fail freshness flag, so that a stale reading is visible as a number rather than absent as a non-alert; this side-steps the alert-volume problem by moving from alerting to display. (d) Where a single consumption path dominates, script the boundary check for that path and record explicitly which paths are unmonitored — the synthetic-monitoring literature's own recommended discipline.

### Recommendation: NO-CHALLENGE-FOUND

*(Core claim unchallenged by this search. The implied remedy — relocate the assertion to the consumption boundary — is partially challenged as insufficient on its own.)*

---

## STEELMAN

**Item:** PRESUMPTION-780

**Strongest counterargument (offered honestly as the best available, and it is not strong):** The presumption identifies a real divergence but mislabels the instrument as wrong when it is merely partial. A snapshot-age check is a legitimate stage-latency measurement in every reference data-observability architecture; the architecture also carries a separate freshness SLA on the published table, and the standard is to run both, precisely because neither alone covers the pipeline. So the finding is "one of two required instruments is missing," not "the existing instrument measures the wrong thing." Furthermore, the natural fix carries a documented ceiling: consumption-boundary checks are synthetic checks, and synthetic checks verify only scripted paths, so a system that adopts the remedy and declares the gap closed will have acquired precisely the false confidence the presumption warns against, one layer out. And freshness is the highest-volume alert family in this domain; adding assertions per artefact per path has a measurable cost in ignored alerts.

**What would need to be true for C2A2 to be safe:** Both instruments must exist — a stage-level age signal and an assertion on the published artefact resolved the way a consumer resolves it — and the set of consumption paths must be enumerated, with unmonitored paths named rather than assumed absent. Under those conditions the divergence observed becomes detectable at the moment it occurs.

**How to test:** On the morning in question, resolve `metabolism_data.json` (or its analogue) by the exact path a consumer uses and read its mtime, then read the mtime of the snapshot the gate asserted on. If the two handles resolve to different files, the presumption is confirmed outright and no further literature is needed — this is a one-read empirical question, and ASSUMPTION-1024 in the same intake already queues it as such. The literature question worth testing separately is whether adding a boundary assertion actually closes the gap or merely narrows it: enumerate the consumption paths and check how many the proposed assertion covers.

---

## Search scope

Preliminary-to-moderate, and weaker than the other items in this batch. Query families executed: synthetic versus real-user monitoring and its limitations; data-pipeline freshness SLOs and staleness detection. Almost all sources located were vendor or practitioner material rather than peer-reviewed work, and they are marked as such; this is a domain where the peer-reviewed literature is thin relative to practice. Not searched: the distributed-systems literature on cache coherence and read-your-writes consistency, which is the formal analogue of this failure and may contain a genuine challenge or a sharper statement of the claim. **Broader search recommended before treating "no challenge found" as settled** — this is a case of "not enough searched" as much as "searched and found nothing."

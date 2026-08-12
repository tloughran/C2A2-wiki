# PRESUMPTION-776 CHALLENGE REPORT

## SEARCH-AGAINST-PRESUMPTION-776

**Date searched:** 2026-08-12

**Original item:** PRESUMPTION-776

**Original statement:** That an unwritable git is a deferral rather than a data-loss exposure — 191 uncommitted paths in ephemeral compute, and the yield metric reads git as ground truth.

### PROVENANCE

- **Origin:** 14b
- **Chain:** [14b → 15b]
- **Item type:** PRESUMPTION (unstated — surfaced by inference)
- **Transform at each step:**
  - 14b: Inferred from an inability to commit plus a count of 191 uncommitted paths that the system is treating a durability failure as a scheduling inconvenience; risk graded Critical.
  - 15b: Searched for challenging literature on ephemeral-storage durability boundaries and on the validity of git as a measurement substrate.
- **Current status:** PARTIALLY-CHALLENGED

**What is being challenged:** the composite. The durability half is largely uncontested. The measurement half is challenged hard — the literature says git was never a valid yield substrate, so "the yield metric reads git as ground truth" is a finding against the metric, not evidence that the uncommitted paths are lost.

### Challenging evidence found: Partial

### Sources

1. **GitClear, "Measuring Developer Productivity: A Comprehensive Guide for the Data Driven" — [unverified — figures from search snippet].** — Reports that even the most strongly correlated git-derived metric (Diff Delta) reaches only ~61% correlation with measured effort in the most favourable repository (n=655 issues), and states plainly that "no existent git metric can tell you the full story." Challenges the presumption's implicit premise that git *should* be ground truth for yield: it is a weak proxy under the best conditions.
2. **"Measuring developer productivity? A response to McKinsey," The Pragmatic Engineer.** — The standing practitioner critique of commit-derived productivity measurement: metrics of this family are "gamed, misused, or turned into tools for micromanagement," and output counting is identified as the most persistent myth in the field. Challenges the framing that a git-blind yield metric is a measurement failure rather than an escape from a bad measurement.
3. **"SpaceX: Exploring metrics with the SPACE model for developer productivity," arXiv:2511.20955.** — Multi-dimensional frameworks exist precisely because single-substrate (repository-derived) measurement is known-insufficient; the corrective is to add dimensions, not to restore commit access.
4. **Ephemeral-storage durability literature (MongoDB, "What is Ephemeral Storage in Kubernetes?"; Chainguard, "The principle of ephemerality"; appsecuritystandards.org glossary) — [unverified — practitioner sources from search snippets].** — Confirms the durability half: ephemeral data is removed on eviction, restart, upgrade, autoscaling, or host maintenance, and the design guidance is that workloads must be built so temporary data can be *regenerated*. Note the direction of that guidance: regenerability, not commit access, is the prescribed property — a partial challenge to the "commit or lose it" framing.

### Strength of challenge: Moderate

### Summary

This item bundles two claims of very different evidential standing. The durability claim — that work held only in ephemeral compute is at risk — is corroborated, not challenged; the cloud-storage literature is unambiguous that ephemeral state is destroyed by ordinary lifecycle events and that no warning is given. The measurement claim is challenged sharply. Empirical work on git-derived productivity metrics finds ceiling correlations around 61% with effort under favourable conditions and a long record of misuse, which means a yield metric that reads git as ground truth was already invalid; the fact that it now reads zero is a symptom of a pre-existing measurement defect rather than new evidence about the 191 paths. There is also a scoping challenge to the durability half that the presumption does not address: the guidance in the ephemerality literature is that workloads should make their outputs *regenerable* or write them to a durable mount, and if the 191 paths live on a mounted host filesystem rather than container-local storage, the exposure is a version-control gap, not a data-loss gap. The presumption asserts "ephemeral compute" without establishing which storage class the paths occupy, and that is the load-bearing unverified step.

### Specific risks

Two failure directions. If the presumption is accepted wholesale, effort goes into restoring commit access as a data-durability measure and the invalid yield metric is repaired rather than retired — leaving the system with a restored bad measurement and false confidence in it. If the presumption is rejected wholesale, and the paths genuinely sit on container-local storage, the next eviction destroys 191 paths of work with no signal. The cheap resolution is to determine the storage class first; the expensive error is to argue severity before that is known.

### Mitigations available

(a) Establish the storage class of the 191 paths — one command — and grade accordingly; this dominates all other mitigations. (b) If the paths are on a durable mount, downgrade to a version-control/provenance finding and treat commit access as a traceability need, not a durability need. (c) Replace the git-as-ground-truth yield metric with an artefact-count metric read from the durable store directly, which is both more valid per the SPACE-model literature and immune to commit-access loss. (d) Adopt the regenerability discipline: record enough input state that any lost path can be recomputed.

### Recommendation: PARTIALLY-CHALLENGED

---

## STEELMAN

**Item:** PRESUMPTION-776

**Strongest counterargument:** The presumption's two halves fail in opposite directions and combining them produces a Critical grade neither half supports on its own. On measurement: the developer-productivity literature has spent a decade establishing that commit-derived metrics are weak proxies — a ~61% ceiling correlation with effort in the best case — so a yield metric that reads git as ground truth is not a good instrument that has gone blind, it is a bad instrument whose badness has become visible. Repairing it is the wrong move. On durability: the cloud-native guidance is that ephemeral state must be *regenerable* or written to a durable mount, and the presumption never establishes that the 191 paths are on ephemeral rather than mounted storage; if they are on a host mount, there is no data-loss exposure at all and the finding collapses to "we lack version control on work in progress," which is a real but ordinary traceability gap. A Critical grade resting on an unverified storage-class premise plus an already-invalid metric is a grading error, and it is the kind of error that consumes remediation capacity that the other items in this batch have better claims on.

**What would need to be true for C2A2 to be safe:** The 191 paths must reside on a durable, host-backed mount that survives container lifecycle events, and the yield metric must be re-pointed at that durable store rather than at git. Under those two conditions the exposure is traceability only.

**How to test:** Inspect the mount table and resolve the 191 paths to their filesystem device; check whether the device is container-local or a bind/host mount. Then, separately, recompute the yield metric from the durable store and compare with the git-derived figure — the gap is the measured size of the metric defect, which is worth knowing regardless of how the durability question resolves.

---

## Search scope

Moderate on the measurement half, preliminary on the durability half. Query families executed: ephemeral-storage durability; git-metric validity critique; multi-dimensional productivity measurement. Not searched: backup/RPO literature and the specific literature on work-in-progress loss rates in CI/sandbox environments. Broader search recommended for the durability half.

# Pre-Registration — Coil / Triplet Usefulness Falsifier

**Version:** v1.1 (2026-06-24). See §7 Amendment Log for the v1.0→v1.1 rationale.
**Discharges:** REVISE-111 (HIGH — reflexive falsification non-circular) and coupled REVISE-105 (HIGH — falsifier ≠ yield metric). Couples REVISE-115 (yield-count Goodhart) and REVISE-124 (built = start of validation).
**Phase:** Metabolism Monitor Phase 2 ("Characterize"). The highest-value design decision in `METABOLISM_MONITOR_AGENT_SPEC.md` §2a.2 / §8.
**Status:** PRE-REGISTERED DRAFT — frozen at the registering commit. Drafted in Cowork 2026-06-24; **not yet committed** (commit on the Mac — see §8).
**Author of record:** T. Loughran (programme owner). Drafted with Cowork assistant.

---

## 0. Pre-registration attestation (the load-bearing clause)

> As of the commit that registers this version, **no coil-outcome ledger, before/after Δ, shared-resource yield statistic, or falsifier result relevant to the confirmatory test has been inspected by the author or the drafting assistant.** The falsifier statistic has not been computed. Only *instrument knowledge* — what data exist, their schema, metric definitions, the connectome vocabulary — was consulted. This document fixes the test **before the confirmatory data are seen.**

Why: REVISE-111's charge (Simmons et al. researcher degrees of freedom; auditor self-review impairment) is that a dyad applying its own falsifier to its own ledger is "passable by construction." Chang's escape — the common ground 15a and 15b converge on — is that self-testing is non-vicious *iff the falsifier is specified independently of the tested outcomes.* That independence is real only if specification precedes inspection. **Register, then look.**

---

## 0a. Stance: this is a PoC measurement DRAFT, honestly revisable

Success at this construction stage is **landing in the neighborhood of sensible testing**, not delivering a final instrument. This document is therefore explicitly a *draft we expect to redraft* — but under a discipline that protects the one thing pre-registration exists to protect (§7): **the spec may be revised freely before any confirmatory run, and after a run only on a rationale that makes no reference to the obtained results.** "We realized shared-ids miss synthesis-by-novelty" is a legitimate (results-independent) reason to amend; "the p-value came back at 0.06 so we widened the window" is not. Every confirmatory result is tagged to the exact version + commit hash that produced it.

---

## 0b. The asymmetry — what a pass and a fail are each allowed to mean (foundational)

Usefulness is **not** productivity. MacIntyre does not validate a tradition by output volume, and the connectome doc itself holds that convergence detection is "descriptive: *where* convergence is, not a verdict that it *is right*." So the test is deliberately **asymmetric**, and this asymmetry is load-bearing, not a hedge:

- **A FAIL is strong and clean.** A coil that predicts *no* downstream cross-tradition activity above a degree-matched random fiber is, to a good approximation, **decoration** — a line that changed nothing. Falsification is the informative outcome.
- **A PASS is weak by design.** A coil that *does* predict downstream activity has passed a **necessary condition** for being a real bridge — nothing more. It has **not** been "validated as a good bridge," because it might predict spurious, low-quality, or self-fulfilling activity. The vocabulary for a pass is *"necessary-condition met, provisional"* — never *"useful, confirmed."*

Locking in "downstream yield = usefulness" as a two-sided verdict would be an assessment choice that warps the architecture toward productivity-ism — the exact Goodhart hazard the measurement framework resists. The asymmetry is the firewall against it.

---

## 1. The claim under test

The programme asserts (`narrative_prs_connectome.md`) that **coils are association fibers, not decoration** — long-range cross-tradition connections that let two tradition-modules begin to function as one. The skeptical counter-claim (REVISE-111's substrate) is that a coil merely *adds graphics*.

- **H1 (programme claim):** A coil between traditions A and B marks a genuine bridge — its formation is followed by elevated cross-A–B resource-sharing in its neighborhood, beyond what a degree-matched random fiber would produce.
- **H0 (null / "just graphics"):** Coil placement carries no predictive information about subsequent cross-A–B activity beyond node degree.

Per §0b: the test can falsify H1 cleanly; it can only fail-to-falsify H1 (a necessary-condition pass), never confirm it.

---

## 2. The convergence battery (safeguard 2)

The construct is judged on **several operationally independent indicators**, not one — both to reduce single-indicator fragility and because spoofing three different things is far harder than gaming one. Each indicator has its own pre-set gate; the verdict combines them by the **fixed decision lattice in §4** (no post-hoc weighting).

### 2.1 PRIMARY — cross-A–B shared-resource yield (retrospective, DiD vs degree-preserving null)
- **Unit:** each coil `c` with endpoints `A(c), B(c)` and **formation time `t_c`** = discovery-time ("altitude" rule: where the bridging insight formed, not the age of the ideas joined).
- **Event:** a newly-*articulated* PRS triplet (`prs_articulated` date) sharing ≥1 **canonical resource-id OR problem-id** (exact normalized match, never fuzzy) with an existing triplet of the coil's *other* tradition.
- **Statistic (difference-in-differences):** `Δ(c) = [events in (t_c, t_c+W]] − [events in [t_c−W, t_c)]`; `S_obs = mean Δ(c)` over eligible coils. The pre-window controls for traditions already integrating before the coil.
- **Null (degree-preserving rewire):** `N = 10,000` configuration-model rewirings preserving each tradition's coil-degree; recompute `S` each time → null distribution; one-sided p = fraction `≥ S_obs`.
- **Gate:** passes iff `p < 0.05` AND rate-ratio `RR = (post rate)/(null mean) ≥ 1.5`.

### 2.2 SECONDARY A — confidence-upgrade near coils
Rate at which **Speculative** triplets in a coil neighborhood are later upgraded to **High** (dated upgrade events), vs Speculative triplets *not* in any coil neighborhood, same degree-preserving null logic. **Gate:** one-sided `p < 0.05`. (Independent of 2.1: measures quality maturation, not resource overlap.)

### 2.3 SECONDARY B — human-verified relevance (corroborate-only)
Directional check against the sparse email/human relevance confirmations (≈1/6 coverage today). **Too sparse for a p-value** — reported as *direction + coverage* only; can corroborate the lattice, never anchor it. Its sparsity is itself reported as an instrument limitation.

### 2.4 EXPLORATORY — synthesis-by-novelty (NOT confirmatory yet — instrument not built)
The deepest worry about 2.1 is a **false negative on real synthesis**: genuine fusion of A and B often coins *new* vocabulary rather than reusing the parents' resource-ids, so the shared-id test would score a true bridge as zero. The honest indicator is "new resource-ids first-appearing in the coil neighborhood post-formation that **descend from** resources of *both* traditions." But this requires **resource lineage the schema does not currently record.** Reconstructing "descends from both" after the fact is itself a researcher-degrees-of-freedom hole as dangerous as the one we are closing.

**Therefore:** this indicator is **exploratory only** until the instrument exists. The architecture change that would promote it to confirmatory: add a `derived_from:` (parent resource-ids) field to the PRS resource schema, populated **at articulation time** (so lineage is contemporaneous, not reconstructed). Until then it is reported with an explicit "instrument not yet built" caveat and **never enters the lattice**. *Build the instrument before trusting the reading.*

---

## 3. Ungameable-by-construction (safeguard 1) + architectural firewall

The reflexive hazard (your "formative slide" / Campbell's Law): the *same swarm* lays coils and articulates triplets, so once "good coil → more cross-resource triplets" is announced, agents could manufacture the very events the test counts. Defenses, in order of strength:

1. **Retrospective-only confirmatory run.** The confirmatory test runs on the ledger that already exists **as of the registering commit**. Past behavior cannot be steered by a future rule, so the confirmatory result is ungameable by construction. (Cost: it cannot become a live dashboard without the gaming risk returning the moment the metric is public — which is *intended*. This is an occasional epistemic **audit**, never a steering signal.)
2. **Never a control target.** The falsifier outputs are *never* fed back as an optimization target or shown to the triplet-generating agents (extends the spec's "cross-counts must never become a control target," REVISE-115).
3. **Architectural firewall (separation of powers).** For any *future* re-run on post-announcement data, three roles must be structurally distinct agents: the **coil-author**, the **triplet-author**, and the **falsifier-runner** — and the triplet-author must be **blind to the coil-reward**. Without that separation, no post-announcement run is admissible. (This is an architecture commitment, logged here so future-me cannot quietly violate it.)

**Foundational caveat (pushback):** retrospective ≠ clean. The historical ledger was generated by one swarm under unknown biases; retrospect only buys *un-gameability by the future*, not freedom from the past's idiosyncrasies. So the confirmatory set is **used once**, tagged to this version; treat its result as one audit under known limitations, not a timeless verdict.

---

## 4. Decision lattice (PRE-FIXED — no post-hoc weighting; safeguard 2 completion)

Combine PRIMARY (2.1) and SECONDARY A (2.2); SECONDARY B (2.3) only nudges, never decides:

| PRIMARY | SECONDARY A | Verdict |
|---|---|---|
| fails gate | fails gate | **FALSIFIED** — coils indistinguishable from random fibers on every independent measure (the strong, clean outcome) |
| passes gate | passes or directionally agrees | **NECESSARY-CONDITION MET (provisional)** — not "useful, confirmed" (see §0b) |
| passes | fails (opposes) | **TENSION** — do not declare; re-examine the *specification* (results-independent only, §7) |
| fails | passes | **TENSION** — same |
| any | n eligible < 20 (PRIMARY) | **INCONCLUSIVE / underpowered** — re-run later |

A corroborated (necessary-condition-met) result is still **descriptive/provisional** (REVISE-124). Only FALSIFIED is a strong claim.

---

## 5. Contrast-blind calibration pass (safeguard 4) + frozen degrees of freedom

A power/feasibility pass is permitted **before** the confirmatory run, inspecting *instrument* properties only, with the outcome contrast sealed:

- **MAY inspect:** number of coils; distribution of `t_c`; how many coils have a full ±`W` window (power); the *overall* base rate of cross-tradition shared-resource events per unit time (for sizing only, **not** paired to specific coils' before/after); degree distribution (null feasibility).
- **MUST NOT inspect:** any coil-specific `Δ`, any `S`, any per-coil neighborhood outcome, any per-coil upgrade count.
- **Output:** a dated calibration note setting `W`, the power floor, and `N`, justified by instrument properties alone. Logged; auditable.

**Frozen choices (defaults; calibration may move the starred ones with a logged, instrument-only rationale):**

| Choice | Committed value |
|---|---|
| Outcome date field | `prs_articulated` primary; `prs_added` sensitivity check |
| Resource match | ≥1 shared canonical resource-id OR problem-id, exact normalized; no fuzzy |
| Coil time `t_c` | discovery-time (altitude rule) |
| Neighborhood | module-level (tradition A or B); k-hop endpoint = exploratory only |
| Baseline | equal-length pre-window (DiD) |
| Null draws `N` | 10,000 ★ |
| RNG seed | `20260624` |
| Significance | one-sided α = 0.05 |
| Effect gate (PRIMARY) | RR ≥ 1.5 |
| Power floor | n ≥ 20 eligible coils ★ |
| Primary window `W` | 90 d ★ (robustness 30, 60 reported, primary decisive) |
| Construct-identity gate | Pearson r ≥ 0.7 (§6) |
| Exclusions | coils with `t_c > (data_end − W)` excluded from primary; **listed, never silently dropped** |

---

## 6. Jingle guard — falsifier ≠ §6 yield (discharges REVISE-105)

The master-plan **§6 "interaction yield"** is the *total* triplet/milestone count per session — a global productivity headline. The PRIMARY falsifier is a *different* observable: a local, coil-paired, null-referenced difference-in-differences. **The falsifier is never scored on total yield, and total yield is never an outcome variable.** Whether they secretly co-move is a **separate, secondary hypothesis**: correlate the two counts across sessions; treat them as one construct **only if r ≥ 0.7**; otherwise report as distinct. Demonstrated, not stipulated (the REVISE-105 NOVELTY clause).

---

## 7. Amendment discipline (reconciles "PoC draft" with "commit before data")

- The spec is **versioned** (v1.0, v1.1, …). Each confirmatory run is tagged to one version + commit hash.
- **Before any confirmatory run:** amend freely.
- **After a confirmatory run:** amend **only on a results-independent rationale** — one that makes no reference to the obtained S/p/RR/verdict. Each amendment records: date, version bump, the rationale, and a **self-classification ("results-independent: yes — because …")**. The outside auditor (§9) verifies the classification; an amendment whose rationale references results is rejected and flagged.
- The original version always stands in the record; results are reported per version. No silent edits — that is the whole point.

### Amendment Log
- **v1.0 → v1.1 (2026-06-24, results-independent — no run has occurred):** added the convergence battery (§2) replacing the single-indicator design; added the pre-fixed decision lattice (§4); added ungameable-retrospective design + architectural firewall (§3); added the contrast-blind calibration pass (§5); added the necessary-condition asymmetry (§0b) and the synthesis-by-novelty false-negative caveat with its schema prerequisite (§2.4); added this discipline (§7). Rationale: foundational review (Tom, 2026-06-24) — a single yield indicator risked (a) Goodhart capture, (b) a false negative on synthesis-by-novelty, and (c) smuggling productivity in as a two-sided verdict. All purely design-level; no outcome data exists or was seen.

---

## 8. Registration Act (MAC TODO) — what makes this binding

The registering commit is done by Tom on the Mac and **must precede any confirmatory run.**

```bash
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project"
git add wiki/architecture/coil_falsifier_preregistration.md
git commit -m "Pre-register coil/triplet falsifier v1.1 (REVISE-111 + REVISE-105; battery + asymmetry + amendment discipline)"
git push origin main          # commit timestamp = the registration; cite the hash with results
# THEN: contrast-blind calibration pass (§5) -> set W/n/N -> write the deterministic analysis script
#       (faithful transcription of §2,§4,§5) -> run via the independent falsifier-runner agent ->
#       human audit a random sample -> report a lattice verdict into the flag pipeline.
```

---

## 9. Independence & verification (REVISE-111 core)
1. Specification precedes data (§0, §8).
2. A structurally independent **falsifier-runner** agent (not the coil-author, not the triplet-author, not the daily wiki agent) computes the lattice deterministically (frozen seed/procedure).
3. **Human audit:** T. Loughran (outside the authoring loop) recomputes a pre-set sample by hand — **10 coils' Δ + 1 null draw + 5 confidence-upgrade classifications** — logged pass/fail.
4. Degrees of freedom frozen (§5); changes are Amendments (§7); the auditor flags undisclosed changes and rejects results-dependent amendments.

---

## 10. Swarm-contract trace (`swarm-contract.md`)
1. **Introspecting** — §0 states exactly what was and wasn't inspected.
2. **Creative** — a genuine prospective, falsifiable prediction, not a re-description.
3. **Transparent** — every choice tabled (§5); versioned and diffable (§7).
4. **Falsifiable / self-correcting** — the strong outcome is self-falsification; the asymmetry (§0b) blocks self-congratulation.
5. **Pluralistic** — H1 and the "just graphics" null are stated fairly; the test can vindicate either.
6. **Reversible** — registration is additive; amendments are append-only, disclosed, and results-independent.

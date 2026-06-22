# Metabolism Monitor Agent — Spec

**Status:** draft for review (2026-06-19)
**Author:** drafted in Cowork (RC Karpathy Wiki Project), pending Tom's sign-off
**Convention:** modeled on `scripts/janitor.py` + `connector-health/` — weekly scheduled, baseline-then-deltas, writes a named output dir, surfaced through `morning-system-health`. Written against the six properties in `architecture/swarm-contract.md`.

---

## 1. Purpose (the sharpened ask)

The OpenStory→Metabolism pipeline is healthy and produces a real signal. We now want an agent that *learns from* that signal and, eventually, *acts on* it. The original ask bundled four jobs — clean the data, learn the system, recommend one-time tweaks, and control the ecosystem on the fly. Those are **not one workload; they are a maturity ladder**, and the fourth rung is a different risk class from the first three: jobs 1–3 only observe and recommend, job 4 *actuates*.

Reframed as a control problem, the ladder is not arbitrary — each rung is a precondition for the next:

> You cannot control on a signal until (a) the signal is reliable, (b) you have characterized its normal range, and (c) you understand its lead/lag against outcomes.

So the agent is specified as **one role, phased**, where each phase has a falsifiable done-gate and no phase is promoted until the prior gate is met. Phases 1–3 ship on the existing weekly-agent pattern. Phase 4 never runs autonomously; it runs in shadow.

---

## 2. What the signal actually is (verified 2026-06-19)

Measured against the live `open-story.db` (150,254 events / 912 sessions; last event 2026-06-19 19:00) and the `wiki/metabolism/` build:

**Token metabolism — healthy.** The Apr-7 schema migration that zeroed tokens Apr 6→Jun 17 is closed. Re-running extraction over 57,853 assistant events, the both-paths fix verifies across the boundary:

| month | output tokens | old path `data.token_usage` | new path `agent_payload.token_usage` |
|---|---|---|---|
| 2026-03 | 275,798 | 1,015 | 0 |
| 2026-04 | 8,191,477 | 2,557 | 13,016 |
| 2026-05 | 20,386,902 | 0 | 15,191 |
| 2026-06 | 33,315,276 | 0 | 26,074 |

April fires on both paths (the boundary); May/June run fully on the new path, nonzero and growing.

**Yield — already real, including PRS.** `build_metabolism_view.py::compute_vault_yield` computes four live per-day yield series from `wiki/` git history and the WS2 single source `architecture/metrics/prs_yield_detail.csv` (DECISION-058):

- `links_added`, `files_added` — vault git deltas
- `prs_added` — PRS triplet **first-seen** (git commit-day a `PRS-NN` id first appeared; objective but backfill-clustered)
- `prs_articulated` — PRS triplet **self-reported Date Added** (when the work was actually done)

The CSV tracks **283 triplets**; the current snapshot carries 283 first-seen / 281 articulated across 44 yield-days. **Correction to an earlier draft:** PRS-triplet yield is *live, not "still to come"* — that phrase survives only in the stale `_meta.note` string inside `metabolism_data.json` and should be edited there.

**Three known gaps (Phase-1 fodder, not breaks):**
1. **Freshness lag.** `metabolism_data.json` is a manual regen — the reviewed snapshot was 2 days behind a live db. Everything downstream reads this snapshot, so a monitor reading it would "learn" from frozen data.
2. **Zero-token lanes.** The build script already flags lanes with cadence but no token payloads — an instrumentation gap, *not* zero work. Quantifying and explaining these is the first real hygiene task.
3. **Thinking-token join gap (found 2026-06-19).** `system.thinking_tokens` exists as its own event subtype (25,415 events), but `thinking_tokens` reads 0 across all metabolism lane rows — the thinking stream isn't being joined into the lane view. Concrete Phase-1 fix.

Also unresolved and directly in scope: **OPEN-083** (the metabolism "cliff" — artifact vs. real) stayed undecided because the headless agent's mount can't reach the live db. A Cowork session *can* reach it (confirmed 2026-06-19), so the monitor — or its operator — can close OPEN-083 directly.

---

## 2a. What's already present (answers to the four pre-Phase-0 questions)

Verified against the repo 2026-06-19. The headline: **a large, descriptive signal set already exists with zero new instrumentation** — and a reflexive epistemic-hygiene system (the daily `14a`/`15c` metrics snapshots) is *already running*, which the monitor must feed and consume rather than duplicate.

**(1) PRS quality — two distinct layers, never to be blended.**
- *Confidence* (the agent's self-assessment, in each `prs_triplets.md`): High 142 / Medium 114 / Medium-High 6 / Speculative 20. Deterministically countable now. It is a self-report, not validation.
- *Verified relevance* (your email-comm confirmation): real but **sparse** — the 2026-06-17 snapshot records verification as "single-point (06-07 cross-check only) = 1/6 commit-day coverage; per-day audit of the other 5 unrun (ASSUMPTION-323)."
- **Baseline rule:** report the confidence *distribution* and the verification *coverage* (1/6) as two separate descriptive facts. Do not fuse them into one "quality score."

**(2) Coil / crosslink usefulness — the semantics you flagged.** This is the sharp one, and the project's own documents already draw the honest line. There are 90 cross-program connections and a coil layer (~49 coil refs in `generate_prs_3d.py`); `narrative_prs_connectome.md` already supplies a real network-measurement vocabulary (degree/hubs, modularity, **cross-module fiber density**, path length) and explicitly frames convergence detection as *"descriptive: where convergence is, not a verdict that it is right."* The metrics snapshot reinforces this with a **HIGH systemic-risk flag** (the system treats PRS-yield as more complete/validated/singular than evidence warrants) and **REVISE-124 KEYSTONE** — *"'built' = start of validation; provisional until challenges clear; do NOT harden the view layer on it"* — plus **REVISE-111 (HIGH): pre-register falsifiers.**
  - **Honest answer to "improving vs. busy graphics":** *today, nothing is validated as improvement.* Coils/crosslinks are descriptive structure. To cross from graphics to signal you need a **pre-registered falsifier** — stated in advance, e.g. *"a meaningful coil predicts subsequent shared-resource yield / cross-citation / a verified upgrade of a Speculative triplet to High, at a rate a coincidental coil would not."* That falsifier does not yet exist (REVISE-111 outstanding). **Baking the falsifier test into the monitor (Phase 2–3) is the single highest-value design decision here** — it is the difference between counting coils and learning whether coils mean anything.

**(3) Cross-tradition indicators in the Phase-0 baseline — yes, include them, as census only.** Count (90), by-type, cross-module fiber density, and modularity belong in the baseline *because* a baseline is a normal-range snapshot, which is exactly what makes later drift detectable. Tag every cross-tradition number **descriptive/provisional** per REVISE-124. Also surface, don't paper over, the **three-count divergence** (269 / 264 / 262 — connectome nodes / cumulative / on-disk; OPEN-084), which 15c recommends reporting as three distinct constructs rather than reconciling. The only red line: cross-counts must never become a control *target* (Goodhart).

**(4) Other present signals + efficiency metrics already calculable (no new instrumentation).**
- *Efficiency ratios from existing lane fields* (computed 2026-06-19): system **out/in ≈ 2.5**; per-lane out/in ranges 1.1–8.8 (Wolfram 8.8, interactive 7.9, lit-search 7.2 vs. review/handoff lanes ~1.1). System **cache-read fraction ≈ 91.3%** of all tokens — i.e. the swarm overwhelmingly *reads recirculated context rather than regenerating it*, which is the Karpathy wiki-as-environment thesis showing up as a measured number (logbook-worthy). Plus out-per-run and `median_gap_h` (cadence) per lane.
- *Yield-per-token (crude, Goodhart-dangerous → report-only):* ~204k output tokens per articulated PRS triplet; tokens-per-file and tokens-per-wikilink also computable.
- *The reflexive / epistemic-yield stream* (maintained by `14a`/`15c`, not to be rebuilt): assumptions 327, presumptions 360, validated premises 65, decisions 59, open questions 84, AWAITING-REVIEW backlog 78, plus monitor/revision queues.
- *Pipeline flow/backlog health:* lit-search 15a/b/c dispositions per day; proposal approval rate (0 APPROVE / 0 DENY, 12 pending, review overdue since 06-06).

---

## 3. The phase ladder

| Phase | Job | Done-gate (falsifiable) | Model's role |
|---|---|---|---|
| **0 — Reliable signal + descriptive census** | Schedule the regen; add a freshness check; emit a one-time wide **descriptive baseline** of everything already present (§2a) — token metabolism, efficiency ratios, confidence distribution, verification coverage, cross-tradition census, reflexive-stream totals, known divergences | json never >24h behind db `mtime`; a freshness assertion exists and fails loud; baseline census written, every line tagged descriptive/provisional, **no verdicts** | near-none — deterministic census; model only narrates |
| **1 — Hygiene** | Spot data to clean / improve | every zero-token lane is fixed or explained in writing; instrumentation gap quantified per lane | judgment only: "is this drift meaningful or expected?" |
| **2 — Characterize** | Learn the system as it runs | a written, dated baseline of *normal ranges* per lane (cadence, in/out ratio, the four yield series) exists and updates weekly | synthesis/narration over deterministic stats |
| **3 — Tweak** | One-time recommendations | each recommendation carries evidence + an explicit reversal note; **never auto-applies** | the core judgment work |
| **4 — Control** | Metabolism as on-the-fly control signal | runs **shadow/dry-run only** ("what I would have done") for a long, named eval window before any actuation; reversible per swarm contract | hypothesis + gated decision, never silent action |

**Promotion rule (inherited from the janitor):** a phase is promoted only after the prior phase has produced a clean, reviewed cycle. Phase 4 is never promoted to autonomous by the agent itself — only Tom promotes it, after reading enough of its shadow log to trust it.

---

## 4. Scheduling across phases

- **Phase 0** — wire `metabolism_data.json` regen into a scheduled task (daily, ahead of `morning-system-health` at 06:00) or have the monitor regen-then-read at the top of its own run. Add a freshness assertion that fails loud if the snapshot is stale.
- **Phases 1–3** — one weekly scheduled task, `metabolism-monitor-weekly`, suggested **Sunday ~06:05** (after the janitor's 05:45, so the week's hygiene context is fresh). Baseline-then-deltas: first run snapshots current state as accepted noise; later runs flag only deltas.
- **morning-system-health integration** — the daily 06:00 report reads the monitor's `## New since last week` section directly (same wiring as `janitor/findings.md`), so weekday mornings restate the latest weekly deltas. No separate brief file.
- **Phase 4** — **not** a recurring autonomous task. It runs in shadow mode on demand or on a slow cadence, emitting a would-have-done log to `metabolism-monitor/shadow/`. Actuation stays manual until explicitly promoted.

---

## 5. Output layout

Following the `janitor/` and `connector-health/` shape, outside `wiki/` so Obsidian doesn't index it:

```
metabolism-monitor/
  findings.md          # weekly, ephemeral: New since last week + accepted-noise baseline
  state.json           # baseline + last-run state for delta computation
  logbook.md           # DURABLE, accumulates: the Phase-2 characterization, dated entries
  shadow/              # Phase-4 only: would-have-done control decisions, never actuated
```

The split matters: **findings are ephemeral** (this week's deltas), **the logbook is durable** (the accumulating "what we've learned about how the system metabolizes"). The logbook is the "assemble learning" deliverable from the original ask, and it is the wiki philosophy applied to the agent itself — write learning to the environment, don't re-derive it each run.

---

## 6. SKILL.md brief (sketch)

> You are the C2A2 Metabolism Monitor. Each week you read the current metabolism snapshot (`wiki/metabolism/metabolism_data.json`) and its source (`open-story.db` via the existing extractor) and report what changed and what it means. You do **not** recompute statistics the build pipeline already computes — counting, ranges, and drift are deterministic and belong in code; your judgment is reserved for *interpretation*: is this drift meaningful, what hypothesis explains a lane going quiet, which finding is worth a human's attention. You write three things: this week's deltas to `findings.md` (baseline-then-deltas), durable characterization to `logbook.md`, and — only once promoted to Phase 4 — would-have-done control notes to `shadow/`, which you never actuate. You fail loud: "no findings" after weeks of findings is itself a finding you must surface.

**Phase gating in the prompt:** the SKILL.md ships at Phase 1 scope. Phases 2–4 are added as named, separately-promotable sections so an outside reviewer can see exactly which capabilities are live.

---

## 7. Swarm-contract trace (`architecture/swarm-contract.md`)

1. **Richly introspecting** — every run states what it read, what it skipped, and the state it left in `state.json`.
2. **Richly creative** — the model's job *is* hypothesis generation about system behavior (Phase 2–3); PRS-shaped where it fits.
3. **Optimally transparent** — `findings.md` and `logbook.md` are short, sourced, dated, and diffable week over week.
4. **Falsifiable / self-correcting** — baseline-then-deltas, freshness assertions, and shadow dry-runs; a finding-count drop is escalated, not hidden.
5. **Pluralistic / charitable** — n/a to a metrics agent at face value, but recommendations about a thinker-lane must not privilege high-token lanes as "better"; cadence-only lanes are reported as instrumentation gaps, not as idle agents.
6. **Reversible** — no Phase-4 actuation without a prior shadow cycle; Phase 4 is permanently manual-promote. Mirrors the janitor's "destructive categories stay notify-only."

---

## 7a. Do not duplicate the self-awareness system

The project already runs a reflexive epistemic-hygiene layer: the daily `14a`/`15c` agents emit metrics snapshots in a rich assumptions/presumptions/premises/systemic-risk-flag vocabulary, and `narrative_prs_connectome.md` already defines the connectomic measurement vocabulary. The Metabolism Monitor must **own only the metabolism + efficiency slice that snapshot agent is not already computing**, (a) emit its findings *in the existing flag/assumption vocabulary* so they route into the same review pipeline, and (b) *consume* the standing flags rather than re-deriving them — specifically REVISE-124 (don't harden views on PRS-yield), REVISE-111 (pre-register falsifiers), OPEN-083 (metabolism cliff), OPEN-084 (three-count divergence). This is the same non-duplication discipline by which the janitor defers orphan-detection to the sewing agent.

## 8. Two cautions to bake in

**Keep the model out of the arithmetic (Rule 5).** Token counts, normal ranges, drift detection — deterministic, all code. The model's only jobs are "is this meaningful?" and "what explains this?". If the prompt doesn't draw that line, the agent burns tokens recomputing what a query answers.

**Don't close the loop on a Goodhart-vulnerable proxy.** *Corrected from the earlier draft:* the worry is **not** that PRS yield doesn't exist yet — it does (283 triplets, two series). The real worry is what the proxy measures: it counts triplets *present*, not their quality or validity, and the two series have different semantics (`prs_added` is git-first-seen, backfill-clustered; `prs_articulated` is self-reported and can be backdated — the snapshot even carries a 2022-07-01 articulated date). If agents are ever throttled or steered on metabolism, they will optimize the count, not the work. Phase 4 should therefore (a) control on `prs_articulated`-style "real work done" signal rather than token volume, and (b) wait until a *quality/validity* gate on triplets exists, not merely a count. The quality layer is partly here already — Confidence labels + sparse (1/6) email verification — but it is self-reported and thin; **the missing piece is a pre-registered falsifier** (REVISE-111) that says, in advance, what observation would distinguish a coil/triplet that *improves the system* from one that merely *adds graphics*. Until that falsifier is stated and the monitor is measuring against it, "usefulness" remains asserted, not shown. That is the honest reason to let Phase 4 lag well behind 1–3.

---

## 9. First concrete increment

**Phase 0 only**, now scoped as *reliable signal + descriptive census*:
1. Schedule the `metabolism_data.json` regen (or regen-then-read inside the monitor) and add a freshness assertion that fails loud if the snapshot is >24h stale.
2. Stand up `metabolism-monitor/` and write the one-time **descriptive baseline** census from §2a — token metabolism, the efficiency ratios (out/in, cache-read fraction, out/run, cadence), confidence distribution, verification coverage (1/6), cross-tradition census (90 + density/modularity), reflexive-stream totals, and the known divergences — every line tagged descriptive/provisional, **no verdicts**.
3. Fix the thinking-token join gap and resolve OPEN-083 (the live db is reachable from Cowork).
4. Edit the stale `_meta.note` string so the generator stops claiming PRS yield is "still to come."

Everything downstream reads that snapshot, so a reliable, fresh signal plus an honest census of what already exists is the load-bearing first step. The *judgment* work — pre-registered falsifiers and any verdict on coil/triplet usefulness — is deliberately deferred to Phase 2–3.

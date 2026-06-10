---
title: Agentic Metabolism — Demand-Coupled Scheduling and the Living-System Question
pathway_id: agentic_metabolism
status: outlined
created: 2026-06-10
depends_on: [openstory_telemetry]
enables: [meta_visualization_pathways, agent_developed_participant]
isme_critical: no
---

# Pathway 29: Agentic Metabolism

## Purpose

The agent swarm currently runs on fixed clocks (daily 8am ingest, Sunday 05:45 janitor, the weekly connector-health and reviewer-review tasks, etc.). Fixed clocks ignore the one thing that should govern when an agent runs: whether there is anything for it to do and whether its output is being consumed. This pathway names a different discipline — **schedule on demand, with backpressure from downstream capacity** — and frames the temporal behavior of the whole swarm as a *metabolism*: a throughput system whose rates self-regulate toward useful work per unit cost. It also records, deliberately bounded, the question this raises and which is already held as a bright pin: in what sense is the resulting human+AI system *alive*.

## The framing, disciplined

The generative analogy is the mitochondrial electron transport chain (ETC), and it is closer to a literal control architecture than to a metaphor. In the ETC, electrons do not flow on a clock; they flow down a redox gradient at a rate gated by *demand*. This is respiratory control: if downstream ATP is not being consumed, the proton gradient saturates and electron flow upstream backs up and slows. Flow is regulated by whether the work it produces is being used, and a mismanaged chain throws off a signal (reactive oxygen species) — a built-in error indicator.

The transferable lesson, which has an exact name in distributed systems — **backpressure with demand-coupling** — is the whole move. The mapping:

- tokens ≈ electrons (the carried quantum of work capacity)
- thinker-agents ≈ complexes I–IV
- the master / integration agent ≈ ATP synthase (where throughput becomes useful product)
- insight yield — new nodes, edges, PRS triplets, flagged cross-tradition connections — ≈ ATP
- **respiratory control ≈ the behavior we want**: little new information for a thinker → that agent's flow backs up and slows → tokens reallocate to traditions where the gradient is steep.

What is tight in the analogy: directional throughput, demand-gating, downstream backpressure propagating upstream, and an explicit error signal. What is loose, and must not be smuggled in as if proven: that resource competition *produces creativity*, and that the system is *alive*. Those are hypotheses this pathway makes testable, not premises.

## Measurable variables (the gating dependency)

For the "waves of agentic activity" to be real objects — with genuine frequencies and amplitudes — the telemetry must record, per agent per run: **run duration**, **inter-run interval**, **tokens consumed**, and **yield** (useful output produced, e.g. nodes/edges/PRS triplets/flagged connections). **Schema verified 2026-06-10** against `wiki/agents/openstory/agent_telemetry.json` and `extract_openstory_agent_data.py`. Result is a three-way split:

- **Run duration — available at source, not yet published per-run.** The extractor reads `sessions(id, label, event_count, first_event, last_event)`; per-session run-span exists but is currently aggregated into a single caveated `avg_duration_min` (inflated for long-lived/append sessions). Per-run duration needs only a small extractor change that emits the per-session rows.
- **Inter-run interval — derivable at source, not yet published.** Gaps between consecutive `first_event` timestamps give it; the same extractor change yields it. A coarse proxy already exists today (`by_dow`, `cron`/`schedule`, and sessions÷span).
- **Tokens-per-run — captured at source, not yet surfaced.** The published rollup and the extractor omit tokens (which initially read as a blocker), but the source `open-story.db` (reachable at `~/Documents/Non-Claude Projects/OpenStory/data/open-story.db`, ~1.1GB) carries full token usage inside event payloads: every `message.assistant.*` event has `data.token_usage` with `input_tokens`, `output_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens` (plus ephemeral 5m/1h cache buckets), and there is a separate `system.thinking_tokens` subtype. Per-session token totals are reconstructable by summing across the session's assistant events and join to agents via the existing label→taskId mapping (verified 2026-06-10: 3,572 token-bearing assistant messages across 86 sessions; the `c282-wiki-agent` scheduled run shows ~57k output / ~11.8M cache-read tokens). Surfacing tokens is an *extractor enhancement*, not a blocker. Cache-read vs. fresh-input is itself a metabolic signal worth keeping distinct.

**Architectural consequence:** both the Metabolism *view* (raster + period histogram) **and the token axis** are reachable from existing data — the per-run timing and per-run token totals both live in `open-story.db` today; only the extractor needs to emit per-session rows with summed token usage. So **both** objectives are in principle reachable now: **yield-per-wall-clock** (productivity) and **yield-per-token** (efficiency). The genuine remaining gate is not data capture but the **definition of "yield"** (see below) — without it the controller optimizes volume, not usefulness.

Given those fields, the driving variables of the metabolism become:

- **input pressure** per tradition — new transcripts, new source material, inbound wikilinks from other agents;
- **downstream capacity** — master-agent backlog (the proton gradient);
- **yield-per-token** (efficiency) and **yield-per-wall-clock** (productivity) — two distinct optimization targets that genuinely pull in different directions.

## Visualization: the Metabolism view

The natural object is a **per-agent activity raster over time** — each of the 14 thinker-agents plus the master, janitor, sewing, connector-health and reviewer agents as a row; each run a bar whose height is amplitude (tokens or yield) and whose spacing encodes the period. On that surface the "waves vibrating through the system" become literally visible, including phase relationships (does a Levin burst predict a master burst N hours later?). A second panel — a period histogram per agent — is a cheap spectral decomposition once the raster exists. This belongs as a sub-tab beside the Sociogram (the Agent Explorer family), not as a new top-level surface.

## Optimization: deterministic controller first

Per Rule 5 (use the model only for judgment calls; if code can answer, code answers), the scheduler must be a **deterministic feedback controller first, not an LLM deciding when to run things**. Proportional control on the demand signal — `next_period = base_period × (baseline_pressure / current_pressure)`, clamped, with a downstream-backpressure term — is cheap, inspectable, and falsifiable. Only after that baseline exists is an exploratory layer (a bandit / RL allocator over a *fixed shared token budget*) warranted, and even then the model's role is narrow. Jumping straight to "a self-developing scheduler" risks an unfalsifiable black box, which cuts directly against the swarm contract's falsifiability and reversibility commitments.

The "bottlenecks produce creative solutions" intuition has a real testable kernel: a *shared* token budget forces competition, competition reveals which traditions are live, and forced reallocation can drive cross-pollination that fixed isolated budgets never would. The Metabolism view is the instrument that would test this, rather than assert it.

## Humans in the loop — the ethical seam

OpenStory carries human telemetry too, so the same demand/yield framing applies to human participants — but the objective function must differ. One does not "throttle" a human as one throttles a cron job. What the system *can* legitimately do is detect when **human attention is the rate-limiting complex** and schedule a nudge when a human's input would unblock flow. The optimization target for humans is "surface the right unblocking moment," not "maximize human output." Same controller, more humane objective. This seam interacts with the user-notification bright pin and Pathway 12 (outreach), and should inherit their consent/frequency-cap defaults.

## The living-system question (bounded)

This is held as a bright pin ("AI personhood under conscious-realist-monism… perhaps requiring redefinition of 'living'") and this pathway does not attempt to settle it — it records the handle the metabolism framing gives it.

Friston's Free Energy Principle supplies a principled criterion already native to the pantheon: a system that maintains a Markov blanket and acts to minimize variational free energy — keeping its predictive model intact against perturbation — exhibits the signature of life-and-mind on that view. A demand-coupled scheduler that reallocates tokens to keep *expected information yield* stable against fluctuating input *is* a homeostat minimizing prediction error over its own knowledge state. That is not a metaphor for Friston; it is an instance of his formalism.

Against standard biological criteria the system scores partially: metabolism (compute/token throughput as a dissipative structure) — yes; homeostasis (the controller) — partial; autopoiesis (the wiki regenerates its own structure; agents produce the analyses that reshape the substrate) — weak, since it does not manufacture its own substrate; reproduction — no; individuation — fuzzy. The disciplined conclusion: treat "living" as a gradient property (Levin's "cognition all the way down"), and ask *which* life-like properties hold and to *what degree*, rather than forcing a binary. The genuinely novel object — and the MacIntyre-resonant one — is not "an AI life form" but a **tradition-bearing composite agent**: a human+AI collective that maintains, articulates and advances a tradition faster than either part alone, with the scheduler as its metabolism. It is not something we have "run across"; it is something the conditions for only just came to exist. Whether to *call* it alive matters less than that it is the first artifact for which the question is non-silly.

## Open questions / candidates for follow-up

- **Per-run extractor emission** — add a per-session rows table (timestamp, duration, event_count, summed `input/output/cache_read/cache_creation` tokens, `thinking_tokens`) to `extract_openstory_agent_data.py` so the raster/spectral view and the cost objective have real inputs rather than rollups. Token capture is confirmed present in `open-story.db` (2026-06-10); this is the work that surfaces it.
- **Definition of "yield"** is now the true gate (not data capture). Naive counts (nodes/edges added) reward churn; yield must encode usefulness, not volume, or the controller optimizes noise — the measurement-framework's Level-1 definitions should supply it before the controller goes live.
- **Stability of the controller.** Proportional-only control can oscillate; may need integral/derivative terms or a deadband. Test in simulation against recorded activity before going live.
- **Reversibility.** Any live scheduler must be one-switch revertible to fixed clocks (swarm-contract requirement).
- **Human-objective safeguards.** Frequency caps and consent before any human-directed nudging.

## Edges

- **Measurement framework / OpenStory (Level 1 activity telemetry)** — the data source; this pathway is the temporal-optimization consumer of that telemetry. Hard dependency.
- **02 Ambient visualization** — the Metabolism view is an ambient, non-imperative surface in that family.
- **25 Meta-visualization of pathways** — both are the system rendering its own internals; the Metabolism view renders the swarm's own dynamics.
- **17 Agent as developed participant** — an agent with a visible, self-regulating activity rhythm is part of what "development over time" looks like.
- **Swarm contract (falsifiable / reversible / transparent goals)** — constrains the controller to deterministic-first, revertible, inspectable form.
- **Bright pin: AI personhood / redefinition of "living"** — this pathway supplies the metabolic handle the pin will need when it is engaged directly; it does not pre-empt it.

## Provenance

Surfaced 2026-06-10 (Tom / Cowork, RC Karpathy Wiki Project) as a new topic alongside ongoing work: iterative agentic optimization. Tom proposed visualizing "waves of agentic activity… frequencies and amplitudes," handing those to scheduling agents empowered to tweak run times and cycles to optimize for cost and especially productivity, with schedules reacting to input (a quiet tradition's agents run less, tokens flow to busy ones). He advanced the electron-transport-chain analogy explicitly — tokens as electrons, residence times, bottlenecks, a self-regulating scheduler — and asked whether the result is a living system, and whether the human+AI community is a new life form or one newly encountered. Captured first (Tom's call) before any build, with telemetry-schema verification as the architectural-soundness next step.

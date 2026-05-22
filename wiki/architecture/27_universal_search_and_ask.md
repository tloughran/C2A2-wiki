---
title: Universal Search and Ask
pathway_id: universal_search_and_ask
status: drafted
created: 2026-05-19
depends_on: [broker, perspective_lattice, honesty_layer]
enables: [recursive_episode, apprentice_mode]
isme_critical: yes
---

# Pathway 27: Universal Search and Ask

## Purpose

Every tab of the C2A2 explorer should answer two different questions a visitor arrives with:

- **"I know the thing — take me to it."** A name (Levin), a concept (Markov blanket), an identifier (PRS-04, FINDING-018a, CROSS-051), a Summa locus (I-II.Q19.A10), a pathway (00 Broker). The visitor wants the origin file, fast, with no inference.
- **"I have a question — answer it from the corpus."** A natural-language query that has no single home file and needs synthesis across traditions.

These are different intents and they want different machinery. Conflating them into one box produces something that does neither well. Pathway 27 provides **both**, on every tab: a deterministic **Search** box and a semantic **Ask** box.

The non-obvious design move is that the first of these shares a substrate with a third, already-wished-for capability — *maximal hyperlinking of every name, concept, and relationship to its origin*. Search-with-jump-to-origin and auto-hyperlinking are two surfaces of the same underlying artifact: an entity → origin-file index. Build it once; expose it three ways.

## Search is not hyperlinks, and hyperlinks are not Search

A natural temptation is to think that if every entity in the prose were hyperlinked to its origin, a Search box would be redundant. It is not. Hyperlinks serve the visitor who is *already on a page* and wants to jump laterally ("reading Levin, click 'Friston'"). Search serves the visitor who arrives *cold* ("just opened the app — where is the thing on the cognitive light cone?"). Maximal linking presupposes you have already landed somewhere; it cannot cover the cold-start entry point. So the system needs both — but, crucially, they can be driven by one index.

## The shared substrate: an entity index

The vault already carries clean, structured, rename-safe identifiers: the fifteen tradition names; `PRS-NN`, `FINDING-NN`, `CROSS-NN`, `OPEN-NN`, `ASSUMPTION-NN`, `PRESUMPTION-NN`, `DECISION-NN`; pathway ids; and Summa loci (`I-II.Q19.A10`). A build step — modeled on the existing `summa_index.json` / `extract_vault_data.py` generation — produces a single `entity_index.json` mapping each canonical entity to its origin file(s) and a short gloss. This index is the spine of the whole pathway:

1. It powers the **Search** box (autocomplete + jump-to-origin).
2. It powers **canonical auto-hyperlinking** of those entities wherever they appear in rendered prose.
3. It powers **pop-up-with-link-to-origin** when an entity is touched in any view (Sociogram node, Summa article, pathway doc).

Linking *canonical structured entities* — not every word in every sentence — is what keeps this from becoming visual noise and a maintenance sink. Keyed by ID, the links survive renames.

## Function set

The pathway holds four jobs:

1. **Entity index build.** A deterministic generator scans the vault for the canonical entity set, resolves each to its origin file(s) plus a one-line gloss, and emits `entity_index.json`. Runs in the same family as the Sociogram/Summa index builds; should be wired so the flag/scope can never be silently dropped (cf. the `--summa` recurrence — see `regen_sociogram.sh`).

2. **Search box (lexical, deterministic, client-side).** Present on every tab via the explorer shell. Typeahead over the entity index; selecting a result jumps to the origin file (or pops it in an overlay). No broker, no API, instant. This is the cold-start entry point.

3. **Ask box (semantic, broker-backed).** A natural-language query box that routes through the **broker** (Pathway 00) for the API call, scope enforcement (answers stay within vault topics), and the **honesty layer** (Pathway 14) for evidence-strength tagging and source citation. Draws on the precomputed overviews of the **perspective lattice** (Pathway 04) where possible to keep latency and cost down. Slower and non-deterministic by nature — kept visibly distinct from Search so the visitor knows which they are using.

4. **Canonical auto-hyperlinking.** A render-time pass that turns recognized entities in displayed prose into links to their origin, driven by the same `entity_index.json`. First-mention-per-view (or a similar density rule) to avoid over-linking.

## Architecture fit

- **Search + hyperlinking are client-side**, off the prebuilt `entity_index.json` (same deployment pattern as the Sociogram's baked-in data). No server dependency.
- **Ask requires the broker** (Pathway 00) — it cannot live in client JS (API key exposure, scope enforcement, consent gating), and its answers must pass through the honesty layer (Pathway 14).
- **Depends on:** `broker` (Ask), `perspective_lattice` (overview source for Ask), `honesty_layer` (Ask answer discipline).
- **Enables:** faster navigation across all tabs; feeds `recursive_episode` (Pathway 11) and `apprentice_mode` (Pathway 15) by making any referenced entity one hop from its source.

## ISME staging

The two halves do not have to ship together:

- **Search + canonical hyperlinking — ISME-critical, ship before 2026-07-08.** Cold-start navigation is table-stakes for a public demo, and it is broker-independent, so it can land early with low risk.
- **Ask — stage after.** It is broker-dependent and heavier; it should follow once the broker (Pathway 00) and honesty layer (Pathway 14) are themselves shipped, not before.

## Open questions

- **Index freshness.** Like the Sociogram and Summa indexes, `entity_index.json` is a derived artifact and will drift unless its rebuild is wired into the daily pipeline. How is it kept current — own build step, or folded into an existing regen? (The lesson from the `index_summary.md` staleness and the `--summa` recurrence: a derived index that nothing schedules *will* go stale.)
- **Two boxes or one labeled toggle?** Two visibly distinct boxes is the safe default, but a single box with a Search/Ask toggle may read more cleanly on the ≤640px mobile layout (Pathway 02 / mobile pass) — to be decided in the design-critique step.
- **Hyperlink density rule.** First-mention-per-view vs. per-section vs. all-mentions — needs a usability call so links inform without becoming noise.
- **Entity disambiguation.** Some surface strings are ambiguous (a thinker's surname vs. a tradition page vs. a PRS author attribution). The index needs a precedence/disambiguation rule, and Ask needs to handle "did you mean…".

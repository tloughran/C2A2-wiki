# C2A2 — Community Context for AI Alignment

A research-preview knowledge system that builds rich, structured **context** about a community of human intellectual and spiritual traditions, so that AI systems can be aligned to the actual diversity of how people reason — not a flattened average of it. Mechanically, it is a *community dialogue accelerator and detector*: it holds each tradition at enough depth that AI agents can reason inside it, surfaces where traditions **converge, conflict, or formally bridge**, and audits its own assumptions as it grows.

> **Live explorer:** https://tloughran.github.io/C2A2-wiki/wiki/explorer.html
> *(Pages URL — please confirm against your repository's Pages source setting before relying on this link.)*

---

## What this is

C2A2 treats each thinker's body of work as a *research-program tradition* in the sense Alasdair MacIntyre and Thomas Kuhn use the term: a living, problem-solving enterprise with its own questions, resources, and solved problems. Fifteen traditions are currently held in the system:

Levin · Friston · Hoffman · Hawkins · McGilchrist · Fredrickson · Stump · Carroll · Arkani-Hamed · Wolfram · Kastrup · Wright · Rohr · MacIntyre · Loughran

Each tradition lives under `wiki/traditions/<name>/` as a program overview (`wiki.md`) plus a full record of its **PRS triplets** (`prs_triplets.md`). A master integration layer cross-indexes the programs and a pattern-detector layer flags cross-tradition findings.

The system is built to do three things at once:

- **Accelerate traditions** — hold each program deeply enough that an agent can carry on a mature internal conversation in its idiom.
- **Detect cross-tradition structure** — surface convergences, conflicts, and formal bridges between programs (e.g., Hoffman's trace operator ↔ Levin's cognitive light cone).
- **Stay methodologically self-aware** — a self-awareness pipeline continuously extracts the system's own assumptions and presumptions, runs literature searches for and against them, and dispositions the results, so the framework's commitments stay visible and revisable.

## The explorer

`wiki/explorer.html` is the public shell, with four working visualizations:

- **Sociogram** — a force-directed graph of the full wiki (1,500+ nodes across the traditions and the integrated Summa companion), with assembled narration tracks and text-to-speech.
- **3D PRS** — a three-dimensional view of the Problem–Resource–Solution triplet network.
- **Agent Map** — the network of autonomous agents that maintain and extend the wiki.
- **Curriculum Tools** — the **Summa Explorer**: Aquinas's *Summa Theologiae* browsable article-by-article, each paired with a contemporary-science commentary written from the fifteen-tradition worldview (the companion "Summa 2026 in a Year" project).

## Method and authorship

The **PRS triplet** form (Problem → Resource → Solution) and the **Synergistic Coil** concept (a single resource bridging many problem⇒solution transitions) are the author's own framework, not any tradition's. The per-tradition `prs_triplets.md` files are a *re-description* of each thinker's work in PRS form, used to interlink the traditions — they are not the thinkers' own self-descriptions.

The lineage behind the method: **Kuhn** (the solved problem as the unit of scientific progress) + **MacIntyre** (traditions as narratives of shared goals, advanced through problem-resource-solution moves) + **Levin**, via **William James** (intelligence as problem-solving under limited resources — one resource solving many problems).

The integrative orientation under which the traditions are read together is a **conscious-realist monism**: roughly, that consciousness is a real feature of the world rather than an illusion, and that the phenomena studied across the sciences are aspects of a single underlying reality. This orientation is held openly and is itself subject to the system's honesty-layer discipline — it is the frame under which the traditions are read, not a claim imposed on them.

## Repository layout

```
wiki/
  explorer.html              # public four-tab shell
  wiki_narration.html        # Sociogram (force-directed graph)
  prs_3d.html                # 3D PRS view
  agents_tab.html            # Agent Map
  summa_explorer.html        # Curriculum Tools / Summa Explorer
  traditions/<name>/         # per-tradition wiki.md + prs_triplets.md
  master/                    # cross-program index + integration layers
  architecture/              # self-awareness pipeline (assumptions, presumptions, decisions, lit-search)
  vault/                     # Summa transcripts + contemporary commentary + index
scripts/                     # reindexers and build tooling
sync_vault.sh                # syncs the Summa vault into the wiki and publishes
```

## Status

This is an active **research preview**. The traditions are maintained by a network of scheduled agents; the explorer is demoable but has visible rough edges. Cross-tradition findings are produced continuously and are best read as *signals for further inquiry*, not settled results.

## Provenance

The wiki was first shipped publicly within 24 hours of the Andrej Karpathy post that prompted it, and has been a public repository since 2026-05-04. Commit history documents that timeline.

## Author

Tom Loughran — University of Notre Dame, Department of Physics & Astronomy.

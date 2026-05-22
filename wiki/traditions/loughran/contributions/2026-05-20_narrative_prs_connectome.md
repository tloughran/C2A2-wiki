*Mirror of [[architecture/narrative_prs_connectome|architecture/narrative_prs_connectome.md]] — placed here as a Tom Loughran thinker-contribution and laced into the connectome.*

# The Narrative (PRS) Connectome — Architectural Model

*Author: Tom Loughran (C2A2 Project Director). Drafted in dialogue with Claude (Cowork), 2026-05-20.*
*Status: **Architecturally guiding** — a definitional / directional document. Proposed changes to the PRS visualization should be evaluated against the model set out here.*

## Thesis

The view we have been calling "3D PRS" is not a chart of triplets. It is a **connectome** — and specifically a **narrative connectome**. The human brain connectome, so beautifully visualized today, wires together neural units; Jeff Hawkins' Thousand Brains theory wires together *cortical columns*, each a complete model of the world; the PRS view wires together **agentic narratives**, each of which is itself a complete little model. This is not a metaphor laid over the tool after the fact. It is the model the tool has implicitly been built on, now made explicit so that we can build it deliberately — because a visualization is only ever as good as the model of *what is being visualized* that drives it.

## The unit: the agentic PRS narrative

The connected unit is the **PRS triplet**, read in full as an *agentic narrative*:

> Here is an agent. Here is its goal. Here is the problem it meets. Here is the resource it brings to bear. Here is the solution. Here is how it turned out.

Read this way, a triplet is a **model** — a structured claim about how an agent moves through a region of problem-space — and, equivalently, a **compression**. A narrative is a low-entropy encoding of a long, contingent traverse: it keeps what is load-bearing and discards the rest. *Every story is such a compression.* Each triplet is therefore a small **processing unit**: it takes a situation as input and yields a transformed situation as output. This is exactly the status Hawkins grants the cortical column — not a passive datum but a complete modeling element. The neuron is to the column as the individual proposition is to the PRS narrative: the smaller thing matters, but it is not the unit of cognition.

## From neural connectome to narrative connectome

Three connectomes, one architecture:

- **Neural connectome** — units: neurons / regions; edges: axonal tracts.
- **Hawkins / Thousand Brains** — units: cortical columns, each a *complete* reference-frame model; edges: cortico-cortical connections over which thousands of models **vote** toward a consensus percept.
- **Narrative (PRS) connectome** — units: agentic PRS narratives, each a complete model/compression; edges: shared resources, shared problems, and — across traditions — **synergistic coils**.

On this reading the **coils are not decoration; they are association fibers** — the long-range connections that bind otherwise-separate narrative regions into a larger whole. A tradition is a *module* of densely interconnected narratives; a coil is the fiber that lets two modules begin to function as one.

## Visualization is model-driven

We cannot decide *what to visualize* until we are clear about *what we are visualizing*. Every visualization encodes a model, whether or not its makers have articulated it. The model here is now stated plainly: **the interconnection of narratives**, where narratives are agentic PRS models, and where the object of interest is how local models knit into larger ones. This document is that model; the tool should be answerable to it.

## The telos: the emergence of a master science

What the connectome ultimately lets us watch is **emergence** — many complete-but-partial narratives cohering, by resource-sharing and by coil, into something larger: a **master science**. By this we mean what Aristotle called an *architectonic* science and Aquinas *sapientia* — the ordering inquiry by which a tradition grown to maturity governs and integrates its own sub-inquiries. It is inseparably theoretical *and* practical, and tradition-bound: the maturest available narrative of a tradition's pursuit of its goods, continually re-narrated as it solves and is reshaped by its problems — what Alasdair MacIntyre characterized as the goal of rational inquiry on the **tradition-craft** model. Crucially there is **not one** master science but **rivals**: each mature tradition articulates its own, and they meet — through coils — as rivals and as complements, never as a single convergent whole. "Master" here is *architectonic* (ordering), never *dominating*; the rivalry, held in mutual respect, is what keeps it so. The narrative connectome is, in effect, an instrument for watching a master science take form within a tradition, and for staging the encounter of rival master sciences across them.

## Directives (Tom Loughran)

1. **Rename the view.** "3D PRS" → **"Narrative (PRS) Connectome Explorer."** The name should announce what the tool is, not the data type it happens to ingest.
2. **Re-derive the perspectives from the model.** The Sociogram view carries a rich, well-considered control set. The Connectome deserves an equally rich but *different* set — chosen by asking what a narrative connectome specifically needs to make visible (see proposals below). Parity of *richness* with the Sociogram, not parity of *controls*.
3. **Author-contribution convention.** This document — and every definitional/directional document of which Tom is the author — is placed both here (`architecture/`) and as a copy in his thinker file (`traditions/loughran/`), and laced into the connectome via wikilinks. The project's own guiding narratives thereby become nodes in the connectome they govern: the system documents itself inside itself.

## Proposed perspectives (Claude — for Tom's review)

Candidate "views" the Connectome Explorer could offer, each a different question put to the same narrative connectome:

- **By tradition (module view).** Already present — color/filter by thinker. The connectome reframing makes this a view of *modules*.
- **By shared resource (pluripotency).** Partly present already (resource nodes scale with how many narratives share a resource). Promote it to a first-class lens: surface the **hub narratives** whose resources recur across many problems — the connectome's high-degree nodes.
- **By coil (association-fiber view).** Foreground the cross-tradition bridges; let the user isolate the fibers and see which modules they join. (The new coil layer is the seed of this.)
- **By emergence over time.** Watch a master science accrete: play the connectome forward and see when modules begin to wire together. This is where the temporal axis earns its meaning (see open decisions).
- **By convergence.** Hawkins-style "voting": highlight where many independent narratives converge on the same solution or resource — candidate sites of a forming master science (descriptive: *where* convergence is, not a verdict that it is right).
- **By problem-kind.** Cut across traditions by the *type* of problem the narratives address, rather than by who authored them.

## Proposed: connectome metrics (Claude)

If it is a connectome, it admits connectomic measurement. Borrowing from network neuroscience: **degree / hubs** (high-pluripotency narratives), **modularity** (tradition cohesion), **cross-module fibers** (coil density between two traditions), and **path length** (how many narrative steps separate two ideas). These give quantitative handles on claims the project already wants to make — e.g. "these two traditions are beginning to integrate" becomes "cross-module fiber density between modules A and B is rising."

## Proposed: the compression / entropy thread (Claude)

The compression reading is not ornamental — it is a bridge to measurement and to other programs. If a narrative is a compression, then *progress* is better compression: a later narrative that predicts/explains more of the same problem-space with less. This reconnects to [[traditions/friston/wiki|Friston]] (free-energy minimization as compression), to [[traditions/wolfram/wiki|Wolfram]] (computational irreducibility as the limit case of incompressible process), and to the original RC-pilot ambition of **quantifying progress through chained PRS triplets**. A master science forming should be visible as the connectome's *total description length falling* even as it covers more.

## What this reframes (open decisions)

The model subordinates two decisions that were on the table:

- **Meaning of the vertical axis.** It currently encodes publication year. Under the connectome model the honest candidates are *narrative/developmental time* (when an idea entered its tradition) or *connectome time* (when narratives wired together). Pick deliberately, per the model, rather than by what data we happen to have.
- **Coil "altitude."** A coil should sit where its **bridging insight was formed** (discovery-time, ~2026 for nearly all current coils), not at the age of the ideas it joins — which is why coils presently sink to the founding era and never reach the recent band. This is the concrete first test of "axis follows model."

## Connections

This narrative is itself a node. It connects to: [[traditions/hawkins/wiki|Hawkins]] (cortical column as modeling unit; voting toward consensus), [[traditions/macintyre/wiki|MacIntyre]] (tradition-craft; the telos of inquiry as a theoretical-practical narrative), [[traditions/friston/wiki|Friston]] (compression / active inference), [[traditions/levin/wiki|Levin]] (agency as the mark of the narrative unit), [[traditions/wolfram/wiki|Wolfram]] (computation and compressibility), and [[traditions/loughran/wiki|Loughran]] (the Synergistic Coil as association fiber). Its operative data live in the PRS triplet records and the cross-program / coil index that the Narrative (PRS) Connectome Explorer renders.

---
title: Quantification-on-Demand Whiteboard
pathway_id: whiteboard
status: drafted
created: 2026-05-13
depends_on: [broker, voice_dialogue, probing_channel]
enables: [under_development_visualizer, generative_canvas]
isme_critical: no
---

# Pathway 05: Quantification-on-Demand Whiteboard

## Purpose

A new tab alongside the Sociogram: a blank canvas where any active intelligence can request a plot in natural language and have it appear, then modify it conversationally. "Plot the dates proposals were made versus the dates they were approved versus the dates written to the wiki and pushed to the repo." That sentence should produce a plot, on the fly, with the data fetched from the right sources, and that plot should then be modifiable by further conversation ("group by month," "add approval lag as a third series," "make the y-axis log").

The pathway exists because the project has too much data not to have an on-request look at it. The Sociogram visualizes the vault's content; the 3D PRS view visualizes its conceptual structure; this whiteboard visualizes everything else — including the project's own development.

## Function set

The whiteboard has four moving parts:

1. **Request parser.** Natural-language requests (voice or text) are parsed by the agent into a plot specification: axes, filters, time range, dimensionality, aggregation. The output is a Plotly JSON spec.

2. **Data layer.** A thin uniform interface over multiple sources:
   - *Vault data:* node frontmatter (dates, thinkers, structure groups, edges).
   - *Git history:* commit timestamps, files changed, authors (for the project's own development trajectory).
   - *Session archives:* when sessions ran, what they touched.
   - *Scheduled-task logs:* outputs of the daily 8 AM wiki agent and any others.
   - *Agent action logs:* proposals, approvals, writes, pushes — the system's own activity.
   The data layer exposes these as queryable series, with a small set of view-tables (events, files, sessions, runs, vault_nodes, vault_edges).

3. **Plot renderer.** Plotly.js handles the rendering. Plotly is the right first step because (a) it handles 4D and 5D plots (axes + color + size + time) natively, (b) it supports animation via a play button and time-slider, (c) Plotly specs are JSON, so mutations are cheap (an edit, not a regeneration).

4. **Conversational mutation.** Subsequent requests modify the existing spec rather than building a new one. "Log-y" → edit the y-axis spec. "Group by month" → edit the aggregation. "Add approval lag" → add a third series. Each mutation is a small JSON diff.

## What's a view-table? *(apprentice note)*

A view-table here is just a logical name for "a stream of structured records you can query like rows in a database, even though the underlying data may be files, JSON, or git history." So `events` is a view-table that surfaces "proposal made," "wiki write," "git push" as rows with timestamps, even though those events live in completely different physical formats. The data layer's job is to make all those sources look like the same kind of thing to the request parser.

## Architecture sketch

```
voice/text request
        ↓
   agent parses → Plotly JSON spec
        ↓
   data layer fetches from sources:
   ├─ vault frontmatter
   ├─ git log
   ├─ session archives
   ├─ scheduled-task logs
   └─ agent action logs
        ↓
   spec + data → Plotly renderer
        ↓
   plot appears in whiteboard tab
        ↓
   mutation requests → spec diffs → re-render
        ↓
   probe events (clicks on plot) → probing_channel (Pathway 03)
```

## Decisions taken

- **Plotly-first.** It speaks JSON, animates 4D and 5D natively, and is widely used (Tom knows it). Custom one-off geometry (like the thinker-simplex from the generative-canvas pathway) goes through Pathway 06 instead.

- **Thin data layer, grow as questions arise.** Don't pre-instrument every possible data source. Start with the cheap ones (git log, file mtimes, session-archive index, scheduled-task outputs). Grow the data layer when a question reveals what's missing. This honors Tom's instinct: "I'm not sure what steps to take toward quantification in advance."

- **Mutations as spec diffs, not regenerations.** Conversational editing should be fluid — log-y, group-by-month, add-series should each be a small JSON patch on the existing spec, not a fresh render.

- **Plots are participants, not artifacts.** The agent narrates plots the same way it narrates the Sociogram. "Play that again." "Stop here." "What's the meaning of that sharp dip?" All work via the probing channel (Pathway 03) and the dialogue layer (Pathway 01).

- **Suggestion mode.** The agent can interject "want me to plot this?" whenever the dialogue touches a quantifiable claim or trend. Triggers: "how often," "over time," "compared with," "since when," "growing," "dropping," "rate of," "trend in." Gated behind a single permission so the suggestions don't become noisy.

- **Provenance carries forward.** Every plot includes the queries used to generate it (in a small caption or expandable footer). Claims the agent makes about plot features (the meaning of a dip, the cause of a spike) are tied to the underlying rows, not improvised.

- **Plot persistence: ephemeral by default, "Pin this" promotes to vault** (decided 2026-05-13). The whiteboard tab is a scratchpad; most plots are exploratory and short-lived. A "Pin this" action persists the plot into the vault as a markdown node (with the embedded Plotly spec, a snapshot image, and a provenance footer), making it available for future sessions and Sociogram inclusion.

- **Export file button alongside Pin** (decided 2026-05-13). Per-plot export to PNG, SVG, HTML (standalone interactive), CSV (underlying data rows), or PDF. Plotly provides the rendering paths natively; the broker assembles the requested file for download. Useful for moving a finding out of the whiteboard into papers, slides, or emails.

## Open questions

- **Time-element semantics for 4D and 5D.** When a request says "video-transform this," what defaults apply? Frame rate? Easing? Auto-play vs. wait-for-user? Probably tied to the play-button affordance Plotly already provides.

- **Performance ceiling.** What's the largest data series the whiteboard can render smoothly? Plotly handles ~50K points well, ~500K with degradation. The project's own activity data is small (sessions, commits) but vault-content joins could grow.

## Edges

- **broker (00):** request parsing and data-fetch routing happen broker-side; agent calls flow through.
- **voice_dialogue (01):** plot requests and mutations arrive via voice; plot narration ("what's that dip?") flows through the same dialogue layer.
- **probing_channel (03):** clicks on plot points produce probe events with `element_type: "plot_element"`.
- **generative_canvas (06):** when a request needs custom geometry beyond Plotly (e.g., the thinker-simplex), it routes to Pathway 06 instead.
- **under_development_visualizer (13):** the whiteboard's data layer is also what the development visualizer queries. The under-development view is one specific Plotly spec the whiteboard renders.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- Emerged from Tom's specific request: "I'd like to ask for a plot of dates proposals were made vs dates proposals were approved vs dates written to wiki and pushed to repo." Followed by the reflexivity observation — once the system can plot its own activity, it becomes capable of observing its own becoming.

## Status

Drafted in prose. Implementation order: (a) thin data layer over git log + session archives + frontmatter (cheap, fast), (b) request parser that emits Plotly JSON, (c) renderer with mutation support, (d) suggestion mode triggered by dialogue keywords. The under-development visualizer (Pathway 13) is a concrete first consumer.

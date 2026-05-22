---
title: Under-Development Visualizer
pathway_id: under_development_visualizer
status: drafted
created: 2026-05-13
depends_on: [whiteboard, voice_dialogue]
enables: []
isme_critical: no
---

# Pathway 13: Under-Development Visualizer

## Purpose

A live view of the system's own build state, surfaced as a peer tab in the Sociogram shell. Pathways shown as nodes; dependencies as edges; statuses (outlined / drafted / in-progress / implemented) as colors. Open questions as annotations. Activity (commits, scheduled-task runs, agent actions) as time-series.

The visualizer is more than a status board. It is the entry point for a distributed community of builders. **GitHub is a vector** — possibly a more important reach channel than YouTube — and this view points newcomers at what's open, what's underway, what needs help, and (eventually, via Pathway 15) at the apprentice-mode pathway for ramping into the project's conceptual layer.

## Function set

Four moving parts:

1. **Build-state node graph.** A force-directed graph of the eighteen pathways with their dependencies. Each pathway carries: status, ISME-criticality, open-questions count, last-touched timestamp. Edges show `depends_on` and `enables` relationships from each pathway's frontmatter.

2. **Activity time-series.** A Plotly view (via Pathway 05) of project activity: commits per day, sessions per week, agent actions over time, pathways moving status. This is the reflexive data that lets contributors see the project's pulse.

3. **GitHub integration.** Each pathway node links to its corresponding GitHub Issues and Pull Requests (created with a `pathway:NN` label). Newcomers click a pathway and see open issues, recent PRs, discussion threads. The visualizer is the project's developer-facing tab.

4. **Contributor on-ramp.** For new arrivals, the visualizer highlights pathways with `help wanted` issues, links to a CONTRIBUTING document, and points at the apprentice-mode pathway (Pathway 15) for those who want to ramp into the conceptual layer rather than the code layer.

## Architecture sketch

```
data sources (via Pathway 05 data layer):
├─ pathway frontmatter (architecture/*.md and wiki/Architecture/*.md)
├─ git history
├─ session archives
├─ scheduled-task logs
├─ agent action logs
└─ GitHub API (Issues, PRs, Discussions)
        ↓
   visualizer renderer (whiteboard tab)
   ├─ pathway node graph (force-directed)
   ├─ activity time-series
   ├─ GitHub overlay
   └─ contributor on-ramp panel
```

## Decisions taken

- **GitHub-as-vector framing.** The visualizer is built for contributors, not just observers. YouTube reaches viewers; GitHub reaches builders. The under-development view treats the project as a community of practice substrate, not as a one-direction broadcast.

- **Reflexive data is first-class.** The system observes itself. Build state, activity, agent actions — all are visible. This embodies the project's larger commitment to traditions observing their own becoming.

- **Renders on the whiteboard.** Not a bespoke viz, but a specific Plotly + custom-canvas spec the whiteboard renders. Same data layer, same renderer, same probing channel.

- **GitHub Issues are the participation surface.** Each pathway has a corresponding label; newcomers find work by browsing labels rather than reading the entire codebase.

## Open questions

- **What counts as "help wanted."** Tom-curated, agent-curated, or community-curated? Strawman: agent proposes, Tom approves, community can suggest via Issues.

- **Contributor authentication.** Public contributors need a GitHub identity. The visualizer can show their PRs and Issues; how much of their work gets surfaced in the C2A2 narrative is a separate question.

- **Public vs. internal view.** The visualizer's full state (including unfinished decisions, in-progress pathways, internal-only annotations) is useful internally but possibly noisy publicly. Two views, with a privacy toggle? Or one view with the same content for everyone? Worth Tom's judgment.

- **Apprentice-mode link surface.** When the apprentice pathway exists, the visualizer should make the on-ramp obvious. UX detail: a persistent "new here? start with the conceptual tour" link in the contributor on-ramp panel.

## Edges

- **whiteboard (05):** primary renderer. The visualizer is one specific spec the whiteboard's data layer produces.
- **broker (00):** broker's own activity logs feed the visualizer (rate of requests, escalation approvals, outreach issued).
- **outreach_automation (12):** outreach activity surfaces as a time-series on the visualizer.
- **apprentice_mode (15):** newcomers click through from the visualizer's on-ramp into the dialogical curriculum.

## Provenance / source dialogue

- Session: 2026-05-13 dreaming pass (Sarah / Cowork).
- Tom: "we want an under-development visualizer, as well, I think. That should be easy enough. … a construction pathway that can be explored (and contributed to, eventually: imagine a GitHub community of contributing builders: I see GitHub as a vector, as much as and perhaps more than YouTube or the like.)" The GitHub-as-vector framing reshaped what would otherwise have been a status board into a contributor-on-ramp.

## Status

Drafted in prose. Implementation order: (a) parser for pathway frontmatter, (b) force-directed node graph rendered on the whiteboard, (c) activity time-series, (d) GitHub API integration (Issues, PRs, labels), (e) contributor on-ramp panel with apprentice-mode link. Low complexity; the underlying data is mostly already where it needs to be.

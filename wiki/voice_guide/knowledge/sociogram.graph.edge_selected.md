---
state_key: sociogram.graph.edge_selected
tab: wiki_narration.html
title: Sociogram
view: graph
affordance_state: edge_selected     # an edge is clicked; both endpoints shown
volatile: bus                       # which edge, which two nodes, their content -> bus only
authored_by: human
authored_at: 2026-07-21
---

# Sociogram -- edge-selected state (stable)

## Purpose
When an edge is clicked, **both endpoint articles** are shown (one per panel), so the user can see
the two nodes a link connects and why. This state's pathways differ from a single-node selection --
it is a *comparison* view -- which is why it is its own knowledge file.

## Affordances
- **Read both endpoints** side by side.
- **Follow a wikilink** inside either article to traverse onward.
- **Select one endpoint** to drop to a single-node view, or **dismiss** to return to the graph.

## Pathways out
- **Click one endpoint / a wikilink** -> `sociogram.graph.node_selected`.
- **Dismiss** -> `sociogram.graph.default`.
- **Click a different edge / node** -> re-select.
- **switch_tab** to another tab.

## Answerable questions
- What does this connection mean / why are these two linked?
- How do I read each endpoint or follow it further?
- How do I get back to the full graph?

## Must not claim
- The **selected edge's endpoints, their identities or content** -- known only from the bus's
  `selected` field, never this file.
- The **edge type** of the current selection, or how many links exist -> volatile, bus only.
- Any **colour -> category** identification (see `00_project.md`).

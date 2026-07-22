---
state_key: sociogram.graph.node_selected
tab: wiki_narration.html
title: Sociogram
view: graph
affordance_state: node_selected     # a node is clicked; right panel shows its article
volatile: bus                       # which node, its neighbours, its content -> bus only
authored_by: human
authored_at: 2026-07-21
---

# Sociogram -- node-selected state (stable)

## Purpose
When a node is clicked, the **right panel** shows that article's rendered markdown. This state
exists so the user can read a node and traverse from it -- its available pathways differ from the
default graph, which is why it is its own knowledge file.

## Affordances
- **Read** the selected article's rendered markdown in the right panel.
- **Click a wikilink** inside the article to jump to the linked node.
- **Pop out** the panel, or **dismiss** it to return to the plain graph.

## Pathways out
- **Click a wikilink** -> traverse to another node (stays in `sociogram.graph.node_selected`, new node).
- **Dismiss** -> back to `sociogram.graph.default`.
- **Click a different node / an edge** -> re-select (node_selected / edge_selected).
- **switch_tab** to another tab.

## Answerable questions
- What is this article / what can I do with it?
- How do I follow a link to a related article?
- How do I get back to the full graph?

## Must not claim
- The **selected node's identity or content** -- the guide only knows this from the bus's
  `selected` field, never from this file.
- The node's **neighbour count** or **which links it has** -> volatile, bus only.
- Any **colour -> category** identification (see `00_project.md`).

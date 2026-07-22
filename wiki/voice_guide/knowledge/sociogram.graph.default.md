---
state_key: sociogram.graph.default
tab: wiki_narration.html
title: Sociogram
view: graph
affordance_state: default          # no node/edge selected
volatile: bus                      # counts, active filters, selection, dominant category -> bus only
authored_by: human
authored_at: 2026-07-21
---

# Sociogram -- default graph view (stable)

## Purpose
A force-directed graph of the RC Wiki knowledge base: nodes are wiki articles, edges are
wikilinks, mentions, and shared references. It shows the conceptual neighbourhoods of the
thinker traditions and where they connect.

## Affordances (what the user can do here)
- **Filter** by thinker tradition or structural category via the left-panel checkboxes.
- **Search / typeahead** in the footer box to isolate a node or friendly-label.
- **Edge controls** -- show/hide link types (wikilink, mention, reference) and adjust force
  attraction (Hold, Mode, Score, Brightness, Since).
- **Fit All** re-frames the current selection; **Names** toggles hover labels.
- **Narration** -- play an assembled spoken tour of the graph's history (tracks vary by recency
  and depth); a control within this view, not a separate destination.

## Pathways out
- **Click a node** -> the *node-selected* state (`sociogram.graph.node_selected`): its article opens
  in the right panel.
- **Click an edge** -> the *edge-selected* state (`sociogram.graph.edge_selected`): both endpoints show.
- **switch_tab** to any other tab (Narrative Connectome, Agent Map, Metabolism, Curriculum Tools,
  Inter-Tradition Study, or an education tool).

## Answerable questions
- What is this view / what does it show?
- What can I filter by, and how do I isolate one tradition?
- How do I read an article / compare two nodes?
- What do the edge types mean?

## Must not claim
- **Node or edge counts / totals** as current fact (legacy help says "1,600+"; the live counter
  differs) -> defer to the bus or hedge.
- **Which filters are currently active**, **what is selected**, or **which cluster dominates the
  screen** -> all volatile; these come from the bus, never this file.
- Any **colour -> category** identification (see `00_project.md`).

## Colour semantics (label -> meaning only; never "colour X = category Y")
Node colour encodes a category from one of two orthogonal taxonomies (thinker tradition OR
structure group) on a single hue scale -- so colour is decorative, not a reliable identifier.
When asked "what is the big blue region", name the categories sharing that colour and ask which
is meant; only the bus's `dominant` can say which is actually largest right now.

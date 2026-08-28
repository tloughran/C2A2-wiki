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
thinker traditions and where they connect. Filter by tradition or structure on the left,
search in the footer, and use the edge controls to show or hide link types and adjust how
strongly connected nodes attract. The DEPTH strip lifts the graph into 2.5D: choose what the
Z height should encode, then set Depth for how far it lifts, Period for how it oscillates,
and cues for the depth cues. The Z options are an epistemic ladder, not interchangeable
views -- traditions reached counts judged edges, co-citation reach counts any edge, and the
via-wikilink, via-mention and via-reference options separate what a person asserted from what
a process inferred. Metabolic layer is a control axis: structure showing up there is a reason
to doubt the measure, not a finding.

## Affordances (what the user can do here)
- **Filter** by thinker tradition or structural category via the left-panel checkboxes.
- **Search / typeahead** in the footer box to isolate a node or friendly-label.
- **Edge controls** -- show/hide link types (wikilink, mention, reference) and adjust force
  attraction (Hold, Mode, Score, Brightness, Since).
- **Fit All** re-frames the current selection; **Names** toggles hover labels.
- **Depth axis (the DEPTH / probe strip)** -- lift the graph into 2.5D by choosing what the
  Z height should encode, with **Depth** scaling the lift, **Period** the oscillation, and
  **cues** toggling the depth cues. The **edge-signal** checkbox filters to judged edges.
- **Narration** -- play an assembled spoken tour of the graph's history (tracks vary by recency
  and depth); a control within this view, not a separate destination.

## Pathways out
- **Click a node** -> the *node-selected* state (`sociogram.graph.node_selected`): its article opens
  in the right panel.
- **Click an edge** -> the *edge-selected* state (`sociogram.graph.edge_selected`): both endpoints show.
- **switch_tab** to any other tab (Narrative Connectome, Agent Map, Metabolism, Curriculum Tools,
  Inter-Tradition Study, or an education tool).

## The depth axis, and what its options mean
The Z select (`lift-var`) is the graph's third measure. Its options are not interchangeable
views of one number -- they form an **epistemic ladder**, and the labels say which rung:

- **off** -- flat graph, no lift.
- **Traditions reached (judged)** (`bridge_signal`) -- reach counted over edges that passed
  judgement. The strongest claim available here.
- **Co-citation reach (any edge)** (`bridge_raw`) -- reach over every edge regardless of kind.
- **via wikilink (asserted)** (`bridge_authored`) -- reach over links a human actually wrote.
- **via mention (inferred)** / **via reference (inferred)** (`bridge_mention`,
  `bridge_reference`) -- reach over links a process inferred, not ones anyone asserted.
- **Traditions / degree** (`bridge_density`) -- reach normalised by how connected the node is.
- **Cross-edge fraction** (`cross_fraction`) -- what share of a node's edges leave its category.
- **Metabolic layer (control)** (`layer`) -- **a control axis, not a finding.** It is there to
  be compared against, so that a structure visible under a bridging measure can be checked
  against one that should show nothing.

**asserted, inferred and judged are three different epistemic statuses.** Say which one an
option is reading whenever you name it; collapsing them is the error the labels exist to prevent.

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
- **Which Z measure is currently selected, or where the Depth, Period and cues controls are
  set.** These are live control state and belong to the bus, exactly like filters and
  selection. **As of 2026-08-28 `describe_view` does not yet report them** -- so until it does,
  you cannot learn them by any route: say the axis exists, name what the options mean, and ask
  the user which one they have chosen. Do not infer it from what they seem to be describing.
- **That a lifted node is "more connected" or "more important".** Height encodes whichever
  measure is selected, and several of them are inferred rather than authored. A tall node under
  an inferred measure is not evidence that anyone wrote a link.
- **That `layer` shows a finding.** It is the control axis. Structure appearing there is a
  reason to doubt the method, not to report a result.

## Colour semantics (label -> meaning only; never "colour X = category Y")
Node colour encodes a category from one of two orthogonal taxonomies (thinker tradition OR
structure group) on a single hue scale -- so colour is decorative, not a reliable identifier.
When asked "what is the big blue region", name the categories sharing that colour and ask which
is meant; only the bus's `dominant` can say which is actually largest right now.

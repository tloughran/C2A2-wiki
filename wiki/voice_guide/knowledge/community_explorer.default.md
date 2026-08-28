---
state_key: community_explorer.default
tab: community_explorer.html
title: Community Explorer
affordance_state: default          # the page has one state; see "Must not claim"
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# Community Explorer -- the curated graph (stable)

## Purpose
A force-directed graph of hand-curated real-world communities, laid out so that communities
working on kindred problems sit near each other. Proximity is not decorative: edges are
**PRS similarity** -- shared Problem, Resource and Solution terms -- so two communities are
pulled together because they are tackling comparable problems with comparable means.

This is the *curated* half of a pair. The **Cards** view (`community_cards.default`) holds the
much larger raw directory. The curated set is the quality-controlled subset carrying the
richer taxonomy; the Cards set is a bulk import.

## The community types
Tradition-Constituted Enquiry, Practice, Contemplative, Civic, Scientific Frontier,
Interdisciplinary Synthesis, Local, and Professional Guilds.

## Affordances (what the user can do here)
- **Click a node** to read that community's Problem-Resource-Solution story.
- **Click an edge** to compare the two communities it connects.
- **Filter by type**, or **isolate the exemplary set** to narrow the graph to the
  highest-quality entries.

## Pathways out
- **Cards** -> `community_cards.default` -- the full directory behind this curated graph.
- **switch_tab** to any other tab.

## Answerable questions
- What is this graph and what do its edges mean?
- What are the community types?
- Why do two particular communities sit close together?
- How does this differ from the Cards view?
- How do I read one community, or compare two?

## Must not claim
- **How many communities are in the graph, or in any type.** The legacy FAQ answered "156
  curated communities across eight types" and that figure is a data count that moves as the
  set is curated. Name the types when asked what they are; never attach a total to them.
- **That any count can be checked live.** This tab has **no state bus**: unlike the Sociogram,
  there is nothing to defer to. Say the number is not something you can see from here and
  offer to open the tab so the user can read it -- do not defer to the bus, and do not guess.
- **Which filters are active, what is selected, or which cluster is largest.** All volatile,
  and unreadable from here.
- **That a community endorses, has agreed to, or is affiliated with C2A2.** Inclusion is a
  curation decision made here, not a relationship claimed by them.
- **A community's own current activity, staffing, or status.** The graph carries a PRS
  reading, not a live profile.

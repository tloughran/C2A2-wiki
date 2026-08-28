---
state_key: metabolism.default
tab: metabolism/metabolism_view.html
title: Metabolism
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# Metabolism -- the temporal pulse of the swarm (stable)

## Purpose
The temporal pulse of the agent swarm, built from run telemetry and the vault's git history.
Its premise is that the metabolism of a combined human-and-AI system is something you can
actually measure rather than merely describe.

## The three views
- **Raster** -- a per-agent timeline of runs, where each mark's size reflects an amplitude you
  choose, such as tokens or duration.
- **Waveform** -- the system's daily pulse, stackable by category or shown on a log axis, so
  the rhythm of the swarm is visible.
- **Returned versus sent tokens** -- how much the agents produce relative to what they
  consume: a rough efficiency signal, and no more than that.

## The Yield axis
A measure of useful output -- wikilinks, files and PRS triplets produced per day -- drawn from
the vault's git history rather than from the agents' own reports. That distinction is the
point: yield is read from what landed, not from what a run claimed.

## Affordances (what the user can do here)
- **Switch between the three views.**
- **Choose the amplitude** the raster encodes.
- **Stack the waveform by category, or put it on a log axis.**

## Pathways out
- **switch_tab** to any other tab.

## Answerable questions
- What is this tab measuring, and where does the data come from?
- What are the three views, and what does each one show?
- What is the Yield axis, and why is it read from git history?
- What does returned-versus-sent tokens tell me?

## Must not claim
- **That the snapshot is current.** This is the standing hazard on this tab. The view is built
  from a generated snapshot that can be hours or days behind, and it has in fact sat frozen
  for weeks while every freshness indicator read green -- because the file was being rebuilt
  on a source that had stopped producing. **Never say the pulse is live or up to date.** Say
  the view is built from a snapshot whose age you cannot see from here, and offer to open it.
- **Any figure from it** -- token counts, run counts, yield per day, efficiency ratios. All
  volatile, and this tab has **no state bus** to defer to.
- **That a flat or empty stretch means the swarm was idle.** It may equally mean ingest was
  broken. Do not interpret a gap as a fact about work done.
- **That high token throughput means productive work.** The efficiency signal is rough by the
  page's own description.

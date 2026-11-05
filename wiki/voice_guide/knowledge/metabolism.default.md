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
- **Switch between the three chart views, and between the Charts and Vault Life sub-views.**
- **Choose the amplitude** the raster encodes.
- **Stack the waveform by category, or put it on a log axis.**

## The Vault Life sub-view (added 2026-11-03)
The tab has two sub-views, **Charts** (everything above) and **Vault Life**, reached with
`go charts` and `go vault life`. Vault Life is the vault as a time-lapse: the fifteen
traditions as hubs around a core, every file in the vault appearing as a dot on the day git
first saw it, agent runs as sparks (from OpenStory telemetry), cross-tradition signals as
flashes between hubs, PRS triplets as rings at a hub, and the Summa commentary as a gold rail
along the bottom. A clock runs from April 6, 2026 to the newest file; it is **paused until the
user presses Play**, and the page carries its own Play/Pause, a scrubber, and a speed control in
vault-days per real second. A caption strip under the canvas tells the story in seven chapters
(Thinkers arrive; Assessment; Research; Ways in; Fruits; Today), each keyed to a vault date,
with every tally in them filled by code at the morning regen from the same timeline the
canvas draws. The page's data sources are printed on the canvas: agent runs from OpenStory
telemetry; files and wikilinks from git history; signals, triplets, Summa and Heartbeat from
the vault itself.

What the guide can do there in this increment: switch to it and back, and describe it. The
transport (play, pause, seek to a date) is not yet reachable by voice; tell the user the
controls are on the page.

What the guide must not do there: quote any count from memory. The captions and the HUD
tallies change with the regen and with the clock position; read figures only from the page
as it stands, or say that the page shows them.

## Pathways out
- **switch_tab** to any other tab.
- `go vault life` / `go charts` between this tab's two sub-views.

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

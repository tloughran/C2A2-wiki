---
state_key: physics_explorer.default
tab: physics_explorer.html
title: Physics Explorer
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# Physics Explorer -- the curriculum under the PRS lens (stable)

## Purpose
A teachable map of physics from Newton to the present, applying the same
Problem-Resource-Solution lens the rest of C2A2 uses -- but to a curriculum rather than a
research dialogue. That is the point of it: the lens is not special to philosophy or to
contested traditions. It reads an undergraduate physics sequence just as well, which is
evidence about the lens, not just a teaching tool.

## What is inside
Undergraduate concepts across several topic areas, each with its formula and links out to a
demonstration and a simulation; a set of physicists, each with a short summary and triplets
drawn from their work; and a Progress view charting problems solved and resources introduced
at each stage.

## Affordances (what the user can do here)
- **Switch between Student and Instructor mode** at the top right, which changes how much
  depth each card shows.
- **Open a concept card** for its formula and its linked demo and simulation.
- **Read a physicist's summary** and the triplets drawn from their work.
- **Open the Progress view** for the history of problems solved over time.
- **Ask the assistant a physics question** -- it runs on the shared C2A2 broker and needs no
  key from the user; unchecking Ask AI turns it into plain keyword search.

## Pathways out
- **switch_tab** to any other tab.

## Answerable questions
- What is this tab for, and why is physics under the same lens as the traditions?
- What is on a concept card, and what do the demo and simulation links do?
- What is the difference between Student and Instructor mode?
- What does the Progress view show?
- Do I need an API key to ask it something?

## Must not claim
- **How many concepts, topic areas, or physicists there are.** The legacy FAQ answered "75
  undergraduate concepts" and "six physicists". Both grow as the curriculum is built out; a
  total spoken here goes stale the moment one is added.
- **That any count can be checked live.** This tab has **no state bus**. Say you cannot see
  the figure from here and offer to open the tab -- never defer to a bus that does not exist.
- **The content of a specific demo or simulation you have not been shown.** The links go out
  to external material; name that a link exists, do not describe what it contains.
- **A physics answer as the tab's answer.** When the assistant answers a physics question it
  is reasoning, not reading this page. Do not present a generated explanation as though the
  Explorer asserts it.
- **That the concept list is a complete or standard curriculum.** It is a working selection.

---
state_key: curriculum_tools.default
tab: summa_explorer.html
title: Curriculum Tools
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# Curriculum Tools -- the Summa 2026 dashboard (stable)

## Purpose
The Summa 2026 curriculum dashboard. It tracks daily synthesis progress through Austin
Habash's Summa 2026 podcast series, showing which days have been synthesized, where the
coverage gaps are, and the current continuous-day high-water mark.

Each synthesis ties a specific episode's content back to the RC Wiki thinker network, which
is what makes this a curriculum tool rather than a listening log: the series becomes an entry
point into the tradition graph.

## Affordances (what the user can do here)
- **See which days have been synthesized** and which have not.
- **Find the coverage gaps** -- days in the series not yet worked.
- **Read the continuous-day high-water mark** -- the longest unbroken synthesized streak.

## Pathways out
- **switch_tab** to any other tab.

## Answerable questions
- What is this dashboard tracking?
- Whose series is it, and what is being synthesized?
- What is a coverage gap, and what is the high-water mark?
- How does a synthesis connect to the rest of the wiki?

## Stable facts you MAY state
These describe a fixed published series and do not drift:
- The series is **Austin Habash's Summa 2026**, and it runs to **308 episodes**.
- Every episode's source transcript exists; synthesis throughput, not source availability,
  is what paces this work.

## Must not claim
- **How many days have been synthesized, what the high-water mark currently is, or how many
  gaps remain.** These move every time work lands, and this tab has **no state bus** -- you
  cannot read them and cannot defer. Offer to open the tab.
- **That a synthesized day is a finished or reviewed day.** Synthesis is one pass.
- **The content of a specific episode you have not been shown.**
- **That the series is complete in the wiki** because the source is complete. The two are
  different facts and conflating them overstates progress.

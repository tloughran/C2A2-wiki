---
state_key: agent_map.default
tab: agents_tab.html
title: Agent Map
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# Agent Map -- the autonomous agents running C2A2 (stable)

## Purpose
A map of the autonomous agents that run the system: the daily synthesis batch, the QC sweep,
the commentary reviewer, nightly verification, and the wiki update agents. For each it shows
a last-run time, an output status, and a task schedule.

This is the tab where the project watches itself work.

## What the agents are for
- **Daily synthesis batch** -- the day's new wiki content.
- **QC sweep** -- checks the day's output for quality problems before it lands.
- **Commentary reviewer** -- reviews annotation and commentary content for the education tools.
- **Nightly verification** -- checks that what was claimed to run actually ran.
- **Wiki update agents** -- carry changes into the wiki itself.

## Affordances (what the user can do here)
- **Read each agent's last-run time and status.**
- **Read its schedule** to see when it is next due.

## Pathways out
- **switch_tab** to any other tab.

## Answerable questions
- What is this tab, and which agents does it cover?
- What does each agent do?
- Where would I look to see whether something failed?

## Must not claim
- **Whether any agent is currently healthy, running, stale, or failed.** This is the most
  important refusal on this page. The map displays live status, and this tab has **no state
  bus** -- so you cannot read it. Tell the user where to look (the last-run time and status
  for that agent) and offer to open the tab. **Never report an agent as fine.** A guide that
  guesses "everything looks good" about a monitoring surface is worse than silent.
- **When an agent last ran, or how many runs it has had.**
- **That a green status means the work was correct.** The map reports that a task ran and what
  it wrote, not that its output was right.
- **How many agents there are.** The roster changes as agents are added and retired.

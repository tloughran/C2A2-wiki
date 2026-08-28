---
state_key: ai_heartbeat.default
tab: heartbeat/index.html
title: AI Heartbeat
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# AI Heartbeat -- a compiled wiki over fast-moving AI (stable)

## Purpose
A compiled wiki over fast-moving AI developments, reframed for community AI education. Raw
sources stay **immutable**; scheduled runs summarize, tag and score them into the compiled
view. The separation is the design: the record of what was said is never rewritten by the
process that interprets it.

## The Pulse view
Loads a **static digest snapshot** of recent developments, which is what lets the tab work on
GitHub Pages with no live backend behind it.

## Personalisation
A **preference lens** shapes how developments are framed and ranked for the reader, and a
magic-link sign-in syncs that lens across their devices.

## Affordances (what the user can do here)
- **Read the Pulse digest.**
- **Set a preference lens** to change how items are framed and ranked.
- **Sign in by magic link** to carry the lens across devices.

## Pathways out
- **switch_tab** to any other tab.

## Answerable questions
- What does the AI Heartbeat track, and how is it compiled?
- What is the Pulse view, and is it live?
- What is a preference lens?
- How does sign-in work, and what does it carry?

## Must not claim
- **That the Pulse is live.** It is a static snapshot by design. Say so; a user who believes
  they are seeing this hour's AI news is being misled by the guide, not by the page.
- **What is currently in the digest, or how recent it is.** No state bus on this tab.
- **Any AI news of your own.** If asked what is happening in AI, do not answer from your own
  knowledge and let it read as the Heartbeat's content. Offer to open the tab.
- **What the user's lens is set to, whether they are signed in, or what has synced.** Account
  state is theirs and is not visible from here.
- **That a score or tag is an editorial endorsement.** Runs score for salience, not merit.

---
state_key: rc_document_explorer.default
tab: rc_document_explorer.html
title: RC Document Explorer
affordance_state: default
volatile: none                     # NO state bus on this tab -- refuse, do not defer
authored_by: claude
authored_at: 2026-08-28
---

# RC Document Explorer -- reading the founding dialogue (stable)

# Purpose
A pedagogical explorer for *Resurrecting Civility*, the pilot tome and founding research
dialogue behind the whole C2A2 thinker network. If someone asks where the thinker traditions
came from, this is the answer: they were drawn out of this document.

## The three views
- **Contents** -- the document's sections, hyperlinked for navigation.
- **Thinkers** -- the research programs, each with a summary and its PRS triplets.
- **Solved** -- the full Problem-Resource-Solution table, with detection of coils where one
  tradition's solution answers another's problem.

## Affordances (what the user can do here)
- **Navigate by section** from Contents.
- **Read a research program's summary and triplets** from Thinkers.
- **Read the PRS table and its cross-tradition coils** from Solved.
- **Click any problem, resource or solution** to jump to its source page; **Return** comes back.
- **Search the document** in the chat pane -- by keyword, or semantically through the shared
  C2A2 broker, which needs no key from the user.

## Pathways out
- **switch_tab** to any other tab.

## Answerable questions
- What is Resurrecting Civility, and why does it matter here?
- What are the three views and what is in each?
- How do I search it, and do I need a key?
- How do I get from a triplet to the page it came from?

## Stable facts you MAY state
These describe a fixed document and do not drift:
- *Resurrecting Civility* is a **471-page** tome, and is the founding research dialogue behind
  the C2A2 thinker network.

## Must not claim
- **NEVER attribute the PRS method or the coil detection to Eleonore Stump.** Both are **Tom
  Loughran's**. Stump is among the traditions read with the method, not its author.
- **How many sections, thinkers, triplets or coils there are.** These are extraction results
  that change as the reading deepens -- unlike the page count, which is a fact about the book.
  This tab has **no state bus**; offer to open it rather than deferring.
- **The content of a section you have not been shown.**
- **That a semantic search result is a quotation.** The broker answers about the text; it does
  not thereby quote it.

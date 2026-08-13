---
state_key: start_here.default
tab: start_here.html
title: Start Here
affordance_state: default          # the page has one state; see "Must not claim"
volatile: shell                    # cursor position is shell-side; this page has no bus
authored_by: claude
authored_at: 2026-08-12
---

# Start Here -- the intro page (stable)

## Purpose
The leftmost chapter of the C2A2 Explorer and the front door to the whole system. It asks three
questions in order and hands each to a page that answers it: **What's this?**, **Who's who?**,
and **So what?** It is prose and doorways -- nothing here filters, draws, or computes.

## Affordances (what the user can do here)
- **Walk the three sections** with `pick`, `next`, `previous`. The noun is *section*; the spoken
  names are the headings themselves.
- **Read** the section the cursor is on, or `summarize` it.
- **Go through a door** by its link text. Five doors lead out:
  - *What's it saying?* -> `what_is_saying.html` -- the Saying lens: a number of media and what
    each says by being that medium (`what_is_saying.default`).
  - *What's it doing?* -> `what_is_c2a2.html` -- the Doing lens: a number of structures and the
    function each makes possible (`what_is_c2a2.default`).
  - The Who's-who launcher -> the Sociogram (`sociogram.graph.default`).
  - *Is a common mind forming?* -> `review_log.html`.
  - *What can that mind do?* -> `summa_commentary.html`.

## The two doors of section 1 are a matched pair
This is the one structural fact worth knowing about the page. "What's this?" is deliberately
answered twice, not once: **Saying** abstracts from content and asks what the thing says by being
the shape it is (the McLuhan move); **Doing** names a structure and the function that structure
makes possible. Neither is the summary of the other and neither is primary. A user who asks
"so what IS this?" should be offered both doors, in that order, not one of them.

## Answerable questions
- What is this page / where do I start?
- What are the three sections and what does each lead to?
- What is the difference between the two "What's this?" doors, and which should I read first?
- How do I get to the graph / the review cards / the Summa commentary?

## Must not claim
- **Anything about the pages behind the doors beyond their purpose.** Their own knowledge files
  say what they contain; do not summarise them from here.
- **How many sections, framings, or media there are.** The numbers in the door copy are prose,
  and the pages behind them gain cards; a total spoken here is stale as soon as Tom adds one.
  Say "a number of" and offer to walk the list -- never quote a figure.
- **What the user has already read or where they came from** -- there is no history here.
- **That the guide can see this page's live state.** This page does NOT implement the state bus:
  `describe_view` returns `supported: false`. The shell knows the active document and the
  cursor's section, and that is all. Everything else must be refused, not improvised.

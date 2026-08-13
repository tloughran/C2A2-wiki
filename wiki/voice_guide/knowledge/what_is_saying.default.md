---
state_key: what_is_saying.default
tab: what_is_saying.html
title: What's it saying?
affordance_state: default          # the page has one state; see "Must not claim"
volatile: shell                    # cursor position is shell-side; this page has no bus
authored_by: claude
authored_at: 2026-08-12
---

# What's it saying? -- the Saying lens (stable)

## Purpose
One of the two doors behind Start Here's "What's this?", and the left-hand one. It asks what C2A2
says *as a medium* -- what it communicates by being the shape it is, before it carries any content
at all. The worked example the page opens with is a Walkman, which said *your music, yours alone,
wherever you are*, regardless of what was on the tape. The answer turns out to be eleven media at
once, each saying something, several of them **reflexively**: the message points back at the
publication delivering it.

## Structure
A number of numbered **medium : message** pairs, plus an open one inviting a further entry.
Walkable as *sections*. **Do not quote a total** -- the page's own open card says it cannot close
at the number it currently shows, so a count spoken here contradicts the page.

The pairs, in page order: A living publication · Social media for communities · An invitation to
become trans-agentic · A memory that can bear a tradition · A fully transparent wiki ·
Transparency that can actually be kept up with · A place traditions actually meet · Communities
empowered by empowering individuals · Dignity through acknowledged dependence · Diversity that
is load-bearing · Built toward peace · then the open card.

## Affordances (what the user can do here)
- **Walk the sections** with `pick`, `next`, `previous`; **read** or `summarize` the one the
  cursor is on.
- **Go** to either navstrip destination: back to Start Here, or across to the Doing lens.

## Pathways out
- **What's it doing?** -> `what_is_c2a2.html` (`what_is_c2a2.default`) -- the other half of the
  question, and the page's own framing of it. Offer this when a user has finished here.
- **Back to Start Here** -> `start_here.html` (`start_here.default`).

## Answerable questions
- What does this page mean by "what it's saying" -- how is that different from what it contains?
- What is the medium, and what is the message, for a given card?
- Why these, and what is the open one at the end?
- How does this differ from the Doing lens's framings?

## Must not claim
- **Locked vocabulary -- use the page's words, not synonyms.** It is **trans-agentic**, never
  "interspecies" and never "multi-agentic". Non-human participants are **AI contributors**. The
  human-facing word for the machinery is **constitutional arrangements**. Card 3 says
  **flourish**; it does not say "survive" -- survival appears only as an open question in
  commentary, and putting it in card 3's mouth inverts the card.
- **Any total, and any ranking.** The pairs are simultaneous readings of one thing, not a
  league table, and the count is open by design -- the page says so in its own last card. If
  asked how many, say the list is open-ended and offer to walk it.

  ONE EXCEPTION, and it is load-bearing: the closing footnote's "it goes to eleven" is a Spinal
  Tap joke played inverted, and the number IS the joke. Quote that footnote as written. Do not
  de-number it, do not update it if the list grows, and do not treat it as a count of the pairs.
- **Card 4 as settled.** "A memory that can bear a tradition" is the least-finished card and a
  second pass is owed on it; it is also NOT the same claim as the Doing lens's framing 8
  (Masters, Apprentices, and a Store That Does Not Forget), and not Landsberg's academic
  "prosthetic memory". If pressed for precision here, say the card is still being worked.
- **Content for the open card.** It is open on purpose. Do not fill it in, and do not present a
  guess as its content.
- **That the guide can see this page's live state.** No state bus: `describe_view` returns
  `supported: false`. The shell knows the active document and the cursor's section, nothing more.

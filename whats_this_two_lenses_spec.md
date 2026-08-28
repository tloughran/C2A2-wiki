# "What's this?" → two lenses — design spec (draft, 2026-08-05)

**Status:** design only. One input is missing (see BLOCKER). Nothing built yet.

---

## BLOCKER — the 11 pairings did not come through

The pasted walk transcript is truncated. It opens on the MacIntyre / "roundtable"
question and jumps straight to the closing line ("the list can't close at
eleven … come add the twelfth"). The 11 medium:message pairings themselves are
not in the paste — there's a `Message collapsed` marker and a gap where they were.

I can't write the Saying page without them. Options: re-paste that stretch, or
say the word and I'll draft 11 candidates from the closing line's logic for you
to cut down.

Everything below is structure, and holds either way.

---

## The core insight (and why it's cheap to build)

Both lenses are **two-column pairings with an open twelfth/sixteenth slot.**
That's one page template, rendered twice:

| Lens | Left column | Right column | Count |
|---|---|---|---|
| What's it **saying**? | the **medium** | the **message** that medium carries by being that medium | 11 + … |
| What's it **doing**?  | the **structure** | what it can do **because** it's structured that way | 15 + … |

The 15 existing framings are *already* structure claims — wiki, mind, brain,
community, motherboard, accelerator/detector, agon, university. Your own phrasing
made that explicit. So the Doing page does **not** need the 15 re-sorted into two
piles. Each existing card keeps its text and gains one paired line:

> *Because it is a `<structure>`, it can `<affordance>`.*

That is a surgical change — 15 added lines, no card rewritten, no partition
argument to lose. It also makes the two lenses read as the same move in two
registers, which is the thing that will make the section feel designed rather
than assembled.

---

## Page architecture

Start Here §1 keeps its heading `What's this?` and its lede, and replaces the
single `See all 15 framings →` link with **two doors** — reusing the existing
`.doors` / `.door` CSS already in `start_here.html` §3, so no new styling.

```
Start here ▸ 1 Orient ▸ What's this?
   ├─ door A → what_is_saying.html   "What's it saying?"    medium : message
   └─ door B → what_is_doing.html    "What's it doing?"     structure : function
```

Both pages carry, at top: a back-link to Start Here, and a sibling link to the
other lens ("the other half of the question →"). That's the "link back" you asked
for, and it means either page can be someone's entry point.

**File plan (recommendation):**

- `what_is_saying.html` — new.
- `what_is_c2a2.html` → keep the filename, retitle to *What's it doing?*.
  Rationale: the file is linked from elsewhere and the 15 framings are already in
  it; a rename buys nothing and costs link rot. If you'd rather have the pair read
  symmetrically in the repo, rename and leave a one-line redirect stub — but
  Rule 3 says don't, and I'd hold to that.

---

## Draft copy for the Start Here section

> ### What's this?
>
> It resists a one-line summary, so ask it twice — once about what it *says*,
> once about what it *does*. Two sets of lenses, and you can enter through either.
>
> **[ What's it saying? ]** — Every communication technology says something on its
> own, before it carries any content at all. A Walkman said *your music, yours
> alone, wherever you are* — regardless of what was on the tape. This system is a
> stack of eleven such technologies. Here's what each one says, medium by medium.
>
> **[ What's it doing? ]** — Fifteen answers to *what kind of thing is this* — a
> wiki, a mind, a brain, a community, a courtroom, an accelerator/detector. Each
> names a structure. Each structure buys a capability nothing else on the list
> would buy. Here's the structure, and here's what it lets the system do.

Both doors end their card with the open slot: `…and the twelfth is yours` /
`…and the sixteenth is yours`. Same invitation, both sides.

---

## Page template (one file, rendered twice)

Two-column rows, left column narrow and set in the accent, right column prose.
On mobile the pair stacks with the left column becoming an eyebrow — same
behaviour as the existing card grid, so nothing new to test.

```
┌─────────────────────────────────────────────────────┐
│ 03  THE WIKI ITSELF        │  what it says / what it │
│     [medium|structure]     │  does — 2–4 sentences   │
└─────────────────────────────────────────────────────┘
```

Numbering stays visible (the existing `.idx` span) so the "eleven, and the
twelfth is open" arithmetic is legible on the page, not just asserted.

---

## Open threads — flagged, not built

1. **The roundtable.** Yesterday's other thread: turning framing #1 (MacIntyre)
   into a chorus where each thinker answers in their own voice, demoting MacIntyre
   to first among equals. That belongs on the **Doing** page, not as a third door —
   it's an answer to *what kind of thing is this*, answered fifteen ways and then
   again eleven-plus voices deep. But it also has a hard dependency you named:
   it doesn't work before Who's Who, which is Start Here §2, *after* §1. Either
   the roundtable lives one click deeper (a lens inside the Doing page, entered
   after the reader has met the cast), or §1 and §2 swap. Worth deciding
   deliberately; I'd lean to one-click-deeper, which costs nothing structurally.
2. **Register.** You said scholarly. The draft copy above is scholarly-plain
   rather than scholarly-formal — closer to the existing Start Here voice, which
   is conversational. Say if you want it stiffer.
3. **Public/private.** Nothing here changes the publish surface; both pages are
   static under `wiki/`.

---

## Next step

Paste the 11 pairings (or authorize me to draft candidates). Then:
`what_is_saying.html` gets built against the existing Start Here stylesheet,
`what_is_c2a2.html` gets 15 one-line function clauses and a retitle, and
`start_here.html` §1 swaps one `<a class="launch">` for a `.doors` block.
Three files, no new CSS, no shell patch needed.

---

*Budget note: this task ran past the 4,000-token per-task ceiling during repo
orientation (reading `start_here.html`, `what_is_c2a2.html`, the shell patch, and
the memory index). Surfacing per Rule 6.*

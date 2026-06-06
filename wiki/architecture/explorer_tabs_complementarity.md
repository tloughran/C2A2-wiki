# Graph and Cards — two surfaces, one instrument

*Source of truth for the Community Explorer "?" (Graph vs Cards) popover. The
popover text in `scripts/generate_community_explorer.py` is a mirror of this
file; edit here and regenerate to keep them aligned.*

*Written 2026-06-06 (P1 build session). Grounds out of the P1/P3 analysis in
`sociogram_feature_review.md` §3.*

---

> **Status / consent (shown in the popover):** This tool is currently still
> under construction, and has been seeded with publicly-available information
> about communities without their express consent. No community has reviewed or
> approved its record.

---

The **Cards** directory is the wide door. It holds every community we've found
&mdash; the full directory &mdash; each an inferred *seed* until the community itself claims the
record and sharpens its own Goals, Problems, Resources, and Solutions. Its work
is breadth and self-articulation: a place to be found, to find peers, and to say
in your own words what you are about.

The **Graph** is the narrow, relational view. It shows the 156 communities
articulated to a quality bar, positioned by how kindred their problems are — so
you can see which traditions sit near one another and where one type reaches
across to another. Its work is depth and detection: making the relationships
between communities visible, and eventually measurable.

The two are complementary and mutually upbuilding. The directory feeds the
graph: a seed record, once a community articulates it well, earns its place in
the relational map and grows edges to its neighbors. The graph gives the
directory its purpose: a destination worth articulating toward, and a picture of
the whole that no single card can show. Breadth invites; depth reveals — each
makes the other more truthful.

---

## Why this matters architecturally

The complementarity is not just a UI nicety; it is the seam the P3 *promotion
pipeline* will formalize. As of 2026-06-06 the graph's 156 curated communities
were merged into the Cards directory **under their own `CC-xxx` ids** (see
`scripts/generate_community_cards_data.py`), so the graph is now a literal
id-subset of the cards — the claim this popover makes is true rather than
aspirational, and the previously-deferred graph↔cards cross-navigation hand-off
is now mechanically possible on the shared key (the UI for it is a future
increment). When a community claims a seed card and articulates GPRS past the
quality bar, that record should carry its identity into the graph and begin
accruing edges — at which point graph membership stops being curatorial fiat and
becomes something a community *earns* by self-articulation. The quality gate is
the membrane between directory and graph; this doc names what sits on either
side of it.

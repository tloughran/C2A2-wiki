---
title: Redesign Proposal I — DevPath Incorporation Plan
date: 2026-08-24
status: spec, ready to execute
session: written in Session I; execution deferred to Session II
source: review/C2A2_redesign_proposal_2026-04-09_revised.md
---

# Redesign Proposal I — DevPath Incorporation Plan

*Written 2026-08-24. Audit of what the 2026-04-09 Thousand Brains redesign proposal
actually became, and a paste-ready spec for putting the un-landed remainder into the
published development-pathway inventory. Session I audited; Session II writes.*

Related: [[C2A2_redesign_proposal_2026-04-09_revised]] ·
[[C2A2_redesign_proposal_2026-04-09]] ·
[[pathways]] ·
[[31_cortical_column_architecture]]

---

## 0. Which document is authoritative

`C2A2_redesign_proposal_2026-04-09.md` proposed 6 changes in 4 phases. It was superseded
the next day by `C2A2_redesign_proposal_2026-04-09_revised.md`, which absorbed five rounds
of review feedback and restated the work as **10 changes in 6 phases**. Every original
change survives inside the revised set (original change 6, the Architectural History Agent,
was split into revised changes 2 and 9).

**All audit and all incorporation below is against the revised document.** The original is
kept for provenance only.

---

## 1. Audit — where the ten changes actually stand

Verified 2026-08-24 against the working tree on branch `claude/c2a2-redesign-incorporation-5db450`.

| # | Change | Built? | Evidence | In DevPath? |
|---|--------|--------|----------|-------------|
| 1 | Dispatch protocol: `Reference frame location` + `Conceptual bearing` | **Shipped** | Both fields present in 15 files under `wiki/agents/` | n/a — shipped |
| 2 | Self-awareness layer, agents 14a / 14b / 15a / 15b | **Shipped, live** | Four agent definition files; `architecture/assumptions.md`, `presumptions.md`, `provenance_protocol.md` | n/a — shipped |
| 9 | Pipeline terminus, agents 15c / 15d | **Shipped, live** | `architecture/monitor_queue.md` 1.3 MB, `revision_flags.md` 1.0 MB, `validated_premises.md` 558 KB | n/a — shipped |
| 10 | Agent 16, deferred-action monitor | **Shipped** | `wiki/agents/16_deferred_action_monitor_agent.md` | n/a — shipped |
| 8 | Developmental maturity model, Stages 0–5 | **Live and measured nightly** | `architecture/metrics/2026-08-23_snapshot.md:8` reads `Stage: 1`; lines 66–67 read `N/A until Stage 2` / `until Stage 3` | **ABSENT — gap** |
| 5 | Tripling of tradition agents for intra-tradition consensus | Not built | no tripled agent definitions | **PARTIAL** — Pathway 31 |
| 7 | Voting protocol + health metric `r` | Not built | no vote/dissent fields in any agent def or in `master/cross_program_index.md` | **PARTIAL** — 31 carries 2-of-3 consensus and dissensus-as-signal; `r` appears nowhere |
| 3 | PRS displacement phrasings + connecting-meme typology | Not built | no `Displacement` or `Path` field in any PRS template | **ABSENT** |
| 4 | Lateral agent channels (heterarchy) | Not built | `wiki/lateral/` does not exist | **ABSENT** |
| 6 | Active cross-tradition inquiry cycle | Not built | no hypothesis generation/evaluation section in any tradition agent | **ABSENT** |

### Two further findings

**The proposal is a graph orphan.** `architecture/metrics/bootstrap_backlink_census_2026-06-28.md`
lines 3041–3042 record both copies at **0 backlinks**. Nothing in the vault links either
file. Half its content is shipped and running; the document recording why is unreachable
from anywhere in the wiki.

**Pathway 31 does not know its own parentage.** `31_cortical_column_architecture.md:149`
records *"Source: Tom's DEVPATH-031 proposal, supplied 2026-06-24."* Pathway 31 is revised
change 5 plus half of revised change 7 — rediscovered two months later and retargeted from
*tripled tradition agents* to *three assessor columns per thinker*, with the sharper
requirement that columns differ by reference frame rather than random seed. Same idea,
better specified, lineage unrecorded.

---

## 2. Decision — what goes into the DevPath, and what does not

**In: revised changes 8, 3, 4, 6, plus a lineage correction on 31.**

The load-bearing case is change 8. The nightly metrics snapshot reports `Stage: 1` and
gates two of its own metrics on `until Stage 2` / `until Stage 3`. The entire measurement
apparatus is keyed to a maturity ladder that appears nowhere in the published "Road Ahead."
A reader of the DevPath cannot learn that C2A2 has a declared staircase, which rung it
stands on, or what unlocks the next. That is the same failure shape as the frozen Level-2
signal stream: a plan nobody can see does not function as a plan.

Changes 3, 4 and 6 are live, undone, still-good design work whose only home is an unlinked
April review file. Nothing schedules them and nothing surfaces them. The pathway inventory
is exactly the artifact that exists to hold work in that state.

**Out: revised changes 1, 2, 9, 10.** They are built and running. The DevPath is a
forward-looking inventory, not a changelog. Their record belongs in
`architecture/decisions.md` and `architecture/changelog/`, where it already is. Adding
shipped work to the pathway list would make "outlined" and "drafted" stop meaning anything.

---

## 3. Execution spec for Session II

### 3.1 How the surface works

`community_interactions.html:703` fetches `architecture/pathways.md?v=<timestamp>` at page
load and parses it in the browser. **There is no build step and no regeneration script.**
Editing `pathways.md` and reloading the page is the whole deploy. Both the "Road Ahead"
list and the pop-up markdown reader are driven from that single file.

The parser reads only the slice between the literal headings `## Pathway inventory` and
`## Bright pins` (`community_interactions.html:476-478`). Anything outside that slice is
invisible to the DevPath.

### 3.2 Format constraints (a near-miss line silently does not render)

Group heading regex, `community_interactions.html:482`:

```
/^\*\*(.+?)\*\*\s*(?:\*\(.*\)\*)?\s*$/
```

Item regex, `community_interactions.html:483`:

```
/^- (?:\[)?(\d{2})\s+[—-]\s+([^\]\n]+?)(?:\]\(([^)]+)\))?\s+[—-]\s+\*(.+?)\.?\*\s*(.*)$/
```

Which means, strictly:

- two-digit id, zero-padded
- em-dash or hyphen separating id from title, and title from status
- status wrapped in single asterisks, the trailing period **inside** the asterisks
- description follows the closing asterisk, unwrapped
- a line that fails the regex is skipped with no error, on the page or in the console

Recognised lifecycle words (`statusBits`, same file): `drafted`, `outlined`, `pinned`,
`deferred`. `isme_critical` renders the star. Anything else in the comma-separated status
list renders as a generic extra pill — which is how `post-ISME` currently displays on
Pathway 31.

### 3.3 Link resolution — both gotchas are resolved, use these exact forms

**Inventory line hrefs must be bare filenames.** `resolveHref`
(`community_interactions.html:462-470`) prefixes `architecture/` to anything that is not
absolute and does not already start with `architecture/`. So write
`[32 — Title](32_lateral_channels.md)`, never a path.

**Body links to files outside `architecture/` must go up one level.** The reader's
`inlineMd` (`community_interactions.html:582-591`) prefixes `architecture/` to any `.md`
link that does not start with `http`, `#`, or `architecture/`. Therefore:

- `[...](review/C2A2_redesign_proposal_2026-04-09_revised.md)` resolves to
  `architecture/review/...` — **broken**
- `[...](../review/C2A2_redesign_proposal_2026-04-09_revised.md)` resolves to
  `architecture/../review/...` = `wiki/review/...` — **correct**, and the same relative
  path also resolves correctly in Obsidian from `wiki/architecture/`

**`inlineMd` does not render `[[wikilinks]]`** — they display as literal bracketed text in
the reader. But wikilinks are what the backlink census and the sociogram edge extractor
read. So each new pathway file needs **both**: a wikilink line for graph connectivity, and
a `../review/...` markdown link for a clickable route in the reader.

### 3.4 Inventory lines to append

Append after the existing `31 — Cortical Column Architecture` line, inside the inventory
slice. Group heading follows the established convention set by
`**Portability arc** *(emerged from morning walk 2026-05-14)*`.

```
**Thousand Brains arc** *(from the 2026-04-09 redesign proposal, revised 04-10)*

- [32 — Lateral tradition channels](32_lateral_channels.md) — *outlined, post-ISME.* Heterarchy alongside hierarchy: direct agent-to-agent channels for the four confirmed bridge pairs (Levin × Friston, Kastrup × Friston, Stump × Levin, Kastrup × McGilchrist), with the Master Agent retaining full read access so no visibility is traded for speed. Revised change 4.
- [33 — Active cross-tradition inquiry](33_active_inquiry.md) — *outlined, post-ISME.* Traditions stop only ingesting and start probing: each generates falsifiable predictions about what another tradition would say, routed for CONFIRM / REVISE / REJECT with reasoning. Operates on consensus outputs, so it depends on 31 and routes over 32. Revised change 6.
- [34 — PRS displacement phrasings](34_prs_displacement.md) — *outlined.* A fourth PRS field recording how the Resource transforms the Problem into the Solution, as a natural-language vector rather than a pointer, so triplets sharing endpoints but differing in path become comparable. Carries the finite-connecting-meme hypothesis: that cross-paradigm transformations may fall into a limited recurring typology. Revised change 3.
- [35 — Developmental maturity model](35_maturity_model.md) — *drafted.* Stages 0 through 5 with measurable benchmarks, plus the health metric r (intra-tradition consensus rate over cross-tradition survival rate, which must be statistically greater than 1). Already measured nightly in the metrics snapshots, which currently report Stage 1; this publishes the ladder those measurements are keyed to. Revised changes 7 and 8.
```

**These five lines were validated on 2026-08-24** by running the two regexes above,
copied verbatim out of `community_interactions.html`, over the block under `node`. All five
parse: the group heading resolves, and ids 32/33/34/35 each yield the right href, status
and title. If Session II edits the wording, re-run that check rather than trusting the eye
— a failed item line produces no error anywhere.

The pair names use `×` (U+00D7), matching the existing usage in `pathways.md` and in
`31_cortical_column_architecture.md`. The repo's ASCII-only rule governs shell blocks pasted
into a terminal, not the contents of vault markdown, so no substitution is needed here.

### 3.5 Lineage correction on Pathway 31

Two edits, both additive:

1. Append to 31's inventory description in `pathways.md`: *"Descends from the 2026-04-09
   Thousand Brains redesign proposal (revised change 5, with half of change 7),
   independently resurfaced 2026-06-24 and retargeted from tripled tradition agents to
   per-thinker assessor columns."*
2. Amend `31_cortical_column_architecture.md:149` so the provenance line names both origins
   rather than only the 2026-06-24 one. Do not delete the existing attribution — add to it.

### 3.6 Pathway file contents

Each of the four new files follows the shape of `31_cortical_column_architecture.md`:
frontmatter with `title`, the motivating insight, the concrete change, dependencies, cost,
a falsifiable success criterion where one is available, and a provenance line at the foot.

Content is already written and reviewed — lift it from the revised proposal rather than
re-deriving:

- **32** ← revised change 4 (lateral communication), including the start-narrow mitigation
- **33** ← revised change 6, including the critical ordering note that inquiry runs on
  consensus outputs, not raw agent proposals
- **34** ← revised change 3, including the connecting-memes hypothesis and the instruction
  that 14a track it and 15a/15b test it
- **35** ← revised changes 7 and 8 together: the r definition, its three-way interpretation
  (`r ~ 1` traditions are not distinct, `r -> infinity` echo chambers, statistically `> 1`
  healthy), the null hypothesis it is tested against, and the full Stage 0–5 ladder

Every one of the four gets both link forms from 3.3, which also closes the 0-backlink
orphan on the proposal.

### 3.7 Verification before any push

The standing rule applies in full — this is HTML-affecting content on a published page, not
a data-only refresh, so the heartbeat carve-out does not cover it.

```bash
cd "/Users/tomloughran/Documents/Claude/Projects/RC Karpathy Wiki Project/wiki" && python3 -m http.server 8080
```

Then at `http://localhost:8080/explorer.html`, on the Community Interactions tab, open
"The Road Ahead" and confirm:

1. the count reads **36 development pathways**, up from 32 — a wrong count means one of the
   four lines failed the item regex silently
2. the new "Thousand Brains arc" group heading renders as its own group
3. all four titles are links, and each opens the pop-up reader rather than 404ing
4. inside each reader, the `../review/...` link to the proposal resolves
5. Pathway 31's description carries the added lineage sentence
6. no console errors

Report those observations, then wait for sign-off before pushing.

---

## 4. Parked, deliberately

- **Revised changes 1, 2, 9, 10** — shipped; belong to the changelog, not the inventory.
  See section 2.
- **Whether the sociogram edge extractor reads markdown links as well as wikilinks.** Not
  checked. The plan hedges by writing both forms, so the answer does not block execution.
- **Re-running the backlink census** to confirm the orphan closed. Cheap, but it is a
  separate artifact with its own cadence; do not fold it into this change.
- **Actually implementing 32 / 33 / 34.** This plan puts them on the published roadmap. It
  does not build them, and all three sit behind 31, which is itself post-ISME.

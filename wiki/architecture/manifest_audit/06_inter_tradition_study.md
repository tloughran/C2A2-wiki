# Inter-Tradition Study

**family** reader · **manifest entry** NONE (knowledge file only)

## identity
`wiki/interT_study.html`, 98,879 B, 1,504 lines. Explorer tab "Inter-Tradition
Study" (`explorer.html:457`; key `inter_tradition_study` at `:1935`).
**Generated** by `scripts/build_study.py` (docstring `:2`, `OUT` at `:30`) from
the template `wiki/study_shell.html`, substituting `__TAB_BUTTONS__` and
`__DOC_BLOCKS__` (`:64-65`). A non-writing `--check` run reports "OK: matches its
2 markdown sources", so the built file is currently in sync.

**Edit the template, never the output.** A hand-edit of `interT_study.html`
would be overwritten and would fail `--check`. `study_shell.html` is a build
input, not a page (see `23_non_surfaces.md`).

## purpose
Presents the preregistered inter-tradition dialogue study and its N=38
replication as two readable documents with a contents sidebar.

## data sources
Both sources inlined as `<script type="text/markdown">` blocks
(`build_study.py:33-44, 60-62`):
- `openstory-legibility/study_interT_dialogue_c2a2.md` (64,877 B, 14 H2)
- `openstory-legibility/replication_rung1_N38.md` (20,221 B, 7 H2)
Plus `marked@11.1.1` from CDN (`study_shell.html:7`). No runtime fetch.

## entities and fields
Two documents, each a tree of H2/H3 headings slugified to 50 chars (the TOC).
The study has §1-§7 plus Appendices A-G, with H3s under §3-§5 (e.g. 4.1 Rung 1,
4.2 BRIDGE negative, 4.5 Scorecard); the replication has §1-§7. There are
markdown tables (52 `|` lines in the study) but **no structured data layer** —
the study's findings are prose, not records.

## cut
A pure address, plus one action.

| dim | kind | binding |
|---|---|---|
| document | set, 2-way | `#doctabs button[data-doc]` → `render(key)`; deep link `#doc=<key>` |
| section | address (ordinal) | `#toc a` → `#<slug>` ids; an `IntersectionObserver` scroll-spy marks `.active` |
| help | action | `#help` overlay, Esc to close |

The address **is** written to the hash (`#doc=<key>`), making this one of only
three surfaces in the project whose cut is linkable — see main document §4.4(a).
Section slugs are stable but derived from heading text, so `go <section>` would
be free-text resolution, not a coordinate. Tables and figures inside the prose
are unaddressed.

## change signal
A change to either source markdown, with `build_study.py --check` as the existing
staleness gate — a real, cheap, already-written freshness check that nothing
consumes. Grain: one document, or per H2/H3 if diffed. Frequency is near zero: the
study is "preserved exactly as preregistered" and the replication is separate.

## export shape
CSV: `doc_key, section_id, level, heading, word_count`. JSON:
`{doc, section_id, heading, markdown}`. Whole-document export is just the source
markdown, which already exists — so for this surface "export" should mean *link
to the source*, not generate a file.

## narration
The `#help` modal prose in `study_shell.html` is a good seed.
`voice_guide/knowledge/inter_tradition_study.default.md` exists and is mapped at
`explorer.html:6162`. **No shell `descriptions` entry** — one of only two tool
tabs with no "?" at all.

## current capability
Contract: none (0 `c2a2` hits). No `c2a2Ask`, no export, no state bus. One
one-off "What is this" modal, not an explainer system. **No manifest entry** —
`inter_tradition_study` is absent from `manifests.json`'s 9 keys, so
`activeManifest()` returns null on this tab and the shell falls back to generic
caps.

## what resisted description
- Whether the shell has a blurb for this tab: none found in the lines read
  (inferred absent, consistent with the missing `descriptions` key).
- Whether `go <section>` would work at all, given free-text heading addresses.
- Nothing amorphous. It is a two-document reader with a linkable address and a
  working staleness gate, and it is missing from the manifest for no reason the
  audit could find.

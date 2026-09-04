# SPEC: Tome extraction (Phase A1)

Status: written 2026-09-04, NOT YET EXECUTED. Repo untouched.
Plan of record: `handoffs/explorer-roadmap.md`, seventh entry (+ its A1 correction note).
House style: diff this against `wiki/inbox/rc_sandbox/batches/CLASSIFY_SPEC.md` before use — that
spec produced 0 malformed / 0 duplicate / 0 missing across 2,246 judgment cells and its
conventions win where they differ from mine.

## 1. Purpose

Turn the Pilot Tome from a baked HTML page into unit-level records with stable anchors, so that
it and the RC Sandbox live in one corpus and can be linked, indexed and cited at the same
precision. **A1 is extraction only.** No classification, no node assignment, no voice
assignment — those are A4/A5 and they inherit from this.

## 2. Source of record

**Extract from `wiki/rc_document_explorer.html`** (1,738,922 bytes, mtime 2026-07-01).

- A second, older copy exists at `Resurrecting Civility Whole/RC_Document_Explorer.html`
  (1,608,953 bytes, 2026-06-04). **Do not use it.** Record the SHA-256 of the file actually
  parsed in the run log.
- `Resurrecting Civility Whole/RC_Document_Explorer.md` (120,810 words) and
  `Resurrecting Civility Pilot ChatGPT Tome - Google Docs.pdf` are **cross-checks only**, never
  inputs.

## 3. Measured structure — verified 2026-09-04, do not re-derive

| selector | count | role |
|---|---|---|
| `p.doc-body` | **1,106** | the prose unit. Flat `<p>`, not nested. |
| `h1.doc-h1` / `h2` / `h3` / `h4` | 177 / 194 / 254 / 65 = **690** | section headings |
| headings carrying an `id="pNNN-slug"` | **679** | ~11 headings are unanchored — see §7 |
| `div.page-marker` (`id="page-N"`, `data-page="N"`) | **472** | page boundaries |
| `a.toc-link` | **615** | the existing ToC |
| `div.prs-card` (`data-thinker`, `data-implicit`) | 184 / 101 | PRS layer — **A3, not A1** |
| `div.prs-row` | 156 | PRS layer — A3 |
| `.sp-cell-p` / `-r` / `-s` | 53 each | Synergistic-Coils P/R/S table — A3 |

⚠️ Two numbers in the seventh handoff entry were wrong and are corrected here: the ToC is
**615** links, not ~1,196 (that figure was the `data-page` attribute count, which spans
toc-links *and* page-markers); and headings number 690, of which 679 are anchored.

## 4. Unit definition — the contract

A **unit** is one `p.doc-body` element. Nothing else is a unit in A1.

Each unit is stamped with, by document order:
- the nearest **preceding** `div.page-marker` → `page`
- the nearest **preceding** anchored heading → `heading_id`, `heading_level`, `heading_text`
- its ordinal within that heading → `seq` (1-based)

Headings are **not** units. They are metadata carried on the units beneath them, and they are
emitted separately to `tome_headings.csv` (§6) so the ToC can be rebuilt without re-parsing.

Rationale for choosing `p.doc-body` over the page: 1,106 paragraphs against 472 pages, at no
extra cost, and every downstream link, index entry and bibliography citation inherits that
precision permanently. Page granularity was considered and rejected in the seventh entry.

## 5. `unit_id` scheme

    tome:p<PAGE>h<HEADING_ORDINAL>s<SEQ>      e.g.  tome:p104h02s07

- `PAGE` zero-padded to 3, `HEADING_ORDINAL` and `SEQ` zero-padded to 2.
- Namespaced so it never collides with `sandbox:r247c04`.
- **Derived from position, not from the slug.** Heading slugs in this file are truncated at ~44
  characters and are not unique (`p104-de-veritate` and
  `p104-de-veritate-question-2-article-14-the-so` coexist), so a slug-keyed id would collide.
  Same trap as `feedback_processed_log_slug_keying` — slug is too loose. Keep the slug as a
  *field* (`heading_slug`) for backward links; never key on it.

## 6. Outputs — `wiki/inbox/rc_tome/`

`tome_units.csv` — one row per unit, columns exactly:

    unit_id, doc, ord, page, heading_id, heading_level, seq, words, text

`doc` is the literal `tome`. `ord` is global document order, 1..N. `text` is the unit's visible
text, HTML entities decoded, inline tags stripped, **whitespace-collapsed but otherwise
unaltered**. Verbatim lives here and nowhere else.

`tome_headings.csv` — `heading_id, page, level, ordinal, heading_slug, text, reconstituted`

`tome_extract_log.md` — source SHA-256, counts asserted vs found, every §8 assertion with its
result, and every §7 decision taken with its reason.

**Do not write `corpus_units.csv` in A1.** The merge with the migrated Sandbox rows is A2, and
keeping A1's output separate means a bad extraction is deleted, not unpicked.

## 7. Known hazards — each needs a decision recorded in the log

**H1. Wrapped headings — the wrap is IN THE HTML, not just the .md.**
Corrects F7 of the seventh entry, which blamed PDF extraction into the markdown. Measured: page
41 carries `<h1>Sean Carroll's Critique of Consciousness-Centric</h1>` and
`<h1>Universe Models</h1>` as two separate elements. It is an upstream artifact that propagated
into both files, so **reconstitution is required regardless of which source is parsed.**
Rule: two adjacent headings of the same level, under the same page, where the first ends without
terminal punctuation and the second begins lowercase or continues the clause, are **candidates**
for joining. Emit every candidate to the log with both texts; **join only the unambiguous ones**
and set `reconstituted=1`. Do not silently join. Do not join across a `page-marker`.

**H2. ~11 unanchored headings** (690 elements, 679 with a `pNNN-` id). Find them, list them in
the log, and assign each a synthetic `heading_id` of the form `pNNN-x<ordinal>`. Never drop a
unit for want of an anchored parent.

**H3. Units before the first heading.** Any `p.doc-body` preceding the first anchored heading
gets `heading_id = pNNN-frontmatter` rather than being dropped.

**H4. Tables.** 178 `<td>` / 23 `<th>` exist. Cells are **not** `p.doc-body` and are therefore
out of A1. Count them, log the count, and note where they sit. Do not invent a unit type for
them here — that is a decision for A5 once the outline transfer is tested.

**H5. Markdown-significant leading characters.** The Sandbox generator hit this (68 cells). It is
a *rendering* concern for the generated views, never a reason to alter `text`.

## 8. Verification — the run is not done until every assertion passes

Assertions run as code against the written CSV, re-parsed from disk. **Never accept the
extractor's self-report** — the same discipline that made the Sandbox pass trustworthy.

- **V1 Counts.** `len(tome_units.csv) == 1106`. Assert against a number obtained by an
  *independent* method (a `grep -c` on the source), not by the parser's own tally.
- **V2 Ids.** Every `unit_id` unique; zero missing; zero extra; format matches §5.
- **V3 Verbatim.** For every unit, its `text` is present in the source after entity decoding and
  whitespace collapse. Zero exceptions. A single failure stops the run.
- **V4 Word total.** Sum of `words` compared against the .md cross-check (120,810). This will not
  match exactly — the .md includes headings and the HTML includes non-`doc-body` text.
  **Record the delta and explain it. Do not tune the extractor to close it.**
- **V5 Monotonic page.** For every unit, `page >= page` of the preceding unit by `ord`.
- **V6 Parentage.** Every unit has a `page` and a `heading_id`, per H2/H3.
- **V7 ToC closure.** All 615 `a.toc-link` hrefs resolve to a `heading_id` present in
  `tome_headings.csv`. This checks the anchor set from a direction the extractor did not build.
- **V8 The falsifier — mandatory.** Run the checker against two deliberately corrupted copies:
  one with a unit removed, one with a single character mutated inside a unit's text. **The
  checker must FAIL both.** A checker that only ever passes has not been tested. If it does not
  fail, the checker is the bug, not the data.

## 9. Stop conditions

Stop and report rather than proceed if: V3 fails at all; V1 is off by any amount; the source
SHA-256 does not match what the log records; or the H1 candidate list contains cases you cannot
call unambiguously. A partial extraction that reports success is the failure mode this whole
spec exists to prevent.

## 10. Explicitly out of scope for A1

Classification, node assignment, `voice` (A4 — and note the Tome's default voice is the MODEL,
not Loughran), `about`, the PRS card harvest (A3), the Sandbox migration (A2), either ToC design
(A6), and any commit of the 13.7 MB workbook. A1 produces two CSVs and a log. Nothing else.

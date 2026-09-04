# Tome extraction log (A1) — run 2026-09-04

Source: wiki/rc_document_explorer.html
SHA-256: 9ecb26fa762fbc1c4391935a3331dd71f35a7adf671755631740f55febe52157
Scripts: extract_tome.py, verify_tome.py (copies in this directory; scratch originals in ~/rc_tome_work on the Mac)

## Counts asserted vs found
- p.doc-body: asserted 1106, found 1106 (978 plain + 128 styled). The 128 styled ones are ALL the
  "Appendix: Works Consulted" bibliography entries after `<!-- APPENDIX -->`, under page marker
  `page-appendix` (non-numeric). The spec's 1106 silently included them. DECISION: kept as units with
  page = `appendix`, unit_id prefix `tome:pAPP`. They are bibliography, not Tome prose; A5 should
  filter on page == appendix before classifying. Word count of the appendix is inside the 117,222.
- headings with class doc-h1..h4: 690 found (177/194/254/65). 22 further `<h4 style=...>` headings in
  the appendix carry no doc-hN class and are NOT in tome_headings.csv (matches the spec's 690).
- page markers: 472 (471 numeric + appendix).
- a.toc-link: 615.

## Hazard decisions
- H1 wrapped headings: 69 candidates by rule (unbalanced brackets/quotes across the pair, second half
  lowercase, first half ending on a function word, or a known fragment). 4 excluded as lettered/roman
  siblings (`a. … + b. …`, `I. … + II. …`). 65 joins applied, including one 4-heading chain (p238).
  Merged heading keeps the FIRST id; absorbed ids listed in the `absorbed` column and kept resolvable
  for old ToC links. 80 units remapped. Lists: h1_join_candidates.json, h1_joins_applied.json.
  690 -> 625 headings.
- H2 unanchored: 11 headings without an id, assigned synthetic ids pNNN-xN (anchored=0).
- H3 units before first heading: none on page 1 needed frontmatter (first heading precedes first unit? see V6 pass).
- H4 tables: 178 td / 24 th, out of A1 as specced.
- H5: text untouched.

## Verification (re-parsed from disk)
V1 PASS 1106/1106 (independent regex count). V2 PASS unique + format. V3 PASS all 1106 texts byte-present
after entity decode + whitespace collapse. V4 total 117,222 words; delta -3,588 vs the .md's 120,810 —
the .md includes heading text (625 headings, roughly 3.5k words) which units exclude. Not tuned.
V5 PASS. V6 PASS. V7 PASS 615/615 (one link targets `#page-appendix`, a page marker; checker resolves
page-marker ids and absorbed heading ids).
V8 falsifier: unit removed -> V1 FAIL (exit 1); one character mutated -> V3 FAIL (exit 1). Both fail as required.

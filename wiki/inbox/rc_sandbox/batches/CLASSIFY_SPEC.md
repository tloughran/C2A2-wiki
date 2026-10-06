# Classification spec — RC Sandbox (TL sandbox tab)

You are assigning cells from Thomas Loughran's research sandbox spreadsheet to nodes in an
outline he approved. Read `../outline_v2.md` first for the full outline and rationale.

## Output: ONE line per cell, pipe-delimited, in the order the cells appear in your batch file
```
cell_id|node|voice|about|discipline|work_order|confidence|reason
```
- `node` — EXACTLY one ID from the controlled list below. No invented IDs. No blanks.
- `voice` — `Loughran` (the DEFAULT, ~92% of cells) or the name of the person actually
  speaking when the cell is a quotation/transcript/testimony. Use `apparatus` for X.1/X.2.
  Append `?` to a non-Loughran voice you are not sure of (e.g. `UNKNOWN-testimony?`).
- `about` — semicolon-separated figures the cell ENGAGES. Merge the `auto_about=` hint given
  on the cell's header line with what you read; drop auto hits that are false positives
  (e.g. `Sarah` is Sara Walker the astrobiologist, NOT any Sarah; `Bloom` may be Allan Bloom).
  Empty string if none.
- `discipline` — semicolon-separated from: physics, chemistry, biology, neuroscience,
  computer science, philosophy, theology, sociology, psychology, history, economics. May be empty.
- `work_order` — `1` if the cell is a note-to-self / task ("find reference to...", "write the
  paper...", "pull these quotes out carefully", "need an example here"), else `0`.
  A work-order cell STILL gets its topical node.
- `confidence` — high | med | low
- `reason` — under 90 chars, no pipes, no newlines, no commas needed. Say what the cell IS.

## Controlled node list — use these strings verbatim
I.1 I.2 I.2.1 I.2.2 I.2.3 I.2.4 I.3.1 I.3.2 I.3.3 I.4 I.4.1 I.4.2 I.4.3 I.5
II.1 II.2 II.3 II.4
III.1 III.1.1 III.1.2 III.1.3
III.2.0 III.2.A III.2.I III.2.S III.2.N III.2.P III.2.C III.2.SO III.2.X
III.3 III.4
X.1 X.2 Z

## What each node means (short)
- I.1 diagnosis: why civility failed, what is at stake, empire, polarization
- I.2 MacIntyre's algorithm generally; I.2.1 traditions as unit of enquiry;
  I.2.2 epistemological crisis + resolution; I.2.3 incommensurability, vindication on the
  rival's own terms; I.2.4 natural law and intractable dispute (IDM/IDNL reading seam)
- I.3.1 observables — what counts as a signal when traditions meet
- I.3.2 scoring — rubrics, criteria, the quantitative model of information transfer between
  traditions (content, rate, saturation, maturity of members)
- I.3.3 provenance — the evidentiary record, right to know the background of public claims
- I.4 the accelerator generally; I.4.1 conditions of encounter (in person/online, print,
  AI-accelerated); I.4.2 rhetoric, invitation, persuasion, bounds of argument;
  I.4.3 community as the medium (rich communities, PoP, families, teachers as inviters)
- I.5 failure modes — what would falsify the design, relativism conceded, limits
- II.1 membership criterion (expect ~zero cells; it is to be written, not harvested)
- II.2 a figure discussed AS a figure (biography, standing, who they are)
- II.3 modes of interaction — meeting, correspondence, podcasts, AI conversation as a mode
- II.4 bibliography and source pointers — cited works, page refs, URLs, reading notes whose
  content is the SOURCE rather than an argument
- III.1 the core claim: conscious realist monism, fundamental consciousness, limited
  perspective; III.1.1 arguments against physicalist priority AND rival positions stated at
  full strength (IIT, GNW, physicalism); III.1.2 prediction, modeling, interface theory,
  how ideas are constructed; III.1.3 truth as an achieved relation between intellect and object
- III.2.0 statements of the LAYERING ITSELF (the A-I-S / S-N-B-P / P-C-S ladder)
- III.2.A Awareness level · III.2.I Information level · III.2.S Space-time level
  (physics, computer science, philosophy contribute here)
- III.2.N neuronal/columnal level (chemistry, biology, neuroscience contribute)
- III.2.P personal · III.2.C communal · III.2.SO social (psychology, sociology; MacIntyre's
  social theory applies at P-C-S)
- III.2.X cross-level claims: "empirical everywhere", computation as matrix multiplication
  running through all layers, philosophy and CS at every level
- III.3 goods, freedom, will, natural law, ethics, human dignity, telos
- III.4 love, community, the person, friendship, healing
- X.1 numeric/bookkeeping cells the spreadsheet wrote to itself (bare numbers, subtotals)
- X.2 in-sheet labels, stray table headers, numbered list items, fragments that head another cell
- Z unclassifiable CONTENT (a real fragment you cannot place). Use sparingly; target <5%.

## Rules
1. **Verbatim discipline.** You are placing cells, not editing them. Never rewrite text.
2. **Default voice is Loughran.** Only override on evidence: quotation marks, a page citation
   introducing a passage, an obvious change of register, first-person narrative that is not his.
   Unmarked quotation exists — a 200-word first-person testimony that does not sound like a
   philosopher writing notes is probably quoted. Flag with `?`.
3. **Disciplines are a facet, not the structure.** A cell about the economics of social business
   at the communal level is `III.2.C` with `discipline=economics`, NOT an economics node.
4. **Levels beat topics in III.2.** Ask "at what level of the ladder does this operate?"
5. When a cell fits I and III equally, ask: is it about the RULES of tradition-encounter (I)
   or about WHAT IS TRUE (III)? Rules go to I.
6. Do not use Z to avoid a hard call. Use it only when the cell has no placeable content.
7. Some cells are fragments continuing the previous cell in the same row. Read neighbours
   in your batch file for context before assigning.

## Worked examples (from the approved pilot)
```
r54c7|I.3.2|Loughran|MacIntyre||0|high|explicit rubric for mastery of the tradition-encounter account
r85c4|I.1|Smedley Butler||history|0|med|QUOTED war-is-a-racket passage as empire diagnosis
r567c3|I.5|MacIntyre|MacIntyre|philosophy|0|high|AV2:277 no a priori guarantee against relativism
r456c17|I.3.2|Loughran||sociology|0|high|quantitative model of inter-tradition information transfer
r422c8|I.3.3|Loughran||sociology|0|high|a right to full information provenance for public claims
r186c8|III.2.SO|Loughran|Pentland|sociology|0|high|connections predict behavior better than demographics
r357c5|III.2.N|Loughran|Hoffman|neuroscience|0|high|correlation without causation in Cs-brain studies
r172c4|III.2.0|Rohr|Rohr|theology|0|high|QUOTED Rohr passage on reading scripture
r29c9|III.2.N|Loughran||biology|1|med|to-do find biologist allowing empirical Lamarckian evolution
```
(Note: r172c4 above is theology content — it would in fact be `III.2.P`; treat the example as
showing FORMAT, and use the node meanings above for placement.)

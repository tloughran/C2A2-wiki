---
proposal_id: PROP-2026-10-13-003
thinker: Multiple (see entries)
tradition_key: multi
source_type: dataset-explorer
source_title: "RC Sandbox: the TL Sandbox worksheet (wiki/rc_sandbox_notebook.html; page title 'Quodlibet Notebook'), 2,191 cells"
source_url: n/a
source_date: 2026-10-13
searched_on: 2026-10-13
status: pending
---

## Verification caveats

- **Source identification.** The explorer's tool registry (wiki/explorer.html, section "Community Education") names "RC Sandbox — the TL Sandbox worksheet, 2,191 cells" as the spreadsheet tool. wiki/rc_sandbox_notebook.html matches: its topbar reads "TL sandbox · 2,191 cells · 137,828 words · verbatim", and its About section says every block is "the unedited text of a single cell of the TL sandbox tab." Anomaly: its HTML title is "Quodlibet Notebook", not "RC Sandbox." wiki/rc_sandbox_figures.json is the notebook's figure-bio index (76 figures, 63 drafted by a model); it was not used as evidence. wiki/rc_document_explorer.html mentions spreadsheets but is a document tool and was excluded.
- **Criteria.** wiki/c2a2-prs-3d/testcorpus/CRITERIA.md defines C1 to C6 for links between corpus entries. They do not apply to evidence inside one source. Tiers below were assigned by hand on the High/Medium/Speculative scale, not by those criteria.
- **Quote check.** Each quote is an exact substring of wiki/rc_sandbox_notebook.html and occurs inside the named cell's article block. Quotes that match only in HTML-escaped form (apostrophes written as &#x27;) are marked. Quotes were not checked against the thinkers' own books, which the explorer does not hold.
- **Voice labels.** 183 cells carry a quoted-voice label. Of these, 62 labels end in "?" (uncertain), 11 read UNKNOWN, and 121 name a voice cleanly. Only clean labels are used as thinker evidence. The 1,997 unlabelled cells are treated as Tom's own words, per the notebook's About section. Figure links, discipline tags and figures.json are [MODEL].
- **Abbreviations not expanded in the explorer.** "IDM" is an edited volume whose contributors named in cells include Philpott, Porter, Ratzinger, McKenny and MacIntyre. "WJWR" is cited as the MacIntyre source with page numbers; it is inferred, not confirmed, to be Whose Justice? Which Rationality? "M" means MacIntyre by context. "1st Ps" is not expanded.
- **Count gap.** The file has 2,191 cell articles; 2,180 carry a data-date and were parsed. The other 11 are single-word rung labels (r246c4 to c11, r60c4, r62c4, r64c4). None is a candidate.
- **Scratch space.** The /sessions volume reported no free space during the run, so scratch work went to /tmp/rc_scratch_2026-10-13, outside the project. Nothing else was written, edited or committed.
- **Search limits.** A recursive grep for the exact phrase "spreadsheet explorer" across the wiki timed out, and a narrower pass returned nothing. Absence of the phrase is therefore not confirmed; identification rests on explorer.html's registry.

## Summary

Five candidates are kept, all at Medium. Each rests on at least one [THINKER] or [TOM] item and each passed the verbatim check. PRS-SE-01, -02 and -04 rest on [THINKER] text and qualify for their thinker's PRS file (macintyre, kastrup). No file was edited. PRS-SE-03 has no Porter file. PRS-SE-05 is [TOM] only and is not attributed to a thinker file.

Dropped, reported only (9 groupings):
- Perez "principles of modularity" (r517c10 to c21): numbered principles, no Problem stated.
- Ratzinger? questions (r48c4 to c6): question form only; label uncertain.
- Rohr "On Law" (r460c4): one sentence, no Problem or Solution.
- Tom's summary of MacIntyre's "3 essential requirements of a paradigm shift" (r238c3): [TOM] paraphrase; the three requirements are not stated in the cell.
- Irving and Askell alignment subproblems (r232c3, c5, c6, c10): source not identified in the cell.
- Lyon? basal cognition definitions (r595, r609): definitional; label uncertain.
- Jack Ma and Elon Musk exchange (r270): [TOM] paraphrase with speaker tags, not verbatim.
- AwareComm (r234c4 to c9): corporate self-description, not an argument.
- Tim Urban? narrowcasting (r396): label uncertain; quoted passages with no claim structure.

Top three reasons for rejection: no Problem or Solution stated in the cell's own words (4 groupings); attribution uncertain (3 groupings); paraphrase by Tom rather than thinker text (2 groupings).

## Candidate triplets

### PRS-SE-01 (Medium): Justification as narrated history (MacIntyre voice)

- **Problem** [MODEL framing, not evidence]: How can a tradition's first principles be justified without a view from outside every tradition?
- **Resource** [THINKER: MacIntyre]: "to justify is to narrate how the argument has gone so far (WJWR p.8);" — r348c10, section I.2.2 (Epistemological crisis), row 348, seq 5, dated 2019-12-31, voice label "MacIntyre." Verbatim: PASS.
- **Solution** [THINKER: MacIntyre]: "They are justified insofar as in the history of this [that is, any successful] tradition they have, by surviving the process of dialectical questioning, vindicated themselves as superior to their historical predecessors." — r359c3, section I.2.2, row 359, seq 1, dated 2019-12-31, voice label "MacIntyre." Verbatim: PASS. Tom's gloss in the same cell ("// WJWR p. 360: on 1st Ps:") is [TOM].
- **Authorship:** Resource and Solution [THINKER: MacIntyre]; Problem [MODEL]; page references [TOM].
- **Tier:** Medium. Two passages in MacIntyre's voice with page references; the explorer does not hold the book, so page accuracy is unchecked.
- **Thinker file:** macintyre/prs_triplets.md is eligible on the [THINKER] basis. Overlap with existing macintyre entries was not checked. Not edited.

### PRS-SE-02 (Medium): Truthful speech as the condition of shared enquiry (MacIntyre voice)

- **Problem** [THINKER: MacIntyre]: "We need to avoid allowing our own thinking to give expression to our prejudices" — r27c5, section I.4.2 (Rhetoric and invitation), row 27, seq 3, dated 2024-11-30, cell tagged "IDM p. 22." Verbatim: PASS.
- **Resource** [THINKER: MacIntyre]: "a form of intellectual and moral asceticism" — r27c5, same cell. Verbatim: PASS.
- **Solution** [THINKER: MacIntyre]: "If I am to engage with you in shared rational enquiry,we must both be assured that we can expect the other to speak the truth, as she or he understands it. There must be no deceptive or intentionally misleading speech." — r27c7, row 27, seq 4, dated 2024-11-30, cell tagged "IDM p.. 23." The source has no space after "enquiry,"; quoted as written. Verbatim: PASS.
- **Authorship:** all [THINKER: MacIntyre].
- **Tier:** Medium. All three elements come from one short passage of one volume (IDM, pp. 22 to 23), so the triplet is less independent than PRS-SE-01. Problem and Resource sit in the same cell.
- **Thinker file:** macintyre eligible; overlap not checked.

### PRS-SE-03 (Medium): Practical reason presupposes desire, not theory (Porter voice)

- **Problem** [MODEL framing, not evidence]: Must the precepts of natural law rest on a prior speculative theory of human nature?
- **Resource** [THINKER: Porter]: "reason in its practical operations always presupposes a rational desire for some perceived good" — r38c6, section I.2.4 (Natural law and intractable dispute), row 38, seq 4, dated 2017-12-29, voice label "Porter." Verbatim: PASS. This is Porter's exposition of Aquinas.
- **Solution** [THINKER: Porter]: "does not presuppose a speculative theory, about the inclinations or anything else" — r39c6, row 39, seq 3, dated 2017-12-29, label "Porter IDM (NL) p. 83." Verbatim: PASS. The cell's text is run together and OCR-like in places ("ofthe inc linat io ns"); the quoted stretch contains no garbled word.
- **Authorship:** [THINKER: Porter] (surname only; first name not in the cells). Problem [MODEL].
- **Tier:** Medium. Porter is not one of the fifteen traditions in wiki/traditions, so there is no thinker file. Report under Multiple.

### PRS-SE-04 (Medium): Experience-first dissolution of the matter problem (Kastrup voice)

- **Problem** [THINKER: Kastrup]: "Where we get lost and confused is in imagining that what we are describing is a non-mental reality underlying our perceptions, as opposed to the perceptions themselves." — r598c4, section III.1.1 (Against physicalist priority), row 598, seq 2, dated "live," voice label "Kastrup." Verbatim: PASS. The same sentence recurs in r598c7 (file count 2).
- **Resource** [THINKER: Kastrup]: "solidity and concreteness are qualities of our experience" — r598c4. Verbatim: PASS.
- **Solution** [THINKER: Kastrup]: "The problem we face is thus merely an artifact of thought, something we conjure up out of thin air because of our theoretical habits and prejudices." — r598c4 (and r598c7). Verbatim: PASS.
- **Authorship:** all [THINKER: Kastrup]. The cell opens "from Bernardo Kastrup:"; the source text is not named.
- **Tier:** Medium. The cell is undated ("live" sheet date), and the "conundrum" in its first sentence is not defined there.
- **Thinker file:** kastrup/prs_triplets.md is eligible on the [THINKER] basis. Keyword check ("artifact of thought," "conjure," "thin air," "solidity," "immediately present") found no existing entry using these passages. Not edited.

### PRS-SE-05 (Medium): Information overload as the problem the RC project answers (Tom's own words)

- **Problem** [TOM]: "We're in an information shitstorm, and it's drowning us, polarizing us as we go under." — r480c4, section I.1 (The diagnosis), row 480, seq 2, dated 2020-12-28, unlabelled. Verbatim: PASS (apostrophe written as &#x27; in the HTML).
- **Resource** [TOM]: "We've lost something we once had, a craft of being human, or many crafts, and a way to learn from them all." — r480c5, row 480, seq 3, same date. Verbatim: PASS (escaped apostrophe). The same cell attributes the suggestion to "M" ("This is M's disquieting suggestion"), read as MacIntyre by context; that attribution is Tom's, not verified.
- **Solution** [TOM]: "The RC project will deliver a solution set that addresses all these challenges." — r480c8, row 480, seq 6, same date. Verbatim: PASS.
- **Authorship:** all [TOM]. No [THINKER] text carries the core claims, so this is not attributed to a thinker file, and loughran/prs_triplets.md is not edited.
- **Tier:** Medium. The three cells form a numbered block from one dated entry, and the Solution names no mechanism. A keyword check of traditions/loughran/prs_triplets.md (information overflow or overload, shitstorm, overwhelm, natural law) found no duplicate.

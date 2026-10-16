---
proposal_id: PROP-2026-10-13-001
thinker: Alasdair MacIntyre
tradition_key: macintyre
source_type: book
source_title: "Three Rival Versions of Moral Enquiry (1990)"
source_url: n/a
source_date: 1990
searched_on: 2026-10-13
status: pending
---

## Verification caveats

- **Quote check.** Each quoted string was matched exactly (grep-style substring test) against `wiki/commentary-explorer/data/ocr_text.json`, page by page. "Line" means the zero-based line index of that page string after splitting on newlines. Quotes are the OCR's own characters. The OCR is poor: word spaces are missing (e.g. "ofutterance"), words are misread, and lines break mid-phrase. So these are not clean print. A quote spanning two OCR lines was not used.
- **Scan not viewed.** `3RVME.pdf` is 287 MB, over the 250 MiB render limit of the PDF tool, so no page image was checked. Every `[MARK]` item below is **unverified**. The index's `content` field is a transcription that can differ from the OCR (for example "Incapacities" in the OCR against "incapacities" in the index).
- **Criteria.** `wiki/c2a2-prs-3d/testcorpus/CRITERIA.md` defines C1 to C6 for links between entries in a corpus (naming, inherited distinctive terms, placement, direction, asymmetry, coinage). It does not apply to evidence inside one author's triplet. C2 to C6 do not apply here, and C3 was measured and dropped in that file. Tiers follow the High / Medium / Speculative scale of the existing macintyre file.
- **Anomalies (reported, not fixed).** Annotation count: the index header reads "Annotations found: 1819" (line 21), the frontmatter reads `annotation_count: 3400`, and the index holds 3400 annotation entries on 236 pages. `handoffs/RUNBOOK_3rv_part2_ingest_2026-09-14.md` reports 3015 annotations across 218 pages. Model: `RC_Commentary_Pipeline_Technique.md` names `claude-sonnet-4-6`. `chapters.json` and the September runbook name `claude-opus-5` for the later chapters, and the runbook splits Sonnet (Ch. I to VIII) from Opus (Ch. IX to X).

## Summary

Three candidates are kept, all at Medium confidence. Every kept candidate rests on printed quotes that pass the exact check, and none rests on a mark alone. Further candidates were dropped for overlap with PRS-01 to PRS-06, for OCR too damaged to verify, or for resting on a mark alone; they are listed in the run report and not in this file. Two things block the proposal from being larger. First, the OCR is too damaged to verify many passages. Second, several strong passages overlap the existing PRS-01 to PRS-06, so they were not repeated.

Overlaps not proposed: p.116 and pp.124 to 126 (epistemological crisis and assertibility, close to PRS-02); pp.202 to 205 (narrative life and "the problem of personal identity", close to PRS-04); pp.229 and 233 (institutional enforcement of consensus, close to PRS-03); p.134 (all education is self-education, close to PRS-05/PRS-06); p.33 (encyclopaedists' blindness, close to PRS-01).

## Candidate triplets

### PRS-MC-01 (Medium): Thomism offered as a rival account of rights (p.81)

- **Problem:** [PRINTED] "Quixotic" (p.81, line 13); "tempt to present Thomism as offering a rival" (p.81, line 14). [MODEL gloss, not evidence: how Thomism can stand as a rival account of the moral subject matter that modern rights doctrines address.]
- **Resource:** [PRINTED] "thesis that every human being has within" (p.81, line 19). [MODEL gloss: Aquinas's thesis that every person has natural moral knowledge.]
- **Solution:** [PRINTED] "an uncharacteristic lapse" (p.81, line 45); "responded to the French academic" (p.81, line 9). [MODEL gloss: Maritain's restatement of Aquinas as a rights theorist, which the text judges a lapse. This is a rejected solution, not an endorsed one.]
- **Named sources:** "Maritain" appears at p.81 lines 18 and 45 (verified).
- **Marks:** [MARK, UNVERIFIED] underline 81.3 "responded to the French academic philosophy"; underline 81.4 "offering a rival and superior account of the same moral subject matter as do other modern nontheological doctrines of universal rights". The OCR reads "rivaleand superior", so the mark's wording is not verified.
- **Tier:** not applicable (single-author criteria). **Confidence:** Medium.

### PRS-MC-02 (Medium): The Meno paradox and the Augustinian source (pp.114 to 115)

- **Problem:** [PRINTED] "Confronted with the paradox" (p.114, line 48); "of the Meno as to how we" (p.114, line 49). [MODEL gloss: how a learner can come to know what something is without already having the capacity to recognize the answer.]
- **Resource:** [PRINTED] "discovery of its inabilities and" (p.114, line 47). [MODEL gloss: the mind's discovery of its own incapacity, which the Augustinian scheme treats as essential to its progress.]
- **Solution:** [PRINTED] "supplying what the mind cannot itself supply" (p.115, line 10). [MODEL gloss: an external source supplies what the mind cannot supply by itself. The sentence around this phrase is badly garbled in the OCR, so the Augustinian term it refers to is not legible.]
- **Marks:** [MARK, UNVERIFIED] underline 114.20 "paradox of the Meno" (anchor "Confronted with the paradox of the Meno as to how we" matches the OCR across lines 48 and 49); underline 114.19 (content "the mind's discovery of its inabilities and incapacities which are essential to its progress"; the OCR differs in case).
- **Tier:** not applicable (single-author criteria). **Confidence:** Medium.

### PRS-MC-03 (Medium): The genealogist's denial problem and the temporary stance (p.211)

- **Problem:** [PRINTED] "theologian and the metaphysician assert without falling back into" (p.211, line 25); "the very mode ofutterance which the genealogist aspires to discret" (p.211, line 26). The line "This is a problem whose" (line 27), "inescapability" (line 28) and "was recognized in" (line 29) are separate OCR lines, and each is quoted on its own. [MODEL gloss: the genealogist cannot deny the theologian's and metaphysician's claims without speaking in the very mode being rejected.]
- **Resource:** [PRINTED] "adopts a temporary" (p.211, line 33); "stance and wears, for the purpose of this" (p.211, line 35). [MODEL gloss: the temporary stance, the mask. The text presents it as part of the solution, so Resource and Solution are not cleanly separated in print.]
- **Solution:** [PRINTED] "genealogical solution" (p.211, line 30). [MODEL gloss: the temporary-mask device is the genealogical solution the text describes.]
- **Marks:** [MARK, UNVERIFIED] underline 211.12 (content "problem whose inescapability was recognized in the second lecture"). The OCR does not show "in the second lecture", so the wording is not verified.
- **Tier:** not applicable (single-author criteria). **Confidence:** Medium.


## Tom's decision (2026-10-15): CHANGE

Flag for sewing agent: texts that overlap with existing PRS triplets should be identified and written to the appropriate PRS triplet file; these are connections we do not want to lose.

---
proposal_id: PROP-2026-09-16-001
thinker: Iain McGilchrist
tradition_key: mcgilchrist
source_type: talk
source_title: "Ralston College — AI and the Battle for the Soul with Iain McGilchrist — Lecture 1: Information is Not Understanding"
source_url: https://channelmcgilchrist.com/ralston-college-ai-and-the-battle-for-the-soul-with-iain-mcgilchrist-lecture-1-information-is-not-understanding/
source_date: 2026-08-18
searched_on: 2026-09-16
status: pending
---

## Summary

McGilchrist's own site published the Ralston College Lecture 1 recording on 2026-08-18 under the title **"Information is Not Understanding"**, running time **00:53:56**, YouTube embed ID **QNAC_QVY9BU**. The wiki already holds this lecture at PRS-61/62/63, but under a different title — "Do We Really Understand Understanding?" — sourced from the host institution's page at `ralston.ac` (PROP-2026-08-26-001). The runtime is identical, so these are the same recording carrying two different titles from two different publishers.

## Why This Matters for This Tradition

**This is a metadata correction, not new doctrine, and it should be handled as one.** The 2026-09-02 ingestion log records that PRS-61/62/63 "rest on a host's promotional summary" and that verification against the audio is "scheduled, not done." This proposal narrows that gap from the metadata side: it supplies a canonical, self-published title and a resolvable video ID, and it raises a question the wiki cannot currently answer — which of the two titles is the lecture's own. The distinction is not cosmetic. "Do We Really Understand Understanding?" is a reflexive question; "Information is Not Understanding" is a flat assertion with a truth value, and it is the form in which PRS-61's problem statement would be falsifiable.

The same page also confirms the artifact PROP-2026-08-26-002 asked to be checked — the Ralston recordings do resolve at `channelmcgilchrist.com`, so the Lecture 2 page (which returned HTTP 429 and was never retried) should be re-fetched from this publisher rather than from search results.

## Candidate PRS Triplets

**HANDLING NOTE — read before ingesting.** Do not mint a doctrinal triplet from this card. It carries no new claim by McGilchrist; its whole content is a title, an ID, and a runtime. The correct disposition is the one taken for PROP-2026-08-26-001's candidate-02: a dated CORRECTION block appended to `prs_triplets.md`, not a new PRS number. Candidate-01 below is written as a correction assignment for that reason.

PRS-CANDIDATE-01 (correction assignment — do not mint as a new PRS):
  Problem: PRS-61 through PRS-63 record a lecture title taken from the host institution's promotional page; the author's own publisher gives a different title for a recording of identical length, so the tradition does not currently know what this lecture is called or which title states its thesis.
  Resource: `channelmcgilchrist.com` posting of 2026-08-18 — title "Information is Not Understanding", running time 00:53:56, YouTube ID QNAC_QVY9BU, author-of-record Jay Livingstone (site editor, not McGilchrist).
  Solution: Append a dated CORRECTION block recording both titles, the shared runtime, and the resolvable video ID; carry the self-published title as canonical and the `ralston.ac` title as the host's variant, flagged as unresolved until the audio is heard. Add the video ID to PRS-61/62/63's Evidence lines so the scheduled verification has something to point at.
  Confidence: High (for the metadata; the identity of the two recordings is inferred from the matching runtime, which is strong but not proof)
  Evidence: Page `meta-article:published_time: 2026-08-18T07:07:36+00:00`; "Running Time: 00:53:56"; embed `https://www.youtube.com/embed/QNAC_QVY9BU`. The 00:53:56 figure is the same one recorded in this wiki's 2026-09-02 ingestion log for PROP-2026-08-26-001.

PRS-CANDIDATE-02 (procedural, not doctrinal — mint nothing):
  Problem: PROP-2026-08-26-002 left Lecture 2's URL and title unverified because the video page returned HTTP 429 and was not retried; the citation rests on search results.
  Resource: The Lecture 1 page demonstrates that `channelmcgilchrist.com` carries the Ralston recordings itself, with runtime and embed ID on the page.
  Solution: Re-fetch Lecture 2 from `channelmcgilchrist.com` rather than from search results or `ralston.ac`, and apply the same correction treatment if its title also diverges.
  Confidence: High (as a procedural instruction; it asserts nothing about content)
  Evidence: This page resolved cleanly on 2026-09-16 with full metadata; the "Recent Posts" sidebar lists the Ralston series as current site content.

## Cross-Tradition Signals

Weak but worth recording. The Ralston symposium is the venue that produced the McGilchrist × Wolfram exchange cross-filed at PRS-67/68/69, and the wiki's standing note says that disagreement "should not be adjudicated from one side's wiki." A title correction on Lecture 1 touches the chronology that exchange sits in — the 2026-09-02 log already found the symposium's date wrong by roughly two months (delivered May 2026, not July/August). If the Wolfram tradition holds the same dates copied from release pages rather than delivery dates, it has the same error. **Recommend the Master agent check whether the Wolfram-side entries carry the corrected May 2026 delivery date.** No new cross-tradition claim is made here.

No Kastrup, Stump, or Fredrickson signal. Nothing in this card bears on the hemisphere-as-model-for-tradition-dialogue question.

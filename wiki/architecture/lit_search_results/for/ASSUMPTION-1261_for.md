SEARCH-FOR-ASSUMPTION-1261:
  Date searched: 2026-09-05
  Original item: ASSUMPTION-1261
  Original statement: "Restart the self-awareness pipeline — five days dark means five days of assumptions,
    presumptions and open questions unsurfaced."  (Claim under test, per 14a's routing: the gap is
    DEFERRED work, i.e. the assumptions of 08-31…09-03 remain recoverable from artifacts after the fact.)

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1261
    Item type: ASSUMPTION (stated — quoted from a derived digest)
    Transform at each step:
      14a: Extracted verbatim; flagged rationale drift against PRESUMPTION-903 (evidence destroyed vs.
        work deferred). Routed to literature on recoverability of design rationale from artifacts.
      15a: Searched for supporting literature (2026-09-05). NOTE ON AUTHORSHIP: run by the 15c
        orchestrating context after the delegated 15a subagent was interrupted; written BEFORE any 15b
        search for this item was begun in the same context.
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Alkadhi, Laţa, Guzman, Bruegge 2017, "Rationale in Development Chat Messages: An Exploratory Study,"
       MSR'17, arXiv:1704.08500 [VERIFIED: title/ID/venue/authors] and Alkadhi et al. 2018, "How Do
       Developers Discuss Rationale?" (SANER 2018; TUM PDF located) [VERIFIED: title; year/venue from
       result text] — Rationale IS recoverable from persisted developer communication after the fact:
       ~25% of 7,500 annotated IRC messages (1,910) contained rationale. Direct support for the premise
       that a dark period leaves surfaceable material if the artifacts (here: sandbox files, CSVs,
       daily-sync digests) persist.
    2. "End-to-End Rationale Reconstruction," arXiv:2209.00398 [VERIFIED: title/ID; authors NOT verified]
       — Defines rationale reconstruction as retrospective creation of rationale from development
       artifacts and decomposes recovery into extraction, formalisation and reuse. Establishes
       after-the-fact recovery as a recognised, tooled activity rather than a hope.
    3. "CoMRAT: Commit Message Rationale Analysis Tool," arXiv:2506.10986; "Rationale Dataset and Analysis
       for the Commit Messages of the Linux Kernel Out-of-Memory Killer," arXiv:2403.18832; "Fine-grained
       Multi-Document Extraction and Generation of Code Change Rationale," arXiv:2604.10345 [all VERIFIED:
       title/ID; authors NOT verified] — A current line of work extracting rationale from commit messages
       and multi-document histories, i.e. retrospective surfacing from artifacts at scale. Analogous
       support: what 14a/14b do to transcripts, this literature does to commits.
    4. Naur 1985, "Programming as Theory Building" [established work; multiple secondary sources VERIFIED]
       — Cited here for the LIMITED support it offers: secondary readings note that before the people
       change, "a similar theory can be reconstructed from the artifacts," though incomplete and different.
       For a five-day gap with the same author present, the reconstruction condition Naur allows is met.

  Strength of support: Moderate (for recoverability of SOME rationale) / Weak (for "nothing was lost")

  Summary: The rationale-reconstruction literature supports the assumption's frame that a surfacing gap is
  deferred work: rationale is recoverable after the fact from chat logs, commit messages and documents,
  at measured rates (~25% of chat messages carry it), and there is a recognised toolchain for doing so.
  Naur's stricter position concedes that reconstruction from artifacts is possible while the original
  people remain. What the literature does not support is the stronger reading that a same-day run and a
  five-days-later gap-filling run recover the SAME set: every recovery study reports recovery as partial,
  and 14a's own 09-04 run recovered nothing for 08-31…09-03 because it did not attempt to. The support is
  for recoverability in principle, not for equivalence.

  Caveats: (a) All recovery rates are measured on artifacts written to be read (chat, commits); the
  transient reasoning of a Cowork session that was never persisted is exactly the class these studies
  cannot see, which is PRESUMPTION-903's point and is left to 15b. (b) Naur's stronger claim — the
  theory is not in the artifacts — is the direct counter and was not pursued here. (c) Search scope:
  preliminary — 3 queries; the design-rationale-capture literature proper (Lee 1997; Burge & Brown;
  Dutoit et al. 2006) was not retrieved in this search and is cited nowhere above.

  Recommendation: PARTIALLY-SUPPORTED

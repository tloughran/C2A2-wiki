SEARCH-AGAINST-PRESUMPTION-925:
  Date searched: 2026-09-08
  Original item: PRESUMPTION-925
  Original statement: [inferred] A day reconstructed from file mtimes and agent run-reports has the same
    evidential standing as one read from session transcripts; mtime is a reliable authorship and timing
    signal.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-925
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an inconsistency between two claims held by the same layer on the same day —
        the 2026-09-07 18:40 Cowork→Chat run note read against ASSUMPTION-1276 (mtime is NOT an
        authorship signal in this repo — the 09-05 commit sweep) and against the 22:00 mass-mtime batch
        observed across ~60 files including all five self-awareness registers.
      15b: Searched for challenging literature (2026-09-08), AGAINST direction only. Did not read the
        `for/` directory, `lit_search_returns.md`, or any 15a output.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Mokhov, A., Mitchell, N. & Peyton Jones, S., 2018. "Build Systems à la Carte." Proceedings of the
       ACM on Programming Languages 2(ICFP), Article 79.
       [VERIFIED: PDF retrieved from Microsoft Research; §2, §4.2.1 and Table 1 read this run] — This is
       the most directly on-point source found. The paper treats mtime-based change detection as a
       known-unsound design that the field has migrated away from. Verbatim, footnote 5: "Technically,
       you can fool Make by altering the modification time of a file without changing its content, e.g.
       by using the command touch. Make is therefore minimal only under the assumption that you do not
       do that." And in §4.2.1, on Make's repurposing of filesystem metadata as a dirty bit: "Note that
       Make requires that file timestamps only go forward in time, which can be violated by backup
       software." Table 1 records that Make alone persists file modification times, while Shake and
       Bazel persist content hashes in verifying traces. An entire engineering discipline whose core
       problem is "what changed since last time" concluded that mtime cannot answer it and replaced it
       with hashing — and named backup software as a violator, which is C2A2's exact environment.
    2. Quick, D. & Choo, K.-K.R., 2013. "Dropbox analysis: Data remnants on user machines." Digital
       Investigation 10(1):3–18; and Quick, D. & Choo, K.-K.R., 2013. "Forensic collection of cloud
       storage data: Does the act of collection result in changes to the data or its metadata?" Digital
       Investigation.
       [NOT-verified — both cited from search-result summaries; neither retrieved this run] — The
       reported finding is that file timestamp properties "change considerably" when files are
       downloaded via a browser, and that only last-written time is preserved when the vendor sync
       client is used. The second title states the problem in its own words: the act of collection
       changes the metadata. A mass-mtime batch across ~60 files at a single instant is the canonical
       signature of a sync, restore or re-index event, not of sixty edits.
    3. Willassen, S.Y., 2008. "Finding Evidence of Antedating in Digital Investigations"; with Palmbach,
       D. & Breitinger, F., 2020, "Artifacts for Detecting Timestamp Manipulation in NTFS on Windows and
       Their Reliability" (Forensic Science International: Digital Investigation), and Galhuber &
       Luh, 2021, "Time for Truth: Forensic Analysis of NTFS Timestamps."
       [NOT-verified — titles/venues confirmed via search listings; abstracts not opened this run] —
       The consistent position of the forensic literature is that filesystem timestamps are trivially
       manipulable, that manipulation is "difficult to detect retrospectively using conventional
       forensic artifacts," and that establishing a timestamp as evidence requires corroboration from
       independent artefacts ($MFT, $LogFile, $USNjrnl, prefetch, event logs). Where the discipline
       whose job is establishing what happened when treats a signal as requiring corroboration, that
       signal does not have the same evidential standing as a primary record.
    4. Bird, C., Rigby, P.C., Barr, E.T., Hamilton, D.J., Germán, D.M. & Devanbu, P.T., 2009. "The
       Promises and Perils of Mining Git." MSR 2009.
       [VERIFIED: title, full author list and venue confirmed via DBLP and the MSR 2009 listing; the
       paper itself was NOT retrieved, so no specific finding is claimed from it beyond its stated
       subject] — The canonical statement that decentralised version histories carry
       misinterpretation hazards in exactly the timestamp/attribution area. Cited here only to mark
       that even an explicit, purpose-built authorship record is treated in the literature as needing
       care; mtime is not such a record at all.
    5. German, D.M., Adams, B. & Hassan, A.E. (cregit), 2019. "cregit: Token-level blame information in
       git version control repositories." Empirical Software Engineering 24(4).
       [NOT-verified — figures from search-result summary; paper not retrieved this run] — Reported:
       across five large open-source systems, blame-per-line accuracy is 75%–91%, versus 94.5%–99.2%
       for token-level blame. The relevance is a fortiori: a system that records an explicit author
       field per commit still misattributes up to a quarter of lines. A filesystem mtime records no
       author at all — it is a single scalar with no agent, no operation type, and no distinction
       between a substantive edit, a whitespace change, a `touch`, a restore, and a re-index.
    6. OAIS / PREMIS preservation-metadata practice (ISO 14721; PREMIS Data Dictionary).
       [NOT-verified — cited from memory; no primary document retrieved this run] — Digital preservation
       standards require provenance to be recorded as explicit *events* with an associated *agent*, and
       do not accept filesystem metadata as provenance. Named here as a convergent standard, not as an
       evidential source.

  Strength of challenge: Strong

  Summary: Every literature I searched treats filesystem mtime as a weak, non-authorial, corroboration-
  requiring signal, and two of them describe fields that abandoned it after finding it unsound. The
  build-systems literature is the sharpest: Mokhov, Mitchell and Peyton Jones state plainly that Make's
  minimality holds only on the assumption that nobody touches a file without changing it, and that Make
  additionally requires timestamps to move only forward — "which can be violated by backup software."
  Shake and Bazel persist content hashes instead. Digital forensics reaches the same place from the
  adversarial side: timestamps are manipulable, manipulation is hard to detect after the fact, and no
  competent investigator rests a timing claim on mtime without corroborating artefacts. The cloud-sync
  forensics work adds the non-adversarial failure mode that actually matters here — timestamps are
  altered by the ordinary operation of sync and collection, so a mass-mtime event across ~60 files is
  better explained by one machine action than by sixty human ones. On authorship the presumption is not
  weakly supported but definitionally unsupported: mtime contains no agent field. Even systems that do
  record an author explicitly misattribute up to a quarter of lines at line granularity. So the two
  halves of the presumption fail differently: the timing half is unreliable in a way that is unbounded
  and non-random (mtime can be later than, earlier than, or identical across the substantive changes it
  is supposed to date), and the authorship half is not unreliable but absent — any authorship read from
  mtime is an inference from co-occurrence, which is precisely the inference the 09-05 commit sweep
  already falsified in this repo.

  Specific risks: (a) The changelog's "Changes Detected" section, the daily sync summaries and part of
  every metrics snapshot are built on a signal with unbounded error in both directions; every count they
  report is an upper bound contaminated by machine events and a lower bound truncated by
  metadata-preserving copies. (b) A single sync, restore or re-index event manufactures a day of
  apparent activity — the 22:00 batch across ~60 files including all five self-awareness registers is
  the worst case, because it makes the audit layer itself look active on a day it may not have been.
  (c) Authorship claims derived from mtime co-occurrence will systematically attribute machine batches
  to whichever agent ran nearest in time, which biases the human-vs-agent authorship split that
  PRESUMPTION-926 and the 54.5% corpus-share measurement depend on — an error here propagates into
  three other open items. (d) Because a reconstructed day is written in the same register format as a
  transcript-read day, the two become indistinguishable downstream; the weaker evidence inherits the
  standing of the stronger simply by sharing a template. (e) This project has already been damaged once
  by this exact inference, which makes the presumption a repeat exposure rather than a hypothetical.

  Mitigations available: Adopt the build-systems answer — content hashes. A per-file hash recorded at
  each run turns "changed" into a verifiable predicate and makes mass-mtime batches immediately visible
  as no-content-change events. Adopt the archival answer for authorship — an explicit event log with an
  agent field, written by whichever process made the change, so authorship is recorded rather than
  inferred. Until either exists: (i) mark every mtime-derived statement in the changelog, sync summaries
  and metrics snapshots with a provenance tag naming mtime as its basis, so the two kinds of day are not
  interchangeable in the register; (ii) add a cheap detector for mass-mtime clusters (n files sharing a
  timestamp to the second) and suppress or annotate those runs; (iii) forbid authorship claims from
  mtime outright, since the field does not exist — this is not a confidence threshold but a category
  error. Note that mitigation (i) is itself a declarative tag and therefore falls under ASSUMPTION-1282's
  question; it needs a named consumer.

  Search scope: Preliminary — 5 queries plus 1 document retrieval, across four literatures (build
  systems, digital forensics, cloud-storage forensics, mining software repositories). Not covered:
  empirical measurement of mtime-vs-content-hash divergence rates in macOS/APFS trees specifically
  (searched for; only grey literature returned), Spotlight/Time Machine behaviour, Obsidian/iCloud sync
  behaviour, and the archival-standards literature at primary-source level. The build-systems source is
  strong enough on its own that a broader search is not needed to establish the challenge; it would be
  needed only to put a number on the local error rate, which is better obtained in-house by hashing.

  Recommendation: CHALLENGED

STEELMAN:
  Item: PRESUMPTION-925
  Strongest counterargument: mtime is not a weak version of a transcript; it is a different kind of
  thing. It is a single scalar with no agent, no operation type and no content binding, written by
  whatever last called the filesystem — a human edit, a sync client, an indexer, a restore, a formatter,
  or `touch`. The discipline whose entire purpose is detecting "what changed since last time" looked at
  this signal and abandoned it: Make's authors' own successors record, in print, that Make is minimal
  only if you promise not to touch files and that backup software violates its assumption that
  timestamps move forward, which is why Shake and Bazel hash content instead. The forensic discipline
  reached the same verdict from the adversarial direction and will not rest a timing claim on a
  timestamp without corroboration. And the cloud-sync work shows the failure does not require an
  adversary at all — routine collection mutates the metadata. On authorship the argument does not even
  need evidence: there is no author field to be unreliable about, so every authorship claim from mtime
  is an inference from temporal co-occurrence, which is exactly the inference the 09-05 sweep already
  falsified here. A day reconstructed this way is therefore not a lower-fidelity transcript; it is a
  record of when the filesystem was last written to, being read as a record of who did what and when.
  The 22:00 batch across sixty files, including every self-awareness register, is what that error looks
  like when it happens all at once — and if it can happen at that scale in one instant, it is happening
  at smaller scales continuously and invisibly.
  What would need to be true for C2A2 to be safe: The vault would have to be a strictly local tree with
  no sync, no backup agent, no indexer, no editor that rewrites files on open, no batch formatting or
  linting, and no restore events — and every write would have to be made by exactly one agent whose
  identity is recoverable from something other than the timestamp. Under those conditions mtime is a
  decent proxy for edit time, though still not for authorship. None of those conditions appear to hold
  here.
  How to test: Cheap and decisive, in-house. Record a content hash for every file in the vault now, and
  again after the next daily run. Then compare three sets: files whose mtime changed, files whose hash
  changed, and their intersection. The fraction of mtime-changed files with unchanged content is the
  false-positive rate of every "Changes Detected" line the changelog has ever printed. Run it again
  across the 2026-09-07 22:00 batch specifically, using any pre-batch snapshot or backup: if the ~60
  files' hashes are unchanged, the batch was a machine event and every register that recorded it as a
  day of work is wrong in a way that can be quantified. Separately, for authorship: take a sample of
  files whose authorship is independently known from transcripts, and check what fraction would be
  attributed correctly by nearest-run-in-time from mtime alone.

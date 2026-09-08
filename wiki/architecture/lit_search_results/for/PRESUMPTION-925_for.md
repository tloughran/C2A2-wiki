SEARCH-FOR-PRESUMPTION-925:
  Date searched: 2026-09-08
  Original item: PRESUMPTION-925
  Original statement: [inferred] A day reconstructed from file mtimes and agent run-reports has the same
    evidential standing as one read from session transcripts; mtime is a reliable authorship and timing
    signal.
  Routed question: How reliable is filesystem mtime as evidence of authorship and of the time of
    substantive change, in the presence of sync, backup and indexing processes? 15a searches for the
    contexts in which mtime IS a validated proxy.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-925
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from an inconsistency between two claims held by the same layer on the same day —
        the 2026-09-07 18:40 Cowork→Chat run note read against ASSUMPTION-1276 (mtime is NOT an
        authorship signal in this repo) and against the 22:00 mass-mtime batch across ~60 files.
      15a: Searched for supporting literature (2026-09-08), FOR direction only.
    Current status: PARTIALLY-SUPPORTED (timing limb only); NO-SUPPORT-FOUND (authorship limb)

  Supporting evidence found: Partial

  Note on structure: the presumption bundles two distinct claims, and the literature separates them
    cleanly.
    LIMB A (TIMING) — mtime is a reliable signal of the time of substantive change.
    LIMB B (AUTHORSHIP) — mtime is a reliable signal of WHO made the change.
    LIMB C (EVIDENTIAL PARITY) — an mtime-reconstructed day has the same standing as a transcript-read
      day.
  I found real support for A under stated conditions, none for B, and none for C.

  Sources (LIMB A — timing):
    1. Pennekamp, J., Lohmöller, J., Schütte, D., Loos, J., Henze, M., 2026. "Hidden Secrets in the
       arXiv: Discovering, Analyzing, and Preventing Unintentional Information Disclosure in Source
       Files of Scientific Preprints." arXiv:2604.20927 (RWTH Aachen COMSYS).
       [VERIFIED: authors, title, arXiv id and scope via arxiv.org/abs listing and the RWTH COMSYS
       publication page; §6.2.2 read verbatim from arxiv.org/html/2604.20927 this run] — The strongest
       FOR evidence located. Corpus: ~2.7 million arXiv submissions, 93% of all preprints to December
       2025. Verbatim from §6.2.2: "72 % of submissions carry modification timestamps within one hour
       (35 % within five minutes) before arXiv-recorded submission timestamps," and "For creation times,
       we observe wide ranges, with 83 % of submissions indicating creation dates more than 180 days
       before submission, reflecting long-term authoring processes." This is an mtime distribution
       validated against an *independent, authoritative* event clock (the arXiv submission record), at
       very large n. It is direct empirical evidence that mtime tracks real authoring activity closely
       in the majority of cases, and that mtime and creation time carry different and separable signals.
    2. Agrawal, N., Bolosky, W.J., Douceur, J.R., Lorch, J.R., 2007. "A Five-Year Study of File-System
       Metadata." Proceedings of USENIX FAST'07; also ACM Transactions on Storage 3(3), Article 9.
       [VERIFIED: authors, affiliations, title, venue, and the >60,000-Windows-filesystem scope via the
       USENIX FAST'07 conference page and the Microsoft Research publication record retrieved this run;
       the ToS 3(3) art. 9 placement from the ACM DL listing. FULL TEXT NOT READ — LISTING-LEVEL ONLY]
       — Annual metadata snapshots from >60,000 file systems over five years, with "file age" as one of
       the reported measured quantities. Weight: empirical precedent that mtime is treated, in the
       systems-measurement literature, as a usable population-level proxy for last-write time at very
       large scale. CLAIM RESTING ON THIS SOURCE: population-level usability only. It does NOT support
       per-file inference, which is what C2A2 does.
    3. Forensic timeline-analysis practice: modification time as a comparatively reliable member of the
       MACB set. Sources consulted: Thierry, A. and Müller, T., 2022, "A systematic approach to
       understanding MACB timestamps on Unix-like systems," Forensic Science International: Digital
       Investigation (DFRWS EU 2022), sciencedirect.com/science/article/pii/S2666281722000075.
       [VERIFIED: title, venue (DFRWS EU 2022 / FSI:DI) and the DFRWS-hosted PDF via dfrws.org and
       ScienceDirect listings retrieved this run. AUTHOR ATTRIBUTION: the search summary attributes the
       paper to Thierry and Müller and explicitly corrects my initial guess of Nordvik & Axelsson; I did
       not open the paper to confirm the byline. FULL TEXT NOT READ — LISTING-LEVEL ONLY] — Plus
       practitioner literature retrieved this run stating that M and B times are the more reliable
       members of the MACB set for establishing file activity, while access time is historically
       unreliable. Weight: WEAK. This supports "mtime is the best of the filesystem timestamps," which
       is a much weaker claim than "mtime is reliable," and the Thierry & Müller paper's own headline
       finding cuts against parity — see Caveat (b).
    4. Clausen, L., 2004(?). "Concerning Etags and Datestamps."
       [VERIFIED: title only, via a ResearchGate record retrieved this run. YEAR, VENUE, AUTHOR FORENAME
       AND PAGE DETAILS NOT VERIFIED — I am not inventing them. FINDING IS SEARCH-SUMMARY LEVEL ONLY —
       WEAK] — Experimental study on a few million Danish web pages reporting that the best archiving
       strategy is to download whenever the ETag is missing and otherwise download only when
       Last-Modified indicates change — i.e. the datestamp is good enough to act on when no stronger
       signal exists. Weight: analogous, weak, and partially self-undermining, since the same search
       surfaced the contrary general statement that Last-Modified "is not reliable in general."

  Sources (LIMB B — authorship): NONE FOUND.

  Strength of support: Weak-to-Moderate on the timing limb (one strong large-n source, three weak ones);
    None on the authorship limb; None on the evidential-parity limb.

  Summary: The timing limb of PRESUMPTION-925 has one genuinely strong piece of support. Pennekamp et
  al. (2026), across ~2.7M arXiv submissions, found that 72% of submissions carried modification
  timestamps within one hour of an independently recorded submission event and 35% within five minutes
  — mtime validated against an external clock, at scale, and behaving as a close proxy for the time of
  real authoring work. The systems literature (Agrawal et al. 2007) treats mtime as a usable population-
  level measure of file age, and forensic practice treats modification time as among the more dependable
  members of the MACB set. So "mtime tracks the time of substantive change, most of the time, in
  ordinary conditions" is defensible. Nothing found supports the other two limbs. I found no study, in
  forensics, in mining-software-repositories, or in archival science, validating mtime as a signal of
  WHO made a change — filesystem mtime simply does not carry an actor field, and no source I located
  proposes reconstructing one from it. And I found nothing supporting evidential parity between metadata
  reconstruction and a primary record: the forensic literature's consistent position, even in its
  supportive passages, is that timestamps must be corroborated against logs and system events rather
  than read alone.

  Caveats:
  (a) THE STRONGEST SOURCE CONTAINS ITS OWN COUNTER-CASE, AND IT IS C2A2'S CASE. Pennekamp et al.
      §6.2.2 also report, verbatim, that they "excluded commonly reused templates, as we only found 38 %
      of them carrying unique timestamps, whereas most timestamps seem to originate from template
      providers." That is precisely the mass-mtime-batch failure 14b observed on 2026-09-07 at 22:00:
      files whose mtimes derive from a copying/provisioning process rather than from the author. The
      72% figure holds for files the author actually edited; it does not hold for files that arrived by
      copy. C2A2's registers are exactly the second kind on the day in question.
  (b) THE FORENSIC SOURCE CUTS AGAINST PARITY. Thierry & Müller's reported headline finding is that
      POSIX does not fully determine Unix-family timestamp behaviour and that Linux, FreeBSD, OpenBSD
      and macOS diverge from the specification and from one another. Supportively read, this means mtime
      behaviour is documentable and therefore interpretable — but only once you have established which
      stack produced it. Read plainly, it is a reason not to treat mtime as self-interpreting evidence.
  (c) THE 28% TAIL IS THE OPERATIVE NUMBER FOR C2A2. A signal correct 72% of the time within an hour is
      a good population statistic and a poor basis for a per-day reconstruction that names specific
      files as evidence of specific work. The presumption asserts *parity* with transcripts; a 72%
      one-hour concordance is not parity with a primary record, it is a lossy proxy.
  (d) SYNC, BACKUP AND INDEXING WERE NOT ADDRESSED BY ANY SUPPORTIVE SOURCE FOUND. The question 14b
      routed names these explicitly. Nothing in the FOR direction addresses cloud-sync-induced mtime
      churn; searches surfaced forensic work on OneDrive timestamp behaviour across NTFS and ext4, which
      I did not retrieve, and which is likely to be 15b's material rather than mine.
  (e) SEARCH SCOPE. Preliminary — broader search recommended. Four queries in this direction. Not
      covered: mining-software-repositories work on timestamp-based authorship attribution error rates
      (searched, nothing supportive found — see NOVELTY-FLAG); OAIS/archival provenance standards;
      empirical mtime-vs-content-hash divergence in Dropbox/iCloud/Drive trees; build-system literature
      on mtime-based rebuild correctness (Mokhov et al., "Build Systems à la Carte"), which was not
      searched and which is the most likely remaining source of FOR evidence on the timing limb.

  Recommendation: PARTIALLY-SUPPORTED
    (timing limb: PARTIALLY-SUPPORTED, Weak-to-Moderate, with an explicit exclusion for copied/
     provisioned files that matches the observed C2A2 failure;
     authorship limb: NO-SUPPORT-FOUND;
     evidential-parity limb: NO-SUPPORT-FOUND.)

  NOVELTY-FLAG:
    Item: PRESUMPTION-925, authorship limb
    Searched: four queries across digital-forensics timestamp reliability, MACB semantics on Unix-like
      systems, large-scale filesystem metadata measurement, timestamp-based authorship attribution, and
      Last-Modified reliability in web archiving.
    Finding: No existing literature was found that validates filesystem mtime as an authorship signal.
      This is not a gap in the sense of "unstudied" — it appears to be a gap in the sense of "no one has
      proposed it," because mtime records no actor. The nearest thing found (Pennekamp et al.) infers
      author *behaviour* from timestamp distributions only after author identity is already known from
      the submission record.
    Implication: This is a negative novelty finding rather than a positive one. C2A2's use of mtime as
      an authorship signal does not appear anywhere in the literature as a validated method, and the
      absence should be read as absence of warrant, not as an original contribution. It corroborates
      ASSUMPTION-1276 (which 14a recorded as SUPPORTED in-house this run) from the outside.
    Recommended status: NOVEL (in the unfavourable sense) — the authorship limb is an unwarranted
      C2A2-local practice, not a recognised method.

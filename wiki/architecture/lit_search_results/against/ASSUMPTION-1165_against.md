SEARCH-AGAINST-ASSUMPTION-1165:
  Date searched: 2026-08-25
  Original item: ASSUMPTION-1165
  Original statement: "That coverage of a source can be declared complete on a secondary channel
    when the primary channel is known unreadable — 'the PEP Lab page is the authoritative roster';
    'a real zero, not a search failure'."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1165
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Set two agents' stated zero-findings against their own stated channel failures
        in the same reports.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: Queries run 2026-08-25: single-database sufficiency and recall in systematic
    review; database coverage overlap (MEDLINE/Embase/CENTRAL/Google Scholar/Web of Science);
    grey literature and preprint capture rates; accuracy and completeness of institutional and
    author-curated publication lists; absence-of-evidence interpretation. Venues reached:
    Systematic Reviews (BMC), Journal of Clinical Epidemiology, Scientometrics, BMJ, Cochrane/
    university systematic-review methods guidance (Monash, KCL, UCL, McGill, Groningen, UCC),
    PMC. Date range: 1995–2025. Depth: COMPREHENSIVE for the information-retrieval leg;
    PRELIMINARY for the specific PEP Lab instance (I did not and could not verify the state of
    the actual PEP Lab page — this is an evidential gap, and nothing below should be read as a
    finding about that particular page). Web-search budget exhausted before a dedicated search on
    web-page decay / link rot rates for academic lab sites.

  Challenging evidence found: Yes

  Sources:
    1. Bramer, W. M., Rethlefsen, M. L., Kleijnen, J., & Franco, O. H., 2017. "Optimal database
       combinations for literature searches in systematic reviews: a prospective exploratory
       study." Systematic Reviews, 6:245. DOI 10.1186/s13643-017-0644-y
       — Direct contradiction of single-channel sufficiency. Median coverage of a single database
       was 83–91% and median recall 71–76%; neither Embase nor MEDLINE alone suffices. Any
       combination of at least two databases reached 94–99% coverage and 85–90% recall. A single
       secondary channel is therefore expected to miss roughly a quarter of relevant records.
       ABSTRACT plus PMC full text located (PMC5718002).
    2. "Searching two or more databases decreased the risk of missing relevant studies: a
       metaresearch study." Journal of Clinical Epidemiology, 2022. Article S0895-4356(22)00144-5.
       https://www.jclinepi.com/article/S0895-4356(22)00144-5/fulltext
       — Metaresearch finding that even MEDLINE + Embase + CENTRAL together did not achieve total
       recall or guarantee that systematic-review conclusions were unchanged. Authors not resolved
       (full-text fetch returned empty); title, venue and article ID verified from the publisher
       index. SNIPPET-ONLY.
    3. Bramer, W. M., Giustini, D., & Kramer, B. M. R., 2016. "Comparing the coverage, recall, and
       precision of searches for 120 systematic reviews in Embase, MEDLINE, and Google Scholar: a
       prospective study." Systematic Reviews. PMC4772334.
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4772334/
       — Quantifies channel-to-channel substitution loss across 120 reviews. Author list from the
       PMC record. ABSTRACT-ONLY.
    4. "Supplementary databases increased literature search coverage beyond PubMed and Embase."
       Journal of Clinical Epidemiology, 2025. Article S0895-4356(25)00037-X.
       https://www.jclinepi.com/article/S0895-4356(25)00037-X/fulltext
       — Recent replication of the same effect: the two largest channels still leave residual
       coverage recoverable only by adding further channels. Authors not resolved. SNIPPET-ONLY.
    5. "Accuracy of PubMed-based author lists of publications and use of author identifiers to
       address author name ambiguity: a cross-sectional study." Scientometrics, 2021.
       DOI 10.1007/s11192-020-03845-3
       — The closest analogue to the "authoritative roster" claim. Curated publication lists
       contained on average 5 articles not authored by the subject and omitted 3 that were, i.e.
       both false positives and false negatives are routine in human-curated rosters. Authors not
       resolved from snippet. SNIPPET-ONLY.
    6. Altman, D. G. & Bland, J. M., 1995. "Statistics notes: Absence of evidence is not evidence
       of absence." BMJ, 311:485. PMC2550545.
       — The canonical statement of the inferential error the claim commits: a non-finding is
       evidence of absence only if the instrument had power to detect the thing. A channel that was
       never read has zero power, so a zero across a degraded channel set is not licensed as "a
       real zero." FULL-TEXT.
    7. Cochrane / systematic-review methods guidance on grey literature and supplementary searching
       (Monash, KCL, UCL, McGill, Groningen, UCC library guides, consulted 2026-08-25).
       — Consistent guidance that finding studies must not depend solely on database searching;
       coverage of grey literature is patchy across mainstream channels; hand-searching routinely
       recovers records missed by indexed search because they are in non-indexed venues or are
       poorly/incorrectly indexed. Institutional methodological guidance, not primary research.
       FULL-TEXT (guidance pages).
    8. "Applying systematic review search methods to the grey literature: a case study examining
       guidelines for school-based breakfast programs in Canada." PMC4619264.
       — Worked case showing grey-literature material that indexed search does not surface.
       Authors not resolved. SNIPPET-ONLY.

  Challenging evidence found: Yes

  Strength of challenge: Strong

  Summary: The information-retrieval literature contradicts this assumption about as directly as a
    literature can. Bramer et al. 2017 measured exactly the quantity at issue — how much of a target
    set a single channel returns — and found median recall of 71–76% for the best single biomedical
    databases, with two or more channels needed to reach 85–90%. The 2022 Journal of Clinical
    Epidemiology metaresearch strengthens this: even three major channels together failed to
    guarantee total recall or stable review conclusions. The specific move in ASSUMPTION-1165 is
    worse than the case those studies model, because here the primary channel was not merely
    incomplete but known unreadable, so the secondary channel is not supplementing a working
    channel — it is substituting for a channel whose content is entirely unobserved. The
    "authoritative roster" step compounds it: curated publication lists have measured false-negative
    rates (Scientometrics 2021), so a lab web page is a sample of a lab's output, not its
    definition. Altman & Bland supply the inferential rule the claim violates: a zero is evidence of
    absence only in proportion to the power of the instrument that produced it, and an unread
    channel contributes no power at all.

  Specific risks: If this claim is false, every register entry derived from a degraded-channel
    search is overstated. Concretely: (a) zeros recorded as substantive findings ("there is no such
    work") when the correct entry is "not established"; (b) a systematic bias in *which* items go
    missing — records absent from a curated web page are disproportionately recent, negative,
    non-flagship, or authored by departed lab members, so the missingness is not random and the
    residual sample is skewed toward the lab's self-presentation; (c) downstream items that consume
    this zero as an input inherit an error they cannot see, because the register entry no longer
    carries the channel-failure fact that would let a later reader discount it. The
    "authoritative roster" framing is the most dangerous element, because it converts an
    incompleteness into a definition and thereby makes the gap unrecoverable by later search.

  Mitigations available:
    - Record channel state alongside the finding. PRISMA 2020 already requires "reports sought for
      retrieval" and "reports not retrieved" to be reported separately from exclusions; adopting the
      same two-field structure preserves the distinction the claim collapses
      (https://www.prisma-statement.org/prisma-2020-flow-diagram).
    - Never certify completeness from one channel. Minimum-two-channel rule with an explicit recall
      expectation of ~85–90%, per Bramer et al. 2017 (DOI 10.1186/s13643-017-0644-y).
    - Downgrade the verdict vocabulary: replace "a real zero" with "no records retrieved on
      channels X, Y; channel Z unreadable" — an honest statement that carries its own limitation
      (Altman & Bland 1995, BMJ 311:485).
    - Treat a curated roster as one channel, cross-checked against an index (PubMed/OpenAlex/Google
      Scholar), given measured false-negative rates in curated author lists (Scientometrics 2021).
    - Retry or route around the blocked primary channel before closing the item; if it cannot be
      reopened, mark the item BLOCKED rather than ZERO.

  STEELMAN:
    Item: ASSUMPTION-1165
    Strongest counterargument: The claim substitutes a channel of unknown and probably low recall
      for one of unknown content and then reports the result at full confidence. The measured
      numbers make this untenable: the best single indexed biomedical channels return only about
      three-quarters of the target set, and a hand-curated lab page is not an indexed channel at all
      — it is a self-presentation artefact with documented false-negative rates and no update
      guarantee. The failure is not merely a loss of recall, it is a loss of *known* recall: because
      the primary channel was never read, there is no way to estimate what fraction of the target
      set the secondary channel captured, so the confidence attached to "a real zero" has no
      basis at all. Calling the roster "authoritative" makes the error self-sealing, because it
      redefines the missing records out of existence rather than recording them as unretrieved.
    What would need to be true for C2A2 to be safe: The claim would be defensible if (1) the
      secondary channel were demonstrably a superset of the primary for the specific target class
      — e.g. if the lab page were contractually maintained as the complete roster and had been
      independently spot-checked against an index on the relevant date; (2) the target class were
      one where non-listing is genuinely dispositive (membership in a named lab, say, rather than
      existence of a publication); and (3) the finding were scoped to that channel in the register
      text rather than asserted as a fact about the world. Absent (1), a two-channel minimum is
      required before any completeness claim.
    How to test: Directly and cheaply. Take the specific roster page, and independently query one
      or two indexed channels (PubMed/OpenAlex/Google Scholar) for the same lab and date window.
      Compute recall of the roster against the union. If roster recall is below ~0.9, the
      "authoritative roster" claim is falsified for this instance and every zero derived from it
      must be re-labelled. The same test is repeatable for any future roster-based coverage claim
      and would give the pipeline a calibrated discount factor rather than a binary.

  Recommendation: CHALLENGED

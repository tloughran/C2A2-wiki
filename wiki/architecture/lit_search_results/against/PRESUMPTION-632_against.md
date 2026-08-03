SEARCH-AGAINST-PRESUMPTION-632:
  Date searched: 2026-08-03
  Original item: PRESUMPTION-632
  Original statement: That withdrawing reliance on an unverifiable citation is equivalent
    to withdrawing the citation.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-632
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by comparing a run report against the flag file it produced
           (origin ASSUMPTION-652)
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Hsiao & Schneider, 2021. "Continued use of retracted papers: Temporal trends in
       citations and (lack of) awareness of retractions shown in citation contexts in
       biomedicine." Quantitative Science Studies 2(4):1144 — of 13,252 post-retraction
       citation contexts, only 722 (5.4%) acknowledged the retraction. The correction
       does not travel: 94.6% of downstream uses are unaware.
    2. Why do some retracted articles continue to get cited? 2024. Scientometrics
       10.1007/s11192-024-05147-4 — retraction status frequently fails to change citation
       behaviour at all; the marker does not reach the reader.
    3. Teixeira da Silva, 2025. "The Citation of Retracted Papers and Impact on the
       Integrity of the Scientific Biomedical Literature." Learned Publishing
       10.1002/leap.1667 — bibliographies are not checked against retraction status at
       publication; there is no automatic reaper.
    4. Case analysis reported in Illinois News Bureau (2021) — retraction unmentioned in
       96% of 112 direct post-retraction citations.

  Strength of challenge: Strong

  Summary: The literature refutes the equivalence squarely and quantitatively. The status
  of a source and the reliance one author places on it are independent variables
  downstream: an invalidated source left in a bibliography continues to be read, reused
  and propagated at essentially undiminished rates, and the invalidation is visible to
  fewer than one downstream reader in twenty. The mechanism the literature identifies —
  readers trusting the citing author's judgement rather than re-checking the source —
  applies with full force in C2A2, where the downstream readers are agents that perform
  no verification pass at all and have no retraction-checking step.

  Specific risks: An unlocatable figure remains in the Critical flag's literature basis,
  unmarked, while the argument that rested on it has been quietly re-based. Any agent that
  later reads that flag inherits the bad figure with no signal, and may re-cite it into a
  further artifact. Because C2A2's registers are append-only and cross-referencing, the
  propagation surface is larger than a journal bibliography, not smaller.

  Mitigations available: Yes, and trivially cheap relative to the risk. The bibliometric
  literature's own recommended remedy — mark the record rather than rely on the reader —
  maps directly onto a one-line edit: annotate the citation in place as UNVERIFIABLE with
  the date and the reason, rather than silently ceasing to rely on it. This is strictly
  more informative than removal, since it preserves the audit trail of the error.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-632
    Strongest counterargument: The presumption conflates two different acts with two
    different audiences. Re-basing the argument fixes the argument for its author.
    Withdrawing the citation fixes the record for everyone else. Only the first was done.
    The strongest form of the objection is that the omission is not neutral but actively
    misleading: a citation that sits in a "literature basis" section carries an implicit
    warrant from the system that it was checked, and leaving it there after discovering it
    is unverifiable converts an honest error into a standing false assertion. The
    retraction literature's central finding is that the burden cannot be shifted to the
    reader — 94.6% of them will not notice — so a system that leaves the marker off is
    choosing, in effect, to propagate.
    What would need to be true for C2A2 to be safe: that no other agent or human ever
    reads the flag's literature basis, or that every downstream reader independently
    verifies every citation. Neither holds; the flag is Critical and is written to be read.
    How to test: grep the vault for downstream re-citations of the unverifiable figure.
    A single hit converts this from a risk to a realised defect.

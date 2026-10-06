SEARCH-AGAINST-PRESUMPTION-1019:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1019
  Original statement: [inferred] That legal and archival authority standards — FRE 803(6), Restatement (Third) of
    Agency §2.03, UETA §14, diplomatics' author/writer distinction — transfer to an internal wiki's provenance
    markers without an argument about jurisdiction, scale, adversarial setting, or the absence of a tribunal.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1019
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the 999 disposition's sources against the transfer conditions it did not state
      15b: Searched for challenging literature; found the home-domain sources themselves carry conditions
           (regular activity, custodian/tribunal, juridical acts, third-party reliance) that a single-designer
           wiki does not meet; found no direct literature on transferring them to internal wiki provenance;
           strength: Moderate
    Current status: PARTIALLY-CHALLENGED

  Search scope: PRELIMINARY — broader search recommended (7 sources checked at source or via fetched summary;
    no direct transfer-critique literature located; 2 fetches failed, see Limits).

  Challenging evidence found: Partial

  Sources:
    1. Federal Rules of Evidence, Rule 803(6), "Records of a Regularly Conducted Activity" (Cornell LII text,
       https://www.law.cornell.edu/rules/fre/rule_803; fetched 2026-10-05). The exception requires a record made
       at or near the time by someone with knowledge, kept in a regularly conducted activity of an organization,
       made as a regular practice, shown by a custodian or qualified witness (or Rule 902(11)/(12) certification),
       and not undermined by an opponent showing lack of trustworthiness. Conditions (A)-(E) presuppose a
       tribunal, a witness/certifier and an opponent; an agent's watch-list note meets (A)-(C) at most partially
       and (D)-(E) not at all. The "trustworthiness" clause is adversary-triggered, not a free-standing property.
    2. Restatement (Third) of Agency §2.03 (American Law Institute, 2006; text via opencasebook.org excerpt,
       https://opencasebook.org/casebooks/16481-selected-excerpts-of-restatement-of-agency-third-professor-randle-pollard/as-printable-html/).
       Apparent authority is power to affect "a principal's legal relations with third parties" when a third
       party reasonably believes the actor has authority and that belief is "traceable to the principal's
       manifestations." It presupposes a principal, a third party who relies, and legal relations at stake; none
       of these is present in an internal wiki marker with no external relying party.
    3. Uniform Electronic Transactions Act §14 "Automated Transaction" (as enacted, W. Va. Code §39A-1-14,
       https://code.wvlegislature.gov/39A-1-14/). Concerns contract formation by electronic agents; the terms
       are "determined by the substantive law applicable to it." It is a rule about contract validity and is
       jurisdiction-dependent (state enactments); it says nothing about attribution within a record-keeping
       system. Its home function (binding parties) is not the function of a provenance marker.
    4. W3C, PROV-DM: The PROV Data Model (https://www.w3.org/TR/prov-dm/; fetched 2026-10-05). Delegation
       (actedOnBehalfOf) is "the assignment of authority and responsibility to an agent ... to carry out a
       specific activity ... while the agent it acts on behalf of retains some responsibility," and is "intended
       to be broad, including contractual relation, but also altruistic initiative by the representative agent."
       PROV deliberately models attribution broadly and neutrally; it does not import legal authority standards,
       which cuts against treating legal tests as the governing standard for provenance markers.
    5. Duranti, L. & MacNeil, H., 1996. "The Protection of the Integrity of Electronic Records: An Overview of
       the UBC-MAS Research Project." Archivaria 42: 46-67 (https://archimuse.com/erecs97/ARCH421.HTM).
       Diplomatics treats records as evidence of juridical acts ("dispositive" or "probative"), with author
       (person with authority to issue), addressee and writer as personae. The authors found the principles
       valid for electronic records only with significant adaptation, since the components "exist separately"
       and must be made explicit. Author/writer presupposes juridical acts and an issuing authority; a wiki note
       is not obviously a juridical act. Adaptation was itself needed for one domain shift (paper to electronic).
    6. ISO 15489-1:2016, Information and documentation — Records management, Part 1 (summary via
       https://iteh.es/catalog/standards/iso/baf32a1d-182a-428d-aca9-74f0e33d01a7/iso-15489-1-2016; secondary).
       Frames records as evidence of business activity, with management decisions resting on "analysis and risk
       assessment of business activities, in their business, legal, regulatory and societal contexts." Its
       authenticity criterion (created "by the agent purported to have created it") is attribution, not
       authorisation, and is risk- and context-scaled. This supports the item: the records standard itself makes
       the legal/regulatory context a parameter rather than a constant.
    7. Kenneally, E., 2003. "Evidence Enhancing Technology." ;login: (USENIX), (https://www.usenix.org/system/files/login/articles/1160-kenneally.pdf).
       Argues that "the application of the standard to log evidence is unsettled" and that courts rely on witness
       testimony about system function rather than technical integrity measures. Shows that legal evidentiary
       standards fit machine-generated logs poorly even in their home (tribunal) setting; a fortiori for a
       non-tribunal setting.

  Strength of challenge: Moderate
    (Disanalogy is well supported by the sources' own stated conditions. But no source was found that directly
    tests or criticises transfer of these standards to internal wiki provenance, and the challenge is derived by
    comparing conditions, not by an empirical failed transfer. Several sources are secondary or summarised.)

  Summary: Each cited standard carries explicit application conditions: FRE 803(6) requires regular activity,
    a custodian or certifier and an opponent who can contest trustworthiness; Agency §2.03 requires a principal,
    a relying third party and legal relations; UETA §14 requires contract formation under state law; diplomatics
    requires juridical acts and an issuing authority. A single-designer estate with no adversary, no relying third
    party and no fact-finder meets few of these. PROV-DM and ISO 15489 show that provenance and records
    practice treat the legal context as a scalable parameter, and Kenneally shows legal standards fit machine
    logs poorly even in court. What the literature does not show is that the transfer fails, only that it is
    unargued and condition-laden. The "one field" conclusion of REVISE-476 may survive on functional grounds,
    but its HIGH weight cannot borrow home-domain authority without an argument.

  Specific risks: (1) REVISE-476's HIGH weight and the withdrawal of 14b's "formalised three times over" novelty
    flag rest on authority that does not carry over, so the novelty flag may have been wrongly withdrawn.
    (2) Legal terms (authority, apparent authority, business record) may import connotations (liability,
    reliance, trustworthiness presumption) that mislead readers of provenance markers. (3) Jurisdiction-bound
    sources (UETA state enactments, US-only FRE) are generalised to a non-jurisdictional setting.

  Mitigations available (reported, not recommended): re-cite the sources as analogy with named conditions rather
    than as authority; read the cited sources at primary level (this search read FRE, PROV-DM and §2.03 text but
    only summaries of ISO 15489 and Duranti/MacNeil); state which transfer conditions the estate satisfies and
    which it does not; ground the weight in functional evidence (audit-log attribution literature) instead.

  Limits of this search: Duranti 2010 (Emerald) fetch returned a CAPTCHA page and was not read; DOJ computer
    records manual chapter (computer-generated vs computer-stored records, hearsay) could not be read. The
    human-declarant requirement under FRE 801 (machine output is not a "statement") was not verified at source
    and is NOT cited as a source. CSCW/organisational-memory literature on authorship in shared logs was not
    searched in depth. No claim above relies on the 15a ("for") output, which was not read.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1019
  Strongest counterargument: The legal and archival standards cited are not free-floating tests of "who
    authored what"; they are mechanisms for allocating evidentiary or legal consequences between parties under a
    tribunal. FRE 803(6) works because a custodian can be cross-examined and an opponent can attack
    trustworthiness; Agency §2.03 works because a third party relied on a principal's manifestation; UETA §14
    works because state law then supplies contract terms. Strip away the tribunal, the adversary and the relying
    party and what is left is a vocabulary, not a standard. Using that vocabulary to assign HIGH weight to a
    disposition, and to retire a novelty flag, borrows authority the sources only hold inside their institutions.
    The estate's own l.2666 premise (a claimed equivalence is not legitimate merely because it is statable)
    applies to this very transfer.
  What would need to be true for C2A2 to be safe: The cited standards are used only as analogies whose
    conditions are named; REVISE-476's conclusion stands on a functional argument (provenance markers do one job
    whichever vocabulary is used) independent of legal authority; and the novelty flag is re-examined without
    leaning on home-domain authority.
  How to test: (1) For each source, tabulate its application conditions against the estate's actual setting and
    mark met / partly met / unmet. (2) Re-derive REVISE-476 with the legal sources removed and see whether HIGH
    weight survives. (3) Read ISO 15489-1 and Duranti (2010) at primary level.

SYSTEMIC-RISK-FLAG: none raised from this item alone. Candidate only: the same borrowed-authority pattern
  appears to link PRESUMPTION-999 and the l.3150/3242/3498 "ANALOGICAL and contested" transfers named in the
  pre-check; I did not read those items, so no flag is filed.

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1019
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Moderate
  Key source: Federal Rules of Evidence, Rule 803(6) (conditions A-E presuppose a custodian, an opponent and a tribunal); with Restatement (Third) of Agency §2.03 and Duranti & MacNeil 1996, Archivaria 42
  Specific risk: REVISE-476's HIGH weight and the withdrawal of the novelty flag borrow authority from sources whose application conditions (tribunal, adversary, relying third party, juridical act) the estate does not meet.
  Summary: Each cited standard carries explicit conditions the estate does not satisfy, and no source argues the transfer; the disanalogy is derived, not demonstrated. Search scope preliminary.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1019_against.md

  SYSTEMIC-RISK: none flagged (candidate link to PRESUMPTION-999 noted, not verified).
  QUEUE STATUS: PRESUMPTION-1019 [SEARCHED-15b: 2026-10-05] — PARTIALLY-CHALLENGED, Moderate; awaiting 15a and 14b reconciliation.

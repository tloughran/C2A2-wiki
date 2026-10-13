SEARCH-FOR-ASSUMPTION-1766:
  Date searched: 2026-10-11
  Original item: ASSUMPTION-1766
  Original statement: The lit pipeline took 15b's systemic-risk flag ("adding five new correction rules to an
    unattended pipeline could create clutter nobody reads") as a limit on the size of fixes: five items produced two
    premises and two flags, not five new processes. Question: Does consolidating corrective rules (fewer, broader
    rules) reduce alert/rule fatigue in unattended or lightly-supervised pipelines?

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-1766
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the lit pipeline's stated rationale for capping the number of new rules (citing 15b's
        "clutter nobody reads" systemic-risk flag); queued 2026-10-10
      15a (2026-10-11): 3 web searches, 1 fetch (FRA eLibrary page for Ranney & Nelson; succeeded, abstract). Found
        support that rule proliferation lowers compliance ("safety clutter"; railroad rules overlap), that alarm-volume
        reduction is the target of most alarm-fatigue interventions, and one small study where shortening a checklist
        from 31 to 10 items raised compliance. No study tests rule consolidation in an unattended software pipeline.
    Current status: PARTIALLY-SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) alarm fatigue / reducing alert numbers, systematic reviews;
    (b) rule proliferation in safety management; (c) checklist length and compliance. 1 fetch: FRA eLibrary abstract
    page for Ranney & Nelson (succeeded; abstract only, PDF not opened).

  Supporting evidence found: Partial

  Sources:
    1. Ranney, J. & Nelson, C. "Impacts of Participatory Safety Rules Revision in U.S. Railroad Industry: An
       Exploratory Assessment." Transportation Research Record 1899 (FRA report TRR1899-20). [fetched, abstract]
       "Voluminous and overlapping rules might contribute to poor compliance because of confusion and disagreement about
       which rules are to be followed." Participatory revision showed a significant incident-rate effect at one carrier;
       declines at two others could not be attributed with confidence. Relevance: direct statement of the
       proliferation-harms-compliance mechanism; outcome evidence for consolidation is mixed.
    2. RMIT SHINE "Safety clutter" position paper (Rae, Provan, Weber, Dekker line of work). [search-result; authors not
       verified] Names "safety clutter": rules added after incidents, paperwork and forms nobody reviews; argues some
       safety activities impede safety. Relevance: near-exact analogue of "clutter nobody reads".
    3. Alarm-fatigue systematic reviews: Winters et al. 2018 (Critical Care Medicine); Kane-Gill et al. 2017
       "Technologic Distractions" Parts 1-2; Chromik et al. 2022 (69 publications). [search-result] Interventions that
       cut total or false alarms mostly succeed in cutting volume; Kane-Gill lists prioritisation and "multipart rules
       instead of simple alerts" (i.e., consolidation). Two studies found slower nurse response at higher alarm counts.
       Relevance: theoretical and partial empirical support. Reviewers note alarm fatigue is rarely measured directly.
    4. Urology checklist study (UK; via BJMSU/SAGE search result). [search-result] Replacing a 31-question checklist
       with 10 questions raised compliance on those items from 53% to 92% (p<0.05). A separate study found locally
       modified surgical checklists grew (33.5 vs 28 items) by accretion. Relevance: shorter rule sets, better uptake;
       rule sets tend to grow unless capped.

  Strength of support: Moderate for "proliferation harms attention/compliance"; Weak for "consolidation fixes it".

  Summary: Safety-management and clinical-alarm literatures agree that volume and overlap of rules or alerts degrade
    compliance and attention, and the term "safety clutter" describes exactly the risk 15b flagged. Consolidation
    (multipart rules, prioritisation, shorter checklists) is a recommended remedy, and one small checklist study shows
    a large compliance gain from cutting items. Evidence that consolidation itself improves outcomes is thin: the
    railroad intervention showed effects at one of three carriers, and alarm reviews note alarm fatigue is seldom
    measured directly. The C2A2 choice (2 premises + 2 flags instead of 5 processes) is consistent with this guidance.

  Caveats: (i) All evidence concerns human workers; in C2A2 the "reader" is partly agents and partly one human
    reviewer, so the mechanism (attention, confusion) transfers only to the human end. (ii) Consolidation can drop
    critical items; the checklist literature stresses keeping essential items. (iii) Some sources (Dekker, Mercatus)
    are advocacy-leaning. (iv) Unattended-pipeline context not studied.

  NOVELTY flag: partial. The principle is established; its application to rule-count caps in an unattended multi-agent
    pipeline was not found.

  Recommendation: PARTIALLY-SUPPORTED (Moderate). Preliminary search; broader search recommended (CDS alert
    consolidation and override rates; ISA-18.2 alarm rationalisation in process industries).

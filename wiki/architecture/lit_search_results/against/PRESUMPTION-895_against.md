SEARCH-AGAINST-PRESUMPTION-895:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-895
  Original statement: [inferred] Voluntary self-report suffices as the detector of register damage.
  Generalizable limb searched: Whether voluntary self-attestation can function as a detective
    control — what assurance frameworks accept as detection evidence, and what the measured
    under-reporting rates are in mature voluntary incident-reporting systems.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run (2 Pass 1 + 1 Pass 2); no
    full-text reads. The healthcare under-reporting limb returned strong peer-reviewed sources
    including an NEJM study; the aviation limb returned only qualitative barrier descriptions with
    no quantified under-reporting fraction, so that limb is under-searched.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-895
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the absence of any automated or independent check on register integrity —
        damage is discovered only if an agent notices and volunteers it. Flagged Risk: Critical.
      15b: Searched for challenging literature (2026-08-31)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Bates, Levine, Salmasian, et al., 2023. "The Safety of Inpatient Health Care." New England
       Journal of Medicine, 388:142-153 (DOI as listed: 10.1056/NEJMsa2206117). — Peer-reviewed
       measurement of adverse events by systematic record review rather than by voluntary report.
       Cited in the search results for the finding that many U.S. hospitals relying solely on
       voluntary reporting produce "substantial undercounting and, in some cases, misleading reports
       of zero harm." The zero-harm point is the sharpest form of the challenge: a voluntary-only
       detector does not degrade gracefully — it reports clean.
    2. Nuckols, Bell, Liu, Paddock & Hilborne, 2007. "Rates and types of events reported to
       established incident reporting systems in two US hospitals." Quality & Safety in Health Care
       (PMC2464990). — Compared voluntary incident reports against independently measured event
       rates in two hospitals with *established* reporting systems; the search result reports a
       measured adverse-event incidence roughly 20 times higher than voluntary reporting indicated.
       An order-of-magnitude sensitivity shortfall in a mature, resourced, professionally staffed
       reporting regime.
    3. AHRQ Patient Safety Network (PSNet). "Reporting Patient Safety Events" and "Strategies and
       Approaches for Investigating Patient Safety Events" (primers). — State that adverse events
       and near misses are underreported, and that when record review and direct observation are
       performed, incident reports are found to have captured only a small percentage of events and
       "may not reliably identify serious events." Note the second clause: under-reporting is not
       uniform across severity, so the assumption that serious damage would surely be noticed and
       reported is specifically contradicted.
    4. Adverse drug event reporting study in AHRQ "Advances in Patient Safety: From Research to
       Implementation," Volume 1 (NCBI Bookshelf, NBK20453). — Reports voluntary incident reporting
       yielding much lower ADE rates than other detection methods, with considerable variation
       between units and service areas. The variance finding matters: voluntary detection rates
       differ by local culture and workload, so the detector's sensitivity is not a stable property.
    5. PCAOB / SOC 2 evidence practice, as characterised across the search results (Konfirmity,
       "SOC 2 Evidence Requirements"; Zip Security, "SOC 2 Compliance Checklist: 8 Controls Auditors
       Test"; AWS Audit Manager SSAE-18 SOC 2 documentation). — Consistent practitioner reporting
       that auditors do not accept self-attestations as evidence of control effectiveness: system
       exports, logs, records and test results carry weight where "screenshots or self-attestations"
       do not, and detective controls must be "supported by actual monitoring evidence and logs
       rather than just self-reported compliance." Secondary/practitioner sources characterising the
       standards rather than the standards themselves.
    6. ASHRM. "Value of Incident/Event Reporting" (PDF, 2021). — Cited for the barrier taxonomy:
       organisational culture of blame, fear of repercussions, documentation burden, inadequate time,
       lack of clarity on when and how to report. Relevant because several of these have direct
       analogues for an agent operating under time and context pressure with an incentive toward
       task completion.

  Strength of challenge: Strong

  Summary: This is the strongest challenge in my batch, and it is supported from two directions that
    do not depend on each other. Normatively, assurance frameworks do not count self-attestation as
    a detective control at all — detection must be evidenced by logs, exports, and test results
    produced independently of the party being assessed, and a control whose only output is the
    assertion of the controlled party is not a control in the technical sense. Empirically, the
    healthcare literature supplies what is effectively a natural experiment on exactly this design:
    mature voluntary reporting systems, staffed by trained professionals with explicit ethical
    duties and institutional support, detect on the order of one event in twenty. That is the
    *ceiling* for a voluntary regime under favourable conditions, and C2A2's conditions are less
    favourable, not more — an agent has no persistent stake in the register's long-run integrity,
    is under completion pressure, and by PRESUMPTION-894 may not reliably know what it did in the
    first place. The most consequential finding is the failure signature: a voluntary-only detector
    does not report degraded confidence when it is failing, it reports zero incidents. Silence is
    the shared output of "nothing went wrong" and "detection is not working," and nothing in the
    current arrangement can distinguish them. That is what makes the Critical risk rating
    appropriate rather than merely High: the presumption is not just probably false, it is
    self-concealing, and every quiet cycle strengthens misplaced confidence in it.

  Specific risks: If voluntary self-report is not a sufficient detector, register damage accumulates
    undetected and its discovery is deferred to some future moment when a downstream consumer
    happens to trip over it — by which point the damage may be many runs old, past snapshot
    retention, and no longer attributable to a specific cause. The compounding risk is evidential:
    a long run of clean cycles will be read as evidence that the register is healthy, when it is
    equally consistent with the detector being blind. Every mitigation elsewhere in the pipeline
    that assumes damage would be noticed inherits this failure. Note the direct interaction with
    PRESUMPTION-894: the detector is voluntary *and* its input channel is unreliable, so the two
    failures multiply rather than back each other up.

  Mitigations available: (a) Add at least one non-voluntary, automated integrity check that runs
    regardless of whether any agent reports anything — file counts, byte sizes, hash manifests,
    schema/parse validation, or a link-integrity sweep across the register; (b) instrument the
    detector so that "no report" and "check ran and passed" are distinguishable states, which alone
    removes the silence ambiguity; (c) adopt the record-review pattern from the safety literature —
    periodically sample register entries and verify them against source artefacts, which is how the
    20x gap was measured in the first place and would give C2A2 an estimate of its own detection
    sensitivity; (d) reduce reporting friction and any completion-pressure disincentive, which the
    barrier literature identifies as suppressors, while recognising that this improves a voluntary
    channel rather than replacing it; (e) treat voluntary reports as a supplement that adds
    sensitivity on top of an automated floor, never as the floor.

  STEELMAN:
    Strongest counterargument: The healthcare comparison overstates the difficulty. Under-reporting
      in hospitals is driven overwhelmingly by *disincentive* — blame culture, fear of enforcement,
      career consequences, documentation burden on already-overloaded clinicians. None of those
      apply to an agent, which has no fear of repercussion, no reputational stake, and negligible
      marginal cost to filing. Remove the disincentives and the reporting rate should be far closer
      to the noticing rate. Furthermore, the SOC 2 objection is about *organisations attesting to
      auditors* — an adversarial-incentive setting with an external party to satisfy. C2A2's
      self-report is internal instrumentation with no counterparty to deceive, so the independence
      concern that motivates the standard is absent. On this view the binding constraint is not
      willingness but *noticing*, and the correct fix is better observability rather than abandoning
      self-report as a channel.
    What would need to be true for C2A2 to be safe: The agent would need to reliably *notice* damage
      in the first place — meaning the damage must be visible in the agent's normal working path,
      not silent — and reporting must be genuinely costless and unpenalised, including no implicit
      pressure toward declaring a run successful. It would also require that PRESUMPTION-894 hold,
      since a report is only as good as the recollection behind it; given that 894 is separately
      CHALLENGED, this condition currently fails. If damage were always loudly visible and reporting
      were free, voluntary report would be a reasonable *supplementary* detector — though still not
      a sufficient sole one under any assurance framework found.
    How to test: Inject known damage — silently truncate a register file, drop an entry, corrupt a
      link — at randomised points across runs, and measure what fraction is voluntarily reported
      before any automated check is added. This directly yields the detector's sensitivity and is
      the same methodology (independent measurement versus voluntary report) that produced the 20x
      finding in the hospital literature. A pilot of even ten injections would distinguish a
      high-sensitivity detector from a near-blind one.

  Recommendation: CHALLENGED

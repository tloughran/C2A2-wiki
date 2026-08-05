SEARCH-FOR-PRESUMPTION-669:
  Date searched: 2026-08-05
  Original item: PRESUMPTION-669
  Original statement: That a hold is a state with terms someone re-reads; a
    length-only hold was read by two independent runs as "unreviewable,"
    excluding a 15-pair band whose semantic content had never been reviewed, and
    the correction came only from a run that read the hold's terms rather than
    its label.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-669
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from one documented over-broad hold plus one condition known
        to be permanently unsatisfiable
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. GMP material quarantine and disposition practice (ICH Q7, Good
       Manufacturing Practice guidance for active substances; and the associated
       SOP literature on disposition of production materials). — The strongest
       empirical precedent that the presumption *can* hold. In regulated
       pharmaceutical manufacturing a hold is a formal state with enumerated
       terms: material is labelled Quarantine or Quarantine-Hold, the state
       hard-blocks allocation, picking, use and shipment, and it can only be left
       by an authorised disposition posted against a named specification.
       Periodic re-confirmation is mandatory — at least annually for
       supplier-tested material against a COA — and the whole arrangement is
       externally audited. Here the terms are re-read by construction, by a named
       authority, on a clock. Note what carries the property: not the label, but
       the mandate, the named authority and the audit.
    2. Expiring-hold tooling in software practice: eslint-plugin-unicorn rule
       `expiring-todo-comments`; PHPStan TODO-comment expiration; the
       expiring-todo-comments GitHub Action. — Analogous support that the
       mechanism is constructible and in production use. A hold is given an
       expiry condition at the moment it is created — a date, a package version,
       an engine version — and the build fails when the condition is met, which
       forces the terms back in front of a reader. The associated practitioner
       consensus is the relevant design rule: a TODO or suppression should carry
       either an expiry or a ticket number, and is otherwise not useful.
       Practitioner sources, not peer-reviewed.
    3. Hu, H., Wang, Y., Rubin, J. & Pradel, M., 2025. "An Empirical Study of
       Suppressed Static Analysis Warnings." Proceedings of the ACM on Software
       Engineering 2(FSE). doi:10.1145/3715729. — Reported in full per the
       no-cherry-picking rule; the first systematic study of the question and it
       goes against. Across Python, Java and JavaScript with Pylint, Checkstyle,
       PMD and ESLint: the number of suppressions in a project increases
       continuously over time; many are never removed; those that are removed are
       removed quickly or not at all, with the removed fraction dropping toward
       zero as lifetime increases. Most directly on point for this item, 50.8% of
       all suppressions do not affect any warning — the label persists after its
       terms have ceased to apply, and no one re-read it.
    4. Flaky-test quarantine practice literature (test-quarantine guidance,
       2024-2026; Microsoft and Google engineering-productivity findings on flaky
       tests). — Analogous support for the failure mode and for the remedy.
       Quarantine used without an established exit process produces an
       ever-growing backlog; the standing advice is that a quarantined test is a
       TODO and not a solved problem, and that quarantine must be paired with an
       owner and a deadline. Microsoft's finding that developers who encounter
       flaky tests are significantly less likely to investigate subsequent test
       failures is the propagation mechanism: the label, once trusted,
       substitutes for the terms. Practitioner and industry-report material;
       the Microsoft and Google findings are cited secondhand and the primary
       sources are UNVERIFIED.

  Strength of support: Moderate

  Summary: The presumption is supported where it is enforced and not otherwise,
    and the literature is unusually clear about which is which. The GMP
    quarantine regime is a working demonstration that a hold can be a state whose
    terms are genuinely re-read: it has enumerated terms, a named disposition
    authority, a mandatory review interval and an external auditor, and under
    those conditions holds do exit. Expiring-TODO and expiring-suppression tooling
    show the same property achieved cheaply in software by attaching an expiry
    condition at creation time so the build itself forces the re-read. Against
    this, the only systematic empirical study located — Hu et al. at FSE 2025 —
    finds that where nothing enforces the re-read, suppressions accumulate
    monotonically, are largely never removed, and in over half of cases no longer
    correspond to any live warning. The flaky-test quarantine literature reports
    the same shape and adds the mechanism by which a label displaces its terms:
    once a suppression label is trusted, subsequent readers stop investigating.
    The specific event in the item — two independent runs reading a length-only
    hold as "unreviewable," corrected only by a run that read the terms — is the
    predicted behaviour of an unenforced, non-expiring hold.

  Caveats: The supporting precedents are asymmetric in cost. GMP's guarantee is
    bought with regulatory compulsion and external audit, which C2A2 does not
    have and cannot cheaply simulate; the transferable part is the structure
    (enumerated terms, named authority, review interval), not the enforcement.
    The expiring-TODO evidence is tooling existence rather than measured
    effectiveness — no study was found measuring whether expiring suppressions
    are in fact re-read and resolved rather than having their expiry dates
    extended, which is the obvious defeat and is worth flagging as an open
    question. Hu et al. covers static-analysis suppressions in open-source
    repositories and its transfer to a review-hold in an agent pipeline is
    analogical, though the accumulation dynamic is generic. Sources 2 and 4 are
    practitioner material; the Microsoft and Google figures within source 4 could
    not be traced to primary publications and should not be cited as such. The
    item's sharpest sub-claim — that the *label* was read in place of the terms —
    is supported here only indirectly, by Hu et al.'s useless-suppression finding
    and by the flaky-test investigation-decay finding; no source was located that
    studies label-versus-terms substitution directly, and that specific mechanism
    is a candidate literature gap.

  Recommendation: PARTIALLY-SUPPORTED

  Search scope: Adequate. Concepts searched: quarantined tests and deferred
    defects that never exit quarantine; suppression accumulation, lifetime and
    removal; scope creep in exclusions; un-expiring suppressions; expiring TODO
    comments, feature-flag sunset dates and forced re-review; GMP/ICH Q7 hold and
    quarantine status with mandatory periodic review. Not searched: legal and
    regulatory sunset-clause literature; deprecation policy studies; medical
    device or clinical-hold review intervals — any of which could strengthen the
    enforced-review precedent.

SEARCH-FOR-PRESUMPTION-893:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-893
  Original statement: [inferred] No recovery-point objective is held for the registers, so a remedy at
    one-snapshot-per-run granularity reads as sufficient.
  Generalizable limb searched: Does the absence of a stated recovery-point objective causally permit a backup
    regime to under-provision — i.e. is a stated RPO the thing that would otherwise reveal a snapshot interval as
    too coarse? (The in-house limb — whether *these* registers in fact have no RPO — is not searchable and was
    not searched.)
  DIRECTION NOTE: the item is a presumption filed as unsafe. "Support" below means literature supporting 14b's
    finding that a missing RPO makes an under-sized remedy read as sufficient — not support for the presumption
    being a safe belief.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Source base is heavily
    vendor/practitioner (Druva, Commvault, Veeam, Cohesity, Trilio, AvePoint) plus patent prosecution text. No
    peer-reviewed empirical study of RPO-specification practice was found. This is the main quality limit on the
    item and I am flagging it rather than dressing it up.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-893
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from ASSUMPTION-1233 — the remedy was proposed at a granularity nobody had to justify, which
           14b read as evidence that no objective exists against which granularity could be judged.
      15a: Searched for supporting literature (2026-08-31)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. MongoDB, undated. "Guidance for Atlas Backups." MongoDB Atlas Architecture Center docs — States that when
       continuous backup is disabled, RPO corresponds directly to the interval between snapshots (4-hourly backups
       => maximum 4-hour RPO). Establishes the identity that makes the presumption consequential: snapshot
       granularity *is* the RPO, whether or not anyone named it.
    2. TechTarget (WhatIs), undated. "What Is A Recovery Point Objective (RPO) And How Does It Work?" — Snippet:
       once the RPO is defined, it *determines* the minimum frequency with which backups must be made. The causal
       arrow runs objective -> schedule; with no objective, the schedule is unconstrained.
    3. US Patent 10754729 and US Patent 10761942, "Recovery point objective (RPO) driven backup scheduling in a
       data storage management system" (and enhanced-data-agent variant) — Prosecution background states that
       operators are conventionally required to work out and re-work backup schedules to satisfy the RPO, and
       that "in many cases, this ad hoc approach fails to meet the RPO, resulting in unacceptable amounts of lost
       data." Patent background sections are self-serving about the problem they solve, but the failure mode
       described is exactly the item's.
    4. Trilio, undated. "RPO in Disaster Recovery: What It Means and Why It Matters." — Two relevant snippets:
       most organisations "don't think seriously about it until they're already staring at the damage," and RPO
       drift, where a configured regime is verified once and never revalidated while conditions change.
    5. Druva, undated. "Recovery Point Objective (RPO): Definition, Calculation, and Best Practices." — Worked
       illustration: a 6:00 AM validated backup with a 9:00 AM failure yields a three-hour actual loss window, and
       a one-hour stated RPO is missed regardless of restore speed. Shows what the stated objective does — it
       makes the shortfall legible as a miss rather than as a normal outcome.
    6. US Patent 11573866 / 10860443, "Evaluation and reporting of recovery readiness in a data storage management
       system" — Existence of a patent family specifically for *evaluating and reporting* recovery readiness is
       indirect evidence that unevaluated regimes are the default state being remedied. Weak, indirect.

  Strength of support: Moderate

  Summary: The generalizable limb is supported, though by a source base weaker than one would like. The literature
  is unanimous and unambiguous on the mechanism: with interval-based snapshotting, RPO simply equals the snapshot
  interval, and a stated RPO is what determines minimum backup frequency. That relationship makes the item's
  inference sound in form — where no objective is stated, the interval faces no test, so any interval that runs
  reliably will read as sufficient because "it ran" is the only available success criterion. Practitioner sources
  add two supporting observations: organisations characteristically do not confront RPO until after a loss, and
  regimes verified once drift silently thereafter. Patent background text describing ad hoc scheduling that "fails
  to meet the RPO, resulting in unacceptable amounts of lost data" describes the same failure with a stated
  objective present; the unstated case is strictly worse, since the miss is not even detectable. I found no source
  arguing that an unstated RPO is adequate.

  Caveats: (i) No peer-reviewed or independently-collected empirical evidence on the *prevalence* of missing RPO
  specification was found; the prevalence claims are vendor-authored by parties selling RPO tooling. (ii) The
  mechanism (interval = RPO) is definitional rather than empirical — it supports the inference's validity but is
  not evidence that this particular register regime under-provisions. (iii) All sources address organisational
  disaster recovery at data-centre scale; transfer to a single-agent file register is by analogy, and the analogy
  weakens where the cost of loss is low or where the loss is externally reconstructible. (iv) The Cockroach Labs
  *State of Resilience 2025* figures surfaced in this search were seen only as a secondhand quotation inside a
  vendor page and are not cited here as primary.

  Recommendation: SUPPORTED

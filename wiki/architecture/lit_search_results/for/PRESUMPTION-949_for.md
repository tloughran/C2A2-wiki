SEARCH-FOR-PRESUMPTION-949:
  Date searched: 2026-09-11
  Original item: PRESUMPTION-949
  Original statement: "[inferred] That a flag which names its own defect condition has thereby been
    dispositioned — that stating 'a third undispositioned flag would mean the flag channel is the
    defect' is itself a kind of disposition."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-949
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a pattern across three independent runs on one day; this register recorded as
        inside the pattern rather than exempted from it.
      15a: Searched for supporting literature; found strong support for the *value* of naming and none
        for naming *constituting* disposition — including from the one tradition (Toyota andon) most
        often cited in favour of it, which turns out to require an effector by definition.
    Current status: PARTIALLY-SUPPORTED

  Register pre-check:
    - PREMISE-173 (ACTIVE) — "NAME THE FINAL ELEMENT." Adapted from IEC 61511: a sensor with no final
      element is not a protection layer; a remedy consisting only of observing, recording, counting or
      reporting is not a remedy. This bears on the item **verbatim** and rules it against. 14b's note
      that PREMISE-173 may bear is confirmed.
    - PREMISE-131 (ACTIVE) — a warning is not a control, and an undelivered warning is not a mitigation;
      warnings occupy the two least-effective tiers of the hierarchy of controls.
    - PREMISE-138 (ACTIVE) — repetition inside a channel with no effector is not a remedy; its only
      admissible function is transfer of obligation to a named actor outside the channel.
    - PREMISE-108 (ACTIVE) — transmission is not delivery; a finding "flagged for" an agent is held by
      nobody while the record shows it discharged, and that state is worse than not flagging.
    - PREMISE-116, PREMISE-123 (ACTIVE) — a finding does not change the behaviour it describes;
      propagation must be engineered and then confirmed.
    This is the most heavily pre-answered item of the ten. Recording the hit per OPEN-192; searched
    anyway.

  LIMB SPLIT:
    Limb A (NAMING HAS INDEPENDENT VALUE): surfacing a defect is a real and creditable act whose worth
      does not depend on a fix following.
    Limb B (NAMING IS DISPOSITION): a well-worded record with a named test and no owner discharges the
      finding and may be reported as the outcome.

  Supporting evidence found: Partial (Limb A only)

  Sources:
    1. Toyota Production System primary and semi-primary material (Toyota Motor Corporation global
       site; Art of Lean "Andon" TPS Encyclopedia entry; Toyota UK TPS glossary). — SECONDARY —
       Retrieved as the strongest available FOR-direction case: the andon is the canonical instrument
       whose purpose is *making a problem visible*, and TPS culture is explicitly described as an
       "obsession with surfacing problems instead of hiding them." Supports Limb A strongly. But the
       same sources destroy Limb B: "the defining feature of andon is that it is activated by the person
       doing the work **to call for help**. It is a pull system for problem-solving," and jidoka is
       defined by "stopping immediately when abnormalities are detected." The andon has a line-stop as
       its final element. Naming without the stop is not andon; it is the condition andon was built to
       replace.
    2. ITIL / incident-management process descriptions (Atlassian, ISACA-adjacent practitioner sources,
       OnPage, Asana). — SECONDARY — Identification is uniformly the *first* of five or six steps, never
       the terminal one; logging is step two and the lifecycle closes on resolution and review. Supports
       Limb A (identification is a named, valued, distinct stage) and refutes Limb B (it is a stage, and
       stages have successors).
    3. Municipal/public-sector audit follow-up reporting (Oakland City Auditor, 2024 Audit
       Recommendation Follow-Up Report; South Florida Water Management District 2023 Q2 follow-up;
       EUROSAI 2021 report on follow-up of audit recommendations). — SECONDARY — Departments implemented
       **44%** of recommendations from audit reports issued 2014–2023. Formal follow-up methods yielded a
       **61%** implementation rate against **82%** for self-assessment methods (the inversion is itself
       a measurement-validity warning and should not be read as self-assessment working better). Over a
       ten-year period there were **21 repeat recommendations, 16 of them partially or not implemented**.
       These are the best quantitative estimates I could reach of the gap between a well-worded finding
       and a change in the world. All SECONDARY — I did not retrieve the underlying PDFs' tables.
    4. Static-analysis alert literature (Heckman & Williams actionable-alert work, reported in
       arXiv:2509.11787 and in "How Do Developers Act on Static Analysis Alerts? An Empirical Study of
       Coverity Usage"). — SECONDARY — Only **27.4%–49.5% (median 36.7%)** of static analysis alerts are
       actionable across projects; and "if developers mark reports in a particular scan as false
       positives, then they are less likely to triage future reports in the same file." The second
       finding is the one that matters here: an accumulating stock of named-but-unowned findings
       actively suppresses future triage of the same surface. That is a mechanism by which Limb B is not
       merely neutral but self-worsening.
    5. Guo, P. J. & Engler, D., 2009. "Linux Kernel Developer Responses to Static Analysis Bug Reports."
       USENIX ATC. — UNVERIFIED — located but not retrieved; listed because it is the primary study of
       what developers do with named-not-owned defect reports and would be the right source to read if
       this item is pursued. No figure from it is used.

  Strength of support: Moderate (Limb A), None (Limb B)

  Summary: Limb A is well supported and should be stated plainly, because the estate's self-directed
    findings are genuinely good work and the register should not read as though naming were worthless.
    Surfacing a defect is the first step of every incident lifecycle I found and the constitutive act of
    the most admired quality system in manufacturing. Limb B has no support and is contradicted by the
    same sources: andon calls for help and stops the line; incident identification is step one of five;
    audit recommendations reach implementation at 44% over a decade *with* a formal tracking apparatus
    the estate does not have; and static-analysis practice shows that unowned findings depress future
    attention to the surface they name. PREMISE-173 already states the governing rule and the search
    found nothing that would loosen it. The honest reading of 14b's three instances is that all three
    were correct acts of identification reported as though they were dispositions — the defect is in the
    report's terminal grammar, not in the finding.

  Caveats: The audit figures are municipal public-sector and the alert figures are large-scale software;
    both are domains with vastly more reviewers than this estate, so the *rates* do not transfer even as
    order-of-magnitude estimates. The TPS material is drawn from Toyota's own and from lean-practitioner
    sources, which are advocacy-adjacent; the andon's "line stop" is nonetheless a documented mechanical
    fact, not a claim about effectiveness, so it carries here. Nothing found addresses the *self*-
    referential case — a flag naming a defect in the flag channel itself — which is where the item's
    reflexivity lives.

  NOVELTY-FLAG:
    Item: PRESUMPTION-949, Limb B (that naming constitutes disposition).
    Searched: incident-management lifecycles, hierarchy of controls, safety-instrumented-function
      acceptance criteria, andon/jidoka, near-miss reporting, audit recommendation follow-up, static
      analysis alert triage, and the reflexive case (a control whose subject is the control channel).
    Finding: no literature argues the position. The positions available are "identification is step one"
      and "a warning is the weakest control"; no source treats a record as a terminal disposition.
    Implication: nobody asked because the answer is obvious once stated explicitly — which is exactly
      why it functions as an *unstated* premise and not a stated one.
    Recommended status: NOVEL — and the novelty is **unfavourable**. This is not an original
      contribution; it is a premise that survives only by remaining unarticulated. Its value to the
      estate is diagnostic, not intellectual.

  Search scope: comprehensive — searched incident-management process definitions, near-miss and hazard
    reporting, andon/jidoka primary material, audit recommendation implementation rates and follow-up
    mechanisms, and static-analysis alert actionability and triage behaviour. Did not search the
    organisational-behaviour literature on "voice" (Morrison, Detert) or psychological safety, which
    would strengthen Limb A further but cannot touch Limb B.

  Recommendation: PARTIALLY-SUPPORTED. The recommendation rests on Limb A. Limb B — the load-bearing
    limb, and the one carrying 14b's High risk — is NO-SUPPORT-FOUND and is already ruled against by
    PREMISE-173, PREMISE-131 and PREMISE-138. The actionable residue is small and concrete: the three
    instances named (ASSUMPTION-1316, MONITOR-599, the pre-answered-rate observation) each need an owner
    and a date, and the reflexive point stands — this file is also speech, and names no owner either.

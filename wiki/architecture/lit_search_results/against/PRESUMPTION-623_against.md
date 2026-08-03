SEARCH-AGAINST-PRESUMPTION-623:
  Date searched: 2026-08-02
  Original item: PRESUMPTION-623
  Original statement: That documented warnings, memory notes and operational rules reduce recurrence of a known trap absent an executable check. Evidence in hand: three recorded recurrences of one trap against a note written specifically to prevent it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-623
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced an unstated assumption that writing a rule or warning into the durable record constitutes a control against recurrence; noted three observed recurrences against one such note.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Joint Commission Journal on Quality and Patient Safety, 2023. "Use of Technology to Improve the Adherence to Surgical Safety Checklists in the Operating Room" (PubMed 37198060). — The decisive comparison: completeness was 27.1% for the traditional (documented) checklist versus 100.0% for an electronic checklist with a forcing function. Same content, same staff, same institution; the difference is whether the check is executable and blocking. This is close to a direct experimental test of the presumption, and it fails it.
    2. Ivers, N. et al., Cochrane Database of Systematic Reviews CD000259 (2012, updated 2025/2026). "Audit and feedback: effects on professional practice." — The best-powered estimate of what telling people about a problem achieves: median absolute improvement of 2.7-4.3% in compliance with desired practice. Documented feedback is a real but very small effect, insufficient to prevent recurrence of a trap encountered repeatedly.
    3. Russ, S. et al., 2015. "Implementation of safety checklists in surgery: a realist synthesis of evidence." Implementation Science (PMC4587654). — Longitudinal studies show intervention decay: over 6-12 months, usage patterns become variable and compliance across checklist items wanes. A written control is not stable over time even where it initially works.
    4. Donahue, A.K. & Tuohy, R.V., 2006. "Lessons We Don't Learn: A Study of the Lessons of Disasters, Why We Repeat Them, and How We Can Learn Them." Homeland Security Affairs 2(2). — Documented lessons recur because documentation is not the mechanism of change; sustained recurrence prevention requires long-term resource commitment and organisational discipline that transient attention does not supply.
    5. "Learning From Software Failures: A Case Study at a National Space Research Center," 2025 (arXiv 2509.06301) and "Learning From Lessons Learned: Preliminary Findings From a Study of Learning From Failure," 2024 (arXiv 2402.09538). — Engineers report encountering the same classes of failure repeatedly across projects despite formal lessons-learned processes; the "black hole repository" pattern — lessons captured into systems from which they cannot be extracted at the moment of need — is named directly.
    6. Canadian Centre for Occupational Health and Safety, "Hazard and Risk — Hierarchy of Controls" (ISO 45001-aligned); CanadiEM, "Checklists and the Hierarchy of Effectiveness." — Administrative controls — rules, training, warnings, notes — rank second-lowest in the standard hierarchy, above only PPE, because they depend on a person doing the right thing every time. Person-based approaches (education, new rules) are easy to implement and have a high tendency to fail; systems-based approaches (forcing functions) have the highest leverage.

  Strength of challenge: Strong

  Summary: This is the best-evidenced item of the seven and the challenge is close to unambiguous. The occupational-safety hierarchy of controls exists specifically to rank written rules and warnings near the bottom of effectiveness, and the mechanism is exactly the one observed here: the control depends on a human or agent recalling and applying it at the moment of exposure. The forcing-function comparison — 27.1% versus 100.0% completeness for the same checklist — quantifies the gap between a documented check and an executable one. Audit and feedback, the closest analogue to a memory note, moves compliance by 2.7-4.3% absolute. The lessons-learned literature independently documents recurrence despite formal capture. Three recurrences against one note is entirely consistent with these base rates and does not require any additional explanation.

  Specific risks: Writing the note is recorded as remediation, so the trap is marked closed while remaining fully live. Each recurrence then produces another note rather than an executable check, and the note corpus grows as a monotone function of unfixed defects — the archive of warnings becomes an index of active hazards misread as an index of resolved ones. Because notes are cheap and checks are expensive, the system will preferentially generate notes, and the ratio of administrative to engineering controls will drift steadily in the wrong direction. Decay compounds it: even a note that works initially loses effect over 6-12 months.

  Mitigations available: (a) Promote any trap with 2+ recurrences to an executable, blocking check — a linter rule, a pre-commit hook, a validator, a schema constraint — and treat the note as documentation of the check, not as the control; (b) classify every recorded control by hierarchy tier and track the administrative:engineering ratio; (c) never close a recurrence with a note alone; (d) prefer restriction of the failure path over instruction against it (see PRESUMPTION-621, PMC8797538); (e) if a check genuinely cannot be automated, place it at a point where it cannot be skipped rather than in a document that must be recalled.

  Search scope: Comprehensive. Checklist adherence, forcing functions, hierarchy of controls, audit-and-feedback and lessons-learned repositories were all searched and converge. The one caveat is that the forcing-function comparison is from a single institutional study; a broader search of the human-factors forcing-function literature would strengthen the effect-size estimate but is unlikely to reverse the direction.

  STEELMAN:
    Strongest counterargument: Not every trap can be made executable. Some are judgement calls, some are context-dependent, some would cost more to encode than the failures cost. In that regime a note is the only available control and a 2.7-4.3% improvement is better than nothing — and the Cochrane review notes that effects are larger where baseline performance is low and where co-interventions are present, which is the situation of a repeatedly recurring trap. The three observed recurrences are also a sample of three: without a base rate for how often the same trap recurred *before* the note, they do not establish that the note had no effect. It is possible the note reduced recurrence from ten to three.
    What would need to be true for the system to be safe: (i) the trap is genuinely not mechanisable; (ii) the note is surfaced at the point of exposure rather than stored in a repository that must be searched; (iii) recurrence is counted and triggers automatic promotion to an executable check at a threshold; (iv) note effectiveness is measured against a pre-note baseline, not assumed.
    How to test: For the trap in hand, count occurrences per unit of exposure in the window before the note was written and the window after. Then implement an executable check for the same trap and count a third window. Two comparisons — note versus nothing, and check versus note — give the effect of each control tier for this system, directly comparable to the 27.1%/100.0% checklist figures.

  Recommendation: CHALLENGED

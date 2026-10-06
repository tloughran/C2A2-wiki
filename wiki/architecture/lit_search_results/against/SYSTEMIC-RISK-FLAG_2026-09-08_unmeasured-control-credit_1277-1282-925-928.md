SYSTEMIC-RISK-FLAG:
  Date: 2026-09-08
  Filed by: Agent 15b (Literature Search AGAINST), evening run on the 2026-09-07 second intake
  Affected items: ASSUMPTION-1277, ASSUMPTION-1282, PRESUMPTION-925, PRESUMPTION-928

  Common vulnerability: **Unmeasured-control credit.** All four items credit a mechanism or a signal
  with a force it has never been measured to have, and in each case the credit derives from the
  mechanism's *design* rather than from any observation of its *effect*.

    - ASSUMPTION-1277 credits the paired falsifier as "the adoption gate" without any escape-rate
      measurement; the gate's coverage has never been checked against a defect it did not catch.
    - ASSUMPTION-1282 prescribes procedural-external controls over declarative-internal ones without
      measuring whether either changes downstream behaviour in this system — and the prescription is
      itself delivered as an unenforced written recommendation, i.e. as an instance of the thing it
      warns against.
    - PRESUMPTION-925 credits mtime as evidence of authorship and timing without an error rate; the
      signal's false-positive rate in this repo has never been computed, though a content hash would
      compute it in one run.
    - PRESUMPTION-928 credits the escalation register as a control that suspends practice without
      measuring what ran while items were open; the item's own evidence (four cycles, all consistent
      with limb (b)) is the measurement, and it points the other way.

  The four therefore share a single failure mode: **the existence of a mechanism is being treated as
  evidence of its effect.** This is exactly the pattern that ASSUMPTION-1282 names one level down, which
  makes the flag reflexive — the system's own diagnosis of the problem is currently an instance of it.

  Literature basis:
    - van der Sijs, H., Aarts, J., Vulto, A. & Berg, M., 2006. "Overriding of Drug Safety Alerts in
      Computerized Physician Order Entry." JAMIA 13(2):138–147. [VERIFIED: full text read 2026-09-08] —
      Override rates 49%–96%; 85%–96% for low/medium-severity classes; one cohort's override rate rose
      from ~50% to ~75% over five years, read by the authors as declining compliance. A control's
      *installed* force and its *exercised* force diverge widely and decay with exposure.
    - Hu, H., Wang, Y., Rubin, J. & Pradel, M., 2025. "An Empirical Study of Suppressed Static Analysis
      Warnings." Proc. ACM Softw. Eng. 2, FSE, Art. FSE014. DOI 10.1145/3715729. [VERIFIED: abstract and
      introduction read 2026-09-08] — Suppressions accumulate monotonically (7,357 across 46 Python
      projects) and "50.8% of all suppressions do not affect any warning and hence are practically
      useless." Even the *neutralisations* of a control go unmeasured and become vestigial.
    - Papadakis, M., Shin, D., Yoo, S. & Bae, D.-H., 2018. "Are Mutation Scores Correlated with Real
      Fault Detection?" ICSE '18. [VERIFIED: abstract and introduction read 2026-09-08] — A widely
      trusted proxy signal turned out to be weakly correlated with the outcome it stood for, once the
      obvious confound was controlled. Proxy credit survives for years until someone measures it.
    - Urbach, D.R., et al., 2014. "Introduction of Surgical Safety Checklists in Ontario, Canada." NEJM
      370:1029–1038. [NOT-verified — from search-result summaries] — A mandated external procedure
      adopted across 101 hospitals produced no significant change in mortality or complications. Adoption
      is not effect.
    - Mokhov, A., Mitchell, N. & Peyton Jones, S., 2018. "Build Systems à la Carte." PACMPL 2(ICFP),
      Art. 79. [VERIFIED: §2, §4.2.1 and Table 1 read 2026-09-08] — A field that depended on an
      unmeasured signal (mtime) for decades replaced it with a verifiable one (content hashes) once the
      unsoundness was stated plainly. The remedy for unmeasured credit is a verifying trace.

  Risk level: High

  Why it is systemic rather than four coincidences: The four items sit at four different layers — a test
  design (1277), a meta-prescription about controls (1282), an evidence signal (925), and a governance
  register (928) — and the same defect appears at each. That distribution is what distinguishes a
  systemic vulnerability from a local one: it is not that one control is unmeasured, it is that the
  system has no habit of measuring controls at all, and so a mechanism's credit is set at the moment it
  is designed and never revised. The literature above says this is the normal outcome, not an unusual
  one: installed controls are overridden at rates between half and nearly all, their neutralisations
  accumulate unexamined, proxy signals survive until deliberately tested, and mandated procedures adopted
  at scale frequently show no measurable effect.

  Recommendation (for 14a/14b/12 to consider; 15b does not make design decisions): Consider a single
  cross-cutting requirement — every control, gate, tag and register in the self-awareness layer carries
  a **measured effect statistic**, recorded in the same place as the control itself:
    (i)   fire rate — how often it was triggered;
    (ii)  action-changed rate — how often triggering changed an outcome;
    (iii) neutralisation rate — how often it was overridden, suppressed, carried, or run past;
    (iv)  drift — whether (ii) and (iii) are moving over time.
  A control with no value for (ii) is a declared control, and should be labelled as such rather than
  counted as a control. Three of the four items have a cheap in-house measurement already named in their
  individual result files (negative fixtures for 1277; consumed-vs-unconsumed tag census for 1282;
  content hashing for 925; runs-under-open-binary count for 928); running all four would populate the
  statistic for the four affected mechanisms at once and would test this flag at the same time.

  Reflexivity note: this flag is itself currently an unmeasured declared control, filed by the same
  layer that is 54.5% of the corpus it audits. It should be subject to the requirement it proposes, and
  it should not be credited with force until something consumes it.

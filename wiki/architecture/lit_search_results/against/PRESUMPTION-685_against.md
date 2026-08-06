SEARCH-AGAINST-PRESUMPTION-685:
  Date searched: 2026-08-06
  Original item: PRESUMPTION-685
  Original statement: That deferring to a prior published figure is the conservative move; a
    run withheld its own 57 in favour of the prior day's 24 on the ground that its parser had
    carried a bug, a rule that makes a figure durable in proportion to how long it has gone
    unchallenged.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-685
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: 14b read a stated deference rule against the same run's opposite use of the same
        register.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Henrion, M. and Fischhoff, B., 1986. "Assessing uncertainty in physical constants."
       American Journal of Physics 54(9), 791-798. (Journal, volume, pages and year confirmed
       this session; full text available at gwern.net and via AIP.) The canonical empirical
       demonstration that deference to prior published figures is not conservative. Examining
       historical measurement series for the fundamental constants, the authors found reported
       uncertainties consistently biased toward *underestimating* actual error, and identified
       a bandwagon effect in which successive measurements cluster around the incumbent value
       rather than around the truth. The speed-of-light series is the exhibit: measurements
       from 1876-1902 overestimated c by roughly 70 km/s, then from 1905-1950 underestimated
       it by roughly 15 km/s — long runs of mutually consistent, confidently reported, wrong
       values. Each individual run in that series was behaving exactly as C2A2's deference
       rule prescribes, and the aggregate result was a decades-long error with artificially
       tight error bars.
    2. Klein, J. and Roodman, A., 2005. "Blind Analysis in Nuclear and Particle Physics."
       Annual Review of Nuclear and Particle Science 55, 141- (DOI 10.1146/annurev.nucl.55.
       090704.151521; confirmed this session). Names the exact mechanism at issue. The review
       lists "consistency with previous measurements" among the preconceptions that bias
       results, and identifies *stopping bias* — continuing to hunt for mistakes or to
       "improve" the analysis until the result agrees with expectation — as probably the most
       common bias in the field. C2A2's run did precisely this: it found a disagreement with
       the incumbent, searched for a fault in its own instrument, found a candidate (a parser
       bug), and stopped. The remedy the field adopted is blinding, i.e. deciding selection
       and analysis procedure *before* seeing whether the answer agrees — the structural
       opposite of a post-hoc deference rule.
    3. Particle Data Group, Review of Particle Physics, "Introduction" section, treatment of
       discrepant data (pdg.lbl.gov review PDFs confirmed this session; see also "Alternative
       to the application of PDG scale factors," European Physical Journal C 80:541 (2020),
       arXiv:2004.01219 — [UNVERIFIED — author list not confirmed this session]). The field
       with the longest institutional experience of exactly this problem does not resolve
       discrepancy by suppression. Its prescription is to retain all measurements, preserve
       the central values, and inflate the uncertainty on the mean by a scale factor
       S = sqrt(chi-squared/ndf), explicitly so that "the reader is warned of this situation
       by the size of the scale factor" and can return to the literature and redo the average
       with a different choice of data. This is a direct, worked alternative to C2A2's rule:
       the discrepant new figure is published *with* the disagreement made visible, not
       withheld in favour of the incumbent.
    4. Selective outcome-reporting / outcome non-reporting bias literature (confirmed this
       session: "Selective reporting bias of harm outcomes within studies: findings from a
       cohort of systematic reviews," PMC4240443; "Rethinking the assessment of risk of bias
       due to selective reporting," PMC4938957; AHRQ/NCBI Bookshelf NBK100617, "Selective
       Outcome Reporting as a Source of Bias in Reviews of Comparative Effectiveness"). This
       body of work reclassifies the act C2A2 performed. Withholding a measured result because
       of a judgement about its magnitude or its relation to expectation is not caution — it
       is the definition of selective non-reporting, and it is treated as a risk-of-bias
       domain in its own right. One methodological study reported that 13% of 8434 studies in
       Cochrane reviews were rated high risk of bias on the selective-reporting domain, most
       often for outcome non-reporting concerns [figure confirmed this session from the search
       result summary; the specific source article was not opened, so treat the attribution as
       provisional]. The framing that matters for C2A2: the suppressed 57 is not a null event.
       It is a datum that has been removed from the record for a reason correlated with its
       value.
    5. "A selected history of expectation bias in physics," American Journal of Physics 74(7),
       578 (2006) — [UNVERIFIED — author not confirmed this session; title, journal, volume,
       issue and page appeared in search results]. Surveys the recurring pattern in which
       experimental values migrate toward the incumbent and only later jump, which corroborates
       source 1 outside its original sample.

  Strength of challenge: Strong

  Summary: The presumption inverts the finding of the only literatures that have measured it.
    Deference to the incumbent published figure is not the conservative option; it is a known,
    named, quantified bias (bandwagon effect, stopping bias, expectation bias) that produces
    long runs of confidently wrong values with underestimated uncertainty. The specific
    asymmetry in the C2A2 case — a run that scrutinised its own instrument only after
    discovering disagreement, and stopped scrutinising once it found a reason to defer — is the
    textbook description of stopping bias. The mature alternatives are well developed and
    cheap: blind the decision procedure from the answer (Klein & Roodman), or retain both
    figures and inflate the stated uncertainty so the discrepancy is visible downstream (PDG
    scale factor). The evidence-synthesis literature adds that suppression on a
    value-correlated ground is itself a bias category, not a null act. 14b's observation that
    the rule makes a figure durable in proportion to how long it has gone unchallenged is
    precisely the property Henrion and Fischhoff measured.

  STEELMAN:
    Strongest counterargument: The run had a *specific, identified* defect in its own
      instrument — a parser bug — not merely a disagreement with the prior. That is a
      materially different epistemic situation from bandwagon deference. When an instrument is
      known to be faulty, discarding its output is not anchoring; it is correct triage, and
      publishing a figure you have positive reason to believe is wrong would be the reckless
      move. Blind analysis, notably, permits and encourages unblinding-and-fixing when a
      genuine defect is found; it prohibits only the *search* for defects conditioned on the
      answer. Furthermore, the asymmetry of costs is real: a spurious 57 propagates into
      downstream records and later runs will defer to *it*, so the incumbent-preserving choice
      genuinely limits the blast radius of a single bad run. There is also no
      C2A2 equivalent of the PDG's community of independent measurers — with a single
      instrument, "retain both and inflate uncertainty" may just publish noise twice.
    What would need to be true for C2A2 to be safe: (a) the parser bug was identified by a
      route independent of the disagreement — i.e. it would have been found and fixed even if
      the run had produced 24; (b) the deference is recorded as a *suppressed observation*
      with its value, not silently dropped, so the record retains the fact that a 57 existed;
      (c) the incumbent 24 is not thereby strengthened — its confidence must not rise because
      a challenge was withheld; (d) there is a scheduled re-measurement with a fixed parser
      that will be published regardless of whether it agrees; (e) the deference rule is
      symmetric, i.e. it would equally have suppressed a run producing 12. 14b's finding that
      the same run used the same register in the opposite direction is evidence that (e)
      fails.
    How to test: Build the time series of this figure from the vault's daily records and check
      three things. First, symmetry: over all historical revisions, how many moved *away* from
      the incumbent versus *toward* it, and were downward and upward disagreements suppressed
      at equal rates? A bandwagon signature is asymmetric suppression. Second, provenance of
      the doubt: for each instance where a run withheld its own figure citing an instrument
      fault, check whether the fault was documented before or after the disagreement was
      observed — timestamp order is decisive for stopping bias. Third, run the counterfactual
      cheaply: re-run the current parser over the historical inputs that produced 24 and see
      which figure the fixed instrument returns. If it returns 57, the deference rule cost the
      record 118-day-class latency on a correct value.

  Specific risks: If deference is not conservative, then C2A2's record acquires values whose
    durability is a function of age rather than of evidence, with stated confidence that rises
    as challenges are absorbed silently. Concretely: (i) the incumbent figure becomes
    progressively harder to dislodge, since each suppressed challenge both removes evidence
    against it and adds an implicit vote for it; (ii) uncertainty is systematically
    understated, because the spread of suppressed values never enters any error estimate;
    (iii) downstream reasoning that treats the register as a measurement series inherits a
    correlated, not random, error; (iv) the audit trail loses the ability to distinguish "no
    one has re-measured" from "re-measurements disagreed and were withheld," which is the
    single most important distinction for later reconstruction. The compounding version: a run
    that finds 57 today and defers, then next week finds 55 and defers to the 24 again, has
    manufactured a false record of stability.

  Mitigations available: (1) Never suppress — record both figures with a discrepancy flag and
    an inflated uncertainty, the PDG pattern; this preserves the incumbent's central value
    while making the disagreement visible downstream. (2) Pre-register the acceptance
    criterion: decide before running what would count as a parser fault, so the defect hunt
    cannot be conditioned on the answer (blind-analysis discipline). (3) If a figure is
    withheld, log a SUPPRESSED entry containing the value, the stated reason and the timestamp
    at which the reason was identified relative to the disagreement — this alone makes stopping
    bias auditable. (4) Symmetry audit: periodically check whether suppression rates differ for
    upward and downward disagreements. (5) Fix-and-rerun as a standing obligation: a parser
    bug cited as grounds for deference creates a scheduled re-measurement, so the incumbent's
    survival is time-bounded rather than indefinite. (6) Forbid confidence increases derived
    from the absence of published challenges.

  Search scope: Comprehensive for the measurement-epistemics framing — historical
    physical-constants bias, blind analysis, discrepant-data combination practice — and for the
    evidence-synthesis framing of suppression as reporting bias. Preliminary on two adjacent
    areas that could sharpen the steelman: the metrology literature on key comparison reference
    values and how national metrology institutes handle a single outlying laboratory, and the
    software-engineering literature on trusting a known-buggy measurement pipeline's output.
    Broader search recommended on both. The classic Millikan oil-drop anecdote about the
    electron charge drifting slowly toward the true value is frequently cited in this context
    but was not confirmed to a primary source this session and is therefore not relied upon
    here [UNVERIFIED — not confirmed this session].

  Recommendation: CHALLENGED

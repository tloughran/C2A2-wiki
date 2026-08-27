SEARCH-AGAINST-PRESUMPTION-881:
  Date searched: 2026-08-26
  Original item: PRESUMPTION-881
  Queue ref: for_lit_search.md — ITEM: PRESUMPTION-881 (Priority Critical)
  Original statement: [inferred] That a loudly surfaced breach is a discharged breach — that
    disclosing a violated constraint is compliance with it.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-881
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day disclosures with identical form and no run asking what the
           disclosure was for. High confidence. **That run was itself an instance** — recorded so the
           presumption is not stated from outside the population it describes.
      15b: Searched for challenging literature
    Current status: CHALLENGED
    Note: this search is *also* an instance of the population, in the reverse direction — it is a
      15b run reporting on a budget it did not exceed. Recorded for symmetry.

  Search scope: Four WebSearch queries executed 2026-08-26. Literatures reached: (a) Vaughan's
    normalisation of deviance and its safety-critical successors; (b) alarm/alert fatigue with
    quantitative override and desensitisation data from clinical decision support; (c) the
    behavioural-economics literature on the perverse effects of disclosure and disclosure-induced
    moral licensing; (d) technical-debt and known-error-database survivability. Venues reached: PMC
    and BMC Medical Informatics and Decision Making, Springer (Journal of Business Ethics), Wiley
    (Journal of Software: Evolution and Process), CMU institutional repository, ResearchGate
    abstracts, Wikipedia/practitioner sources for concept framing.
    NOT COVERED, and these matter: (i) Vaughan's *Challenger Launch Decision* (1996) in primary form
    — I reached it only through encyclopaedia and practitioner summaries, so the mechanism is
    second-hand; (ii) the nuclear/aviation regulatory literature on **standing waivers and temporary
    exemptions that become permanent**, which is the single most on-point body of work for "a
    constraint violated on every run that touched it and still formally in force," and which my
    fourth query missed by drifting into technical debt; (iii) the *escalation of commitment* and
    *organisational drift* literatures (Snook's practical drift, Dekker); (iv) any work on
    budget/quota breach specifically in agentic AI runtimes. Search confidence: HIGH on the mechanism,
    MODERATE on the specific waiver-permanence limb.

  Challenging evidence found: Yes

  Sources:
    1. Diane Vaughan. 1996. *The Challenger Launch Decision* — the normalisation-of-deviance thesis,
       reached via https://en.wikipedia.org/wiki/Normalization_of_deviance and
       https://psychsafety.com/normalisation-of-deviance/ — The definition is a direct hit: deviance
       from a rule "becomes culturally normalized" through repetition without consequence, and
       crucially the practitioner literature makes the disclosure point explicit: "repeated often
       enough without consequence, it becomes the team's actual practice **even though the documented
       standard never officially changed**." That last clause is C2A2's exact situation — fifteen
       consecutive breaches of a Summa cap that "remains formally in force." Note also the
       Challenger mechanism itself: the O-ring erosion was *known, documented and discussed at every
       launch*. Disclosure was never the missing ingredient; ruling was. SNIPPET-ONLY (primary text
       not reached; tertiary and practitioner sources only). This is the single most important
       citation in this file and it is the one I read least directly — flagged.
    2. [authors unverified — the AANA Journal / Prielipp-group attribution is my recollection and is
       NOT confirmed by this search]. 2010. "The Normalization of Deviance: Do We (Un)Knowingly Accept
       Doing the Wrong Thing?" https://www.researchgate.net/publication/46819021 — Extends Vaughan
       into routine clinical practice; establishes that the process "does not require negligence or
       malice — it emerges from the ordinary dynamics of organizations under competitive pressure."
       This matters because C2A2's agents are behaving with conspicuous good faith and the literature
       says good faith is not protective. ABSTRACT-ONLY.
    3. Ancker et al. [attribution recalled from the literature, not confirmed in this search]. 2017.
       "Effects of workload, work complexity, and repeated alerts on alert fatigue in a clinical
       decision support system." BMC Medical Informatics and Decision Making.
       https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-017-0430-8 ·
       https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5387195/ — The quantitative core of the challenge.
       "The likelihood of reminder acceptance dropped by 30% for each additional reminder received per
       encounter, and by 10% for each five percentage point increase in proportion of repeated
       reminders." Two named mechanisms: cognitive overload, and **desensitisation from repeated
       exposure to the same alert over time**. Applied literally: a fifteenth identical disclosure is
       not fifteen times as informative as the first; on this dose-response curve it is close to
       inert. FULL-TEXT available at the BMC link (open access); I read the abstract and the
       search-surfaced effect sizes, not the full methods.
    4. Cain, Loewenstein & Moore [attribution high-confidence but year and venue not confirmed in this
       search]. "The Dirt on Coming Clean: Perverse Effects of Disclosing Conflicts of Interest."
       https://www.cmu.edu/sites/default/files/cmu-tepper-site-files/2025-06/organizational-behavior-and-theory-cain-dissertation.pdf
       — The decisive theoretical result against the presumption. Disclosure can *increase* the
       problem it discloses, "because it leads advisors to feel morally licensed and strategically
       encouraged to exaggerate their advice even further." The mechanism named is precise: "prior to
       disclosure, conflicted advisors rein in their bias; postdisclosure, they might feel less
       obliged" — i.e. **the act of disclosing is experienced as discharging the obligation**, which
       is the presumption stated as a finding. FULL-TEXT PDF available at the CMU link; I read the
       search-surfaced summary of it, not the document itself. SNIPPET-ONLY on my actual reading.
    5. [authors unverified]. 2022. "Preventing Disclosure-Induced Moral Licensing: Evidence from the
       Boardroom." Journal of Business Ethics.
       https://link.springer.com/article/10.1007/s10551-022-05226-7 — Replicates the licensing effect
       in an organisational rather than advisory setting, and the title alone establishes that
       disclosure-induced moral licensing is a named, studied hazard requiring active prevention
       rather than an edge case. ABSTRACT-ONLY.
    6. [no author — practitioner]. "Transparency Alone Doesn't Lead to Accountability." Corporate
       Compliance Insights. https://www.corporatecomplianceinsights.com/transparency-alone-accountability/
       — States the general form and adds a second mechanism relevant to PRESUMPTION-879:
       "transparency may lead to the diffusion of moral responsibility, where the person disclosing
       the information feels they can act upon their bias once it is openly admitted, and
       responsibility is passed to the recipient of the information." In C2A2 the recipient is the
       seventeen-day-silent gate. SNIPPET-ONLY; practitioner source, low independent weight, cited for
       the framing.
    7. Zabardast et al. [first names unverified]. 2022. "Further investigation of the survivability of
       code technical debt items." Journal of Software: Evolution and Process.
       https://onlinelibrary.wiley.com/doi/full/10.1002/smr.2425 — Base rate for the "documented and
       therefore handled" assumption in a software setting: only 8.76% of code technical debt items
       (bugs, code smells, vulnerabilities) are ever removed; code smells in particular "are never
       removed and stay as long as the software system operates." Documentation is not removal.
       ABSTRACT-ONLY.
    8. ITIL known-error semantics, https://en.wikipedia.org/wiki/Known_error — Included because it is
       the industry's formalisation of the presumption's failure mode: a known error "remains in that
       state until a permanent fix is implemented **or the affected system is decommissioned**." The
       KEDB is explicitly a register of documented-and-unfixed items with no expiry. SNIPPET-ONLY;
       tertiary.

  Strength of challenge: Strong

  Summary: This is the most heavily and directly refuted item in the batch. The presumption states
  that disclosure discharges a breach; the literature's central finding is that repeated,
  unconsequenced deviation is the *definition* of normalisation of deviance, and Vaughan's founding
  case turns on exactly the point C2A2 has reached — the O-ring erosion at Challenger was known,
  documented and discussed before every launch, and the documented standard never officially changed
  while the actual practice moved. The practitioner formulation is nearly verbatim: repeated often
  enough without consequence, the deviation becomes the team's real standard even though the written
  one is untouched. Three further literatures converge. The disclosure-economics work goes further
  than "disclosure is insufficient" to "disclosure is sometimes counterproductive," and it names the
  mechanism as moral licensing — the discloser feels released by the act of disclosing, which is
  precisely the presumption's content restated as an empirical finding. The alert-fatigue data supply
  a dose-response curve: acceptance of a reminder drops ~30% for each repetition, so a fifteenth
  identical disclosure is, on the best available quantification, close to informationally inert
  regardless of how honestly it was made. And the technical-debt survivability data give the base
  rate for the underlying hope: 8.76% of documented debt items are ever removed. The one honest
  complication is that C2A2's disclosures are made in good faith, in the open, and are *requested* by
  Rule 12 — but the normalisation literature is explicit that the process "does not require
  negligence or malice." Good faith is not the protective factor; a ruling is. The register's own
  counter-instance is real and worth weighting: the QC sweep that stopped at one pair rather than
  doing two badly is a breach that changed an output instead of only being announced, and that is the
  behaviour the constraint was for.

  Specific risks: (a) A budget that exists on paper only — fifteen runs of breach with no ruling means
  the register can no longer distinguish a run that overran because the work demanded it from one that
  overran because overrunning is now routine; the constraint has lost its discriminating power, which
  is its entire function. (b) Silent amendment — per Vaughan, the operative standard has already
  moved; what has not moved is the document, so every future reader of the document is misinformed
  about how the system actually behaves. (c) Disclosure-fatigue at the gate — on Ancker et al.'s
  curve, the gate's probability of acting on breach report fifteen is a small fraction of its
  probability of acting on report one, which means the *system's own remedy* (surfacing) has been
  consumed. (d) Moral licensing — the strongest and least comfortable risk: the disclosure ritual may
  be actively raising the breach rate by removing the felt cost of breaching. This is testable (see
  below) and has not been tested. (e) Rule 12 is currently unfalsifiable as a control: it asks for
  surfacing, surfacing is being done perfectly, and the constraint is violated every time — so
  compliance with Rule 12 and violation of the budget are perfectly correlated, and no observation
  could show the control failing. (f) Compounds with PRESUMPTION-879: transparency diffuses
  responsibility to the recipient, and the recipient is unresponsive.

  Mitigations available:
    - **Set an expiry on unanswered disclosures.** After N unruled breaches, the constraint either
      auto-amends to the observed value (making the paper budget honest) or auto-hardens into a hard
      stop (making it real). Either is better than the current state, which is a constraint whose
      status is undefined. This is the single highest-value change identified in this batch.
    - Count and publish the breach series as a first-class metric with its own trend, so "fifteenth
      consecutive" is a number the system reacts to rather than a phrase in an evening summary.
    - Distinguish *announced* breaches from *acted-on* breaches in the record. The QC sweep's decision
      to stop at one pair is a categorically different event from a run that overran and said so, and
      the register currently files them alike.
    - Test the moral-licensing hypothesis directly rather than assuming good faith is protective
      (method below).
    - Do not respond to disclosure fatigue by making the disclosures louder or more frequent. The
      alert-fatigue literature says that is the intervention that makes it worse.
    - Treat the KEDB analogy seriously: if a breach is genuinely acceptable, record it as a
      *ruled waiver with an expiry date*, not as a standing violation. An accepted deviation with a
      review date is a normal engineering artefact; an unruled one is the thing Vaughan describes.

  STEELMAN:
    Item: PRESUMPTION-881
    Strongest counterargument: Normalisation of deviance is a theory about *concealed or unremarked*
    drift — its diagnostic feature is that the deviation stops being perceived as a deviation. C2A2's
    case is the exact inverse: every breach is named as a breach, in the breach's own language, and
    the evening summary is *counting them* and has noticed that fifteen have gone without a ruling.
    A deviation that the system explicitly tallies and flags as anomalous has not been normalised; it
    has been escalated and not yet answered. On this reading the presumption is not operating at all —
    the agents are not treating disclosure as discharge, they are treating it as the only action
    available to them within remit (which is PRESUMPTION-879's territory, not this item's), and the
    failure is wholly at the gate. Moreover, the alternative behaviours are worse: silently cutting
    corners to fit the budget would degrade outputs invisibly, and hard-stopping mid-task would
    produce truncated artefacts. Surfacing-and-continuing may be the least-bad option available, and
    the literature offers no evidence that a *counted, named, escalated* deviation carries the same
    risk as an unremarked one. The moral-licensing result also concerns disclosure to a *party who can
    act on it and adjust their reliance*; disclosure into silence does not obviously produce the same
    licensing, because there is no advisee to feel released from.
    What would need to be true for C2A2 to be safe: (i) the breach rate must be flat or falling, not
    rising — a rising rate under constant disclosure is the licensing signature and would settle the
    question; (ii) the *content* of the disclosures must not be converging on boilerplate, since
    identical form across three same-day instances is already weak evidence that the disclosure has
    become ritual; (iii) the breaches must be causally necessary — each run must be able to show that
    the work genuinely required the overrun, which is exactly what a constraint violated on every run
    can no longer demonstrate; (iv) the gate must eventually rule, because the counterargument
    depends entirely on the breach being *pending* rather than *tacitly accepted*, and after enough
    time those become the same thing; (v) at least one run must have *changed its behaviour* because
    of the budget — the QC sweep's stop-at-one-pair is the one instance, and one out of fifteen is a
    thin basis for saying the constraint is live.
    How to test: Three tests, all computable from the existing record. (1) **Breach-rate trend.** Plot
    breach magnitude (overrun as % of cap) against run index across all fifteen. A flat or rising
    slope under constant disclosure is direct evidence of licensing/normalisation; a falling slope is
    evidence the disclosure is working. (2) **Disclosure-text convergence.** Measure lexical
    similarity across the fifteen breach notes. The brief already observes that three same-day
    disclosures had "identical form"; if similarity is rising over time, the disclosure has become
    ritual and its informational content is near zero — the Ancker dose-response prediction made
    measurable. (3) **Behaviour-change count.** Count runs in which the constraint changed an output
    versus runs in which it produced only an announcement. The current count appears to be 1 : 14. A
    constraint with that ratio is, operationally, not a constraint. If all three tests point the same
    way the presumption is not merely challenged but demonstrated false in this system's own data,
    without recourse to any literature.

  Recommendation: CHALLENGED

  SYSTEMIC-RISK-FLAG:
    Date: 2026-08-26
    Affected items: PRESUMPTION-878, PRESUMPTION-879, PRESUMPTION-880, PRESUMPTION-881,
      PRESUMPTION-882, PRESUMPTION-883, PRESUMPTION-884
    Common vulnerability: **Every remedy path in this batch terminates at the same single, currently
      unresponsive human review gate, and not one of the seven presumptions conditions its behaviour
      on that gate's responsiveness.** PRESUMPTION-881 supplies the clearest quantitative evidence
      that the gate's silence is not neutral: on the alert-fatigue dose-response curve, fifteen
      unanswered disclosures have already consumed most of the remedy's efficacy, and on Vaughan's
      account the unanswered disclosure is not a pending request but an in-progress amendment to the
      standard.
    Literature basis: Vaughan's normalisation of deviance
      (https://en.wikipedia.org/wiki/Normalization_of_deviance); ~30% drop in reminder acceptance per
      repetition (Ancker et al. [attribution recalled], BMC MIDM 2017,
      https://bmcmedinformdecismak.biomedcentral.com/articles/10.1186/s12911-017-0430-8);
      disclosure-induced moral licensing (Cain, Loewenstein & Moore [attribution high-confidence];
      J Bus Ethics 2022, https://link.springer.com/article/10.1007/s10551-022-05226-7); 8.76%
      removal rate for documented technical debt items
      (https://onlinelibrary.wiley.com/doi/full/10.1002/smr.2425).
    Risk level: Critical
    Recommendation: Give unanswered disclosures an expiry that forces a disposition. See the identical
      note on PRESUMPTION-878, -879, -880, -882, -883 and -884.

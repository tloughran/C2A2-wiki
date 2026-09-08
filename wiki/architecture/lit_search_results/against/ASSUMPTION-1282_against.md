SEARCH-AGAINST-ASSUMPTION-1282:
  Date searched: 2026-09-08
  Original item: ASSUMPTION-1282
  Original statement: "The fix for this class of problem is procedural and external, not declarative and
    internal; a system that accepts declarations in lieu of procedure will tend to produce more of the
    thing declared, not less."
  Routed question (as narrowed by 14a): does the human-disclosure finding survive when the "reader" is
    an automated downstream agent and the annotation is a structured machine-readable tag rather than
    prose? The human-disclosure sources were read in the 09-07 cycle and were NOT re-searched here.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-1282
    Item type: ASSUMPTION (stated — quoted from an agent-authored risk flag: SYSTEMIC-RISK-FLAG
      2026-09-07, declaration-substitutes-for-procedure, High, filed by the delegated 15b subagent on
      ASSUMPTION-1274 / PRESUMPTION-918)
    Transform at each step:
      14a: Extracted verbatim; narrowed the routed question to the generalisation (machine reader,
        structured tag), since the human-case sources were read in the 09-07 cycle.
      15b: Searched for challenging literature (2026-09-08), AGAINST direction only, on (i) the transfer
        of the disclosure finding to a machine pipeline and (ii) the "procedural not declarative"
        prescription itself. Did not read the `for/` directory, `lit_search_returns.md`, or any 15a
        output.
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Logozzo, F., Fahndrich, M., Mosaad, I. & Hooimeijer, P., 2019. "Zoncolan: How Facebook uses
       static analysis to detect and prevent security issues." Engineering at Meta.
       [VERIFIED: full blog post retrieved and read this run] — Zoncolan rules are *declarations*: a
       source (where information comes from) and a sink (where it must not end up). The blog reports
       that in 2018 Zoncolan "helped find and triage more than 1,100 security issues with severity
       'significant' or higher," of which 46% were "flagged to code authors directly without the
       involvement of a security engineer; this typically also takes place before the code is landed."
       This is the exact configuration the routed question asks about — a structured, machine-readable
       annotation whose reader is an automated downstream consumer — and the annotation changes
       downstream behaviour at scale, pre-merge, without a human intermediary.
    2. Distefano, D., Fähndrich, M., Logozzo, F. & O'Hearn, P.W., 2019. "Scaling Static Analyses at
       Facebook." Communications of the ACM 62(8); and Meta's Pysa reporting.
       [NOT-verified — figures from search-result summaries; neither the CACM article nor the Pysa
       write-up was retrieved this run] — The commonly quoted figures are that Zoncolan accounted for
       43.3% of severe security bug detections, and that Pysa detected 44% of all security bugs found
       in Instagram's server-side Python in H1 2020. If these hold, declaration-driven analysis is the
       single largest detection channel, not a substitute for one.
    3. Bandrowski, A. et al., 2016 (Resource Identification Initiative; Bandrowski & Martone, 2016,
       "RRIDs: A Simple Step toward Improving Reproducibility through Rigor and Transparency of
       Experimental Methods").
       [ABSTRACT-ONLY / secondary — the figure was read this run in a secondary source (paasp.net
       article, retrieved in full) which states: "With the RRID, 'identifiability' of antibodies
       increases from 50% to well over 90%." The primary Bandrowski et al. paper was NOT retrieved;
       PMC was blocked by CAPTCHA this run. The claim resting on this source is only that a structured
       identifier measurably outperformed prose description of the same thing] — This is the sharpest
       counterexample to the transfer. The failure mode the human-disclosure literature documents —
       a qualification written in prose does not survive downstream — is precisely what a structured,
       resolvable tag fixes. Same information, same downstream readers, format changed, behaviour
       changed.
    4. Gao, Z., Bird, C. & Barr, E.T., 2017. "To Type or Not to Type: Quantifying Detectable Bugs in
       JavaScript." ICSE 2017.
       [VERIFIED: title, authors and venue confirmed via UCL Discovery and Microsoft Research listings;
       full text NOT retrieved and the frequently quoted "15%" figure is NOT confirmed by anything read
       this run] — The design of the study is the load-bearing point, not the number: declarative type
       annotations, consumed mechanically, detect a measurable fraction of real, already-fixed public
       bugs. A declaration plus a checker is an enforcement mechanism.
    5. Hu, H., Wang, Y., Rubin, J. & Pradel, M., 2025. "An Empirical Study of Suppressed Static Analysis
       Warnings." Proc. ACM Softw. Eng. 2, FSE, Article FSE014. DOI 10.1145/3715729.
       [VERIFIED: PDF retrieved from software-lab.org; abstract and Introduction read this run] —
       Suppressions are "relatively common, e.g., with a total of 7,357 suppressions in 46 Python
       projects"; "the number of suppressions in a project tends to continuously increase over time";
       and "50.8% of all suppressions do not affect any warning and hence are practically useless."
       This challenges the *prescription*: an external, procedural, blocking control is routinely
       neutralised by a one-line declaration, the neutralisations accumulate monotonically, and half of
       them are vestigial. Procedure degrades into declaration by default.
    6. van der Sijs, H., Aarts, J., Vulto, A. & Berg, M., 2006. "Overriding of Drug Safety Alerts in
       Computerized Physician Order Entry." J Am Med Inform Assoc 13(2):138–147. DOI 10.1197/jamia.M1809.
       [VERIFIED: full text retrieved and read this run] — "Drug safety alerts are overridden by
       clinicians in 49% to 96% of cases." Abookire et al. (reviewed therein) found override rates
       rising "from about 50% to 75% during a five-year period, indicating a declining compliance to
       safety alerts." An external, interrupting, procedural control is overridden most of the time and
       its force decays with exposure. "External and procedural" is not by itself a safety property.
    7. Urbach, D.R., Govindarajan, A., Saskin, R., Wilton, A.S. & Baxter, N.N., 2014. "Introduction of
       Surgical Safety Checklists in Ontario, Canada." New England Journal of Medicine 370:1029–1038.
       [NOT-verified — findings from search-result summaries of PubMed/NEJM listings; full text not
       retrieved this run] — Across 101 hospitals with mandated checklist adoption, adjusted mortality
       moved from 0.71% to 0.65% and did not reach significance; no significant reduction in
       complications. The canonical "make it procedural and external" intervention, mandated at
       population scale, produced no measurable effect.
    8. Blanken, I., van de Ven, N. & Zeelenberg, M., 2015. "A Meta-Analytic Review of Moral Licensing."
       Personality and Social Psychology Bulletin 41(4):540–558; with Urban, Bahník & Kohlová, 2019 and
       Rotella & Barclay, 2020 (failed replications).
       [NOT-verified — all three cited from search-result summaries; none retrieved this run] — The
       meta-analysis (91 studies, 7,397 participants) puts the licensing effect at d ≈ 0.31 with
       published effects larger than unpublished, i.e. publication bias; several preregistered studies
       fail to replicate. Limb 2 of the assumption ("will tend to produce more of the thing declared")
       is the licensing mechanism. In humans it is a small, contested effect; in a pipeline where no
       agent gains anything from having declared, there is no mechanism at all.

  Strength of challenge: Strong (on the transfer to the machine/pipeline case); Moderate (on the
    "procedural and external" prescription)

  Summary: The generalisation does not survive as stated, and it fails in an interesting way: in a
  machine pipeline the declarative/procedural distinction largely dissolves. A declaration with a
  mechanical consumer *is* a procedure — Zoncolan's source/sink rules, a type annotation, a taint label
  and an RRID are all declarations, and all of them change downstream outcomes at scale precisely
  because no human reader stands between the annotation and the action. Conversely a procedure with no
  enforcement is a declaration: Hu et al. (2025) show external blocking analysers being neutralised by
  one-line suppressions that accumulate monotonically and are half-vestigial, and van der Sijs et al.
  (2006) show an external, interrupting control overridden 49–96% of the time with compliance decaying
  over five years. What actually predicts effect is neither the declarative/procedural axis nor the
  internal/external axis; it is whether an unbypassable mechanism consumes the artefact. The
  human-disclosure result the flag generalises from depends on a *reader who may decline to act* and, in
  its second limb, on a *declarer who benefits from having declared*. Neither condition is present when
  the reader is a deterministic consumer of a structured tag. The second limb is additionally weak at
  source: moral licensing meta-analyses put the effect at d ≈ 0.31 with evident publication bias and
  several preregistered replication failures, so the mechanism being exported is small and contested even
  in its home domain. The RRID case is the cleanest inversion: the very failure the disclosure literature
  documents — a qualification stated in prose is lost downstream — is what a structured identifier fixed,
  taking identifiability from about 50% to over 90%.

  Specific risks: (a) The flag is currently shaping REVISE-437/438 toward procedural, external controls
  on the strength of an untested transfer; if the transfer is wrong, the system will spend its scarce
  design effort building gates rather than building consumers, and gates without consumers are the exact
  artefact the flag warns against. (b) The prescription is self-undermining: an unenforced procedure
  is a declaration, so "make it procedural" delivered as a written recommendation is itself a
  declaration in lieu of procedure. The 09-07 flag is at present an instance of the thing it names.
  (c) Rejecting structured tags on the strength of the human-prose finding forfeits the one intervention
  with direct evidence in the machine case (Zoncolan, type checkers, RRID), i.e. the transfer error has
  an opportunity cost, not merely an accuracy cost. (d) Limb 2 exported into an agent pipeline predicts
  that tagging will *increase* the tagged behaviour; if the system acts on that prediction it may
  suppress provenance tagging, which reduces the observability the audit layer depends on. That is a
  live risk given REVISE-437's ABSTRACT-ONLY tag is exactly such an annotation.

  Mitigations available: Reframe the design axis from declarative-vs-procedural to
  *consumed-vs-unconsumed*. For every tag the system mints (ABSTRACT-ONLY, NOT-verified,
  SEARCHED-15b, escalation status), name the mechanical consumer and the action it takes, and treat a
  tag with no named consumer as unbacked. Where a consumer exists, measure it the way the static-analysis
  literature does: fire rate, action-changed rate, suppression/override rate, and suppression growth over
  time — Hu et al.'s "useless suppression" statistic is directly portable to this repo (count tags that
  never gate anything). Retire limb 2 of the assumption for the machine case unless a mechanism is
  proposed; retain it for the human-facing case where it was established. Finally, apply the flag to
  itself: the 09-07 SYSTEMIC-RISK-FLAG should carry a procedural consumer, or be recorded as a
  declaration.

  Search scope: Preliminary — 6 queries plus 3 document retrievals, deliberately excluding the
  human-disclosure literature per the routing note. Covered: taint/source-sink annotation in production
  (Meta), gradual typing as declarative bug detection, structured identifiers vs prose in scientific
  reporting, suppression of external analysers, override of external interrupting controls, mandated
  procedural checklists, and the replication status of the licensing mechanism. Not covered: W3C PROV
  downstream consumption studies specifically (searched for but not reached), FAIR-data qualifier
  attrition, information-flow-control deployments outside Meta, and any study directly comparing prose
  vs structured caveats in an LLM-agent pipeline — that last is the item's real question and I found no
  study of it. Broader search recommended there; the challenge as it stands rests on adjacent-domain
  counterexamples rather than on a direct test.

  Recommendation: CHALLENGED

STEELMAN:
  Item: ASSUMPTION-1282
  Strongest counterargument: The declarative/procedural dichotomy is a category error once the reader is
  a machine. What made prose disclosure fail was a human reader free to skim past the caveat and a human
  declarer who felt discharged by declaring; strip out the discretionary reader and the interested
  declarer and neither limb has a mechanism left. In their place, structured declarations consumed by
  automata are among the most effective controls anyone has measured: Meta's Zoncolan rules are nothing
  but declared sources and sinks, and they surfaced over a thousand significant-or-worse security issues
  in a single year with nearly half routed to authors before the code landed; an RRID is nothing but a
  declared identifier, and it lifted antibody identifiability from about half to over nine in ten. The
  prescription fares no better than the thing it displaces: mandated external checklists across 101
  Ontario hospitals moved mortality not at all; external analysers are silenced by one-line suppressions
  that grow monotonically and are half of them useless; external interrupting alerts are overridden in
  half to nearly all cases and compliance decays year on year. And the mechanism being generalised —
  licensing — is a d ≈ 0.31 effect with publication bias and preregistered replication failures. So the
  assumption exports a small contested human effect into a domain that lacks its preconditions, and
  prescribes a remedy that the same literature shows failing in the same way. The distinction that
  actually carries the weight is not declarative versus procedural but consumed versus unconsumed.
  What would need to be true for C2A2 to be safe: The system's tags would have to have no mechanical
  consumers — that is, every tag is read only by an agent that may exercise discretion about whether to
  honour it, and the agents that mint tags gain standing or closure from having minted them. Under those
  conditions the human finding transfers, because the conditions are the human conditions. If instead any
  tag is consumed by something that cannot decline (a script that refuses promotion, a check that fails
  a run), the assumption's prediction does not apply to that tag.
  How to test: Enumerate every provenance/status tag the layer mints and classify each as *consumed*
  (some non-discretionary mechanism reads it and changes behaviour) or *unconsumed*. Then measure two
  numbers on this repo's own history: for consumed tags, the rate at which the mechanism actually
  changed an outcome; for unconsumed tags, the survival rate of the tag through one downstream retelling.
  The assumption predicts unconsumed tags fail *and* that their presence increases the tagged behaviour —
  so also count, before and after each tag's introduction, the frequency of the behaviour it annotates
  (e.g. did ABSTRACT-ONLY reading go up after REVISE-437?). If consumed tags show a nonzero
  outcome-change rate, the generalisation is false as stated. If the behaviour frequency did not rise
  after tagging, limb 2 is false for this system.

SEARCH-AGAINST-PRESUMPTION-896:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-896
  Original statement: [inferred] Filing a defect discharges the obligation to fix it.
  Generalizable limb searched: Whether disclosure/reporting measurably substitutes for remediation —
    evidence on moral licensing and the perverse effects of disclosure, and on the fate of filed
    defects in practice.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 2 queries run (Pass 1 only; Priority Medium,
    so no Pass 2 by budget rule); no full-text reads. The moral-licensing limb returned strong
    peer-reviewed sources (a meta-analysis and the foundational disclosure experiment); the
    defect-backlog limb returned only practitioner blogs with unsourced heuristics, and is weak.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-896
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from a pattern in which surfacing a defect into the register was treated as the
        terminal action, with no tracked commitment to repair.
      15b: Searched for challenging literature (2026-08-31)
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Cain, Loewenstein & Moore, 2005. "The Dirt on Coming Clean: Perverse Effects of Disclosing
       Conflicts of Interest." (Journal of Legal Studies; identified via Loewenstein's "Disclosure:
       Psychology Changes Everything," Carnegie Mellon.) — The foundational experimental result that
       disclosure can worsen rather than improve behaviour. The mechanism as described in the search
       results is directly on point: disclosure creates "a moral license that emboldens agents and
       encourages them to act in self-serving ways," because the perception that the other party has
       been warned makes the discloser feel less responsible for the underlying problem. This is
       precisely the structure of "I filed it, so it is handled."
    2. Blanken, van de Ven & Zeelenberg, 2015. "A Meta-Analytic Review of Moral Licensing."
       Personality and Social Psychology Bulletin, 41(4). — Meta-analytic support for the licensing
       effect: behaving morally at one point makes subsequent problematic behaviour more likely.
       Establishes the effect as replicated across studies rather than a single finding. (Noted for
       15c: moral licensing has been part of the broader replication debate in social psychology;
       the meta-analysis reports a small-to-moderate effect and I did not read it in full.)
    3. Cain, Loewenstein & Moore, and successors, via The Center for Growth and Opportunity.
       "Keeping a Clean Reputation: More Evidence on the Perverse Effects of Disclosure." — Further
       evidence in the same direction; the framing that a disclosure policy "may prove harmful"
       where its licensing magnitude is not appreciated by the parties relying on it. Snippet-level;
       working-paper-grade source.
    4. Ethics Unwrapped (UT Austin), "Moral Equilibrium," and the moral credit / moral credential
       models as characterised in the search results (including a moral licensing study in Frontiers
       in Psychology, PMC6411788). — Describes the mechanism by which prior good acts accumulate
       "moral credits" that make later omissions feel permissible. Explanatory framing rather than
       independent evidence.
    5. Practitioner defect-management sources (Full Scale, "Managing the Bug Backlog"; minware, "Bug
       Closure Rate"; Bug0, "Defect management: process from triage to closure"; Jonathan West on
       triage at scale). — Report widely-repeated heuristics that defects open beyond ~90 days, and
       certainly beyond 12 months, are unlikely ever to be fixed; that backlogs accumulate hundreds
       of aged tickets that "nobody trusts"; that "closed does not always mean fixed" because
       tickets close as duplicate, invalid, or deferred; and that closure-rate metrics can be
       inflated by sweeping low-severity items while severe ones stay open. IMPORTANT CAVEAT: these
       are unsourced practitioner heuristics, not measurements. I found no empirical study
       quantifying filed-versus-fixed rates. This limb is weak and should not be leaned on.
    6. Jonathan West (Medium), on triage. — Contains the directly relevant normative statement that
       documenting a bug as a known issue "is fine, but is very much a last resort versus
       fixing/mitigation." Opinion, not evidence; cited because it names the exact distinction at
       issue.

  Strength of challenge: Moderate

  Summary: The challenge splits cleanly into a well-supported general mechanism and a poorly
    evidenced specific application. The mechanism is solid: the disclosure literature, anchored by
    Cain, Loewenstein & Moore and supported by a meta-analysis of moral licensing, establishes that
    the act of disclosing a problem can reduce felt responsibility for it, and can do so precisely
    because the discloser believes the disclosure discharged something. This is not a claim that
    reporting is bad — it is a claim that reporting and fixing are separate obligations, and that
    completing the first can psychologically substitute for the second in a way that the actor does
    not notice. Applied here, filing a defect into the register may function as the moral credit
    that licenses leaving it unfixed. The specific application is where evidence thins out badly: I
    found no study measuring what fraction of filed software defects are ever remediated, only
    practitioner folklore about 90-day and 12-month thresholds. I am not willing to treat that as
    evidence, and I flag it as the weakest link in this file. The honest position is that the
    licensing mechanism gives good theoretical grounds to doubt the presumption, and that the
    presumption is in any case suspicious on structural grounds independent of any literature —
    filing creates a record, and a record is not a repair. Note also the interaction with the rest
    of my batch: C2A2's register is *itself* the defect-filing system, so a licensing effect here
    would manifest as a growing register of accurately-described unfixed problems, which reads as
    diligence.

  Specific risks: If filing does discharge the felt obligation, C2A2 accumulates an accurate and
    growing catalogue of known defects that are never repaired, while the accuracy of the catalogue
    is itself experienced as evidence of a healthy process. The specific danger is that the register
    is optimised for the wrong output: it measures items surfaced rather than items closed, so a
    pipeline that finds a great deal and fixes nothing scores identically to one that fixes
    everything. Second-order risk: aged unfixed defects interact with the other items in this batch
    — a filed-but-unfixed integrity gap (see PRESUMPTION-895) is functionally identical to an
    undetected one, since neither results in repair.

  Mitigations available: (a) Track a close/fix rate, not just a file rate, so remediation is
    measured rather than presumed; (b) age the backlog visibly and force an explicit decision at a
    threshold — fix, formally accept the risk, or withdraw — so that "unfixed" becomes a stated
    choice rather than a default; (c) distinguish "closed as fixed" from "closed as deferred/
    duplicate/invalid" in the register schema, since the practitioner literature identifies conflation
    of these as the standard way closure metrics mislead; (d) require that any item filed at high
    severity carry a named next action, which is the standard structural counter to licensing —
    licensing operates on vague obligations, not on specific committed ones; (e) at minimum, restate
    the norm explicitly: filing discharges the obligation to *disclose*, and nothing else.

  STEELMAN:
    Strongest counterargument: The presumption as stated may be a strawman of a reasonable division
      of labour. In a pipeline with separated roles, the assumption-extraction stage legitimately
      *should* terminate at filing — its job is surfacing, and remediation belongs to a different
      stage with different information and authority. An extractor that tried to fix everything it
      found would exceed its remit, act on incomplete context, and destroy the auditability that
      comes from having discovery and repair be separate recorded steps. On that reading, filing
      genuinely does discharge *this agent's* obligation, and the real question is not about moral
      licensing at all but about whether a downstream remediation stage exists and functions. The
      moral licensing literature also concerns individual psychology under self-interest; a
      stateless agent with no continuity of self-regard is a poor candidate for accumulating "moral
      credits."
    What would need to be true for C2A2 to be safe: A remediation stage must actually exist,
      be triggered by filings rather than by chance, and have its throughput measured. The handoff
      must be explicit — an item's status must record that it was passed on, not merely written down.
      And someone or something must own the aggregate: if no stage is accountable for the size and
      age of the unfixed set, the division of labour has a hole in it regardless of how clean each
      individual stage is. If a functioning downstream remediation stage with measured throughput
      exists, this challenge largely does not apply.
    How to test: Straightforwardly measurable from the register's own history. Take all items filed
      over some past window, classify each as fixed / accepted / still open, and compute the fix
      rate and the age distribution of the still-open set. If the fix rate is near zero or the age
      distribution has a long right tail with no accepted-risk annotations, the presumption is
      operating in practice whatever the intended design. This requires no literature and no new
      instrumentation — the data already exists in the register.

  Recommendation: PARTIALLY-CHALLENGED

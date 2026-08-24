SEARCH-FOR-PRESUMPTION-833:
  Date searched: 2026-08-18
  Original item: PRESUMPTION-833
  Original statement: That an accusation costs nothing. The status lifecycle has terminal states for a claim that fails verification and none for a flag that is withdrawn; four flags were retracted in one day and each cost a later run real budget to discover.

  Proposition searched FOR: Per the item's own stated search angle, the proposition tested in the supportive direction is the *negation* of the presumption as worded — i.e. that a false or subsequently-withdrawn accusation carries real, non-zero, and only-partly-recoverable cost. Support below is support for that concern, not for the presumption's literal wording. Downstream readers should not read "SUPPORTED" here as "accusations are costless."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-833
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred by noticing that all four of today's retractions ran opposite to the week's established direction, and checking `provenance_protocol.md` for a terminal state covering a withdrawn flag. There is none.
      15a: Searched for supporting literature; found a large, well-replicated cognitive literature showing retracted claims continue to influence inference after retraction, plus operational evidence that high false-positive rates degrade detection through desensitisation.
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Lewandowsky, Stephan; Ecker, Ullrich K. H.; Seifert, Colleen M.; Schwarz, Norbert; Cook, John, 2012. "Misinformation and Its Correction: Continued Influence and Successful Debiasing." Psychological Science in the Public Interest 13(3): 106–131. — Review establishing the continued influence effect: a retraction will at most halve references to the misinformation even when the retraction is acknowledged and demonstrably remembered, and in some studies does not reduce reliance at all; explicit warnings reduce but do not eliminate the effect. Direct support for the claim that withdrawing a flag does not restore the prior state.
    2. Johnson, Hollyn M.; Seifert, Colleen M., 1994. "Sources of the continued influence effect: When misinformation in memory affects later inferences." Journal of Experimental Psychology: Learning, Memory, and Cognition 20(6): 1420–1436. — The canonical paradigm establishing that corrected information continues to affect downstream inference. Independently replicated: see Ecker-tradition replication published in Acta Psychologica (2023), which reports the effect persisting under protocol deviation, with a smaller effect size.
    3. Alert- and alarm-fatigue evidence base (clinical monitoring and security operations). Non-actionable alert rates routinely exceed 70% in physiological monitoring; in security operations, desensitisation from sustained alert volume causes analysts to miss, delay or ignore genuine signals, with a reported 42% of alerts going entirely uninvestigated and false positives named as the top detection challenge by 73% of security teams. [Practitioner and vendor sources, plus arXiv:2601.04486 "Decision-Aware Trust Signal Alignment for SOC Alert Triage"; figures are industry-reported and not peer-reviewed — treat as indicative of magnitude only, not as measured constants.] — Supports the second cost channel: false positives consume triage capacity and degrade response to true positives.

  Strength of support: Strong (for the persistence channel); Moderate (for the alarm-fatigue channel)

  Summary: The presumption that an accusation is costless is contradicted by a strong and well-replicated cognitive literature. Lewandowsky et al. (2012) establish that retraction is not an eraser: the retracted claim continues to inform inference at roughly half strength or more, even among people who remember the retraction and were warned in advance. Applied to 833, this means a withdrawn flag leaves residue in whatever downstream reasoning consumed it, and the absence of a terminal state for withdrawn flags in `provenance_protocol.md` means that residue is not even tracked, let alone corrected. The second channel is the resource cost the item observed directly: the alerting literature across clinical monitoring and security operations documents that high false-positive volume produces desensitisation, so the cost of a false flag is not confined to the effort of retracting it but is also paid as reduced sensitivity to real ones. The asymmetric-loss framing in that literature is relevant in an instructive way: systems are typically tuned on the assumption that misses cost far more than false alarms, which is exactly the assumption that generates the false-positive burden 833 identifies — the presumption is not idiosyncratic to C2A2 but is the standard design default.

  Caveats: One located source runs the other way and is recorded here for honesty rather than suppressed: "Does Exonerating an Accused Researcher Restore the Researcher's Credibility?" (PMC4430488) reports that exoneration *does* restore an accused researcher's credibility, which is a partial counter-example to unbounded persistence in the specific setting of formal institutional clearance. Full assessment of that line belongs to 15b. Separately, the continued influence literature is about human memory and inference; whether it transfers to an agent pipeline whose "memory" is a document store depends on whether retracted flags are physically removed or merely superseded — if removal is complete the mechanism may not apply, and no located source addresses machine-mediated correction. Source 3's numbers come from vendor and practitioner reporting with obvious commercial incentives and should not be cited as measured rates. Finally, none of the located work quantifies the cost of a *withdrawn* accusation specifically, as distinct from an uncorrected false one.

  Search scope: continued influence effect; misinformation correction and retraction; persistence of retracted findings; alarm fatigue and alert fatigue; false-positive cost in screening, audit and transaction monitoring; asymmetric loss functions in inspection; reputational cost of false accusation and exoneration. Comprehensive on the continued-influence arm; preliminary on the formal decision-theoretic arm (asymmetric loss in optimal inspection/screening design), where a broader search would likely add established statistical-decision-theory results this pass did not reach.

  Recommendation: SUPPORTED

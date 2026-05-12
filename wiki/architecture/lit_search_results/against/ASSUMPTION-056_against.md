SEARCH-AGAINST-ASSUMPTION-056:
  Date searched: 2026-04-21
  Original item: ASSUMPTION-056
  Original statement: "An honest null is more valuable than thin proposals."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-056
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from Hawkins/Hoffman specialist run
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Convenient-null literature / "file-drawer problem" (Rosenthal 1979; Scargle 2000): null outputs are often under-interrogated. Without documented search scope, "null" can mean "I looked and found nothing" or "I did not look thoroughly" — and the downstream consumer cannot distinguish. Self-reported null without audit trail collapses these two categories.
    2. Self-assessment bias literature (Dunning-Kruger 1999; Kruger & Dunning later replications 2008-2020): self-evaluation of judgment quality is systematically biased. A specialist declaring its own null "honest" is vulnerable to motivated reasoning — especially under time pressure or when "I already rejected X" is the convenient frame.
    3. Minimum-information / "weak signal beats no signal" literature (Edward Tufte on "noise is information about the process"; intelligence-analysis literature on weak-signal aggregation): in some domains, weak signals aggregated over time provide better coverage than null-preference. Rejecting thin proposals means information loss at the specialist layer that cannot be recovered downstream.
    4. Quality-score-based alternatives (learning-to-rank literature; expert-review systems): instead of a binary "emit null OR emit thin proposal," a calibrated system would emit all candidates with quality scores, letting the downstream filter choose thresholds. Null-preference preempts that flexibility.
    5. Specialist self-validation anti-pattern literature (ties to internal PRESUMPTION-015 self-referential circularity; PRESUMPTION-067 specialist self-eval): when the specialist is the sole evaluator of its own null quality, the system has no independent check on the null-quality claim. Ties to the CRITICAL SELF-AWARENESS-META cluster.

  Strength of challenge: Moderate

  Summary: The stance has a well-documented failure mode: absent an independent audit, "honest null" can silently degrade into "convenient null" — the specialist gives up early, declares success, and the downstream consumer cannot distinguish. Literature on the file-drawer problem, self-assessment bias, and weak-signal aggregation all caution against treating self-reported nulls as first-class without a criterion. The alternative — emit all candidates with quality scores — is standard in search/recommendation systems and preserves flexibility. The stance is also structurally similar to several items in the CRITICAL SELF-AWARENESS-META cluster: self-referential judgment without independent cross-check.

  Specific risks: (a) False-null rate cannot be measured without ground truth, so the system has no feedback signal on specialist null quality; (b) specialist rejection reasons go unaudited — the three Hoffman-candidate rejections (already-captured v2 preprint; abstract-less Harvard talk; out-of-window Nov 2025 MBS interview) may be correct or may reflect unexamined criteria; (c) joins PRESUMPTION-067 (specialist self-eval) which extends the self-referential cluster to the specialist layer.

  Mitigations available: (a) Pair "honest null" with a downstream filter-audit criterion (analogous to the PRESUMPTION-053 remediation); (b) change the output format to "all candidates with quality scores" plus an explicit "specialist recommendation: null" — gives downstream consumers flexibility without losing information; (c) rotate specialist coverage to detect specialist-specific null patterns (e.g., Hawkins/Hoffman has null-days but Levin does not).

  Recommendation: PARTIALLY-CHALLENGED (methodologically defensible as a stance; requires a criterion for "honest" and an independent audit to avoid degrading into convenient-null; standalone it extends self-referential circularity to specialist layer)

  STEELMAN:
    Item: ASSUMPTION-056
    Strongest counterargument: "Honest null > thin proposals" smuggles a self-judgment claim: that this particular null is honest. Without an independent audit, the distinction between honest null and convenient null collapses to the specialist's own assessment — a well-documented failure mode (Dunning-Kruger; file-drawer problem). The literature on weak-signal aggregation notes a third alternative — emit all candidates with quality scores, letting the downstream filter choose — which preserves information that null-preference destroys. The stance is methodologically sound as a design principle; it is methodologically incomplete as an operational default without a criterion or audit.
    What would need to be true for C2A2 to be safe: Independent filter-audit of specialist null-days; documented "honest" criterion; periodic false-null-rate measurement; or adopt the emit-all-with-quality-scores alternative.
    How to test: Run a second-pass audit on the three 2026-04-21 Hawkins/Hoffman rejections against a broader candidate set; measure false-rejection rate over 30 days of specialist runs; compare against emit-all-with-scores alternative on the same candidate streams.

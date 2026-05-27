SEARCH-AGAINST-PRESUMPTION-239:
  Date searched: 2026-05-23
  Original item: PRESUMPTION-239
  Original statement: "The reviewer presumes the transcript_authenticity_check FABRICATION verdict on fidelity-passing summary renders is a false-positive, not a real signal."

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-239
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred: the reviewer dismissed a FABRICATION verdict as classifier error.
      15b: Searched for challenging literature (training-corpus grounding per ASSUMPTION-199 convention; FLAG E noted)
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Maynez et al. (2020) "On Faithfulness and Factuality in Abstractive Summarization." — Abstractive summaries frequently contain intrinsic/extrinsic hallucinations; a fabrication verdict on a summary may be detecting a real fault, not noise.
    2. Kryscinski et al. (2020) "Evaluating the Factual Consistency of Abstractive Text Summarization" (FactCC). — Factual inconsistency in summaries is common and detectable; "fidelity-passing" by one check does not entail authenticity.
    3. Alarm-dismissal anti-pattern / automation complacency (Parasuraman & Riley 1997). — Dismissing a flag as a false positive without adjudication is a recognized failure mode; it is the same "assume the alarm is wrong" move the project's own honesty layer is meant to resist (couples ASSUMPTION-198 transcript-fabrication family).

  Strength of challenge: Moderate-Strong

  Summary: The presumption may be exactly backwards: abstractive summary renders are a well-documented site of genuine hallucination, so a FABRICATION verdict could be a true signal that the summary introduced content not in the source, even when a separate "fidelity" check passes (the two checks measure different things). Treating the verdict as a false positive WITHOUT a labeled error analysis is automation complacency and self-undermines the project's own anti-fabrication commitment. The challenge is moderate-strong: it does not prove the verdict is correct, but it shows the dismissal is unverified and risky on an honesty-critical signal.

  Specific risks: A genuinely fabricated/hallucinated summary render is shipped because its FABRICATION alarm was waved off as classifier noise, corrupting the corpus's authenticity guarantees.

  Mitigations available: Adjudicate before dismissing — run a small labeled error analysis (sample flagged renders, hand-check against source) to estimate the false-positive rate; only then tune/trust the classifier (OPEN-063); never act on "false positive" as an assumption.

  Recommendation: CHALLENGED (moderate-strong)

  STEELMAN:
    Item: PRESUMPTION-239
    Strongest counterargument: Abstractive summarization is a documented source of real hallucination, and a separate "fidelity" pass measures something different from authenticity, so a FABRICATION verdict on a fidelity-passing summary render may be a true positive. Dismissing it as classifier error without a labeled error analysis is automation complacency on an honesty-critical signal — the very "assume the alarm is wrong" move the system's anti-fabrication commitment (ASSUMPTION-198) exists to prevent.
    What would need to be true for C2A2 to be safe: The false-positive hypothesis is confirmed by a labeled error analysis before any flagged render is trusted; until then the verdict is treated as a live signal.
    How to test: Sample flagged renders and hand-check each against its source transcript; a non-trivial true-positive rate refutes "uniformly false-positive."

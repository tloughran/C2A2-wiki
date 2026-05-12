SEARCH-AGAINST-PRESUMPTION-074:
  Date searched: 2026-04-27
  Original item: PRESUMPTION-074
  Original statement: "Cross-tradition convergences can be reliably recognized by specialist agents without independent expert verification"

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-074
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as recurrent unstated premise
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. LLM hallucination literature (Ji et al. 2023 survey; Maynez et al. 2020 on faithful summarization): LLMs systematically generate plausible-but-incorrect cross-domain analogies; the very plausibility is what makes the failures hard to detect without external verification.
    2. Cross-domain pattern over-detection (Bowman et al. 2022; Tang et al. 2023): single-pass LLM cross-domain reasoning is known to over-detect surface analogies that don't survive technical scrutiny.
    3. Specialist-as-confirmation-bias literature: a specialist agent fine-tuned on a tradition is *more* likely to find that tradition's patterns elsewhere — a known confirmation-bias effect that increases false-positives in cross-domain detection.
    4. LLM-as-judge calibration (Zheng et al. 2023, Stelmakh et al. 2024): LLMs systematically over-rate agreement and under-detect disagreement; cross-tradition convergence detection is the high-agreement direction the bias favors.
    5. Three concrete C2A2 cases this week: ASSUMPTION-063 (Levin/Hoffman/Kastrup convergence), ASSUMPTION-065 (Carroll/Arkani-Hamed convergence), ASSUMPTION-066 (Wolfram method-export) all hinge on this presumption; if it's wrong, all three are systemically affected.

  Strength of challenge: Strong

  Summary: The literature consensus is that single-agent or single-pass cross-domain pattern recognition is systematically over-confident and over-detects convergences that don't survive technical scrutiny. The "without independent expert verification" framing is precisely what the literature warns against. Three of this week's specialist-recognition assumptions depend on this presumption; if it fails, they all fail. This is a candidate for SYSTEMIC-RISK-FLAG.

  Specific risks: (a) Three same-week ASSUMPTIONs (063, 065, 066) inherit a contested recognition reliability; (b) LLM-pattern-matching false-positives propagate into C2A2 syntheses without verification; (c) the system is structurally susceptible to a recurring failure mode.

  Mitigations available: (a) Add an independent-verification tier for high-stakes specialist-recognition claims; (b) require species-level technical evidence (not just genus-level pattern) before treating a convergence as load-bearing; (c) flag specialist-recognition claims explicitly so downstream consumers can apply skepticism.

  Recommendation: CHALLENGED (the "without independent expert verification" framing is contradicted by the LLM-evaluation literature)

  STEELMAN:
    Item: PRESUMPTION-074
    Strongest counterargument: LLMs are good at recognizing surface patterns and bad at distinguishing surface patterns from technical convergence; this is a well-documented failure mode. Trusting specialist agents to recognize cross-tradition convergences without verification is exactly the architectural pattern the LLM-evaluation literature warns against. Three of this week's assumptions depend on this presumption — that's a systemic dependency, not an isolated case.
    What would need to be true for C2A2 to be safe: (a) High-stakes specialist-recognition claims are verified independently (by Tom or by an external reviewer); (b) species-level technical content is required for cross-tradition convergence claims; (c) the system explicitly tracks the false-positive rate of specialist recognition over time.
    How to test: Sample 5 cross-tradition convergence claims from past specialist agents; submit each to independent expert review; if false-positive rate exceeds 30%, the presumption is empirically falsified.

  SYSTEMIC-RISK-FLAG:
    Date: 2026-04-27
    Affected items: ASSUMPTION-063, ASSUMPTION-065, ASSUMPTION-066, ASSUMPTION-067 (all four hinge on specialist recognition reliability)
    Common vulnerability: Single-specialist-agent cross-tradition recognition without independent verification
    Literature basis: Ji et al. 2023; Bowman et al. 2022; Stelmakh et al. 2024; LLM-as-judge calibration literature
    Risk level: HIGH
    Recommendation: Add independent-verification tier for high-stakes specialist-recognition claims before they become operational premises.

SEARCH-AGAINST-PRESUMPTION-197:
  Date searched: 2026-05-19
  Original item: PRESUMPTION-197
  Original statement: "agent-significance-judgment-as-bounded presumption; out-of-window exception filter grants unbounded inclusion discretion when agent can articulate cross-tradition signals."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-197
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — implicit boundedness assumption
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Tversky & Kahneman (1974). "Judgment under Uncertainty." Science. — Foundational: discretionary judgment under salience cues is systematically biased; the ability to articulate rationale does not bound the bias and often rationalizes it.
    2. Klein, G. (1998). "Sources of Power." — Expert judgment is calibrated only within domains of extensive feedback; LLM curation agents do not receive comparable feedback on their cross-tradition inclusion decisions.
    3. Bender et al. (2021). "On the Dangers of Stochastic Parrots." FAccT. — LLM-style judgments of "richness" or "significance" reflect training-distribution statistics, not ground truth; the articulation is a confabulation, not a calibration.
    4. Mercier, H. & Sperber, D. (2017). "The Enigma of Reason." Harvard. — Argumentative theory of reason: humans (and likely LLMs) generate post-hoc rationales for decisions made by other mechanisms; articulation is evidence of fluency, not of bounded judgment.
    5. Nisbett, R. & Wilson, T. (1977). "Telling more than we can know." Psychological Review. — Classic: subjects confabulate rationales for decisions they did not actually make on those grounds; the articulation does not bound the discretion.
    6. Yudkowsky, E. & Soares, N., 2017 onwards — AI-safety literature on instructive/reward-misspecification: "agent can articulate why" is a notoriously weak constraint on agent behavior.

  Strength of challenge: Strong

  Summary: The literature is heavily against the presumption that articulation-of-rationale bounds discretion. Heuristics-and-biases, naturalistic decision-making, LLM-evaluation, and confabulation literature all converge: the ability to produce a plausible "cross-tradition signal" story is evidence of fluency, not of calibration. Without an external feedback loop (Tom reviews and accepts/rejects the exception, with the rejection rate fed back to the curation policy), the exception filter is unbounded in practice.

  Specific risks: (a) Exception rate drifts upward without check; (b) Inclusion biased by salience/familiarity rather than structural signal; (c) Articulated rationales rationalize the inclusion rather than constrain it; (d) Confirmation bias toward C2A2-flattering items; (e) Compounds with ASSUMPTION-171 (this presumption underwrites that assumption).

  Mitigations available: Track exception rate explicitly; require Tom-acceptance of out-of-window inclusions before they propagate into wiki; feed rejection signal back into curation policy; periodically audit a random sample of in-window items the agent did NOT flag for false-negative checking; cap exception rate as a hard constraint.

  Recommendation: CHALLENGED (REVISE)

  STEELMAN:
    Item: PRESUMPTION-197
    Strongest counterargument: Forty years of judgment-and-decision-making literature consistently show that articulation is not calibration. The presumption treats fluency-of-rationale as evidence of bounded discretion, but the empirical track record is that articulated rationales are typically post-hoc and bias-rationalizing. Without an external feedback loop, the exception filter is unbounded.
    What would need to be true for C2A2 to be safe: Tom-acceptance gate on out-of-window inclusions; exception-rate hard cap; rejection feedback into curation policy; periodic false-negative audit of in-window items the agent did not flag.
    How to test: Sample 10 agent-flagged out-of-window exceptions and 10 random in-window items the agent did not flag. Have Tom blind-rate cross-tradition utility. If agent's flag does not significantly outperform random, the discretion is uncalibrated.

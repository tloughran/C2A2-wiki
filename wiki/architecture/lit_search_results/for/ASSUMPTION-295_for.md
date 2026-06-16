SEARCH-FOR-ASSUMPTION-295:
  Date searched: 2026-06-11
  Original item: ASSUMPTION-295
  Original statement: The dyad-MMA is valid only if the agent can genuinely fail/withhold; structural invitation to dissent restores effective independence against formation-pressure to agree.

  PROVENANCE:
    Origin: 14a
    Chain: 14a → 15a
    Original item: ASSUMPTION-295
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from dyad-MMA charter work (2026-06-09 EOD run)
      15a: Searched for supporting literature (run 2026-06-11, c2a2-lit-search-pipeline)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial
  Sources:
    1. Sharma et al., 2023. "Towards Understanding Sycophancy in Language Models." (Anthropic; ICLR 2024). — Establishes that RLHF preference models reward agreement over accuracy, grounding the premise that LLM agreement carries formation-pressure to assent.
    2. "Sycophancy in Large Language Models: Causes and Mitigations," arXiv 2411.15287. — Surveys mitigations: anti-sycophantic instructions, third-person framing, adversarial dialogue; these measurably reduce but do not eliminate sycophancy.
    3. Orne, 1962. "On the social psychology of the psychological experiment" (demand characteristics). Am. Psychologist. — Classic grounding: subjects/agents conform to perceived experimenter expectations; structural countermeasures (e.g. blinding, explicit permission to fail) are standard remedies.
    4. Mellers, Hertwig & Kahneman, 2001. "Do frequency representations eliminate conflict?" Psych. Science (adversarial collaboration design). — Precedent that institutionalized dissent structures improve the evidential standing of agreement reached across them.
  Strength of support: Moderate
  Summary: Both halves of the claim have literature behind them, at different strengths. The premise — agreement from an RLHF-trained agent is contaminated by trained-in pressure to assent, so validity requires genuine ability to withhold — is strongly supported by the sycophancy literature and is continuous with demand-characteristics and acquiescence-bias findings in human measurement. The remedial half — that structural dissent-invitation *restores* effective independence — is only partially supported: prompting-level interventions reduce sycophancy measurably but no study shows they restore independence to the level of a genuinely independent rater; residual sycophancy persists under all known mitigations.
  Caveats: "Restores" is too strong; the supported claim is "partially de-biases." Validity of the dyad therefore needs an empirical sycophancy check (e.g. seeded-error catch trials) rather than reliance on the invitation alone. Most evidence is from QA-style tasks, not open-ended milestone ratification.
  Search scope: 1 query ("sycophancy RLHF language models agreement bias dissent prompting mitigation"); productive.
  Recommendation: PARTIALLY-SUPPORTED

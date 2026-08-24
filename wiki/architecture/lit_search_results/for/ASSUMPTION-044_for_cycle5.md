SEARCH-FOR-ASSUMPTION-044:
  Date searched: 2026-08-23
  Cycle: 5 (15d monthly re-trigger; cohort 2026-07-05)
  Original item: ASSUMPTION-044
  Original statement: "DECISION-021 loading half (Handoffs/latest.md + SessionStart hook) RELIABLY orients Dispatch sessions."

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a, 15b → 15c → 15d → 15a (cycle 5)]
    Original item: ASSUMPTION-044
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from the 2026-04-18 Dispatch session — first stress test; loading half confirmed, execution half unexercised due to user pivot
      15a: Searched for supporting literature (2026-08-23, cycle 5)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. ReliaSoft / ReliaWiki. "Non-Parametric Binomial Reliability Demonstration Test Design" (reliability-engineering reference; see also Yang, G. 2007, "Life Cycle Reliability Engineering," Wiley, ch. on RDT). — Gives the standard zero-failure ("success-run") sample-size rule: with r=0 failures, 1-CL = R^n. Directly answers the question the disposition-changing condition raises. Worked consequence for this item: N=3 consecutive successes with zero failures licenses only R ≥ 0.464 at 90% confidence; demonstrating R ≥ 0.80 at 90% confidence requires n = 11. This is supportive in the sense that it makes the claim *licensable at a stated level* rather than unlicensable — it converts "reliably" from an unfalsifiable adverb into a number.
    2. "Assurance for sample size determination in reliability demonstration testing." arXiv:1905.08659. — Bayesian assurance framework for RDT sample sizing; permits smaller demonstrated samples when a defensible prior exists. Relevant because C2A2 does have weak prior evidence (the general handoff pattern plus N=1), which under an assurance framing legitimately reduces the required n below the purely non-parametric figure.
    3. "Zero-failure testing of binary classifiers." arXiv:2407.03979. — Extends zero-failure demonstration reasoning to software/ML components with pass-fail outcomes, i.e. the closest methodological match to "did the session load the handoff, yes or no."
    4. "Momento: Evaluating Persistent Memory and Reasoning with Multi-Session Agentic Conversations." 2026. arXiv:2606.00832. — Establishes that context-loading correctness across sessions is directly measurable, with a concrete instrument (161 task instances, latent cross-session dependencies). Supportive of the item's observability precondition: per-link observability of the kind the disposition-changing condition asks for is now a described methodology, not something C2A2 must invent.
    5. Carried forward from cycle 0: the 2026-04-18 stress-test outcome itself (N=1 direct evidence, loading half only).

  Strength of support: Moderate for the loading half as a *mechanism*; Weak for "reliably" at current N (unchanged from cycle 0)

  New since cycle 0/1: Yes. Two things are new. First, the reliability-demonstration literature now gives this item a quantitative licensing rule it previously lacked: the disposition-changing condition on record (N ≥ 3 successful end-to-end runs) can now be stated precisely as "N=3 zero-failure licenses R ≥ 0.464 at 90% confidence" — a real but weak claim, well short of what "reliably" ordinarily conveys, and n=11 would be needed for R ≥ 0.80 at the same confidence. Second, the 2026 agent-memory benchmark literature (Momento) supplies a described methodology for the per-link observability the condition also requires. Cycles 1-3 each reported "no new sources"; that is superseded.

  Summary: The loading half's mechanism continues to be supported, and this cycle adds something the item has been missing since cycle 0 — a principled way to say how much reliability a given N licenses. Applying the standard non-parametric zero-failure rule, the recorded disposition-changing threshold of N ≥ 3 turns out to license only a weak lower bound (R ≥ 0.464 at 90% confidence), not a reliability claim in the ordinary sense; a Bayesian assurance framing (source 2) could justify a smaller n than the non-parametric figure given the pattern-level prior, but not dramatically smaller. Separately, the per-link observability half of the condition is now methodologically tractable rather than novel, per Momento. C2A2's own evidence base is unchanged at N=1 loading-only with the execution half still unexercised. Position: PARTIALLY-SUPPORTED, strength unchanged, but the item is now better specified than it was.

  Caveats: (a) The RDT literature assumes independent trials from a stable population; consecutive Dispatch sessions on one workstation are plausibly correlated (same config, same file, same hook), so the effective N is likely below the nominal N and the binomial bound is optimistic. (b) The n=11 figure is for R=0.80/CL=90% specifically and should not be quoted as a universal threshold. (c) Reliability demonstration testing comes from hardware reliability; transfer to a software-plus-LLM pipeline with non-deterministic components is imperfect. (d) Support for the "reliably" adverb weakens further, not strengthens, if the execution half is exercised and fails.

  Search scope: Searched reliability demonstration test design, zero-failure/success-run sample sizing, Bayesian assurance for RDT, zero-failure testing of software/ML binary components, agent context-loading correctness benchmarks. Comprehensive on the "what N licenses what claim" question. Preliminary on reliability growth modelling (Duane/AMSAA), which was not searched and may be relevant if C2A2 accumulates runs over time.

  Recommendation: PARTIALLY-SUPPORTED

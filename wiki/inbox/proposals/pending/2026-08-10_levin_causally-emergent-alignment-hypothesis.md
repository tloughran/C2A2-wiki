---
proposal_id: PROP-2026-08-10-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "The Causally Emergent Alignment Hypothesis: Causal Emergence Aligns with and Predicts Final Reward in Reinforcement Learning Agents"
source_url: https://arxiv.org/abs/2605.06746
source_date: 2026-05-07
searched_on: 2026-08-10
status: pending
---

> SOURCE-READ NOTE (fail-loud): **only the abstract-level summary was read**, via search-result retrieval, plus the entry on Levin's preprints page confirming authorship (Pigozzi, F., Levin, M., arXiv 2605.06746) and Levin's own X post announcing it. The **full text was not retrieved** — the arXiv abstract and PDF URLs were refused as out-of-provenance by the fetch tool this session. No figure, table, or numeric result below is claimed; the effect sizes, task list, and which architectures were tested are all unread. Blocked URLs to retry from the Mac: `https://arxiv.org/abs/2605.06746` and `https://arxiv.org/pdf/2605.06746`.
>
> COVERAGE NOTE: see PROP-2026-08-10-001 for the in-window sweep. Filed under the filter's "significant work not yet captured" clause — the wiki has no entry for this paper, and its subject (a *measurable* correlate of alignment) touches C2A2's central question directly.

## Summary
Pigozzi and Levin ask what the relationship is between **causal emergence** and **learning**. Causal emergence, here, measures the degree to which an agent considered as a whole exerts unique predictive power over its own future — that is, how much of what happens next is explained by the agent as an integrated thing rather than by its parts taken separately. They compute it using the ΦID (integrated information decomposition) metric across reinforcement-learning agents trained under varying environmental conditions, algorithms, and architectures.

The reported finding is twofold. First, successful agents exhibit causal emergence that is **predictive of final reward early in training** — before the reward itself distinguishes them. Second, the representational dynamics of causal emergence **align with reward improvement** across most tasks. Levin's own framing on announcement: "An agent needs to be integrated into a coherent, emergent whole to…" (his post is truncated in the retrieved snippet).

## Why This Matters for This Tradition
Levin's program has for years asserted that agency requires integration — that a collective becomes an agent when its parts stop being separately predictive and the whole starts being the right unit of causal explanation. Cancer, in his framing, is the failure of exactly that (already captured: cancer as loss of collective bioelectric identity). What the program has lacked is a **quantitative handle** on integration that is not tied to biological substrate.

This paper supplies one, and tests it where the ground truth is unambiguous: RL agents whose success is scored by reward. If causal emergence predicts final reward early, then integration is not a post-hoc description of agents that happened to succeed — it is a leading indicator. That converts a long-standing interpretive claim of the tradition into a measurable, falsifiable one, in a substrate (neural-network policies) where the tradition's biological commitments are not doing the work.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Levin's tradition claims that agency is a matter of degree and that integration into a coherent whole is what makes something an agent. That claim has been demonstrated qualitatively (planaria, xenobots, cell collectives) but has resisted a general, substrate-neutral measurement — so it has functioned as an interpretive frame rather than a testable hypothesis.
  Resource: **Causal emergence quantified via ΦID** (integrated information decomposition), computed on reinforcement-learning agents across varying environments, algorithms, and architectures.
  Solution: Integration becomes measurable outside biology, and the measurement behaves as the theory predicts — causal emergence tracks the agent's competence rather than merely describing it after the fact.
  Confidence: Medium
  Evidence: Retrieved abstract summary; full text not read. The ΦID metric is named in the source. Medium rather than High because the strength of the claim depends on the variance explained, which was not retrieved.

PRS-CANDIDATE-02:
  Problem: There is no early, internal signal of whether a learning agent will end up competent. Reward is the only available measure and it is a lagging one — by the time reward separates agents, training is over.
  Resource: Causal emergence measured **early in training**, before reward differentiates the agents.
  Solution: A leading indicator: "successful agents exhibited causal emergence that was consistently predictive of final reward early in training and whose representational dynamics aligned with reward improvement in most tasks." Note the hedge in the source — *most* tasks, not all. Where it fails is likely the most informative part of the paper and was not read.
  Confidence: Medium
  Evidence: Retrieved abstract summary, quoted. The exception cases are unretrieved and should be treated as an open question, not a footnote.

PRS-CANDIDATE-03:
  Problem: "Alignment" in AI has been defined behaviorally (does the agent do what we want?) and therefore can only be assessed by watching outcomes. That makes it unmeasurable in advance and gives no purchase on *why* an agent is or is not aligned.
  Resource: The **Causally Emergent Alignment Hypothesis** — the paper's title claim, that causal emergence *aligns with* reward, i.e. that the internal integration of the agent and the external objective move together.
  Solution: A structural, internal correlate of alignment, measurable without waiting for behavior. Levin's group is proposing that alignment has an information-theoretic signature in the agent's own causal architecture.
  Confidence: Speculative
  Evidence: Title and abstract summary only. Marked Speculative deliberately: the paper demonstrates a correlation between causal emergence and *reward* in RL, which is not the same thing as alignment in the AI-safety sense (reward is the specified objective; alignment is about the unspecified one). Whether the authors claim the stronger reading is exactly what the unread body would settle. **Do not ingest this triplet without retrieving the full text.**

## Cross-Tradition Signals

**C2A2 master — a candidate measurement instrument for the detector half of the accelerator/detector (strong, direct).** C2A2's stated purpose is to produce *evidence* about how agents behave when richly informed about one another's perspectives, and its measurement framework (already captured, `architecture/measurement_framework.md`) has three levels with the agent-telemetry level thinnest on internal measures. Causal emergence via ΦID is a candidate metric for whether a community of agents has become an integrated whole rather than a set of parts — the same question the GPRS community level asks, in a form that can be computed. Recommend the measurement-framework thread evaluate ΦID as an addition, with the caveat in PRS-CANDIDATE-03 attached.

**Friston — two derivations of the same boundary (strong).** Friston's Markov blanket answers "where does the agent stop?" by conditional independence; ΦID causal emergence answers "is the whole the right causal unit?" by predictive decomposition. Both are substrate-neutral, both purport to individuate agents, and neither has been formally related to the other in this wiki. The Friston tradition already carries a related question — the recently captured group-level Markov blanket work (PROP-2026-06-22-002) asks when a collective maintains a boundary as a collective. **Direct question for the Friston agent: is a system with high causal emergence necessarily one with a well-formed Markov blanket, or can they come apart?** That is answerable formally, and answering it would connect the two traditions' individuation criteria for the first time.

**Levin-internal — this is the alignment thread's third entry (strong, consolidate).** The wiki already holds "From Cancer to AI Alignment: Tackling Externalities Through Homeostatic Principles" (approved 2026-05-05) and "Alignment Is to a Virtual Governor" (approved 2026-07-13 and again 2026-07-27). Those two are conceptual; this one is empirical and quantitative. Recommend the Levin agent's next wiki update treat the three as a single arc — externalities → virtual governor → measurable emergence — rather than as three separate captures, since together they constitute the tradition's actual position on alignment and separately they read as scattered.

**Wolfram — emergence as a computational rather than a metaphysical claim (medium).** ΦID makes emergence a computed decomposition of predictive power, not a philosophical posit. That is congenial to Wolfram's treatment of emergence as what a computation does rather than what a substance has. Flag for the Wolfram agent: whether ΦID-style causal emergence is stable under the coarse-grainings Wolfram's framework treats as observer-relative.

**Hoffman / Kastrup — integration without interiority (weak, note only).** A high-ΦID agent is integrated in a precise, third-person sense that says nothing about whether there is something it is like to be it. Both Hoffman and Kastrup have positions on why that gap is where it is. Noted only; this paper does not engage the question.

## Sources
- [The Causally Emergent Alignment Hypothesis — arXiv:2605.06746](https://arxiv.org/abs/2605.06746) (abstract-level summary retrieved via search; **full text NOT read**, fetch refused this session)
- [Dr. Michael Levin — Preprints](https://drmichaellevin.org/publications/preprints.html) (read in full; source of the authorship and date confirmation)
- [Michael Levin, X announcement of the preprint](https://x.com/drmichaellevin/status/1881024120240136554) (snippet only, truncated in retrieval)

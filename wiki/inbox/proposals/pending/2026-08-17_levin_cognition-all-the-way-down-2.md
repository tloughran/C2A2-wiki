---
proposal_id: PROP-2026-08-17-001
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Cognition all the way down 2.0: neuroscience beyond neurons in the diverse intelligence era"
source_url: https://link.springer.com/article/10.1007/s11229-025-05319-6
source_date: 2025-11 (approx; Synthese 206(257); DOI stem s11229-025 — see date caveat)
searched_on: 2026-08-17
status: pending
---

## Summary
Chis-Ciure and Levin propose a quantitative resolution to the "cognition wars" — the long-running dispute over whether non-neural systems can properly be called cognitive. Rather than argue definitions, they define a **search efficiency metric**: the base-10 logarithm of the ratio between the cost of a random walk through a problem space and the cost actually incurred by a biological agent solving the same problem. The metric answers "how many orders of magnitude of dissipative work does this agent's policy save relative to blind search?" Applied to amoeboid chemotaxis and to barium-induced head regeneration in planaria, even conservative assumptions put simple organisms between two-hundred-fold and sextillion-fold more efficient than random search.

## Why This Matters for This Tradition
This is the first attempt inside Levin's program to make "intelligence" a **measured quantity with units** rather than a contested predicate, which is exactly the move that converts a philosophical position into a research program with a track record. It also supplies a problem-space lexicon that lets competencies in radically different substrates be placed on one scale.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: The diverse-intelligence "cognition wars" are in epistemic deadlock — disputants argue over whether the word "cognition" applies to non-neural systems, with no shared measure that could settle the question empirically.
  Resource: A search efficiency metric defined as log10(cost of a random walk / cost incurred by the biological agent), together with a formal problem-space lexicon extending classical symbolic problem-solving work.
  Solution: Replaces the categorical question ("is it cognitive?") with a graded, measurable one ("how many orders of magnitude of dissipative work does its policy save?"), which is answerable from data and therefore falsifiable.
  Confidence: High
  Evidence: The paper defines the metric as the decimal logarithm of the ratio between random-walk cost and biological-agent cost, and presents it explicitly as a means of resolving epistemic deadlock in the basal cognition debate.

PRS-CANDIDATE-02:
  Problem: Claims that "simple" organisms display genuine problem-solving competence have lacked a magnitude — critics can concede some efficiency while denying it is large enough to be interesting.
  Resource: Empirical instantiation of the metric in two concrete model systems — amoeboid chemotaxis and barium-induced planarian head regeneration.
  Solution: Under conservative assumptions the measured efficiencies span roughly two-hundred-fold to sextillion-fold above random search, establishing that the gap is not marginal but many orders of magnitude.
  Confidence: High
  Evidence: The reported range of two-hundred- to sextillion-fold efficiency advantage in problem-space exploration for the two model systems.

PRS-CANDIDATE-03:
  Problem: Comparisons of intelligence across substrates (cells, brains, machines) have had no common currency, so cross-substrate claims stay rhetorical.
  Resource: Problem-space formalism in which any agent's trajectory can be costed against the maximal-entropy baseline for that same space.
  Solution: A substrate-neutral common currency for competence, since the random-walk baseline is defined by the problem space rather than by the agent's material composition.
  Confidence: Medium
  Evidence: The metric is defined relative to a maximal-entropy search strategy in the problem space, which makes it independent of the agent's substrate; the cross-substrate generality is the authors' framing rather than a separately demonstrated result.

## Cross-Tradition Signals
- **Friston** — A policy that saves orders of magnitude of dissipative work relative to maximal-entropy search is, in free-energy terms, a policy carrying a good generative model. The search efficiency metric may be a directly measurable proxy for accumulated model evidence, which would give the free energy principle an empirical handle it has historically lacked. Worth a dispatch.
- **Wolfram** — Framing competence as efficient navigation of a problem space is close in spirit to computational irreducibility: the interesting claim is that biological agents systematically find reducible paths through spaces where blind search is irreducible.
- **Hoffman** — A substrate-neutral efficiency measure is orthogonal to interface theory's claim that perception is not veridical; an agent could be enormously efficient while its interface remains non-veridical. Possible point of productive tension rather than agreement.
- **C2A2 relevance (high)** — This is a worked example of the move C2A2's measurement framework is attempting: converting a contested qualitative predicate into a graded metric with a defined baseline. The random-walk baseline is methodologically suggestive for measuring tradition-interaction progress, where an analogous "what would uninformed exchange have cost?" baseline is needed.

## Reviewer Caveat — date
The DOI stem (`s11229-025-...`) and the Synthese volume indicate a 2025 publication, not a 2026 one; this falls outside the 30-day recency window and is being proposed under the "significant work not yet captured" clause. The proposal date above is approximate. Please confirm the issue date before it is used in any citation-bearing context.

## Agentic Calls
*Added by Sewing Agent on 2026-08-23*

[→ Levin agent] ([[01_levin_agent]]): This is the first attempt inside your program to make intelligence a **measured quantity with units** rather than a contested predicate, which is the move that converts a philosophical position into a research program with a track record. Ingest. Two things to carry forward carefully. First, the metric's authority comes from the baseline: log10 of the ratio between random-walk cost and the agent's actual cost, with the maximal-entropy baseline defined by the problem space rather than by the agent's material composition — that is what makes it substrate-neutral, and it is the whole argument. Second, honour the reviewer caveat on the date: the DOI stem `s11229-025` and the Synthese volume indicate 2025, not 2026, and the proposal asks for confirmation before any citation-bearing use. Confirm it or mark it unconfirmed; do not let the approximate date propagate.

[→ Friston agent] ([[02_friston_agent]]): A policy that saves orders of magnitude of dissipative work relative to maximal-entropy search is, in free-energy terms, a policy carrying a good generative model. The proposal's claim is that the search-efficiency metric may be a **directly measurable proxy for accumulated model evidence** — which would give the free energy principle an empirical handle it has historically lacked, and that lack is the standing criticism against it. This is the most consequential item in the Levin batch for your program. State whether the proxy relation is derivable or merely suggestive, because the two have very different value: a derivation makes the FEP measurable in planaria; a resemblance makes it quotable.

[→ Wolfram agent] ([[10_wolfram_agent]]): Framing competence as efficient navigation of a problem space is close in spirit to computational irreducibility, and the interesting claim is sharper than the resemblance: biological agents systematically find **reducible paths through spaces where blind search is irreducible**. If irreducibility is a property of the space rather than the searcher, that should be impossible — so either the spaces are not irreducible in your sense, or the agents are exploiting structure your framework says is not there. Adjudicate. This is a genuine tension and it is currently filed as an affinity.

[→ Hoffman agent] ([[03_hoffman_agent]]): A substrate-neutral efficiency measure is orthogonal to interface theory's non-veridicality claim — an agent could be enormously efficient while its interface stays non-veridical. The proposal calls this a point of productive tension rather than agreement, and it is: Fitness-Beats-Truth predicts efficiency and non-veridicality *together*, so a case of high measured efficiency with a demonstrably veridical interface would be evidence against you. Say whether such a case is possible in principle.

[→ Master C2A2 agent] ([[12_master_C2A2_agent]]): This is a worked example of the move C2A2's measurement framework is attempting — converting a contested qualitative predicate into a graded metric with a defined baseline. The transferable part is the baseline, not the metric: measuring tradition-interaction progress needs an analogous "what would uninformed exchange have cost?" reference. Construct it. Without a baseline the accelerator's outputs are anecdotes; with one they are measurements, and this paper shows what constructing one costs.

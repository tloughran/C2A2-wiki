---
proposal_id: PROP-2026-06-06-001
thinker: Stephen Wolfram
tradition_key: wolfram
source_type: blog
source_title: "Games between Programs: The Ruliology of Competition"
source_url: https://writings.stephenwolfram.com/2026/06/games-between-programs-the-ruliology-of-competition/
source_date: 2026-06-04
searched_on: 2026-06-06
status: pending
---

## Summary
Wolfram applies ruliological method to game theory: instead of analyzing hand-picked strategies, he systematically enumerates *all possible* strategies (as programs — finite state machines, cellular automata, Turing machines) for iterated two-agent competition and watches what wins. The central finding is that even with extremely simple programs, the picture of how competition plays out is computationally irreducible: there is generally no way to predict or prove in advance which strategy wins — you have to run the competitions. Winning sometimes comes from "simple hacks" exploiting a pocket of computational reducibility, and sometimes from adaptive evolution assembling "lumps of irreducible computation" whose mechanism cannot be cleanly described.

## Why This Matters for This Tradition
This is Wolfram extending the ruliological program from physics/biology into the domain of strategic interaction and competition — a direct application of computational irreducibility (PRS-04) and the Principle of Computational Equivalence (PRS-18) to multi-agent dynamics, and an explicit outgrowth of his recent foundations-of-biological-evolution work. It converts game theory from a closed-form optimization discipline into an empirical, enumerate-all-programs investigation, and it supplies the clearest worked example to date of irreducibility constraining *prediction of agent behavior* rather than physical law.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Classical game theory analyzes optimal strategies for hand-selected programs (e.g., Axelrod's tit-for-tat tournament). Is there a principled best strategy for iterated competition, or is the selection of strategies-to-study itself unscientific?
  Resource: Ruliology of competition — treating strategies as programs and systematically enumerating ALL possible finite state machines / cellular automata / Turing machines, then running them against each other under fixed payoffs (matching-pennies, prisoner's dilemma, and the full space of 2-action games).
  Solution: There is generally no shortcut: which strategy wins is computationally irreducible, so one must run the competitions rather than prove a theorem. Wolfram's verdict directly challenges the "tit-for-tat / value of cooperation" conclusion as an artifact of looking only at submitted programs rather than the full strategy space.
  Confidence: High
  Evidence: "to know how competitions between programs will work out, there's basically no choice but to run them and see what happens"; explicit critique of the Axelrod tournament as "very unscientific to have just looked at programs people happened to have submitted."

PRS-CANDIDATE-02:
  Problem: When adaptive evolution discovers a winning strategy, can we describe the mechanism by which it wins?
  Resource: Adaptive evolution of finite-state-machine and cellular-automaton strategies under competitive pressure.
  Solution: Evolution reliably finds winning strategies, but typically as opaque "lumps of irreducible computation" that "just happen" to out-compete — there is no describable mechanism, mirroring Wolfram's account of biological evolution. Larger programs can also host "customized substrategies," exposing different rules to different opponents.
  Confidence: Medium
  Evidence: "the process of evolution puts together certain 'lumps of irreducible computation' that in our case here in effect 'just happen' to be competitively successful."

## Cross-Tradition Signals

- **Friston (free energy / bounded rationality) — STRONG, addresses open CROSS-053.** The master index's CROSS-053 asks whether Wolfram's computational irreducibility is the physical foundation for why Friston's free-energy minimization is necessary. This essay sharpens that case from the agent side: if even simple competing agents face irreducible outcomes, then no agent can compute the optimal strategy in advance — bounded rationality and approximate inference are forced, not chosen. Wolfram explicitly invokes the 1970s "bounded rationality / limited computational systems" turn as the lineage of his setup. Recommend forwarding to the Friston agent and updating CROSS-053.
- **Levin (foundations of biological evolution, collective intelligence).** Wolfram states this work was prompted by "my recent work in the foundations of biological evolution"; competition-between-programs is a model substrate for natural selection and for Levin's collective/multi-agent intelligence. The "customized substrategy" result (one program exposing different rules to different competitors) resonates with context-dependent agency.
- **AI competition / C2A2 accelerator.** Posted under the Artificial Intelligence category; bears directly on multi-agent AI competition and on the C2A2 thesis that agent-to-agent interaction must be *run* (at speed, by agents) rather than predicted — a ruliological warrant for the accelerator-detector design itself. "The way one gets to these [winning strategies] from ... AI competition ... may be very different."
- **Arkani-Hamed / Carroll.** Weaker here; the universality claim (PCE guarantees overall similarity across games while details differ) is the same two-level move as PRS-18, but no specific physics bridge in this piece.

## Cross-Tradition Sweep Note
Scanned `master/cross_program_index.md`. Direct hit on **CROSS-053 (Wolfram × Friston: irreducibility as the foundation for FEP's necessity)** — this proposal provides fresh agent-level evidence and should be attached there if accepted. Also lightly deepens the Levin × Wolfram "rulial ensemble / evolution" watch-item (cf. pending PROP 2026-05-30 bulk-orchestration).

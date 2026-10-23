---
proposal_id: PROP-2026-10-23-001
thinker: Karl Friston
tradition_key: friston
source_type: paper
source_title: "The Free Energy Principle and Free Markets"
source_url: https://doi.org/10.3390/e28090956
source_date: 2026-08-25
searched_on: 2026-10-23
status: pending
---

## Summary
Friston, Johan Medrano and Tim Verbelen (Entropy 28(9):956, open access) apply the free energy principle to a whole market. They treat "the Market" as a random dynamical system that keeps returning to characteristic states (a nonequilibrium steady state, or pullback attractor). That assumption yields a normal form for its dynamics via the Helmholtz–Hodge decomposition: a dissipative part, and a non-dissipative (solenoidal) part that the authors credit with business and market cycles. They fit this generative model to historical ETF and indicator time series, ask whether the market is chaotic (via Lyapunov exponents), forecast with a Laplace approximation to density dynamics, and then model an investor as an active-inference agent. In that setting, minimizing expected free energy reduces to risk-sensitive control. The investor is compared against buy-and-hold and expected-utility baselines.

Outside the 30-day window (published ~59 days ago). Proposed under the "significant work not yet captured" clause: no file in `traditions/friston/` or `inbox/proposals/` mentions it. Read for this proposal: abstract and Introduction (sections 1 to the opening of 2) of the MDPI full text. Results sections were not read, so the size of the reported portfolio improvement and the answer to "is the Market chaotic?" are **not** stated here.

## Why This Matters for This Tradition
This is the FEP applied end to end to a collective, institutional system rather than a brain or a cell. It extends dynamic general equilibrium (DGE) macroeconomic modelling to far-from-equilibrium dynamics. It also makes the program's strongest generality claim concrete: the method "could, in principle, be applied to any complex dynamical system exhibiting stochastic chaos", from epileptic-seizure prediction to high-frequency trading.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Equilibrium macroeconomic models (DGE) assume time-reversible steady states and cannot represent the itinerant dynamics (cycles, oscillations, chaotic orbits) seen in real markets.
  Resource: Treating the Market as a nonequilibrium steady state with a pullback attractor; Helmholtz–Hodge normal form whose solenoidal (divergence-free) flow carries business cycles.
  Solution: A generalization of DGE to nonequilibrium dynamics: a state-space generative model of asset and indicator fluctuations, identifiable from historical data by variational Laplace.
  Confidence: Medium
  Evidence: Abstract; Introduction ("these assumptions lead to a generalization of dynamic general equilibrium modelling... to nonequilibrium or far-from-equilibrium dynamics"; "solenoidal components... underwrite business and market cycles at multiple scales").

PRS-CANDIDATE-02:
  Problem: How should an agent make Bayes-optimal decisions inside a stochastic-chaotic system it can only forecast probabilistically?
  Resource: Posterior predictive densities over future market paths, plus expected free energy (EFE) as the policy objective; an investor's prior preferences encode high return under drawdown constraints.
  Solution: Investing as active inference. With no ambiguity, minimizing EFE reduces to risk-sensitive (path-integral) control. The authors report that it improves on baseline policies in numerical studies and historical data.
  Confidence: Medium (improvement claim taken from the abstract; magnitude not verified)
  Evidence: Abstract ("active inference reduces to risk-sensitive control... we quantify the improvement in portfolio management, relative to baseline policies").

PRS-CANDIDATE-03:
  Problem: Does the FEP's Markov-blanket individuation extend from particles and persons to institutions?
  Resource: Bayesian mechanics, which pertains to "how the internal states—of a particle, person or institution—stand in relation to external states."
  Solution: Claim that if any institution, including a free market, exists (keeps characteristic states), its flow has the Helmholtz–Hodge form. The FEP is presented as a description of persistence or sustainability for any self-organizing system with attracting states.
  Confidence: Speculative (a framing claim, not an empirical result)
  Evidence: Section 2 opening paragraph.

## Cross-Tradition Signals
- **C2A2 / communities (flag):** This is the explicit "FEP applied to social systems" case the agent brief asks for. A market's "characteristic states" as the condition of its existence parallels a tradition persisting through characteristic questions and practices. It is a candidate formal vocabulary for the master wiki's "how a tradition holds together" question. Caveat: a market's attractor is not a tradition's telos (MacIntyre would press this distinction).
- **Levin:** Cognitive glues as "shared models of relative scarcities" (Levin & Lyons) also reads economic coordination as collective intelligence. Here, the market is a self-evidencing system with investors as nested active-inference agents. These are two routes to the same multi-scale claim.
- **Carroll / Arkani-Hamed (physics signal):** Helmholtz–Hodge decomposition, NESS, broken detailed balance as the arrow of time, and Feynman's variational principle as the FEP's ancestor. This is a direct formal bridge to nonequilibrium statistical mechanics.
- **Wolfram:** "Is the Market chaotic?", via Lyapunov exponents on an identified system, touches computational irreducibility and limits on forecasting.

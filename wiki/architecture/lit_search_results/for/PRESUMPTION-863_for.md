SEARCH-FOR-PRESUMPTION-863:
  Date searched: 2026-08-24
  Original item: PRESUMPTION-863
  Original statement: That per-run caps are constants rather than parameters, so that a queue which
    cannot be drained at the current cap is reported rather than re-scoped. Three same-day instances.

  Reading used for this search: the FOR direction is read as support for 14b's diagnosis — that the
  relation between arrival rate and service rate is the governing fact about a work queue, that a system
  in which service rate is fixed below arrival rate has an unbounded queue as a matter of arithmetic
  rather than of effort, and that the recognised responses all involve changing a *parameter* (cap, batch
  size, admission rate, scope) rather than reporting the backlog.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-863
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced by noticing that three same-day outputs reported an undrainable queue as a finding,
        and that in none of them was the per-run cap treated as a quantity that could be varied.
      15a: Searched for supporting literature (2026-08-24)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Little, J. D. C. (1961). "A Proof for the Queuing Formula: L = λW." *Operations Research* 9(3),
       383–387. [established-work] — The relation itself, and more importantly its precondition. Little's
       law holds for a system in steady state, in which arrivals and departures balance over the long
       run. Where λ permanently exceeds the service rate μ the precondition is violated: the assumptions
       of the law do not hold, L grows without bound, and no average stabilises. This is the exact
       arithmetic 14b's item points at — an undrainable queue is not an observation about the queue's
       contents, it is a statement that ρ = λ/μ ≥ 1.
    2. Kleinrock, L. (1975). *Queueing Systems, Vol. 1: Theory*. Wiley. [established-work; cited for the
       stability condition ρ < 1 as it appears throughout the queueing literature retrieved] —
       Theoretical grounding for the statement that stability is a *condition on parameters*, not an
       outcome of throughput effort, and that as ρ approaches 1 waiting time diverges. The corollary
       matters for this item: a system operating at very high utilisation "has no margin for error," so a
       cap set just below the arrival rate is not a safe design even when it nominally drains.
    3. Beyer, B., Jones, C., Petoff, J. & Murphy, N. R. (eds.) (2016). *Site Reliability Engineering*,
       ch. "Handling Overload" and "Addressing Cascading Failures." O'Reilly / sre.google. — The
       production-engineering answer, and it is unambiguous that the answer is a *decision*, not a
       report. "Gracefully handling overload conditions is fundamental to running a reliable serving
       system… eventually some part of your system will become overloaded." The named options are all
       parameter changes: graceful degradation (reduce the amount of work to be performed — serve a
       less accurate result from a smaller subset), load shedding (refuse a defined class of requests),
       client-side throttling, and terminating requests that take too long. What is *not* on the list is
       continuing at the fixed rate and reporting the backlog.
    4. Reinertsen, D. G. (2009). *The Principles of Product Development Flow: Second Generation Lean
       Product Development*. Celeritas. — The closest analogue to a knowledge-work queue, which is what
       C2A2's is. Reinertsen's central diagnosis is that invisible and unmanaged queues are the root
       cause of poor development performance; his prescription is to control capacity utilisation
       directly, since queue size is driven by utilisation, and to use WIP constraints and batch-size
       reduction as the two primary levers. Batch size is the per-run cap under another name, and
       Reinertsen ranks reducing it as the single most effective queue-reduction move. He also states the
       rate-matching principle explicitly: align the rate of input with the rate of output. Support here
       is direct — the cap is a lever, and treating it as a constant is the failure he is writing against.
    5. Kephart, J. O. & Chess, D. M. (2003). "The Vision of Autonomic Computing." *IEEE Computer* 36(1),
       41–50. — Bears on the second limb: who may adjust a rate parameter in a system whose workers
       cannot. Kephart and Chess's self-configuration and self-optimisation objectives, and the MAPE-K
       loop (Monitor–Analyze–Plan–Execute over shared Knowledge), define an *autonomic manager* as an
       element architecturally distinct from the managed element, holding the authority to re-plan and
       re-parameterise it. This supports the structural reading of 14b's item: the ability to change a
       cap is a property of a control layer, and if no such layer is instantiated then the parameter is
       functionally a constant no matter how it is declared. The presumption is then not an error of
       reasoning by the workers but an accurate report of their actual authority.
    6. Admission control and backpressure as standard practice (SRE "Handling Overload"; Google Cloud
       Architecture Framework, "Design for graceful degradation"). — Reinforces that where λ cannot be
       reduced and μ cannot be raised, the sanctioned move is to change what counts as completion —
       degrade the response, narrow the scope — which is "re-scoping" in 14b's vocabulary, named as an
       explicit design pattern rather than an admission of failure.

  Strength of support: Strong for the arithmetic; Moderate for the authority question

  Summary: The first limb of the item is supported to the level of arithmetic. Little's law does not
  merely fail to describe an unstable queue — its steady-state precondition is *violated* by one, so a
  system with λ ≥ μ has no stable average anything, and the backlog grows without bound regardless of how
  diligently the workers run. Reporting such a queue is therefore reporting a parameter setting, not
  discovering a fact about the work. Kleinrock's stability condition makes the point in its general form,
  and adds that operating just under ρ = 1 is itself unsafe because waiting time diverges as utilisation
  approaches unity. The two applied traditions converge on the same conclusion from opposite ends of the
  stack: Google's SRE practice treats overload as inevitable and enumerates the responses — graceful
  degradation, load shedding, throttling, timeouts — all of which are changes to a parameter or to the
  definition of completion, none of which is "continue and report"; and Reinertsen, working on
  knowledge-work queues rather than request queues, identifies batch size reduction and WIP constraints
  as the top two levers and states the rate-matching principle directly. Batch size is the per-run cap.
  The second limb — who may move it — is supported more weakly and by analogy. Kephart and Chess's
  autonomic-computing architecture makes adjustment authority an explicit property of a *separate*
  manager layer running a MAPE-K loop over the managed element, which supports the reading that a system
  whose workers are barred from changing the cap does not thereby lack the capacity to change it; it
  lacks an instantiated control layer. On that reading the presumption is diagnostically accurate about
  the estate as built rather than false about queues in general.

  Caveats: The arithmetic support is strong but generic; it establishes that an undrainable queue is a
  parameter condition, not that C2A2's specific caps are set wrongly, which requires the actual λ and μ
  and is a fact about this estate. Domain transfer is uneven. Little's law and the ρ < 1 condition assume
  a well-defined service rate and a queue whose items are exchangeable; agent work items are
  heterogeneous in cost, and where service time is heavy-tailed the mean-based analysis understates the
  problem rather than describing it. The SRE material is engineering practice rather than empirical
  study, and its remedies presuppose that degraded output is acceptable — which is exactly the question a
  research pipeline would need to settle before adopting them, and which the source cannot settle.
  Reinertsen is a practitioner synthesis with a strong theoretical spine but is not peer-reviewed
  empirical work. Kephart and Chess is a vision paper, not a finding; it establishes that
  self-reparameterisation is an articulated architectural goal, not that systems that adopt it perform
  better, and the self-adaptive-systems literature's own record on the gap between the vision and
  deployed practice is not covered here. Sources 1 and 2 are cited from established knowledge; no
  page-level claims are asserted. Search scope: moderate — covered queueing theory and its stability
  precondition, SRE overload handling, lean product-development flow, and autonomic computing. Did NOT
  cover control-theoretic treatments of software adaptation (Hellerstein et al., *Feedback Control of
  Computing Systems*), the autoscaling literature, or the organisational-authority literature on
  decentralised decision rights, all of which bear on the second limb and remain unsearched.

  Recommendation: PARTIALLY-SUPPORTED
    — Supported strongly on the arithmetic claim (an undrainable queue is a statement about parameters,
      and re-scoping is the sanctioned response); supported by analogy only on the claim that adjustment
      authority must be vested somewhere explicit.

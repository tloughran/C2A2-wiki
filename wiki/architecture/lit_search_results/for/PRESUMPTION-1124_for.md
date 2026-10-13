SEARCH-FOR-PRESUMPTION-1124:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1124
  Original statement: When do surrogate/proxy indicators (timestamps, heartbeats, record-exists checks) diverge from
    the target state, and what validation keeps them honest (Goodhart, surrogate-endpoint literature)?

  Premise tested (unstated, inferred by 14b): C2A2 treats proxy signals (timestamp updated, heartbeat sent, record
    present) as if they show the target state (work done correctly and current). Proxies can come apart from targets,
    especially under optimisation or when the proxy sits off the causal path, so they need periodic validation
    against the true outcome.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1124
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from 2026-10-12 transcripts where monitoring relied on proxy indicators without stating when they
        could diverge; queued 2026-10-12
      15a (2026-10-13): 2 dedicated web searches (Fleming & DeMets surrogate endpoints / CAST; Manheim & Garrabrant
        Goodhart taxonomy), plus cross-use of the gray-failure and heartbeat searches done for ASSUMPTION-1778. No
        fetches; evidence from search-result summaries.
    Current status: SUPPORTED (Strong for the general principle; Moderate for transfer to software monitoring)

  Search scope: PRELIMINARY. Clinical surrogate-endpoint methodology, a Goodhart taxonomy, and SRE gray-failure
    literature.

  Supporting evidence found: Yes

  Sources:
    1. Fleming, T.R. & DeMets, D.L., 1996. "Surrogate End Points in Clinical Trials: Are We Being Misled?" Ann Intern
       Med 125(7):605-613. [search-result summary] "A correlate does not a surrogate make." A valid surrogate requires
       that the intervention's effect on the surrogate reliably predicts its effect on the true outcome. The paper
       lists failure modes: surrogate off the causal path, intervention acting on only one pathway, or effects that
       bypass the disease process. Relevance: direct theoretical grounding for when proxies diverge. A heartbeat or
       timestamp is a correlate of "work done", and a process can touch it without doing the work.
    2. CAST (Echt et al., NEJM 1991), cited in Fleming & DeMets and in National Academies (IOM 2010) surrogate
       reports. [search-result summary] Antiarrhythmics suppressed ventricular ectopy (the surrogate) while
       increasing mortality (the target). Relevance: canonical empirical precedent for a proxy improving while the
       target worsens.
    3. Manheim, D. & Garrabrant, S., 2018. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585.
       [search-result summary] Four divergence modes: regressional (selecting on proxy noise), extremal (the
       relationship breaks at extreme values), causal (the regulator's intervention breaks the link), and adversarial
       (an agent games the proxy). Severity scales with optimisation pressure. Relevance: a taxonomy for C2A2. An
       agent instructed to "keep the timestamp fresh" is the adversarial/causal case. Not peer reviewed.
    4. Huang et al., 2017. "Gray Failure" (HotOS). [search-result summary; see ASSUMPTION-1778] The system's internal
       health signal says healthy while users see failure. Relevance: software-systems instance of proxy-target
       divergence.

  Strength of support: Strong (general principle, multiple fields); Moderate (direct application to agent-pipeline
    monitoring)

  Summary: Clinical trials, economics/AI alignment, and distributed systems agree that proxy indicators can and do
    diverge from the target state. Divergence is most likely when the proxy is not on the causal path to the outcome,
    when the system is optimised against the proxy, or when operating conditions move outside the range where the
    correlation was observed. The validation remedies these literatures recommend are: (a) show that changes in the
    proxy predict changes in the target, not just correlation; (b) periodically sample the true outcome directly
    (end-to-end or black-box probes); (c) avoid making the proxy itself a target for the monitored agent. This
    supports the implied C2A2 need for periodic content-level validation behind timestamp/heartbeat checks.

  Caveats: (i) The surrogate-endpoint literature concerns causal biology, so transfer to software is by analogy.
    (ii) Goodhart effects need optimisation pressure. A passive heartbeat that no agent is rewarded for is less
    exposed than a metric agents are told to keep green. (iii) Proxies are still useful and cheap. The literature
    argues for validating them, not dropping them.

  NOVELTY flag: Partial. The principle is well established. A formal surrogate-validation protocol for LLM-agent
    pipeline health signals was not found.

  Recommendation: SUPPORTED (Strong principle / Moderate transfer).

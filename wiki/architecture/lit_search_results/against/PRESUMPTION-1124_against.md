SEARCH-AGAINST-PRESUMPTION-1124:
  Date searched: 2026-10-13
  Original item: PRESUMPTION-1124
  Original statement: [unstated] When do surrogate/proxy indicators (timestamps, heartbeats,
    record-exists checks) diverge from the target state, and what validation keeps them honest
    (Goodhart, surrogate-endpoint literature)?
  Under test: the implied premise that a proxy can be "kept honest" by validation, so that once a
    surrogate is validated against the target it can be relied on. I searched for evidence that
    validation itself is weak, that it does not transfer to new interventions or contexts, and that it
    decays under optimisation pressure.

  READ-CHANNEL INDEPENDENCE ATTESTATION: I did not read `lit_search_results/for/`, any *_for file,
    `lit_search_returns.md`, or any 15a output for this item.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1124
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b (2026-10-12): Inferred from 2026-10-12 transcripts, where proxy signals (timestamps,
        record-exists) were treated as standing in for target state.
      15b (2026-10-13): Searched for challenging literature. 3 searches: Fleming & DeMets 1996 / CAST;
        Prasad et al. 2015 trial-level surrogate validation; Manheim & Garrabrant 2018 Goodhart
        taxonomy. No fetch. Also uses Huang et al. 2017 (fetched under ASSUMPTION-1778).
    Current status: PARTIALLY-CHALLENGED

  EVIDENCE GRADE: PRELIMINARY. Snippets, abstracts and secondary summaries, plus one full-text source
    carried over from 1778.
  Search scope: preliminary (3 searches, 0 new fetches).

  Challenging evidence found: Yes
  Strength of challenge: Moderate

  Sources:
    1. Fleming TR & DeMets DL. 1996. "Surrogate end points in clinical trials: are we being misled?"
       Ann Intern Med 125:605-613. [abstract and secondary summary, DeMets slides] In CAST, encainide
       and flecainide suppressed the surrogate (PVCs) while more than tripling mortality. The paper
       gives four failure modes, including "the intervention acts through pathways independent of the
       surrogate". Correlation between surrogate and outcome is not enough. The treatment effect must
       be mediated by the surrogate, and that is intervention-specific. Bearing: a proxy validated under
       one mechanism of change can fail silently when the system changes by a different mechanism.
    2. Prasad V, Kim C, Burotto M, Vandross A. 2015. "The Strength of Association Between Surrogate End
       Points and Survival in Oncology." JAMA Intern Med 175(8):1389-98. [snippet/abstract] Of 65
       trial-level surrogate-survival correlations, 52% were weak (r ≤ 0.7) and only 23% strong
       (r ≥ 0.85). Many surrogates were nonetheless in regulatory use. Bearing: even in a domain with
       formal validation machinery, most proxies that have been "validated" do not meet a strong
       standard. In practice validation is often a ritual and not a guarantee.
    3. Manheim D & Garrabrant S. 2018. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585.
       [abstract/snippet] Four mechanisms (regressional, extremal, causal, adversarial). The importance
       of each depends on how much optimisation pressure is applied to the proxy. Bearing: validation
       done before optimisation pressure is applied does not certify behaviour under that pressure
       (extremal Goodhart). Agents that learn what the check inspects are a case of
       adversarial/causal Goodhart.
    4. Huang et al. 2017 (see ASSUMPTION-1778) [full text]. Heartbeats work as a validated proxy for
       fail-stop failures and diverge for gray failures, a regime change of the kind CAST describes.

  Summary: The surrogate-endpoint literature is the most mature body of work on proxies, and it argues
    against the comfortable reading of "validation keeps them honest". Validation is specific to a
    mechanism (CAST). Most formal validations in oncology yield only weak correlations (Prasad). The
    Goodhart taxonomy predicts that validation done before a proxy is optimised against says little
    about its behaviour afterwards. Validation is necessary but has to be repeated, specific to the
    mechanism of change, and done against the true target (end-to-end outcome), not against another
    proxy.

  Specific risks: (a) A one-time audit "validates" that the freshness timestamp tracks real work. Later
    a new failure mode (fresh but empty output) breaks the link without anyone noticing. (b) The
    validation reference is itself a proxy, for example "a downstream file exists", so the validation
    goes in a circle. (c) Agents optimise toward what the checks inspect.

  Mitigations available: Revalidate periodically against a true-outcome sample, such as a human or deep
    audit of N items. Revalidate whenever the producing agent's prompt or mechanism changes. Track the
    proxy-target agreement rate over time as its own metric. Use more than one proxy so that no single
    one is optimised against.

  STEELMAN:
    Item: PRESUMPTION-1124
    Strongest counterargument: Validation does not stop proxies from drifting. It records how well they
      tracked the target under the conditions that held during validation. CAST's surrogate was
      plausible, mechanistically motivated, and it moved in the right direction, and patients died.
      Oncology's formally validated surrogates are mostly weakly correlated with survival. A C2A2
      health signal validated once, in one failure regime, is weaker than either of these. Validation
      is the start of an ongoing measurement of proxy-target agreement, not a certificate.
    What would need to be true for C2A2 to be safe: Proxy-target agreement is re-measured on a
      schedule and after every mechanism change. The reference standard is an end-to-end outcome.
    How to test: For one month, pair each proxy-green reading with a sampled deep check. Report
      sensitivity and specificity of the proxy, and repeat after the next agent-prompt change.

  Recommendation: PARTIALLY-CHALLENGED (the premise survives only in its "continuous revalidation"
    form)

  SYSTEMIC-RISK-FLAG: see SYSTEMIC-RISK-FLAG_2026-10-13_remedy-is-another-proxy_1778-1780-1124-1125-1127.md

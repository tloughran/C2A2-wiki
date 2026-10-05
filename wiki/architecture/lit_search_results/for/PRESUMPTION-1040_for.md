SEARCH-FOR-PRESUMPTION-1040:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1040
  Original statement: Registry liveness does not track process liveness. A status flag set at launch cannot distinguish a slow process from a dead one; only a progress heartbeat with a timeout can, and that distinction is provably not free.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1040
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (third observed instance of registry status diverging from process state; downstream drain currently zero)
      15a: Searched for supporting literature; found foundational failure-detector theory plus QoS and practice sources; strength: Moderate-to-Strong (see Caveats on sub-claims)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed Systems." Journal of the ACM 43(2), 225-267. DOI 10.1145/226643.226647. (Text read via https://cs.nyu.edu/~apanda/classes/sp25/papers/chandra-toueg.pdf) — States that the impossibility results stem from the difficulty of determining whether a process has crashed or is only very slow; defines failure detectors by completeness and accuracy and shows useful detectors are necessarily unreliable (may make mistakes). Directly supports "slow vs dead is not distinguishable by status alone" and "detection is not free" (accuracy is traded for completeness).
    2. Fischer, M.J., Lynch, N.A. & Paterson, M.S., 1985. "Impossibility of Distributed Consensus with One Faulty Process." Journal of the ACM 32(2), 374-382. (Located via search; PDF at https://groups.csail.mit.edu/tds/papers/Lynch/jacm85.pdf; contents not fetched here, relied on Chandra-Toueg's characterization of it.) — Foundational impossibility: in an asynchronous system a single crash cannot be told apart from arbitrary delay. Theoretical grounding for the "provably" part.
    3. Chen, W., Toueg, S. & Aguilera, M.K., 2002. "On the Quality of Service of Failure Detectors." IEEE Transactions on Computers 51(5). (Abstract read at https://www.microsoft.com/en-us/research/publication/quality-service-failure-detectors/) — Frames failure detection by two quantities, detection speed and avoidance of false detections; the abstract fetched did not state the tradeoff formula explicitly, so the speed/accuracy tension is the tool's gloss, to be confirmed against full text. Supports the "not free" claim in a heartbeat-timeout setting.
    4. Kubernetes documentation, "Configure Liveness, Readiness and Startup Probes" (https://www.kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-probes/). — Practice precedent: production orchestrator separates launch/registered state from liveness probes (restart on failure), readiness probes and startup probes. Page existence and title confirmed; body text was NOT retrievable in this search, so specific doc claims are unverified.

  Strength of support: Moderate (Strong for the theoretical core; Weak for the practice and job-scheduler sub-claims)

  Summary: Distributed-systems theory strongly supports the core claim. In asynchronous systems a crashed process cannot be distinguished from a slow one (FLP; Chandra & Toueg), so a static flag set at launch carries no information about later liveness, and any detector that does distinguish them must rely on timing assumptions (timeouts) and will sometimes be wrong. Chen/Toueg/Aguilera treat the resulting detection-speed versus false-positive tradeoff as a quantified design problem, consistent with "not free." Kubernetes' separation of liveness, readiness and startup probes is an engineering precedent for treating launch status and ongoing liveness as distinct signals.

  Caveats:
    - "Provably not free" is supported in the failure-detector sense (unreliability/tradeoff), not as a proof about registry flags or progress heartbeats specifically. Chandra-Toueg and FLP concern crash detection under asynchrony; the "progress heartbeat" (application-level progress, not just process-alive) is an extension not directly covered by those papers.
    - "Only a progress heartbeat with a timeout can" is stronger than the literature: other mechanisms exist (leases, OS-level process supervision/waitpid, which detects death on the same host reliably since the parent observes exit). Where the registry and process share a supervisor, process death is directly observable, weakening "only".
    - Liveness (process alive) vs progress (making headway on work) are distinct; heartbeats prove the former, not the latter, unless emitted from the work loop. Not searched in depth.
    - Searches for supervisor trees (Erlang/OTP) and dead-man's-switch/absence-alarm literature were not completed; search scope is preliminary, broader search recommended. Kubernetes page body unverified. FLP and Chandra-Toueg are foundational and subject to publication-bias only mildly, but their assumptions (asynchrony, crash faults) may not match C2A2's agent-job environment.

  Search scope: web search for Chandra-Toueg, FLP, Chen et al. QoS, Kubernetes probes; fetched Chandra-Toueg text, Chen et al. abstract page, K8s page (empty body). Tradition wikis not consulted. Preliminary search — broader search recommended.

  Recommendation: PARTIALLY-SUPPORTED

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1040
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Chandra, T.D. & Toueg, S., 1996. "Unreliable Failure Detectors for Reliable Distributed Systems." JACM 43(2).
  Summary: Theory (FLP, Chandra-Toueg) strongly supports that slow and dead are indistinguishable without timing assumptions and that detection incurs accuracy/speed cost; "only a progress heartbeat" and "provably" as applied to registry flags are stronger than the literature states.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1040_for.md

NOVELTY-FLAG: not warranted (the core claim is well covered by existing literature; only the application-level progress-heartbeat framing for agent registries is unaddressed, which does not rise to novelty).

Queue summary: PRESUMPTION-1040 [SEARCHED-15a: 2026-10-05] PARTIALLY-SUPPORTED, Moderate; FLP/Chandra-Toueg ground core claim, "only heartbeat"/"provably" overreach; preliminary scope.

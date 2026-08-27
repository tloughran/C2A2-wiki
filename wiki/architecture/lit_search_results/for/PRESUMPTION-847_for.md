SEARCH-FOR-PRESUMPTION-847:
  Date searched: 2026-08-25
  Original item: PRESUMPTION-847
  Original statement: [inferred] That a terminal marker is an account — that a run which stops
    has thereby explained itself.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-847
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from four identical terminal markers over four different failure surfaces.
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Search scope: WebSearch, August 2026, no date restriction. Queries covered: proximate cause vs.
    root cause in postmortem practice (Cook, resilience engineering); log sufficiency for failure
    diagnosis (LogEnhancer, ASPLOS'11); empirical analysis of production failures and the evidence
    available in logs (Yuan et al., OSDI'14); exit-code and signal taxonomies for abnormal
    termination (SIGKILL / exit 137 / OOMKilled); blameless postmortem methodology and evidence
    sufficiency (Dekker's "second story"). Classification: comprehensive for the systems-diagnosis
    and postmortem-methodology literature; preliminary on any work that would *defend* the claim,
    because I could locate essentially none. Gaps: I searched specifically for literature arguing
    that termination records are diagnostically sufficient and found no such position advanced
    anywhere; the closest supportive material is the design intent behind structured exit-status
    conventions.

  Supporting evidence found: Partial

  Sources:
    1. Kubernetes/Docker exit-status documentation and analysis, e.g. Spacelift, "Exit Code 137 —
       Fixing OOMKilled Kubernetes Error," https://spacelift.io/blog/oomkilled-exit-code-137 ;
       Komodor, "How to Fix OOMKilled (Exit Code 137)," https://komodor.com/learn/how-to-fix-oomkilled-exit-code-137/ ;
       Middleware, "Exit Code 137 in Kubernetes: Causes, Diagnosis, and Fixes,"
       https://middleware.io/blog/exit-code-137-in-kubernetes-causes-diagnosis-fixes/
       — [read as search snippets] This is the strongest support available for the claim, and it
       is genuine but narrow. Terminal markers are *deliberately designed* to be self-describing:
       exit code 137 decomposes as 128 + 9, naming SIGKILL as the terminating signal; and
       orchestrators add a dedicated reason field — Kubernetes' `Reason: OOMKilled`, Docker's
       `OOMKilled` flag in `docker inspect` — whose entire purpose is to make the terminal marker
       carry its own cause. Where such a field is populated, a terminal marker really does
       constitute a (partial) account, and the platform intends it to.
    2. Same source set, contrary detail recorded for honesty: semicolony.dev, "exit code 137 —
       SIGKILL, and why it is not always out-of-memory," https://semicolony.dev/errors/exit-code-137
       — [read as search snippet] "137 means the process was killed by SIGKILL (128 + 9), and the
       OOM killer is only one possible sender; stop-timeout escalations, CI runners, and
       orchestrators send the very same signal." Directly bounds how much account a bare terminal
       marker can give: the marker names the mechanism, not the agent or the reason, and
       disambiguating requires evidence from outside the run (the node's `dmesg`, the inspect flag).
    3. Yuan, D., Zheng, J., Park, S., Zhou, Y., Savage, S., 2011/2012. "Improving Software
       Diagnosability via Log Enhancement." *Proceedings of ASPLOS '11* (Best Paper nominee); also
       *ACM Transactions on Computer Systems*, DOI 10.1145/2110356.2110360.
       https://www.eecg.toronto.edu/~yuan/papers/logenhancer-tocs.pdf
       — [read as search snippet + abstract] Premise of the paper is the negation of this claim:
       diagnosing field failures is "exacerbated by the paucity of information that is typically
       available in the production setting," and "the ad-hoc nature of such reports [is] frequently
       insufficient for detailed failure diagnosis." The contribution — automatically enhancing
       existing logging code so as to "dramatically reduce the set of potential root failure causes
       that must be considered" — presupposes that existing terminal/log records leave a large
       candidate set open. Included because it is the definitive treatment of the question the
       claim answers affirmatively.
    4. Yuan, D., Luo, Y., Zhuang, X., Rodrigues, G., Zhao, X., Zhang, Y., Jain, P.U., Stumm, M.,
       2014. "Simple Testing Can Prevent Most Critical Failures: An Analysis of Production Failures
       in Distributed Data-Intensive Systems." *Proceedings of the 11th USENIX Symposium on
       Operating Systems Design and Implementation (OSDI '14)*.
       https://www.usenix.org/system/files/conference/osdi14/osdi14-paper-yuan.pdf
       — [read as search snippet + abstract] Empirical study of 198 randomly selected user-reported
       production failures across Cassandra, HBase, HDFS, Hadoop MapReduce and Redis, tracing "how
       one or multiple faults eventually evolve into a user-visible failure." The framing — faults
       plural, evolving into a failure — is the standard finding that a terminal event is the end
       of a chain rather than a summary of it. I did not obtain full text and so do not cite any
       specific statistic from it.
    5. Cook, R.I., 1998/2000. "How Complex Systems Fail." Cognitive Technologies Laboratory,
       University of Chicago. https://how.complexsystems.fail/
       — [read as search snippet + landing page] "Post-accident attribution to a 'root cause' is
       fundamentally wrong," because complex systems "run with multiple latent flaws that only
       produce an outage in combination"; "because overt failure requires multiple faults, there is
       no isolated 'cause' of an accident... each of these is necessarily insufficient in itself."
       This is the methodological position against which the claim must be assessed, and it does
       not support it.
    6. Dekker, S., as summarised in blameless-postmortem practitioner literature, e.g. PagerDuty,
       "The Blameless Postmortem," https://postmortems.pagerduty.com/culture/blameless/ ; Atlassian,
       "How to run a blameless postmortem," https://www.atlassian.com/incident-management/postmortem/blameless
       — [read as search snippets; Dekker's primary works not reached] The "second story" framing:
       "underneath every simple, obvious story about human error, there is a deeper, more complex
       story about the organization." Relatedly: "a production incident can have a trigger without
       having one sufficient explanation." [Dekker attribution: quotation reached via secondary
       summary only — primary bibliographic details unverified.] Supports the claim only in the
       trivial sense that the trigger is real evidence; denies that it is an account.

  Strength of support: Weak

  Summary: There is real but narrow support for this claim, and it lives entirely in the design of
    structured terminal markers. Exit statuses and signal encodings are deliberately built to be
    self-describing — 137 decomposes into 128 + SIGKILL — and container orchestrators go further,
    attaching a dedicated reason field (`Reason: OOMKilled`) whose explicit purpose is to make the
    termination record carry its own cause. Where such a field is present and populated, a terminal
    marker genuinely does explain the run, and the platform's designers intended exactly that.
    Beyond this the literature runs the other way and does so with unusual consistency: the same
    exit-status sources note that SIGKILL has several possible senders and that disambiguation
    requires evidence gathered outside the run; Yuan et al.'s LogEnhancer work is premised on
    production log records being "frequently insufficient for detailed failure diagnosis" and
    leaving a large candidate-cause set open; and the resilience-engineering tradition from Cook
    onward holds that a terminal event marks where a chain surfaced rather than summarising why.
    I searched specifically for a position defending the diagnostic sufficiency of termination
    records and found none advanced anywhere.

  Caveats: (a) The support is conditional on the terminal marker being *structured and populated* —
    a reason field, a signal number, a typed error. A bare, undifferentiated terminal marker (the
    condition described in the provenance: four identical markers over four different failure
    surfaces) falls outside even this narrow support, since identical markers across distinct
    surfaces are by construction not discriminating between them. (b) Domain-transfer risk is low
    in the unhelpful direction: the diagnosis literature is drawn from large distributed data
    systems and from safety-critical accident analysis, both of which are more complex than a
    scheduled-job fleet — one could argue simpler systems admit simpler accounts, but I found no
    source making that argument. (c) The Dekker material was reached only through secondary
    practitioner summaries; primary bibliographic details are unverified. (d) I did not obtain full
    text for either Yuan et al. paper and have deliberately cited no numeric findings from them.

  Recommendation: PARTIALLY-SUPPORTED

  PARTIAL NOVELTY-FLAG:
    Item: PRESUMPTION-847
    Searched: proximate vs. root cause in postmortem practice; error and exit-status taxonomies in
      job schedulers and container runtimes; log-sufficiency literature for failure diagnosis;
      blameless postmortem methodology on evidence sufficiency; empirical production-failure
      analyses.
    Finding: The general question — how much a termination record explains — is very well addressed,
      and the answer the literature gives is "less than it appears to." What is unaddressed is the
      specific epistemic situation in the provenance: a marker that is *identical across
      distinguishable failure surfaces*. The literature treats under-informative logs as a coverage
      problem (not enough was recorded) or a complexity problem (no single cause exists). I found no
      treatment of the case where the marker is uniform by design and its uniformity is itself the
      diagnostic signal — i.e. the inference that four identical terminal markers over four
      different surfaces indicates a common terminating agent external to all four rather than four
      coincident internal faults.
    Implication: The claim's supported region is limited to structured, reason-bearing terminal
      markers. Where markers are uniform and unreasoned, the literature offers no basis for treating
      them as accounts, and offers no established method for reading uniformity-across-surfaces as
      evidence in its own right.
    Recommended status: PARTIAL NOVELTY — unaddressed sub-claim: that an undifferentiated terminal
      marker, identical across distinct failure surfaces, constitutes an explanation of the run.

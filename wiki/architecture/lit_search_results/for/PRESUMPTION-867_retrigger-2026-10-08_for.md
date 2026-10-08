SEARCH-FOR-PRESUMPTION-867 (OWED LIMB ONLY: conjunct 2 — success accounting of failure-reporting runs):
  Date searched: 2026-10-08
  Original item: PRESUMPTION-867
  Original statement: "A 'fail loud' norm improves system health; its second-order effect on success
    accounting is benign."
  Limbs searched: conjunct 2 only, i.e. whether a run that ends by faithfully reporting total failure can
    be booked as a completed/successful run without corrupting the aggregate health metric. "Support" =
    evidence that such booking is harmless, or a documented practice under which it is harmless.
    Conjunct 1 is not re-searched (its SUFFICIENCY reading is already refuted by PREMISE-102/PREMISE-173).
  Cycle: 1 (RE-TRIGGER by 15d 2026-09-13, MONITOR-551; processed 2026-10-08)

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15a (re-trigger cycle 1)]
    Original item: PRESUMPTION-867
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from three same-day runs that completed by reporting total failure
      15a (cycle 0, 2026-08-25): PARTIALLY-SUPPORTED, Moderate (Strong clause 1; Weak-to-None clause 2);
        clause 2 carried only by the fail-stop analogy (Schlichting & Schneider 1983); partial NOVELTY-flag
      15b (cycle 0): PARTIALLY-CHALLENGED, Moderate, clause 1 only; clause 2 not searched (budget);
        declined to cite Goodhart/Vaughan from memory
      15c: DISPOSITION-808 → MONITOR-551 (HIGH)
      15d: re-triggered cycle 1 2026-09-13; owed = Manheim & Garrabrant, Vaughan, measurement gaming,
        Inozemtseva & Holmes 2014; 15d did not evaluate evidence
      15a (cycle 1, 2026-10-08): 4 searches, 3 fetch attempts (1 refused, 2 succeeded); see below
    Current status: PARTIALLY-SUPPORTED (conditional form only); NO-SUPPORT-FOUND for the unconditioned
      claim that booking failure-reports as successes is benign

  Search scope: 4 web searches (Manheim & Garrabrant Goodhart taxonomy; Inozemtseva & Holmes 2014;
    Vaughan normalization of deviance; lifecycle-status vs outcome-conclusion separation in CI tooling).
    Fetches: arxiv.org/abs/1803.04585 REFUSED (not in provenance set); arxiv.org/abs/1803.04585v4
    succeeded (abstract); cs.ubc.ca/~rtholmes/papers/icse_2014_inozemtseva.pdf succeeded (full text,
    abstract + conclusions read). All four named literatures were reached. Preliminary on "measurement
    gaming" as a separate literature (covered only via Goodhart's adversarial category).

  Supporting evidence found: Partial (for a conditional design, not for the presumption as stated)

  Sources:
    1. Manheim, D. & Garrabrant, S., 2018 (rev. 2019). "Categorizing Variants of Goodhart's Law."
       arXiv:1803.04585. [fetched, abstract] "There are several distinct failure modes for
       overoptimization of systems on the basis of metrics", sorted into regressional, extremal, causal and
       adversarial variants [variant names: search-result]. Read for support: none. The paper treats any
       proxy that diverges from its goal under pressure as a failure class. Booking a "reported total
       failure" as a success makes the success count diverge from task outcome by construction, which is
       the causal variant (intervening on the proxy does not move the goal). Recorded as the boundary
       source: it gives no condition under which the conflation is benign.
    2. Inozemtseva, L. & Holmes, R., 2014. "Coverage Is Not Strongly Correlated with Test Suite
       Effectiveness." ICSE 2014, 435–445. [fetched, full text; abstract + conclusions read] Coverage is
       "often used as a proxy" for fault detection. Once suite size is controlled for, the correlation is
       "low to moderate". Coverage is "useful for identifying under-tested parts of a program" but "should
       not be used as a quality target". The supportive reading, which is the only one available, is
       narrow. A proxy can stay informative when used diagnostically (to find gaps) rather than as a target.
       Its other lesson cuts against the item: an uncontrolled confound (suite size) inflated the apparent
       proxy validity, and counting failure-reporting runs as successes is a confound of the same shape.
    3. Vaughan, D., 1996. *The Challenger Launch Decision.* Univ. of Chicago Press. [search-result, via
       Columbia Magazine and THE summaries; book not read] Repeated anomalies were redefined as "acceptable
       risk" while "every prescribed procedure was followed and every box checked", so the organisation did
       not see the system as failing. No support. This is the mechanism by which a run that "completed"
       procedurally while reporting failure, if counted as success, would normalise the failure.
    4. GitHub REST API, "Using the REST API to interact with checks" (Enterprise Server 3.6/3.7 docs).
       [search-result] The only supportive precedent found, and it is a documented practice, not research.
       A check run has a lifecycle `status` (queued/in_progress/completed) and a separate `conclusion`
       (success/failure/timed_out/…/stale). A run can be `completed` with conclusion `failure`, and suite
       roll-ups report the highest-priority conclusion, so a completed failure surfaces as failure. This
       shows exactly how a failure-reporting run can be booked as COMPLETED without corrupting a SUCCESS
       metric: keep the two on separate fields.
    5. [carried from cycle 0, not re-read] Schlichting & Schneider 1983, fail-stop processors. It licenses
       "a failure-reporting component is behaving correctly". Read together with source 4, that maps onto
       `status = completed` and leaves the outcome field untouched.

  Strength of support: Weak. Moderate only for the narrowed, conditional claim (sources 4, 5); none for
    the claim as stated.

  Summary: All four literatures 15d named were reached. None supports booking a faithfully reported total
    failure as a success. Goodhart formalisations (1) classify the resulting divergence as a failure mode.
    Inozemtseva & Holmes (2) show how a confounded proxy overstates its own validity. Vaughan (3) gives the
    organisational trajectory by which procedurally complete failures become normal. What the search did
    find is support for a different, narrower claim. Production CI tooling (4) separates lifecycle
    ("completed") from outcome ("failure") as a matter of course, so a failure-reporting run can be
    recorded as correctly completed without touching the success rate. The fail-stop model (5) gives that
    separation its formal warrant. Conjunct 2 is supportable only if "completed" and "successful" are
    distinct fields and the health metric is computed on the outcome field.

  Caveats: (i) Source 4 is vendor documentation read at search-result level. (ii) Vaughan was read only
    through secondary summaries. (iii) Manheim & Garrabrant was read at abstract level, and the variant
    definitions came from search summaries. (iv) None of these sources measures the effect in an LLM-agent
    pipeline. MONITOR-551's in-house test (the 49-day success rate with and without failure-reporting
    runs counted as successes) remains the decisive discriminator and needs no literature.

  Recommendation: PARTIALLY-SUPPORTED, for the conditional "booked as COMPLETED on a lifecycle field,
    never as SUCCESS on the outcome field". NO-SUPPORT-FOUND for the presumption as stated. By MONITOR-551's
    own rule, the honest supportive result points toward REVISE with the separation as the fix, not
    INCORPORATE.

  NOVELTY-FLAG: No. Cycle 0's partial novelty flag on clause 2 is withdrawn. The metric-inflation pathway is
    addressed by the Goodhart/proxy literature (against), and the two-field remedy is established practice.

  Independence attestation: Read: agents/15a_lit_search_for_agent.md; architecture/provenance_protocol.md;
    for/PRESUMPTION-897_retrigger-2026-10-07_for.md (format); for/PRESUMPTION-867_for.md (cycle 0);
    for_lit_search.md ~21499–21535; monitor_queue.md MONITOR-551. NOT read: any against/ file dated 2026-10-08.

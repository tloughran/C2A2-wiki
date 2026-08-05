SEARCH-AGAINST-PRESUMPTION-660:
  Date searched: 2026-08-04
  Original item: PRESUMPTION-660
  Original statement: That a fallback check answers the same question as the check it
    replaces — two disclosed substitutions whose qualifications did not reach the artifact
    carrying the PASS.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-660
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the 2026-08-03 observation of two disclosed check substitutions
        whose qualifications were absent from the PASS-bearing artifact
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Fleming, T.R. & DeMets, D.L., 1996. "Surrogate End Points in Clinical Trials: Are
       We Being Misled?" Annals of Internal Medicine, 125(7), 605-613. — The foundational
       statement that a proxy correlated with the true endpoint is not thereby a valid
       substitute for it; a surrogate can move in the right direction while the outcome of
       interest moves in the wrong one, because the intervention acts through pathways the
       surrogate does not capture.
    2. (2023). "A framework for the definition and interpretation of the use of surrogate
       endpoints in interventional trials." eClinicalMedicine (Lancet Discovery Science).
       — Modern framework enumerating the ways surrogates fail: not capturing intervention
       effects, missing the safety profile entirely, and licensing approval of harmful
       interventions. Cites the rosiglitazone case, where blood-glucose and HbA1c proxies
       supported approval while cardiovascular harm led to withdrawal a decade later.
    3. (2023). "Definitions, acceptability, limitations, and guidance in the use and
       reporting of surrogate end points in trials: a scoping review." Journal of Clinical
       Epidemiology. — Documents systematic under-reporting of surrogate limitations in
       the artifacts that carry the conclusion; the qualification is known to the analysts
       and absent from the abstract. This is structurally the same defect as the item.
    4. Kubernetes probe guidance (e.g. Better Stack, "Kubernetes Health Checks and Probes";
       web-alert.io, "Health Check Endpoint Design: /health, /livez, /readyz"). — "TCP
       probes pass on applications that accept connections but can't serve anything," and
       the always-200 health check is named explicitly as a check that hides real failures.
       The substitution of a cheaper probe for a deeper one changes the question answered.
    5. Risknowlogy, "Graceful Degradation — Degraded Mode in Safety Systems"; SRE School,
       "Graceful Degradation." — Both make the alerting-property point: graceful degradation
       hides failures by design, a fallback can remain silently active for days while the
       surface looks fine, and the corrective is to alert on the degraded state itself so
       that reduced functionality is a tracked signal rather than an invisible one.
    6. Huang, P. et al., 2017. "Gray Failure." HotOS '17. — The PASS-emitting substituted
       check is a differential-observability instance: detector says healthy, subject is not.

  Strength of challenge: Strong

  Summary: The surrogate-endpoint literature is a thirty-year, high-stakes,
    heavily-replicated demonstration that a substitute measure does not answer the same
    question as the measure it replaces, even when the correlation is strong and the
    substitution is made in good faith by experts. Fleming and DeMets is the canonical
    statement; the modern frameworks add that surrogates fail specifically by missing the
    harm pathway, which is the pathway a check exists to detect. The scoping review then
    identifies the exact defect named in the item — the qualification is known to the
    people doing the work and does not travel with the conclusion into the artifact that
    downstream readers consume. The engineering literature converges independently: a
    shallow probe passes on a hung process, and degraded-mode operation is documented to
    hide failure by design unless the degradation itself is alerted on. Two disclosed
    substitutions whose qualifications did not reach the PASS artifact is therefore not a
    minor documentation gap; it is the exact mechanism by which proxy substitution causes
    harm in every domain searched.

  Specific risks: The artifacts carrying PASS now assert more than was tested, and no
    downstream reader can recover the difference. If the substituted checks are weaker in
    the relevant dimension — which is the typical reason for substituting — then the class
    of failure the original check existed to catch is now uncovered while being reported as
    covered. Because the disclosure exists somewhere but not in the artifact, the system
    will also fail an audit in a particularly bad way: the qualification is discoverable
    after the fact, establishing that the gap was known and not propagated. The
    degraded-mode literature adds the temporal risk: substitutions introduced as temporary
    persist silently, and there is currently no signal that would reveal how long they have
    been active. This compounds directly with PRESUMPTION-655 (no provenance on
    verification marks) and PRESUMPTION-648 (a suppressed validator still emitting PASS) —
    three independent routes to the same outcome: an unqualified PASS with no record of what
    actually ran.

  Mitigations available: (1) Make PASS carry its own provenance: no artifact should emit a
    bare PASS; it should emit PASS(check=X, method=Y, substitutions=[...]). If the field is
    empty it should say so explicitly. (2) Introduce a distinct verdict value — PASS-DEGRADED
    or PASS-BY-PROXY — so that the two cases are not representable by the same token. This is
    the single highest-value change and it is purely mechanical. (3) Alert on the degraded
    state itself, per the safety-systems guidance: a fallback that has been active for more
    than N runs should raise, independent of whether it is passing. (4) Validate the proxy
    before trusting it: construct an input that the original check would fail and confirm the
    substitute also fails it. If it passes, the substitution is invalid and this is
    demonstrable in one test. (5) Give every substitution an owner and an expiry, and treat an
    expired substitution as a failing check rather than a passing one.

  Recommendation: CHALLENGED

  STEELMAN:
    Item: PRESUMPTION-660
    Strongest counterargument: The substitutions were disclosed — the information exists and
      was not concealed, which distinguishes this sharply from the surrogate-endpoint
      failures where the proxy was presented as equivalent. A fallback check that covers most
      of the original's ground is far better than no check while the original is unavailable,
      and the alternative (failing closed) would have blocked all work for a defect that may
      be immaterial. The surrogate literature also concerns irreversible regulatory decisions
      affecting patients; a wiki PASS is a low-stakes, re-runnable assertion, so the cost of a
      proxy mismatch is bounded and cheaply corrected once noticed. Requiring every
      qualification to propagate into every artifact is a real engineering cost that may
      exceed the risk.
    What would need to be true for C2A2 to be safe: (a) The substitute check is demonstrably
      sensitive to the same failure class as the original — tested, not assumed. (b) The
      substitution is short-lived and its duration is recorded. (c) Every consumer of the
      PASS artifact has access to, and actually consults, the disclosure. (d) No irreversible
      or compounding decision is taken on the strength of a substituted PASS.
    How to test: Cheap and decisive. Take a known-bad input that the original check catches.
      Run it through both fallback checks. If either returns PASS, the construct-validity
      challenge is confirmed empirically for this system. Separately, grep the PASS-bearing
      artifacts for any mention of the substitution; absence confirms the propagation failure
      that the scoping review describes.

  Search scope: Adequate. Concepts searched: construct validity of proxy and surrogate
    measures; surrogate endpoint failures and reporting of limitations; shallow vs deep
    health checks and probes that pass on hung processes; degraded-mode monitoring and
    retention of alerting properties under substitution.

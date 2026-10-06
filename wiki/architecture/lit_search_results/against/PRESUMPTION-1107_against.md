SEARCH-AGAINST-PRESUMPTION-1107:
  Date searched: 2026-10-03
  Original item: PRESUMPTION-1107
  Original statement (presumption under test): A monitoring task's successful action (a ping, a prior PASS, a registry entry) is a valid measure of the outcome the task exists to secure.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1107
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred across three sessions; generalises PRESUMPTION-890.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Fleming, T.R. & DeMets, D.L., 1996. "Surrogate End Points in Clinical Trials: Are We Being Misled?" Annals of Internal Medicine 125(7):605–613 [search-result; full text located at edisciplinas.usp.br] — For a surrogate to be valid, the intervention's effect on the surrogate must reliably predict its effect on the true outcome; "in practice, this requirement frequently fails". Correlation with the outcome is not sufficient; failure occurs when the surrogate is not on the causal pathway or when the intervention acts through pathways the surrogate misses. Direct analogue: "the ping succeeded" is a surrogate for "the project stayed up".
    2. Manheim, D. & Garrabrant, S., 2018. "Categorizing Variants of Goodhart's Law." arXiv:1803.04585 [search-result] — Four mechanisms (regressional, extremal, causal, adversarial) by which optimizing or relying on a proxy decouples it from the goal. Causal Goodhart applies directly: the action (ping) can occur without the causal effect on the goal (activity being credited).
    3. Beyer, B. et al., 2016. Site Reliability Engineering (Google), ch. 6 "Monitoring Distributed Systems" [background-knowledge] — Recommends symptom-based (user-visible outcome) alerting over cause-/action-based checks; black-box probes confirm reachability, not correct service.
    4. "99.99% Uptime, 5% Rage: How Synthetic Monitoring Lets You Lie to Yourself" (HackerNoon); drdroid.io "Symptom-Based Alerts" [search-result, practitioner sources] — Synthetic checks test only expected paths and pass while real outcomes fail; recommend combining synthetics with outcome/RUM and SLO monitoring.

  Strength of challenge: Strong

  Summary: Across clinical trials, measurement theory and SRE practice, an action or proxy succeeding is not accepted as evidence that the target outcome holds unless the proxy has been validated as causally and predictively linked to it. Fleming and DeMets document that this link "frequently fails" even for correlated biomarkers; Goodhart variants show proxies decouple further once they become the thing being checked; SRE doctrine treats probe success as a check on reachability, not on outcome. A ping returning 200, a prior PASS, or a registry entry each verifies that the task ran, not that the protected state (project unpaused, data fresh, coverage complete) exists.

  STEELMAN:
    Item: PRESUMPTION-1107
    Strongest counterargument: Every monitoring task that marks itself successful based on its own action is measuring itself rather than the world. The surrogate-endpoint literature shows such proxies fail exactly when the mechanism linking action to outcome is unknown or changeable; this is the case here (vendor pause heuristics, search-index coverage, registry staleness). A chain of PASSes can then build false confidence across sessions, and the failure shows up only when the outcome is directly observed, usually too late.
    What would need to be true for C2A2 to be safe: Each monitor directly observes the outcome variable (e.g., project status = ACTIVE; file content updated since T; an independent recall check), or the action-outcome link has been validated empirically and is re-validated periodically.
    How to test: For each monitoring task, write down the outcome it secures and check whether its PASS condition reads that outcome directly; inject a known failure (paused project, stale file) and confirm the monitor reports FAIL.

  Specific risks: Silent failures across multiple tasks; stale PASS carried forward; registry entry mistaken for existence/health of the thing registered.

  Mitigations available: Outcome-based assertions; periodic fault injection; expiry on prior PASS results; independent second check.

  Caveats: Proxy measures are sometimes adequate where the action-outcome link is tight and stable; the challenge is to treating the proxy as valid by default, not to proxies per se.

  Search scope: preliminary search (2 searches, 0 fetches) plus well-established background literature; independent of 15a.

  Recommendation: CHALLENGED

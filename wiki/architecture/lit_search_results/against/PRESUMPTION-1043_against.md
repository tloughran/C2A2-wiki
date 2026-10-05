SEARCH-AGAINST-PRESUMPTION-1043:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1043
  Original statement: A failure taxonomy organised per-component systematically hides causes shared across components, and the independence it implicitly assumes inflates estimates of system reliability.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1043
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference (per-component FAIL rows carried independently for 2+ weeks; both died on one shared 5.9 GB ceiling; related ASSUMPTION-1530/1531/1532, OPEN-244, PRESUMPTION-1044)
      15b: Searched for challenging literature; found no source refuting the core claim; found weak-to-moderate boundary-condition evidence (CCF quantification is data-starved and parameter-uncertain; ownership model is a long-standing practice with an accountability rationale); strength: Weak
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Search scope: PRELIMINARY — broader search recommended. Web search returned titles/URLs only; sources below were fetched and bibliographically checked (abstract level). Full texts were not read. No source was found that directly measures MTTR of per-component vs cross-cutting analysis, and none that directly argues per-component ownership costs are overstated. These two search directions are "not enough searched / literature gap", NOT "searched and found nothing".

  Sources:
    1. Hark, F., Britton, P., Ring, R., Novack, S.D., 2016. "Common Cause Failure Modeling." NASA Technical Reports Server, ntrs.nasa.gov/citations/20160007009. — Verified at abstract level. Notes launch-vehicle-specific CCF data is scarce, so NASA PRA borrows nuclear-plant databases. Boundary condition: CCF parameters (beta) are weakly grounded outside nuclear, so the quantitative correction to reliability is itself highly uncertain.
    2. Zheng, X., Yamaguchi, A., Takata, T., 2013. "α-Decomposition for estimating parameters in common cause failure modeling based on causal inference." Reliability Engineering & System Safety 116:20-27. — Verified at abstract level. Frames CCF parameter estimation under limited data as a persistent uncertainty problem requiring Bayesian-network machinery; supports the "over-parameterised / hard to estimate" objection (though it is a method to mitigate it, not a refutation).
    3. Shorthill, T., Bao, H., Chen, E., Ban, H., 2022. "An Application of a Modified Beta Factor Method for the Analysis of Software Common Cause Failures." arXiv:2206.11321. — Verified at abstract level. Software CCF analysis is possible but needs a modified beta-factor model because operational CCF data is scarce and components belong to multiple failure groups. Transfer-condition evidence: classical CCF models do not port cleanly to software; relevant to C2A2 (software/agent estate).
    4. Guey, C.N., 1984. "A method for estimating common cause failure probability and model parameters: the inverse stress-strength interference (ISSI) technique." MIT (dspace.mit.edu/handle/1721.1/60627). — Verified at abstract level. Found beta-factor results comparable to alternative method; illustrates that CCF estimates are model-dependent when failure data are scarce.
    5. O'Hanlon, C., 2006. "A Conversation with Werner Vogels." ACM Queue 4(4):14-22 (doi:10.1145/1142055.1142065). — Bibliographic details verified; contents NOT read in this session. Commonly cited origin of "you build it, you run it" per-service ownership. Cited only as the canonical statement of the ownership position the claim must contend with; it supplies no measured MTTR result.
    6. Google SRE Book, ch. 15 "Postmortem Culture: Learning from Failure" (sre.google/sre-book/postmortem-culture/). — Fetched. Describes blameless postmortem practice; the page does NOT address action-item ownership or shared/cross-cutting causes. Reported as a gap, not as challenge.

  Strength of challenge: Weak
    (Core claim — per-component decomposition hides shared causes — is not contradicted. The challenge is limited to: (a) quantified correction is poorly parameterised outside nuclear, (b) ownership-based practice has an accountability rationale but no located evidence that it outperforms cross-cutting analysis.)

  Summary: Nothing located refutes the claim that independence assumptions inflate reliability estimates when shared causes exist; the CCF literature found (sources 1-4) presupposes this. What the literature does challenge is the claim's practicality: CCF parameters are data-starved and model-dependent outside nuclear/aerospace, and classical beta-factor models need modification for software. The ownership counter-position (source 5) is a widely held practice, but no empirical comparison of MTTR under per-component vs cross-cutting analysis was found. The claim's wording "systematically" and "inflates" is the least-supported part: inflation direction is generally established, magnitude is not estimable for C2A2 without local data.

  Specific risks: (1) If C2A2 responds by building a formal CCF model (beta/alpha factors) with only ~2 observed shared-cause events, parameters will be unsupported and could give false precision; (2) adding a cross-cutting taxonomy layer may slow repair or blur ownership if shared causes are rare; (3) the one 5.9 GB ceiling event may be a single observation (N=1 common cause) over-generalised into a systemic claim.

  Mitigations available: Treat the shared-cause category as a qualitative tag/field on existing rows (cheap, keeps per-component ownership) rather than a quantitative model; use a Bayesian/prior-based approach with explicit uncertainty (sources 2, 3); track MTTR with and without the shared-cause tag to test the ownership objection locally; revisit once more shared-cause incidents accumulate.

  Recommendation: PARTIALLY-CHALLENGED (weak; preliminary scope)

STEELMAN:
  Item: PRESUMPTION-1043
  Strongest counterargument: Common-cause modelling earns its keep in nuclear and aerospace because incident data are pooled across hundreds of plants over decades and consequences are catastrophic. A small software/agent estate has neither: with a handful of incidents, any estimated shared-cause fraction is dominated by prior choice, and the literature itself must borrow data across domains (NASA from nuclear) or invent modified models for software. Meanwhile, per-component ownership gives a named responder, a bounded diagnostic scope and fast repair; a cross-cutting taxonomy risks diffusing accountability so that the shared substrate is "everyone's problem". Under this view, two FAIL rows dying on one ceiling is a single anecdote best fixed by one targeted patch, not evidence that the taxonomy is systematically biased or that reliability estimates were meaningfully inflated.
  What would need to be true for C2A2 to be safe: Shared-cause events remain rare and cheap to detect ad hoc; the per-component rows are not being used to compute system-level reliability numbers (so independence inflation has no downstream consumer); and the owner of each component can see substrate-level limits (quota, memory ceiling) from their own view.
  How to test: Review the full incident/FAIL history for how many failures had a shared upstream cause (fraction of events, not N=1); compare time-to-diagnose for events tagged shared-cause against component-local ones; check whether any decision actually used an independence-based reliability estimate.

SYSTEMIC-RISK-FLAG: not raised (single item reviewed; no cross-item shared vulnerability established by this search).

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1043
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak
  Key source: Hark, Britton, Ring, Novack, 2016. "Common Cause Failure Modeling." NASA NTRS 20160007009 (CCF data scarcity outside nuclear); also Shorthill et al., 2022, arXiv:2206.11321 (classical beta-factor needs modification for software CCF).
  Specific risk: A formal CCF model on very few observed shared-cause events would give false precision, and a cross-cutting layer could dilute per-component accountability if shared causes are rare; the N=1 ceiling event may be over-generalised.
  Summary: Core claim not contradicted; literature challenges only the tractability/parameterisation of quantifying it outside safety-critical domains. No empirical evidence located on MTTR of per-component vs cross-cutting analysis (literature gap; preliminary search).
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1043_against.md

QUEUE SUMMARY: [SEARCHED-15b: 2026-10-05] PRESUMPTION-1043 — PARTIALLY-CHALLENGED (Weak); core claim stands, quantification/ownership objections only weakly evidenced; preliminary scope. No SYSTEMIC-RISK flag.

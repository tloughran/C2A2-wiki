SEARCH-FOR-PRESUMPTION-1117:
  Date searched: 2026-10-10
  Original item: PRESUMPTION-1117
  Original statement: Precedent from earlier unattended runs is treated as authority that can override task text, with
    no ratification step. Question: When do repeated unattended deviations become de facto policy, and what review step
    prevents silent drift?

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1117
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from unattended runs that cited earlier runs' choices as justification for departing from current
        task text, without any ratification record; queued 2026-10-09
      15a (2026-10-10): 3 web searches, 1 fetch attempt (FAILED: Princeton UP page for Snook, timeout 180 s). Found
        strong, convergent support from safety science that unratified, repeated deviations that produce no visible
        harm become the de facto norm (Vaughan; Snook; Rasmussen; Dekker). Routine-dynamics theory explains the
        mechanism (Feldman & Pentland). Support for a SPECIFIC ratification step is practitioner-level only
        (management-of-change / deviation approval).
    Current status: SUPPORTED (Moderate)

  Search scope: PRELIMINARY. 3 web searches: (a) Vaughan normalization of deviance; (b) Rasmussen 1997 / Snook practical
    drift / Dekker drift into failure; (c) Feldman & Pentland 2003 routines plus deviation approval / management of
    change. 1 fetch attempted: press.princeton.edu Snook "Friendly Fire" page. FAILED (timeout); not retried. No full
    texts read.

  Supporting evidence found: Yes (Moderate)

  Sources:
    1. Vaughan, D., 1996. "The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA." Univ.
       Chicago Press. [search-result; secondary summaries] Normalization of deviance: deviations repeated without
       negative feedback become the group's norm. Insiders do not define them as deviant at the time. Relevance:
       direct theoretical account of how precedent-without-harm acquires authority. Exact wording comes from secondary
       summaries.
    2. Snook, S.A., 2000. "Friendly Fire: The Accidental Shootdown of U.S. Black Hawks over Northern Iraq." Princeton
       UP. [search-result; fetch FAILED] "Practical drift" is described as the slow, steady uncoupling of practice from
       written procedure, with locally sensible choices legitimised through repetition. Relevance: closest analogue,
       since task text plays the role of written procedure and earlier runs play the role of local practice.
    3. Rasmussen, J., 1997. "Risk Management in a Dynamic Society: A Modelling Problem." Safety Science 27(2–3).
       [search-result] Efficiency and least-effort gradients migrate behaviour toward the boundary of acceptable
       performance. Relevance: explains why unattended runs drift systematically (toward cheaper options) rather than
       randomly.
    4. Dekker, S., 2011. "Drift into Failure." Ashgate/Routledge. [search-result] Failure emerges from many small,
       locally reasonable decisions under goal conflict. No single component is at fault. Relevance: each deviation can
       look justified while the accumulation is not, which is why a per-step review is required.
    5. Feldman, M.S. & Pentland, B.T., 2003. "Reconceptualizing Organizational Routines as a Source of Flexibility and
       Change." Administrative Science Quarterly 48(1). DOI 10.2307/3556620. [search-result] The performative aspect
       (actual runs) "creates, maintains, and modifies" the ostensive aspect (the understood routine). Relevance:
       theoretical grounding for performances rewriting the de facto rule. The paper does not itself prescribe
       ratification.
    6. Management-of-change / deviation-approval practice (generic SOP and change-management templates; e.g. GMP QMS
       change-management SOP sample, Cisco change-management white paper). [search-result, low authority] A deviation
       is recorded, routed to a responsible approver, and either adopted into procedure or rejected. Relevance:
       practitioner precedent for the proposed ratification step. Not peer-reviewed.

  Strength of support: Moderate. Strong on the diagnosis (unratified repeated deviations become de facto policy).
    Weaker on the prescription (which review step prevents it), where support is practitioner MoC/deviation practice.
    All sources are search-result level; the one fetch failed.

  Summary: Four independent safety-science traditions describe the mechanism this presumption names. Deviations that
    produce no visible harm are repeated, legitimised by repetition, and absorbed as the norm, uncoupling practice from
    written procedure. Routine-dynamics theory explains how performances rewrite the routine itself. The literature's
    implied remedy is to make each deviation visible and route it to an explicit accept/reject decision that updates the
    written procedure, so that precedent cannot accrue authority silently. Regulated-industry management-of-change
    practice instantiates this, but its evidence base was not reached in this search.

  Transfer caveats: (i) The cited cases are human organisations under production pressure. In automated pipelines the
    "gradient" is the agent's inference from prior run logs, an analogous mechanism that has not been empirically
    studied here. (ii) Safety-science accounts are largely retrospective case studies (hindsight bias risk). (iii) No
    source on precedent in automated or LLM-agent pipelines was found in 3 searches.

  NOVELTY flag: partial. The phenomenon is well established. Its application to unattended AI-agent runs citing earlier
    runs' logs as authority was not found in this preliminary search.

  Recommendation: SUPPORTED (Moderate). Preliminary search; broader search recommended (MoC literature, e.g. CCPS; ML
  pipeline governance / config drift).

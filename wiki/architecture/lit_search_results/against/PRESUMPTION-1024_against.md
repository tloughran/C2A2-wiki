SEARCH-AGAINST-PRESUMPTION-1024:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1024
  Original statement: A permission tier that lets an unattended run create an artefact (Gmail draft) but not modify one is
    treated as safe because creation is the lower-risk act, without noticing the asymmetry makes the first draft the final
    draft and removes the run's only means of correcting an error it introduced.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-1024
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference: daily run wrote "7th failed attempt" into the decision draft,
           was auto-declined on update_draft, disclosed the error only in a log the recipient does not read (draft
           r8191906678905695603; inbox/PROCESSED_LOG.md l.1326-1327, l.1335). Pre-check found no covering premise.
      15b: Searched for challenging literature; found general support for gating modification/external-facing actions and for
           validate-before-write, but no source that directly refutes the claim that the asymmetry removes self-correction;
           strength: Weak
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial
  Search scope: PRELIMINARY — broader search recommended (no peer-reviewed work found on agent self-correction allowances;
    sources are standards/principles papers plus practitioner/vendor guidance).

  Sources:
    1. Saltzer, J. H. & Schroeder, M. D., 1975. "The Protection of Information in Computer Systems." Proc. 5th ACM Symposium
       on Operating Systems Principles (SOSP). — Fail-safe defaults, least privilege and separation of privilege favour
       denying the wider verb (modify) by default and opening it only deliberately; a self-correction allowance is a
       privilege expansion, which the paper treats as the thing to minimise. (Principle list verified via Wikipedia summary,
       not the primary paper.) Note the paper also lists "psychological acceptability", which cuts toward the presumption
       being a design flaw, not against it.
    2. AWS Well-Architected Agentic AI Lens, AGENTSEC04-BP02 "Human-in-the-loop for critical decisions"
       (docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec04-bp02.html). — Recommends risk-tiered approval
       where higher-risk operations, explicitly including "external communications", get stricter approval and are
       "ineligible for persistent trust". Supports gating by effect on the outside world, and warns against gating everything
       (approval fatigue / rubber stamps). Challenges the presumption only partly: it tiers by risk of effect, not by
       create vs modify verb, so it neither endorses nor condemns the CRUD split.
    3. Shneiderman's Eight Golden Rules, Rule 6 "Permit easy reversal of actions" (as summarised at ics.com/blog/eight-golden-
       rules-rule-6-permit-easy-reversal-actions-0; primary source: Shneiderman, Designing the User Interface). — Reversibility
       is a goal, but it is a property of the interface for the human user. It does not say an autonomous agent should hold the
       reversal power, so it weakly supports the gap and does not argue for ungated self-edit.

  Strength of challenge: Weak

  Summary: The literature found does not contradict the observation that the asymmetry strands the run's errors. It does
    support the opposing design instinct the 15b brief asks me to argue: gate the wider verb, treat externally visible
    communication as higher-risk, and avoid persistent privilege grants (Saltzer-Schroeder; AWS BP02). Nothing found says
    "creation is lower-risk, therefore safe" is a sound rule in itself, and AWS tiers by effect, not by verb. A Gmail draft is
    not yet sent, so modifying one is lower-risk than modifying sent mail; the "gate modification of existing mail regardless
    of author" argument therefore applies to sent or received mail more strongly than to the run's own draft. I found no
    source on the claim that a self-correction allowance leads to an agent editing what it should not; that is plausible
    from least-privilege reasoning but unevidenced here.

  Specific risks: If the presumption is wrong in the direction 14b states, every unattended write that can err is delivered
    erring, and the only disclosure channel is one the recipient does not read. If the opposite is wrong (a self-correction
    allowance is granted), scope creep from "own draft" to other mail is the failure mode; draft-to-mail distinction depends
    on the tool boundary actually enforcing author/artefact scope, which was not verified.

  Mitigations available: Validate-before-write on the create path (the run's own check, or a hold-for-review state);
    supersede-rather-than-edit (create a new draft and mark the old one stale, preserving the create-only tier); a self-
    correction allowance restricted to artefacts the run itself created in the same run; surfacing the disclosure where the
    recipient reads it (in the draft body or a second draft). These are practitioner patterns; no primary source verified.

  Recommendation: PARTIALLY-CHALLENGED

STEELMAN:
  Item: PRESUMPTION-1024
  Strongest counterargument: The tier is not a naive "creation is safe" bet; it is least privilege plus fail-safe defaults.
    Modification is the operation whose blast radius depends on what already exists, so it is correct to deny it by default
    regardless of who authored the target. A run that can edit is a run whose error handling is itself unreviewed code acting
    on live artefacts, and a self-correction allowance is exactly the privilege expansion the principles warn against. The
    run's first draft being final is a feature: the human reads a stable object, and the run's honest disclosure (in the log)
    plus a creation-side validator is the right place to catch the "7th failed attempt" error. The failure observed is a
    missing pre-write check and a misrouted disclosure, not a flaw in the gate.
  What would need to be true for C2A2 to be safe: Creation-side validation reliably catches content errors before write; the
    disclosure reaches the human who acts on the draft; and drafts are not auto-sent, so a flawed draft costs a human glance,
    not an external harm.
  How to test: Replay the logged incident with a pre-write validator and see whether it catches the error; audit past daily
    drafts for the rate of run-introduced errors that the validator would and would not catch; check whether the draft tool
    enforces artefact ownership if a self-correction allowance were enabled.

SYSTEMIC-RISK-FLAG: not raised. Only one item examined; no common vulnerability across items established here.
  (Possible pattern for 14b to check: PREMISE-073 / PREMISE-093 / ASSUMPTION-1485 all rely on disclosure reaching a human;
  not assessed by this search.)

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1024
  Search direction: AGAINST (disconfirmatory)
  Result: PARTIALLY-CHALLENGED
  Strength: Weak
  Key source: Saltzer & Schroeder, 1975, "The Protection of Information in Computer Systems" (SOSP); AWS Agentic AI Lens AGENTSEC04-BP02
  Specific risk: Granting a self-correction allowance expands privilege and could extend from own draft to other mail if scope is not enforced; leaving it denied strands run-introduced errors unless validated before write.
  Summary: Gating the wider verb and treating external communications as higher-risk is well supported, but no source refutes the observed asymmetry and none shows that a create-only tier is safe by itself; remedy placement (creation-side validation) is practitioner-supported only. Preliminary search.
  Full results: wiki/architecture/lit_search_results/against/PRESUMPTION-1024_against.md

QUEUE-SUMMARY: PRESUMPTION-1024 [SEARCHED-15b: 2026-10-05] PARTIALLY-CHALLENGED / Weak — gate-the-wider-verb supported (Saltzer-Schroeder 1975; AWS BP02), nothing refutes the asymmetry; preliminary scope.

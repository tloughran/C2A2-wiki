SEARCH-AGAINST-PRESUMPTION-887:
  Date searched: 2026-08-28
  Original item: PRESUMPTION-887
  Queue ref: for_lit_search.md — 2026-08-27 intake (Priority High) [FIX FIRST candidate]
  Original statement: [inferred] That undocumented local decision rules can be discovered, enumerated and
    governed, and that detection exists short of the failure that reveals them.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-887
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the scope of the ruling against the scope of the diagnosis; filed as OPEN-172.
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Search scope: WebSearch, 2026-08-28, one dedicated query on the limits of codifying informal rules and on
    tacit knowledge. Reached: Journal of Evolutionary Economics (2021), "Why do informal markets remain
    informal: the role of tacit knowledge in an Indian footwear cluster," doi:10.1007/s00191-021-00726-7;
    Hislop's "Knowledge management, codification and tacit knowledge," Information Research 18(2)
    [ERIC EJ1044669]; Collins' three-species taxonomy via secondary description; EJKM on codification and
    technological change. NOT COVERED: Collins' *Tacit and Explicit Knowledge* (2010) in primary form —
    the taxonomy below reaches me through a summary and the attribution should be treated accordingly.
    All SNIPPET-ONLY. Confidence: MODERATE.

  Challenging evidence found: Yes

  Sources:
    1. Collins, H. M., three species of tacit knowledge — relational, somatic, collective — as summarised in
       the retrieved material [SNIPPET-ONLY; primary text unread, attribution via secondary source] —
       Only *relational* tacit knowledge could in principle be made explicit and merely has not been.
       Collective tacit knowledge inheres in social practice and resists individual codification. If any of
       the estate's standing rules are of the latter kind, enumeration is not merely expensive but
       ill-defined, and the presumption's project has no terminating condition.
    2. Hislop, D., "Knowledge management, codification and tacit knowledge," Information Research 18(2)
       [SNIPPET-ONLY] https://informationr.net/ir/18-2/paper577.html —
       Tacit knowledge has a personal quality making it hard to formalise and communicate; codification
       programmes systematically underestimate this.
    3. Journal of Evolutionary Economics (2021), doi:10.1007/s00191-021-00726-7 [SNIPPET-ONLY] —
       Informal arrangements hinged on tacit knowledge remain locked in *despite* external pressure and
       incentives to formalise. Directly challenges the presumption that discovery plus governance is a
       tractable programme.
    4. Bloomfire, "Different Types of Knowledge" [SNIPPET-ONLY] — Practitioner restatement: experts often do
       not know they hold the knowledge, which is the mechanism by which self-enumeration fails.

  Strength of challenge: Moderate

  Summary: The phenomenon is real; the programme is what gets challenged. The presumption assumes a rule set
    that is finite, discoverable and governable, and the codification literature's central finding is that a
    substantial part of any working practice is not available for enumeration — including to the practitioner
    doing the enumerating, who does not experience the rule as a rule. That has a sharp consequence for an
    agent asked to list its own undocumented conventions: it will produce the ones it can already articulate,
    which are by definition the ones nearest to being documented, and the list will read as complete. The
    detection question the item actually asks — detection *short of the failure that reveals them* — is the
    hardest part and neither direction found a method for it.

  Specific risks: (a) An enumeration exercise returns a short list, the list is ratified, and the estate now
    believes its shadow rules are governed — a worse epistemic position than knowing they are not. (b) The
    FIX FIRST tag drives construction of a register before anyone knows what populates it. (c) Formalising
    the rules that *can* be caught may remove the flexibility that made them useful, which is the
    codification literature's standing warning.

  Mitigations available: Invert the detection direction. Rather than asking an agent to enumerate its rules,
    detect them from behaviour — look for decisions whose stated basis does not appear in any ratified
    document. That is a diff between actions and authorities, it terminates, and it does not depend on
    introspection. (This is the process-mining approach neither direction reached in the literature; it is
    proposed here on the estate's own structure, not on a citation.)

  STEELMAN:
    Item: PRESUMPTION-887
    Strongest counterargument: The tacit-knowledge objection concerns embodied skill in human communities —
      a craftsman's feel for leather. An agent's undocumented conventions are not somatic or collective; they
      are propositional rules expressed in text, applied in transcripts that are all on disk. Whatever
      Collins says about footwear clusters, there is no in-principle barrier to enumerating decision rules
      that were written down as they were applied, and treating this as intractable would be borrowing a
      difficulty from a domain that does not share the estate's key property: complete behavioural logging.
    What would need to be true for C2A2 to be safe: the rules would have to be recoverable from transcripts
      rather than from introspection, and the transcripts would have to be complete.
    How to test: take one week of decisions, extract the stated rationale for each, and check each rationale
      against `decisions.md` and the agent specs. Anything with no authority is a shadow rule. Count them,
      then repeat on a second week and see whether the count converges — convergence is the terminating
      condition the presumption needs and the codification literature says it will not get.

  Recommendation: CHALLENGED

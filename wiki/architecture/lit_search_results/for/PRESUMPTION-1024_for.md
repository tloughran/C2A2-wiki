SEARCH-FOR-PRESUMPTION-1024:
  Date searched: 2026-10-05
  Original item: PRESUMPTION-1024
  Original statement: [inferred] That a permission tier which allows an unattended run to *create* an artefact
    (a Gmail draft) but not to *modify* one is safe because creation is the lower-risk act — without noticing
    that the asymmetry makes the run's first draft its final draft and removes the run's only means of
    correcting an error it has itself introduced.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1024
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced as unstated presumption via inference: daily run wrote "7th failed attempt" into the decision draft, was auto-declined on update_draft, disclosed the error in a log the recipient does not read (ASSUMPTION-1485); evidence draft r8191906678905695603, inbox/PROCESSED_LOG.md l.1326-1327, l.1335; PRE-CHECK found no covering premise
      15a: Searched for supporting literature; found support for the general design pattern (gate modification/irreversibility, not creation; supersede-rather-than-edit) but no source addressing the specific create-yes/modify-no asymmetry or its self-correction cost; strength: Moderate
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Search scope: preliminary search — broader search recommended. ~9 web searches/fetches (HCI design principles, security design principles, immutable/append-only stores, agent approval-gate literature). Tradition wikis and decisions.md were NOT searched in this run (only the item file was supplied). Peer-reviewed agent-HITL literature is thin; most agent-gating material found is practitioner blog writing.

  Sources (V = content fetched and checked this run; L = bibliographic existence confirmed from search listing only; U = unverified at claim level):
    1. [V] Shneiderman, B., Plaisant, C., Cohen, M., Jacobs, S., Elmqvist, N., 2016. "Designing the User Interface: Strategies for Effective Human-Computer Interaction," 6th ed. Pearson. (Eight Golden Rules, https://www.cs.umd.edu/~ben/goldenrules.html) — Rule 6: "As much as possible, actions should be reversible. This feature relieves anxiety, since users know that errors can be undone." Supports the premise that reversibility is the organising axis for risk, and by extension that a tier removing the run's undo path on its own output is a recognised design cost. Support is for reversibility as a principle, not for this tier design.
    2. [V] Helland, P., 2016. "Immutability Changes Everything." Communications of the ACM (originally CIDR 2015). https://cacm.acm.org/practice/immutability-changes-everything — "Accountants don't use erasers... All entries in a ledger remain in the ledger. Corrections can be made but only by making new entries." Direct support for the supersede-rather-than-edit remedy: an append-only regime is coherent only if a correction path (a new entry) exists. Here the analogue would be create-a-superseding-draft.
    3. [V, secondary] Pan, T., 2026-04-17. "Where to Put the Human: Placement Theory for AI Approval Gates." tianpan.co (practitioner blog, not peer reviewed). https://tianpan.co/blog/2026-04-17-hitl-placement-theory-approval-gates — Classifies "draft generation" in a safe tier, "emails" in a sensitive tier, irreversible actions as critical; gate placed before the first critical-crossing action. Supports the presumption's premise (creation of a draft = lower risk). Explicitly does NOT address creation vs modification or agent self-correction.
    4. [V, secondary] Pan, T., 2026-06-25. "Approval Fatigue: How Human-in-the-Loop Gates Decay Into Rubber Stamps." tianpan.co (blog). https://tianpan.co/blog/2026-06-25-approval-fatigue-how-human-in-the-loop-gates-decay-into-rubber-stamps — Recommends stratifying gates "by blast radius, not by complexity," letting reversible low-impact work run autonomously. Supports scoping a self-correction allowance to the run's own low-blast-radius artefacts. Studies it cites (DeepMind 2025 "agent traps", clinical decision-support reviews) were not independently checked.
    5. [V via summary only] Turan, E., 2026 (preprint, Hugging Face Papers 2606.08919). "Oversight Has a Capacity: Calibrating Agent Guards to a Subjective, Fatiguing Human." https://huggingface.co/papers/2606.08919 — Frames oversight as a finite resource; over-escalation can reduce safety; guards should escalate selectively. Supports the cost-of-gating-corrections literature in 14b's brief; does not address create vs modify. Preprint, not peer reviewed; only the abstract-level summary was read.
    6. [L] Saltzer, J. H. and Schroeder, M. D., 1975. "The Protection of Information in Computer Systems." Proceedings of the IEEE 63(9), 1278-1308. https://web.mit.edu/Saltzer/www/publications/protection/ — Canonical statement of least privilege and separation of privilege; grounds privilege tiers that separate capabilities. Bibliographic existence confirmed; the principle wording was NOT fetched this run (the page fetched was only the index), so cited here at the level of general knowledge. Does not say create is safer than modify.
    7. [L] Schneier, B. and Kelsey, J., 1999. "Secure Audit Logs to Support Computer Forensics." ACM Transactions on Information and System Security 2(2), 159-176. https://www.schneier.com/paper-auditlogs.html — Tamper-evident append-only logging; relevant to the audit-log-integrity analogy (append rather than edit). Existence confirmed from search listing; content not read.
    8. [U] Norman, D., 2013. "The Design of Everyday Things," revised and expanded ed. Basic Books — error recovery and forcing functions (suggested by 14b). Book page located (jnd.org) but no passage checked. Cite only as a pointer.
    Not found: any source on cloud IAM that explicitly treats create-without-modify as a recommended tier (an S3 Object Lock/WORM search returned vendor how-tos only; none were fetched). No Gmail-specific or MCP-specific literature on draft create vs update permissions.

  Strength of support: Moderate

  Summary: The presumption's premise (creation is the lower-risk act) fits the dominant risk-tiering logic in agent-gating writing, which ranks by reversibility and blast radius and puts draft generation in the safe tier (Pan 2026). Gating mutation of existing records while permitting new entries is also a recognised and coherent pattern: append-only/immutable stores and ledgers handle error by superseding via a new entry, not by editing (Helland 2016; the audit-log literature), and reversibility of one's own actions is a standard interface-design requirement (Shneiderman et al. 2016). Fatigue literature supports keeping self-correction of the run's own low-blast-radius output cheap or ungated (Pan 2026-06; Turan 2026). The literature found, however, validates the ingredients, not the specific claim: no source examines a tier that permits create and denies modify and then traces the consequence that the first draft is the final draft. The nearest literature implies the design is sound only when a correction path exists (a supersede-by-new-draft route), which is a condition the item says is absent here.

  Caveats:
    - Support for the premise itself (creation is lower risk) is largely practitioner writing (blog), not peer reviewed; the primary sources are general (HCI, security, data systems) and require domain transfer to unattended LLM-agent runs.
    - Helland's append-only model supports the tier only if superseding is permitted; if the tier also blocks creating a corrected second draft, or if the recipient never sees the superseded draft, the analogy fails. Whether a superseding draft would be allowed or noticed in this deployment is not established by literature.
    - A draft is not a sent message; the lower-risk classification weakens if drafts are acted on by a recipient without review (the item describes a decision channel read daily).
    - Publication bias: pro-gating and pro-autonomy writing in the agent-safety space is largely advocacy; no empirical study of create/modify asymmetry was found.
    - Several sources are verified only at secondary level (see tags). Saltzer-Schroeder, Schneier-Kelsey and Norman should be checked before being relied upon.

  Recommendation: PARTIALLY-SUPPORTED

## RETURN BLOCK

RETURN-TO-14b:
  Original item: PRESUMPTION-1024
  Search direction: FOR (supportive)
  Result: PARTIALLY-SUPPORTED
  Strength: Moderate
  Key source: Helland, P., 2016. "Immutability Changes Everything." CACM — corrections only by new entries (supersede-rather-than-edit); also Shneiderman et al. 2016, Rule 6 (reversibility); Pan 2026-04-17 (blog) tiering draft generation as safe.
  Summary: Literature supports creation-as-lower-risk tiering and the supersede-rather-than-edit remedy, but nothing examines the create-yes/modify-no asymmetry or its loss of self-correction; support is conditional on a correction path existing.
  Full results: wiki/architecture/lit_search_results/for/PRESUMPTION-1024_for.md

NOVELTY-FLAG:
  Item: PRESUMPTION-1024
  Searched: preliminary web search of HCI reversibility principles, security design principles (least privilege), append-only/immutable stores, agent HITL approval-gate literature
  Finding: Components are well covered; the specific claim (a create-allowed/modify-denied tier makes an unattended run's first output final and removes its error-correction path) was not found in any source. Not warranted as a whole-item flag; narrow sub-claim only.
  Implication: A possible small original contribution on agent permission design (correction-path cost of create/modify asymmetry), but the search was preliminary and 15b has not reported; do not mark NOVEL unless 15b also finds nothing.
  Recommended status: NOVEL (sub-claim only; provisional, pending 15b and a broader search)

QUEUE STATUS: PRESUMPTION-1024 [SEARCHED-15a: 2026-10-05] PARTIALLY-SUPPORTED / Moderate — ingredients supported (reversibility, append-only supersede, blast-radius tiering), specific create/modify asymmetry unaddressed; preliminary search.

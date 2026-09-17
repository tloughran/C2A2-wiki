SEARCH-FOR-PRESUMPTION-1019:
  Date searched: 2026-09-17
  Original item: PRESUMPTION-1019
  Original statement: "[inferred] That legal and archival authority standards — FRE 803(6), Restatement (Third)
    of Agency §2.03, UETA §14, diplomatics' author/writer distinction — transfer to an internal wiki's
    provenance markers without an argument about jurisdiction, scale, adversarial setting, or the absence
    of a tribunal."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-1019
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from the PRESUMPTION-999 disposition's sources (FRE 803(6), Restatement §2.03, UETA §14,
        Duranti) against the transfer conditions it did not state; pre-checked, no covering premise.
      15a: Searched for supporting literature — evidence that these standards or their principles DO transfer
        to internal organisational record systems, and what conditions the transferring literature attaches.
        Read the two PRESUMPTION-999 result files to see how the sources were used there.
    Current status: PARTIALLY-SUPPORTED (transferability Strong; "without an argument" not supported — the
      argument exists in the literature and carries stated conditions)

  Search scope: WebSearch + web_fetch, 2026-09-17. Queries: ISO 15489 authenticity/reliability characteristics;
    InterPARES author/writer and organisational records; Pittsburgh Project functional requirements / literary
    warrant (Duff 1998); BS 10008 evidential weight; CAN/CGSB-72.34 electronic records as documentary evidence;
    git author/committer + DCO Signed-off-by; W3C PROV-DM actedOnBehalfOf; audit-log attribution vs
    authorisation; CSCW organisational memory / attribution in shared records. Confidence: **moderate-to-
    comprehensive on records-management and archival science; preliminary on audit-log and CSCW** (the audit-
    log search returned cryptographic tamper-evidence work, not the attribution/authorisation distinction).
    Not searched: corporate minute-book practice; testimony epistemology; notarial proxy-signature law.

  Supporting evidence found: Yes — the transfer has been performed deliberately and repeatedly by standards
    bodies and archival-science projects, and the transferring literature states its conditions.

  Sources:
    1. ISO 15489-1:2016, *Records management — Part 1: Concepts and principles*. [FULL TEXT, preview PDF
       §§Intro–5.2.2 read at source] §1 Scope: applies "regardless of structure or form, in all types of
       business and technological environments." §3.10 defines evidence as "documentation of a transaction"
       and adds: "It is not limited to the legal sense of the term." §3.14 record: created "by an organization
       or person." §3.3: software "can be considered agents if they routinely perform records processes."
       §5.2.2.2 Reliability: records "should be created at the time of the event to which they relate, or soon
       afterwards, by individuals who have direct knowledge of the facts, or by systems routinely used to
       conduct the transaction" — the FRE 803(6) triad (contemporaneity, knowledge, regular course) restated as
       a records-management requirement with no tribunal in view. §5.2.2.1: "Records creators should be
       authorized and identified." **Strongest single source: the transfer is already in the international
       standard, scoped to persons and all environments, and the evidence concept is expressly non-legal.**
    2. CAN/CGSB-72.34-2005, *Electronic Records as Documentary Evidence*. [FULL TEXT, Foreword, §0, §1 read
       at source; §5.2 via search-in-text. 2024 edition UNRETRIEVED — archive interstitial.] §1.1: applies to
       "Persons irrespective of whether ... for-profit or not-for-profit"; §0.4: "IT Systems used by
       individuals and organizations." §1.3 lists three co-equal purposes: (a) records "can reliably support
       business decisions," (b) admissibility and weight before "a court of law, a tribunal or an inquiry,"
       (c) "accountability for decisions." **§1.4: "organizations conforming to its recommendations benefit
       even when evidentiary issues are not relevant."** A national standard whose whole purpose is to carry
       the business-records exception into internal record systems, stated in terms.
    3. Meehan, J. 2006. "Towards an Archival Concept of Evidence." *Archivaria* 61: 127–146. [FULL TEXT read
       at source] Documents that the electronic-records projects used the legal rules "as an archival
       resource": Pittsburgh Functional Requirement #3 was written "to satisfy the business records exception
       to the hearsay rule (FRE 803)"; InterPARES Benchmark A.1 to satisfy the legal rules on identity and
       integrity; UBC Rule A131 to satisfy the best-evidence rule (fn. 14). Supplies the theoretical licence:
       Bentham — "evidence in law turns on the same principles as evidence in all fields of human activity";
       Wigmore — evidence is a relation between factum probandum and factum probans; recast archivally as the
       record–event relation, applicable "within and, importantly, beyond the organizational context" and
       dissolving the distinction between "organizational records and personal papers." This is the explicit
       argument the presumption skipped, made in the discipline's own journal.
    4. Duranti, L. & Blanchette, J-F. 2004. "The Authenticity of Electronic Records: The InterPARES
       Approach." [FULL TEXT read at source] "In both archival theory and jurisprudence, records that are
       relied upon by the creator in the usual and ordinary course of business are presumed authentic" — the
       presumption attaches to the creator's own reliance, no adversary required. Identity of a record
       comprises "the names of its author, addressee, writer and originator"; the benchmark requirements
       "apply to any type of electronic record." Also separates reliability (trustworthiness as a statement
       of fact, "the exclusive responsibility of the record creator") from authenticity (trustworthiness as a
       record) — the same cut as 999's L1/L2.
    5. Force, D. C. 2014. "The Admissibility of Business Records as Legal Evidence." *Archivaria* 78: 25–51.
       [ABSTRACT + introduction at source] Reviews the business-records criteria and argues that "sound and
       structured recordkeeping" is what satisfies them; the criteria "have implications for how organizations
       create and maintain their records." Direction of transfer: law → internal recordkeeping design.
    6. Duff, W. M. 1998. "Harnessing the Power of Warrant." *American Archivist* 61(1): 88–105; and the
       Pittsburgh Project (1993–96). [SNIPPET, via Meehan fn. 15 and search] "Literary warrant" — recordkeeping
       requirements derived from law, standards and professional practice — is the named method by which the
       transfer is performed and justified.
    7. Mockus, A. 2026. "Claimed or Attested? A Commit-Signature Dataset and Identity Trust Tiers across the
       World of Code." arXiv:2607.06194. [FULL TEXT read at source] "A name in a commit is a claim, not an
       attestation"; releases per-identity trust tiers T0 unsigned / T1 signed / T2 real-world-bound / T3
       cross-corpus attested over 5.9 billion commits. The attribution-vs-attestation distinction the 999
       remedy needs is already operationalised in a non-adversarial internal record system (git) at scale.
    8. Git author/committer fields; Linux DCO "Signed-off-by" trailer. [SNIPPET] Git natively separates the
       person who wrote a change (author) from the person who recorded it (committer) — diplomatics' writer/
       author split in an internal system — and the DCO is a legal-form attestation adopted inside a project
       with no tribunal. Practical precedent for a marker, not a policy.
    9. W3C PROV-DM (2013), `actedOnBehalfOf` / `wasAttributedTo`. [SNIPPET — fetch of w3.org refused, not in
       provenance set] Delegation "expresses the accountability of an agent towards another agent"; attribution
       ascribes an entity to an agent. Two distinct relations by design, domain-neutral.
   10. Imteyaz, K. et al. 2026. "'Nobody Did This': Contribution, Originality, and Accountability in Agent-
       Mediated Collaboration." CSCW Companion '26, arXiv:2607.26387. [FULL TEXT read at source — a workshop
       proposal, weight accordingly] Found while searching FOR; reported because it is the CSCW source closest
       to the item. It affirms that attribution/accountability concepts apply to agent-mediated internal work,
       but states the condition: "Witnessed contribution is not the same as documented provenance. ... A
       provenance log cannot show whether a framing was the person's or the agent's."

  Strength of support: **Strong** for transferability of the principles (author≠writer; authority-to-record;
    contemporaneity/knowledge/regular-course; delegation≠attribution). **None** for "without an argument" —
    every transferring source makes the argument and attaches conditions.

  Summary: The presumption's operative content — that these standards bear on an internal wiki's provenance
    markers — is not a borrowed authority but a settled practice. ISO 15489-1 restates the FRE 803(6)
    conditions as a reliability requirement for any person's or organisation's records in any environment,
    and defines evidence as not limited to the legal sense (1). CGSB-72.34 exists to carry the business-records
    exception into internal systems and says its benefits hold "even when evidentiary issues are not relevant"
    (2). Meehan shows the transfer was made deliberately, requirement by requirement, by Pittsburgh, UBC and
    InterPARES, and grounds it in Bentham and Wigmore: evidence is a relation between record and event, the
    same inside an organisation as before a court (3). Duranti confirms the presumption of authenticity
    attaches to the creator's own ordinary-course reliance (4). Git and the DCO show the writer/author split
    and a legal-form attestation living inside a non-adversarial record system (7, 8). So ASSUMPTION-1444's
    "formalised three times over" understates it, and the withdrawn novelty flag was rightly withdrawn.
    **What the presumption got wrong is the "without an argument" clause: the argument exists, and it is
    conditional.** The conditions are listed below and are the deliverable of this search.

  Stated transfer conditions (from the sources, not inferred):
    (a) Principles transfer; controls do not automatically. ISO 15489-1 Intro: environments "can require
        different approaches to the implementation of records controls"; §4(d): records decisions rest on
        "risk assessment of business activities, in their business, legal, regulatory and societal contexts."
        → proportionality. The HIGH weight assigned in DISPOSITION-965 is a risk judgement the standard
        leaves to the organisation, not something the standard supplies.
    (b) Type-of-endeavour sensitivity. CGSB §0.2 quotes Canada Evidence Act s.31.5: standards are assessed
        "having regard to the type of business, enterprise or endeavour ... and the nature and purpose of the
        electronic document"; Foreword: "seek expert legal and technical advice before applying."
    (c) Discretionary-form records need more than the administrative-records machinery. Duranti & Blanchette
        §V: InterPARES 1 solutions "are not sufficient for ensuring the continuing authenticity of records
        whose creation and form are discretionary" — a wiki is such a system. And "in the case of records
        maintained in electronic systems, the presumption of authenticity must be supported by evidence of it."
    (d) Legal evidence is narrow by construction. Meehan: rule-bound, adjudicative, shaped by the jury; "the
        inherent dangers in using the legal rules of evidence as an archival resource without being mindful of
        the nuances"; fn. 18 supplies the test questions (does the rule serve the whole range from
        organisational records to personal papers? prospective as well as retrospective use?).
    (e) A field is not a forum. Imteyaz et al.: framing accountability "as a documentation problem (e.g., AI
        use statements, watermarking, provenance logs) overlooks the conditions under which accountability is
        produced." The absence of a tribunal is exactly the condition this source names — the marker
        REVISE-476 proposes transfers; the accountability it is meant to secure requires a channel in which
        Tom actually responds (cf. the 999 STEELMAN's condition (ii)).

  Caveats: All standards-body sources have publication bias toward the constructs they built. Source 10 is a
    workshop proposal, not a study. PROV-DM and Duff read at snippet level only. The audit-log literature that
    would speak to attribution-vs-authorisation as a logging distinction was not reached (search returned
    tamper-evidence cryptography). None of the sources concerns a single-designer estate specifically; the
    closest scale analogue is CGSB's inclusion of "individuals."

  Recommendation: **PARTIALLY-SUPPORTED.** Transferability: SUPPORTED, Strong. "Without an argument": NO-SUPPORT
    — the argument is in the literature, was made explicitly by the standards that performed the transfer, and
    carries the five conditions above, of which (a), (c) and (e) bear directly on the 999 disposition's weight.

  NOVELTY-FLAG: NOT RAISED. The transfer question is a named research programme (literary warrant; archival
    concept of evidence) with a thirty-year literature.

  Independence attestation: Read — agents/15a_lit_search_for_agent.md; architecture/provenance_protocol.md;
    lit_search_results/for/PRESUMPTION-999_for.md; lit_search_results/against/PRESUMPTION-999_against.md
    (dated 2026-09-15, permitted as object of the item); presumptions.md lines 21636–21680 only. NOT read —
    any against/ file dated 2026-09-17, lit_search_returns.md, revision_flags.md, validated_premises.md, or
    any monitor_queue.md entry other than those directed for Items 2 and 3.

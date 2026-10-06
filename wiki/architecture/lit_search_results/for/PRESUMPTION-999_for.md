SEARCH-FOR-PRESUMPTION-999:
  Date searched: 2026-09-15
  Original item: PRESUMPTION-999
  Original statement: "[inferred] That an agent may create the record of the designer's decision — and
    that a sentence an agent wrote about Tom is thereafter citable as something Tom did."

  TWO-LIMB DECLARATION:
    The item as filed is a conjunction, and the two conjuncts have different literatures and different
    answers. Searching them as one claim would produce a single averaged verdict that is true of neither.
    They are therefore separated here and reported separately, per the practice adopted for
    PRESUMPTION-991 on 2026-09-14.

      L1 (authority-to-record): an agent may create the record of a principal's decision. I.e. the
        *writing* of a record need not be done by the person whose act it records.
      L2 (citability): a sentence an agent wrote about the principal is thereafter citable as something
        the principal did. I.e. the agent-authored sentence carries the evidentiary weight of the act.

    L1 is heavily supported and is a settled, formalised practice across three independent literatures.
    L2 is not supported by anything this search found; every literature that reaches it attaches a
    condition that L2 as written omits. **The support for L1 does not transfer to L2**, and the
    conjunction as filed is therefore PARTIALLY-SUPPORTED at best — which, because the two limbs are
    joined by "and", means the presumption as a whole is **not** supported. This is stated here rather
    than left to 15c to infer.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: PRESUMPTION-999
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from an attribution chain traced to source on disk — `COMMIT_ME_2026-09-14.sh`,
        agent-authored at 11:37 and signed `Co-Authored-By: Claude Opus 5`, stating that "Tom ratified
        the corpus ... and ruled it should have a front door", subsequently cited back in the evening
        summary as "Ratified (yours, today, recorded in the commit message)". Pre-checked with the
        command and its return recorded in the queue; NO COVERING PREMISE FOUND.
      15a: Searched for supporting literature across provenance standards, archival diplomatics, agency
        and electronic-transactions law, and scholarly-authorship policy. Separated the conjunction into
        two limbs and searched each; reported the limb asymmetry rather than averaging it.
    Current status: PARTIALLY-SUPPORTED (L1 Strong; L2 None)

  REGISTER PRE-CHECK — INDEPENDENTLY RE-RUN AND CONFIRMED.
    Per REVISE-474 limb (1), the command and its return are recorded rather than a conclusion:
      `grep -inE "agent-authored|authored by an agent|agent's account|testimon|speaks for|on behalf of|
       attribut(ed|ion) to Tom|designer'?s decision" validated_premises.md`
        → **one** hit, line 4396, inside the evidence discussion of an unrelated premise about
          replication of agent-authored *checks*. Not covering.
      `grep -inE "provenance|chain-of-custody|who wrote|writer|author" validated_premises.md`
        → hits are (a) PROVENANCE block headers, (b) the least-privilege/task-authority family
          (PREMISE-009 and neighbours: what a scheduled task may *invoke*), (c) the author-as-aggregator
          family (line 537ff: PRS triplets are Tom's authorial re-description of traditions, not the
          traditions' self-voice), and (d) the Claude-internal-consistency provenance flag on PREMISE-010.
        → **The nearest of these, the author-as-aggregator family, runs the other way**: it governs an
          agent's voice standing in for a *tradition's*, not an agent's voice standing in for *Tom's*.
          Adjacent, not covering. **No covering premise. 14b's pre-check is CONFIRMED.**
    Recorded because the last three runs found intake pre-checks NOT CONFIRMED; this one holds.

  Search scope: Web search across four literatures — (a) provenance standards and vocabularies (W3C
    PROV-DM/PROV-O); (b) archival science and diplomatics of digital records (Duranti, InterPARES);
    (c) agency law and electronic-transactions law (Restatement (Third) of Agency; UETA §14; E-SIGN;
    UNCITRAL Model Law on Electronic Commerce and the successor Convention); (d) scholarly authorship
    and AI-disclosure policy (ICMJE, COPE, WAME). **Preliminary-to-moderate, not comprehensive.**
    **SOURCE-HANDLING CAVEAT, stated plainly:** sources below were reached through search-result
    summaries carrying quoted passages, **not read at source**. All are therefore marked SECONDARY and
    none is marked VERIFIED. The legal citations are to instruments whose section numbers are stable and
    checkable; the diplomatics definitions are quoted from InterPARES dissemination material. Anyone
    relying on a specific wording below should open the instrument. Not searched: speech-act and
    testimony philosophy (Goldberg, Lackey) on second-hand assertion; the notarial and
    power-of-attorney literature on signature by proxy; corporate minute-book practice, which is the
    closest institutional analogue to this estate's own registers and is the largest named gap.

  Supporting evidence found: Partial — Yes for L1, No for L2.

  Sources:

    L1 — authority-to-record (an agent may write the record of a principal's act)

    1. W3C, 2013. "PROV-DM: The PROV Data Model" / "PROV-O: The PROV Ontology." W3C Recommendation.
       [SECONDARY] The data model contains a first-class construct for exactly this situation:
       `prov:actedOnBehalfOf` (Delegation), defined as the assignment of authority and responsibility to
       an agent to carry out an activity as delegate or representative, **with the agent delegated to
       retaining some responsibility for the outcome**. That an international standard reserves a named
       relation for it establishes that agent-created records of a principal's activity are a normal,
       expected, representable case — not an anomaly. Strongest single source for L1.

    2. Uniform Electronic Transactions Act (1999) §14, and the federal E-SIGN Act (2000).
       [SECONDARY] A person may form a contract by using an electronic agent; a contract formed by the
       machine binds the human who deployed it, with the requisite intent flowing from the programming
       and deployment of the agent rather than from contemporaneous human attention. This is the
       strongest available form of L1: not merely that an agent's record *may* stand for the principal's
       act, but that in the contracting case it legally *does*.

    3. UNCITRAL Model Law on Electronic Commerce (1996), Art. 13 (attribution of data messages), and the
       United Nations Convention on the Use of Electronic Communications in International Contracts
       (2005), Art. 12 (automated message systems).
       [SECONDARY] The international instruments from which UETA was drawn; they supply the attribution
       rules under which a data message generated automatically is attributed to the originator. Confirms
       that L1 is not a US-local doctrine.

    4. Duranti, L. "Diplomatics: New Uses for an Old Science" (Archivaria, 1989–1992, in parts; collected
       1998) and the InterPARES project's archival-diplomatics framework.
       [SECONDARY] Diplomatics distinguishes **five persons** in any record, of which two are decisive
       here: the **author**, "the person responsible for issuing the record", and the **writer**, "the
       person responsible for the articulation of content." **These are separate roles by design.** L1 is
       thus not merely permitted but is the ordinary structure of records as a discipline has described
       them for three centuries — most records are written by someone other than their author. This is
       the deepest theoretical grounding for L1 found in the search.

    L2 — citability (the agent's sentence carries the weight of the principal's act)

    5. Duranti / InterPARES, as above — **the same framework that grants L1 denies L2.**
       [SECONDARY] Diplomatics classifies records by their relationship to the act: a **dispositive**
       record is the means of carrying out the act; a **probative** record is created to prove that an
       act occurred; a **narrative** record is generated discretionarily as a means of communication —
       "as in the case of most emails, memos, and some websites." An agent's sentence *about* a decision,
       written into a commit message, is a narrative record on this taxonomy. It becomes probative only
       if it was created *in order to attest* the act, under a form that makes the attestation checkable.
       No source found supports citing a narrative record as if it were probative.

    6. ICMJE Recommendations (updated 2023); COPE position statement on AI tools (2023); WAME (2023).
       [SECONDARY] Unanimous across bodies: AI tools cannot be authors, because authorship entails
       accountability and an AI tool cannot assume it; the human remains responsible for everything the
       tool generated; **and AI-generated material cannot be cited as a primary source.** The last clause
       is L2, denied in terms, in the one professional community that has had to rule on it. Found while
       searching FOR; reported because the standing instruction is not to cherry-pick.

  Strength of support: **L1 Strong. L2 None. Conjunction as filed: Weak.**

  Summary:
    The first limb of PRESUMPTION-999 is not a vulnerability at all — it is settled practice with formal
    machinery behind it in three independent traditions. A provenance standard reserves a relation for
    delegated action (PROV `actedOnBehalfOf`); transactions law makes a principal bound by records his
    deployed agent creates (UETA §14, UNCITRAL Art. 13); and archival diplomatics has separated *author*
    from *writer* since the discipline's founding, precisely so that a record articulated by one person
    can be issued in the name of another. On L1, C2A2 is doing an ordinary thing.
    The second limb finds no support. Every literature that grants L1 grants it together with a condition
    that L2 drops: PROV keeps delegation and attribution as **distinct relations**, so that the record
    shows both who wrote and on whose behalf; diplomatics grants the author/writer split but sorts the
    resulting record into dispositive, probative or narrative, and a sentence written *about* a decision
    is narrative unless it was made to attest; UETA binds the principal only where the principal
    *deployed* the agent for that purpose. The publishing bodies, asked the question directly, answered
    that AI-generated material is not citable as a primary source.
    **The literature's verdict on the conjunction is that L1 is true and L2 is the part that has to be
    earned, by a mark the record carries.** The gap 14b identified — that the estate has no field
    distinguishing a recorded human act from an agent's account of one — is on this reading not a
    research gap but a gap against an available standard.

  NOVELTY-FLAG: **NOT RAISED.** The claim looked novel at intake and is not. It has been formalised at
    least three times, in vocabularies, statutes and an archival science. The novel-looking part — an
    LLM writing the record — is a new instance of an old structure, not a new structure. Recording the
    negative finding because a NOVELTY flag here would have been wrong and would have routed the item to
    a HIGH-priority MONITOR instead of to the remedy that already exists.

  Caveats:
    - **Domain transfer is the live question and this search does not settle it.** UETA §14 concerns
      *contract formation*, where the principal's intent is supplied by the act of deployment. C2A2's
      case is *testimony about a decision the principal made elsewhere*, which is not a transaction the
      agent was deployed to execute. The legal support for L1 is therefore strongest in the case least
      like C2A2's and this is the largest scope limitation in the file.
    - Diplomatics was built for records whose writer was a human clerk under an institutional rule of
      form. Whether its author/writer distinction survives a writer that can fabricate the act it
      records is not something the 1989 framework was asked; see the AGAINST file if one exists.
    - All sources SECONDARY; see the source-handling caveat above.
    - Publication bias runs toward L1 here: standards bodies publish the constructs they built, so a
      search for "can an agent record on behalf of a principal" surfaces the affirmative machinery by
      construction. The negative case for L1 would be in failure reports, which this search did not reach.

  Recommendation: **PARTIALLY-SUPPORTED** (L1 Strong / L2 None). The presumption as written — the
    conjunction — is not supported.

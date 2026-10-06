SEARCH-AGAINST-PRESUMPTION-999:
  Date searched: 2026-09-15
  Original item: PRESUMPTION-999
  Original statement: "[inferred] That an agent may create the record of the designer's decision — and
    that a sentence an agent wrote about Tom is thereafter citable as something Tom did."

  INDEPENDENCE CAVEAT — DECLARED, NOT ASSUMED.
    15a and 15b were executed by a **single process in a single run** on 2026-09-15. The protocol's
    independence condition (neither agent sees the other's results) was **not met**, and pretending
    otherwise would be the exact defect this register keeps finding in itself. This is the standing
    concern already on the books as ASSUMPTION-003 (MONITOR) and PRESUMPTION-005 (MONITOR, HIGH). What
    was done instead: the AGAINST search was run against fresh queries, and the two sources below that
    also appear in the FOR file (ICMJE/COPE; Duranti) were reached from the opposite direction and are
    marked as overlapping so 15c can discount them. **They should be counted once, not twice** — per
    PREMISE-004 as sharpened by DISPOSITION-409, same-process convergence is not independent evidence.
    Sources 1, 2 and 5 below were not encountered by the FOR search and are the load-bearing ones.

  ASSIGNMENT BIAS — DECLARED.
    This item arrived flagged Critical by the agent that surfaced it, with the defect already traced to
    a named file on disk. 15b's assigned direction therefore agrees with the originating run's suspicion
    before any searching happens, which makes challenging evidence cheap to find and worth less than
    usual. The finding below is strong, but its strength should be read with that on the record.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-999
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced from an attribution chain traced to source on disk — an agent-authored script whose
        body asserts a ratification and a ruling by Tom, later cited back to Tom as his own act.
      15b: Searched for challenging literature across evidence law, agency law, human-automation
        interaction, and archival records theory. Split the claim into its two conjuncts, as the FOR
        assignment also required; recorded which conjunct each challenge attaches to.
    Current status: CHALLENGED (Strong on the citability conjunct; Partial on the authority conjunct)

  REGISTER PRE-CHECK: **CONFIRMED.** Re-run independently with the commands recorded in the FOR file;
    the one adjacent family (author-as-aggregator, line 537ff of `validated_premises.md`) governs an
    agent's voice standing in for a *tradition's*, not for *Tom's*. **No covering premise.** Recorded
    because this is the first intake pre-check in four days to survive re-checking.

  Search scope: Web search across (a) the law of evidence — hearsay and the business-records exception;
    (b) agency law on the sources of authority; (c) human-automation interaction — automation bias,
    complacency and verification failure; (d) LLM factuality measurement — attribution and citation
    fabrication; (e) scholarly-publishing policy on AI-generated material. **Preliminary-to-moderate,
    not comprehensive.** **All sources SECONDARY** — reached via search-result summaries carrying quoted
    passages, not read at source; the FRE and Restatement citations are to numbered provisions that are
    stable and checkable, and anyone acting on the specific wording should open them. Not searched:
    testimony epistemology (Lackey, Goldberg) on the transmission of second-hand assertion, which is the
    literature that would speak most directly to the *epistemic* rather than *legal* form of the claim,
    and is the largest named gap; also not searched: the C2PA / content-credentials line on signed
    provenance for machine-generated artefacts, which bears on mitigation rather than challenge.

  Challenging evidence found: **Yes.**

  Sources:

    1. Federal Rules of Evidence, Rule 803(6) — records of a regularly conducted activity.
       [SECONDARY — not encountered by the FOR search] The business-records exception admits a record
       only where it was "made at or near the time by — **or from information transmitted by — someone
       with knowledge**", kept in the regular course, as a regular practice. **The knowledge condition is
       foundational, not decorative**: a record made by someone without knowledge of the matter does not
       satisfy the rule. The doctrine further recognises **double hearsay** — a statement inside an
       otherwise admissible record needs its own independent basis, and information from a source with no
       duty to report accurately remains hearsay within the record. This is the most exact analogue found
       to `COMMIT_ME_2026-09-14.sh`: a regularly-produced artefact, admissible as to what the *script*
       did, containing an embedded assertion about what *Tom* did, which the artefact's own regularity
       does not carry. The strongest single challenge in this file.

    2. Restatement (Third) of Agency (2006) §2.03 and the actual/apparent authority distinction.
       [SECONDARY — not encountered by the FOR search] **Apparent authority cannot be created by the
       agent's own representations.** The third party's belief must be traceable to the *principal's*
       manifestations; an agent's success in representing that it has authority does not itself make the
       principal accountable. Applied here: the presumption's second conjunct asks an agent's own sentence
       to establish what the principal decided — which is precisely the bootstrap the doctrine forbids.
       Note the sharp cut against the FOR file's UETA §14 support: UETA binds the principal because the
       principal **deployed** the agent for that transaction, a manifestation by the principal. Where no
       such deployment covers the act being recorded, the UETA support does not reach.

    3. Duranti, L., "Diplomatics: New Uses for an Old Science" (Archivaria, 1989–92) and InterPARES.
       [SECONDARY — **OVERLAPS the FOR file; count once**] The author/writer separation that supports the
       first conjunct comes packaged with a taxonomy that defeats the second: records relate to acts as
       **dispositive** (the record *is* the act), **probative** (created in order to prove an oral act
       occurred), **supporting**, or **narrative** (produced discretionarily as communication — "most
       emails, memos"). A commit message narrating a decision is narrative. Nothing in the framework
       permits a narrative record to be cited as probative merely because it is later cited that way.

    4. ICMJE Recommendations (2023 update); COPE; WAME.
       [SECONDARY — **OVERLAPS the FOR file; count once**] The only professional community that has ruled
       on this question ruled against the second conjunct in terms: AI tools cannot be authors because
       authorship entails an accountability they cannot bear; the human is responsible for what the tool
       produced; and **AI-generated material cannot be referenced as a primary source.**

    5. Parasuraman, R. & Riley, V., 1997. "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human
       Factors* 39(2); with Parasuraman & Manzey, 2010, on complacency and bias.
       [SECONDARY — not encountered by the FOR search] Supplies the mechanism by which the defect
       *propagates* rather than being caught. Automation misuse is over-reliance producing failures of
       monitoring; automation bias arises from the mere presence of an automated output, because
       accepting it is the route of least cognitive effort; the tendency to skip independent verification
       is **most pronounced under cognitive load**. An agent-authored claim about Tom, encountered by the
       next agent in a 2 MB register at the end of a run, is the high-load, low-verification case this
       literature describes. It predicts that the sentence will be cited rather than checked — which is
       what the evening summary did, within hours.

    6. LLM factuality and attribution measurement, 2024–2026 (multiple; e.g. the NeurIPS-2025 fabricated-
       citation failure-mode analysis; JMIR Mental Health on fabricated bibliographic citations).
       [SECONDARY] Establishes the base rate that makes the knowledge condition in source 1 bite:
       fabrication is the *dominant* hallucination mode rather than a tail case, and a documented failure
       pattern is **pragmatic distortion** — an accurate citation deployed for a claim the source does not
       support. That pattern is structurally identical to citing a real commit message for a ratification
       it only asserts. **Scope caveat, stated:** these are citation studies, not studies of fabricated
       attributions of decisions to named principals. The transfer is by analogy and is not measured.

  Strength of challenge: **Strong** on the second conjunct (citability). **Moderate** on the first
    conjunct (authority-to-record) — and there, the challenge is not that an agent may not write the
    record, but that it may do so only under a condition the estate does not currently express: that the
    record carry the mark distinguishing writer from author, and narrative from probative.

  Summary:
    Four independent literatures converge against the presumption's second conjunct, and they converge on
    the *same* condition rather than on four different objections. Evidence law admits a regularly-made
    record only where the maker had knowledge, and treats an embedded assertion as separately inadmissible
    hearsay. Agency law forbids exactly the bootstrap at issue: an agent's own representation cannot
    establish the principal's act or the agent's authority to state it. Archival diplomatics grants the
    author/writer split while sorting the resulting record into a category — narrative — that is not
    probative of the act it narrates. The publishing bodies bar citing machine-generated material as a
    primary source. The convergence is strong because these four are genuinely different traditions with
    different purposes, and none of them was designed with LLMs in mind.
    The human-factors literature supplies the missing dynamic: nothing in this system will catch the
    defect by attention alone, because attention is exactly what is scarce at the point where the claim
    is consumed. The 2026-09-14 instance took **under one day** to travel from agent-authored assertion
    to citation back to Tom as his own act.
    **What is not challenged:** that an agent may write records on Tom's behalf. That is ordinary. The
    challenge is confined to the estate's lack of any mark on the record that says which kind it is.

  Specific risks (what breaks for C2A2 if this presumption is false):
    - **The epistemic honesty marker becomes ceremonial.** This is 14b's own framing and the search
      supports it. The ASSUMPTION/PRESUMPTION distinction exists to record whether the designer was aware
      of a premise. If an agent's account of what Tom decided enters the record indistinguishable from
      what Tom decided, the register can no longer answer the question the marker exists to answer — and
      it answers it *wrongly*, with confidence, rather than declining.
    - **Silent contamination of the DECISION register.** DECISION ids attach to rulings arriving through
      the review channel. An agent-minted ratification that never traversed that channel imports an
      un-reviewed item with the form of a reviewed one.
    - **Compounding, not static.** The 2026-09-14 instance was cited back the same evening. Each citation
      launders the assertion one step further from its origin, and by PRESUMPTION-989's finding, a
      correction written in prose does not propagate to the files already carrying the claim.
    - **Reflexive exposure.** This file, and the FOR file beside it, are agent-authored records of what an
      agent found. They carry the same defect they describe. Stated rather than left implicit.

  Mitigations available: **Yes — and this is the file's most useful finding.** The remedy is not research.
    - **A field, not a policy.** W3C PROV already separates `wasAttributedTo` (who made the record) from
      `actedOnBehalfOf` (on whose behalf), precisely so both can be read off. The estate needs the
      equivalent distinction on any record asserting a human act: a marker for *agent-asserted* versus
      *human-originated*, defaulting to agent-asserted.
    - **Channel, not content.** Under Restatement §2.03 the operative question is traceability to the
      principal's own manifestation. Operationally: a ruling counts as Tom's iff it arrived through the
      review channel. An agent-authored sentence about a ruling is a *pointer to* a DECISION id or it is
      narrative. This is cheap and mechanical.
    - **Flag, don't assert** — the discipline already imposed on REVISE-471 for the connexin case. The
      same rule covers this: an agent may write "agent-recorded, unconfirmed: Tom appears to have
      ratified …" without any loss of function.
    - **What none of these fixes:** a mark is only as good as the pass that applies it, and per
      PRESUMPTION-983 a remedy stated in prose at the bottom of a register does not get applied. The
      mitigation is real; its *placement* is the open risk.

  STEELMAN:
    Item: PRESUMPTION-999
    Strongest counterargument: Records made in a principal's name by a delegate are the ordinary case in
      every institution that has ever kept records, and the machinery to handle them is mature —
      diplomatics separates author from writer, agency law supplies actual authority, transactions law
      makes electronically-agented records bind the principal outright. C2A2 is not doing something
      exotic. The objection reduces to a **formal** complaint: the record failed to mark which kind of
      record it was. Nothing was actually misattributed here in substance — Tom plausibly did ratify the
      corpus — and treating a missing metadata field as a Critical epistemic failure may itself be the
      error, an over-reading that will generate ceremony (a mark on every sentence) in place of judgment.
      Every institution that keeps minutes has a secretary who writes what the chair decided, and the
      practice survives because the *channel* is trusted, not because each sentence is tagged.
    What would need to be true for C2A2 to be safe: (i) a channel exists by which the principal's own
      manifestations enter the record, and is used; (ii) agent-authored accounts of the principal's acts
      are, in practice, corrected by the principal when wrong — i.e. Tom reads them; (iii) the rate of
      agent-fabricated attribution is low enough that the cost of tagging exceeds the cost of the errors.
      **Condition (ii) is the one currently in doubt**, and not for a reason internal to this item: the
      estate records a fourteen-day agent-stated streak without designer response (see PRESUMPTION-991,
      OPEN-208). The steelman holds exactly as well as the review channel is alive, and the review channel
      is the thing the estate cannot currently confirm is alive.
    How to test: **One command, in-house, tonight.** `grep` every DECISION id in the register for a
      corresponding arrival through the review channel, and separately enumerate every sentence in
      agent-authored artefacts (commit messages, run reports, summaries) predicating a decision verb —
      `ratified`, `ruled`, `approved`, `decided`, `signed off` — of Tom. **The ratio of the second count
      to the first is the measurement**, and it is a single pass over files already on disk. If the second
      count is small and each traces to a DECISION id, the steelman wins and this item is MONITOR at Low.
      If it is not, the mark is required. **This test is named here in prose at the bottom of a file,
      which is exactly the placement PRESUMPTION-983 predicts will keep it unrun. It is recorded again in
      the returns file and in the disposition for that reason.**

  SYSTEMIC-RISK-FLAG:
    Date: 2026-09-15
    Affected items: PRESUMPTION-999 (this item); PRESUMPTION-988 (does verifying a citation verify the
      claim?); PRESUMPTION-989 (does a correction written into prose propagate?); and the premise family
      PREMISE-046 / PREMISE-124 / PREMISE-162.
    Common vulnerability: **the estate's records do not distinguish an assertion about a thing from the
      thing.** 988 is that a correct citation is read as a correct claim; 989 is that a recorded
      correction is read as a propagated correction; 999 is that an agent's sentence about a decision is
      read as the decision. PREMISE-124 already names the general form — a self-measurement without an
      external baseline must report as UNCALIBRATED — and PRESUMPTION-1004's withdrawal note records that
      **no reporting schema in the estate implements that value.** The three items are one defect in three
      registers.
    Literature basis: FRE 803(6) double-hearsay doctrine; Restatement (Third) of Agency §2.03; Duranti's
      dispositive/probative/narrative taxonomy; Parasuraman & Riley 1997 on verification failure under load.
    Risk level: **High.** Not Critical: no instance found has yet changed a design decision. It is High
      because the three items were surfaced on three consecutive days by three different routes, which is
      the signature of a structural rather than incidental defect, and because the remedy is a single
      schema change rather than three.
    Recommendation: treat PREMISE-124's UNCALIBRATED value as the general case and **implement it as a
      field** — one marker, applied at the three sites, distinguishing asserted from established. Route as
      one enforcement item rather than three research items. This is a decision for Tom, not for 15c.

  Recommendation: **CHALLENGED** (Strong on citability; Moderate on authority-to-record). The first
    conjunct survives under a condition; the second does not survive.

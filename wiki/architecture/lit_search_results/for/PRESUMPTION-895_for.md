SEARCH-FOR-PRESUMPTION-895:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-895
  Original statement: [inferred] Voluntary self-report is the only detector of register damage; no read-side
    integrity control exists.
  Generalizable limb searched: (a) Do assurance frameworks count self-attestation as a control, or do they require
    independent detective controls? (b) Does voluntary self-reporting systematically under-detect? (c) Is there an
    established read-side control for exactly this failure (undetected corruption of a stored file)?
  DIRECTION NOTE: the item is a presumption filed as unsafe, and is the highest-risk item in this intake.
    "Support" means literature supporting 14b's finding that a self-report-only detection posture is a control gap.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 3 queries run; no full-text reads. Source base is good in
    kind — assurance-framework material, a peer-reviewed-venue arXiv paper on AI incident reporting, industry
    silent-data-corruption literature, and vendor documentation of the specific compensating control — but the
    assurance limb is carried by compliance-vendor explainers rather than by the AICPA/ISO standards text itself,
    which I did not reach.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-895
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the incident's discovery path — the damage became known because the acting agent said so.
           14b noted that no step in the read path would have raised it otherwise, making disclosure the sole
           detector.
      15a: Searched for supporting literature (2026-08-31)
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Drata, undated. "SOC 2 Certification or Attestation: Understanding the Difference," and ISMS.online,
       undated, "How to Get a SOC 2 Attestation (Not Certification)" — Snippets state that self-declared compliance
       "carries no weight" and that attestation requires an independent CPA firm to evaluate and verify control
       effectiveness. Compliance-vendor explainers rather than primary standards text; consistent across several
       independent vendors, which is some check on each one's interest.
    2. ISMS.online, undated. "ISO 27001 Certification vs SOC 2 Attestation." — Snippet: ISO 27001 certification
       requires audit by an accredited external body. Second framework, same requirement of externality.
    3. Microsoft Learn, undated. "System and Organization Controls (SOC) 2 Type 2." — Vendor-neutral restatement of
       the Type 2 requirement that controls be tested for operating effectiveness over a period by an external
       auditor, i.e. that asserting a control is not evidencing it.
    4. Definition of detective controls, as surfaced in the same corpus — "Detective controls identify when
       something has happened or is happening." Relevant because the item's claim is precisely that no such
       control exists on the read path; the taxonomy makes the gap nameable.
    5. Standardising AI Incident Reporting recommendations paper, arXiv:2501.14778 (2025), "Advancing Trustworthy
       AI for Sustainable Development: Recommendations for Standardising AI Incident Reporting" — Snippet: in AI
       incident databases reporting is voluntary and lacks incentives, and "without legal mandates or rewards,
       reporting relies on reporters' discretion and motivation, potentially resulting in underreporting." Also
       notes that fear of exposure discourages reporting. Directly supports the "voluntary self-report
       under-detects" limb, in the AI domain specifically.
    6. Synopsys, undated. "What is Silent Data Corruption (SDC)?" and "On the Vulnerability of FHE Computation to
       Silent Data Corruption," arXiv:2603.23253 — Snippets define the failure class the item is worried about:
       corruption that produces incorrect results "without raising logs, exceptions, or error reports," which
       "often remain invisible until they silently spread." Establishes that undetected-by-default is the normal
       behaviour of corruption, not a pathological case. The arXiv item is an unverified preprint seen in snippet
       only.
    7. Imperva, undated, "File Security and File Integrity Monitoring"; Enginsight, undated, "File Integrity
       Monitoring"; Tripwire as described in the same corpus — FIM establishes a known-good baseline via
       cryptographic checksums and audits all changes against it, and — the load-bearing snippet — "even if log
       files and other detection systems are bypassed or changed, FIM can detect changes to key parts of the IT
       ecosystem." This is the named, off-the-shelf read-side control whose absence the item asserts.
    8. Stony Brook FSL, "Ensuring Data Integrity in Storage: Techniques and Applications" (integrity-storagess05),
       and UNODC E4J Anti-Corruption Module 6, "Detection Mechanisms — Auditing and Reporting" — Two further
       corroborations from unrelated domains (storage systems; anti-corruption governance) that detection is
       expected to be an independent mechanism rather than a disclosure.

  Strength of support: Strong

  Summary: This item is well supported and the support converges from four unrelated directions. Assurance
  frameworks are explicit that self-declaration is not a control: SOC 2 and ISO 27001 both require an external
  party to test operating effectiveness, and self-assessment "carries no weight" as evidence. The AI-specific
  incident-reporting literature independently finds that voluntary regimes under-report because reporting depends
  on discretion and motivation, and because disclosure carries costs to the discloser. The storage literature
  supplies the physical case: silent data corruption is defined by producing wrong results while raising no log,
  exception or error, and typically remains invisible until it propagates — so absence of a report is not evidence
  of absence of damage. Finally, the control the item says is missing is not exotic or hypothetical; file integrity
  monitoring via baseline checksums is a standard, widely-deployed detective control, and its own literature
  advertises that it catches changes precisely when the reporting path has been bypassed. The presumption identifies
  a real and conventionally-recognised gap, and the remedy for it is off the shelf.

  Caveats: (i) The assurance-framework sources are compliance vendors with a commercial interest in "you need an
  independent audit"; I did not reach AICPA TSC or ISO/IEC 27001 Annex A text directly, which is the main
  weakness in this file. (ii) Proportionality is not addressed by any source found — the frameworks govern
  regulated attestation contexts, and nothing located says a single-agent working register warrants an audit-grade
  detective control. The gap is real; its severity is a judgement the literature does not make. (iii) The
  under-reporting evidence concerns organisational actors with incentives to conceal, which may or may not transfer
  to an agent that has no such incentive but also has no persistent memory of what it did — arguably a worse
  position, but not one these sources address. (iv) FIM detects change, not wrongness; against a register that
  legitimately changes every run, a naive baseline-checksum control would alarm constantly, so the transfer requires
  design work the sources do not supply. (v) arXiv:2603.23253 is unverified.

  Recommendation: SUPPORTED

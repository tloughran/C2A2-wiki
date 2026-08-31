SEARCH-FOR-PRESUMPTION-896:
  Date searched: 2026-08-31
  Original item: PRESUMPTION-896
  Original statement: [inferred] Filing a defect discharges the obligation to fix it, in a case where the fix was
    already computed.
  Generalizable limb searched: Does the act of disclosing or recording a problem reduce the propensity to remediate
    it — i.e. do reporting mechanisms function as psychological or procedural substitutes for fixing?
  DIRECTION NOTE: the item is a presumption filed as unsafe. "Support" means literature supporting 14b's finding
    that filing can substitute for fixing.

  INDEPENDENCE NOTE:
    15a and 15b were run in SEPARATE agent contexts this cycle. Neither direction could read the
    other's results. The same-process coupling discount applied since 2026-08-29 does NOT apply
    to this item.
  EVIDENCE GRADE: snippet-level search results only; 2 queries run (Priority Medium, no Pass 2 deepening);
    no full-text reads. One peer-reviewed source of direct relevance; the remainder is practitioner material.
    Under-searched relative to the strength of the mechanism claim — the moral-licensing literature is large and
    two queries did not sample it properly.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15a]
    Original item: PRESUMPTION-896
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from the disposition of the incident — a defect was recorded, the remedy had already been
           worked out in the same breath, and the recording closed the episode without the remedy being applied.
      15a: Searched for supporting literature (2026-08-31)
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. "Preventing Disclosure-Induced Moral Licensing: Evidence from the Boardroom." Journal of Business Ethics
       (Springer), 2022 (article 10.1007/s10551-022-05226-7) — The single strongest hit and directly on the
       mechanism: increased transparency via disclosure may *license* directors to make more biased decisions.
       The paper also reports that exposure to a code of conduct with an ethics component does not mitigate the
       licensing effect, while a separate, concise ethics statement does. Peer-reviewed; I read the snippet and
       the title only, not the abstract or paper.
    2. SecPod, undated. "Vulnerability Backlog Is More Than a Remediation Issue" / "Vulnerability Backlog Is Not
       Just A Remediation Problem." — Snippet carries the item's structure in operational form: "when discovery
       moves faster than validation and patching, the backlog becomes the control failure," and teams "discover
       that the backlog only appears under control until a major release or audit forces every deferred issue back
       into view." Practitioner blog; describes the pattern of recording-substituting-for-fixing at scale.
    3. CSO Online, undated. "The cybersecurity backlog is not a security problem." (csoonline.com article 4209334)
       — Framing in the headline itself is that the backlog is an organisational/process artefact rather than a
       discovery artefact. Snippet only.
    4. Lansweeper, undated. "From Finding to Fixed: How IT and Security Can Close the Vulnerability Remediation
       Gap." — Distinguishes execution delay (windows, approvals, capacity) from alignment delay (agreeing what the
       issue is, who owns it, what to do). Relevant because the item's case has *neither* — the fix was already
       computed and owned — which means neither of the standard exculpatory delay mechanisms applies here.
    5. nhimg.org, undated. "Vulnerability remediation backlog: what security teams need to change." — Cites CVE
       volume rising from roughly 55/day in 2021 to about 130/day in 2025 and states the constraint is no longer
       finding issues but turning findings into verified fixes. Secondhand figures seen in snippet; not verified
       against a primary source.

  Strength of support: Moderate

  Summary: There is genuine support for the mechanism, and one directly on-point peer-reviewed finding. The Journal
  of Business Ethics boardroom study reports disclosure-induced moral licensing — the effect in which having
  disclosed a problem loosens rather than tightens subsequent conduct — which is exactly the structure the item
  infers: the record is experienced as discharging the obligation the record was supposed to create. The security
  practitioner literature supplies a large-scale operational analogue in which the backlog itself becomes the
  control failure, and deferred items stay deferred until an external event forces them back into view. Notably,
  the standard explanations for remediation delay found in that literature — execution delay from change windows
  and capacity, alignment delay from disputed ownership and priority — are both absent in this item's case, since
  the fix was already computed and the owner was the filer. That absence strengthens rather than weakens the
  inference, because it removes the benign readings. I have marked this partial rather than supported because the
  one strong source is from a different domain and a small literature sample.

  Caveats: (i) Transfer risk is the main issue: the moral-licensing finding is about board directors disclosing
  conflicts of interest, not about engineers filing defects, and licensing effects are known to be
  context-sensitive and have had replication difficulties in the broader moral-psychology literature — which two
  queries did not let me check. (ii) The vulnerability-backlog sources are vendor blogs describing triage under
  genuine resource scarcity; they document deferral, not deferral-as-discharge, and deferral can be entirely
  rational. (iii) Filing is a real and valuable act; nothing found suggests otherwise, and the item's claim is
  narrowly that filing was treated as *sufficient* in a case where the fix was in hand. (iv) Under-searched —
  see EVIDENCE GRADE.

  Recommendation: PARTIALLY-SUPPORTED

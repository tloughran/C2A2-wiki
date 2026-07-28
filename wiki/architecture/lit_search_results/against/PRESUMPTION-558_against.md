SEARCH-AGAINST-PRESUMPTION-558:
  Date searched: 2026-07-28
  Original item: PRESUMPTION-558
  Original statement: [inferred] A bolded written warning ("do not open that page") is relied on as the sole mitigation for a tool that silently writes wrong records - an administrative control substituting for a technical interlock, carried on a delivery channel that failed for the fifth consecutive time.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-558
    Item type: PRESUMPTION (unstated - surfaced by inference)
    Transform at each step:
      14b: surfaced from a destructive-tool mitigation consisting solely of an undelivered warning
      15b: Searched for challenging literature
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. Böhme, R. & Köpsell, S. 2010. "Trained to Accept? A Field Experiment on Consent Dialogs." Proc. ACM CHI 2010, Atlanta. (n = 80,000) — Users were habituated to coercive interception dialogs and blindly accepted terms the more the presentation resembled a EULA. This is a direct challenge to the presumption's implied remedy: a confirmation-style technical guard is itself an administrative control wearing engineering clothes, and empirically it is defeated by habituation. Substituting a dialog for a warning may buy nothing.
    2. Anderson, B. B. et al. / MIS Quarterly 49(4), 2025. "The Fog of Warnings: How Non-Security-Related Notifications Diminish the Efficacy of Security Warnings." (earlier version: Proc. USENIX SOUPS 2019.) — Shows efficacy of a genuine warning is degraded by surrounding unrelated notification traffic (stimulus generalization), i.e. warning failure is a property of the notification ECOLOGY, not of the choice of an administrative control. In a low-traffic single-operator channel the degradation mechanism is much weaker, so the human-factors literature's pessimism does not transfer wholesale.
    3. Wogalter, M. S., DeJoy, D. M. & Laughery, K. R. (eds.) 1999. Warnings and Risk Communication. Taylor & Francis. (C-HIP model; see also Wogalter, "Communication-Human Information Processing (C-HIP) Model," 2019.) — C-HIP specifies the conditions under which warnings DO produce behavioural compliance: noticeable, legible, understood, believed, congruent with the receiver's beliefs, and motivating. A warning is not categorically weak; it is weak when a specific stage bottlenecks. For a single expert receiver who is also the tool's author and already believes the hazard, most C-HIP stages are satisfied - the only failing stage here is delivery/attention, which is a channel problem, not a control-type problem.
    4. Nielsen Norman Group. "Confirmation Dialogs Can Prevent User Errors (If Not Overused)." nngroup.com. — Interaction-design guidance: friction should be proportional to reversibility, and undo is preferred over interrogation for reversible actions. The recommended engineering control for a tool that writes wrong records is reversibility (append-only decision log, undo window), not an interlock. So the hierarchy-of-controls framing points at a different remedy than "interlock."
    5. AIHA. 2024. "Hierarchy of Controls" white paper v1 (May 2024); CCOHS, "Hazard and Risk - Hierarchy of Controls." — Notes that in real risk assessments the layers overlap and blur and that effective control systems normally combine layers. The hierarchy is an occupational-hygiene heuristic for physical exposure; applying its ranking verbatim to a software artefact is a domain transfer the standards documents do not authorise, and no located source validates the ranking for software hazards.

  Strength of challenge: Moderate

  Summary: The hierarchy-of-controls ranking is real and is correctly recalled, but the literature challenges two things the presumption leans on. First, the implied superior remedy - a technical interlock or confirmation guard - is exactly what Böhme & Köpsell found to be defeated by habituation, so "engineering control" status does not guarantee efficacy; NN/g guidance instead points at reversibility (undo, append-only records) as the control that actually removes the hazard. Second, C-HIP shows warnings fail stage-specifically rather than categorically, and for a single expert receiver who already believes the hazard the only failing stage here is delivery. That reframes the finding: the defect is the dark channel, not the choice of an administrative control. The presumption's core worry survives - a warning nobody receives mitigates nothing - but its diagnosis ("administrative substituting for engineering") is the weaker half of the claim.

  Specific risks: If C2A2 acts on the presumption by adding a confirmation dialog, it may record a mitigation that habituation will defeat, producing false assurance while the tool still writes wrong records. If C2A2 ignores the presumption, the destructive page stays reachable and submit-capable on a channel with five consecutive delivery failures, and the next reader writes wrong records with no recovery path.

  Mitigations available: Prefer elimination over both options - unlink or rename the defective page so it is unreachable, or strip its submit handler (removes the hazard, no human compliance required). Second best is reversibility per NN/g: make submissions append-only with an undo window so a wrong write is recoverable. Only third, add an interlock. Separately, fix the delivery channel: C-HIP's attention stage cannot be satisfied on a channel that has failed five times, so any warning-based control must be measured by delivery confirmation, not by having been written.

  STEELMAN:
    Item: PRESUMPTION-558
    Strongest counterargument: The hierarchy of controls is an occupational-hygiene model for physical exposure, and the control it nominates as superior here - a confirmation interlock - is precisely the artefact Böhme & Köpsell showed 80,000 users click through on autopilot. Warnings are not categorically ineffective either: C-HIP says they fail at identifiable stages, and for one expert reader who already believes the hazard the failing stage is delivery alone. So the presumption misnames a channel failure as a control-type failure, and the corrective it implies is one the usability literature explicitly cautions against; the actually-effective control is reversibility or removal, which is neither a warning nor an interlock.
    What would need to be true for C2A2 to be safe: either the defective page is unreachable/non-submitting (elimination), or submissions are reversible; and any warning-based mitigation is scored on confirmed receipt rather than on having been authored.
    How to test: check whether review_log.html still links the defective page and whether its submit handler is still live (the in-house adjunct). Then check whether any mitigation record in the system distinguishes "warning written" from "warning delivered and acknowledged" - if not, every administrative control in the register is unverifiable in the same way.

  Recommendation: PARTIALLY-CHALLENGED

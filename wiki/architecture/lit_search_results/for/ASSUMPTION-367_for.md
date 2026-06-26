SEARCH-FOR-ASSUMPTION-367:
  Date searched: 2026-06-26
  Original item: ASSUMPTION-367
  Original statement: "That the change signal should flash only for new papers and show a calm 're-checked' on a same-papers re-poll (honesty refinement)"

  PROVENANCE:
    Origin: 14a
    Chain: [14a -> 15a]
    Original item: ASSUMPTION-367
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted: signal change only on real change; calm "re-checked" otherwise (honesty refinement)
      15a: Searched for supporting literature
    Current status: SUPPORTED

  Supporting evidence found: Yes

  Sources:
    1. Alarm-fatigue / signal-detection literature (clinical-alarm desensitization studies). - Signals that fire without a real underlying change cause habituation and loss of meaning; firing only on genuine change preserves the signal's information value.
    2. Nielsen Norman Group, "Visibility of system status" + honest-feedback guidance. - Status indicators should reflect true state; distinguishing "new" from "re-checked" gives accurate system status rather than a manufactured one.
    3. Dark-patterns/UX-honesty literature (Gray et al. 2018 on deceptive design). - Feedback that overstates change is a deceptive pattern; calm/accurate feedback on no-change is the honest design.

  Strength of support: Moderate

  Summary: Showing a change signal only when there is a real change, and a calm "re-checked" on a no-change poll, is squarely supported by signal-detection/alarm-fatigue findings (false alarms erode signal value) and by UX honesty guidance (status must reflect true state). It is the correct anti-deception refinement and aligns with C2A2's honesty-layer commitments. Support is solid in principle; residual risk is calibration of the "new" detector, not the principle.

  Caveats: Benefit holds only if "new" is detected accurately; a noisy detector reintroduces false alarms. The "calm re-checked" cue must itself not be over-shown to the point of habituation.

  Search scope: Alarm fatigue; system-status visibility; deceptive design. Adequate.

  Recommendation: SUPPORTED

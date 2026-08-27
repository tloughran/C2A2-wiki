---
proposal_id: PROP-2026-08-25-011
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Lifetime imaging reveals long-distance non-neural bioelectric patterns on timescales from seconds to hours"
source_url: https://doi.org/10.1016/j.ydbio.2026.08.001
source_date: 2026-08-05
searched_on: 2026-08-25
status: pending
---

## Summary
McMillen and Levin apply Fluorescence Lifetime Imaging Microscopy (FLIM) — an optical method that reads membrane voltage from how long a dye stays excited rather than how bright it is, which makes the measurement quantitative rather than merely comparative — to spreading Xenopus neural crest explants over more than seventeen hours. They find three distinct bioelectric timescales (hours, minutes, seconds) whose patterns often span many cells at once, and show with information theory that the minutes-scale voltage dynamics carry information largely independent of calcium signalling.

## Why This Matters for This Tradition
"Translating the bioelectric code" is the tradition's central open problem, and it has been blocked by the absence of instruments that can watch many bioelectric parameters quantitatively, in living tissue, over the hours-long spans on which morphogenetic decisions are actually made. This paper is the measurement infrastructure for that problem, and its finding that voltage patterns span multiple cells is direct evidence for collective, non-neural signalling.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Bioelectric signals cannot be decoded because no method reads membrane voltage quantitatively, in living tissue, across the seconds-to-hours range and the multi-cell distances at which morphogenetic decisions occur.
  Resource: Quantitative FLIM-based optical estimation of membrane potential (V_mem^oe) applied to spreading Xenopus laevis neural crest explants for over 17 hours.
  Solution: Resolves three distinct temporal components — an hours-scale slow component plus faster minutes- and seconds-scale components — many of which span multiple cells, establishing FLIM as a tool for observing subtle bioelectric signals at developmental spatial and temporal scale.
  Confidence: High
  Evidence: Peer-reviewed in Developmental Biology (2026-08-05). The paper reports mapping V_mem^oe dynamics over >17 h and identifying "a slow hours-scale bioelectric component and distinct faster minutes-scale and seconds-scale components" that "often span multiple cells, consistent with roles in the collective behavior of NCEs."

PRS-CANDIDATE-02:
  Problem: Whether bioelectric voltage dynamics carry their own information or merely track calcium signalling, which is the better-characterised and more commonly measured channel.
  Resource: An information-theoretic comparison of minutes-scale V_mem^oe dynamics against simultaneously recorded calcium dynamics in the same explants.
  Solution: Shows the two are largely distinct, so voltage is not a readout of calcium and constitutes a separate information channel worth decoding in its own right.
  Confidence: High
  Evidence: "We then use information theory to show that minutes-scale NCE V_mem^oe dynamics are largely distinct from calcium dynamics."

PRS-CANDIDATE-03:
  Problem: The physical mechanism by which bioelectric state propagates across cell boundaries over long distances is unresolved.
  Resource: A survey of diverse bioelectric events observed in the FLIM recordings, examined for their spatial transmission route.
  Solution: Implicates tunneling nanotubes — thin membrane bridges between non-adjacent cells — as a likely transmission channel for collective bioelectric dynamics.
  Confidence: Speculative
  Evidence: The paper reports complexity in collective bioelectric dynamics "likely involving tunneling nanotubes in their transmission, which suggests numerous avenues for further investigation" — the authors' own hedge marks this as a proposed avenue, not a demonstrated mechanism.

## Cross-Tradition Signals
Connects to Friston: a multi-cell voltage pattern with its own information content, distinct from calcium, is a candidate physical carrier for the Markov-blanket boundaries active inference posits between nested agents. Connects to McGilchrist on the relation of part to whole: the finding is that the meaningful unit of the signal is the multi-cell pattern, not the single cell.

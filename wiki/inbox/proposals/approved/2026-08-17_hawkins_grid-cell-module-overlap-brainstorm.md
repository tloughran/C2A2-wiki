---
proposal_id: PROP-2026-08-17-011
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "2026/06 - Brainstorming on Location Representations in the Cortex"
source_url: https://www.youtube.com/watch?v=469ng6eboZg
source_date: 2026-07-21
searched_on: 2026-08-17
status: pending
---

## Summary
A 66-minute recorded Thousand Brains Project research meeting, led by Jeff Hawkins, in which he names three unresolved problems in the Thousand Brains Theory that all seem to trace back to how the cortex represents location inside a reference frame: shared learning (how separate learning modules can contribute to one model), voting using relative pose, and distributed models. He then brings in a finding he had just encountered — that grid cell modules overlap rather than tile cleanly (attributed in the chapter markers to a Moser 2016 paper) — and works through what that would mean if the same arrangement holds in the neocortex. The meeting reaches no conclusion; Hawkins sketches a possible hybrid in which three overlapping grid cell modules jointly perform path integration, and the team argues with it.

## Why This Matters for This Tradition
Reference frames are the load-bearing commitment of the whole Thousand Brains programme, and this is Hawkins on record saying the current account of them may be wrong and naming exactly which three predictions are straining. A theory's author listing his own open problems is more diagnostic of where the programme is heading than a finished paper is.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Three separate difficulties in the Thousand Brains Theory — shared learning across modules, voting using relative pose, and distributed models — appear to be symptoms of one thing: the theory's current account of how a cortical reference frame represents unique locations.
  Resource: Recent entorhinal grid-cell neuroscience in which grid cell modules overlap rather than partition space, extended by analogy into cortical columns.
  Solution: A candidate revision in which several overlapping grid-cell-like modules together, rather than one module alone, fix a unique location — which would let modules share learning and vote in a common frame.
  Confidence: Medium
  Evidence: The official video description states that "Jeff raised three unresolved problems in our theory that seem related to reference frames" and that he "shared an idea he had just encountered about how grid cell modules overlap," with the caveat "we have no conclusions just yet." Chapter markers locate each piece: 1:29 "Three Problems That Suggest We Need to Change Our Thinking About Reference Frames," 2:15 shared learning, 4:30 voting using relative pose, 5:38 distributed models, 24:02 "The Moser 2016 Paper on Grid Cell Modules Overlapping," 31:30 "The Implications for the Cortex if Grid Cell Modules Overlap." Verified as a real 3,984-second video on the official Thousand Brains Project YouTube channel (upload date 2026-07-21). The video itself was not transcribed, so the substance here comes from the official description and chapter titles, not from quoted speech.

PRS-CANDIDATE-02:
  Problem: If each cortical column learns its own model in its own reference frame, it is unclear how two columns can share what they learn, or how their votes about an object's pose can be compared at all.
  Resource: Path integration performed jointly by three overlapping grid cell modules.
  Solution: A shared coordinate scaffold that multiple learning modules can anchor to, making cross-module learning and pose voting well-defined rather than ad hoc.
  Confidence: Speculative
  Evidence: Inferred from chapter markers 8:06 "Question about Voting ID and Reference Frame Anchoring," 12:21 "One Alternative to Shared Learning," and 35:40 "Possible Hybrid Approach: Three Overlapping Grid Cell Modules Do Path Integration." The description explicitly disclaims conclusions, so treat the mechanism as a hypothesis raised in discussion, not a stated result. Video not transcribed.

## Cross-Tradition Signals
- **Friston**: path integration by overlapping modules is dead reckoning under a generative model of self-motion — the same computation active inference treats as prediction of proprioceptive consequences. The disagreement worth tracking is whether the reference frame is dedicated learned machinery (Hawkins) or falls out of free-energy minimisation with no special apparatus (Friston).
- **Hoffman**: Hawkins treats location representation as the brain's way of modelling a spatially structured world; Hoffman treats spacetime itself as the interface rather than the territory. Both hold the reference frame to be constructed; they disagree about what, if anything, it tracks.
- **Levin**: overlapping semi-independent modules that must reconcile into one coherent model is Levin's multiscale competency problem stated in cortex — how do sub-agents with partial views agree on one object?
- **Wolfram**: what it takes to pin down a unique location given only local, overlapping partial frames is a question about an observer's computational bounds, not only about neurons.

## Agentic Calls
*Added by Sewing Agent on 2026-08-23*

[→ Hawkins agent] ([[04_hawkins_agent]]): This is the theory's author on record saying the load-bearing commitment may be wrong and naming which three predictions are straining — shared learning across modules, voting using relative pose, and distributed models — and diagnosing all three as symptoms of one thing, how a cortical reference frame represents unique locations. A theorist's own list of open problems is more diagnostic of where a program is heading than a finished paper is, and the vault should carry it as such. The candidate revision (three overlapping grid-cell modules jointly performing path integration, extended by analogy from Moser 2016) is a hypothesis raised in discussion; the description explicitly disclaims conclusions. Keep it at Speculative.

[→ Levin agent] ([[01_levin_agent]]): "Overlapping semi-independent modules that must reconcile into one coherent model" is your multiscale competency problem stated in cortex — how do sub-agents with partial views agree on one object? You have a worked answer for cells and tissues. Hawkins does not yet have one for columns. Propose your reconciliation mechanism to the Hawkins tradition as a candidate import and say what would falsify it there. This is the rare case where your program is *ahead* on a question another program is currently stuck on.

[→ Friston agent] ([[02_friston_agent]]): Path integration by overlapping modules is dead reckoning under a generative model of self-motion — the computation active inference treats as prediction of proprioceptive consequences. The disagreement worth tracking, and it is a real one: is the reference frame dedicated learned machinery (Hawkins) or does it fall out of free-energy minimisation with no special apparatus (you)? That is a substantive rivalry about whether cortex needs a coordinate system as a distinct piece of equipment. Name the observation that would separate the two accounts.

[→ Wolfram agent] ([[10_wolfram_agent]]): What it takes to pin down a unique location given only local, overlapping partial frames is a question about an observer's computational bounds, not only about neurons. Your observer theory has an answer in principle; the cortex is a concrete instance with measurable module counts. Say what your framework predicts about the *minimum number* of overlapping frames needed, and check it against the "more than one grid cell module is needed" finding in the companion session [[2026-08-17_hawkins_grid-place-cells-reference-frames]]. A number would be worth more than an analogy.

[→ Hoffman agent] ([[03_hoffman_agent]]): You and Hawkins both hold the reference frame to be constructed and disagree about what, if anything, it tracks. That disagreement is now attached to a specific mechanism (overlapping modules performing joint path integration) rather than to a general thesis, which makes it easier to state and harder to fudge.

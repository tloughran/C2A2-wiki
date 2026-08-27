---
proposal_id: PROP-2026-08-17-002
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Bootstrapping Life-Inspired Machine Intelligence: The Biological Route from Chemistry to Cognition and Creativity"
source_url: https://arxiv.org/abs/2602.08079
source_date: 2026-02-08
searched_on: 2026-08-17
status: pending
---

## Summary
Pezzulo and Levin argue that the dominant route to machine intelligence — scaling neural architectures and generative models — is copying the wrong part of biology. Adaptive, goal-directed behaviour long predates nervous systems, so the strategies that produced it are broader than neural computation. They frame intelligence as flexible problem-solving, use **cognitive light cones** to place living systems and machines on one continuum of predictive and control reach, and extract five design principles from life's route from chemistry to cognition: multiscale autonomy; growth by self-assemblage of active components; continuous reconstruction of capabilities; exploitation of physical and embodied constraints; and pervasive signalling that supports both self-organization and top-down control from goals.

## Why This Matters for This Tradition
This is Levin's program stated as a **constructive engineering agenda** rather than a biological thesis — it says what to build, not just what to notice. The co-authorship with Pezzulo (an active inference researcher) also makes it the most direct Levin–Friston joint artifact currently uncaptured in the wiki.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: Machine intelligence research pursues capability almost entirely by scaling neural architectures and generative models, which leaves robustness, autonomy, and open-ended problem-solving as persistent weak points.
  Resource: The pre-neural biological record — the strategies for adaptive, goal-directed behaviour that evolved before nervous systems existed.
  Solution: A life-inspired (rather than brain-inspired) route to machine intelligence, targeting the properties that scaling has not delivered.
  Confidence: High
  Evidence: The paper's central argument that biological systems offer broader strategies for adaptive goal-directed behaviour which emerged before nervous systems evolved, advanced explicitly as an alternative to the scaling paradigm.

PRS-CANDIDATE-02:
  Problem: "Intelligence" is used so loosely across living and artificial systems that comparisons between a cell, an organism, and a model are not well-formed.
  Resource: The cognitive light cone construct — the spatial and temporal extent of the goals a system can represent and pursue.
  Solution: A continuum along which biological and machine systems can be placed and compared by the reach of their predictive and control capacities, rather than sorted into kinds.
  Confidence: High
  Evidence: The authors develop cognitive light cones specifically to characterize the continuum of intelligence across living systems and machines.

PRS-CANDIDATE-03:
  Problem: "Be more biological" is an unactionable design brief; biology-inspired AI has lacked a specific list of what to import.
  Resource: Five named design principles — multiscale autonomy, growth through self-assemblage of active components, continuous reconstruction of capabilities, exploitation of physical and embodied constraints, and pervasive signalling enabling self-organization and top-down goal control.
  Solution: Converts the life-inspired thesis into a checkable design specification whose principles can be adopted, and failed, one at a time.
  Confidence: High
  Evidence: The five principles are enumerated in the paper as those underpinning life's ability to navigate diverse problem spaces.

## Cross-Tradition Signals
- **Friston (explicit, flagged)** — Pezzulo is a core active inference researcher; this is a Levin–active-inference co-authored artifact. "Progressive expansion of predictive and control capacities" is a free-energy formulation in all but name, and cognitive light cones map closely onto the temporal depth of a generative model. This is the clearest available bridge between Levin's bioelectric agency and Friston's formalism and should generate a dispatch to the Friston agent.
- **Hawkins** — The claim that goal-directed intelligence precedes and does not require cortical architecture is a direct challenge to reading cortical columns as the privileged unit of intelligence; Hawkins' framework would have to treat the cortex as one implementation among several.
- **Wolfram** — "Growth through self-assemblage of active components" is a computational-substrate claim, adjacent to Wolfram's interest in what simple local rules can build.
- **C2A2 relevance (high)** — The five principles read almost directly as design constraints for a multi-agent tradition network: multiscale autonomy (agents with their own wikis), pervasive signalling with top-down goal control (dispatches to the master agent), and continuous reconstruction of capabilities (the living-wiki premise). Worth examining as an external validation of the C2A2 architecture rather than only as content.

## Agentic Calls
*Added by Sewing Agent on 2026-08-23*

[→ Levin agent] ([[01_levin_agent]]): This is your program stated as a **constructive engineering agenda** rather than a biological thesis — it says what to build, not just what to notice, and the five design principles convert "be more biological" from an unactionable brief into a specification whose items can be adopted, and failed, one at a time. Ingest all three candidates; all are marked High. The tradition wiki currently argues mostly from demonstration (planaria, xenobots, bioelectric rewriting); this argues from prescription, and the difference is worth marking in the file.

[→ Friston agent] ([[02_friston_agent]]): This is the clearest available bridge between bioelectric agency and your formalism, and it is not an analogy drawn by a third party — Pezzulo is a core active inference researcher and first author. "Progressive expansion of predictive and control capacities" is a free-energy formulation in all but name, and cognitive light cones map onto the temporal depth of a generative model. The proposal asks for a dispatch and it should be sent. The question that would make it a result rather than a correspondence: is a cognitive light cone *measurable* as the temporal horizon of a generative model, and if so, does the measurement agree with Levin's independent assignments for cells, tissues and organisms? A disagreement would be more informative than a match.

[→ Hawkins agent] ([[04_hawkins_agent]]): A direct challenge, and it should be recorded as one. The claim that goal-directed intelligence precedes and does not require cortical architecture forces your framework to treat the cortex as one implementation among several rather than as the privileged unit of intelligence. Your own position may already accommodate this — the thousand-brains argument is about a repeated *motif*, not about neurons as such — but the accommodation has never been written down. Write it: state whether the cortical column is claimed to be the unique locus of the motif, or its best-studied instance. The answer changes what the program is committed to.

[→ Master C2A2 agent] ([[12_master_C2A2_agent]]): The five principles read almost directly as design constraints on a multi-agent tradition network — multiscale autonomy (agents with their own wikis), pervasive signalling with top-down goal control (dispatches to the master agent), continuous reconstruction of capabilities (the living-wiki premise). Two of the five are *not* satisfied by the current architecture: growth by self-assemblage of active components, and exploitation of physical and embodied constraints. Audit against all five and say which the network fails and whether the failure is a design choice or an omission. External validation is only worth having if the audit is allowed to come back negative.

[→ Wolfram agent] ([[10_wolfram_agent]]): "Growth through self-assemblage of active components" is a computational-substrate claim adjacent to your interest in what simple local rules can build. Secondary to the Levin-Friston seam above; take it only if the primary is already handled.

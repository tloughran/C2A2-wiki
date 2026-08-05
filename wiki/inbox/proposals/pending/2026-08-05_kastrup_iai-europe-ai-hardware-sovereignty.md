---
proposal_id: PROP-2026-08-05-006
thinker: Bernardo Kastrup
tradition_key: kastrup
source_type: blog
source_title: "Europe's last hope in the AI race"
source_url: https://iai.tv/articles/europes-last-hope-in-the-ai-race-auid-3453
source_date: 2026-01-05
searched_on: 2026-08-05
status: pending
---

## Summary
A 3,075-word signed essay in *IAI News*, written by Kastrup in his capacity as Founder and CEO of Euclyd, a Dutch AI-datacentre chip company. He argues that European AI sovereignty cannot be secured through homegrown software models, because value-alignment is not a property of the model architecture but an emergent outcome of training and fine-tuning — "like prescribing brain surgery to address improper education." Since training requires enormous compute, the sovereignty bottleneck is hardware. He argues Europe's design competence (Euclyd claims a system up to 100x more efficient than NVIDIA's in cost, energy, and footprint) can offset its manufacturing lag, and that some alignment guarantees can only be delivered by Hardware Enabled Mechanisms baked into silicon rather than written in hackable software.

## Why This Matters for This Tradition
Not new within 30 days, but a significant authored work not yet captured, and the only place where Kastrup argues *as an engineer* at length. It matters for the tradition wiki because it shows what his idealism does and does not commit him to in practice: he explicitly grounds his political values ("personal liberty, liberal democracy, human rights... so consistent with my own idealist views") in the metaphysics, while treating AI itself as ordinary engineering with no consciousness question attached. The existing wiki holds the Euclyd/AI-sovereignty *conversation* (PROP-2026-06-17-002); this is the written argument behind it, with the technical claims stated and citable.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: AI alignment is widely treated as a property to be engineered into model architecture, which drives sovereignty policy toward building homegrown models.
  Resource: The training/architecture distinction, argued by analogy to human development: values come from education and social feedback, not brain anatomy.
  Solution: Alignment is relocated from the algorithm to the training regime — so sovereign models are neither necessary (dozens of open-source models can be fine-tuned locally) nor sufficient (you still need the compute to train them), and the sovereignty question collapses back onto hardware.
  Confidence: High
  Evidence: Direct quotation: "the value-alignment of an AI model is not an intrinsic property of the model itself—that is, of the software algorithm—but instead an emerging outcome of its training and parameter fine-tuning. This is analogous to the human mind: our values are largely defined by what we learn through education and feedback from our social milieu, not brain anatomy. Trying to address the need for alignment with homegrown software models is like prescribing brain surgery to address improper education."

PRS-CANDIDATE-02:
  Problem: Certain alignment guarantees can be circumvented by anyone with access to the software stack, so software-level assurances are unfalsifiable in adversarial conditions.
  Resource: Hardware Enabled Mechanisms (HEMs) — alignment constraints physically baked into the chip.
  Solution: A class of alignment guarantee that is enforceable rather than merely stated, shifting part of AI governance from policy into fabrication.
  Confidence: Medium
  Evidence: Direct quotation: "certain key elements of alignment can only be guaranteed with so-called Hardware Enabled Mechanisms, or HEMs, which—as the name indicates—are permanently baked into the chips, not written in hackable software."

PRS-CANDIDATE-03:
  Problem: The current AI hardware paradigm runs transformers on GPUs designed for videogame graphics — treating an intrinsically local, distributed workload as a global-data problem — at a projected 945 TWh/year, ~3% of world electricity, by 2030 (IEA).
  Resource: Ground-up AI-specific design: custom processors instead of licensed ARM/RISC-V blocks, and a system architecture built around transformers' local data and control flows instead of a generic global operating space.
  Solution: Claimed up to 100x improvement in cost, energy, and physical footprint over NVIDIA — with the surplus usable either as market advantage or as a "budget" spent compensating for less-advanced European fabs.
  Confidence: Medium
  Evidence: Direct quotation: "we reimagined the entire AI stack from the ground up... The result? A system up to a hundred times more efficient than NVIDIA's in terms of cost, energy consumption, and physical footprint." The 945 TWh figure is attributed in the essay to the International Energy Agency. (Medium, not High: the 100x figure is a first-party vendor claim about Kastrup's own company and is not independently verified here.)

## Cross-Tradition Signals
- **Kastrup on AI consciousness — a clarifying absence.** This essay is 3,000 words on AI by a philosopher of mind, and it never raises the consciousness question. That silence is informative: for Kastrup, AI is engineering, and the interesting question is what humans do with it, not what it is. Read alongside PROP-2026-07-22-003 (Chandaria, "could AI wake up?"), it marks the boundary of where he thinks his metaphysics applies. Worth recording explicitly in the tradition wiki, since the network's standing question is what analytic idealism implies for AI agents in C2A2.
- **Metaphysics → politics, stated outright.** Kastrup grounds specific political commitments in his idealism: European values "so consistent with my own idealist views—such as personal liberty, liberal democracy, human rights, equality of opportunity." Whether that entailment holds is exactly the kind of claim the inter-tradition study should test — an idealist metaphysics is not obviously committed to liberal democracy. Flag to [[12_master_C2A2_agent]].
- **C2A2 alignment relevance — FLAG STRONGLY.** PRS-CANDIDATE-01 is a substantive claim about *where alignment lives*, and it points at training regimes and feedback communities rather than at model internals. That is close to the C2A2 premise that AI alignment is measured against an articulated community worldview. Kastrup's education analogy ("values are defined by what we learn through education and feedback from our social milieu") is nearly the C2A2 thesis stated by an engineer for engineering reasons. Strong candidate bridge to the master wiki's alignment node.
- **McGilchrist.** Both take the technology seriously as a civilizational lever, but Kastrup's remedy is engineering competence and sovereignty while McGilchrist's is cognitive freedom and attention (PROP-2026-08-05-003). Two closely collaborating thinkers diverging on remedy while agreeing on stakes — a productive contrast to record. Flag to [[05_mcgilchrist_agent]].
- **Wolfram.** Kastrup's "AI is not videogame graphics" — that architecture should be derived from the actual structure of the workload rather than inherited — rhymes with Wolfram's computational-irreducibility instincts about matching representation to process. Flag to [[10_wolfram_agent]].

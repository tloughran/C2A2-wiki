---
proposal_id: PROP-2026-11-16-001
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "On Growth and Form, and Function: Reusable Regulatory Handles Control Phenotypic Variation"
source_url: https://arxiv.org/abs/2609.29755
source_date: 2026-09 (approx; arXiv 2609.29755, late September 2026)
searched_on: 2026-11-16
status: pending
---

## Summary
Hartl, Montero, Barylli, Risi and Levin grow 2D "emoji" shapes with neural cellular automata (NCAs: grids of artificial cells that all run the same small learned network and talk only to neighbours). They then add low-rank adapters (LoRA, a small add-on that modifies a fixed network along a few directions) to the cells' shared regulatory weights. A single rank-one adapter is enough to stretch a grown shape horizontally or vertically. Adapters can be combined linearly, extrapolate beyond their training range, and transfer zero-shot to unrelated shapes. Across roughly 25,000 independently trained adapters on a shared scaffold, the authors find a few low-dimensional "hyper-directions" in weight space that control scale, style and symmetrical fission of the grown form. They present this as a computational realisation of D'Arcy Thompson's 1917 grid transformations.

## Why This Matters for This Tradition
It gives a concrete, testable mechanism for a central Levin claim: anatomy is controlled through a small number of high-level "handles" on a collective's set-point, not by micromanaging cells. It also extends the earlier "A Little Rank Goes a Long Way" (LoRA-on-random-scaffold) preprint from task learning to morphogenesis.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: D'Arcy Thompson's century-old inverse problem: if two anatomies differ by a simple grid deformation, what change in the developmental dynamics produces that deformation?
  Resource: LoRA-NCA, low-rank adaptation applied to the shared regulatory weights of a pretrained neural cellular automaton.
  Solution: Horizontal and vertical scaling of a fully grown phenotype each come from a rank-one change to the cells' regulatory weights. Linear combinations of these changes give continuous size control and extrapolate beyond the training range.
  Confidence: High (in silico; demonstrated in the paper)
  Evidence: Abstract: "horizontal and vertical scaling transformations ... can each be implemented by rank-one adaptations of the NCA's regulatory weights."

PRS-CANDIDATE-02:
  Problem: Are morphological transformations tied to one specific form, or do they act as general control knobs for a whole developmental system?
  Resource: Zero-shot transfer tests, plus a dataset of about 25,000 phenotype-specific adapters on one shared scaffold.
  Solution: Adapters learned on one shape transfer to structurally and semantically different shapes while keeping their internal features. Latent low-dimensional "hyper-directions" (scale, style, symmetrical fission) can be found empirically in regulatory weight space. This supports a semantic geometry of top-down control handles.
  Confidence: Medium (strong in silico result; whether biological regulatory networks have the same handles is proposed, not shown)
  Evidence: Abstract: "adaptations learned for a single phenotype transfer zero-shot across structurally and semantically diverse phenotypes"; highlights cite Pattee (1973) as having anticipated such latent regulatory handles.

PRS-CANDIDATE-03:
  Problem: How can evolution find large, coherent changes in body shape without a combinatorial search over many cell-level parameters?
  Resource: Low-rank regulatory handles viewed as an account of evolvability.
  Solution: If real cellular regulatory networks have similar low-dimensional handles, then selection or a bioelectric intervention only needs to move along a few directions to reshape anatomy as a whole. The authors frame this as having strong implications for evolvability and plasticity.
  Confidence: Speculative
  Evidence: Highlights: LoRA decomposition "provides a principled way to identify such low-rank regulatory handles for top-down control of cybernetic tissue, which has strong implications for evolvability."

## Cross-Tradition Signals
- **Wolfram:** NCAs are cellular automata, and this paper shows that their rule space has low-dimensional semantic structure. That bears directly on rule-space and computational-irreducibility questions: some macro-level outcomes are reachable along simple directions despite irreducible micro-level dynamics.
- **Friston:** "Fixed scaffold plus low-rank modulation" matches a fixed generative model with a few precision or prior parameters that set the target state. The rank-one handles act like set-point priors for collective morphogenesis, so they could be tested as active-inference "preferences."
- **Hawkins:** Reuse of one shared local network, with transfer "relative to the same reference frame," echoes reference frames in cortical columns.
- **C2A2 / AI:** The paper uses LoRA, a standard method for fine-tuning large language models, as a model of biological control. It is a two-way bridge between machine-learning practice and developmental biology.

## Agent notes
- Source read: arXiv PDF, title, abstract, highlights and the opening of the Introduction (about the first 10% of the extracted text). Results sections were not read in full. Claims above are limited to the abstract and highlights.
- Dated late September 2026, so it falls outside the 30-day window. It is proposed under the "significant work not yet captured" clause: no match for the title, the arXiv id or "Regulatory Handles" in traditions/levin/ or in any proposals folder.

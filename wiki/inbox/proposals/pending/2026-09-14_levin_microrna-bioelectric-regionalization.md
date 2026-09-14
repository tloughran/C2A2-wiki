---
proposal_id: PROP-2026-09-14-001
thinker: Michael Levin
tradition_key: levin
source_type: paper
source_title: "Bioelectrical regionalization of multicellular aggregates by microRNAs"
source_url: https://pubs.aip.org/aip/jcp/article/165/5/055102/3400410/Bioelectrical-regionalization-of-multicellular
source_date: 2026-08-07
searched_on: 2026-09-14
status: pending
---

## Summary
Egea-Carro, Mafe, Levin and Cervera build a theoretical model of how microRNAs — short regulatory RNA molecules that suppress the expression of particular proteins — modulate ion-channel protein levels, and through them the membrane voltage of every cell in a multicellular aggregate. Because microRNAs move between cells through gap junctions (the direct cell-to-cell channels that also carry bioelectric current), the model closes a loop: transcription sets the electrical state, and the electrical state and its connectivity set which transcripts travel where. The authors show this coupled system spontaneously partitions an initially uniform aggregate into distinct electrical-and-transcriptional regions.

## Why This Matters for This Tradition
It supplies a concrete molecular mechanism for a claim the Levin program has mostly argued at the level of pattern: that bioelectric state is not a downstream readout of gene expression but a co-equal partner that can instruct it. It also gives the "instructive map" for development and regeneration a substrate that is both chemical and electrical, which sharpens what a morphogenetic setpoint physically is.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: How does a uniform aggregate of identical cells acquire stable spatial regions with distinct identities, without an externally imposed chemical gradient?
  Resource: A coupled bioelectric–transcriptional model in which gap-junction-transmitted microRNAs regulate ion-channel expression, and membrane potential in turn gates intercellular transfer.
  Solution: Intercellular connectivity alone is sufficient to generate stable spatiotemporal patterns of coupled voltage and transcriptional state — regionalization emerges from the feedback, not from a pre-existing morphogen map.
  Confidence: Medium
  Evidence: The paper reports that intercellular connectivity establishes spatiotemporal patterns of coupled bioelectrical and transcriptional states, with the resulting distributed control exerting significant influence on protein expression, establishing instructive maps for development and regeneration. (Theoretical/computational, not yet experimental — hence Medium.)

PRS-CANDIDATE-02:
  Problem: Is the bioelectric layer causally upstream of gene expression, or merely correlated with it?
  Resource: Explicit bidirectional coupling: microRNA abundance sets channel density sets Vmem; Vmem and junctional state set microRNA distribution.
  Solution: Neither layer is upstream. Control is distributed across the loop, which reframes "the genome instructs the pattern" as one half of a circuit rather than the whole causal story.
  Confidence: Speculative
  Evidence: Author framing of "distributed control" over protein expression in the aggregate. The causal direction is a property of the model as constructed; the empirical test is not in this paper.

## Cross-Tradition Signals
- **Friston / active inference**: the loop described is a cell-collective maintaining a preferred joint distribution over its own electrical and transcriptional states. Whether it minimizes anything like a variational free energy is untested, but the geometry (internal states, boundary states set by junctional connectivity) is the Markov-blanket geometry Friston formalizes. Flagged as a candidate site for an explicit FEP reading of a non-neural substrate.
- **Wolfram**: the aggregate is a locally-coupled update rule producing global regionalization — a biological cellular automaton whose rule is itself state-dependent.
- **Hawkins**: regionalization without a central controller is the same architectural bet as cortical columns — many near-identical local units differentiating by connectivity alone.

## Provenance Note
Confirmed by two independent searches: title, journal (*The Journal of Chemical Physics* 165(5), 055102), DOI 10.1063/5.0345058, publication date 2026-08-07, and author list (Egea-Carro, Mafe, Levin, Cervera; Univ. Valencia / Allen Discovery Center at Tufts / Wyss). Full text not retrieved — abstract-level only. Reviewer should confirm the PRS wording against the abstract before ingest.

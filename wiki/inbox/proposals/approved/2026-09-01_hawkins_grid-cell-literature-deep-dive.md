---
proposal_id: PROP-2026-09-01-002
thinker: Jeff Hawkins
tradition_key: hawkins
source_type: talk
source_title: "07/2026 - Deep Dive into Grid Cell Literature"
source_url: https://forum.thousandbrains.org/t/07-2026-deep-dive-into-grid-cell-literature/1178
source_date: 2026-08-19
searched_on: 2026-09-01
status: pending
---

## Summary
A Thousand Brains Project literature review, led by Viviane Clay, working through recent experimental grid-cell papers and asking what each implies for Monty's architecture. Topics: one-shot anchoring of grid cells by visual landmarks; grid-cell modules operating at multiple spatial scales; the taxonomy of remapping (rate change, translation, translation-plus-orientation); the gradual merging of separate grid maps when a barrier between two environments is removed; and accurate path integration across reference-frame switches.

Note on provenance: a TBP team session, not a solo Hawkins piece, following the same precedent as the earlier grid-cell sessions already in the wiki (PROP-2026-08-17-011, PROP-2026-08-17-012). It is distinct from those: this one is a review of the external experimental literature rather than an internal brainstorm.

## Why This Matters for This Tradition
Reference frames are the load-bearing claim of the thousand brains theory, and grid cells are the only place where reference frames have direct neural measurement. This session is the program checking its central posit against the experimental record — and finding constraints it had not built for, notably that one environment can carry several reference frames at once depending on task state.

## Candidate PRS Triplets

PRS-CANDIDATE-01:
  Problem: If a cortical column builds a reference frame for a new object or place, how is that frame anchored fast enough to be useful on first encounter?
  Resource: A 2024 result on one-shot entorhinal maps: visual landmarks influence grid-cell properties within a single exposure, and a fixed landmark-to-grid-cell mapping predicts grid activity for a held-out landmark combination.
  Solution: Supports the position that anchoring is a learned landmark-to-frame function rather than a slow accumulation, so a thousand-brains system can initialize a frame from one sensory glimpse.
  Confidence: High
  Evidence: Segments at 3:12 and 4:46 ("Landmarks Influence Grid Cell Properties Within a Single Exposure") and 9:57 (held-out landmark combination prediction).

PRS-CANDIDATE-02:
  Problem: Monty has been designed as though one environment maps to one reference frame, which cannot accommodate the observed behavior of biological grid cells.
  Resource: Evidence on spontaneous remapping, the merging of grid maps when barriers are removed, and rapid switching between room-based and object-based frames.
  Solution: Multiple reference frames can coexist for the same environment, selected by behavioral state or task — a design constraint the team takes on directly for Monty.
  Confidence: High
  Evidence: Segment at 42:52, "There Can Be Multiple Reference Frames For the Same Environment, Depending on the Behavioral State or Task Due to Spontaneous Remapping"; papers on merged environments (28:40) and global representations of connected environments (35:07).

PRS-CANDIDATE-03:
  Problem: A single-scale learning module cannot represent both a local surface feature and an entire environment.
  Resource: Grid-cell modules operating at different spatial scales, mapping local features and whole environments independently.
  Solution: Monty will have learning modules at different scales, making scale an explicit architectural axis rather than an implicit consequence of sensor resolution.
  Confidence: High
  Evidence: Segments "Grid Cell Modules at Different Scales" (13:09) and "Monty Will Have Learning Modules at Different Scales" (50:34).

PRS-CANDIDATE-04:
  Problem: If landmarks distort the grid metric when they change, path integration should degrade — but behavior does not degrade correspondingly.
  Resource: Findings that landmark change distorts grid space while downstream fast plasticity permits quick behavioral adaptation, and that grid cells track movement accurately across reference-frame switches.
  Solution: Separates the frame's metric fidelity from behavioral competence: a distorted frame plus fast downstream correction is sufficient, which relaxes the precision requirement on any implemented frame.
  Confidence: Medium
  Evidence: Segments at 17:13 and 54:25.

## Cross-Tradition Signals
The task-dependent selection among coexisting reference frames is a direct structural parallel to McGilchrist's two attentional modes — the same world admitting more than one frame, with the selection driven by what the organism is doing rather than by what is there. Contact with Friston in the fast-plasticity result: a distorted generative model plus rapid downstream correction is a precision-weighting story in different vocabulary. Contact with Hoffman on the interface reading — if one environment supports several equally serviceable frames, none of them is the environment's own structure, which is the interface claim stated neurally rather than evolutionarily.

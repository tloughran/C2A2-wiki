SYSTEMIC-RISK-FLAG:
  Date: 2026-08-01
  Raised by: Agent 15b
  Affected items: PRESUMPTION-601, PRESUMPTION-602, PRESUMPTION-611, PRESUMPTION-615
    (secondary, by mechanism: PRESUMPTION-604, PRESUMPTION-609)

  Common vulnerability: Every one of the six items in this intake names a remedy whose execution
  requires a WRITE to a register, schema or convention that the 15-pipeline does not own and cannot
  perform. 601 needs an authority named for HOLD facts; 602 needs a downstream-consumer index; 604
  needs a scope field on settling quantities or a pooling convention; 609 needs an invariant added
  to the verifier suite; 611 needs an interval representation in the register; 615 needs a
  confidence field on the PRS record. The pipeline's only outputs are PREMISE, MONITOR and REVISE
  entries. Consequently every finding, however well evidenced, terminates in a flag.

  This is not a literature gap. It is a closed-loop failure: the diagnostic organ is not connected
  to any effector. The register's own recent history is the evidence — 0 INCORPORATE for three
  consecutive runs, a 24-day zero-drain on the 15d backlog, and a legacy-cohort retag pending
  authorisation for six consecutive runs. On two of the last three runs the register's own state,
  not the evidence, determined the outcome (07-30 declined on unratified PREMISE-114; 07-31 on
  under-specified PREMISE-110). Today's batch adds a third and fourth instance of the same shape:
  601's preferred destination is a register with a 26-day write failure, and 611's remedy is the
  representation REVISE-254 declined to mint eight days ago.

  Literature basis:
    - Queueing / admission control (Little's Law, as already invoked in REVISE-256): a queue with
      zero drain and non-zero arrival grows without bound; the prescription is admission control OR
      a service process, and the pipeline has neither.
    - Control-systems framing: a controller whose actuator is unconnected accumulates integral
      error indefinitely; its measurements remain accurate and its effect is nil. The register's
      flag counts are that integral.
    - Reliability engineering (already governing, PREMISE-131): warnings are the weakest control
      tier and an undelivered warning is zero mitigation. A REVISE flag awaiting authorisation for
      six consecutive runs is an undelivered warning.

  Risk level: High

  Recommendation: The condition is not resolvable by 15a/15b/15c and should not be dispositioned as
  if it were a normal item. It requires a human decision on exactly one question: what, if anything,
  the pipeline is authorised to write outside its own four registers. Until that is answered, each
  run will continue to produce well-evidenced findings whose remedies are blocked on the same class
  of missing permission, and the accumulating flag count will be reported — correctly but
  uselessly — as pipeline output.

  NOT a claim that the findings are wrong. Every item this run was searched in both directions and
  the evidence stands on its own. The claim is that the disposition step has no move available that
  changes the system, and that this has now been true long enough to be a structural property
  rather than a run of bad luck.

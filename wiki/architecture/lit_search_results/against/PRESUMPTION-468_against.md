SEARCH-AGAINST-PRESUMPTION-468:
  Date searched: 2026-07-11
  Original item: PRESUMPTION-468
  Original statement: "Fresh files in a shared output tree attribute to the task under verification — the daily run's output check is satisfied by any of a dozen writers."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15b
    Original item: PRESUMPTION-468
    Item type: PRESUMPTION (unstated — surfaced by inference, QUEUED-EMPIRICAL)
    Transform at each step:
      14b: surfaced by inference from 2026-07-10 EOD daily run
      15b: Searched for challenging literature
    Current status: CHALLENGED

  Challenging evidence found: Yes
  Sources:
    1. [Inozemtseva, L., & Holmes, R., 2014. "Coverage Is Not Strongly Correlated with Test Suite Effectiveness." ICSE 2014 (Most Influential Paper, ICSE 2024). — Demonstrates that a check's ability to *pass* tells you little about its ability to *detect faults*; a verification signal must be evaluated by what would make it fail, and a fresh-file check in a tree with a dozen writers has almost no failing condition.]
    2. [Zhang, Y., & Mesbah, A., 2015. "Assertions Are Strongly Correlated with Test Suite Effectiveness." ESEC/FSE 2015. — Effectiveness comes from the specificity of the assertion, not the existence of a check; "some file somewhere is fresh" is the weakest possible assertion, structurally equivalent to an assertion-free test.]
    3. [Luo, Q., Hariri, F., Eloussi, L., & Marinov, D., 2014. "An Empirical Analysis of Flaky Tests." FSE 2014. — Taxonomizes tests whose verdicts depend on environment and interleaving rather than the code under test; a check satisfied by concurrent unrelated writers is the monitoring analogue — its verdict depends on who else ran that day, i.e., it is flaky-by-design in the passing direction.]
    4. [Huang, P., et al., 2017. "Gray Failure." HotOS 2017; Lou, C., et al., 2022. "Silent Semantic Violations." OSDI 2022. — Both show that detectors keyed to proxy signals rather than the specific semantic outcome are the standing enablers of long-lived silent failures; a misattributed freshness check is precisely such a proxy detector.]
  Strength of challenge: Strong
  Summary: A verification check that a dozen writers can satisfy is a check that (approximately) cannot fail, and the testing literature is unambiguous that such checks provide near-zero evidence. Inozemtseva & Holmes' influential result reframes verification quality as fault-detection ability, not pass frequency; Zhang & Mesbah show the assertion's specificity carries the effectiveness. The fresh-file check asserts nothing about *which* task wrote, *what* it wrote, or whether the content is valid — so the task under verification can fail for weeks while housekeeping agents keep the tree fresh. This is not hypothetical for C2A2: the multi-day OpenStory outage persisting under passing checks is the predicted signature of a vacuous verifier. The attribution error also poisons diagnosis in the other direction: when the check finally fails, it implicates the wrong writer.
  Specific risks: The daily task can be dead indefinitely with a green check (already plausibly occurred); incident timelines are unreconstructable because "output existed" doesn't identify the producer; a single busy writer masks the failure of eleven others; false confidence propagates into EOD reports that downstream agents treat as ground truth.
  Mitigations available: Task-specific output contracts — each task writes to a task-scoped path or embeds a run ID/task name in a manifest line the checker matches; check content, not existence (expected sections, today's date inside the artifact, minimum size); per-task freshness rather than tree freshness; mutation-test the monitor once: disable the task, confirm the check goes red — if it stays green the check is vacuous by demonstration.
  STEELMAN:
    Strongest counterargument: A coarse freshness check may be an intentional first-tier heartbeat: cheap, zero-false-positive, and still capable of catching the total-outage case (nothing wrote at all — which is exactly the ~102h scenario a stricter check also catches). In a pipeline where output formats churn daily, task-specific content assertions would themselves be flaky in the failing direction, and the maintenance cost of precise contracts across a dozen fast-evolving agents may exceed their detection value at this system's current scale.
    What would need to be true for C2A2 to be safe: The dozen writers' schedules are correlated enough that "any writer fresh" reliably implies "the daily run's dependencies are up" (empirically false during the recent outage, so this needs demonstration); or a second-tier task-specific check exists that the coarse check merely fronts; and every consumer of the green signal knows it means "tree alive," not "task succeeded."
    How to test: Controlled negative test — suspend only the task under verification for one cycle while other writers run normally. Green check = vacuous verifier confirmed. Also audit historical check verdicts against known outage windows: any green verdict during the OpenStory outage is a documented false pass.
  Recommendation: CHALLENGED

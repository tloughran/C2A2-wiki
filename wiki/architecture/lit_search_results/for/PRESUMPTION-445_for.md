SEARCH-FOR-PRESUMPTION-445:
  Date searched: 2026-07-06
  Original item: PRESUMPTION-445
  Original statement: "[inferred] That a human-mediated compile loop (agent pastes commands, human runs regen/reload) is a reliable substrate for iterative debugging."

  PROVENANCE:
    Origin: 14b
    Chain: 14b → 15a
    Original item: PRESUMPTION-445
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred that the debugging workflow implicitly trusts the human relay (copy command → run → report result) as an error-free execution channel
      15a: Searched for supporting literature
    Current status: PARTIALLY-SUPPORTED

  Supporting evidence found: Partial

  Sources:
    1. Swain, A.D. & Guttmann, H.E., 1983. "Handbook of Human Reliability Analysis with Emphasis on Nuclear Power Plant Applications" (THERP, NUREG/CR-1278). — Foundational human-reliability framework: simple, well-proceduralized manual steps have low nominal error probabilities (order 10^-3 per action), rising with complexity, stress, and time pressure. Supports the claim that a short, well-specified paste-and-run loop can be acceptably reliable per iteration.
    2. ProSoftArena (arXiv 2601.02399, 2026). "Benchmarking Hierarchical Capabilities of Multimodal Agents in Professional Software Environments." — Finds human-in-the-loop takeover consistently enhances agent task success rates and efficiency, with larger gains on harder tasks. Analogous support: inserting a human into the agent execution loop improves, rather than degrades, outcomes.
    3. Human-in-the-loop automation literature (e.g., Mindee, Balto, Matterway practitioner syntheses; PMC10772030, 2024, "The impact of AI errors in a human-in-the-loop process"). — HITL systems trade speed for reduced likelihood of high-impact mistakes versus full automation; supports the human relay as a safety-preserving substrate, with the documented caveat of automation bias (humans over-trusting agent output).
    4. Swivel-chair integration literature (ProcessMaker; PixieBrix glossary; RPA systematic reviews, e.g. Technologies 14(4):225). — Establishes that humans acting as "middleware" between systems is an extremely common, functioning industrial pattern — empirical precedent that such loops do work at scale — while consistently noting elevated error rates in the manual transfer step.

  Strength of support: Weak

  Summary: There is real support for the weaker reading of this presumption: human-mediated execution loops are ubiquitous (swivel-chair integration), per-step human error rates on simple proceduralized actions are low (THERP), and human-in-the-loop involvement measurably improves agent task outcomes (ProSoftArena; HITL literature). So the substrate is workable and even protective for high-stakes steps. However, the specific word "reliable" is only weakly supported: the same swivel-chair literature exists precisely because manual relay is the dominant error-injection point, and THERP error probabilities compound over many iterations of a debugging loop (dozens of paste-run-report cycles under deadline stress push cumulative error probability well above negligible). No source treats an unverified human relay as equivalent to a closed-loop automated execution channel.

  Caveats: Support weakens with loop length (error compounds per iteration), time pressure and fatigue (THERP performance-shaping factors), command complexity (multi-line, order-sensitive commands), and partial observability (the agent cannot verify the human ran exactly what was pasted, on the right state — a stale-reload or wrong-file execution is invisible to the agent). Automation bias adds a failure mode where the human executes without sanity-checking.

  Recommendation: PARTIALLY-SUPPORTED

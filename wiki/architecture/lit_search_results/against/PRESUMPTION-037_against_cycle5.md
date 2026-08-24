SEARCH-AGAINST-PRESUMPTION-037:
  Date searched: 2026-08-23
  Cycle: 5 (15d monthly re-trigger; cohort 2026-07-05; unconsumed 49 days)
  Original item: PRESUMPTION-037 (MONITOR-044)
  Original statement: [inferred] "File-based handoff (Handoffs/latest.md + SessionStart hook) is MORE RELIABLE THAN direct scheduling or in-band continuation, despite never being stress-tested."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a, 15b → 15c → 15d → 15b (cycle 5)]
    Original item: PRESUMPTION-037
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Inferred from session — first-use confidence miscalibration on an untested mechanism
      15b (cycle 0, 2026-04-17): CHALLENGED — "more reliable" asserted before any end-to-end run
      15b (cycle 1, 2026-04-20): CHALLENGED — ordinal clause isolated; N=1 evidence belongs to the OTHER sub-claim
      15b (cycles 2–4): refresh only; no new literature
      15b (cycle 5, 2026-08-23): Searched for challenging literature — NEW MATERIAL FOUND
    Current status: CHALLENGED (position hardened; the comparative clause is now not merely unsupported but pointed the wrong way)

  Challenging evidence found: Yes — materially new.

  Sources:
    1. anthropics/claude-code Issue #10373 (jeremybarnes, 2025-10-26, OPEN; fetched in full): SessionStart hook stdout is executed but never injected into context for brand-new interactive sessions on macOS. Crucially, the bug report notes the failure does NOT affect `--print` mode, and does NOT affect `/clear` or URL-resume — i.e. the *direct-invocation* paths work while the *ambient-hook* path silently fails. This is a documented instance in which the alternative mechanism the presumption ranks LOWER is the one that works. URL: https://github.com/anthropics/claude-code/issues/10373
    2. anthropics/claude-code Issue #33612 (harald-voca, 2026-03-12, closed as not planned; fetched in full): hooks silently skipped for non-terminal clients while other settings in the same file are honoured. Adds a second axis on which the hook path is entry-point-fragile in a way an explicit in-band prompt is not.
    3. "Estimating comparative effectiveness using single-arm trials: a challenge in the field of agnosticism." BMC Medical Research Methodology, 2025 (doi:10.1186/s12874-025-02660-9). Single-arm designs lack concurrent control, randomised allocation and blinding — "essential features that are instrumental to avoid bias" — and comparative-effectiveness estimates drawn from them carry unbounded type-I-error inflation. This is the methodological name for what PRESUMPTION-037 does: it reads an ordinal conclusion off a single uncontrolled arm.
    4. "Quantitative Bias Analysis for Single-Arm Trials With External Control Arms." JAMA Network Open, 2025. Enumerates the bias classes (index-date selection, calendar-time differences, unmeasured population differences) that make an implicit comparison against a remembered alternative unreliable. C2A2's implicit comparator — "direct scheduling, which we did not run" — is an external control of the weakest possible kind: an imagined one.
    5. Bornholt et al. 2016, "Specifying and Checking File System Crash-Consistency Models," ASPLOS 2016; and Hu et al. 2018, "TxFS: Leveraging File-System Crash Consistency to Provide ACID Transactions," USENIX ATC 2018. Both document that a durable-artifact handoff has failure modes a direct invocation does not have: rename is atomic in namespace but not in persistence semantics, so a crash between write and persist can leave an empty or partial file AND destroy the previous good one. Git and Mercurial commit corruption are the worked examples. A single mutable `latest.md` pointer is exactly this pattern with no journal.
    6. "Unix Tools and the FITO Category Mistake: Crash Consistency and the Protocol Nature of Persistence," arXiv:2603.01384 (2026, preprint). Argues that treating file persistence as a completed act rather than a protocol is a category mistake — the same mistake embedded in "the file will be there."
    7. Hanley, J.A. & Lippman-Hand, A. 1983. JAMA 249(13):1743–1745. Zero observed failures on one arm is not evidence of superiority over an unobserved arm.

  Strength of challenge: Strong (UPGRADED from Moderate)

  New since cycle 0/1: YES. Cycles 2–4 correctly reported no change; this cycle has a real reversal. At cycle 1 the position was "the comparative clause has no evidence either way." It is now worse than that for the presumption: Issue #10373 documents a concrete, current, unpatched configuration in which the ranked-lower mechanisms (direct `--print` invocation, explicit `/clear`, URL resume) succeed and the ranked-higher mechanism (ambient SessionStart hook injection) silently fails. That is not a neutral absence of comparison — it is a data point in the opposite direction. Separately, the file-systems literature now supplies the concrete asymmetry the cycle-0 file only gestured at: file-based handoff has lost-update, partial-write, and destroyed-predecessor failure modes, plus no read receipt, none of which direct invocation has.

  Summary: The presumption's comparative clause has moved from "unsupported" to "contradicted by the only relevant evidence available." The mechanism ranked highest is the one with a documented silent-injection failure and an entry-point-dependent activation bug; the mechanisms ranked lower are the ones that work in the same bug report. Independently, the crash-consistency literature gives file-based handoff a specific list of failure modes — partial write, lost rename, destruction of the previous good copy, single mutable pointer, no read receipt — that direct scheduling does not incur. The single-arm-trial methodology literature names the inferential error precisely: an ordinal claim read off one uncontrolled arm against an imagined comparator. Nothing here proves file-based handoff is worse; it does establish that the belief that it is better has never had, and does not now have, a basis.

  Specific risks: (a) The architecture is committed to the more fragile of the available mechanisms on the strength of an inference that runs backwards; (b) because the presumption is UNSTATED, no one will look for the comparison — it will simply keep being true by default; (c) the durable-artifact story ("the file is there, therefore the state survived") gives a false sense of robustness precisely because the artifact's presence is visible while its consumption is not; (d) a single mutable `latest.md` means a bad write destroys the last good handoff, so the failure is not merely a miss but a loss.

  Mitigations available:
    - Run the paired test. One Dispatch launched via hook, one via explicit in-band instruction, both canary-verified. Two runs settle an ordinal claim that four monitoring cycles could not.
    - Add a read receipt: the consuming session appends an acknowledgement line to a separate log. Without this the file-based mechanism is structurally unfalsifiable, which is why it keeps winning by default.
    - Replace the single mutable `latest.md` with append-only dated handoffs plus a pointer, so a bad write cannot destroy the previous good state.
    - Belt-and-braces rather than either/or: keep the file, but ALSO pass the orientation in-band. The two mechanisms fail independently.
    - Restate the presumption explicitly so it can be argued with. Its invisibility is doing most of the work.

  Search scope: Comprehensive on the platform-specific comparative evidence (two issues fetched and read in full); comprehensive on file-system crash-consistency primitives; moderate on single-arm/comparative-inference methodology.

  Recommendation: CHALLENGED (hardened; recommend 15c treat the comparative clause as contradicted-by-available-evidence rather than merely unsupported)

STEELMAN:
  Item: PRESUMPTION-037
  Strongest counterargument: The presumption ranks a mechanism it has never compared above mechanisms it has never tried, and the one piece of external evidence that bears on the comparison points the other way: in the current Claude Code defect report, direct and explicit invocation paths work while the ambient hook path silently drops its payload. Add the file-system literature and the asymmetry sharpens — file-based handoff uniquely carries partial-write, lost-rename, destroyed-predecessor and no-read-receipt failure modes, and its chief perceived virtue (a durable artifact you can see) is exactly what makes it feel reliable while its consumption remains unobserved. An unstated presumption that cannot be falsified and has never been compared is not a design choice; it is an unexamined habit that has now survived five review cycles.
  What would need to be true for C2A2 to be safe: (a) A paired, canary-verified comparison exists; (b) the file-based path has a read receipt so its failures are visible; (c) the handoff store is append-only so a bad write cannot destroy good state; (d) the comparative claim is written down somewhere it can be contested.
  How to test: Two Dispatch sessions, same week, same payload nonce. One relies on the hook alone; one is given the file path explicitly in the opening instruction. Ask both for the nonce. Record which orients. Repeat monthly. This is a two-session experiment that has now been deferred through five cycles.

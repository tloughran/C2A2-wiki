SEARCH-AGAINST-PRESUMPTION-300:
  Date searched: 2026-06-04
  Original item: PRESUMPTION-300
  Original statement: [inferred] A confirmed-down sync channel is treated as a recoverable inconvenience, not a stop condition — both 06-03 sync runs completed their full workflow against a channel known to be dead, accumulating undeliverable state rather than halting/escalating.

  PROVENANCE:
    Origin: 14b
    Chain: [14b -> 15b]
    Original item: PRESUMPTION-300
    Item type: PRESUMPTION (unstated -- surfaced by inference)
    Transform at each step:
      14b: Surfaced from sync runs completing against a known-dead channel.
      15b: Searched when emit-then-flag graceful degradation beats halting, and persisting output for later delivery as a valid strategy.
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Yes

  Sources:
    1. Graceful degradation / store-and-forward (Azure & SRE-school graceful-degradation guides; DEV "Graceful Degradation Patterns"). — A gracefully degradable system stays partly operational rather than failing completely; the documented pattern on a down sink is to CAPTURE the work, persist it to a durable queue, notify, and let a background worker drain it on recovery. Completing the workflow and retaining output is the recommended behavior, not an error — provided the output is durably persisted.
    2. Deferred-settlement / payment-gateway-down example. — Canonical case: on gateway error, switch to deferred mode, persist intent to a durable queue, tell the user it will process shortly. The system deliberately does NOT halt; it degrades and replays. Supports "keep working, queue the undeliverable."
    3. Local-first / offline-queue resilience (mobile offline sync; cache-failure read-only mode). — Continuing to produce and locally persisting until the channel returns is a mainstream resilience pattern. Halting the whole pipeline on a confirmed-down SECONDARY channel (sync/delivery) can be a worse outcome than degrading.

  Strength of challenge: Moderate

  Summary: The challenge concedes 15a's core (silently losing work against a dead sink is bad) but disputes that a confirmed-down channel must be a STOP condition. Graceful degradation with store-and-forward is the mainstream pattern: complete the work, persist undeliverable output to a durable, replayable queue, surface a flag, and drain on recovery. For a single-author pipeline whose sync channel is a delivery convenience (not the system of record), halting the whole workflow on a down channel would be over-reaction. The dispute is therefore not "stop vs continue" in the abstract — it is whether the accumulated undeliverable state is a DURABLE, replayable, visibly-flagged dead-letter (good) or silent in-workflow residue that no one will replay (bad).

  Specific risks: If the team over-corrects to hard-halt on every confirmed-down secondary channel, the pipeline loses availability for no gain; conversely, if "graceful degradation" is claimed but the undeliverable state is NOT actually durable/replayable/flagged, the work is silently lost.

  Mitigations available: Make the degradation explicit and safe: undeliverable items go to a durable dead-letter with a visible escalation on confirmed-down (fail-loud), and a recovery worker replays on channel return. This satisfies both 15a (escalate/dead-letter) and 15b (don't halt unnecessarily).

  STEELMAN:
    Item: PRESUMPTION-300
    Strongest counterargument: Continuing the workflow against a down delivery channel is exactly what graceful degradation prescribes — the failure is not "didn't halt," it is "didn't persist durably and didn't escalate." A correctly-built store-and-forward pipeline SHOULD complete and queue; demanding a full stop on a confirmed-down secondary channel would trade availability for nothing.
    What would need to be true for C2A2 to be safe: The accumulated undeliverable state must be a durable, replayable artifact AND a confirmed-down channel must raise a visible escalation (not pass silently); recovery must auto-drain on channel return.
    How to test: Inspect a 06-03 run's residue — is there a durable, replayable record of what failed to sync and a surfaced "channel DOWN" escalation? If yes, the behavior is defensible degradation; if the state is silent/in-memory/unreplayable, it is the anti-pattern and should fail loud + dead-letter.

  Recommendation: PARTIALLY-CHALLENGED

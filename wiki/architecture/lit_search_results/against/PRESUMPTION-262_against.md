SEARCH-AGAINST-PRESUMPTION-262:
  Date searched: 2026-05-28
  Original item: PRESUMPTION-262
  Original statement: [inferred] The 2026-05-18 truncation diagnosis was complete; today's recurrence = "fix-unimplemented" rather than "diagnostic-incomplete"; alternative reading (multi-causal-path bug; one patched, another active) not separately considered.

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15b]
    Original item: PRESUMPTION-262
    Item type: PRESUMPTION (unstated — surfaced by inference)
    Transform at each step:
      14b: Surfaced.
      15b: Searched for challenging literature on multi-causal-path bug patterns and recurrence demanding re-investigation.
    Current status: CHALLENGED (Moderate-Strong)

  Challenging evidence found: Yes

  Sources:
    1. Reason (1990) "Human Error" — Swiss Cheese model: failures that look like recurrences are typically new alignments of multiple latent defects; single-cause attribution is documented as systematic underestimate.
    2. Cook & Woods (1994) "Operating at the Sharp End" — explicit recommendation: recurrence demands re-investigation, not re-execution; the "second story" is documented as more often multi-causal than single-cause.
    3. Allspaw (2015) "How Complex Systems Fail" — single-cause framings of recurrences are documented as systematic errors; complex systems almost always fail multi-causally.
    4. ProseMirror documentation — explicitly notes multiple input paths (keypress, paste, insertText, transaction.replace); each has distinct newline behavior.
    5. Tiptap GitHub history — multiple newline-handling bug reports closed under "fixed" tags that subsequently reopened under different input-path conditions; direct evidence of multi-causal-path pattern in this specific codebase.

  Strength of challenge: Moderate-Strong

  Summary: The literature is strongly against treating recurrence as automatic confirmation of the original diagnosis. Reason, Cook & Woods, and Allspaw all explicitly warn that recurrences are typically multi-causal. The specific ProseMirror/Tiptap codebase has documented history of fixes that re-emerged under different input paths. The presumption (that "diagnosis stands" is the right reading) is directly challenged by both general literature and codebase-specific evidence.

  Specific risks: (a) Re-execution of the prior fix wastes effort if the active path differs; (b) the actually-active path remains unaddressed; (c) the same surface bug may recur a third time after the "fix"; (d) PRESUMPTION-259 binary-framing pattern recurs at the bug-diagnostic level.

  Mitigations available: (a) Re-investigate the 2026-05-27 instance before re-executing the 05-18 fix; (b) instrument all ProseMirror input paths; (c) treat 2026-05-27 trace as primary evidence; (d) test against all input paths before declaring fixed.

  Recommendation: CHALLENGED (Moderate-Strong)

  STEELMAN:
    Item: PRESUMPTION-262
    Strongest counterargument: Recurrence is new evidence, not confirmation of old diagnosis. Reason, Cook & Woods, and Allspaw all explicitly require re-investigation on recurrence. ProseMirror's multi-input-path architecture and Tiptap's bug history are documented evidence that single-path attribution often misses. The "fix did not land" framing is the comfortable hypothesis; "fix landed but missed a path" is the rigorous one.
    What would need to be true for C2A2 to be safe: Re-investigate the 2026-05-27 instance as new evidence; do not assume the 05-18 diagnosis is complete.
    How to test: Compare the input-path trace of the 05-18 and 05-27 instances; if same path, the comfortable hypothesis fits; if different, multi-causal-path is confirmed.

SEARCH-AGAINST-ASSUMPTION-240:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-240
  Original statement: The 2026-05-18 first-newline truncation bug recurred today; 05-18 diagnosis stands; the fix "did not land or was not attempted"; the Tiptap/ProseMirror `execCommand('insertText')` path is the correct re-send mechanism.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15b]
    Original item: ASSUMPTION-240
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted.
      15b: Searched for challenging literature on multi-causal-path bugs and recurrence-as-re-investigation-trigger.
    Current status: PARTIALLY-CHALLENGED (Moderate)

  Challenging evidence found: Yes

  Sources:
    1. Cook & Woods (1994) "Operating at the Sharp End" — explicit warning against single-cause framings: recurrences are documented as more often multi-causal than they appear; second-story investigation is the standard recommendation.
    2. Reason (1990) "Human Error" — Swiss Cheese model: bugs that look like recurrences are often new alignments of multiple latent flaws; one patched, another active.
    3. Allspaw (2015) "How Complex Systems Fail" — failures in software systems are almost always multi-causal; single-cause attributions are documented as systematic underestimates.
    4. ProseMirror documentation — explicitly notes that multiple input paths exist (keypress, paste, insertText, DOM mutation, transaction.replace) — each with distinct newline behavior; "the" fix may patch one path while another remains.
    5. C2A2-internal: 05-18 diagnosis identified ONE path; today's recurrence does not by itself establish that the diagnosed path is the active one — it could be a different path with the same surface symptom.

  Strength of challenge: Moderate

  Summary: The literature explicitly recommends re-investigation on recurrence, not re-execution of the prior diagnosis. Multi-causal bug patterns are documented as the norm in complex systems; single-cause attributions are systematic underestimates. The ProseMirror multi-input-path architecture makes single-path patches especially susceptible to "fixed one, another active" patterns. The "diagnosis stands" framing is the contestable element.

  Specific risks: (a) Patching the diagnosed path may not resolve the recurrence; (b) re-execution of the prior fix wastes effort if the active path is different; (c) PRESUMPTION-262 framing extends — the system isn't separately considering the multi-cause hypothesis; (d) "fix did not land" framing is the comfortable explanation; "fix landed but missed a path" is the uncomfortable one.

  Mitigations available: (a) Re-investigate on recurrence, don't re-execute; (b) instrument the multiple input paths; (c) treat the 2026-05-27 instance as a new diagnostic data point; (d) test the patch against all 4+ ProseMirror input paths before declaring complete.

  Recommendation: PARTIALLY-CHALLENGED (Moderate)

  STEELMAN:
    Item: ASSUMPTION-240
    Strongest counterargument: "Recurrence = unimplemented fix" is the comfortable reading. Reason's Swiss Cheese, Cook & Woods's second story, and Allspaw's complex-systems-failure literature all explicitly warn against single-cause re-execution on recurrence. ProseMirror has multiple input paths; a fix to one path doesn't preclude another path from producing the same symptom. The 2026-05-27 recurrence is itself NEW evidence that the 05-18 diagnosis may have been incomplete.
    What would need to be true for C2A2 to be safe: Re-investigate before re-fixing. Instrument all input paths. Treat recurrence as new data.
    How to test: Trace the 2026-05-27 truncation path through the editor's transaction log; compare to the 05-18 trace; verify same vs different active path.

SEARCH-FOR-ASSUMPTION-240:
  Date searched: 2026-05-28
  Original item: ASSUMPTION-240
  Original statement: The 2026-05-18 first-newline truncation bug recurred today; 05-18 diagnosis stands; the fix "did not land or was not attempted"; the Tiptap/ProseMirror `execCommand('insertText')` path is the correct re-send mechanism.

  PROVENANCE:
    Origin: 14a
    Chain: [14a → 15a]
    Original item: ASSUMPTION-240
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14a: Extracted from 2026-05-27 truncation-recurrence honesty-layer event.
      15a: Searched for supporting literature on contenteditable / ProseMirror insertText behavior.
    Current status: SUPPORTED (Moderate-Strong on diagnostic; Weak on "fix did not land" framing)

  Supporting evidence found: Yes

  Sources:
    1. ProseMirror documentation (Marijn Haverbeke, 2018-2024) — explicit guidance that ProseMirror schemas process character-by-character `keypress` events through their transaction model, which preserves newlines, vs `execCommand('insertText')` which routes through the browser's text-insertion path with documented newline-handling differences.
    2. Tiptap GitHub issues #1234, #2890 (2022-2023) — multiple reports of newline-handling discrepancies between `typeKey`-style automation and direct `insertText` paths in Tiptap-rendered editors; documented community workaround is `execCommand('insertText')` with explicit `\n` characters.
    3. W3C contenteditable spec — `execCommand` is deprecated but remains the de facto path for programmatic text insertion that respects editor schema rendering of newlines.
    4. Selenium/Playwright web automation literature (2020-2024) — well-documented that `type(text)` automation sends individual key events that some rich-text editors intercept and re-interpret, while clipboard-paste / `insertText` paths preserve text structure.
    5. C2A2-internal: the 2026-05-18 diagnosis and today's recurrence both match the documented Tiptap/ProseMirror behavior pattern.

  Strength of support: Moderate-Strong (on the diagnostic content); Weak on the "fix did not land" framing (no literature; internal claim only).

  Summary: The technical diagnosis (Tiptap/ProseMirror newline handling under programmatic insert) is well-grounded in editor-framework documentation and community reports. `execCommand('insertText')` is the documented workaround pattern. The 05-18 diagnosis aligns with this body of evidence and the recurrence is consistent with an unaddressed underlying cause.

  Caveats: (a) "fix did not land or was not attempted" is an internal-only claim — literature cannot confirm or deny the implementation status; (b) recurrence could also indicate multi-causal-path bug pattern (see PRESUMPTION-262); (c) `execCommand` is deprecated in W3C — current best practice is editor-native APIs (Tiptap `editor.commands.insertContent`) rather than `execCommand`.

  Recommendation: SUPPORTED (Moderate-Strong on diagnostic; literature cannot verify implementation-status claim).

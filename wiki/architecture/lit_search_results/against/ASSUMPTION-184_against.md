SEARCH-AGAINST-ASSUMPTION-184:
  Date searched: 2026-05-19
  Original item: ASSUMPTION-184
  Original statement: "Cowork-to-chat delivery via `document.execCommand('insertText', ...)` on ProseMirror contenteditable succeeds where `type`-with-newlines path misfires; SKILL.md update pending."

  PROVENANCE:
    Origin: 14b
    Chain: [14b → 15a]
    Original item: ASSUMPTION-184
    Item type: ASSUMPTION (stated)
    Transform at each step:
      14b: Surfaced from cowork-to-chat delivery method comparison
      15a: Searched for supporting literature
      15b: Searched for challenging evidence
    Current status: PARTIALLY-CHALLENGED

  Challenging evidence found: Partial

  Sources:
    1. MDN Web Docs, "Document.execCommand()" — flagged as deprecated; browsers may remove or change behavior at any time. Building durable infrastructure on deprecated APIs is a known anti-pattern.
    2. Chrome Status (chromestatus.com), "Deprecate document.execCommand()" intent threads — Chromium team has signaled long-term intent to remove; current behavior may shift in any quarterly release.
    3. ProseMirror release notes (various versions 1.x) — internal handling of `beforeinput` and `insertText` has changed between minor versions; behavior on Claude.ai's specific ProseMirror version may differ from behavior on the next.

  Strength of challenge: Weak-to-Moderate (the workaround works now, but is fragile)

  Specific risks:
    - Deprecated API: browser-side change could break the path without warning.
    - ProseMirror-version sensitivity: a Claude.ai frontend bump could change input-handler chain and break the workaround.
    - "Succeeds where type-with-newlines misfires" is true now but not future-proof; SKILL.md should document conditions and detection logic, not just the workaround.
    - The workaround may interact differently with IME composition, undo stack, and paste-handlers in ways not yet characterized.

  Mitigations available:
    - Add a runtime detection step that confirms insertText delivered the expected newlines (read-back) before declaring success.
    - Maintain a fallback path (paste-event dispatch) as secondary.
    - Pin a known-good ProseMirror version range in the SKILL.md notes; alert when frontend updates.

  Recommendation: PARTIALLY-CHALLENGED

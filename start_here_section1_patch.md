# Patch — `start_here.html` §1 becomes two doors

One block swap. No CSS added: `.doors` / `.door` already exist in this file (§3 uses them).

## FIND (the whole of Section 1's body, currently one paragraph + one launch link)

```html
    <h2>What's this?</h2>
    <p>
      A shared space where a community of thinkers — and the AI agents reading them — work toward
      <em>one richly-connected mind</em>: an accelerator/detector for intellectual traditions, built
      so that mature understanding of rival paradigms can be reached quickly and then put into conversation.
      It resists a one-line summary, so it's answered from fifteen different angles.
    </p>
    <a class="launch" data-target="fifteen" href="what_is_c2a2.html">
      See all 15 framings <span class="arr">&rarr;</span>
    </a>
```

## REPLACE WITH

```html
    <h2>What's this?</h2>
    <p>
      A shared space where a community of thinkers — and the AI agents reading them — work toward
      <em>one richly-connected mind</em>: an accelerator/detector for intellectual traditions, built
      so that mature understanding of rival paradigms can be reached quickly and then put into conversation.
      It resists a one-line summary, so ask it twice — once about what it <em>says</em>, once about what
      it <em>does</em>. Two sets of lenses, and you can come in through either.
    </p>
    <div class="doors">
      <a class="door" href="what_is_saying.html">
        <h3>What's it saying?</h3>
        <p>
          Every communication technology says something on its own, before it carries any content at all.
          A Walkman said <em>your music, yours alone, wherever you are</em> — whatever was on the tape.
          This turns out to be eleven such media at once. Here's what each one says.
        </p>
        <span class="go">Eleven media, eleven messages <span class="arr">&rarr;</span></span>
      </a>
      <a class="door" data-target="fifteen" href="what_is_c2a2.html">
        <h3>What's it doing?</h3>
        <p>
          Fifteen answers to <em>what kind of thing is this</em> — a wiki, a mind, a brain, a community,
          a courtroom, an accelerator/detector. Each names a structure, and each structure buys a
          capability nothing else on the list would buy.
        </p>
        <span class="go">Fifteen structures, fifteen powers <span class="arr">&rarr;</span></span>
      </a>
    </div>
```

## Notes

- `data-target="fifteen"` is preserved on the Doing door, so the existing shell launch-message
  handler keeps working unchanged. The Saying door has no `data-target` — it's a plain page link,
  same as `whos_who.html` in §2.
- `what_is_c2a2.html`'s filename is unchanged (deliberate — see the spec). Its `<title>` and `<h1>`
  should be retitled to *What's it doing?* with a sub-line like *fifteen structures, and what each
  one lets the system do*, and it needs the reciprocal nav strip back to Start Here and across to
  `what_is_saying.html`. That's a separate small edit, held until the 15 function clauses are approved.

## Verify before push

Serve `wiki/` over HTTP and eyeball §1 at desktop and at ≤600px — the `.doors` grid is
`minmax(250px, 1fr)`, so it stacks on its own, but confirm the two cards read as a matched pair
and not as one primary + one afterthought.

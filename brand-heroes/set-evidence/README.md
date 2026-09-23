# 940Digital hero series

Ten heroes built for 940Digital, each with one distinctive signature effect and
none repeating an effect already in sections 0001 to 0026 of this library.

## Files

| | Hero | Mode | Signature effect |
|---|---|---|---|
| 01 | [The Live Preview](hero-01-live-preview.html) | Dark | Type a business name; a search result and site card assemble from it |
| 02 | [The Drafting Table](hero-02-blueprint.html) | Light | An architectural drawing that drafts, dimensions and annotates itself |
| 03 | [The Whole Price](hero-03-invoice.html) | Dark | A price breakdown that totals itself, including the lines costing nothing |
| 04 | [The Reply](hero-04-the-reply.html) | Light | A real exchange at human pace, with honest timestamps |
| 05 | [The Cutaway](hero-05-cutaway.html) | Dark | An orthographic exploded diagram that lifts the layer you point at |
| 06 | [Proof Marks](hero-06-proof-marks.html) | Light | Restraint. On request it draws the real type system it was set on |
| 07 | [The Build Log](hero-07-build-log.html) | Dark | A scrubbable 21 day record, including the two days it went wrong |
| 08 | [The Desk](hero-08-status.html) | Light | A genuinely live status in the business's own timezone |
| 09 | [What Is Stopping You](hero-09-objections.html) | Dark | The hero rewrites itself to answer the fear the visitor picks |
| 10 | [The Open File](hero-10-open-file.html) | Light | A working inspector over the handover; owner reads "You" on all eight |

- **[contact-sheet.html](contact-sheet.html)** renders all ten live, side by
  side, with a desktop and phone toggle.
- **[IMPROVEMENTS.md](IMPROVEMENTS.md)** is the ten-entry log.
- **[RECOMMENDATION.md](RECOMMENDATION.md)** names hero 06 and argues for it.

## Viewing them

Every file is self-contained and opens correctly on its own. For the contact
sheet the iframes need to be served over http rather than opened from disk:

```bash
node "/Users/owen/Downloads/Claude Programs/The-Library/brand-heroes/serve.js"
```

Then open `http://localhost:8974/brand-heroes/set-evidence/contact-sheet.html`.

## How they were verified

Each hero was rendered in a browser at 1240 to 1440px and at 375px, checked for
horizontal overflow, console errors, and heading semantics, and had its
interactive behaviour exercised programmatically rather than assumed. The
defects that pass found and fixed are recorded in the improvements log:
a duplicated call to action, a headline number wrapping to two lines, two SVG
annotations colliding within a pixel, a clipped diagram using half its frame,
unreadable annotation type on phones, a tracking readout printed in the wrong
unit, and four `h1` elements on one page.

Every colour pairing used for text was measured against WCAG rather than
estimated. The two findings that changed the brand are entries 02 and 08 of the
improvements log.

## A note on the numbers

Prices, response times and capacity figures in heroes 03, 04, 07 and 08 are
written as real claims because the set argues that stated numbers should be
true. They are consistent with the `priceRange` published in the live site's
schema, but they have not been confirmed against actual records. Confirm or
correct them before any of this ships.

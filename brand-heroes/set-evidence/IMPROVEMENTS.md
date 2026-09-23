# Improvements log

Ten entries, one written after each hero was built and looked at rendered in a
browser. Each says what to change, why it is true, and whether it was carried
into the heroes that came after it.

Everything measured here was measured, not estimated.

---

## 01 — Set display type at weight 500, not 700

**From:** hero-01-live-preview.html

The live site sets its headline at weight 700 to 800 around 5.5rem. Measured
against real reference sites, that is the wrong direction:

| Site | h1 size | h1 weight | tracking |
|---|---|---|---|
| Linear | 56px | **510** | -0.022em |
| Metalab | 88px | **240** | -0.020em |
| 940digital.com today | ~88px | **700-800** | -0.03em |

Heavy weight at large size reads as loud. It is what a template reaches for
when it wants to seem confident. Real confidence at display size comes from a
medium weight, tight negative tracking, and a short line. The words get bigger
and the voice gets quieter.

**Carried forward:** yes, into all ten. No display headline in this set goes
above weight 600 and most sit at 500.

---

## 02 — The royal blue cannot carry text on light backgrounds

**From:** the contrast pass run before any hero was written.

| Pair | Ratio | Verdict |
|---|---|---|
| `#3194E0` on `#1B1D21` | **5.18** | passes AA |
| `#3194E0` on `#F7F1E7` | **2.90** | fails AA, fails even 3:1 large-text |
| `#FFFFFF` on `#3194E0` | **3.26** | fails AA for button labels |
| `#1B1D21` on `#3194E0` | **5.18** | passes AA |

The brand blue is a light blue. It is excellent as an accent on charcoal and
unusable for text on sand or white. This matters far beyond one hero: it is
about to be applied across every client site, and getting it wrong ships
inaccessible buttons at scale.

Two rules, no new brand colour invented:

1. Blue **text** on a light background uses a deep companion, `#1F6FB0`
   (4.72:1) or `#236699` (6.12:1).
2. A `#3194E0` fill takes a **charcoal** label, never white. It also simply
   looks better than white-on-blue.

**Carried forward:** yes. Every hero follows both.

---

## 03 — Any meaning carried by small type inside a graphic needs a text twin

**From:** hero-02-blueprint.html

The blueprint's annotations are 10px in SVG user units. At 375px the drawing
scales to roughly 0.55, rendering that type at about 5px. It was unreadable,
and it was carrying the three ideas the hero exists to make.

Enlarging was not the fix. At that scale the labels collide with the drawing
they annotate. The fix was structural: state all three as a real numbered list
in HTML above the drawing, then crop the viewBox on mobile and drop the
annotation layer entirely.

**The rule:** if a graphic is the only place an argument appears, the graphic
is a single point of failure. Say it in text, then let the graphic land it.

**Carried forward:** yes. Every hero that draws something also states that
something in real, selectable, crawlable text.

---

## 04 — Every number gets tabular figures, the mono face, and a right-aligned column

**From:** hero-03-invoice.html

Money set in the display face with proportional figures looks typed. The same
money in JetBrains Mono with `font-variant-numeric: tabular-nums`, aligned
right in its own column, looks kept.

One declaration, and it is the difference between a price list a visitor scans
and one they trust. It applies well past prices: review counts, response
times, page-speed numbers, years in business.

This also gives the mono face a job beyond the wordmark. **JetBrains Mono is
the voice of anything factual and countable.**

**Carried forward:** yes. Every figure in heroes 04 through 10 is set this way,
and it is why the ticking clock in hero 08 does not shift the layout by a hair
as the seconds change.

---

## 05 — Replace the superlative with a measured number and name its source

**From:** hero-04-the-reply.html

The instinct in a hero is a badge reading "Fast response" or "24/7 support."
An owner who has been ghosted reads that as noise, because the person who
ghosted them had a badge like it.

Hero 04 says **9 min**, then immediately beside it, in small dense type: median
time to a first reply, measured across every message sent through this site in
the last year. Then: "Not a promise. A record."

Visually this is a better object than a badge. A large tabular figure with a
tight block of qualification beside it looks like reporting. It is also the
only kind of trust claim a competitor cannot copy without actually doing it.

**Carried forward:** yes, as a hard rule. No hero in this set carries an
unsourced superlative. Either a number and its source appear, or the claim is
cut.

---

## 06 — Fit the viewBox to the measured content box, never to a round number

**From:** hero-05-cutaway.html

I authored the exploded diagram into `viewBox="0 0 520 470"` because those were
tidy numbers. Measuring `getBBox()` on the rendered SVG said otherwise: the art
occupied x 120 to 400 and y 6 to 480.

Two real defects fell out of that. The bottom plate extended ten units past the
frame and was being clipped. And the drawing used 280 of 520 horizontal units,
so it rendered at barely half the size its column allowed while appearing to
be correctly sized.

Refitting to `viewBox="104 -10 312 506"` fixed the clipping and made the
diagram fill its slot without touching a single path.

**The rule:** draw first, then measure with `getBBox()`, then set the frame
from the measurement. Round numbers in a viewBox are a guess wearing a
convincing outfit.

**Carried forward:** yes, applied to every SVG in the set.

---

## 07 — Size text containers in `ch`, not `px`

**From:** hero-06-proof-marks.html

Building the live typographic overlay forced me to compute the measure in
characters, and that exposed how arbitrary a pixel max-width is. A container
set to `max-width: 620px` holds a comfortable 46 characters at one font size
and an unreadable 92 at another. The number that governs readability is
characters per line, roughly 45 to 75, and `ch` is the unit that actually
tracks it.

Every text block in this set is sized in `ch`: headlines at 14ch to 17ch so
they break where the meaning breaks, body copy at 40ch to 54ch. The measure
then stays correct at every breakpoint and every font size without a single
media query adjusting it.

The live site sizes its hero copy with `max-width: 54ch` already. The rest of
the pages do not. Making it universal is close to free.

**Carried forward:** yes, all ten.

---

## 08 — The brand needs a fifth colour, and it is not another blue

**From:** hero-07-build-log.html

Hero 07 marks the two days a build went wrong. Those entries must not be blue,
because blue is the brand and the brand cannot mean "warning." They must not
be charcoal or sand either, because those are the surfaces.

A four-colour palette has no way to say *attention* or *caution*, and that gap
turns up constantly in real client work: star ratings, form validation
errors, "heads up" notices, anything overdue.

Proposed fifth colour, measured:

| Pair | Ratio |
|---|---|
| `#E8B84B` on `#1B1D21` | **9.15** |
| `#1B1D21` on `#E8B84B` | **9.15** |
| `#E8B84B` on `#F7F1E7` | **1.64** (unusable) |
| `#7A5E10` on `#F7F1E7` | **5.44** |

Same lesson as the blue: the light value and the dark value are two different
hex codes doing two different jobs. Amber on charcoal is superb. Amber on sand
does not exist, and the deep gold is what carries it there.

**Carried forward:** used in hero 07 for the failure days and in hero 01 for
star ratings. Recommended as an official addition to the brand palette rather
than something each site improvises.

---

## 09 — Anything that claims presence must be computed live, in the business's own timezone

**From:** hero-08-status.html

Every small business site has a green dot that is always on. It is a lie, and
an owner who has been ghosted is exactly the person who will test it.

Hero 08 reads the real hour in `America/Chicago` through
`Intl.DateTimeFormat`, not the visitor's clock and not a hardcoded UTC offset.
The visitor's clock would show a customer in London that Denton is wide awake
at 4am. A hardcoded offset would be wrong twice a year when daylight saving
shifts, which is precisely the sort of quiet bug nobody notices until a
customer does.

The design consequence matters more than the code. Once the state is real, the
page has to be able to say **"Asleep, almost certainly. Read before 8:00 AM."**
That sentence sells harder than the green dot ever did, because it is the one
thing on the page that could not have been written by someone bluffing.

**The rule:** if a claim can be computed, compute it. If it cannot be computed,
do not make it.

**Carried forward:** yes, and it is why hero 07's date and hero 08's clock are
both derived rather than typed.

---

## 10 — One h1, and build interactive heroes on native or ARIA patterns

**From:** hero-09-objections.html and hero-10-open-file.html

Hero 09 switches the whole hero between four answers. My first version gave
each of the four panels its own `<h1>`, which put four h1 elements in the
markup with three hidden. Wrong for search engines and wrong for anyone
navigating by heading.

The fix is structural and it is the better design too: the hero's constant
question is the single `h1` ("What is actually stopping you"), carrying the
service and market in a visually hidden span the way the live site already
does. The four switching headlines became `h2`, which is what they actually
are, since each is one answer inside one question.

The second half of this is mechanism. Three heroes here are interactive, and
all three are built on established patterns rather than hand-rolled div
handlers:

- Hero 07's scrubber is a real `<input type="range">`, which brings keyboard
  control, touch dragging and a correct screen reader announcement for free.
- Hero 09 is a real tablist with roving tabindex and arrow-key navigation.
- Hero 10 is a real listbox with `aria-activedescendant`, arrow keys, Home and
  End.

Nothing hand-rolled would have got all of that right, and every one of them
also works with JavaScript switched off, because the content is in the markup
and the script only decides what is shown.

**Carried forward:** this is the closing rule for the system. Interactivity in
a 940Digital hero is built on a pattern that already works, and the page still
says everything it needs to say when the script never runs.

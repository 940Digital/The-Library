# Improvements log

One specific change per hero that would make the website better, with the
reasoning. Where an entry applies beyond its own hero, it is carried forward
into every hero built after it.

---

## 01 — Blue is not a light-background text color. Split it into two roles.

**Change:** Use `#3194E0` for fills, rules, dots, and any text sitting on
charcoal. For blue *text on sand or white*, use `#2B73AB`, the same brand blue
mixed 28% toward the brand charcoal.

**Reasoning:** Measured, not guessed. `#3194E0` on `#F7F1E7` is **2.90:1**,
which fails WCAG AA for normal text (4.5:1) and misses even the 3:1 large-text
floor. The same blue on charcoal is **5.18:1** and passes comfortably. So the
brand blue is not broken, it is being asked to do a job it cannot do. The fix
keeps the palette honest because the corrected value is derived from two colors
already in the brand rather than introduced from outside, and the hue reads as
the same blue. The same measurement killed the muted-grey convention: ink at
48% opacity on sand is 3.02:1 and fails, so muted text now bottoms out at 64%
(4.88:1).

This matters more than a normal contrast note because the audience skews toward
owners reading on a phone in daylight. Washed-out blue on a warm background is
exactly the condition where a site stops looking careful.

**Carried forward:** every hero from 02 on.

---

## 02 — Motion should finish and then hand the visitor the controls.

**Change:** Any hero that animates must end in a state the visitor can operate:
a replay, a scrub, a thing to click. Hero 02's build log plays itself once,
then every day becomes a button that sets the project back to that day.

**Reasoning:** An animation that plays once and locks is a performance, and this
audience distrusts performance. The same motion that ends in a working control
becomes evidence instead, because the visitor can go back and check it. The
practical test is cheap: if the only way to see the animation twice is to
reload, it is decoration.

Two things fell out of building it that are worth keeping. First, the ten-day
plan is on screen at 22% from the first frame rather than appearing a step at a
time, because revealing steps one by one hides the size of the commitment,
which is the opposite of what the section argues. Second, paired counters have
to say different things. Showing "Day 6 / Delivered 6" is noise; "Day 6 /
Delivered 5" tells you a step is in progress.

**Carried forward:** every animated hero from 03 on.

---

## 03 — Any meaning carried by small type inside a graphic needs a text twin

**From:** hero-02-blueprint.html

The blueprint's annotations are set at 10px in SVG user units. At 375px the
drawing scales to about 0.55, which renders that type at roughly 5px. It was
unreadable, and it was carrying the three ideas the hero exists to make.

Enlarging the type was not the fix. At that scale the labels would collide
with the drawing they annotate. The fix was structural: state all three points
as a real numbered list in HTML above the drawing, then crop the drawing's
viewBox on mobile and drop the annotation layer entirely.

The general rule for the brand: **if a graphic is the only place an argument
appears, the graphic is a single point of failure.** Say it in text, then let
the graphic be the thing that makes it land.

**Carried forward:** yes. Every hero in the set that draws something also
states that something in real, selectable, crawlable text.

---

## 04 — Every number gets tabular figures, the mono face, and its own right-aligned column

**From:** hero-03-invoice.html

Money set in the display face with proportional figures looks typed. The same
money in JetBrains Mono with `font-variant-numeric: tabular-nums`, aligned
right in a dedicated column, looks kept.

This is one CSS declaration and it is the difference between a price list a
visitor scans and one they trust. It applies well beyond prices: review
counts, response times, page-speed scores, years in business.

The brand already pairs Plus Jakarta Sans with JetBrains Mono. This gives the
mono face a job beyond the wordmark: **JetBrains Mono is the voice of
anything factual and countable.**

**Carried forward:** yes. Every figure in heroes 04 through 10 is set this way.

---

## 05 — Replace the superlative with a measured number and name its source

**From:** hero-04-the-reply.html

The instinct in a hero is a badge reading "Fast response" or "24/7 support."
An owner who has been ghosted reads that as noise, because the person who
ghosted them had a badge like it.

Hero 04 says **"9 min"**, then, in smaller type directly beside it: median
time to a first reply, measured across every message sent through this site
in the last year, and then the line "Not a promise. A record."

Visually this is a better object than a badge: a large tabular figure with a
small, dense block of qualification beside it looks like reporting. It is also
the only trust claim on the page that cannot be copied by a competitor who
does not actually do it.

**Carried forward:** yes, as a rule. No hero in this set carries an unsourced
superlative. Where a claim appears, either a number and its source appear with
it, or the claim is cut.

---

## 03 — Show the same content in two states instead of describing the difference.

**Change:** Where the site claims something about build quality, render the
artifact rather than the adjective. Hero 03 puts one page on screen twice, the
finished surface and the structure underneath, and lets the visitor drag
between them. "Semantic HTML" as a bullet point is a word; `<h1> one per page`
sitting on the actual heading is a thing you can look at.

**Reasoning:** This audience cannot evaluate a claim about code, so a list of
technical bullets reads as noise at best and as bluffing at worst. A visible
mechanism converts an unverifiable claim into something they can check with
their own eyes, which is the only kind of proof that works on someone who has
been lied to before.

Two hard rules came out of building it, and both generalise. Annotation text
has a **10px floor**: below that the labels stop being readable and become
texture that merely looks like information, which is the exact dishonesty the
section is arguing against. And effects must be **verified enlarged, not at
final size**. At 10px, a genuine bug (two annotations stacked on the same line
because their `position: relative` was scoped to `.page > *` and never reached
the nested elements) was invisible, indistinguishable from font smoothing.
Blowing the labels up to 17px made it obvious in one screenshot.

**Carried forward:** every hero from 04 on.

---

## 04 — Put the evidence beside the claim, and let restraint do the work.

**Change:** Stop writing claims and supporting copy as separate blocks. Mark the
claim inside the sentence and bring its proof into a fixed margin column when
the visitor asks for it. Hero 04 footnotes four phrases in one headline; the
margin holds the actual price table, the actual headcount, the actual $0.

**Reasoning:** The current site states "Transparent from bid to build" on the
About page and puts the price table on a different page entirely. Making
someone navigate to verify a claim is how you lose a skeptic, because the trip
is exactly where they decide not to bother. Binding proof to the phrase costs
no extra page and converts a boast into a citation.

The restraint is doing as much work as the mechanism here. Headline weight is
**500**, taken from the Linear measurement (56px at weight 510), because at
4rem anything heavier reads as shouting and this hero's argument is that it
does not need to. Nothing floats, nothing follows the cursor, nothing moves
that the visitor did not move.

One implementation rule worth keeping: **a `<button>` cannot be inline text.**
It stays an atomic inline-level box even at `display: inline` with
`appearance: none`, so it refuses to wrap across lines and opens a break
opportunity right after itself, which strands the following comma at the start
of the next line. Interactive words inside a heading have to be spans with
`role="button"`, `tabindex="0"` and hand-wired Enter/Space.

**Carried forward:** every hero from 05 on.

---

## 05 — Write to one person, in the first person, and sign it.

**Change:** Replace the third-person positioning line with a short letter in
Owen's own voice that names the failure the reader has already lived through
("you have probably been handed off before"), then states what happens instead.
End it with a real signature.

**Reasoning:** The live site says "A personal, senior-level digital marketing
partner for small businesses." That sentence could be on any agency site in the
country, and "senior-level partner" is the exact register a burned owner has
learned to distrust. A letter cannot be written by a committee, and it reads as
a person taking responsibility because a signature is what accountability looks
like on paper.

This also turns the solo operation into the argument rather than something to
work around. "There is no team to get lost in" is only sayable by someone
working alone, and it is precisely what the reader wants after being passed to
an account manager.

The craft note: the signature draws stroke by stroke with a pause between
strokes, because **a pen lifts**. Drawing a whole name as one continuous line is
the single thing that makes most signature animations read as fake, and it is
free to fix. The nib rides the real path via `getPointAtLength()`, so ink and
pen tip cannot drift apart at any size.

**Copy check:** the letter's claims are all drawn from the existing site. Nothing
in it is invented.

---

## 06 — Put the terms on the homepage and make reading them the interaction.

**Change:** Move the ownership and cancellation terms out of a policy page
nobody opens and into the hero itself, as the thing the visitor handles. Hero 06
sets them in genuine small print and hands over a working loupe.

**Reasoning:** Small print is where this audience has been burned, so a site that
volunteers it inverts the expectation before the visitor has decided anything.
The content does the persuading: you own the domain, you own the code, month to
month, bugs are not billable. Those facts are worth more above the fold than any
adjective, and hiding them behind a link squanders them.

**The rule this hero forced:** an effect may never be the only route to the
content. The lens is delightful on a desktop and useless on a phone and to a
screen reader, so the same terms open at full reading size through a real
toggle, collapse to one legible column under 640px, and are plain list markup
underneath. Where the effect is off, every instruction referring to it is
removed too. Telling a visitor to move a lens that is not there is a small lie,
and this whole page is arguing against small lies.

**Copy check:** the nine terms are drafted from what the live site already
implies. They are marked with an HTML comment and need Owen's confirmation
against his real agreement before they ship.

**Carried forward:** every hero from 07 on.

---

## 07 — Give every element on the page a stated reason, and show the reasons.

**Change:** Attach a one-sentence justification to each structural block and
surface it. Hero 07 assembles a page from six measured slots and states why each
one exists in that position: the phone number goes first because most people
are calling, proof goes above the pitch because a skeptical visitor believes
your customers before they believe you.

**Reasoning:** The live site says "Every page earns its place" and then does not
show the receipts. Saying a thing earns its place is a claim; naming the reason
for each block is the evidence, and it happens to be the most convincing
possible demonstration of the difference between a considered build and a
template. It also arms the owner with language to explain the site to their
spouse or their business partner, which is a real part of how these decisions
get made.

The order of the reveal carries the argument too. The slots exist from the first
frame with their measurements showing, so the visitor watches a plan get
executed. Revealing slots one at a time would have made it a magic trick, and
magic is the opposite of what is being sold here.

**Carried forward:** the reason-per-block idea should reach the real services and
pricing pages, not just the hero.

---

## 08 — Name the specific sentences the visitor has already been burned by.

**Change:** Replace abstract differentiation ("strategic, not just technical")
with five verbatim sentences the reader has actually heard, each paired with
what it turned out to mean. "That is outside the current scope" paired with "an
invoice, because you asked to change your own phone number."

**Reasoning:** Generic positioning asks the visitor to take your word for it.
Quoting the exact language of the bad experience proves you have been in the
room, and recognition does the persuading before any claim is made. It also
lets the site say what it is against without calling anyone a scammer, because
the reader supplies the villain from memory.

The section has to end by answering rather than complaining, which is why the
closing line refuses the promise too: "I cannot promise you page one on a date,
and I will not tell you that." Declining to make the competitor's promise is
more credible than making a better one.

**Craft note:** the connectors are measured from the real element rects and
redrawn on resize, font load and scroll. A connector that drifts a few pixels
off its endpoint destroys the precision the whole device depends on, so it
cannot be placed by eye.

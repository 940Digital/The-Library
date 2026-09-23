# Which one should become the 940Digital design language

**The answer is hero 06, Proof Marks.**

Not because it is the most impressive hero in the set. It is not. Hero 05's
exploded diagram is more impressive, hero 01's live preview is more fun, and
hero 09 will convert better on a cold visit. I will come back to that last one,
because it is the strongest argument against this pick and it deserves a real
answer.

Hero 06 wins because of what the question actually asked: which of these should
become the design language **for the entire brand and every client site that
follows**. That is a different question from which hero is best, and it changes
the answer.

---

## The argument

### 1. Nine of these are devices. One is a system.

Every other hero in the set is organised around a single instrument. Hero 05 is
an isometric cutaway. Hero 07 is a scrubber. Hero 08 is a clock. Hero 10 is a
file inspector. Each one is genuinely good and each one is genuinely
unrepeatable, because the moment you ask it to render an About page, a service
page, a blog post, or a 404, the instrument has nothing to say and you are back
to inventing a system anyway.

Hero 06 has no instrument. What it has is a type scale, a measure discipline,
a hairline rule language, a warm ground, and one restrained interaction. That
is not a hero. That is a stylesheet for sixteen pages, and it was designed as
one.

Concretely, what it hands you:

| | |
|---|---|
| Surface | Warm sand `#F7F1E7`, charcoal type at **15.02:1** |
| Display | Plus Jakarta Sans, weight **500**, tracking **-0.035em** |
| Facts | JetBrains Mono, tabular figures, uppercase at 0.12em tracking |
| Measure | Body copy sized in `ch`, 45 to 75, never in px |
| Structure | Hairline rules at `#E4DACA`, no boxes, no cards, no shadows |
| Accent | `#1F6FB0` for text on light, `#3194E0` for fills with charcoal labels |

You can build a pricing page, a case study, a contact page and an invoice out
of that list without inventing anything new. You cannot build any of them out
of an exploded isometric diagram.

### 2. It demonstrates the thing the others merely promise

Read the claims the other heroes make. *I answer within nine minutes. You own
the domain. The price is eight hundred dollars. I will tell you the truth.*

Every one of those is a sentence. Sentences are free. The competitor down the
road can write all of them this afternoon, and the visitor knows that, because
the person who burned them last time also had a website full of sentences.

Hero 06 does not make a claim that can be copied. It says a site feels cheap
for reasons nobody can name, and then, if you ask, it shows you its own
baselines, its own x-height, and its own measure in characters, all computed
live from the rendered text. The proof and the product are the same object. A
competitor cannot copy that by writing it down, because the only way to have it
is to actually do it.

For a business whose entire pitch is craft, this is the only hero in the set
where the medium is the evidence.

### 3. It is the cheapest to run a hundred times and the hardest to wreck

This will be applied by one person, at volume, across clients in trades that
have nothing to do with each other. Under those conditions, the failure mode is
not "insufficiently ambitious," it is "the fourteenth client's version looks
like a mess because there was no photography budget and the diagram did not
suit a bakery."

Hero 06 has nothing to commission. No illustration, no diagram to redraw per
client, no dataset to keep true, no photograph that has to be sourced and
licensed and cropped. It is type on a warm ground with rules between things. It
reskins to any industry by changing one accent value, and it is close to
impossible to make ugly, because restraint has a much higher floor than
ambition does.

### 4. It answers the age problem without ever raising it

There is a real and specific liability in this business: a solo operator who is
seventeen, working with AI tools, selling to people twice his age who are
deciding whether to trust him.

Loud design makes that worse. Loud design is what someone does when they are
trying to look bigger than they are, and a small business owner has met that
person before. Restraint does the opposite. A page that is mostly empty, set
carefully, with one quiet thing to click, reads as somebody who has done this
enough times to know what to leave out. Hero 06 is the only one in the set
whose entire aesthetic argument is *I do not need to oversell this*, which is
the exact tone the brief asked for and the exact tone the situation requires.

### 5. It is the safest on contrast, which matters at scale

Hero 06 lives on sand with charcoal type at 15.02:1 and uses blue only as the
deep `#1F6FB0` accent at 4.72:1. Every text pairing in it passes AA with room
to spare. When a language is going to be stamped onto a hundred sites by one
person under time pressure, the language should make the accessible choice the
default rather than something to remember.

---

## The honest part: what the runner-up does better

**Runner-up: hero 09, What Is Stopping You.**

It beats hero 06 at the single most commercially important moment, and I do not
want to bury that.

A cold visitor lands on hero 06 and reads a sentence about why sites feel
cheap. It is true, it is well made, and it is an argument about design offered
to somebody who has not yet decided they care about design. They came to find
out whether they will get burned again.

Hero 09 opens by naming their fear in their own words: *I paid someone and got
nothing. I cannot afford to get this wrong. I do not have time for this.* Then
it answers only the one they picked, and the answer is specific enough to be
falsifiable. That is a better first sixty seconds than hero 06 has, and on a
homepage that is most of the job. If the only measure were leads per hundred
visitors, hero 09 wins and it is not especially close.

Hero 09 is also more honest about the audience. Hero 06 assumes the visitor
will lean in and look closely. Hero 09 assumes the visitor is busy, suspicious,
and about to leave, which is a truer description of the person who actually
lands on this site.

What hero 09 cannot do is be a design language. Strip out the four chips and
the switching panels and what remains is large type on charcoal, which is not a
system, it is a default. There is nothing in it that tells you how to set a
pricing table or a case study.

**So the practical recommendation is not one hero, it is a division of labour:**

- Adopt **hero 06's system** as the 940Digital design language. Type scale,
  measure in `ch`, hairline structure, warm ground, mono for facts, the
  two-value blue. That is what every page of every client site gets built from.
- Use **hero 09's structure** for the homepage hero specifically. Name the
  fear, answer the one they picked. Set it in hero 06's language rather than
  its own.
- Keep **hero 08's live status** and **hero 10's owner column** as recurring
  components. They are the two strongest individual trust objects in the set
  and neither one needs to be a hero to work.

---

## What this set does not have, which you should know before choosing

**There is no photography-led hero among the ten.** That was a deliberate
choice and the brief allowed for it, but it leaves a real gap. A roofing client
with twenty years of finished jobs on their phone is badly served by a system
that has no opinion about photographs. Before hero 06's language goes into
production, it needs one more decision: how a full-bleed photograph behaves
inside a system built on restraint and hairlines. My instinct is large, quiet,
uncropped, with the type staying off the image entirely rather than sitting on
a gradient scrim, but that is untested and I would rather flag it than pretend
the set is complete.

**The figures in heroes 03, 04 and 08 are illustrative.** The $800 build and
$45 per month are consistent with the `priceRange` already published in the
site's schema, and the nine-minute median reply is written as a measured claim.
If those numbers are not exactly right, they need to be corrected before any of
this ships, because the entire argument of this set is that the numbers on the
page are real. A hero that says "not a promise, a record" and then quotes a
made-up record is worse than no hero at all.

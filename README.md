# The Library

A growing collection of website sections — heroes, testimonials, pricing blocks, CTAs, and more — adapted from real 940Digital builds (and eventually hand-built originals), each tagged with its type and the emotions/features it's built around.

This repo is public, so every section is fully de-identified before it's added: real company names are replaced with a single shared placeholder brand ("Acme Everything," styled differently per section), reviews and testimonials are entirely fabricated, and nothing — phone numbers, locations, owner names — ties a section back to the real business it was adapted from. See **De-identifying a pulled section** in [docs/schema.md](docs/schema.md) before adding one.

The point isn't a component kit to import wholesale. It's raw material: browse by feeling or by function, grab whatever's closest to what a site needs, and restyle it to fit — or just use it as a reference for a pattern instead of building one from scratch every time.

## Structure

```
sections/
  0001/
    meta.json      # id, website, type, emotions, features, notes...
    section.html   # self-contained: opens directly in a browser, no
                    # external stylesheet or shared nav required
  0002/
  ...
index.json          # generated — every meta.json in one searchable file
docs/schema.md       # the meta.json field reference + controlled vocab
scripts/
  build_index.py    # regenerate index.json after adding/editing a section
  next_id.py        # get the next free section id
.claude/skills/section-library/   # the Claude skill for browsing/pulling sections
```

## Using it

**To browse visually:** open [index.html](index.html) in a browser (double-click it, `open index.html`, or the site's live Vercel URL — it's the homepage) — every section renders as a live, scaled-down thumbnail with filter chips for type and feel, plus search. Click a card to open the real section full-size.

**To search or pull sections programmatically:** `index.json` at the repo root has the same data as one array — filter it with `jq`, or just ask inside Claude Code with this repo checked out ("find me a rugged, trustworthy hero section" or "show me every testimonials section") and the `section-library` skill will search and pull the matching `section.html` files.

After adding or editing any section, regenerate both:
```bash
python3 scripts/build_index.py && python3 scripts/build_gallery.py
```

To add a section, see **Adding a new section** in [docs/schema.md](docs/schema.md).

## Current count

11 sections, adapted and de-identified from 5 real client builds spanning a real range of tone — rugged trade, elegant/soft, plain-spoken, nature-toned, and premium/dark. Meant to keep growing — every new site is a chance to pull 1-2 more sections in before moving on.

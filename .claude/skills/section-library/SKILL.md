---
name: section-library
description: Search, browse, and pull sections from Owen's 940Digital section library (The-Library repo) — real hero/testimonial/pricing/CTA/etc. sections tagged by website, type, emotion, and feature. Use whenever Owen asks for design inspiration, references a "section from the library," wants a section pulled into a site he's building, or asks to add a newly-built section to the library.
---

# Section Library

A local checkout of `git@github.com:940Digital/The-Library.git` — a growing collection of real website sections, each stored as a self-contained `section.html` plus a `meta.json` describing what it is, where it came from, and what it's built to feel like.

**Local path:** `/Users/owen/Downloads/Claude Programs/The-Library`

If that path doesn't exist, clone it first:
```bash
git clone git@github.com:940Digital/The-Library.git "/Users/owen/Downloads/Claude Programs/The-Library"
```
If it exists, `git pull` before relying on it — Owen or another session may have added sections since your last read.

## Finding sections

For Owen to browse visually, open `gallery.html` in a browser (or point him to the published Artifact if one exists) — it renders every section as a live scaled thumbnail with type/feel filter chips and search, regenerated via `python3 scripts/build_gallery.py`.

For search/filtering by you, everything is indexed in `index.json` at the repo root — one JSON array entry per section, with `path` pointing at its `section.html`. Read the whole file (it's small) or filter it:

```bash
cd "/Users/owen/Downloads/Claude Programs/The-Library"
git pull -q
# by type
jq '.sections[] | select(.type=="hero")' index.json
# by emotion
jq '.sections[] | select(.emotions | index("rugged"))' index.json
# by feature
jq '.sections[] | select(.features | index("testimonial-carousel"))' index.json
# by source website
jq '.sections[] | select(.website | test("Brick"; "i"))' index.json
# free-text across name/notes
jq '.sections[] | select((.name + " " + .notes) | test("parallax"; "i"))' index.json
```

No `jq`? `grep`/`python3 -c "import json; ..."` over `index.json` works the same way — it's just an array of the field set documented in `docs/schema.md`.

When Owen describes a vibe rather than a type ("something bold and a little aggressive for a hero"), match against `emotions` first, `features` second, `type` last — emotions are the intentional sort axis here.

## Pulling a section into a real site

1. Find the candidate(s) via `index.json`, then read the actual `sections/<id>/section.html` to see the real markup/CSS — the metadata is a finding aid, not a substitute for reading the code.
2. Read `meta.json`'s `notes` field before reusing anything — it calls out what's a placeholder image, what JS hooks aren't included, what to swap.
3. Copy the relevant markup + CSS into the target site, then restyle: swap in the target site's fonts, color tokens, spacing scale, and real copy/images. Don't paste palette/font values from the library section into a client site verbatim — the whole point is reshaping it to fit.
4. Never claim a pulled section is finished until it's been restyled to the target site's actual design system and QA'd there (see [[foundit-form-handling]] / spec-site build conventions for that project's own bar).

## Using it for inspiration only

If Owen just wants ideas, open a handful of `section.html` matches in the browser preview tool side by side, or describe the layout/feature choices back to him — no need to touch a real project's files.

## Adding a new section

Use this whenever a section built for a client site (or an original) is worth keeping — Owen may ask directly, or flag one proactively when a section is unusually good/distinctive and you're already in that project.

1. `cd "/Users/owen/Downloads/Claude Programs/The-Library" && git pull`
2. `python3 scripts/next_id.py` → next id, e.g. `0012`
3. `mkdir sections/0012`
4. Extract the section as a **self-contained** `sections/0012/section.html`: inline all its CSS in a `<style>` tag (pull only the rules that actually apply — check for a shared `:root` variables block), include any Google Fonts `<link>` it needs, and drop any dependency on the parent site's shared nav/footer/JS. It should render correctly opened on its own in a browser.
5. Write `sections/0012/meta.json` following `docs/schema.md` exactly — reuse existing `type`/`emotions`/`features` vocabulary from `index.json` where it genuinely fits, rather than inventing near-duplicates.
6. `python3 scripts/build_index.py && python3 scripts/build_gallery.py` — regenerates `index.json` (fails loudly on any structural mistake — missing file, mismatched id) and `gallery.html`. Fix anything build_index flags.
7. Commit and push (per [[feedback-auto-push-940digital]], push once verified — no need to ask first; this repo is 940Digital-owned so set `git config user.name "940Digital"` / `user.email "940Digital@gmail.com"` locally first if not already set).

## Notes

- This is a reference/inspiration library, not a component framework — sections are deliberately NOT built to be dropped in unmodified. Restyling is the point.
- Real client names/reviews/photos-as-alt-text appear in some sections verbatim (they're already public on the live sites) — fine to reuse the pattern, but swap in the target business's own content before shipping anything to a real client.
- Image `src` paths in most sections are placeholders pointing at the original site's asset paths and will 404 standalone — that's expected, the markup/CSS is the artifact, not the photos.

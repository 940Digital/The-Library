# meta.json schema

Every section is a folder `sections/<id>/` containing exactly two files:

```
sections/0001/
├── meta.json       # metadata described below
└── section.html    # a single self-contained HTML file (inline <style>, no
                     # external stylesheet). Font links and CDN scripts are
                     # fine; anything site-specific (a shared stylesheet,
                     # a global nav) is not — the section must render on
                     # its own when opened directly in a browser.
```

## Image placeholders

Real client photos aren't kept in this library. Every section's `<img>`/`<source>` points at one of the shared, real stock photos in `/assets/placeholders/`, picked to roughly match what each section actually shows:

| File | Subject | Used for |
|---|---|---|
| `exterior-home.jpg` | Finished house exterior, roofline + siding visible | Roofing, fencing, general-contracting heroes/services |
| `portrait-lifestyle.jpg` | Outdoor portrait, golden-hour | Photography/lifestyle heroes |
| `nature-outdoor.jpg` | Sunlit trees | Tree service, landscaping, outdoor-trade heroes |
| `team-work.jpg` | People outdoors, team moment | Award/proof/about sections |
| `vehicle-car.jpg` | Glossy car close-up | Auto detailing, mobile-service heroes |
| `brutalist-concrete.jpg` | Raw monolithic concrete building | Brutalist/industrial-register heroes |
| `luxury-marble.jpg` | Dark marble interior, warm brass lighting | Luxury/high-end heroes |
| `dynamic-sprint.jpg` | Sprinters bursting from starting blocks | Dynamic/high-energy heroes |
| `brutalist-terracotta.jpg` | Graphic terracotta roofline against sky | Brutalist/industrial heroes wanting a warmer, second option |
| `city-lights-night.jpg` | Starry night skyline, saturated red/teal/blue light reflections on water | Night/urban/tech-forward heroes, especially any invert-filter or color-mask text effect |

When adding a section, point its images at whichever of these fits best (relative path from `sections/000X/` is `../../assets/placeholders/<name>.jpg`) instead of the original site's now-broken asset path — add a new one only if nothing existing fits the vibe at all (the first 5 are deliberately generic/reusable across many trades; the rest are vibe-specific, added for a specific tone rather than a specific trade). Always mark it with an HTML comment (`<!-- LIBRARY PLACEHOLDER: swap for the target site's own photo -->`) so it's obvious this isn't the real content. Whoever pulls a section into a real build swaps in that site's own photo before shipping.

## Fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | 4-digit, zero-padded, matches the folder name exactly (`"0001"`). |
| `number` | number | yes | Same value as `id`, as an integer. Used for sort order. |
| `name` | string | yes | Short, specific description of what the section IS, not just its type — "Full-bleed roofing hero, parallax image + staggered headline", not "Hero section". |
| `website` | string | yes | Always `"ACME Everything"` — the shared fictional brand every section is written under. This repo is public, so no field anywhere stores which real client a section was actually pulled from, the real business name, real reviewer names, or any other identifying detail; all of that gets rewritten before a section is added (see **De-identifying a pulled section** below). |
| `type` | string | yes | One category from the **type vocabulary** below. Pick the single best fit — this is the primary sort key. |
| `emotions` | string[] | yes | 3-6 words describing the *feeling* the section is designed to produce. Free text, but reuse existing words across sections where they genuinely apply — check `index.json` before inventing a new one. |
| `features` | string[] | yes | Functional/structural building blocks present in the section (see **feature vocabulary** below). This is what makes the library searchable by "does any section already do X" — be thorough. |
| `colorMode` | string | yes | `"light"` or `"dark"` — the section's own background, not the site's overall theme. |
| `palette` | string[] | no | 3-5 hex codes actually used in the section, for quick visual sorting. |
| `fonts` | string[] | no | Font family names used. |
| `dateAdded` | string | yes | ISO date (`YYYY-MM-DD`). |
| `file` | string | yes | Always `"section.html"` — kept as a field so the index is self-describing. |
| `notes` | string | no | Anything a future reader (human or Claude) would want to know before reusing this: what JS hooks are/aren't included, what's a placeholder, what to swap out, what pairs well with what. This is the most useful field for "pull into a real site" work — write it like a handoff note. |

## Type vocabulary (pick one)

`hero` · `services` · `testimonials` · `pricing` · `cta` · `about` ·
`gallery` · `footer` · `header-nav` · `contact` · `process` · `stats` ·
`faq` · `team` · `blog-list` · `feature-grid`

Add a new type only when nothing above fits — and add it to this list when you do.

## Feature tag guidelines (use freely, add new ones as needed)

Common ones already in use: `full-bleed-background-image`, `split-layout`,
`gradient-overlay`, `parallax-image`, `video-background-ready`,
`staggered-text-reveal`, `fade-up-on-scroll-hooks`, `scroll-reveal-hooks`,
`animated-counter-hooks`, `testimonial-carousel`, `star-ratings`,
`drag-to-scroll`, `pricing-cards`, `grouped-tiers-per-category`,
`dual-cta-buttons`, `phone-tel-link`, `trust-badge-with-stars`,
`overlapping-stat-card`, `award-plaque-with-photo`,
`google-rating-summary`, `responsive-picture-avif`,
`responsive-picture-srcset`, `svg-line-art-accents`, `radial-glow-accent`,
`label-tag`, `eyebrow-label`, `centered-layout`, `asymmetric-layout`,
`bulleted-capability-list`, `image-placeholder-comment`,
`prefers-reduced-motion-fallback`.

Run `grep -h features -A5 sections/*/meta.json` or just read `index.json` to see the full current set before coining a duplicate under a different name.

## De-identifying a pulled section

This repo is public. Before a section pulled from a real client build gets added, strip everything that ties it back to that business or its owner:

- **Company name** — replace with "Acme Everything" everywhere it appears (headline copy, footer/reply attributions, `<title>`, CSS comments).
- **Logo/brand mark** — add a small text wordmark reading "Acme Everything," styled to match that section's own fonts/colors/palette rather than reused unchanged from another section — the point is every site-family in the library reads as its own brand, not a single reskinned template repeated 11 times.
- **Reviews/testimonials** — fabricate them completely: invented reviewer names (not real people, not the real reviewers renamed), invented quotes. Real review platforms as a generic label ("Verified review") are fine; a real profile link, review count, or business-specific claim is not.
- **Location, phone numbers, founding year, awards** — remove or replace with placeholders. Use `(555) 010-0100`-style numbers (the `555` prefix is reserved for fiction).
- **Owner's first/last name** — never keep it, even in a CSS comment.
- **`meta.json`** — `website` is always `"ACME Everything"`; do not add a field that names the real business, its real repo slug, or its real live URL.

Then rewrite the surrounding copy freely — headlines, subheads, descriptions — so the section reads as its own thing rather than a lightly-edited copy of the source.

## Adding a new section

1. `python3 scripts/next_id.py` → gives you the next id, e.g. `0012`.
2. `mkdir sections/0012`
3. Write `sections/0012/section.html` — self-contained, opens correctly on its own, fully de-identified per above.
4. Write `sections/0012/meta.json` per this schema.
5. `python3 scripts/build_index.py && python3 scripts/build_gallery.py` — regenerates `index.json`/`index.html` and validates every section (fails loudly if a folder is missing a file, or an id doesn't match its folder).
6. Commit and push.

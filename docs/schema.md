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

## Fields

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string | yes | 4-digit, zero-padded, matches the folder name exactly (`"0001"`). |
| `number` | number | yes | Same value as `id`, as an integer. Used for sort order. |
| `name` | string | yes | Short, specific description of what the section IS, not just its type — "Full-bleed roofing hero, parallax image + staggered headline", not "Hero section". |
| `website` | string | yes | The business/site the section was pulled from. Use `"Original"` if hand-built for the library rather than lifted from a real site. |
| `websiteUrl` | string | no | Live URL of the source site, if it has one. |
| `sourceProject` | string | no | Repo/folder slug for the source project, for finding the original file later. |
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

## Adding a new section

1. `python3 scripts/next_id.py` → gives you the next id, e.g. `0012`.
2. `mkdir sections/0012`
3. Write `sections/0012/section.html` — self-contained, opens correctly on its own.
4. Write `sections/0012/meta.json` per this schema.
5. `python3 scripts/build_index.py` — regenerates `index.json` and validates every section (fails loudly if a folder is missing a file, or an id doesn't match its folder).
6. Commit and push.

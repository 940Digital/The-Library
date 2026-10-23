# Scroll reveals

Cards and images fade and rise as they enter the screen, using CSS `animation-timeline: view()`. No library. The effect is wrapped in `@supports (animation-timeline: view())` and in `prefers-reduced-motion: no-preference`. Everywhere else, `.reveal` is just visible.

## Where the idea came from

The view-timeline recipes on [scroll-driven-animations.style](https://scroll-driven-animations.style/), the reference for tying an animation to how far an element has entered the viewport instead of to a clock. This page uses that for a short rise on cards and a slight scale on images. It is not a copy of any one demo there.

## How to drop it into a client site

1. Copy the CSS between the `COPY` comments. Add class `reveal` to each card, and `reveal reveal--media` to each figure that holds an image.
2. Leave headings outside `.reveal`. The page’s structure should not move.
3. Give every image a width, a height, and a frame with `aspect-ratio`, plus `loading="lazy"` and `decoding="async"` when it is below the first screen.
4. Set `--brand` and `--accent`. Only opacity, `translate`, and `scale` animate, so the layout does not shift.
5. Set `animation-duration: auto`. A shorthand `animation:` line resets duration and the timeline never runs.

### Optional script

The script at the bottom of `section.html` is marked optional. It is an `IntersectionObserver` fade for browsers that do not understand `view()`. It does nothing when `view()` works, nothing under reduced motion, and nothing if `IntersectionObserver` is missing. Delete the script and the `.js-reveal-fallback` rules together. If you delete only the script and leave the rules, nothing breaks, because those rules wait for a class the script adds.

## Who it’s for

Any of the owner-run sites — landscaper, detailer, photographer, plumber — on a long page of cards or photos, where a little arrival makes the scroll feel considered. Skip it on a page that is one screen tall. Skip the motion entirely for a client who wants the page to sit still; the CSS already does that when the visitor asks for reduced motion.

## What stays put

Unsupported browser: content is visible, no script required. Reduced motion: the `@media (prefers-reduced-motion: reduce)` block kills the animation and the fallback. Images are the drawn placeholders in `assets/placeholders/`. Swap them before shipping. There are no reviews on this page.

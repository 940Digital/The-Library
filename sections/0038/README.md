# Before / after compare

One frame, two images, a seam you drag. The top image is clipped with `clip-path`. A native `<input type="range">` moves the seam, so arrow keys, Home, End, and touch come from the browser. A few lines of script write a single custom property, `--val`, which both the clip and the line read.

## Where the idea came from

[Yardzen](https://yardzen.com/) uses this on project stories: the designed yard on one side, the site as it was on the other, labels in the corners, a round handle on the line. This is that control, built with no library. The drawings here are placeholders. They are not a Yardzen project and not a client’s yard.

## How to drop it into a client site

1. Copy the CSS, the `div.cmp` markup, and the script between the `COPY` comments in `section.html`.
2. Use two photos of the **same** crop. Matched width and height. Different scenes read as a trick.
3. Rewrite both `alt` texts for what is actually in the photos.
4. Set `--brand` for the knob and the focus ring.
5. `loading="lazy"` is right when the block sits below the first screen. If it is the hero, set the upper image (the after photo) to `loading="eager"` so it can be the LCP image.
6. The frame has `aspect-ratio: 3 / 2` and a background color, so the box is reserved before the files arrive.

Without the script the split stays at halfway. The labels and both alts are still there.

`--thumb` is 44px and has to match the knob. The handle stops half its width in from each edge so it never hangs off the rounded frame.

## Who it’s for

Landscapers and mobile detailers, where the work is the difference between two states of the same thing. Also useful for a painter or a cleaner. Skip it if you only have one photo. Do not build a pair out of two unrelated pictures.

## Accessibility

The control is a labeled range input. `aria-valuetext` says how much of each side is showing. The readout under the frame is visual only, so a screen reader is not told twice. Focus draws a ring on the frame and on the knob. Dragging is something the person is doing, so `prefers-reduced-motion` does not disable it. There is no autoplay.

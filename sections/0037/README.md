# Sticky call / text / book bar

A fixed bar for small screens with three actions: **Call** (`tel:`), **Text** (`sms:`), and **Book**. From 48rem up it leaves the viewport and sits in the page as a row of links, so it does not cover the content. Body padding matches the bar, including the iOS home-indicator inset.

## Where the idea came from

[Benjamin Franklin Plumbing](https://www.benjaminfranklinplumbing.com/) keeps a call control on the screen on a phone — the “24/7” bar on their location pages. The behavior is the part worth keeping: the next step is always one tap away, and it gets out of the way on a desktop. This version adds Text and Book, which is the set an owner-run trade actually uses. It is not their layout, their colors, or their copy.

## How to drop it into a client site

1. In `section.html`, copy the CSS between the two `COPY START` / `COPY END` comments, and the `<nav class="callbar">` between the matching HTML comments. Copy the nav once. The phone frame is demo chrome.
2. Add `class="has-callbar"` to `<body>`.
3. On the viewport meta, add `viewport-fit=cover`. Without it, `env(safe-area-inset-bottom)` is always 0 and the bar sits under the home indicator.
4. Set `--brand` and `--accent` to the client’s colors. `--accent` is the stripe and the focus ring on the green bar (it fails contrast on the paper background, so don’t use it for small text).
5. Replace `(555) 010-0137` in the visible text, the `tel:` href, and the `sms:` href. They have to be the same number.
6. Point the Book link at the real scheduler or contact section.
7. No libraries, no font request, no JavaScript.

The bar is early in the DOM on purpose, so a keyboard user reaches Call before the rest of the page. Keep a skip link if the rest of the site has one.

## Who it’s for

Plumbers, landscapers, mobile detailers, and other owner-run businesses where the job starts with a phone call or a text. A photographer who wants a quiet inquiry form can still use the Book slot and drop Call and Text.

## Accessibility

Each action is a real link with a visible word. On a phone the number is visually hidden and still read (“Call at (555) 010-0137”). Targets are at least 44px. Focus uses `:focus-visible`. `scroll-padding-bottom` keeps in-page targets above the bar. Nothing animates, so reduced motion has nothing to turn off.

#!/usr/bin/env python3
"""
Regenerate gallery.html from index.json + scripts/gallery_template.html.

Run after build_index.py (or anytime a section changes):
    python3 scripts/build_index.py && python3 scripts/build_gallery.py

index.html is a self-contained, visual, filterable browser for the
library — it's the site's homepage (so it loads at the repo's Vercel/root
URL with no path needed), and also opens directly from disk (double-click,
or `open index.html`) to see every section as a live rendered thumbnail
instead of reading JSON.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT, "index.json")
TEMPLATE_PATH = os.path.join(ROOT, "scripts", "gallery_template.html")
OUT_PATH = os.path.join(ROOT, "index.html")


def main():
    with open(INDEX_PATH, encoding="utf-8") as f:
        index = json.load(f)
    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = f.read()

    sections_json = json.dumps(index["sections"], indent=2)
    out = template.replace("__SECTIONS_JSON__", sections_json)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"Wrote index.html with {len(index['sections'])} sections.")


if __name__ == "__main__":
    main()

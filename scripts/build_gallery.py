#!/usr/bin/env python3
"""
Regenerate gallery.html from index.json + scripts/gallery_template.html.

Run after build_index.py (or anytime a section changes):
    python3 scripts/build_index.py && python3 scripts/build_gallery.py

gallery.html is a self-contained, visual, filterable browser for the
library — open it directly in a browser (double-click, or `open gallery.html`)
to see every section as a live rendered thumbnail instead of reading JSON.
"""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_PATH = os.path.join(ROOT, "index.json")
TEMPLATE_PATH = os.path.join(ROOT, "scripts", "gallery_template.html")
OUT_PATH = os.path.join(ROOT, "gallery.html")


def main():
    with open(INDEX_PATH, encoding="utf-8") as f:
        index = json.load(f)
    with open(TEMPLATE_PATH, encoding="utf-8") as f:
        template = f.read()

    sections_json = json.dumps(index["sections"], indent=2)
    out = template.replace("__SECTIONS_JSON__", sections_json)

    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(out)

    print(f"Wrote gallery.html with {len(index['sections'])} sections.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Regenerate index.json from sections/<id>/meta.json.

Run after adding, editing, or removing any section:
    python3 scripts/build_index.py

index.json is the single file a Claude skill (or a human) greps/filters to
find sections by type, emotion, feature, or website without opening every
folder. Keep it in sync — don't hand-edit it.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS_DIR = os.path.join(ROOT, "sections")
INDEX_PATH = os.path.join(ROOT, "index.json")


def main():
    entries = []
    errors = []
    for name in sorted(os.listdir(SECTIONS_DIR)):
        folder = os.path.join(SECTIONS_DIR, name)
        if not os.path.isdir(folder):
            continue
        meta_path = os.path.join(folder, "meta.json")
        html_path = os.path.join(folder, "section.html")
        if not os.path.isfile(meta_path):
            errors.append(f"sections/{name}: missing meta.json")
            continue
        if not os.path.isfile(html_path):
            errors.append(f"sections/{name}: missing section.html")
            continue
        with open(meta_path, encoding="utf-8") as f:
            try:
                meta = json.load(f)
            except json.JSONDecodeError as e:
                errors.append(f"sections/{name}/meta.json: invalid JSON ({e})")
                continue
        if meta.get("id") != name:
            errors.append(
                f"sections/{name}/meta.json: id field is '{meta.get('id')}', "
                f"expected '{name}' (folder name and id must match)"
            )
        meta["path"] = f"sections/{name}/section.html"
        entries.append(meta)

    entries.sort(key=lambda m: m.get("number", 0))

    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        json.dump({"count": len(entries), "sections": entries}, f, indent=2)
        f.write("\n")

    print(f"Wrote index.json with {len(entries)} sections.")
    if errors:
        print("\nErrors found (fix and re-run):")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()

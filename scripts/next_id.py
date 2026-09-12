#!/usr/bin/env python3
"""Print the next free 4-digit section id, e.g. '0012'. Usage: python3 scripts/next_id.py"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECTIONS_DIR = os.path.join(ROOT, "sections")

existing = [int(n) for n in os.listdir(SECTIONS_DIR) if n.isdigit()]
next_n = max(existing, default=0) + 1
print(f"{next_n:04d}")

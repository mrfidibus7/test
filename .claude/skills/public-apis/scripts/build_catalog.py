#!/usr/bin/env python3
"""Build data/apis.json from the public-apis README.

Usage:
  build_catalog.py                 # download the latest README from GitHub
  build_catalog.py path/README.md  # parse a local copy
"""
import json
import re
import sys
import urllib.request
from pathlib import Path

README_URL = "https://raw.githubusercontent.com/public-apis/public-apis/master/README.md"
OUT = Path(__file__).resolve().parent.parent / "data" / "apis.json"

ROW = re.compile(r"^\|\s*\[(?P<name>[^\]]+)\]\((?P<url>[^)]+)\)\s*\|(?P<rest>.*)\|\s*$")


def parse(markdown):
    apis, category = [], None
    for line in markdown.splitlines():
        if line.startswith("### "):
            category = line[4:].strip()
            continue
        # Only the index section uses "### <Category>" followed by 5-column tables.
        if category is None or category.startswith("APIs Covered"):
            continue
        m = ROW.match(line)
        if not m:
            continue
        cols = [c.strip() for c in m["rest"].split("|")]
        if len(cols) != 4:
            continue
        desc, auth, https, cors = cols
        apis.append({
            "name": m["name"].strip(),
            "url": m["url"].strip(),
            "category": category,
            "description": desc,
            "auth": auth.strip("`") if auth.lower() != "no" else "none",
            "https": https.lower() == "yes",
            "cors": cors.lower(),
        })
    return apis


def main():
    if len(sys.argv) > 1:
        text = Path(sys.argv[1]).read_text(encoding="utf-8")
    else:
        with urllib.request.urlopen(README_URL, timeout=30) as r:
            text = r.read().decode("utf-8")
    apis = parse(text)
    if len(apis) < 500:
        sys.exit(f"Parsed only {len(apis)} APIs; README format may have changed. Not writing.")
    OUT.write_text(json.dumps(apis, indent=0, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(apis)} APIs in {len({a['category'] for a in apis})} categories to {OUT}")


if __name__ == "__main__":
    main()

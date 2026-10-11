#!/usr/bin/env python3
"""Search the public-apis catalog (data/apis.json).

Examples:
  search_apis.py weather
  search_apis.py "exchange rate" --no-auth --https
  search_apis.py --category Animals --cors
  search_apis.py --list-categories
  search_apis.py jokes --json --limit 5
"""
import argparse
import json
from pathlib import Path

DATA = Path(__file__).resolve().parent.parent / "data" / "apis.json"


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("query", nargs="*", help="keywords; all must match name, description or category")
    p.add_argument("--category", "-c", help="category name (case-insensitive substring)")
    p.add_argument("--no-auth", action="store_true", help="only APIs that need no key/OAuth")
    p.add_argument("--auth", help="only this auth type: apiKey, OAuth, X-Mashape-Key, User-Agent")
    p.add_argument("--https", action="store_true", help="only HTTPS APIs")
    p.add_argument("--cors", action="store_true", help="only APIs with CORS enabled (browser-callable)")
    p.add_argument("--limit", "-n", type=int, default=25)
    p.add_argument("--json", action="store_true", help="output JSON")
    p.add_argument("--list-categories", action="store_true")
    a = p.parse_args()

    apis = json.loads(DATA.read_text(encoding="utf-8"))

    if a.list_categories:
        counts = {}
        for api in apis:
            counts[api["category"]] = counts.get(api["category"], 0) + 1
        for cat, n in sorted(counts.items()):
            print(f"{cat} ({n})")
        return

    words = [w.lower() for w in " ".join(a.query).split()]
    out = []
    for api in apis:
        hay = f"{api['name']} {api['description']} {api['category']}".lower()
        if words and not all(w in hay for w in words):
            continue
        if a.category and a.category.lower() not in api["category"].lower():
            continue
        if a.no_auth and api["auth"] != "none":
            continue
        if a.auth and api["auth"].lower() != a.auth.lower():
            continue
        if a.https and not api["https"]:
            continue
        if a.cors and api["cors"] != "yes":
            continue
        out.append(api)

    total = len(out)
    out = out[: a.limit]
    if a.json:
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return
    if not out:
        print("No matches. Try fewer keywords, or --list-categories.")
        return
    for api in out:
        flags = f"auth={api['auth']} https={'yes' if api['https'] else 'no'} cors={api['cors']}"
        print(f"- {api['name']} [{api['category']}] — {api['description']}\n  {api['url']}  ({flags})")
    if total > len(out):
        print(f"... {total - len(out)} more; raise --limit or narrow the query.")


if __name__ == "__main__":
    main()

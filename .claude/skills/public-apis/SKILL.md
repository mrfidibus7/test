---
name: public-apis
description: >
  Find and call free public web APIs from the community-curated public-apis
  catalog (~1,900 APIs in 51 categories: weather, currency, finance, books,
  animals, sports, geocoding, government/open data, jokes, music, news, science,
  test data, etc.). Use when the user asks "is there an API for X", wants live
  data an API could provide (exchange rates, weather, holidays, country info,
  random facts...), needs an API to build an app/prototype against, or wants to
  compare APIs by auth/HTTPS/CORS.
---

# public-apis — find and use free APIs

Catalog source: https://github.com/public-apis/public-apis (MIT). A parsed
snapshot lives in `data/apis.json` next to this file; each entry has
`name, url, category, description, auth (none|apiKey|OAuth|X-Mashape-Key|User-Agent), https, cors`.

## 1. Find candidates

Run the search script (Python 3, stdlib only). Paths are relative to this skill's directory.

```bash
python3 scripts/search_apis.py weather --no-auth --https
python3 scripts/search_apis.py "exchange rate" -n 10
python3 scripts/search_apis.py --category "Open Data" --no-auth
python3 scripts/search_apis.py --list-categories
python3 scripts/search_apis.py holidays --json      # machine-readable
```

Keywords are AND-matched against name, description and category. If nothing
matches, drop keywords or browse a category.

**Prefer** `auth=none` + `https=yes` APIs when the user just needs data now.
Use `--cors` only if the API will be called from browser JavaScript.

## 2. Learn the API before calling it

The catalog `url` points to the API's docs, not to an endpoint. Fetch the docs
page (WebFetch, or `curl -s "https://r.jina.ai/<url>"` if the agent-reach skill
is installed) and find the real base URL, parameters and rate limits. Never
invent endpoints.

## 3. Call it

```bash
curl -sS "https://api.example.com/v1/thing?param=value" | python3 -m json.tool
```

- APIs marked `apiKey`/`OAuth` need credentials. Ask the user for the key and
  read it from an environment variable (e.g. `$OPENWEATHER_API_KEY`); never
  hard-code or echo secrets.
- If a call fails with a proxy/network error (e.g. `CONNECT tunnel failed, 403`),
  the sandbox's network policy is blocking that host. Tell the user which host
  to allow; do not fabricate a response.
- Respect rate limits; cache results in `/tmp` when making repeated calls.

## 4. Refresh the catalog

```bash
python3 scripts/build_catalog.py            # pulls the latest README from GitHub
python3 scripts/build_catalog.py README.md  # or parse a local copy
```

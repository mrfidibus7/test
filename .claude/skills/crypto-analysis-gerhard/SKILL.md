---
name: crypto-analysis-gerhard
description: >
  Analyze any crypto project the way Gerhard (YouTube @bitcoinstrategy, "The
  Bitcoin Strategy") does in his coin-analysis videos: a repeatable fundamental
  process of price-driver triage, leverage/derivatives audit, supply and unlock
  audit, buyers-vs-new-supply math, on-chain usage and revenue, value accrual,
  relative-valuation (coin/BTC, coin/ETH, coin/altcoin-market) charts, headline
  verification, and dated trigger numbers. Use when the user asks to analyze,
  evaluate or deep-dive a coin/token/protocol, asks "why is X pumping/dumping",
  "is X worth holding", "what's behind this rally", "compare X vs Y", or wants a
  "Gerhard-style" or "bitcoinstrategy-style" write-up. Produces a structured
  report matching the recap-table columns. Not for price predictions, trade
  signals, or personalized financial advice.
metadata:
  derived_from: 50 transcripts of youtube.com/@bitcoinstrategy, 2026-10-05 to 2026-10-11
---

# Analyze a crypto project like Gerhard

> **Not financial advice.** This skill reproduces one creator's *research process* from
> his public videos. It is not a recommendation to buy, sell or hold anything, and the
> creator sells a paid membership and copy-trading (a conflict to keep in mind). Data are
> snapshots from free APIs and can be wrong or stale. Always state this in the final
> answer and never present a Buy/Hold/Sell label as advice.

Source of the method: `research/bitcoinstrategy/analysis/methods.md` (full detail, quotes
and per-video citations) and `recap-table.md/.csv` (43 coins he analyzed) in the repo this
skill ships with. If those files are not available, everything needed is below.

## When to use

Use for: "analyze X", "why did X go up 40%?", "is X's rally real?", "what would make X a
buy?", comparing two coins, or reviewing an announcement's real impact on a token.
Don't use for: macro-only questions, NFT/price-art questions, or when the user wants a
guaranteed price target (this method gives conditions and triggers, not targets).

## Setup (do first)

1. **Say which tools you use**, e.g. "using agent-reach for web research, public-apis /
   snapshot.py for data".
2. **agent-reach** (web/YouTube/social fetching): `agent-reach --version`; for
   login-backed platforms run `agent-reach doctor --json` first. If it is missing, follow
   the setup note at the top of the agent-reach skill. It only *fetches*; you write the
   analysis.
3. **public-apis** (free APIs): find candidates with
   `python3 ../public-apis/scripts/search_apis.py crypto --no-auth --https` (also
   `defi`, `coin`). The catalog `url` points to docs, not endpoints: read the docs before
   calling; never invent endpoints. If a call fails with a proxy 403, tell the user which
   host to allow.
4. Prefer `curl` (macOS Python often lacks CA certificates). Cache responses in `/tmp`.
5. **Check whether Gerhard already covered the coin** (if the repo is present):
   `grep -i "^<Coin>,\|,<TICKER>," research/bitcoinstrategy/analysis/recap-table.csv`
   and read his latest view and thesis there. Treat it as one input, not the answer.

## Workflow (the checklist)

Write down a number for each step. If you can't find it, write **unknown**; never fill in.

1. **Frame the move.** Price, market cap, one-sentence description, performance vs **BTC
   and ETH** over 7d / 30d / 12m, and what is *not* known (no news, no listing, no upgrade).
2. **Market or coin?** Compare the coin's beta on the day (BTC move, total liquidations).
   Alts often move 2-4x BTC in sell-offs. If it simply followed the market, stop.
3. **What is the token a claim on?** Gas, governance only, fee share, buyback, burn, or
   nothing. "Nothing" means the rest is a bet on a future change.
4. **Leverage audit.** Open interest **in tokens** vs price over the same window; OI ÷
   market cap; funding vs ~11% p.a. (Binance "normal"); 24h liquidations; perp : spot
   volume; long/short account split; did OI jump *before or after* the price?
5. **Spot-buying audit.** Turnover (24h volume ÷ market cap); Binance + Coinbase only (drop
   dubious venues); Korea (Upbit) spikes; big Coinbase orders; average price paid by recent
   buyers (dollars traded ÷ tokens traded) vs now; exchange reserves in $ and in days of
   volume; whale wallets.
6. **Supply audit.** Circulating %, FDV, inflation in % **and** $/day vs daily volume,
   unlock dates/sizes (and what price did after the last ones), burn/buyback vs emissions,
   staking share/locks/exit queue, insider wallets. **Verify the supply on-chain**; price
   sites can be stale or change definitions.
7. **Flow math.** Convert ETF share-count changes, treasury-company buys and buybacks to
   tokens/day and divide by new supply. Use share count, not net assets. Separate the
   launch wave from steady state.
8. **Usage and business.** TVL (also in token terms), fees by source, stablecoin supply,
   transactions, customers. Who is paying? Is it rented or cyclical (launchpads)? What
   leads and what lags? Prefer stablecoin supply over TVL (TVL moves with prices).
9. **Value accrual and multiples.** Name the mechanism (buyback / burn / fee share / none),
   size it in $/yr vs market cap and vs new supply. Compute mcap ÷ annualized revenue
   ("years of revenue"), mcap ÷ fees, mcap per $1 of assets/TVL; compare with peers and
   with the coin's own history; note which pace you annualize.
10. **Ratio charts.** Coin ÷ BTC, ÷ ETH, ÷ "others" (altcoin market excl. top 10),
    dominance (vs total crypto, ideally ex-stablecoins), ÷ ecosystem peer. Mark long-term
    average ("equilibrium"), range, support, resistance; compute % to each (that is the
    risk/reward); classify regime (stabilizing vs persistent decline); require a clean
    breakout (20-30% beyond resistance, not 5-10%).
11. **Verify every headline in the primary source** (proposal, filing, docs, explorer,
    fund page). Classify status: hint / idea / draft / proposal / voted / testnet / mainnet /
    live / has a customer. Watch the words *committed, considering, non-binding, amended,
    not in production, devices not users*. Check quorum on votes and whether it's old news.
12. **Sector and attention.** Peers over 30d; is this a sector rotation? Regional flows;
    retail interest.
13. **Bull case and bear case, each in full, with numbers.**
14. **Verdict by time frame** (next weeks vs 12 months) and position style: hold, add on
    dips (never chase a green day), small position until a binary event resolves, pass,
    or short / BTC-hedged pair if chart *and* fundamentals are bad. No leverage on an
    already-leveraged asset.
15. **Triggers.** One or two bullish and one bearish/exit trigger, each an observable
    number or a date, plus the action tied to it.
16. **Schedule a re-check** and say what would change your mind.

## Rules of thumb (his numbers, as he states them in the videos)

| Metric | Reading |
|---|---|
| Binance funding ≈ 11% p.a. | normal; ~5% below normal; negative = shorts paying ("closer to a low than to a top") |
| OI ÷ market cap | ~2-3% very low · 6-8% small/moderate · 16%+ high · 20%+ very elevated |
| OI in tokens flat/down while price rises | spot-driven rally; OI rising with price = leverage |
| Perp : spot volume | 3-4× normal · 8×+ futures set the price · ≤1× unusual |
| Inflation | ~2% p.a. "still low" · <1% very low · >3% net not deflationary |
| Buyers ÷ new supply | LTC ETF ≈ 3× weekly miner output: "a good sign" · ~1.3× (NEAR) "a very thin margin" · <1× (ETH) "adding to it" |
| Ratio-chart breakout | needs 20-30% beyond resistance |
| Revenue multiple | ~17-24× for a growing leader isn't "expensive"; check the pace you annualize |
| Korea (Upbit) volume spikes | tended to fade 15-17% within days |
| Headline vs. contract | "market pays for contracts, not hints"; filing ≠ approval; committed ≠ deposited |

## Data to fetch and where

All endpoints below were tested with `curl` on 2026-10-11 (HTTP 200) unless marked.
Rate limits apply (CoinGecko free tier is strict; space calls out).

**One-shot snapshot (recommended first step):**

```bash
python3 scripts/snapshot.py --id sui --symbol SUI --chain Sui
python3 scripts/snapshot.py --id raydium --symbol RAY --llama raydium
```

(Paths relative to this skill's directory.) It pulls CoinGecko market/supply/turnover and
performance vs USD/BTC/ETH, OKX + Binance/Bybit funding, open interest in tokens, long/short and
taker ratios, perp:spot volume, and DefiLlama TVL / stablecoins / fees / revenue. Sections degrade to
"unavailable"; copy only what printed.

| Need | Free source (public-apis catalog entry) | Example call |
|---|---|---|
| Price, mcap, FDV, circ/total/max supply, ATH, volume | CoinGecko (auth none) | `curl -s "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=sui"` |
| Price history in BTC / ETH terms (ratio-chart data) | CoinGecko | `curl -s "https://api.coingecko.com/api/v3/coins/sui/market_chart?vs_currency=btc&days=365&interval=daily"` |
| TVL, fees, revenue, holder revenue | DefiLlama (none) | `curl -s "https://api.llama.fi/summary/fees/raydium?dataType=dailyRevenue"`; `.../tvl/raydium`; chains `.../v2/chains`; fees by chain `.../overview/fees/Sui` |
| Stablecoin supply by chain | DefiLlama stablecoins | `curl -s "https://stablecoins.llama.fi/stablecoinchains"` |
| Funding, open interest | OKX public API (no key); Bybit v5 public; Binance futures public data | `curl -s "https://www.okx.com/api/v5/public/funding-rate?instId=SUI-USDT-SWAP"`; `.../public/open-interest?instType=SWAP&instId=SUI-USDT-SWAP`; `curl -s "https://fapi.binance.com/futures/data/openInterestHist?symbol=SUIUSDT&period=1d&limit=8"` |
| Long/short accounts, taker buy/sell | Binance futures data | `.../futures/data/globalLongShortAccountRatio?symbol=SUIUSDT&period=1d&limit=7`, `.../takerlongshortRatio?...` (HTTP 451 in some regions) |
| Alternatives/backups | Coinpaprika (none), CoinCap (docs; DNS failed from the test machine), CorpStacking (ETF/treasury disclosures; untested), FraudCoins (top-holder concentration; untested), CoinLobster (whale trades; untested) | Run `python3 ../public-apis/scripts/search_apis.py crypto --no-auth --https`, then read the docs |

Not free or not scriptable (do manually or say "unknown"): CoinGlass cross-exchange OI and
liquidations, Coinbase large-order tape, Glassnode/Santiment on-chain, rwa.xyz, unlock
calendars (read the project docs/explorer), governance forums. TradingView-style charts are
needed for coin ÷ BTC / ÷ ETH / ÷ "others" ratio charts with trendlines; the API gives you
the data series only.

**agent-reach for the qualitative layer** (announce usage first):

```bash
# Web search (Exa) for news, proposals, filings
mcporter call exa.web_search_exa query="<coin> governance proposal vote" numResults=5
# Read a governance post, ETF fund page, SEC filing, docs page, blog
curl -s "https://r.jina.ai/<URL>"
# Gerhard's own videos on this coin (search, then captions)
yt-dlp --dump-json "ytsearch5:bitcoinstrategy <coin> crypto analysis"
yt-dlp --write-sub --write-auto-sub --sub-lang "en.*" --skip-download -o "/tmp/%(id)s" "<video URL>"
# Community sentiment (login-backed, doctor first)
twitter search "<ticker> unlock OR vote OR ETF" -n 10
```

Auto-captions garble names (SUI → "Swiss", Raydium → "Radium"); check the video title.

## Output template (columns match `recap-table.csv`)

Produce this block per coin, then the sections beneath it. Use `not covered` / `unknown`
rather than guessing. Cite a source (URL or API name + timestamp) for every number.

```
Coin: <name>            Ticker: <TICKER>           Data as of: <YYYY-MM-DD HH:MM UTC>
Use case / tech:                  <one sentence + what the token does>
Tokenomics, supply & unlocks:     <circ/total/FDV, inflation % and $/day, next unlocks, burn/buyback, staking>
Team, backers & partners:         <only if it is the catalyst; else "not covered">
Adoption & on-chain data:         <TVL (also in token terms), fees by source, stablecoins, tx, customers>
Institutional / ETF flows & buybacks: <ETF share counts, treasury cos, buyback in tokens/day vs new supply>
Leverage & derivatives:           <OI tokens vs price, OI/mcap, funding vs ~11% p.a., liquidations, perp:spot, long %>
Valuation vs peers / fundamentals: <mcap / annualized revenue, mcap / fees, mcap per $ assets; peer table>
Chart / relative-valuation setup: <vs BTC, vs ETH, vs "others", dominance: equilibrium, range, % to support/resistance>
Narrative, catalysts & cycle position: <dated catalysts, status of each: idea/proposal/voted/live>
Key risks:                        <3-5 specific risks>
Sentiment (Buy/Hold/Sell):        <label under the rubric below>
Score /10:                        <integer>
Last mentioned (date):            <date of latest Gerhard video on it, or "not covered">
Sources:                          <video IDs and URLs/APIs used>
Thesis summary:                   <3-4 sentences; verdict by time frame; the trigger numbers>
```

Then add:

- **Bull case** and **Bear case** (each with its numbers).
- **Triggers table**: `Trigger | Observable number/date | Action`.
- **What I could not verify** (list unknowns and manual checks left).
- **Footer**: "Not financial advice. Sentiment and score are an interpretation of the data
  using Gerhard's published framework, not a recommendation and not his rating."

**Rubric:** *Buy* = accumulating/starting a position makes sense (even only on dips or for
12 months). *Hold* = keep, neutral, or "too early to call" pending a dated trigger. *Sell* =
avoid / exit / chart favors betting on falling prices. *Score*: 6-7 constructive, 5
neutral, 3-4 cautious, 1-2 avoid/bearish; 8+ only with multiple independent confirmations.

## Honesty rules

- Never invent a number, date, or quote. If a figure is unavailable say so and show how to get it.
- Show formulas (OI ÷ mcap, new supply $/day ÷ volume, mcap ÷ annualized revenue).
- Keep dates explicit; crypto data go stale in hours.
- Distinguish what a project *claims* from what you *verified* (his strongest habit).
- Include the "not financial advice" note and the conflict-of-interest caveat above.

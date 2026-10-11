#!/usr/bin/env python3
"""Gerhard-style quantitative snapshot for one coin, from free public APIs.

Usage:
  python3 scripts/snapshot.py --id sui --symbol SUI [--llama raydium] [--chain Sui]

  --id      CoinGecko coin id (https://api.coingecko.com/api/v3/coins/list)
  --symbol  perp ticker used on exchanges, e.g. SUI -> SUIUSDT / SUI-USDT-SWAP
  --llama   DefiLlama protocol slug (TVL, 30d fees/revenue), optional
  --chain   DefiLlama chain name (TVL, stablecoins, 30d fees), optional

Stdlib only; shells out to curl (macOS Python often lacks CA certs). Every
section degrades to 'unavailable' on error, never invents data. Prints Markdown.
Free-tier rate limits apply (CoinGecko ~10-30 calls/min): ~3 calls here.
"""
import argparse, json, subprocess, sys, time
from datetime import datetime, timezone

def get(url, timeout=15, retries=2):
    err = None
    for attempt in range(retries + 1):
        try:
            out = subprocess.run(["curl", "-sS", "-m", str(timeout), "-w", "\n%{http_code}", url],
                                 capture_output=True, text=True)
            body, _, code = out.stdout.rpartition("\n")
            if code == "429" and attempt < retries:      # CoinGecko free-tier rate limit
                time.sleep(15); continue
            if code != "200":
                return None, f"HTTP {code or '?'} {out.stderr.strip()[:80]}"
            return json.loads(body), None
        except Exception as e:  # noqa: BLE001
            err = str(e)[:100]
    return None, err

def fmt(x, d=2):
    if x is None: return "n/a"
    a = abs(x)
    if a >= 1e9: return f"{x/1e9:,.{d}f}B"
    if a >= 1e6: return f"{x/1e6:,.{d}f}M"
    if a >= 1e3: return f"{x/1e3:,.{d}f}k"
    return f"{x:,.{d}f}"

def pct(x): return "n/a" if x is None else f"{x:+.1f}%"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--id", required=True); ap.add_argument("--symbol")
    ap.add_argument("--llama"); ap.add_argument("--chain")
    a = ap.parse_args()
    print(f"# Snapshot: {a.id}  ({datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC)\n")
    print("_Auto-fetched, unverified. Cross-check supply on-chain before relying on it._\n")

    # 1. Market + supply (USD), then relative performance from daily price history
    d, err = get(f"https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids={a.id}&price_change_percentage=7d,30d,1y")
    u = d[0] if d else None
    mcap = None
    if not u:
        print(f"- CoinGecko: unavailable ({err or 'unknown id'})")
    else:
        mcap = u.get("market_cap"); fdv = u.get("fully_diluted_valuation")
        circ, tot, mx = u.get("circulating_supply"), u.get("total_supply"), u.get("max_supply")
        vol = u.get("total_volume")
        print("## Price, supply, turnover")
        print(f"- Price ${u['current_price']:,.6g} | mcap ${fmt(mcap)} | FDV ${fmt(fdv)} | {pct(u.get('ath_change_percentage'))} from ATH")
        print(f"- Supply: circ {fmt(circ)} / total {fmt(tot)} / max {fmt(mx)}"
              + (f"  -> {circ/tot*100:.0f}% of total circulating" if circ and tot else "")
              + (f"; FDV/mcap {fdv/mcap:.2f}x" if fdv and mcap else ""))
        if vol and mcap: print(f"- 24h volume ${fmt(vol)} = {vol/mcap*100:.1f}% of mcap (turnover)")
        # relative performance: price expressed in BTC / ETH (CoinGecko's *_in_currency fields are USD-only)
        def chg(cur, days):
            h, _ = get(f"https://api.coingecko.com/api/v3/coins/{a.id}/market_chart?vs_currency={cur}&days=365&interval=daily")
            pr = (h or {}).get("prices") or []
            if len(pr) < 8: return {}
            last_t, last_p = pr[-1]
            out = {}
            for lab, dd in (("7d", 7), ("30d", 30), ("1y", 365)):
                tgt = last_t - dd*86400000
                if pr[0][0] > tgt + 86400000*2: out[lab] = None; continue
                p0 = min(pr, key=lambda x: abs(x[0]-tgt))[1]
                out[lab] = (last_p/p0-1)*100
            return out
        time.sleep(1.2); rb = chg("btc", 365); time.sleep(1.2); re_ = chg("eth", 365)
        print("\n## Relative performance (price in each denomination)")
        print("| Window | vs USD | vs BTC | vs ETH |\n|---|---|---|---|")
        for lab, k in (("7d", "price_change_percentage_7d_in_currency"), ("30d", "price_change_percentage_30d_in_currency"),
                       ("1y", "price_change_percentage_1y_in_currency")):
            print(f"| {lab} | {pct(u.get(k))} | {pct(rb.get(lab))} | {pct(re_.get(lab))} |")
        print("\nRead it like Gerhard: compare the windows (strong 30d + weak 1y = 'coming out of a deep hole') and judge vs BTC/ETH, not USD.")
        print("Ratio charts (coin/BTC, coin/ETH, coin/'others', dominance) still need a charting tool such as TradingView.\n")

    # 2. Derivatives
    if a.symbol:
        s = a.symbol.upper()
        print("## Derivatives (perpetuals)")
        d, err = get(f"https://www.okx.com/api/v5/public/funding-rate?instId={s}-USDT-SWAP")
        if d and d.get("data"):
            fr = float(d["data"][0]["fundingRate"])
            h, _ = get(f"https://www.okx.com/api/v5/public/funding-rate-history?instId={s}-USDT-SWAP&limit=9")
            hist = [float(x["fundingRate"]) for x in (h or {}).get("data", [])]
            avg = sum(hist)/len(hist) if hist else fr
            print(f"- OKX funding now {fr*3*365*100:+.1f}% p.a.; avg last {len(hist) or 1} prints {avg*3*365*100:+.1f}% p.a. "
                  "(his 'normal' on Binance is ~11% p.a.; negative = shorts paying)")
        else: print(f"- OKX funding: unavailable ({err})")
        d, err = get(f"https://www.okx.com/api/v5/public/open-interest?instType=SWAP&instId={s}-USDT-SWAP")
        if d and d.get("data"):
            x = d["data"][0]; oi_t, oi_usd = float(x["oiCcy"]), float(x["oiUsd"])
            print(f"- OKX OI {fmt(oi_t)} tokens (${fmt(oi_usd)})" + (f" = {oi_usd/mcap*100:.1f}% of mcap" if mcap else ""))
        else: print(f"- OKX OI: unavailable ({err})")
        d, err = get(f"https://fapi.binance.com/futures/data/openInterestHist?symbol={s}USDT&period=1d&limit=8")
        if d == []:
            print(f"- Binance: no {s}USDT perpetual (empty response); Bybit/OKX lines above may still apply.")
        elif d:
            oi = [float(x["sumOpenInterest"]) for x in d]
            print(f"- Binance OI (tokens) first->last of {len(oi)} days: {fmt(oi[0])} -> {fmt(oi[-1])} ({(oi[-1]/oi[0]-1)*100:+.1f}%)"
                  "  [compare with price change over the same days]")
            ls, _ = get(f"https://fapi.binance.com/futures/data/globalLongShortAccountRatio?symbol={s}USDT&period=1d&limit=1")
            if ls: print(f"- Binance accounts long {float(ls[0]['longAccount'])*100:.0f}% / short {float(ls[0]['shortAccount'])*100:.0f}%")
            tk, _ = get(f"https://fapi.binance.com/futures/data/takerlongshortRatio?symbol={s}USDT&period=1d&limit=2")
            if tk: print(f"- Binance taker buy/sell ratio (latest 2 days): {', '.join(x['buySellRatio'] for x in tk)}  (<1 = sellers hitting the market)")
            pf, _ = get(f"https://fapi.binance.com/fapi/v1/ticker/24hr?symbol={s}USDT")
            sp, _ = get(f"https://data-api.binance.vision/api/v3/ticker/24hr?symbol={s}USDT")
            if pf and sp: print(f"- Binance 24h volume perp ${fmt(float(pf['quoteVolume']))} vs spot ${fmt(float(sp['quoteVolume']))} "
                                f"= {float(pf['quoteVolume'])/max(float(sp['quoteVolume']),1):.1f}x (3-4x is 'normal'; 8x+ means leverage sets the price)")
        else:
            print(f"- Binance futures data: unavailable ({err or 'no data'}); may be geo-blocked (HTTP 451). Using Bybit instead:")
            d, err = get(f"https://api.bybit.com/v5/market/open-interest?category=linear&symbol={s}USDT&intervalTime=1d&limit=8")
            lst = (d or {}).get("result", {}).get("list", [])
            if lst:
                oi = [float(x["openInterest"]) for x in reversed(lst)]
                print(f"- Bybit OI (tokens) {fmt(oi[0])} -> {fmt(oi[-1])} ({(oi[-1]/oi[0]-1)*100:+.1f}%) over {len(oi)} days")
            else: print(f"- Bybit OI: unavailable ({err or 'no ' + s + 'USDT perpetual'})")
        print("- Not available free: CoinGlass cross-exchange OI/liquidations (key needed) and Coinbase large-order tape; check manually.\n")

    # 3. Usage / business (DefiLlama)
    if a.llama or a.chain:
        print("## Usage and business (DefiLlama)")
    if a.llama:
        d, err = get(f"https://api.llama.fi/summary/fees/{a.llama}")
        r, _ = get(f"https://api.llama.fi/summary/fees/{a.llama}?dataType=dailyRevenue")
        h, _ = get(f"https://api.llama.fi/summary/fees/{a.llama}?dataType=dailyHoldersRevenue")
        if d:
            f30 = d.get("total30d")
            print(f"- Fees paid by users: 24h ${fmt(d.get('total24h'))}, 30d ${fmt(f30)}")
        else: print(f"- Fees for '{a.llama}': unavailable ({err})")
        if r and r.get("total30d"):
            r30 = r["total30d"]
            print(f"- Protocol revenue: 24h ${fmt(r.get('total24h'))}, 30d ${fmt(r30)} (annualized ${fmt(r30*12)})"
                  + (f"; mcap / annualized revenue = {mcap/(r30*12):.1f}x (his 'years of revenue')" if mcap else ""))
        if h and h.get("total30d"):
            print(f"- Revenue to token holders (buyback/burn/staking): 30d ${fmt(h['total30d'])}"
                  + (f" = {h['total30d']*12/mcap*100:.1f}% of mcap per year" if mcap else ""))
        t, err = get(f"https://api.llama.fi/tvl/{a.llama}")
        print(f"- TVL ${fmt(t)}" + (f"; mcap/TVL = {mcap/t:.1f}x" if isinstance(t, (int, float)) and mcap else "") if t is not None else f"- TVL: unavailable ({err})")
    if a.chain:
        d, err = get("https://api.llama.fi/v2/chains")
        row = next((c for c in (d or []) if c.get("name", "").lower() == a.chain.lower()), None)
        print(f"- Chain TVL ${fmt(row['tvl'])}" if row else f"- Chain TVL: unavailable ({err or 'name not found'})")
        d, err = get("https://stablecoins.llama.fi/stablecoinchains")
        row = next((c for c in (d or []) if c.get("name", "").lower() == a.chain.lower()), None)
        print(f"- Stablecoins on chain ${fmt(row['totalCirculatingUSD']['peggedUSD'])}" if row else f"- Stablecoins: unavailable ({err or 'name not found'})")
        d, err = get(f"https://api.llama.fi/overview/fees/{a.chain}?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true")
        if d and d.get("total30d") is not None:
            print(f"- Chain+app fees (DefiLlama definition, includes dApp fees; his 'chain fees' = gas only) 24h ${fmt(d.get('total24h'))}, 30d ${fmt(d['total30d'])}"
                  + (f"; mcap/annualized = {mcap/(d['total30d']*12):,.0f}x" if mcap and d['total30d'] else ""))
        else: print(f"- Chain fees: unavailable ({err})")
    print("\n_Next: supply schedule/unlocks, ETF share counts, governance/filings (agent-reach), ratio charts (coin/BTC, /ETH, /others)._")

if __name__ == "__main__":
    sys.exit(main())

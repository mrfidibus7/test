# How Gerhard analyzes crypto projects: methods, generalized

Source: the YouTube channel *The Bitcoin Strategy* (@bitcoinstrategy), host Gerhard. This document covers his last 50 videos (2026-10-05 → 2026-10-11).

> **Not financial advice.** This is a summary of one creator's analysis framework, written to help you reproduce the *process*. It is not a recommendation to buy or sell anything. Every number below is a snapshot he stated on the video's date; none were re-checked against live data.

## 0. Coverage and how to read this file

- **Videos analyzed: 50 of 50.** Every transcript was read start to finish; none were skimmed or sampled.
- **Videos without captions: none.** All 50 have English captions (YouTube auto-generated, see `INDEX.md`).
- **Coins covered: 43** (Quant ×4, Sui ×4 and Solana ×2 were each revisited; all others appear once). Per-coin detail is in `recap-table.md`.
- **Citations.** Every claim carries a tag `[TICKER MM-DD VIDEOID]`; all dates are 2026. Appendix B maps tags to titles and URLs.
- **Quotes** are verbatim from the auto-captions, trimmed. Auto-captions garble names ("Swiss"/"USD" = SUI/USDsui, "Ono" = ONDO, "Radium" = Raydium, "Bitmain" = BitMine, "Casper" = Kaspa, "PIFF" = PYTH, "Athena" = Ethena). I corrected a name only where the video title makes it unambiguous, and I flag figures that look garbled.
- **Source caveats you should keep in mind.**
  - Every description links to his automatic copy-trading offer, the outros pitch his paid "premium" membership, and he says in nearly every video that he "made my first million with altcoin trading". In the Hyperliquid video he discloses that he uses the platform and built copy-trading on it [HYPE 10-06 tq-qId4OLdM].
  - He cites an earlier price 20 times, for 14 different coins ("I covered X when the price was only Y"), and every time the price has since risen [QNT 10-06 2bwkNjZjHy0; ONDO 10-06 KipxCnSMPvc; SUI 10-06 KodaC46SpVI; ICP 10-06 NQgq-ulYpcE; RAY 10-06 Sv-QuZJrcFw; HYPE 10-06 tq-qId4OLdM; AVAX 10-07 sZhra8WARrA; NEAR 10-08 Gt5gxJxZOMU; SUI 10-08 yqsYT4pduzg; KAS 10-09 8xqJ5CJYqYw; UNI 10-09 LgOyfBiX_4I; ZEC 10-09 SEqld8bdys0; ENA 10-10 nTPRqKNSGW8; PUMP 10-11 hEkk41geAgs; AERO 10-11 pJaT2HqKppg]. This sample cannot tell you his hit rate, because there is no equivalent line for calls that went wrong.
  - One week of videos, in a rising altcoin tape, is a narrow window.

## 1. The template behind almost every video

The process is more consistent than the coins. Almost every video follows this sequence, and copying it is half the method:

1. **A hook that is a specific number or contradiction**, not a price target ("Hyperliquid collected more fees in September than the Ethereum, Solana, Tron and BNB chains put together") [HYPE 10-06 tq-qId4OLdM].
2. **"Where we are"**: price, market cap, one sentence on what the token is, the move versus Bitcoin, and a plain note on what is *not* known ("there was no announcement. There was no listing. There was no upgrade") [BEAM 10-05 QwRkPAiX5fc].
3. **A frame that structures the investigation**: suspects ruled out one by one [BEAM 10-05 QwRkPAiX5fc; ICP 10-06 NQgq-ulYpcE; PONS 10-07 w_p5KQgkYNc], "four numbers" [FET 10-05 golbI3jN0Zw; VVV 10-08 WwoSy_hLO6s; LTC 10-07 nQ915SNZ7C4], "three questions where each answer leads to the next" [ONDO 10-06 KipxCnSMPvc; RAY 10-06 Sv-QuZJrcFw], or bull case then bear case "both in full" [S 10-06 _h_LTQaj4dQ; HYPE 10-06 tq-qId4OLdM].
4. **The evidence**, always as a small set of charts or tables: derivatives, supply, usage, outside buyers, and a relative-valuation chart.
5. **A verdict split by time frame**, with a position style (hold, add on dips, small position, stay out).
6. **"What would change my mind"**: one to three observable triggers, each a number or a date (see Method 11).

## 2. Tools and data sources he actually uses

He is vague about where some numbers come from. This table lists only what he names or shows; "unnamed" means he shows the number without saying which site.

| Purpose | What he names or shows | Cited in |
|---|---|---|
| Charting / ratio charts | Charts are shown in every video; descriptions link "My Chart Software" → TradingView (he never names the tool on camera) | all descriptions, e.g. [BEAM 10-05 QwRkPAiX5fc] |
| Open interest, funding, long/short, liquidations | Binance, OKX and Bybit data, plus **CoinGlass** for open interest across exchanges | [FET 10-05 golbI3jN0Zw; ADA 10-06 Dp9MJWeGdDs; QNT 10-07 0HkozsaJpzQ; TRUMP 10-11 GvE7lGieXag] |
| Spot flow and big orders | Binance and Coinbase spot volume; the **Coinbase trade tape** (size and side of large trades); **Upbit** (South Korea) volume; taker buy/sell volume on Binance futures | [QNT 10-08 g8FjETXl2V4; BEAM 10-05 QwRkPAiX5fc; ORCA 10-07 MSUv-hvKgMU; QNT 10-07 0HkozsaJpzQ] |
| Chain usage (TVL, fees, stablecoins, transactions, wallets) | Shown constantly, **source usually unnamed**. Named: **rwa.xyz** (tokenized assets) and a "Blockworks report" (Bonk) | [SOL 10-08 e1OOLAeH_HM; XLM 10-08 muDa7fJBE4w; BONK 10-11 KtWfQ3lPqFw] |
| Supply | Chain/contract data and explorers (he "checked the contract" for FET; the Injective explorer for supply; the Onyx explorer), **CoinGecko** circulating supply, staking dashboards, burn addresses | [FET 10-05 golbI3jN0Zw; INJ 10-07 1JrrfN0U9QA; XCN 10-08 k2VkjEvJsKo; IMX 10-09 9ybKjcs7lik] |
| Bitcoin on-chain / macro | **Glassnode** report, **Santiment**, Fed-odds page, Bitfinex analysts, Binance order book | [BTC 10-08 RiWS7k2O46E] |
| Events | Governance forums and vote pages, protocol docs and blogs, ETF fund pages and amended filings, company quarterly filings, news (CoinMarketCap, Decrypt, CoinDesk, Bloomberg), GMGN data | [ORCA 10-07 MSUv-hvKgMU; DOT 10-10 r3CkKUqxH3U; PEPE 10-10 GoOYmdLX3UI; BONK 10-11 KtWfQ3lPqFw; PONS 10-07 w_p5KQgkYNc] |
| Retail attention | **YouTube Studio**: how his previous video on a coin performed against the channel average | [ADA 10-06 Dp9MJWeGdDs; ONDO 10-06 KipxCnSMPvc; HYPE 10-06 tq-qId4OLdM] |

Not named anywhere in the 50 videos: DefiLlama, Etherscan, Dune, Token Terminal, Nansen, Arkham. Wherever you see those in the skill file, they are my suggested equivalents, not his sources.

---

## 3. The methods

### Method 1: Price-driver triage ("Who is buying?")

**Question it answers:** *Why did this price move, and is the driver durable?*

**Data and tools:** price vs BTC over several windows; news and announcements; chain usage; derivatives data; spot volume by venue; supply changes; ETF and treasury flows.

**Steps**
1. State the move (size, window) and the market cap. Say explicitly what is not known: "I looked for [news], and I could not find any" [FET 10-05 golbI3jN0Zw]; "none of the sources I read gives a reason for it" [ICP 10-06 NQgq-ulYpcE].
2. List the suspects: (a) news, (b) real chain usage, (c) futures/leverage, (d) a specific spot venue, (e) supply change, (f) outside money (ETFs, treasury companies, buybacks).
3. Test each suspect with one number and **rule it out explicitly**. Every video that uses this frame says "we can rule that out".
4. What survives is the driver. Judge durability: spot holders who don't sell are durable; leverage, a Korean volume spike and a headline are not.

**Rules of thumb (quoted)**
- "So, the futures traders followed the price move. They did not start it." [BEAM 10-05 QwRkPAiX5fc]
- "When a token goes up by its own in a weak market, that tends to be real buying." [IMX 10-09 9ybKjcs7lik]
- "I actually think that's the wrong question. The buyers are pretty much the same … what really changed is the other side, as in the biggest seller is now gone." [JUP 10-10 MyAp_YW8rjI]
- "So, this time, the price itself is the story, and that's why I want to know what's behind it." [FET 10-05 golbI3jN0Zw]

**Examples**
- **BEAM** +40% in hours with no news. Chain ruled out (TVL ~$1.2M, fees near zero). Futures ruled out (open interest rose *after* the price; liquidations < $200k). The answer was Upbit: ~$36M volume against < $1M on a normal day [BEAM 10-05 QwRkPAiX5fc].
- **ICP** up 77%. Usage ruled out (~$5.5k of compute burned per day, TVL ~$15M). Futures ruled out (OI ~7% of market cap, neutral funding, ~$300k liquidations). The clue was supply: ~33k new tokens/day (~$120k) against ~$75M daily volume [ICP 10-06 NQgq-ulYpcE].
- **PONS** fees fell > 90%. Gas-subsidy end ruled out (no step-down on Sept 29). Chain ruled out (TVL at an all-time high). The clue was a competitor: Uniswap's launchpad charging 0.25% against Pons's 1% [PONS 10-07 w_p5KQgkYNc].

**Pitfalls / red flags:** media explanations can be wrong. Crypto media said Orca's proposal "sends more revenue to the holders"; he read it and "it says pretty much the opposite" [ORCA 10-07 MSUv-hvKgMU]. "No news" does not mean "no reason".

---

### Method 2: Separate coin-specific moves from market-wide moves

**Question:** *Is this the coin, or the tide?*

**Data:** coin/BTC ratio over 7 days, 30 days and 12 months; BTC price and liquidation totals on sell-off days; the altcoin basket.

**Steps**
1. Always measure performance against Bitcoin, not USD: "we want to measure performance against Bitcoin, not versus the US dollar" [RAY 10-06 Sv-QuZJrcFw].
2. Use three windows: short (7d), medium (30d) and 12 months. A strong 30 days inside a weak 12 months means "we are coming out of a deep hole, and the long-term picture has not yet turned" [FET 10-05 golbI3jN0Zw].
3. On a sell-off day, find the macro cause (BTC drop, liquidation total, yields) and compare the coin's beta: SUI moved "about two and a half times as much as Bitcoin" [SUI 10-09 0pUUjzeP6Mg]; QNT fell ~13% while BTC fell ~3% [QNT 10-08 g8FjETXl2V4].
4. If the coin lags in a market-wide move, treat the drop as macro, not as news about the project [UNI 10-09 LgOyfBiX_4I; XLM 10-08 muDa7fJBE4w].

**Examples:** UNI −9% in 24h while BTC broke below $82,000 and ~$1B of futures were liquidated; "altcoins tend to fall more than Bitcoin" [UNI 10-09 LgOyfBiX_4I]. XLM −12% in a week alongside ~$700M of liquidations and 10-year yields above 5% [XLM 10-08 muDa7fJBE4w].

**Pitfalls:** a rally that is "just Bitcoin pulling everything up" needs no explanation (SHIB: flat versus BTC over 3 months, so "that rally in US dollars was simply just Bitcoin pulling everything up") [SHIB 10-05 x4Gjk-ur2Kk].

---

### Method 3: Derivatives and leverage audit

**Question:** *Is the move built on borrowed money, and how fragile is it?*

**Data and tools:** Binance/Bybit/OKX open interest (OI) **counted in tokens**, CoinGlass OI across exchanges, funding rate, liquidations over 24h, perpetual-vs-spot volume, long/short account ratio, taker buy/sell volume.

**Steps** (he runs this as a repeatable checklist)
1. **OI in tokens vs price over the same window.** Price up with OI flat or down means spot-driven; OI rising with price means leverage. Use tokens, not dollars, so the price move doesn't contaminate the reading.
2. **OI relative to market cap** (all exchanges) for the level of fragility.
3. **Funding rate vs the normal level** (about 11% per annum on Binance in these videos).
4. **Liquidations in the last 24h** to see whether there was a squeeze.
5. **Perp-to-spot volume ratio.**
6. **Long/short account split**, and whether the "big accounts" differ from the crowd.
7. **Timing:** did OI jump before or after the price move?

**Rules of thumb (quoted)**
- Funding: "roughly 11% per annum on Binance. And that's just the normal level" [FET 10-05 golbI3jN0Zw]; 5% is "below the normal level" [ETH 10-07 K3AVBoCrDK8]. Negative funding is the shorts paying: "that tends to happen closer to a low than to a top" [XLM 10-08 muDa7fJBE4w] (and "closer to a low than to a high" [PEPE 10-10 GoOYmdLX3UI]).
- "When the open interest goes down and the price holds, then it's usually the short side that's closing." [QNT 10-06 2bwkNjZjHy0]
- "When the leverage leaves and the price barely moves, somebody else is taking the other side. And those tend to be buyers on the spot market without borrowed money." [ONDO 10-06 KipxCnSMPvc]
- "When a rally runs on leverage, the open interest tends to go up together with the price. This time it went down." [PYTH 10-09 UcM2um0wtHM]
- "A rally without leverage does not get liquidated easily." [SHIB 10-05 x4Gjk-ur2Kk]
- Fewer bears means less squeeze fuel: "fewer bears also means less fuel for a potential short squeeze" [QNT 10-06 2bwkNjZjHy0].
- Ratios as he characterizes them: OI ≈ 2% of market cap is low [SHIB 10-05 x4Gjk-ur2Kk]; 3% "still very low" [STX 10-11 PTBr4ZxRSVI]; 6% "quite small" for a big coin [ADA 10-06 Dp9MJWeGdDs]; 7% "moderate" [ICP 10-06 NQgq-ulYpcE]; 16% "quite high" [STRK 10-10 hTMB4fHaNgc]; 19% "a lot for a token of this size" [PUMP 10-11 hEkk41geAgs]; "more than 20% … very elevated" [NEAR 10-08 Gt5gxJxZOMU]; 38% "quite high" [CRV 10-09 aEJrg2aYRyU].
- Perp:spot volume ≈ 3–4× is "normal" [SUI 10-06 KodaC46SpVI; JUP 10-10 MyAp_YW8rjI]; ≥ 8× (HYPE 8×, STRK 8×, PUMP 8×, ZEC 12×) means "the perpetual futures set the price here with leverage" [HYPE 10-06 tq-qId4OLdM; STRK 10-10 hTMB4fHaNgc; PUMP 10-11 hEkk41geAgs; ZEC 10-09 SEqld8bdys0]; spot ≥ perps is unusual [SHIB 10-05 x4Gjk-ur2Kk; ICP 10-06 NQgq-ulYpcE].
- Long/short: "about 62% of the accounts are betting on rising prices … if the price turns around, those positions have to be closed" [FET 10-05 golbI3jN0Zw].

**Examples**
- **QNT, 3 videos in a row:** shorts paid a record funding bill (about −0.34% in one print, ~$600k in a day) yet price didn't fall; OI then fell 12–18% [QNT 10-06 2bwkNjZjHy0; QNT 10-07 0HkozsaJpzQ]. By Oct 11 he describes the leverage as gone (Bybit OI −28% in 3 days, funding slightly positive, 56% long) [QNT 10-11 R1nqM9s6W_w].
- **LTC:** Binance OI 1.7M → 1.3M tokens (−20%) with price only −6%; long accounts 72% → 65% [LTC 10-07 nQ915SNZ7C4].
- **STRK:** "the leverage went down while the price went up. That tends to be a much healthier kind of rally" [STRK 10-10 hTMB4fHaNgc].

**Pitfalls**
- Aggregated OI can be inflated by tiny exchanges: DOT showed $1.4B on some sites; "most of that comes from a small exchange with almost no volume", about $340M without it [DOT 10-10 r3CkKUqxH3U].
- Exchanges disagree: QNT shorts were crowded only on Binance and Bybit; OKX funding "stayed at zero" [QNT 10-06 2bwkNjZjHy0].
- A spot-driven rally can still sit on a leveraged market: FET OI was ~¼ of market cap [FET 10-05 golbI3jN0Zw].
- Price discovery on futures: when most volume is perps, 10–20% moves "just due to leverage" are normal [QNT 10-06 2bwkNjZjHy0; S 10-06 _h_LTQaj4dQ].

---

### Method 4: Spot-market and holder forensics

**Question:** *Who exactly is buying and selling, on which venue, and at what price?*

**Data and tools:** Binance and Coinbase spot volume; turnover (24h volume ÷ market cap); Upbit volume; the Coinbase tape (large market orders by side); taker volume on Binance futures; exchange reserves; whale wallets; wallet counts; team-linked wallet traces.

**Steps**
1. **Turnover:** 24h volume ÷ market cap, compared with sector peers. FET turned over ~40% of its market cap in a day against ~5% for Bittensor [FET 10-05 golbI3jN0Zw].
2. **Venue check:** which exchange set the price? Korea (Upbit) is a recurring answer [BEAM 10-05 QwRkPAiX5fc; ORCA 10-07 MSUv-hvKgMU]. Discount untrusted venues: "close to a third of that spot volume comes from exchanges that I wouldn't necessarily trust", so look at Binance + Coinbase only [FET 10-05 golbI3jN0Zw].
3. **Average price paid by recent buyers:** "dollars traded divided by tokens traded give us an average price" [QNT 10-07 0HkozsaJpzQ]. Compare with the current price to see whether the newest holders are in profit, at break-even, or underwater.
4. **Who traded at the extremes:** Coinbase tape for the low of a sell-off [QNT 10-08 g8FjETXl2V4]; taker volume to see which side hit the market [QNT 10-07 0HkozsaJpzQ].
5. **Exchange reserves and whale wallets**, translated into dollars and days of volume [SHIB 10-05 x4Gjk-ur2Kk; BTC 10-08 RiWS7k2O46E; KAS 10-09 8xqJ5CJYqYw].
6. **Insider flow:** trace team-linked wallets to exchange deposit addresses [TRUMP 10-11 GvE7lGieXag].

**Rules of thumb (quoted)**
- "A buyer who pays the market price at the low isn't waiting for a discount. The buyer simply wants the tokens right now." [QNT 10-08 g8FjETXl2V4]
- "So, the newest buyers are sitting right at break even. That's a very thin cushion." [QNT 10-07 0HkozsaJpzQ]
- Put an exchange-reserve headline in context: +7T SHIB on exchanges ≈ $40M, "the whole increase is less than half a day of trading" [SHIB 10-05 x4Gjk-ur2Kk].
- "A deposit on exchange is not necessarily a sale yet." [TRUMP 10-11 GvE7lGieXag]
- Korean spikes tend to fade: Beam gave back ~17% within 3 days [BEAM 10-05 QwRkPAiX5fc]; Orca ~15% within a week [ORCA 10-07 MSUv-hvKgMU].
- Volume thresholds he uses as conditions to get more bullish: QNT spot back above $100M/day [QNT 10-06 2bwkNjZjHy0]; KAS "more than $20 million US per day" [KAS 10-09 8xqJ5CJYqYw]; PEPE daily volume above $400M [PEPE 10-10 GoOYmdLX3UI].
- Whale accumulation: BTC big wallets took in "more than 4,000 per day" against ~450 mined, roughly 9× [BTC 10-08 RiWS7k2O46E].

**Pitfalls:** a low-volume rally is "fragile" (Glassnode's "running light") [BTC 10-08 RiWS7k2O46E]; but "selling Bitcoin just because the trading volume is low doesn't make sense to me" [BTC 10-08 RiWS7k2O46E]. Data-site counts of "who holds" can be incomplete: for Kaspa he cites an August on-chain analysis of the largest wallet and does not say it is current [KAS 10-09 8xqJ5CJYqYw].

---

### Method 5: Supply and tokenomics audit

**Question:** *How much new supply do buyers have to absorb, and can it reach the market?*

**Data and tools:** circulating / total / max supply and fully diluted value (CoinGecko or CoinMarketCap, **verified against the chain**); unlock schedules from docs; emission and inflation from the chain; burn addresses; staking ratio, lock durations, exit queue; team and foundation wallets; governance votes that change supply.

**Steps**
1. Circulating vs total (fully diluted value). Share locked: HYPE ~22% circulating [HYPE 10-06 tq-qId4OLdM]; TRUMP ~28% [TRUMP 10-11 GvE7lGieXag]; SHIB 100% [SHIB 10-05 x4Gjk-ur2Kk].
2. Annual inflation in % **and** in dollars per day against average daily volume (ICP ~$120k/day of new tokens vs $75M volume) [ICP 10-06 NQgq-ulYpcE].
3. Unlock calendar: next date, size as % of circulating, and what price did after the last ones (he checked the last 11 STRK unlocks: higher after 7 days six times, lower five) [STRK 10-10 hTMB4fHaNgc].
4. Offsets: burn and buyback vs emissions (INJ burn offsets ~9% of the mint [INJ 10-07 1JrrfN0U9QA]; RAY buyback ≈ 20× emissions [RAY 10-06 Sv-QuZJrcFw]; VVV burns "one token for every four" created [VVV 10-08 WwoSy_hLO6s]).
5. Staking and locks: share staked, lock lengths, exit queue, unclaimed rewards [ICP 10-06 NQgq-ulYpcE; AVAX 10-07 sZhra8WARrA; VVV 10-08 WwoSy_hLO6s; ETH 10-07 K3AVBoCrDK8].
6. **Verify on-chain.** "I checked the contract again. It's still at 2.71 billion tokens" [FET 10-05 golbI3jN0Zw]. Injective's price sites say 100M tokens, the chain says ~123M, so the real market cap is ~23% higher [INJ 10-07 1JrrfN0U9QA]. ENA's market cap jumped by a third because "the data sites simply changed what they counted" [ENA 10-10 nTPRqKNSGW8].
7. Follow insiders: team-linked wallets → exchanges [TRUMP 10-11 GvE7lGieXag]; foundation buying tokens OTC instead of the market ("that supply found a new owner without touching the price") [AVAX 10-07 sZhra8WARrA; HYPE 10-06 tq-qId4OLdM].
8. Governance can change supply: JUP's "Net Zero Emissions" [JUP 10-10 MyAp_YW8rjI]; Sonic's "No to new mints, period" [S 10-06 _h_LTQaj4dQ]; NEAR's inflation-cut proposal [NEAR 10-08 Gt5gxJxZOMU]; ATOM's tokenomics redesign [ATOM 10-10 nYL0xzMjYG8].

**Rules of thumb (quoted)**
- "Every token is already in circulation. So, we've got no unlocks, we've got no team tokens, and we've also got no token inflation. There's no constant selling pressure from early investors. And that's a problem with most altcoins." [SHIB 10-05 x4Gjk-ur2Kk]
- Inflation: ~2% per annum is "still low" [FET 10-05 golbI3jN0Zw; ADA 10-06 Dp9MJWeGdDs]; RAY's 0.7% is "less than Bitcoins"; VVV's ~2.5% is "very low for an altcoin" [RAY 10-06 Sv-QuZJrcFw; VVV 10-08 WwoSy_hLO6s]; INJ "isn't deflationary yet" at >3% net [INJ 10-07 1JrrfN0U9QA]; ATOM at the 10% maximum is the problem case [ATOM 10-10 nYL0xzMjYG8].
- "That's the constant selling pressure that tends to push altcoins down over time." [S 10-06 _h_LTQaj4dQ]
- "Released doesn't mean sold." and the company's forecast "is the ceiling and it tends to be missed by a wide margin" [HBAR 10-08 fdLi-H8CukM].
- Big one-shot unlocks matter: PYTH's remaining 2.1B (+27%) arrive at once in May, and "the buyback alone is not going to absorb that unlock" [PYTH 10-09 UcM2um0wtHM]; ONDO's Jan 18 unlock adds "more than a third" [ONDO 10-06 KipxCnSMPvc].
- A supply cut only helps if demand exists: "a supply that stops growing only helps when somebody actually uses the chain" [S 10-06 _h_LTQaj4dQ]; "a tight supply alone does not yet move the price. So, somebody has to buy" [KAS 10-09 8xqJ5CJYqYw].

**Examples:** AVAX: shortening the staking lock from 14 to 2 days made big validators leave (staked share 46% → 38%), which cut new issuance ~30% "and nobody had to vote on that" [AVAX 10-07 sZhra8WARrA]. VVV: stakers released ~10× the daily emission, so "it's the stakers that set the supply" [VVV 10-08 WwoSy_hLO6s]. ICP: only claimed rewards become tokens, 20% of supply is unclaimed [ICP 10-06 NQgq-ulYpcE].

**Pitfalls:** stale supply on price sites (INJ); data sites changing circulating-supply definitions (ENA); "paused, not canceled" tokens (JUP: ~1/3 of supply could return by vote) [JUP 10-10 MyAp_YW8rjI]; unclaimed rewards as a hidden overhang (ICP); an undisclosed 25M-token step in circulating supply that equaled "roughly 10 years of the token demand from game trading" [IMX 10-09 9ybKjcs7lik].

---

### Method 6: Buyers vs new supply (flow math)

**Question:** *Do identifiable, steady buyers absorb the new supply?*

**Data:** ETF fund pages (share count, net assets, daily flows); treasury-company releases and filings; buyback dashboards and wallets; the daily or weekly new-supply figure from Method 5.

**Steps**
1. Convert all buyers and the new supply into the **same unit** (tokens/day or $/day).
2. Compute the ratio (buyers ÷ supply).
3. Use **share count, not net assets**, for ETFs: "the share count is the cleaner number, though, because it doesn't move with the price" [HBAR 10-08 fdLi-H8CukM].
4. Separate the launch wave from the steady state: NEAR's ETF took ~$59M, almost all in the first 3 days; steady state ≈ $500k/day ≈ new supply [NEAR 10-08 Gt5gxJxZOMU].
5. Ask who the buyer is: "a listed company tends to simply hold and not sell" [SUI 10-06 KodaC46SpVI]; an ETF is "a buyer that doesn't care about the fee line anymore" [INJ 10-07 1JrrfN0U9QA].
6. Scale the ceiling: how many tokens could an ETF actually buy relative to *liquid* (non-staked) supply [INJ 10-07 1JrrfN0U9QA]; compare ETF AUM share of market cap to Bitcoin's [SOL 10-08 e1OOLAeH_HM].

**Examples**
- **ETH, one week:** ETFs sold ~76k ETH, BitMine bought ~15k, network created ~20k. "For the first time since the summer those buyers did not absorb the new supply. They added to it." [ETH 10-07 K3AVBoCrDK8]
- **NEAR:** ETF ($540k) + buyback (~$65k/day) ≈ 1.3× new supply, "a very thin margin"; ≈ 2× if the inflation cut passes [NEAR 10-08 Gt5gxJxZOMU].
- **LTC:** ETF shares 560k → 880k in a week, about three times what the miners produced that week [LTC 10-07 nQ915SNZ7C4].
- **ZEC:** Grayscale's fund returned ~71,000 ZEC in six trading days, about 7 weeks of miner output [ZEC 10-09 SEqld8bdys0].
- **SOL:** Solana ETFs hold ~$1.9B (<3% of market cap) vs ~6.5% for Bitcoin ETFs; parity would need ~$2.5B, "almost 12 months of new Solana supply" [SOL 10-08 e1OOLAeH_HM].

**Pitfalls**
- Filing ≠ approval: "it's a step but it's not an approval yet … no ticker and there is no date and the fee is still a blank line" [PEPE 10-10 GoOYmdLX3UI].
- ETF size is tiny vs the Dogecoin precedent: all DOGE funds hold ~$17M, "an ETF alone doesn't move a token like this" [PEPE 10-10 GoOYmdLX3UI].
- Product structure: XLM's ETF holds futures, only ~$2.4M [XLM 10-08 muDa7fJBE4w]. "Non-binding" interest from the sponsor's own family fund is not outside money [ZEC 10-09 SEqld8bdys0].
- Redemptions *add* supply [ZEC 10-09 SEqld8bdys0; SOL 10-08 e1OOLAeH_HM]. Buyback tokens may be parked, not burned [NEAR 10-08 Gt5gxJxZOMU].

---

### Method 7: Chain usage and business audit

**Question:** *Is there real, growing demand for the product or blockspace, and who is paying?*

**Data and tools:** TVL (USD *and* in native-token terms), fees and revenue (daily/monthly and by source), stablecoin supply on the chain, transactions, wallets and addresses, DEX volume and share, tokenized-asset totals (rwa.xyz), customers and accounts.

**Steps**
1. Choose 3–5 usage metrics and compare them with 12 months ago and with the cycle low.
2. Restate in token terms when the token itself is most of the TVL: "even measured in ADA, there's roughly 40% less capital in the apps" [ADA 10-06 Dp9MJWeGdDs].
3. Compare fees with market cap: Onyx earns "about $2 per day" against a $175M market cap [XCN 10-08 k2VkjEvJsKo]; Hedera ~$650/day against $4B [HBAR 10-08 fdLi-H8CukM]; Celestia $80/day [TIA 10-09 WWUlLvJruZI].
4. Decompose spikes: *who* is paying? (Raydium's jump came from one launchpad moving its launches [RAY 10-06 Sv-QuZJrcFw]; 98% of ZKsync's "$2M" dashboard fees were one tokenized fund [ZK 10-10 mDG94JOHIbE]; Bonk's launchpad went from $174k to $8.4M in a month [BONK 10-11 KtWfQ3lPqFw].)
5. Look for the **leading line**: "that's the line that turned down before the price did" (Raydium fees halved before the price peaked) [RAY 10-06 Sv-QuZJrcFw].
6. Prefer stablecoin supply over TVL: "the regular TVL numbers for a chain are very volatile because crypto prices go up and down. But stable coins are stable coins" [SOL 10-08 e1OOLAeH_HM]. "Stable coins are dollars that are ready to be used, so that's usually the first thing that comes back" [S 10-06 _h_LTQaj4dQ].
7. For RWA chains use rwa.xyz and holder counts [SOL 10-08 e1OOLAeH_HM; XLM 10-08 muDa7fJBE4w; ONDO 10-06 KipxCnSMPvc].

**Rules of thumb (quoted)**
- "The capital comes first and the fees tend to follow the capital afterward." [SUI 10-09 0pUUjzeP6Mg]
- "Launchpad revenue tends to be the most cyclical money in all of crypto." [RAY 10-06 Sv-QuZJrcFw]
- "The transfer itself is not the business. The business is the activity that follows." [SOL 10-10 qcfzkn-xgUI]
- New/active addresses are "the least reliable of those numbers" (bots) [AVAX 10-07 sZhra8WARrA].
- A chain and an exchange earn money in different ways, so don't compare them naively [HYPE 10-06 tq-qId4OLdM].

**Examples:** Solana's weekly chain fees went from ~$2.4M (June) to ~$7.2M while the price fell; app fees were ~15× chain fees [SOL 10-10 qcfzkn-xgUI]. ADA's stablecoins hit a record (~$67M) while app TVL fell by ~40% [ADA 10-06 Dp9MJWeGdDs].

**Pitfalls**
- Headline throughput can be off-chain: Sui's 40M-TPS record ran in tunnels; only ~20,000 on-chain transactions, "about 0.2% to the daily traffic" [SUI 10-08 yqsYT4pduzg].
- Metrics change meaning: Kaspa's transactions fell 99% because the minimum fee rose 100× and spam vanished; "the old figure measured almost nothing" [KAS 10-09 8xqJ5CJYqYw].
- "Committed" capital is not deposited capital [SUI 10-09 0pUUjzeP6Mg].
- A big stablecoin jump may be a single mint (Hedera $27M → $48M, "a single big mint") [HBAR 10-08 fdLi-H8CukM].

---

### Method 8: Value-accrual check and valuation multiples

**Question:** *Does any of the business growth reach the token, and what price is being paid for it?*

**Data:** fee-switch and buyback status (docs, governance), burn dashboards, staking yields, token rights; annualized revenue or fees; market cap; assets or TVL.

**Steps**
1. **Name the mechanism** by which value reaches the token: buyback, burn, fee share to lockers, or nothing. "Nothing" is common: ZK pays gas in ETH, so holders "don't get a share of the fees" [ZK 10-10 mDG94JOHIbE]; ENA gets no share until USDe reaches $7.5B [ENA 10-10 nTPRqKNSGW8]; ONDO's token "still doesn't get a share" until a fee-switch vote with no date [ONDO 10-06 KipxCnSMPvc]; a Solana transfer pays ~1/20 of a cent [SOL 10-10 qcfzkn-xgUI].
2. **Size the demand from that mechanism** against market cap and against new supply: IMX game-trading demand ≈ $440k/yr = 0.26% of market cap [IMX 10-09 9ybKjcs7lik]; CRV's lock yield 1.9% vs ~4% supply growth [CRV 10-09 aEJrg2aYRyU]; SUI's stablecoin reserve yield ≈ $3M/yr, only part of which buys the token, vs one month of unlocks ≈ $28M [SUI 10-06 KodaC46SpVI]; PYTH buyback ≈ 1% of circulating supply per year [PYTH 10-09 UcM2um0wtHM].
3. **Compute multiples:** market cap ÷ annualized revenue ("years of revenue"); market cap ÷ fees; market cap per $1 of assets or TVL. Use them *relative* to peers and to the same coin's own history.
4. **Track the multiple's direction:** "the token got cheaper while the price went up because the revenue grew faster" [PUMP 10-11 hEkk41geAgs; RAY 10-06 Sv-QuZJrcFw].
5. State what the price *assumes*: "the price assumes that the dollar token grows and that it grows very soon" [ENA 10-10 nTPRqKNSGW8].

**Multiples he cites** (all snapshots)

| Coin | Multiple | Cite |
|---|---|---|
| HYPE | ~24× annualized protocol revenue (23× three weeks earlier) | [HYPE 10-06 tq-qId4OLdM] |
| JUP | ~17× | [JUP 10-10 MyAp_YW8rjI] |
| RAY | ~12 years of revenue → < 6 years | [RAY 10-06 Sv-QuZJrcFw] |
| ORCA | ~21× (Raydium ~24×) | [ORCA 10-07 MSUv-hvKgMU] |
| PONS | ~4.3 years (pump.fun ~4.6) | [PONS 10-07 w_p5KQgkYNc] |
| PUMP | ~3× annualized revenue | [PUMP 10-11 hEkk41geAgs] |
| UNI | ~53× annualized burn | [UNI 10-09 LgOyfBiX_4I] |
| SUI vs SOL vs AVAX vs HYPE | ~1,700× / ~190× / ~900× / ~17× market cap ÷ annual fees | [SUI 10-11 iWOCnQuLA4c] |
| ONDO | 72¢ → 63¢ of market cap per $1 of assets | [ONDO 10-06 KipxCnSMPvc] |
| ETH | market cap ≈ 2,000× → 1,500× annual fees | [ETH 10-07 K3AVBoCrDK8] |
| SOL | new supply ≈ 7× the fees users pay | [SOL 10-08 e1OOLAeH_HM] |

**Rules of thumb (quoted)**
- "I don't think 24 times annual revenue is that expensive" for "a market leader that's growing" [HYPE 10-06 tq-qId4OLdM].
- "17 times the revenue is not paying for a boom either" [JUP 10-10 MyAp_YW8rjI].
- "So, we are not buying earnings here. We are buying the potential turnaround, and the turnaround needs trust." [S 10-06 _h_LTQaj4dQ]
- "We are not paying for the usage here at all. We are paying for a plan … I simply don't want to pay for that in advance." [XCN 10-08 k2VkjEvJsKo]
- "The token does not get paid for volume. It gets paid through the burn." [UNI 10-09 LgOyfBiX_4I]

**Pitfalls**
- Protocol revenue ≠ total fees: pump.fun kept ~$18M of ~$51M in fees [PUMP 10-11 hEkk41geAgs]; the PYTH DAO receives ~60 cents of each customer dollar, the developer company keeps ~40 [PYTH 10-09 UcM2um0wtHM].
- A headline buyback can be negligible against unlocks (SUI) or "manual … not locked in code" (Pons) [PONS 10-07 w_p5KQgkYNc].
- Revenue concentrated in a rented source (StonkFun earned ~4× what Raydium itself earned in the month) [RAY 10-06 Sv-QuZJrcFw]; Bonk Inc.'s own filing raises "substantial doubt" about continuing, and he cannot see the burn in the supply [BONK 10-11 KtWfQ3lPqFw].
- Multiple depends on which pace you annualize: UNI's burn at September's pace vs last week's decides "cheap vs still expensive"; "which pace is the real one? I don't know that yet" [UNI 10-09 LgOyfBiX_4I]. BONK ~3× fees at the September pace vs ~80× at the Q2 pace [BONK 10-11 KtWfQ3lPqFw].

---

### Method 9: Relative-valuation (ratio) charts

**Question:** *Is this coin cheap or expensive versus its alternatives, independent of crypto's general ups and downs, and what is the risk/reward?* This is the method he leans on most for timing.

**Data and tools:** a charting tool (his descriptions link TradingView). The ratio series he builds:
- coin ÷ **BTC**; coin ÷ **ETH** (because "there is more correlation between Ethereum and the altcoins compared to Bitcoin and the altcoins" [QNT 10-07 0HkozsaJpzQ]);
- coin ÷ **"others"**: the market cap of all altcoins outside the top 10 ("we divide hype by others, and others is the market cap of all the altcoins that are not in the top 10" [HYPE 10-06 tq-qId4OLdM]);
- **dominance**: coin market cap ÷ total crypto market cap (and an ex-stablecoin version) [INJ 10-07 1JrrfN0U9QA; NEAR 10-08 Gt5gxJxZOMU; HBAR 10-08 fdLi-H8CukM; XLM 10-08 muDa7fJBE4w; SUI 10-08 yqsYT4pduzg; SOL 10-08 e1OOLAeH_HM; BTC 10-08 RiWS7k2O46E];
- coin ÷ **ecosystem or peer**: ÷ SOL for JUP, PUMP, PYTH, BONK, TRUMP [JUP 10-10 MyAp_YW8rjI; PUMP 10-11 hEkk41geAgs; PYTH 10-09 UcM2um0wtHM; BONK 10-11 KtWfQ3lPqFw; TRUMP 10-11 GvE7lGieXag]; ÷ Bittensor for FET [FET 10-05 golbI3jN0Zw].

**Steps**
1. Pick the benchmark that fits the question (see the list above).
2. Mark the **equilibrium** ("the dotted line, that's the long-term average ratio"), the trading range or channel, prior ratio all-time highs, and support/resistance.
3. Measure percentage distance from the current ratio to each level. That *is* the risk/reward, expressed as "outperformance" or "underperformance":
   - HBAR dominance: about −15% risk vs +350% potential [HBAR 10-08 fdLi-H8CukM];
   - ADA/BTC: −23% to the low vs +342% to equilibrium [ADA 10-06 Dp9MJWeGdDs];
   - CRV: −28% vs more than +150% [CRV 10-09 aEJrg2aYRyU];
   - FET/others: about +200% to equilibrium [FET 10-05 golbI3jN0Zw];
   - ENA/ETH: needs +20% to +70% outperformance or ≈ −70% [ENA 10-10 nTPRqKNSGW8].
4. Identify the regime: **stabilizing** (underperformance slowing, higher lows) vs **persistent decline** (lower highs and lows). He often explains stabilization by better tokenomics, using Zcash as the analogy: it stopped bleeding against Bitcoin once halvings cut supply, then outperformed by "more than 5,000%" from the bottom [ICP 10-06 NQgq-ulYpcE]; TIA, KAS and PYTH get the same treatment [TIA 10-09 WWUlLvJruZI; KAS 10-09 8xqJ5CJYqYw; PYTH 10-09 UcM2um0wtHM].
5. Require a **clean breakout**: "just 5% or 10% above the resistance is probably not enough. We might need 20% or even 30%" [IMX 10-09 9ybKjcs7lik].
6. Use the chart to plan the trade: wait for the breakout rather than catching a falling knife [PONS 10-07 w_p5KQgkYNc]; place a "tight stop-loss" near support, or "set a buy order above the current price" for a breakout [PEPE 10-10 GoOYmdLX3UI]; treat the upper range as a place to sell: "we get an idea when we should potentially sell" [ORCA 10-07 MSUv-hvKgMU].

**Rules of thumb (quoted)**
- "Whenever we buy an altcoin, we're taking inherently more risk compared to just buying Bitcoin and Ethereum. And that additional risk needs to get compensated." [ONDO 10-06 KipxCnSMPvc]
- "If you just want to get crypto exposure, we just buy Bitcoin. If we want to buy an altcoin, we should always do that with the expectation of that altcoin doing better than the rest." [SUI 10-06 KodaC46SpVI]
- "Investing is all about opportunity cost." [ETH 10-07 K3AVBoCrDK8]
- "Most altcoins long-term tend to underperform Bitcoin." [SUI 10-06 KodaC46SpVI]
- "In a way, [Injective / Cardano / Solana] is a levered bet on all of crypto": a rising dominance line needs a rising Bitcoin [INJ 10-07 1JrrfN0U9QA; ADA 10-06 Dp9MJWeGdDs; SOL 10-08 e1OOLAeH_HM].
- "Every time the token rallies it's a profit taking opportunity" for chronic underperformers [ATOM 10-10 nYL0xzMjYG8; DOT 10-10 r3CkKUqxH3U; LTC 10-07 nQ915SNZ7C4].

**Examples**
- **HBAR dominance** from 0.01% to 0.15% with parallel trend lines [HBAR 10-08 fdLi-H8CukM].
- **ATOM** "one of the worst charts I've seen in crypto for a while" (about −99% vs the rest of the altcoin market since launch) [ATOM 10-10 nYL0xzMjYG8]. **DOT** −98% over 5 years [DOT 10-10 r3CkKUqxH3U].
- **Bitcoin dominance** looked healthy raw but "does not look that healthy on the stablecoin adjusted dominance chart", which broke support [BTC 10-08 RiWS7k2O46E].

**Pitfalls**
- USD charts hide this: "If we just look at the US dollar charts, we mainly just get the general crypto ups and downs" [ORCA 10-07 MSUv-hvKgMU].
- Trendlines can be arbitrary: he notes the BTC dominance line "is drawn rather arbitrarily" before switching to the ex-stablecoin version [BTC 10-08 RiWS7k2O46E].
- Upside numbers are optimistic bookends: "this is very, very optimistic … probably better to be somewhat cautious and draw the resistance like so" (Orca: +240% vs +95%) [ORCA 10-07 MSUv-hvKgMU]. For STX he offers two competing readings of the same chart (equilibrium vs declining trend) [STX 10-11 PTBr4ZxRSVI].
- Mean reversion isn't guaranteed: ATOM "never made a new high" after launch [ATOM 10-10 nYL0xzMjYG8]. He acknowledges the chart can be self-fulfilling: "sometimes things simply become a self-fulfilling prophecy" [XCN 10-08 k2VkjEvJsKo].

---

### Method 10: Primary-source verification (headline vs fact)

**Question:** *What did the announcement actually say, is it live or just proposed, and who benefits?*

**Data and tools:** governance forum and proposal pages; block explorers and raw transactions; ETF fund pages and amended filings; company quarterly filings; protocol docs and blog posts; the regulator's actual list; the original article rather than the headline.

**Steps**
1. Read the primary document (proposal text, filing, docs, explorer), not the summary.
2. **Classify each catalyst's status:** hint / idea / draft / proposal / voted / testnet / mainnet / live / has a customer. Look for status words: "committed", "considering", "non-binding", "amended", "not in production".
3. **Follow the tokens on-chain** when the story is a transfer: for the 620M-XCN "exploit" he traced the wallet, the stake, proposal #71 and the vote count, concluded it was likely a planned migration, and still flagged the governance weakness [XCN 10-08 k2VkjEvJsKo].
4. Ask what the token itself gets from the news (Method 8).
5. Check whether it is old news repackaged: the XLM "declared a commodity" headline was a March list of 16 tokens; "that's actually not what happened" [XLM 10-08 muDa7fJBE4w].

**Rules of thumb (quoted)**
- "My whole view on [Sui] depends on that one word": *committed*; "that money is not on the chain yet … it's a promise for now" [SUI 10-09 0pUUjzeP6Mg].
- "There is no proposal, and there is no vote. There's a post, and there's a target. So it is an idea and the market priced it like a decision." [STRK 10-10 hTMB4fHaNgc]
- "The market tends to pay for contracts and not for hints." [QNT 10-11 R1nqM9s6W_w]
- "So, so far there is no customer. That's probably why the price didn't react." [SOL 10-08 e1OOLAeH_HM]
- "I can't judge a deal that I'm not allowed to see." [ORCA 10-07 MSUv-hvKgMU]
- "The label brought in the permission, it didn't bring in any buyers for the token." [XLM 10-08 muDa7fJBE4w]

**Examples:** Samsung "82 million" are devices, not users, and the announcement names Solana as well as Sui [SOL 10-10 qcfzkn-xgUI; SUI 10-11 iWOCnQuLA4c]. Cardano's MasterCard and Petrobras headlines "brought attention, but they didn't create new demand for the token" (>100 firms are in the MasterCard programme; Petrobras is research) [ADA 10-06 Dp9MJWeGdDs]. ZEC's "$100 million" is non-binding interest from the sponsor's family fund [ZEC 10-09 SEqld8bdys0].

**Pitfalls:** quorum is tiny on many votes: Polkadot's stablecoin passed with 98% but only 0.11% of DOT voted, "around 100 accounts decided" [DOT 10-10 r3CkKUqxH3U]; Orca's proposal passes at ~4% of supply [ORCA 10-07 MSUv-hvKgMU]; <$1M of XCN tokens could move 620M from a treasury [XCN 10-08 k2VkjEvJsKo].

---

### Method 11: Catalyst calendar, thresholds and "what would change my mind"

**Question:** *What happens next, when, and which number proves me wrong?*

**Data:** governance calendars; unlock schedules; ETF decision windows; upgrade dates; scheduled filings; daily or weekly published metrics (burn, ETF share count, staked share, fees).

**Steps**
1. List dated events (votes, unlocks, upgrades, decisions, filings) and mark each *confirmed* or *penciled in*. ETH's Hoodie testnet (Oct 26) and mainnet (Dec 2) are "neither of them confirmed" [ETH 10-07 K3AVBoCrDK8].
2. For each coin, set one **bullish trigger** and one **bearish/exit trigger**, each an observable number published at least weekly.
3. Prefer numbers you can read directly from the chain or a fund page.
4. State how you will act on each trigger (add, trim, exit, flip to short, or hedge).
5. Re-check on the schedule and publish an update ("I will continue to publish updates").

**His explicit thresholds**

| Coin | Trigger | Action | Cite |
|---|---|---|---|
| HBAR | ETF shares fall below 5.75M (now 5.94M) | give up; short HBAR, hedged with long BTC | [HBAR 10-08 fdLi-H8CukM] |
| LTC | ETF shares stay at 880k and Binance OI back above 1.7M tokens | consider shorting; "880,000 is the number to beat" | [LTC 10-07 nQ915SNZ7C4] |
| AVAX | staked share < 35% (now 38%) | "Below 35% I am out" | [AVAX 10-07 sZhra8WARrA] |
| UNI | weekly burn back toward ~$3M (now $1.7M) = recovery; below $1M with high volume | stop treating UNI as a token that pays holders | [UNI 10-09 LgOyfBiX_4I] |
| QNT | daily close above $270 (rejected on 3 days) / above $278 with spot volume > $100M/day | add; target prior high ~30% above | [QNT 10-08 g8FjETXl2V4; QNT 10-06 2bwkNjZjHy0] |
| FET | daily close above 28¢ (4th test of 26–28¢) or a dip to ~22¢ | add; no extra leverage | [FET 10-05 golbI3jN0Zw] |
| HYPE | a month with > $100M fees (≈ 22× revenue); ETF flows turn positive | more bullish | [HYPE 10-06 tq-qId4OLdM] |
| ONDO | stock-token platform above $1.5B; a date for the fee-switch vote | more bullish before the Jan 18 unlock | [ONDO 10-06 KipxCnSMPvc] |
| SUI | Hashi live for a month without TVL rising / stablecoins on Sui not clearly up by mid-Nov | cut the position | [SUI 10-09 0pUUjzeP6Mg; SUI 10-11 iWOCnQuLA4c] |
| SOL | weekly fees < $5M while headlines continue | adoption isn't turning into activity | [SOL 10-10 qcfzkn-xgUI] |
| ZEC | next green daily inflow for the Grayscale fund (positive); OI rising while the fund shrinks (negative) | follow the flow | [ZEC 10-09 SEqld8bdys0] |
| Sonic | independent supply audit due Oct 13 | clean → bigger position; more tokens than reported → "I don't want to be in this anymore" | [S 10-06 _h_LTQaj4dQ] |
| STX | a published fill number for bond #2; sBTC supply clearly up; bond #3 with more institutional capacity | otherwise "holders front running a story" | [STX 10-11 PTBr4ZxRSVI] |
| ATOM | a published tokenomics proposal with real numbers (good) vs silence until end of December (bad) | | [ATOM 10-10 nYL0xzMjYG8] |
| KAS | spot volume back above $20M/day | needed for the rally to continue | [KAS 10-09 8xqJ5CJYqYw] |
| PEPE | daily volume > $400M without futures doubling; funding staying negative; Canary files fee and ticker | turns into a buy | [PEPE 10-10 GoOYmdLX3UI] |
| XLM | spot-ETF filing; stablecoins on Stellar above $1B and holding; DTCC launch date | more bullish | [XLM 10-08 muDa7fJBE4w] |
| CRV | monthly volume back above $6B; fee-share vote outcome; Yield Basis paying lockers | more bullish | [CRV 10-09 aEJrg2aYRyU] |
| AERO | new weekly supply clearly below ~4M tokens after Oct 21 | the cap works; "the first week after the launch settles it" | [AERO 10-11 pJaT2HqKppg] |
| BONK | Bonk Inc.'s Q3 filing (expected mid-Nov): token balance clearly up or flat | mechanism works vs "September money went somewhere else" | [BONK 10-11 KtWfQ3lPqFw] |

**Pitfalls:** dates slip (Aerodrome's launch "already slipped two times" [AERO 10-11 pJaT2HqKppg]; ZKsync's upgrade was delayed after the Security Council found problems [ZK 10-10 mDG94JOHIbE]); the SEC can delay (ADA: "this is not a guarantee at all") [ADA 10-06 Dp9MJWeGdDs]; "the price tends to move before we get that kind of data" [AERO 10-11 pJaT2HqKppg].

---

### Method 12: Sector, peer and attention context

**Question:** *Is this idiosyncratic, or part of a sector rotation, and is retail attention present?*

**Data:** peer performance tables over 30 days; sector reports (Grayscale); Upbit ranking; his own YouTube Studio analytics.

**Steps**
1. Compare with the 2–4 closest peers over 30 days (FET vs Bittensor and Render [FET 10-05 golbI3jN0Zw]; IMX vs Sandbox, Beam, Axie [IMX 10-09 9ybKjcs7lik]; SHIB vs DOGE and PEPE [SHIB 10-05 x4Gjk-ur2Kk]; PEPE as a share of SHIB's market cap [PEPE 10-10 GoOYmdLX3UI]).
2. If the whole sector moved, say so, and note the idiosyncratic angle is missing: "the price is paying for the gaming sector and not for anything that changed at Immutable" [IMX 10-09 9ybKjcs7lik].
3. Check retail attention through his own channel analytics: Cardano's video from 204 days earlier "still has above average attention" [ADA 10-06 Dp9MJWeGdDs]; the prior ONDO update had ~50% more views than average [ONDO 10-06 KipxCnSMPvc]; the prior HYPE video ~53% more [HYPE 10-06 tq-qId4OLdM].
4. Note regional flows: South Korean retail rotating into gaming tokens (Upbit ranking) [BEAM 10-05 QwRkPAiX5fc].

**Rules of thumb:** "A small market cap tends to move the most when money arrives" [BEAM 10-05 QwRkPAiX5fc]. A sector rally means a token "doesn't need" a special story, but also gives you no idiosyncratic edge [SHIB 10-05 x4Gjk-ur2Kk].

**Pitfalls:** his attention metric is his own audience, which is biased; he does not claim otherwise. Sector narratives can be a story told after the fact ("I couldn't find any news that explains why gaming tokens are in demand again") [IMX 10-09 9ybKjcs7lik].

---

### Method 13: Position expression and risk rules

**Question:** *Given the analysis, how should it be acted on?*

**Rules (quoted or close to it)**
- **Split by time frame.** "Short-term the numbers decide, long-term the ETF does" [INJ 10-07 1JrrfN0U9QA]; "the time frame needs to be at least 12 months, not just a few weeks" [JUP 10-10 MyAp_YW8rjI]; "Short-term, it's a range. Long-term, it's becoming interesting" [QNT 10-11 R1nqM9s6W_w].
- **Add on dips, not on green days.** "I wouldn't buy a full position on a green day" [ICP 10-06 NQgq-ulYpcE]; "I would rather accumulate RAY on dips than chase this after a green week" [RAY 10-06 Sv-QuZJrcFw]; "I wouldn't chase the recent lever rally" [HYPE 10-06 tq-qId4OLdM]; "rather buy on a dip though than chasing the short-term pump" [SUI 10-06 KodaC46SpVI].
- **Don't add leverage** to an already leveraged asset: "it probably does not make sense to add more leverage to that" [FET 10-05 golbI3jN0Zw]; "leverage is not necessarily making sense here in either direction" [QNT 10-06 2bwkNjZjHy0]; "I wouldn't bet on that date with leverage" [ADA 10-06 Dp9MJWeGdDs].
- **Size by uncertainty.** Small until a binary event resolves ("I'd keep that position small until we do know" [S 10-06 _h_LTQaj4dQ]); "a smaller position might make sense" until the ETF decision [INJ 10-07 1JrrfN0U9QA]; "an additional allocation … it shouldn't be the main allocation" [AVAX 10-07 sZhra8WARrA].
- **Trade vs allocation.** "A potential trade that has to be managed actively" [AVAX 10-07 sZhra8WARrA]; stop-loss for active traders [QNT 10-11 R1nqM9s6W_w]; tight stops near support [PEPE 10-10 GoOYmdLX3UI].
- **You can short the losers, or pair-trade.** "We don't always have to find the winners. We can make money by betting on falling prices of the losers as well" [LTC 10-07 nQ915SNZ7C4]; the pair "we buy Bitcoin and we short Polka dot" [DOT 10-10 r3CkKUqxH3U]; short HBAR and "potentially hedge this with a rising Bitcoin price. So, we cancel out the general macro" [HBAR 10-08 fdLi-H8CukM]. But he also won't short an asset that can squeeze: "we could get wrecked very quickly" [XCN 10-08 k2VkjEvJsKo]; shorting SHIB only after another 100–150% surprise rally [SHIB 10-05 x4Gjk-ur2Kk].
- **It's fine to pass.** "I'd rather be late than early here" [PONS 10-07 w_p5KQgkYNc]; "it's probably better to stay out of the official Trump token for now" [TRUMP 10-11 GvE7lGieXag]; "I'm not going to tell you to buy or sell here. It's simply too early for that. We don't have enough data" [ORCA 10-07 MSUv-hvKgMU].
- **Keep holding when the thesis holds, ignore noise.** "Selling Bitcoin just because the trading volume is low doesn't make sense to me" [BTC 10-08 RiWS7k2O46E].

**Pitfalls he warns about:** rallies built on leverage fade (ATOM [ATOM 10-10 nYL0xzMjYG8]); a headline is not a demand source (ADA, SOL, QNT); holding an asset for years "without any fundamentals changing is probably not that great" [BONK 10-11 KtWfQ3lPqFw]; one-sided crowds: "the crowd has not given up yet, and the real low tends to look different" [PEPE 10-10 GoOYmdLX3UI].

---

## 4. Quick-reference thresholds (as he states them)

| Metric | Reading he treats as… | Cite |
|---|---|---|
| Binance funding ≈ 11% p.a. | normal; ≤ 5% below normal; negative = shorts paying ("closer to a low") | [FET 10-05 golbI3jN0Zw; ETH 10-07 K3AVBoCrDK8; XLM 10-08 muDa7fJBE4w] |
| OI ÷ market cap | ~2–3% very low · 6–8% small/moderate · 16%+ high · 20%+ very elevated · 38% "quite high" | [SHIB 10-05 x4Gjk-ur2Kk; STX 10-11 PTBr4ZxRSVI; ICP 10-06 NQgq-ulYpcE; STRK 10-10 hTMB4fHaNgc; NEAR 10-08 Gt5gxJxZOMU; CRV 10-09 aEJrg2aYRyU] |
| Perp : spot volume | 3–4× normal · 8×+ leverage sets the price · ≤ 1× unusual | [SUI 10-06 KodaC46SpVI; HYPE 10-06 tq-qId4OLdM; SHIB 10-05 x4Gjk-ur2Kk] |
| Token inflation | ~2% p.a. "still low" · < 1% very low · > 3% net "isn't deflationary yet" · 10% (ATOM) is the maximum the rules allow and the selling "is real" | [ADA 10-06 Dp9MJWeGdDs; RAY 10-06 Sv-QuZJrcFw; INJ 10-07 1JrrfN0U9QA; ATOM 10-10 nYL0xzMjYG8] |
| Buyers ÷ new supply | LTC ETF ≈ 3× weekly miner output: "a good sign" · ~1.3× (NEAR) "a very thin margin" · < 1× (ETH) "added to it" | [LTC 10-07 nQ915SNZ7C4; NEAR 10-08 Gt5gxJxZOMU; ETH 10-07 K3AVBoCrDK8] |
| Breakout on a ratio chart | 5–10% above resistance not enough; 20–30% needed | [IMX 10-09 9ybKjcs7lik] |
| Revenue multiple | ~17–24× for a growing leader is "not that expensive"; PUMP ~3× and he is buying; UNI ~53× at last week's burn pace is "still expensive" | [HYPE 10-06 tq-qId4OLdM; JUP 10-10 MyAp_YW8rjI; PUMP 10-11 hEkk41geAgs; UNI 10-09 LgOyfBiX_4I] |
| Staked share (AVAX) | < 35% = exit | [AVAX 10-07 sZhra8WARrA] |
| Average recent-buyer price vs spot | spot at or near the average = "a very thin cushion" | [QNT 10-07 0HkozsaJpzQ] |

## 5. What he rarely covers (gaps to fill yourself)

- **Team, investors and cap tables.** Team/backer identity appears only when it *is* the catalyst (BlackRock on ONDO, the Clearing House on QNT, Stripe on USDsui, JPMorgan on Solana DvP, the new Sonic CEO, the Trump companies on TRUMP).
- **Security audits and smart-contract risk** beyond specific incidents (Onyx, Cosmos/Neutron, the FET partner hack).
- **Sources for TVL, fees and stablecoin data** are mostly unnamed; replicate with DefiLlama-style aggregators, but expect small differences.
- **Valuation vs private-market or earnings-based benchmarks.** He uses crypto-native revenue multiples and peers only.
- **Counter-thesis testing of his own picks**: he states bull and bear cases for each coin but doesn't publish a loss log (see caveats in section 0).

---

## 6. Checklist: Analyze a project like Gerhard

Work through these in order. Write down a number for each step; if you can't find one, write "unknown", because he does the same.

1. **Frame the move.** Price, market cap, one-sentence description, the move vs BTC over 7d / 30d / 12 months, and what is *not* known (no news, no listing, no upgrade).
2. **Market or coin?** On a sell-off or rally day, find the BTC move and liquidation total and compare the coin's beta. If the coin simply followed, stop.
3. **Name what the token is a claim on.** Gas, governance only, fee share, buyback, burn, or nothing. If "nothing", the rest is a bet on a future change.
4. **Audit leverage** (open interest in tokens vs price; OI ÷ market cap; funding vs ~11% normal; liquidations; perp : spot volume; long/short split; did OI move before or after price?).
5. **Audit spot buying** (turnover; Binance + Coinbase only; Korea/Upbit; Coinbase tape; average price paid by recent buyers vs now; exchange reserves; whales).
6. **Audit supply** (circulating %; fully diluted; inflation in % and $/day vs volume; unlock dates and sizes; burn and buyback vs emissions; staking share, locks, exit queue; insider wallets). **Verify the supply number on-chain.**
7. **Do the flow math.** ETF share counts, treasury companies, buybacks, in tokens/day vs new supply. Note the ratio and whether the buyers are steady or a launch wave.
8. **Audit usage and the business.** TVL (also in token terms), fees by source, stablecoin supply, transactions, customers. Ask who pays, what's rented, what leads and what lags.
9. **Check value accrual and multiples.** How much of the business reaches the token (size it in $/year vs market cap)? Compute market cap ÷ revenue/fees/assets and compare with peers and with its own past.
10. **Draw the ratio charts** (coin ÷ BTC, ÷ ETH, ÷ "others", dominance, ÷ ecosystem/peer). Mark equilibrium, range, support, resistance; compute % to each; classify the regime (stabilizing vs declining); require a clean breakout.
11. **Verify every headline in the primary source.** Status (hint / proposal / voted / testnet / live), who benefits, quorum, "committed" vs deposited, old news repackaged.
12. **Sector and attention check.** Peers over 30 days; sector rotation; regional flows; how much retail interest.
13. **Write the bull case and the bear case in full**, each with its numbers.
14. **Give the verdict by time frame** (next weeks vs 12 months) and the position style: hold, add on dips (never on a green day), small position, or pass. Consider a short or a BTC-hedged pair if the chart and fundamentals are both bad.
15. **Set triggers.** One or two bullish and one bearish/exit trigger, each a published number or a date, with the action tied to each.
16. **No leverage on a leveraged asset;** size smaller when a binary event is pending; use a stop only for trades, not for allocations.
17. **Schedule the re-check** and compare against your last note: what changed, and did the triggers fire?
18. **Remember the disclaimer:** this is a research process, not advice.

---

## Appendix A: Index of coins by video

See `recap-table.md` for the per-coin angle table, sentiment and scores.

## Appendix B: Video lookup (tag → title, URL)

| Tag | Coin | Title | URL |
|---|---|---|---|
| `[BEAM 10-05 QwRkPAiX5fc]` | BEAM | Why Beam Is Exploding - BEAM Crypto Analysis | https://www.youtube.com/watch?v=QwRkPAiX5fc |
| `[FET 10-05 golbI3jN0Zw]` | FET | Fetch AI Is Waking Up - FET Crypto Analysis | https://www.youtube.com/watch?v=golbI3jN0Zw |
| `[SHIB 10-05 x4Gjk-ur2Kk]` | SHIB | Is Shiba Inu Set To Boom? - SHIB Crypto Analysis | https://www.youtube.com/watch?v=x4Gjk-ur2Kk |
| `[ADA 10-06 Dp9MJWeGdDs]` | ADA | Cardano Buyers Are Back - ADA Crypto Analysis | https://www.youtube.com/watch?v=Dp9MJWeGdDs |
| `[HYPE 10-06 tq-qId4OLdM]` | HYPE | Hyperliquid Keeps Winning - HYPE Crypto Analysis | https://www.youtube.com/watch?v=tq-qId4OLdM |
| `[ICP 10-06 NQgq-ulYpcE]` | ICP | Why Internet Computer Is Up - ICP Crypto Analysis | https://www.youtube.com/watch?v=NQgq-ulYpcE |
| `[ONDO 10-06 KipxCnSMPvc]` | ONDO | Ondo Assets Hit A Record - ONDO Crypto Analysis | https://www.youtube.com/watch?v=KipxCnSMPvc |
| `[QNT 10-06 2bwkNjZjHy0]` | QNT | Quant Bears Are Giving Up - QNT Crypto Analysis | https://www.youtube.com/watch?v=2bwkNjZjHy0 |
| `[RAY 10-06 Sv-QuZJrcFw]` | RAY | Raydium Revenue Just Went 5x - RAY Crypto Analysis | https://www.youtube.com/watch?v=Sv-QuZJrcFw |
| `[S 10-06 _h_LTQaj4dQ]` | S | Sonic Is Turning Around - S Crypto Analysis | https://www.youtube.com/watch?v=_h_LTQaj4dQ |
| `[SUI 10-06 KodaC46SpVI]` | SUI | Big Money Is Buying Sui - SUI Crypto Analysis | https://www.youtube.com/watch?v=KodaC46SpVI |
| `[AVAX 10-07 sZhra8WARrA]` | AVAX | Avalanche Supply Shock - AVAX Crypto Analysis | https://www.youtube.com/watch?v=sZhra8WARrA |
| `[ETH 10-07 K3AVBoCrDK8]` | ETH | Ethereum Upgrade Is Close - ETH Crypto Analysis | https://www.youtube.com/watch?v=K3AVBoCrDK8 |
| `[INJ 10-07 1JrrfN0U9QA]` | INJ | How High Can Injective Go? - INJ Crypto Analysis | https://www.youtube.com/watch?v=1JrrfN0U9QA |
| `[LTC 10-07 nQ915SNZ7C4]` | LTC | Is Litecoin Set To Boom? - LTC Crypto Analysis | https://www.youtube.com/watch?v=nQ915SNZ7C4 |
| `[ORCA 10-07 MSUv-hvKgMU]` | ORCA | Why Orca Just Doubled - ORCA Crypto Analysis | https://www.youtube.com/watch?v=MSUv-hvKgMU |
| `[PONS 10-07 w_p5KQgkYNc]` | PONS | Pons Fees Are Collapsing - PONS Crypto Analysis | https://www.youtube.com/watch?v=w_p5KQgkYNc |
| `[QNT 10-07 0HkozsaJpzQ]` | QNT | Who Is Buying Quant? - QNT Crypto Analysis | https://www.youtube.com/watch?v=0HkozsaJpzQ |
| `[BTC 10-08 RiWS7k2O46E]` | BTC | Bitcoin Whales Are Loading Up - BTC Crypto Analysis | https://www.youtube.com/watch?v=RiWS7k2O46E |
| `[HBAR 10-08 fdLi-H8CukM]` | HBAR | Hedera ETF Keeps Buying - HBAR Crypto Analysis | https://www.youtube.com/watch?v=fdLi-H8CukM |
| `[NEAR 10-08 Gt5gxJxZOMU]` | NEAR | NEAR Protocol Buyers Beat Supply - NEAR Crypto Analysis | https://www.youtube.com/watch?v=Gt5gxJxZOMU |
| `[QNT 10-08 g8FjETXl2V4]` | QNT | Big Buyer Steps In On Quant - QNT Crypto Analysis | https://www.youtube.com/watch?v=g8FjETXl2V4 |
| `[SOL 10-08 e1OOLAeH_HM]` | SOL | Banks Are Coming To Solana - SOL Crypto Analysis | https://www.youtube.com/watch?v=e1OOLAeH_HM |
| `[SUI 10-08 yqsYT4pduzg]` | SUI | Sui Just Broke A World Record - SUI Crypto Analysis | https://www.youtube.com/watch?v=yqsYT4pduzg |
| `[VVV 10-08 WwoSy_hLO6s]` | VVV | Venice Supply Shock Is Coming - VVV Crypto Analysis | https://www.youtube.com/watch?v=WwoSy_hLO6s |
| `[XCN 10-08 k2VkjEvJsKo]` | XCN | Onyxcoin Has A Big Problem - XCN Crypto Analysis | https://www.youtube.com/watch?v=k2VkjEvJsKo |
| `[XLM 10-08 muDa7fJBE4w]` | XLM | Stellar Funds Are Growing Fast - XLM Crypto Analysis | https://www.youtube.com/watch?v=muDa7fJBE4w |
| `[CRV 10-09 aEJrg2aYRyU]` | CRV | Curve Supply Is Drying Up - CRV Crypto Analysis | https://www.youtube.com/watch?v=aEJrg2aYRyU |
| `[IMX 10-09 9ybKjcs7lik]` | IMX | Who Is Buying Immutable? - IMX Crypto Analysis | https://www.youtube.com/watch?v=9ybKjcs7lik |
| `[KAS 10-09 8xqJ5CJYqYw]` | KAS | Kaspa Supply Is Running Out - KAS Crypto Analysis | https://www.youtube.com/watch?v=8xqJ5CJYqYw |
| `[PYTH 10-09 UcM2um0wtHM]` | PYTH | Pyth Network Buyback Is Live - PYTH Crypto Analysis | https://www.youtube.com/watch?v=UcM2um0wtHM |
| `[SUI 10-09 0pUUjzeP6Mg]` | SUI | Sui Lands Half A Billion - SUI Crypto Analysis | https://www.youtube.com/watch?v=0pUUjzeP6Mg |
| `[TIA 10-09 WWUlLvJruZI]` | TIA | Why Is Celestia Going Up? - TIA Crypto Analysis | https://www.youtube.com/watch?v=WWUlLvJruZI |
| `[UNI 10-09 LgOyfBiX_4I]` | UNI | Why Uniswap Just Dropped - UNI Crypto Analysis | https://www.youtube.com/watch?v=LgOyfBiX_4I |
| `[ZEC 10-09 SEqld8bdys0]` | ZEC | Zcash Gets A Cheaper ETF - ZEC Crypto Analysis | https://www.youtube.com/watch?v=SEqld8bdys0 |
| `[ATOM 10-10 nYL0xzMjYG8]` | ATOM | Cosmos Is Waking Up - ATOM Crypto Analysis | https://www.youtube.com/watch?v=nYL0xzMjYG8 |
| `[DOT 10-10 r3CkKUqxH3U]` | DOT | Polkadot Stablecoin Is Live - DOT Crypto Analysis | https://www.youtube.com/watch?v=r3CkKUqxH3U |
| `[ENA 10-10 nTPRqKNSGW8]` | ENA | How High Can Ethena Go Now? - ENA Crypto Analysis | https://www.youtube.com/watch?v=nTPRqKNSGW8 |
| `[JUP 10-10 MyAp_YW8rjI]` | JUP | Who Is Buying Jupiter Now? - JUP Crypto Analysis | https://www.youtube.com/watch?v=MyAp_YW8rjI |
| `[PEPE 10-10 GoOYmdLX3UI]` | PEPE | Pepe ETF Is Getting Closer - PEPE Crypto Analysis | https://www.youtube.com/watch?v=GoOYmdLX3UI |
| `[SOL 10-10 qcfzkn-xgUI]` | SOL | Solana Lands On Samsung Phones - SOL Crypto Analysis | https://www.youtube.com/watch?v=qcfzkn-xgUI |
| `[STRK 10-10 hTMB4fHaNgc]` | STRK | Starknet Plans A Big Move - STRK Crypto Analysis | https://www.youtube.com/watch?v=hTMB4fHaNgc |
| `[ZK 10-10 mDG94JOHIbE]` | ZK | ZKsync Is Waking Up - ZK Crypto Analysis | https://www.youtube.com/watch?v=mDG94JOHIbE |
| `[AERO 10-11 pJaT2HqKppg]` | AERO | Aerodrome Changes In 10 Days - AERO Crypto Analysis | https://www.youtube.com/watch?v=pJaT2HqKppg |
| `[BONK 10-11 KtWfQ3lPqFw]` | BONK | Bonk Is Making Money Again - BONK Crypto Analysis | https://www.youtube.com/watch?v=KtWfQ3lPqFw |
| `[PUMP 10-11 hEkk41geAgs]` | PUMP | Pump.fun Had A Record Week - PUMP Crypto Analysis | https://www.youtube.com/watch?v=hEkk41geAgs |
| `[QNT 10-11 R1nqM9s6W_w]` | QNT | Quant CEO Hints At Japan - QNT Crypto Analysis | https://www.youtube.com/watch?v=R1nqM9s6W_w |
| `[STX 10-11 PTBr4ZxRSVI]` | STX | Stacks Holders Are Locking Up - STX Crypto Analysis | https://www.youtube.com/watch?v=PTBr4ZxRSVI |
| `[SUI 10-11 iWOCnQuLA4c]` | SUI | Sui Faces Three Big Tests - SUI Crypto Analysis | https://www.youtube.com/watch?v=iWOCnQuLA4c |
| `[TRUMP 10-11 GvE7lGieXag]` | TRUMP | Who Is Selling Official Trump? - TRUMP Crypto Analysis | https://www.youtube.com/watch?v=GvE7lGieXag |

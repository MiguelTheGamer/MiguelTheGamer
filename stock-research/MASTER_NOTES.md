# Cash App Catalyst Trading — Master Notes (DO NOT LOSE)
Last updated: Mon 2026-11-23 evening (CT). Owner: Miguel. Broker: Cash App Investing.
Every scheduled check-in must READ this file first and APPEND new findings to the log at the bottom.

## 1. Capital & rules
- Capital: $6,000 cash now; up to $9,600 total. Extra $3,600 stays in cash until after Dec 11, only deployed if account flat/up (skip if down >15%).
- Nothing currently invested (pure cash).
- Cash App Investing constraints (verified via cash.app help pages):
  - NYSE/Nasdaq only; approx listing rules: mkt cap > $300M, 60-day avg vol > 500K, 52-wk low > $5. No OTC buys, no leveraged/inverse ETFs, no ETFs with fees >1%.
  - No options, no shorting, no margin. Bitcoin is only crypto.
  - Order types: market + "Custom Orders" (stop-triggered, fill AT MARKET; not limit orders). Funds for custom buy leave balance when placed.
  - NO extended-hours trading. Orders placed outside 9:30–4:00 ET fill at next open.
  - Fractional shares from $1. $50,000 buy limit per rolling 7 days.
  - T+1 settlement; cash account at Apex (migrating from DriveWealth since May 2026). Avoid good-faith violations: don't rebuy with unsettled sale proceeds.
  - Taxes: short-term gains = ordinary income; set aside ~25%. Wash-sale rule applies. Composite 1099-B, FIFO.
- No Cash App connector/API exists for investing (checked Claude connector directory; Cash App developer API is UK-only, balance/transactions, not investing). Aggregators (SnapTrade, Plaid, Monarch, Empower, Copilot): no evidence they read Cash App Investing holdings. Workarounds: screenshots, monthly statements/trade confirmations (profile → Documents → Account Statements), possibly web CSV export, possibly Cash App trade-confirmation emails via Gmail connector (being checked).
- Suggested data connectors (user must enable in claude.ai settings): Financial Datasets, Alpha Vantage, MT Newswires; Webull (brokerage w/ connector, has limit orders + extended hours). finance:bigquery plugin needs auth.

## 2. Market context (as of Nov 23)
- S&P record close 7,818.93 (Oct 6). Fri Nov 20 close 6,910.39 (−3.7% day, −8.6% week, worst since Apr 2025). Nasdaq 22,617.73 (−10% week).
- Nvidia: Huang resigned Nov 12 (8-K verified), reinstated Nov 23 (8-K + AP/Reuters/CNBC). NVDA +31.5% to ~$165 on Nov 23. Nvidia buyback raised $150B.
- Mon Nov 23: S&P ~+4.7% (SPY 722.29), QQQ +7.0% (651.03), IWM +3.6% (265.74). Best day since Apr 2025. Skeptics call it a "mechanical dead-cat bounce" (Capital Economics). HPE beat but fell ~5% after hours (AI hardware rally may be priced).
- Fed: 3.75–4.00% after Sept 2026 HIKE (12-0); Oct hold 10-2 (two dissents for hike). Chair Kevin Warsh. Dec 8–9 FOMC, decision Dec 9 2pm ET; ~90% odds of 25bp HIKE. Jan hike ~60% priced.
- Data: Oct PCE Wed Nov 25 (core consensus 3.2% y/y); Nov jobs Dec 4; Nov CPI Dec 10; PPI Dec 15; PCE Dec 23; Dec jobs Jan 8; Dec CPI Jan 13.
- Government funding expires Dec 11 (Kalshi ~44% shutdown odds). Democrats won both chambers in midterms; new Congress Jan 3.
- US–China tariff truce extended only 2 months → expires Jan 10, 2027.
- Holidays: market closed Thu Nov 26; half day Fri Nov 27 (closes 1pm ET / 12pm CT).
- Holiday forecasts: NRF $1.013T (+4.2%); Adobe online $275.1B (+6.7%); Black Friday $12.9B (+9.2%); Cyber Monday $15.1B; BNPL $21.3B.
- Seasonals: Santa rally window Dec 24–Jan 5 (failed last 3 years); December 2nd-best month historically.
- Bitcoin ~$64k; CLARITY Act dead (failed 49–50 Sept 15).
- Anthropic IPO (ANT) Nov 19 at $83 — Claude is made by Anthropic: NO opinion given on ANT. Lockups Dec 15, Jan 5, Jan 19, Feb 2.

## 3. CURRENT PLAN ($6,000)
| Ticker | $ | Buy zone | Stop | Target | Notes |
|---|---|---|---|---|---|
| AMZN | 1,300 (650 Nov 24 + 650 Nov 30) | 250–258 | 244 | 272–278 | re:Invent Nov 30–Dec 4; Cyber Week. Mon close 255.39 (IN ZONE) |
| TJX | 900 (450+450) | 136–141 | 131 | 147–150 | Mon 139.46 (IN). Check Burlington (BURL) Tue AM first |
| IMAX | 800 (400+400) | 45–47 | 42.50 | 52–54 | Dune: Part Three Dec 18, exclusive 3 wks IMAX. SELL Dec 14–18. Mon ~46.71 (IN, near top) |
| MU | 700 | 650–700 pullback only; skip >760 | close <590 (mental) | 800–850 | Earnings Dec 17 AMC (confirmed). Trim ≥half by Dec 17 close. Mon 707.70 (low 666.66). Wait for Dell/HP Tue night |
| TGT | 400 | 160–166 | 155 | 172–176 | Catalyst passed (Q3 Nov 18, tariff refund $0.50 EPS). Mon 168.41 (ABOVE zone → wait) |
| COGT | 400 | 26–30 | none (size = stop) | sell half on pop $34–38 | PDUFA GIST Nov 30 (could come early), NonAdvSM Dec 30, AdvSM Jun 29 2027. $400M ATM → expect dilution into strength. Mon ~28.11 (IN). Label risk: liver enzymes |
| MOD | 300 | <127 | 112 / any denial | 145–150 | Samsung buyout talks (Bloomberg Nov 12), unconfirmed; Jana stake; renamed Modexus Solutions. Mon ~137.46 (ABOVE → skip for now) |
| FIVE | 300 | check | sell BEFORE Dec 2 close | +8–12% | Earnings Dec 2 AMC (confirmed). Run-up only. Mon 215.96; 52w 149–264 |
| XENE | 100–200 optional | ~38–40 | none | +25–40% | X-NOVA2 MDD Phase 3 topline Dec 2026. DOWNGRADED: Sept enrollment pause after psychosis events; trial 360 vs 450 planned. Mon ~38.26 |
| Cash | ~700+ | | | | |

Later (extra $3,600, only if flat/up, after Dec 11): CRM ~$600 Dec 20–29 (earnings Dec 2 AMC; BTIG cut PT to $250 Nov 18); optional COGT add for Dec 30; rest cash.

### Tuesday Nov 24 go/wait (from Mon close)
AMZN GO ($650) · TJX GO if BURL fine ($450) · IMAX GO ($400, skip >47) · COGT GO if wanted ($400) · TGT WAIT (above zone; also watch DLTR/BBY) · MOD SKIP for now.

### Exits / key rules
- Stops via Cash App Custom Orders: AMZN, TJX, TGT, IMAX. Gap risk applies.
- No buys before 10am ET (9 CT). No buys Dec 9–11. Exit holiday trades by ~Jan 4 (truce Jan 10).
- Realistic outcome estimate: ~+$650 if most targets hit; ~−$550–600 if most stops hit.

## 4. DROPPED / AVOID (and why)
- EOSE: $1.19 (below $5, not on Cash App), serial dilution.
- CRDO: insiders sold ~$433M/12mo, 0 buys; −55% 3mo; ATR 15%; S&P add unlikely (cap fell below ~$22.7B).
- AMD: CEO Lisa Su sold $35.5M Nov 16; CES Jan 5 runs into Jan 10 truce expiry.
- AVGO: backup AI slot only. Real drop reason = Redburn downgrade Nov 13 (PT $398) + sector selloff; "Kuo/Google TPU cut" story UNVERIFIED/false. Earnings Dec 9 (same day as Fed). Mon 313.55; 52w low ~289.
- DELL (ran +24% before Nov 24 earnings), SPCX (lockup Dec 8, ~798M shares), ANT (no opinion; lockups), CAPR (2nd CRL, −77%), PAL (<$5), VNDA (~$4, <$5), RZLT ($3.87 offering), IMUX (may fail $300M cap), HTZ (maybe <$5).
- MLYS: PDUFA Dec 22, at 52-wk low ~$13.66, UBS PT $19; −40–50% if CRL. Not in plan.

## 5. Watchlist / alternates
- FUN (Six Flags): ~$14.9M insider cluster buy ~$10.30 (Nov 6–10). High debt.
- HUBS: CEO bought ~$5M at $217 (Nov 13). COHR: CEO+chair bought $1.2M (Nov 9–10). INTC: CEO $9.7M at ~$64.73 (Nov 2).
- DG: Piper upgrade Nov 23 PT $170; earnings Dec 3 BMO (confirmed). Mon ~130.5 area (Fri 130.53).
- ULTA (Dec 3 AMC), COST (~Dec 10, Nov sales early Dec; $30 special div record Nov 24), ADBE (Dec 9 AMC), ORCL (~Dec 10–14 unconfirmed), MDB/OKTA (Dec 1 AMC), JBL (~Dec 16–17).
- Biotech: BBIO (Nov 27, ~90%+, muted move), CORT (Dec 17, profitable), PRAX (Dec 27, extended), DYN (Jan 21), ASH Dec 12–15 (late-breakers post Dec 7), JPM Healthcare Jan 11–14.
- Index: S&P rebalance announce ~Dec 4, effective Dec 21 (LNG, ALAB tipped). Nasdaq-100 recon announce ~Dec 11, effective Dec 21.
- Defense: NDAA timing unknown; AVEX (guidance raise), KRMN. Banks for Fed hike: JPM (Jan 14), FHN/MTB/KEY.
- TTWO: GTA VI launched Nov 19 (~17M copies est.).

## 6. Data methods that WORK in this environment
- Most quote sites blocked by proxy (Yahoo, stooq, Nasdaq API, AlphaVantage, finviz, stockanalysis, sec.gov fetch often fails).
- WORKS: raw.githubusercontent.com + git clone of public repos mirroring yfinance:
  - Muraken990/filings-digest-data (5y OHLCV, daily ~12:30 UTC)
  - zhangyuz/Miner (3y OHLCV)
  - AnacolutheSophistiquEe/ohlcv-snapshots, cyyaddsg-git/i004-market-bars (daily bars)
  - GabFx09/radar-saham-us (15-min bars), mrezahajilou-ops/stock-data (quotes branch; official closes ~23:30 UTC)
  - jorgeebarrazagalindo00-png/Consultor-ETF-IA (ETFs)
- Scripts: scratchpad/quant/compute.py, refresh.py, mkmd.py (scratchpad = /tmp/claude-0/-home-user-MiguelTheGamer/6ac5b2ef-e72b-5464-b223-3fe8d3a276bb/scratchpad). Copies of outputs kept in this folder.
- WebSearch works (budget limited across agents). WebFetch mostly blocked.

## 7. Infrastructure
- Google Calendar (user primary calendar, America/Chicago): 12 events created Nov 23 for the plan (Nov 24 buys, Nov 25 PCE, Nov 27 half day, Nov 30 round 2 + COGT, Dec 1 MU window, Dec 2 SELL FIVE, Dec 9–11 no buys, Dec 14 sell IMAX, Dec 16 trim MU, Dec 21 CRM, Dec 29 COGT, Jan 4 exit).
- Scheduled check-in task trig_01STo6wkEQkypep1CGHmLRzk fires into this session (weekdays, CT).
- Drive E: NOT reachable. PC-51608 shares only "Deeper" and "RobloxGame", both unavailable to cloud sessions. User must add an E: folder in Claude desktop app → Settings → Claude Code → Remote Control (and/or update the app).

## 8. LOG (append newest at bottom)
- 2026-11-23 eve: Wave 1 (8 agents) + Wave 2 (9 fable agents) + 3 follow-ups complete. Plan above is current. Next: 7:41am CT check-in Tue Nov 24.

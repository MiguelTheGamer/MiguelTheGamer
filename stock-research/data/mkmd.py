import json,os
B=os.path.dirname(os.path.abspath(__file__))
j=json.load(open(B+"/refresh_tmp.json"))
md=f"""# Data refresh - Monday 2026-11-23 session (pulled ~22:30 UTC / 5:30pm ET)

**Status: Monday data is PARTIAL.** No mirror had a complete official Monday OHLCV bar for all 15 tickers yet. Quality by ticker is in the "Date / quality" column:

- **daily bar / daily close** (MU, SPY, QQQ, IWM, AMZN, AVGO): yfinance daily bar for 11/23 fetched after the close - treat as the close.
- **16:00 bar** (TJX, TGT, FIVE, CRM): close of the last regular-session 15-min yfinance bar (16:00 ET). Within ~0.02% of the daily close on the tickers where both exist (AMZN 255.42 vs 255.39, MU 707.69 vs 707.70, AVGO 313.54 vs 313.55), but not the official auction print.
- **late print HH:MM ET** (IMAX, COGT, MOD, XENE): Nasdaq last-sale print at the stated time, 4-19 minutes BEFORE the close (COGT: 16:01). **Not a close.** For reference the same feed had AMZN at 257.10 at 15:46 vs a 255.39 close (0.7% drift).
- **MLYS**: no Monday price anywhere; Friday close shown.

{chr(10).join(j['table'])}

ATR = Wilder 14-day. "ATR14 (thru Fri)" is exact from full OHLC through 11/20. "ATR14 incl. Mon" is exact only where a Monday high/low exists (MU, SPY, QQQ, IWM; AMZN/AVGO are taken from the i004-market-bars mirror's own ATR, whose method reproduces my MU value exactly). Rows marked ">= (floor)" have no Monday high/low: the figure uses |Mon price - Fri close| as the true range, which can only understate it - use the Friday ATR for sizing. "ATR % of price" uses the exact ATR (Fri ATR for floor rows) over the latest price.

Monday ranges where known: MU O 690.72 / H 720.69 / L 666.66 / C 707.70; SPY H 727.98 / L 713.54; QQQ H 657.50 / L 641.95; IWM H 266.08 / L 263.00.

## FIVE and XENE (history: zhangyuz/Miner, 750 daily bars, through Fri 11/20)

| Ticker | 52W high (date) | 52W low (date) | Fri close | 1M move thru Fri (vs 10/22 close) | Mon price | 1M move thru Mon (vs 10/23 close) | Position in 52W range |
|---|---|---|---|---|---|---|---|
"""
for t,e in j["extra"].items():
    md+=f"| {t} | {e['hi']:.2f} ({e['hid']}) | {e['lo']:.2f} ({e['lod']}) | {e['fri']:.2f} | {e['m1_fri']:+.1f}% (from {e['ref_fri'][1]:.2f}) | {e['last']:.2f} | {e['m1_mon']:+.1f}% (from {e['ref_mon'][1]:.2f}) | {e['pos']:.0f}% |\n"
md+="""
52W range = intraday high/low over the 252 sessions ending 11/20 (Monday's prices are inside both ranges; FIVE's low falls on the first day of that window, 2025-11-20). 1M = 21 trading sessions. FIVE Monday = 16:00 bar; XENE Monday = 15:41 ET print (provisional).

## Interpretation

1. Monday was a sharp rebound after last week's selloff: SPY +4.7%, QQQ +7.0%, IWM +3.6%; MU +19.0%, MOD about +10% (15:56 print).
2. In zone on Monday: AMZN (255.39 in 250-258, upper half), TJX (139.46 in 136-141), and provisionally IMAX (46.71 in 45-47, only 0.6% under the top edge, on a 15:41 print) and COGT (28.11 in 26-30).
3. Out of zone: TGT 168.41 is 1.5% above 166; MOD ~137.5 is ~8% above the <127 line (Friday's 124.67 was inside); MU closed 707.70, 1.1% above 650-700 but under the 760 skip level, after trading 666.66-720.69 intraday (it passed through the zone).
4. XENE ~38.26 is 4.4% below 40 (Fri 37.04), +8.3% over one month but in the bottom ~12% of its 52W range (33.38-72.66); FIVE fell 2.4% on a strong up day to ~215.96, -3.3% over one month, mid-range (149.05-263.87).
5. Volatility is elevated: MU ATR 66 pts (9.4%), MOD ~12 (8.9%), AVGO 20 (6.4%); less than one ATR separates MU, AMZN, TGT and IMAX from a zone boundary, so re-check the provisional names against official closes before acting.

## Sources (all via GitHub mirrors; direct market-data hosts are blocked)

- Friday base OHLCV: Muraken990/filings-digest-data (stocks), jorgeebarrazagalindo00-png/Consultor-ETF-IA (ETFs), zhangyuz/Miner (FIVE, XENE; holds all 12 stocks, 3y, last bar 11/20). None had a Monday bar at pull time (filings-digest commits ~12:30 UTC, so Monday should land there Tuesday).
- Monday: AnacolutheSophistiquEe/ohlcv-snapshots (MU, SPY, QQQ, IWM daily bars), cyyaddsg-git/i004-market-bars (AMZN, AVGO, MU close + ATR), GabFx09/radar-saham-us docs/data/live.json (TJX, TGT, FIVE, CRM), mrezahajilou-ops/stock-data quotes branch (IMAX, COGT, MOD, XENE late prints; its prev-close field matches my Friday closes for all 12 stocks).
- Cross-check: Emf2912147/GEX Schwab spot at 16:06 ET - SPY 723.11, QQQ 651.10, IWM 265.74 (vs daily closes 722.29 / 651.03 / 265.74).
- mrezahajilou-ops/stock-data schedules an "official closing prices" quotes run at 23:30 UTC on weekdays; that is the earliest mirror likely to firm up IMAX/COGT/MOD/XENE/MLYS.
- Scripts: refresh.py and mkmd.py in this directory (inputs under raw/).
"""
open(B+"/refresh_2026-11-23.md","w").write(md); print(md[md.find('## FIVE'):md.find('## Interp')])

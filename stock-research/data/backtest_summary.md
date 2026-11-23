# Swing-setup backtests (run 2026-11-23, data through 2026-11-20 close)

All entries/exits at daily closes, dividend-adjusted prices, no costs or slippage. Every sample here is small; treat results as rough base rates, not edges.

**Data** (Yahoo-derived GitHub mirrors, spliced on overlapping days; median daily-return difference between sources in the overlaps is <0.003%, see data_splice_checks.csv):
MU/TGT/TJX/AMZN = Kronos Universe500 (2015-18) + brownbear (2019-21) + filings-digest-data (2021-26). IMAX = Polygon mirror (2015-21) + filings-digest-data. CRM/INTU/NOW = eshaanmattoo/us_stocks (full history). SPY = kraisr/backtest-sim (2005-18) + brownbear + Consultor-ETF-IA.

## 1. MU pre-earnings run-up
Method: earnings dates hardcoded from memory (MU reports after the close): 28 dates 2019-2025 (high confidence), 16 dates 2015-2018 (medium confidence). The "largest overnight gap" method was tested and rejected: it picked the recalled date in only 59% of quarters. Sep-2026 is excluded (no identifiable date). E = report day.

| Leg | Sample | N | Mean | Median | Win % | Worst |
|---|---|---|---|---|---|---|
| Run-up: close E-7 to close E-1 | 2015-25 | 44 | +2.00% | +1.17% | 59% | -8.4% |
| Run-up: close E-7 to close E-1 | 2019-25 | 28 | +2.88% | +0.88% | 57% | -8.4% |
| Run-up: close E-7 to close E-1 | last 5y | 17 | +1.88% | +0.38% | 53% | -8.4% |
| Hold through: close E-7 to close E+1 | 2015-25 | 44 | +2.12% | +1.56% | 57% | -18.9% |
| Hold through: close E-7 to close E+1 | last 5y | 17 | +2.22% | +0.66% | 53% | -15.3% |
| Earnings reaction only: close E to close E+1 | 2015-25 | 44 | +0.23% | -1.23% | 43% | -18.2% |
| Baseline: any 6-day MU hold | 2015-26 | 2,984 | +0.94% | +0.68% | 54% | -33.2% |

Takeaway: the run-up is mildly positive (t = 2.1 vs zero, but only 1.1 vs MU's normal 6-day drift), so it is not clearly different from simply owning MU. Holding through the print adds almost no expected return (+0.2%) and a coin-flip of roughly +/-6.5% average move with a worst case of -18%; selling before the report is the better risk-adjusted choice.

## 2. Holiday window (Tuesday before Thanksgiving to first trading day of January), 2015-2025
| Ticker | N | Mean | Median | Win % | Worst | Avg max drawdown | Worst max drawdown | Mean excess vs SPY | Beat SPY |
|---|---|---|---|---|---|---|---|---|---|
| TGT | 11 | +2.82% | -0.13% | 45% | -6.9% | -7.1% | -15.5% | +2.25% | 7/11 |
| TJX | 11 | +1.07% | +1.24% | 64% | -4.9% | -4.8% | -14.8% | +0.50% | 7/11 |
| AMZN | 11 | +0.18% | +2.20% | 55% | -7.9% | -8.0% | -24.2% | -0.39% | 5/11 |
| SPY | 11 | +0.58% | +1.97% | 64% | -4.7% | -4.0% | -15.6% | n/a | n/a |

Last 5 seasons only (N=5 each): TGT +4.62% mean, TJX +1.41%, AMZN -0.79%, SPY +0.39%. Max drawdown = peak-to-trough on closes inside the window; the 2018 season produced every "worst" figure.

Takeaway: no reliable holiday edge. TGT's mean is carried by three seasons (2017 +18%, 2025 +16%, 2023 +9%) while its median is about zero; TJX is the steadiest but only about +0.5% over SPY. AMZN has lagged SPY in this window in 4 of the last 5 years, and typical in-window drawdowns of 5-8% are larger than the average gain.

## 3. IMAX around tentpole releases (R = US release day)
22 films 2015-2026: the five requested plus Force Awakens, Rogue One, Dunkirk, Last Jedi, Infinity War, Endgame, Rise of Skywalker, Tenet, No Time to Die, Spider-Man: No Way Home, The Batman, Deadpool & Wolverine, Sinners, M:I Final Reckoning, F1, Avatar: Fire and Ash, The Odyssey. Some windows overlap (Oct 2021; Apr-Jun 2025), so observations are not independent.

| Leg | Sample | N | Mean | Median | Win % | Worst | Mean excess vs SPY |
|---|---|---|---|---|---|---|---|
| Pre: close R-15 to close R-1 | requested 5 | 5 | +3.41% | +1.52% | 60% | -7.0% | +2.41% |
| Pre: close R-15 to close R-1 | all 22 | 22 | +3.52% | +2.08% | 68% | -14.1% | +2.64% |
| Post: close R to close R+5 | requested 5 | 5 | -2.04% | -3.73% | 20% | -13.7% | -2.29% |
| Post: close R to close R+5 | all 22 | 22 | -1.30% | -1.36% | 45% | -14.9% | -1.89% |
| Baseline: any 14-day IMAX hold | 2015-26 | 2,878 | +0.57% | +0.02% | 50% | n/a | n/a |

Takeaway: the pattern leans "buy the anticipation, sell before release", but it is not statistically solid (t = 1.5). Four films (No Time to Die +27%, Tenet +26%, Dune 2 +22%, Deadpool +16%) supply most of the pre-release mean; without the top two it is +1.2%. Post-release is slightly negative on average, with Oppenheimer (+13.6%) and The Odyssey (+10.5%) the notable exceptions.

## 4. Late-December losers bounce (close Dec 23 to close of 7th January trading day)
| Group | Sample | N | Mean | Median | Win % | Worst | Mean excess vs SPY |
|---|---|---|---|---|---|---|---|
| CRM/INTU/NOW, down >20% YTD at Dec 15 | full history | 8 (4 distinct years) | +3.40% | +3.07% | 63% | -7.6% | +0.01% (7 obs) |
| CRM/INTU/NOW, down >20% YTD at Dec 15 | 2015-25 | 5 (2022 and 2025 only) | +1.79% | +3.02% | 60% | -7.6% | -0.60% |
| CRM/INTU/NOW, not down >20% | full history | 58 | +0.68% | -0.50% | 47% | -26.1% | -0.01% |
| CRM/INTU/NOW, not down >20% | 2015-25 | 28 | +0.75% | -1.58% | 43% | -10.8% | -0.07% |
| SPY | 2015-25 | 11 | +1.06% | +1.05% | 73% | -6.0% | n/a |

Down->20% cases: 2022 (CRM +11.9%, INTU +3.0%, NOW +3.1%), 2025 (CRM -1.5%, NOW -7.6%), 2008 (CRM -2.3%, INTU +7.2%), 1996 (INTU +13.3%).

Takeaway: effectively four independent years, so this is anecdote, not evidence. The bounce worked in 2022 and failed in 2025, and on average the losers did no better than SPY over the same days.

## 5. 2xATR(14) stop, entry at close on Nov 24 (or prior trading day), exit Jan 4, 2015-2025
Stop = entry minus 2x Wilder ATR14; triggered by a daily low, filled at the stop (or the open if it gapped below).

| Ticker | N | Avg stop distance | Stop hit | Mean, no stop | Mean, with stop | Hits where stop helped |
|---|---|---|---|---|---|---|
| AMZN | 11 | -5.6% | 6/11 (55%) | +0.44% | -1.43% | 2 of 6 |
| TJX | 11 | -4.7% | 2/11 (18%) | +2.03% | +1.53% | 0 of 2 |
| TGT | 11 | -6.1% | 5/11 (45%) | +2.85% | +1.92% | 2 of 5 |
| IMAX | 11 | -6.9% | 9/11 (82%) | -1.85% | -5.51% | 4 of 9 |
| All four | 44 | -5.8% | 22/44 (50%) | +0.87% | -0.87% | 8 of 22 |

Last 5 seasons (N=20): hit 8/20 (40%); mean +1.15% without the stop vs -0.04% with it.

Takeaway: a 2xATR stop was hit in half of these windows and lowered the average result for every ticker; in 14 of 22 hits the stock finished the window above the stop. Trades that were stopped averaged only -2.9% if simply held, so the stop mostly converted recoverable dips into realised losses of about -6%. It capped the worst case hardly at all (-9.8% unstopped vs -10.4% stopped, the latter from a gap-through in Dec 2018). IMAX in particular is too choppy for a 2xATR stop over a six-week hold.

## Caveats
- N is 5 to 44 per setup; nothing here survives a multiple-comparison correction.
- MU dates before 2019 and all film dates are from memory, not a verified calendar; two 2026 MU dates inferred from gaps are in the CSV but excluded from the stats.
- Close-to-close only: no commissions, spreads, or taxes; stop fills are idealised.

Files: 1_mu_earnings.csv, 2_holiday.csv, 3_imax_releases.csv, 4_dec_bounce.csv, 5_atr_stop.csv, summary_stats.csv, data_splice_checks.csv, data.py, bt.py.

# Holiday data playbook: AMZN, TGT, TJX, FIVE (Nov 24 2026 to ~Jan 4 2027)

Written Mon 2026-11-23. **The headline holiday tallies have not moved these stocks much in 2019-2025, so use them as cut signals and let earnings and price levels drive adds.** Release dates marked "expected" are inferred from prior years, not confirmed for 2026.

## 1. Release calendar (ET)

| Date | Release | Bar to beat | Status |
|---|---|---|---|
| Tue Nov 24, pre-open | Burlington Q3 (off-price read for TJX) | Comp and traffic vs guidance | Confirmed |
| Tue Nov 24, 10:00am | Conference Board confidence | Oct 91.7 | Expected |
| Wed Nov 25, 10:00am | UMich final November | Prelim 51.0 | Expected |
| Fri Nov 27, morning | Adobe Thanksgiving tally | $6.9B, +8.5% | Expected |
| Sat Nov 28, morning | Adobe Black Friday; Mastercard SpendingPulse Black Friday; Salesforce; Shopify live dashboard | Adobe $12.9B, +9.2% | Expected |
| Mon Nov 30 to Tue Dec 1 | Placer.ai foot traffic, Sensor Tower app data (blog posts, no fixed time) | Store visits up or down YoY | Expected |
| Tue Dec 1, morning | Adobe Cyber Monday and Cyber Week; NRF weekend survey; Shopify wrap; Amazon's own press release | CM $15.1B (+6.2%); Cyber Week $47.5B (+7.4%); NRF 183M shoppers | Expected |
| Wed Dec 2, after close | Five Below Q3 (call 4:15pm) | n/a | Confirmed |
| ~Dec 4 / ~Dec 10 | UMich December prelim / BofA Consumer Checkpoint | BofA Oct card spend +5.8% | Expected |
| ~Dec 15-16 | Census November retail sales | n/a | Expected |
| Sat Dec 26 | Mastercard SpendingPulse full season (Nov 1-Dec 24) | +5.5% total, online +11%, stores +3.6% | Expected |
| Early Jan | Adobe full season | $275.1B, +6.7% | Expected |

Other bars: Salesforce expects US Cyber Week online sales of $84B (+6%). NRF expects November-December sales +4.2% to $1.013T.

Cash App constraint: the Saturday and Tuesday pre-market releases can only be acted on at the next 9:30am open, after any gap. FIVE's report lands after the close, so the choice is to hold through it or sell by 4pm Dec 2.

## 2. Is a "beat" priced in?

Mostly yes. Adobe has reported a "record" every year, yet the stocks' reactions were small and mixed. My own check on daily closes, 2019-2025 (7 seasons, return minus SPY):

| | Mon after Black Friday | Tue (Cyber Monday tally day) | Tue before Thanksgiving to Tue after |
|---|---|---|---|
| AMZN | +0.67% mean, up 5/7 | +0.04%, 5/7 | +1.2%, 6/7 |
| TGT | +0.42% mean (median +0.08%), 5/7 | -0.08%, 4/7 | +1.9% mean (median +0.55%), 5/7 |
| TJX | +0.14%, 4/7 | -0.20%, 3/7 | -0.4%, 4/7 |

- Seven observations is anecdote, not an edge. TGT's mean is carried by 2022, 2024 and 2025.
- FIVE and XRT are not tested: I had no price history for them in this environment.
- Fidelity found nearly all of retail's average Q4 gain (about 5%) comes before Black Friday, then stocks go sideways for five weeks.
- CNBC (2018) found XRT lagged the S&P 500 from Black Friday to year-end since 2010.
- The repo's existing backtest (Tue before Thanksgiving to first January session, 2015-2025) agrees: TGT median -0.1%, TJX +1.2%, AMZN +2.2%, with typical in-window drawdowns of 5-8%.

## 3. What is different in 2026

- **Inflation share of growth:** Mastercard says about half of its +5.5% is higher prices; NRF's forecast is also described as partly inflation-driven. A nominal beat with falling units is not bullish.
- **Tariff refunds flatter earnings:** TGT's Q3 EPS of $2.65 included about $0.50 of refunds; TJX had $0.05 in Q3 and says none recur in Q4. Refunds are funding price cuts at mass and off-price chains.
- **Sentiment is low but rising:** UMich 51.0 prelim (three-month high, from 48.0); Conference Board 91.7, expectations 72.6 (below the 80 recession-signal line).
- **K-shape and trade-down:** BofA card data shows holiday spending well above last year but average ticket falling; Fortune reports the strongest hunt for cheaper stores since early 2021. That favors TJX, BURL and FIVE.
- **BNPL:** Adobe forecasts $21.3B, +6.6%, slower than total online growth.
- **Late peak:** BofA says early December may overtake Black Friday, so a soft Black Friday may be timing, not weakness.
- **Bar already raised:** on Nov 18 TGT posted comps +5.6% vs 3.8% expected and raised its outlook; the stock is up roughly 60% this year. TJX rose 5-6% on a 4% comp, but guides Q4 comps to only 2-3% and Marmaxx (US) ran just 2%.

## 4. Decision rules

Default is hold. Because beats are priced in, only a clear miss or a price break should trigger action. "Cut" means sell half; a second trigger sells the rest. Thresholds are my judgment, anchored to the published forecasts.

| Signal | AMZN | TGT | TJX | FIVE |
|---|---|---|---|---|
| Adobe Black Friday >= +9% and Cyber Monday >= +6% | Hold; do not chase a gap up | Hold | Hold | Hold |
| Adobe Black Friday < +6% or Cyber Monday < +4% | Cut | Hold (stores matter more) | Hold | Hold |
| Mastercard in-store Black Friday flat or negative, or Placer visits down > 3% YoY | Hold | Cut | Cut if Burlington comp also missed | Cut |
| NRF shoppers < 175M, or NRF/Adobe say discounts ran deeper than the ~30% forecast | Hold | Cut (margin risk) | Hold | Hold |
| Burlington beats on comp and traffic Nov 24 | n/a | n/a | Add only inside 136-141 | Hold |
| Conference Board < 85 or UMich final < 48 | Hold | Cut | Hold (trade-down helps) | Hold |
| Mastercard Dec 26 season < +4%, or online < +8% | Cut | Cut | Hold | Cut |
| Close more than 1.5x ATR below entry (about AMZN $15, TGT $8, TJX $6, FIVE $14) | Exit | Exit | Exit | Exit |

Adds: only on a pullback into the existing buy zones (AMZN 250-258, TGT 160-166, TJX 136-141) with no cut signal active. TGT at 168.41 is above its zone. Do not add on a "record" headline; the history above says that is the average outcome. For FIVE, decide before 4pm Dec 2 whether to carry it through earnings.

## Sources

- Adobe forecast (Sep 28 2026): https://news.adobe.com/news/2026/09/adobe-us-holiday-shopping-season-to-hit-record
- NRF forecast (Oct 15 2026) and 183M weekend release (Nov 19 2026): https://nrf.com/media-center/press-releases/nrf-forecasts-2026-holiday-sales-growth-as-consumers-remain-resilient , https://nrf.com/media-center/press-releases/183-million-consumers-expected-to-shop-during-thanksgiving-weekend
- Mastercard forecast (2026): https://www.mastercard.com/us/en/news-and-trends/stories/2026/2026-holiday-shopping-forecast.html
- Salesforce forecast (2026): https://chainstoreage.com/salesforce-cyber-week-sales-hit-record-357b-help-ai
- BofA Consumer Checkpoint (Nov 12 2026): https://institute.bankofamerica.com/economic-insights/consumer-checkpoint-november-2026.html ; late-peak study (Oct 29 2026): https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/10/bank-of-america-study--early-december-could-overtake-black-frida.html
- Fortune on trade-down (Nov 16 2026): https://fortune.com/2026/11/16/gen-z-millennials-half-holiday-spending-trading-down-bank-of-america-goldman/
- UMich prelim (Nov 6 2026): https://bankingjournal.aba.com/2026/11/preliminary-consumer-sentiment-rises-in-november/ ; Conference Board (Oct 27 2026): https://investinglive.com/news/october-us-consumer-confidence-vs-81-0-expected/
- Target Q3 (Nov 18 2026): https://corporate.target.com/news-features/article/2026/11/q3-2026-earnings
- TJX Q3 (Nov 18 2026): https://massmarketretailers.com/tjx-cos-posts-third-quarter-sales-gains-and-raises-guidance/ , https://finviz.com/news/424720/tjx-shares-jump-608-as-third-quarter-revenue-beats-estimates-and-fy2027-outlook-strengthens
- Burlington date: https://finviz.com/news/420591/burlington-stores-inc-announces-third-quarter-fiscal-year-2026-earnings-release-date-conference-call-and-webcast ; Five Below date: https://www.helpareporter.com/news-releases/five-below-inc-announces-third-quarter-fiscal-2026-earnings-release
- Tariff refunds (Aug 27 2026): https://www.modernretail.co/operations/big-box-briefing-retailers-get-direct-tariff-relief-their-shoppers-likely-wont/
- Fidelity: https://www.fidelity.com/learning-center/trading-investing/black-friday-stocks ; CNBC (Nov 28 2018): https://www.cnbc.com/2018/11/28/strong-black-friday-sales-arent-necessarily-good-for-retail-stocks.html
- Price history: Yahoo-derived daily bars already in this session (2019-2026); holiday-window backtest in /home/user/MiguelTheGamer/stock-research/data/backtest_summary.md

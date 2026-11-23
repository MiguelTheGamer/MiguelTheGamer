# Mechanics & Tax Audit — Cash App Investing plan (v3)
Written Mon 2026-11-23. General information, not personalized tax advice. cash.app could not be fetched from this session (host not allowed), so Cash App facts come from search snippets of its help/legal pages.

## 1. Calendar and settlement (T+1 business day)
| Date | Action | Settles |
|---|---|---|
| Tue Nov 24 | Buys (from cash) | Nov 25 |
| Wed Nov 25 | any sale | **Fri Nov 27** (Thu closed) |
| Fri Nov 27 | half day, 1pm ET close | Mon Nov 30 |
| Mon Nov 30 | Round 2 buys | Dec 1 |
| Dec 2 | FIVE sell (optional) | Dec 3 |
| Dec 14–18 | IMAX sell | next day |
| Dec 16–17 | MU trim | Dec 17–18 |
| Thu Dec 24 | any sale (likely 1pm close; unconfirmed for 2026) | **Mon Dec 28** |
| Dec 30 | COGT buy | Dec 31 |
| Thu Dec 31 | any sale | **Mon Jan 4** |

What a violation is (Cash App house rules, confirmed): buying with unsettled proceeds is not the violation. A good-faith violation is **selling the new position before the sale that funded it settles**. Freeriding is paying for a buy with proceeds from selling those same shares.

Exposure points:
- **Stops can cause a GFV automatically.** A position bought with unsettled proceeds whose stop triggers the same day is a violation with no decision by the trader.
- **COGT Dec 30** is a binary event the trader may want to sell the same day. Fund it only from a sale made on or before Dec 28, or from idle cash.
- **Round 2 on Nov 30** must not be paid for with a Nov 27 or Nov 30 stop-out.

Fix: the plan keeps about $1,400 idle. Use only that for same-day buys; sale proceeds wait one full business day. The extra $3,600 must be in the Cash App balance before the CRM window (bank transfer timing not checked).

Penalties: the account agreement says only that the account "may face restrictions." The common industry ladder (3–4 GFVs in 12 months, or one freeride, gives 90 days settled-cash-only) is **not confirmed for Cash App**.

## 2. Custom Orders and same-day trading
- **Fractional shares: could not confirm.** No Cash App page found says a custom sell can cover a fractional position. MU ($500 at ~$700) is under one share, and most other positions have fractions. Test in-app on Nov 24 right after the first buy; if whole shares only, those stops become mental stops with price alerts.
- **Not GTC.** Cash App describes an expiration period picked at placement (its example is "1-day", ending at that day's close) and notifies on expiry. Maximum duration not found. Log each expiry and re-place.
- Triggered orders fill at market in regular hours only, so an overnight gap fills at the open.
- Whether a pending custom sell blocks a manual sell of the same shares: unconfirmed; assume cancel first.
- **Pattern day trading does not apply.** Accounts at Apex are cash accounts (confirmed), and FINRA removed the PDT definition and $25,000 minimum effective June 4, 2026 (Notice 26-10; firms may phase in to Oct 20, 2027). Same-day sell and rebuy is allowed, but the rebuy is on unsettled money, so selling it again before T+1 is a GFV. Treatment of an account still at DriveWealth: unconfirmed.

## 3. Taxes
- All trades are short-term: ordinary income rates, plus state tax where applicable. Net losses offset gains, then up to $3,000 of other income.
- **Year split:** trade date, not settlement, sets the tax year (IRS Pub 550 general rule; not re-verified today). Dec 31 sale is 2026; Jan 4 is 2027. FIVE, IMAX, MU trim fall in 2026. CRM, the Dec 30 COGT and the January exits fall in 2027.
- **Wash sales** (30 days before and after a loss sale, crossing year-end; confirmed via Investor.gov):
  1. **COGT:** any loss sale after the Nov 30 decision followed by the Dec 30 rebuy is inside 30 days.
  2. **Two-tranche names (AMZN, TJX, IMAX):** tranche 1 stopped at a loss, then tranche 2 bought Nov 30; or half sold at a loss while the other lot is held.
  3. Stop-out and re-entry in any name within 30 days.
  4. December loss plus January rebuy moves the loss out of 2026.
  The loss is added to the new lot's basis, not lost, but it can shift to the 2027 return. To claim it in 2026, stay out of that ticker 31 days.
- **1099-B** by mid-February; the DriveWealth to Apex move may mean two forms if there were earlier 2026 trades (unconfirmed).
- **Estimated tax** (IRS Topic 306, confirmed): no penalty if the return owes under $1,000 after withholding, or payments cover 90% of this year's or 100% of last year's tax. At the plan's realistic +$650, setting aside ~25% of gains is ample. Q4 date: Jan 15, 2027.
- If claimed as a dependent, dependent filing thresholds and kiddie tax may apply (2026 figures not checked).

## 4. Per-trade checklist
1. 10:00–11:00 ET, market open, check for a half day.
2. Buy money has been settled at least one business day. If not, no buy.
3. Sold this ticker at a loss in the last 30 days? Then this is a wash sale.
4. Price inside zone; size matches v3.
5. After fill: place the stop, screenshot, put its expiry in the calendar.
6. Before a manual sell: cancel the pending stop.
7. After a sell: note the settlement date; that cash is frozen until then.
8. Log the trade and save the confirmation to the Drive folder.
9. Set aside ~25% of any realized gain.

## Sources
- https://cash.app/legal/us/en-us/cash-investing-house-rules
- https://cash.app/legal/us/en-us/cash-investing-account-agreement
- https://cash.app/help/3109-custom-orders
- https://www.finra.org/rules-guidance/notices/26-10
- https://www.investor.gov/introduction-investing/investing-basics/glossary/wash-sales
- https://www.irs.gov/taxtopics/tc306

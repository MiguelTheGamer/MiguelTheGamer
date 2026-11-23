import json, pandas as pd, numpy as np, os
B=os.path.dirname(os.path.abspath(__file__))
T="AMZN TJX TGT IMAX COGT MOD FIVE MU XENE CRM AVGO MLYS SPY QQQ IWM".split()
def base(t):
    if t in("SPY","QQQ","IWM"):
        d=pd.read_csv(f"{B}/raw/other/{t}.csv",parse_dates=["Date"]).rename(columns=str.lower).set_index("date")
        return d[["open","high","low","close","volume"]].sort_index(),"Consultor-ETF-IA"
    p=f"{B}/raw/muraken/{t}.json"
    if os.path.exists(p):
        d=pd.DataFrame(json.load(open(p))["data"]); d["date"]=pd.to_datetime(d["date"]); return d.set_index("date").sort_index()[["open","high","low","close","volume"]],"filings-digest-data"
    d=pd.DataFrame(json.load(open(f"{B}/raw/miner/{t}.json")))
    d["date"]=pd.to_datetime(d.trade_date.str[:10],format="%Y,%m,%d"); return d.set_index("date").sort_index()[["open","high","low","close","volume"]],"zhangyuz/Miner"
def miner_fri(t):
    p=f"{B}/raw/miner/{t}.json"
    if not os.path.exists(p): return None
    j=json.load(open(p))[-1]; return j["trade_date"][:10], j["close"]
q=json.load(open(f"{B}/raw/mrez/quotes.json"))["q"]
gl=json.load(open(f"{B}/raw/gab/live.json"))
def monday(t):
    """returns (close, high, low, open, quality, source)"""
    p=f"{B}/raw/ana/{t}.csv"
    if os.path.exists(p):
        a=pd.read_csv(p,comment="#",parse_dates=["Date"]).set_index("Date"); r=a.iloc[-1]
        if a.index[-1]==pd.Timestamp("2026-11-23"):
            return r.Close,r.High,r.Low,r.Open,"daily bar","yfinance daily bar via AnacolutheSophistiquEe/ohlcv-snapshots (generated 21:30Z)"
    p=f"{B}/raw/cyy/{t}.json"
    if os.path.exists(p):
        j=json.load(open(p))
        if j["last_bar"]=="2026-11-23": return j["price"],None,None,None,"daily close","daily close via cyyaddsg-git/i004-market-bars (src=close, last_bar 2026-11-23)"
    if t in gl["stocks"] and gl["stocks_day"]=="2026-11-23":
        return gl["stocks"][t][0],None,None,None,"16:00 bar","yfinance last 15-min bar close at 16:00 ET via GabFx09/radar-saham-us live.json"
    if t in q and q[t][3].startswith("2026-11-23"):
        return q[t][0],None,None,None,"late print "+q[t][3][11:16]+" ET","Nasdaq last-sale print via mrezahajilou-ops/stock-data quotes.json (NOT official close)"
    return None
def atr_series(d):
    pc=d.close.shift(1); tr=pd.concat([d.high-d.low,(d.high-pc).abs(),(d.low-pc).abs()],axis=1).max(axis=1)
    return tr.ewm(alpha=1/14,adjust=False,min_periods=14).mean()
zones={"AMZN":(250,258),"TJX":(136,141),"TGT":(160,166),"IMAX":(45,47),"COGT":(26,30),"MOD":(None,127),"MU":(650,700),"XENE":(40,40)}
def zone(t,c):
    if t not in zones: return "n/a"
    lo,hi=zones[t]
    if t=="MOD": return "INSIDE (<127)" if c<127 else f"NO - above (+{(c/127-1)*100:.1f}% over 127)"
    if t=="XENE": return f"near ~40? {(c/40-1)*100:+.1f}% vs 40"
    if lo<=c<=hi: return f"INSIDE {lo}-{hi}"
    s=f"NO - below {lo} ({(c/lo-1)*100:+.1f}%)" if c<lo else f"NO - above {hi} ({(c/hi-1)*100:+.1f}%)"
    if t=="MU": s+="; under 760 skip line" if c<=760 else "; ABOVE 760 SKIP"
    return s
rows=[];extra={}
for t in T:
    d,src=base(t); d=d.dropna(subset=["close"]); d=d[d.index<="2026-11-20"]
    assert d.index[-1]==pd.Timestamp("2026-11-20"),(t,d.index[-1])
    fri=d.close.iloc[-1]; atr_f=atr_series(d).iloc[-1]
    mf=miner_fri(t)
    m=monday(t)
    r=dict(t=t,fri=fri,atr_f=atr_f,src=src,xfri=(mf[1] if mf else None))
    if m:
        c,h,l,o,qual,msrc=m
        r.update(last=c,date="2026-11-23",qual=qual,msrc=msrc,chg=(c/fri-1)*100)
        if h is not None:
            d2=pd.concat([d,pd.DataFrame(dict(open=o,high=h,low=l,close=c,volume=np.nan),index=[pd.Timestamp("2026-11-23")])])
            r.update(atr_m=atr_series(d2).iloc[-1],atr_note="exact (Mon OHLC)",hl=(h,l))
        else:
            pc=f"{B}/raw/cyy/{t}.json"
            if os.path.exists(pc): r.update(atr_m=json.load(open(pc))["atr"],atr_note="exact (mirror-computed Wilder ATR14, method verified on MU)")
            else: r.update(atr_m=(13*atr_f+abs(c-fri))/14,atr_note="floor est. (close-to-close TR only; no Mon high/low)")
    else:
        r.update(last=fri,date="2026-11-20",qual="Fri official close (no Mon data)",msrc=src,chg=None,atr_m=None,atr_note="")
    r["zone"]=zone(t,r["last"])
    rows.append(r)
    if t in("FIVE","XENE"):
        y=d.iloc[-252:]; c=d.close
        extra[t]=dict(hi=y.high.max(),hid=y.high.idxmax().date(),lo=y.low.min(),lod=y.low.idxmin().date(),
            m1_fri=(fri/c.iloc[-22]-1)*100,ref_fri=(c.index[-22].date(),c.iloc[-22]),
            m1_mon=(r["last"]/c.iloc[-21]-1)*100,ref_mon=(c.index[-21].date(),c.iloc[-21]),last=r["last"],fri=fri,bars=len(d),
            pos=(r["last"]-y.low.min())/(y.high.max()-y.low.min())*100)
f=lambda v:f"{v:,.2f}"
L=["| Ticker | Latest | Date / quality | Fri 11/20 close | Chg vs Fri | ATR14 (thru Fri) | ATR14 incl. Mon | ATR % of price | Buy zone | In zone? |","|"+"---|"*10]
zt={"AMZN":"250-258","TJX":"136-141","TGT":"160-166","IMAX":"45-47","COGT":"26-30","MOD":"<127","MU":"650-700 (skip >760)","XENE":"~40"}
for r in rows:
    am=f"{'' if r['atr_note'].startswith('exact') else '>= '}{f(r['atr_m'])}{'' if r['atr_note'].startswith('exact') else ' (floor)'}" if r['atr_m'] else "n/a"
    a=r['atr_m'] if (r['atr_m'] and r['atr_note'].startswith('exact')) else r['atr_f']
    L.append(f"| {r['t']} | {f(r['last'])} | {r['date']} - {r['qual']} | {f(r['fri'])} | {('%+.2f%%'%r['chg']) if r['chg'] is not None else 'n/a'} | {f(r['atr_f'])} | {am} | {a/r['last']*100:.1f}% | {zt.get(r['t'],'-')} | {r['zone'] if r['t'] in zt else '-'} |")
print("\n".join(L)); print()
for t,e in extra.items(): print(t,e)
for r in rows: print(r['t'],r['src'],r.get('xfri'),r.get('hl'),r['msrc'])
json.dump(dict(rows=rows,extra=extra,table=L),open(f"{B}/refresh_tmp.json","w"),default=str,indent=1)

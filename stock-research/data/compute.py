import json, pandas as pd, numpy as np, sys, os
B=os.path.dirname(os.path.abspath(__file__))
T="MU TGT TJX AMZN COGT IMAX AVGO MOD CRDO MLYS EOSE INTU NOW CRM AMD NVDA BBIO PRAX LNG DG TTWO SPY QQQ IWM".split()
def load(t):
    if t in("SPY","QQQ","IWM"):
        d=pd.read_csv(f"{B}/raw/other/{t}.csv",parse_dates=["Date"]).rename(columns=str.lower).set_index("date")
        return d[["open","high","low","close","volume"]].sort_index(),"Consultor-ETF-IA (yfinance, adj.)"
    j=json.load(open(f"{B}/raw/muraken/{t}.json"))
    d=pd.DataFrame(j["data"]); d["date"]=pd.to_datetime(d["date"]); return d.set_index("date").sort_index(),"filings-digest-data"
rows=[];xv=[]
for t in T:
    d,src=load(t); d=d.dropna(subset=["close"]); c=d.close; last=c.iloc[-1]
    pc=c.shift(1); tr=pd.concat([d.high-d.low,(d.high-pc).abs(),(d.low-pc).abs()],axis=1).max(axis=1)
    atr=tr.ewm(alpha=1/14,adjust=False,min_periods=14).mean().iloc[-1]
    y=d.iloc[-252:]; hi=y.high.max(); lo=y.low.min()
    ch=lambda n:(last/c.iloc[-1-n]-1)*100
    m20=c.rolling(20).mean().iloc[-1]; m50=c.rolling(50).mean().iloc[-1]; m200=c.rolling(200).mean().iloc[-1]
    rows.append(dict(Ticker=t,Date=d.index[-1].date().isoformat(),Close=last,Chg1W=ch(5),Chg1M=ch(21),Chg3M=ch(63),
      Hi52=hi,PctFromHi=(last/hi-1)*100,Lo52=lo,PctFromLo=(last/lo-1)*100,ATR14=atr,ATRpct=atr/last*100,
      MA20=m20,vsMA20="above" if last>m20 else "below",MA50=m50,vsMA50="above" if last>m50 else "below",
      PctVsMA50=(last/m50-1)*100,PctVsMA200=(last/m200-1)*100,
      AvgVol20=d.volume.iloc[-20:].mean(),AvgVol50=d.volume.iloc[-50:].mean(),Above5="Y" if last>5 else "N",
      Stop1_5ATR=last-1.5*atr,Stop2ATR=last-2*atr,Stop2ATRpct=-2*atr/last*100,Bars=len(d),Source=src))
    # cross-validation
    p=f"{B}/raw/eshaan/{t}.csv"
    if os.path.exists(p):
        e=pd.read_csv(p,parse_dates=["Date"]).set_index("Date"); j=d.join(e[["Close","Volume"]],how="inner").iloc[-252:]
        xv.append((t,"eshaan",len(j),e.index[-1].date(),float((j.close/j.Close-1).abs().max()*100),float((j.close.iloc[-1]/j.Close.iloc[-1]-1)*100)))
    if t in("SPY","QQQ","IWM"):
        b=pd.read_csv(f"{B}/raw/blumenty/etfs.csv",parse_dates=["Date"]); b=b[b.Symbol==t].set_index("Date"); j=d.join(b[["Close"]],how="inner")
        xv.append((t,"blumenty",len(j),b.index[-1].date(),float((j.close/j.Close-1).abs().max()*100),float((j.close.iloc[-1]/j.Close.iloc[-1]-1)*100)))
df=pd.DataFrame(rows); df.to_csv(f"{B}/swing_stats.csv",index=False,float_format="%.4f")
pd.set_option("display.width",300); pd.set_option("display.max_columns",40); print(df.round(2).to_string())
print("XVAL ticker,src,n,lastdate,max|diff|% (252d),diff last %"); [print(x) for x in xv]
f=lambda v,n=2:f"{v:,.{n}f}"; s=lambda v:f"{v:+.1f}%"
vol=lambda v:f"{v/1e6:.2f}M"
L=["| Ticker | Close | 1W | 1M | 3M | 52W High | % from High | 52W Low | % from Low | ATR14 $ | ATR % | 20DMA | 50DMA | vs 20/50 | Avg Vol (20d) | >$5 | Stop 1.5x ATR | Stop 2x ATR |","|"+"---|"*18]
for r in rows:
    L.append(f"| {r['Ticker']} | {f(r['Close'])} | {s(r['Chg1W'])} | {s(r['Chg1M'])} | {s(r['Chg3M'])} | {f(r['Hi52'])} | {s(r['PctFromHi'])} | {f(r['Lo52'])} | {s(r['PctFromLo'])} | {f(r['ATR14'])} | {r['ATRpct']:.1f}% | {f(r['MA20'])} | {f(r['MA50'])} | {r['vsMA20']}/{r['vsMA50']} | {vol(r['AvgVol20'])} | {r['Above5']} | {f(r['Stop1_5ATR'])} | {f(r['Stop2ATR'])} ({r['Stop2ATRpct']:.1f}%) |")
open(f"{B}/swing_stats.md","w").write(f"Swing-trade stats as of close {rows[0]['Date']} (all tickers)\n\n"+"\n".join(L)+"\n")
print(set(r['Date'] for r in rows)); print("\n".join(L))

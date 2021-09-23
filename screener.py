from datetime import date, timedelta
import yfinance as yf
import pandas as pd
from ta import add_all_ta_features
from ta.utils import dropna
from ta.trend import MACD, ADXIndicator
from ta.momentum import RSIIndicator

tickers = ['AKZA.AS']
alerts = []

end = date.today() - timedelta(365)
#now = date.today()
#print(now.strftime("%a"))

def get_price(ticker):
    dfWeek = yf.download(ticker, period="2y", interval="1wk")
    dfWeek = dropna(dfWeek)
    macd = MACD(close=dfWeek['Adj Close'])
    adx = ADXIndicator(high=dfWeek['High'], low=dfWeek['Low'], close=dfWeek['Adj Close'])
    dfWeek['histoMACD'] = macd.macd_diff()
    dfWeek['di+'] = adx.adx_pos()

    dfDayly = yf.download(ticker, period="1y", interval="1d")
    dfDayly = dropna(dfDayly)
    rsi = RSIIndicator(close=dfDayly['Adj Close'])
    dfDayly['rsi'] = rsi.rsi()

    if dfWeek['di+'][-2] > dfWeek['di+'][-3]:
        print(dfWeek['di+'][-2])
        print(dfWeek['di+'][-3])
        if (dfWeek['histoMACD'][-2] < 0):
            print(dfWeek['histoMACD'][-2])
            if (dfWeek['histoMACD'][-2] > dfWeek['histoMACD'][-3]):
                print(dfWeek['histoMACD'][-3])
                if (dfDayly['rsi'][-1] < 70):
                    print(dfDayly['rsi'][-1])
                    alerts.append(ticker)

    print(alerts)
    print(dfWeek)

for ticker in tickers:
    get_price(ticker)

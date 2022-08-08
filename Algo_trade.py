#!/usr/bin/env python3
import pandas as pd
import numpy as np
import yfinance as yf
import matplotlib.pyplot as plt
import ta
from ta.utils import dropna
from ta.trend import EMAIndicator, ADXIndicator
from ta.momentum import RSIIndicator

data = pd.read_csv("BTC-USDT.csv")
data = data.sort_index(ascending=False)
#data = yf.download(tickers="BTC-USD",period="3mo",interval="1h")
data = dropna(data)
adx = ADXIndicator(high=data["high"],low=data["low"],close=data["close"],window=14)
ema100 = EMAIndicator(close=data["close"],window=20)
ema200 = EMAIndicator(close=data["close"],window=300)
ema50 = EMAIndicator(close=data["close"],window=200)
#rsi = RSIIndicator(close=data["Close"], window=14)
data["EMA100"]= ema100.ema_indicator()
data["EMA200"]= ema200.ema_indicator()
data["EMA50"]= ema50.ema_indicator()
data["ADX"] = adx.adx()


print(data.keys())

data.to_csv("BTC-USDT_alligator_ADX.csv")
#plt.figure(figsize=(12.2,4.5))
#plt.plot(data.index, data["Adj Close"], label="Adj close price")
#plt.plot(data.index, data["EMA100"],color="orange", label="EMA100")
#plt.plot(data.index, data["EMA200"],color="red", label="EMA200")
#plt.plot(data.index, data["EMA50"],color="green", label="EMA50")


#plt.title("Adj Close Price")
#plt.show()

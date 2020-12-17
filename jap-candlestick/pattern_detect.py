import talib 
import yfinance as yf

data = yf.download("SPY", start="2020-01-02", end="2020-12-16")



#integer = CDLENGULFING(open, high, low, close)
morning_star = talib.CDLMORNINGSTAR(data['Open'], data['High'], data['Low'], data['Close'])

engulfing = talib.CDLENGULFING(data['Open'], data['High'], data['Low'], data['Close'])

data['morning_star'] = morning_star
data['Engulfing'] = engulfing


engulfing_days = data[data['Engulfing'] != 0]
print(engulfing_days)
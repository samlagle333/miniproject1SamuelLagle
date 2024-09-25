# INF601 - Advanced Programming in Python
# Samuel Lagle
# Mini Project 1
import pprint
import yfinance as yf

mytickers = ["MSFT", "AAPL", "NVDA", "GME", "AMC"]

mydata = {}


mytickers.sort()
for ticker in mytickers:
    result = yf.Ticker(ticker)
    mydata[ticker] = {'ticker': ticker,
                      'dailyHigh': result.info['dayHigh'],
                      }
    print(f"Ticker: {ticker} \tDaily High: {result.info['dayHigh']}")



# get all stock info
#pprint.pprint(msft.info)

# get historical market data for ten days
#hist = msft.history(period="1mo")

#pprint.pprint(hist)
# Analyse Stock market
# pip install yfinance
import yfinance as yf
market = yf.Ticker("MSFT")
# Get stockmarket info
info = market.info
print(info)
# Fetch historical data
historical = market.history(period="1y")
print(historical)
# get actions
actions = market.actions
print(actions)
# get dividends
dividends = market.dividends
print(dividends)
# get splits
splits = market.splits
print(splits)
# get balance sheet
balance_sheet = market.balance_sheet
print(balance_sheet)
# get market news
market_news = market.news
print(market_news)
# show earnings
earnings = market.earnings
print(earnings)
# get recommendation
rec = market.recommendation
print(rec)
# Get another Ticker
market1 = yf.Ticker("AAPL")
market2 = yf.Ticker("TSLA")
market3 = yf.Ticker("GOOG")
# Fetch Market data from multiple tickers
market_data = yf.download("AAPL", "GOOG", start="2019-01-01", end="2019-12-31")
print(market_data)

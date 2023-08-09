import yfinance as yf

GameStop = yf.Ticker("GME")
gme_data = GameStop.history(period='max')
gme_data.reset_index(inplace=True)
print(gme_data.head())


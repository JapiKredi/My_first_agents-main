import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the tickers
tickers = ["NVDA", "TSLA"]

# Get data from this year
data = yf.download(tickers, start=pd.to_datetime('2022-01-01'), end=pd.to_datetime('today'))

# Calculate the percentage change
data_pc = data['Adj Close'].pct_change()

# Calculate cumulative product returns
data_pc_cum = (data_pc + 1).cumprod()

# Plot graphs for both Tickers
data_pc_cum.plot()
plt.title(f'Stock Price Change YTD for {" and ".join(tickers)}')

plt.show()
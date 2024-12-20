   import yfinance as yf
   import matplotlib.pyplot as plt

   # Download historical data for required stocks
   ticker = "GOOGL"
   title = f"{ticker} and Apple Stock Price Comparison"
   start_date = "2021-01-01"
   end_date = "2022-01-01"

   stock = yf.download(ticker, start=start_date, end=end_date)
   apple = yf.download('AAPL', start=start_date, end=end_date)

   # Calculate the daily percentage change for `close` price for each stock and drop NA values
   stock['returns'] = stock['Close'].pct_change().dropna()
   apple['returns'] = apple['Close'].pct_change().dropna()

   # Make the plot and make it look nicer
   fig, ax = plt.subplots()
   plt.title(title)
   stock['returns'].plot(ax=ax, style='-', label=ticker)
   apple['returns'].plot(ax=ax, style='-', label='AAPL')
   plt.legend()

   # Save the plot to a file
   plt.savefig('stock_price_change.png')
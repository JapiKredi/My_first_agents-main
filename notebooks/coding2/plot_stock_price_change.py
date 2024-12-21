# filename: plot_stock_price_change.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the stock symbols
stock_symbol = 'AAPL'  # Replace with the desired stock symbol
openai_symbol = 'OPENAI'  # Replace with OpenAI's stock symbol

# Fetch historical data for the given stock symbols
stock_data = yf.download(stock_symbol, period='1y')
openai_data = yf.download(openai_symbol, period='1y')

# Calculate the daily price change for each stock
stock_data['Price Change'] = stock_data['Close'].diff()
openai_data['Price Change'] = openai_data['Close'].diff()

# Plot the stock price change for both stocks
plt.plot(stock_data.index, stock_data['Price Change'], label=stock_symbol)
plt.plot(openai_data.index, openai_data['Price Change'], label=openai_symbol)

# Customize the plot
plt.title('Stock Price Change Comparison')
plt.xlabel('Date')
plt.ylabel('Price Change')
plt.legend()

# Save the plot as a PNG file
plt.savefig('stock_price_change.png')
plt.show()
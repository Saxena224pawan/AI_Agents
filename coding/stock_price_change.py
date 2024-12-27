# filename: stock_price_change.py
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Define the stock symbols and the period
stocks = ['AAPL', 'TSLA', 'NVDA', 'MSFT']
start_date = '2023-01-01'
end_date = '2023-12-31'

# Download the stock data
data = yf.download(stocks, start=start_date, end=end_date)

# Print the columns to check the structure (this should be commented out or removed for production)
print(data.columns)

# Access the 'Close' data from the MultiIndex for each stock
data_close = data['Close']

# Calculate the percentage change
percentage_change = data_close.pct_change().fillna(0) * 100

# Plotting
plt.figure(figsize=(14, 7))
for stock in stocks:
    plt.plot(percentage_change.index, percentage_change[stock], label=stock)

plt.title('Stock Price Change Comparison (2023)')
plt.xlabel('Date')
plt.ylabel('Percentage Change (%)')
plt.legend()
plt.grid()
plt.savefig('stock_price_change.png')
plt.close()
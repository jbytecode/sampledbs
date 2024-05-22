import yfinance

apple = yfinance.Ticker("AAPL")

print(apple.info)

apple_data = apple.history(period="1mo")

close_values = apple_data.Close 

print(close_values)

for i in range(len(close_values)):
    print("Day", i, ":", close_values.iloc[i])



import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Download Data
data = yf.download("AAPL", start="2020-01-01", end="2024-01-01")

close = data["Close"]["AAPL"]

df = pd.DataFrame()
df["Close"] = close

# Indicators
df["Returns"] = df["Close"].pct_change()
df["MA20"] = df["Close"].rolling(20).mean()

# Signal (158% strategy version)
df["Signal"] = 0
df.loc[df["Close"] > df["MA20"], "Signal"] = 1
df.loc[df["Close"] < df["MA20"], "Signal"] = -1

# Use yesterday signal
df["Position"] = df["Signal"].shift(1)

# Strategy Returns
df["Strategy_Return"] = df["Position"] * df["Returns"]

# Growth Curves
df["Market_Growth"] = (1 + df["Returns"]).cumprod()
df["Strategy_Growth"] = (1 + df["Strategy_Return"]).cumprod()

# Metrics
market_return = (df["Market_Growth"].iloc[-1] - 1) * 100
strategy_return = (df["Strategy_Growth"].iloc[-1] - 1) * 100

sharpe = (df["Strategy_Return"].mean() / df["Strategy_Return"].std()) * np.sqrt(252)

rolling_max = df["Strategy_Growth"].cummax()
drawdown = df["Strategy_Growth"] / rolling_max - 1
max_drawdown = drawdown.min() * 100

print("Market Return:", round(market_return,2), "%")
print("Strategy Return:", round(strategy_return,2), "%")
print("Sharpe Ratio:", round(sharpe,2))
print("Max Drawdown:", round(max_drawdown,2), "%")

# Plot
plt.figure(figsize=(12,6))
plt.plot(df.index, df["Market_Growth"], label="Market")
plt.plot(df.index, df["Strategy_Growth"], label="Strategy")
plt.title("Strategy vs Market Growth")
plt.xlabel("Date")
plt.ylabel("Growth")
plt.legend()
plt.grid(True)
plt.show()
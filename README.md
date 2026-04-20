# Python Trading Backtester

A systematic trading strategy backtesting engine built in Python using historical market data.

## Features

- Downloads real stock data using yfinance
- Generates buy/sell signals using moving averages
- Compares strategy returns vs buy-and-hold benchmark
- Calculates Sharpe ratio and max drawdown
- Visualizes cumulative growth using matplotlib

## Strategy Used

- Buy when price is above 20-day moving average
- Sell when price is below 20-day moving average
- Uses lagged positions to avoid look-ahead bias

## Performance (AAPL 2020–2024)

- Market Return: 163.19%
- Strategy Return: 158.43%

## Technologies

Python, pandas, numpy, matplotlib, yfinance

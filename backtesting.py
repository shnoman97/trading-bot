# backtesting.py

import pandas as pd
import matplotlib.pyplot as plt
import logging

def backtest_strategy(data):
    df = data.copy()
    df['MA_Short'] = df['close'].rolling(window=10).mean()
    df['MA_Long'] = df['close'].rolling(window=30).mean()
    df.dropna(inplace=True)

    df['Signal'] = 0
    df.loc[df['MA_Short'] > df['MA_Long'], 'Signal'] = 1
    df.loc[df['MA_Short'] < df['MA_Long'], 'Signal'] = -1

    df['Position'] = df['Signal'].shift(1)
    df['Market_Returns'] = df['close'].pct_change()
    df['Strategy_Returns'] = df['Position'] * df['Market_Returns']

    df['Cumulative_Market_Returns'] = (1 + df['Market_Returns']).cumprod()
    df['Cumulative_Strategy_Returns'] = (1 + df['Strategy_Returns']).cumprod()

    total_return = df['Cumulative_Strategy_Returns'].iloc[-1] - 1
    logging.info(f"Total Strategy Return: {total_return:.2%}")

    # Plotting
    plt.figure(figsize=(12,6))
    plt.plot(df['time'], df['Cumulative_Market_Returns'], label='Market Returns')
    plt.plot(df['time'], df['Cumulative_Strategy_Returns'], label='Strategy Returns')
    plt.title('Backtesting Results')
    plt.xlabel('Time')
    plt.ylabel('Cumulative Returns')
    plt.legend()
    plt.show()

# strategy.py

import logging

def generate_signal(data):
    df = data.copy()
    df['MA_Short'] = df['close'].rolling(window=10).mean()
    df['MA_Long'] = df['close'].rolling(window=30).mean()
    df.dropna(inplace=True)

    signal = None
    if df['MA_Short'].iloc[-1] > df['MA_Long'].iloc[-1] and df['MA_Short'].iloc[-2] <= df['MA_Long'].iloc[-2]:
        signal = 'buy'
        logging.info("Buy signal generated")
    elif df['MA_Short'].iloc[-1] < df['MA_Long'].iloc[-1] and df['MA_Short'].iloc[-2] >= df['MA_Long'].iloc[-2]:
        signal = 'sell'
        logging.info("Sell signal generated")
    else:
        logging.info("No signal generated")

    return signal

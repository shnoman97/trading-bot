# data_handler.py

import MetaTrader5 as mt5
import pandas as pd
import logging

def fetch_data(symbol, timeframe, bars=1000):
    rates = mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)
    if rates is None or len(rates) == 0:
        logging.error(f"No data fetched for {symbol}")
        return None
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    logging.info(f"Fetched {len(df)} bars for {symbol}")
    return df

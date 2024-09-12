# trade_executor.py

import MetaTrader5 as mt5
import logging

def place_order(symbol, order_type, volume, price=None, stop_loss=None, take_profit=None, deviation=20):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        logging.error(f"{symbol} not found")
        return False

    if not symbol_info.visible:
        if not mt5.symbol_select(symbol, True):
            logging.error(f"symbol_select({symbol}) failed")
            return False

    if price is None:
        if order_type == mt5.ORDER_TYPE_BUY:
            price = mt5.symbol_info_tick(symbol).ask
        elif order_type == mt5.ORDER_TYPE_SELL:
            price = mt5.symbol_info_tick(symbol).bid

    request = {
        "action": mt5.TRADE_ACTION_DEAL,
        "symbol": symbol,
        "volume": volume,
        "type": order_type,
        "price": price,
        "sl": stop_loss,
        "tp": take_profit,
        "deviation": deviation,
        "magic": 123456,
        "comment": "Python script open",
        "type_time": mt5.ORDER_TIME_GTC,
        "type_filling": mt5.ORDER_FILLING_RETURN,
    }

    result = mt5.order_send(request)
    if result.retcode != mt5.TRADE_RETCODE_DONE:
        logging.error(f"Failed to place order: {result.comment}")
        return False
    else:
        logging.info(f"Order placed successfully: {result}")
        return True

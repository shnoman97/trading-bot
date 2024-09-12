# connection_manager.py

import MetaTrader5 as mt5
import logging

def connect_to_mt5(login=None, password=None, server=None, path=None):
    if not mt5.initialize(login=login, password=password, server=server, path=path):
        logging.error(f"initialize() failed, error code = {mt5.last_error()}")
        return False
    else:
        logging.info("Connected to MetaTrader5")
        return True

def disconnect_from_mt5():
    mt5.shutdown()
    logging.info("Disconnected from MetaTrader5")

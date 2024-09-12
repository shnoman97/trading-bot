# risk_manager.py

import logging

def calculate_position_size(balance, risk_per_trade, stop_loss_pips, pip_value):
    risk_amount = balance * risk_per_trade
    position_size = risk_amount / (stop_loss_pips * pip_value)
    logging.info(f"Calculated position size: {position_size}")
    return position_size

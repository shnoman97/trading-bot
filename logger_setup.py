# logger_setup.py

import logging
import os

def setup_logger(name='trading_bot', log_dir='logs', level=logging.INFO):
    logger = logging.getLogger()
    logger.setLevel(level)

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
    log_file = os.path.join(log_dir, f"{name}.log")

    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Clear previous handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    logger.addHandler(file_handler)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

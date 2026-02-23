# utils/logger.py

import logging
import os
from logging.handlers import RotatingFileHandler

class LogGenerator:
    _logger = None

    @staticmethod
    def get_logger(log_level=logging.INFO):
        if LogGenerator._logger:
            return LogGenerator._logger
        logger = logging.getLogger("TestAutomationLogger")
        logger.setLevel(log_level)
        # Prevent duplicate logs
        if logger.hasHandlers():
            logger.handlers.clear()
        # Create logs directory if it doesn't exist
        os.makedirs("reports/logger/logs", exist_ok=True)
        # File handler with rotation (5 files, 2MB each)
        file_handler = RotatingFileHandler(
            "reports/logger/logs.log", maxBytes=2 * 1024 * 1024, backupCount=5
        )
        file_formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(message)s"
        )
        file_handler.setFormatter(file_formatter)
        # Console handler (optional)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(file_formatter)
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        LogGenerator._logger = logger
        return logger

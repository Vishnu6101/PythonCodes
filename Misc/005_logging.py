import logging
import os

from from_root import from_root
from datetime import datetime

from logging.handlers import TimedRotatingFileHandler


def setup_logger(name, log_level=logging.DEBUG):

    log_dir = "logs"
    logs_path = os.path.join(from_root(), log_dir)

    # creating the log directory
    os.makedirs(logs_path, exist_ok=True)

    log_file = "app.log"
    log_file_path = os.path.join(logs_path, log_file)

    # log handler
    handler = TimedRotatingFileHandler(filename=log_file_path, 
                                    when="H", 
                                    interval=6, 
                                    backupCount=28, 
                                    encoding='utf-8')

    handler.suffix = "%Y-%m-%d %H"

    formatter = logging.Formatter("[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(log_level)
    logger.addHandler(handler)

    return logger


logger = setup_logger(__file__)
logger.info("Logger")

# This function can be used in a project for logging with file names
# It uses TimedRotatingFileHandler to rotate log files for every 6 hours and keeps a backup for 1 week
import logging
import sys
import os

logging_str = f"[%(asctime)s - [%(levelname)s] - %(module)s - (%(filename)s).%(funcName)s(%(lineno)d)] : %(message)s"
log_dir = "./logs"
log_filepath = os.path.join(log_dir, "data_extraction_logs.log")
os.makedirs(log_dir, exist_ok=True)


def get_file_handler():
    file_handler = logging.FileHandler(log_filepath)
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter(logging_str))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(logging_str))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger


logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        get_stream_handler(),
        get_file_handler(),
    ],
)

logger = logging.getLogger("dataExtraction")

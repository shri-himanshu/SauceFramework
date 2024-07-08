import logging
import sys

# ANSI color escape sequences
COLORS = {
    'DEBUG': '\033[94m',    # Blue
    'INFO': '\033[92m',     # Green
    'WARNING': '\033[93m',  # Yellow
    'ERROR': '\033[91m',    # Red
    'CRITICAL': '\033[91m\033[1m'  # Bold Red
}

class ColoredFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        if levelname in COLORS:
            record.levelname = f'{COLORS[levelname]}{levelname}\033[0m'  # Apply color to levelname
        return super().format(record)

def setup_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        ch = logging.StreamHandler(stream=sys.stdout)
        ch.setLevel(logging.DEBUG)
        formatter = ColoredFormatter('%(asctime)s UTC %(levelname)s <%(threadName)s> [%(name)s]: %(message)s (%(filename)s:%(lineno)d)',
                                     datefmt='%Y/%m/%d %H:%M:%S,%f'[:-3])
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    return logger


import logging
import sys

from logging import Logger
from logging.handlers import TimedRotatingFileHandler

class Logger(object):

    def log(self, message, logType='info'):
        log_message = f'{message}'

        if logType == 'info':
            logging.info(log_message)
            print(f'{log_message}')
        elif logType == 'debug':
            logging.debug(log_message)
            print(f'{log_message}')
        elif logType == 'warning':
            logging.warning(log_message)
        elif logType == 'error':
            logging.error(log_message)
        elif logType == 'critical':
            logging.critical(log_message)

#!/usr/bin/env python3

"""
contains:
    class `RedactingFormatter`
    function `filter_datum`
    function `get_logger`
"""


import re
import logging
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log records using filter_datum """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return super().format(record)


def get_logger() -> logging.Logger:
    """
    args:   None
    return: logger: logging.Logger object
    """
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    formatter = RedactingFormatter(list(PII_FIELDS))
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function scrubs selected PII data fields with regex"""
    return re.sub('|'.join('(?<={}=).*?(?={})'.format(field, separator)
                           for field in fields), redaction, message)

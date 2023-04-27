#!/usr/bin/env python3

"""
contains:
    class `RedactingFormatter`
    function `filter_datum`
    function `get_logger`
    function `get_db`
"""

import logging
import mysql.connector
from os import environ
import re
from typing import List


PII_FIELDS: tuple = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    function scrubs selected PII data fields with regex
    args:   fields: List[str]
            redaction: str
            message: str
            separator: str
    return: cleaned: str
    """
    cleaned = re.sub('|'.join('(?<={}=).*?(?={})'.format(field, separator)
                              for field in fields), redaction, message)
    return (cleaned)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        filter values in incoming log records using filter_datum
        args:   record: logging.LogRecord
        return: str
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR)
        return (super().format(record))


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
    return (logger)


def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    args:   None
    return: connector: mysql.connector.connection.MySQLConnection
    """
    username = environ.get('PERSONAL_DATA_DB_USERNAME', 'root')
    password = environ.get('PERSONAL_DATA_DB_PASSWORD', '')
    host = environ.get('PERSONAL_DATA_DB_HOST', 'localhost')
    database = environ.get('PERSONAL_DATA_DB_NAME')

    connector = mysql.connector.connect(user=username, password=password,
                                        host=host, database=database)
    return (connector)

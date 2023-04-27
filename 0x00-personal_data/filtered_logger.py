#!/usr/bin/env python3

"""
contains:
    class `RedactingFormatter`
    function `filter_datum`
    function `get_logger`
    function `get_db`
"""

from datetime import datetime
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
    returns a connector to the database
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


def main() -> None:
    """
    obtains a database connection using `get_db`
        and retrieve all rows in the users table and display
        each row under a filtered format
    args:   None
    return: None
    """
    logger: logging.Logger = get_logger()
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM users;')
    fields = ['name', 'email', 'phone', 'ssn',
              'password', 'ip', 'last_login', 'user_agent']
    filtered_fields = ['name', 'email', 'phone', 'ssn', 'password']
    for row in cursor:
        data = dict(zip(fields, row))
        filtered_data = {
            key: '***' if key in filtered_fields else values
            for key, values in data.items()}
        # x = "name=%(name)s; email=%(email)s; phone=%(phone)s; ssn=%(ssn)s;"\
        #     "password=%(password)s; ip=%(ip)s; last_login=%(last_login)s;"\
        #     "user_agent=%(user_agent)s;"
        # logger.info(x, filtered_data)
        # logger.info('Filtered fields: %s', ', '.join(filtered_fields))

        x = "name={name}; email={email}; phone={phone}; ssn={ssn};" \
            "password={password}; ip={ip}; last_login={last_login};" \
            "user_agent={user_agent};"
        logger.info(x.format(**filtered_data))
        logger.info('Filtered fields: %s', ', '.join(filtered_fields))
    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Regex-ing
"""
from typing import List
import re
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """function called filter_datum that returns the log message obfuscated

    Args:
        fields (List[str]): representing all fields to obfuscate
        redaction (str): representing by what the field will be obfuscated
        message (str): representing the log line
        separator (str): representing by which character is separating
        all fields in the log line (message)

    Returns:
        str: log message obfuscated
    """
    for field in fields:
        message = re.sub(fr'{field}=.+?{separator}',
                         f'{field}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum.
        Values for fields in fields should be filtered.

        Args:
            record (logging.LogRecord): [description]

        Returns:
            str: Log formatter
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Get logger

    Returns:
        ogging.Logger: object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger

def get_db() -> mysql.connector.connection.MySQLConnection:
    """
    connect to the MySQL database
    """
    username = getenv('PERSONAL_DATA_DB_USERNAME')
    password = getenv('PERSONAL_DATA_DB_PASSWORD')
    host = getenv('PERSONAL_DATA_DB_HOST')
    db = getenv('PERSONAL_DATA_DB_NAME')

    conect = mysql.connector.connection.MySQLConnection(
        host=host,
        user=username,
        password=password,
        database=db
    )
    return conect


def main():
    """
    get data from database
    """
    data = get_db()
    myCursor = data.cursor()
    myCursor.execute("SELECT * FROM users")
    description = [desc[0] for desc in myCursor.description]

    logger = get_logger()

    for user in myCursor:
        userInfo = "".join(
            f'{des}={str(usr)}; ' for usr, des in zip(user, description)
        )
        logger.info(userInfo)

    myCursor.close()
    data.close()


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""
Regex-ing
"""
from typing import List
import re
import logging


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

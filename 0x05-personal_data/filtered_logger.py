#!/usr/bin/env python3
"""
Regex-ing
"""
from typing import List
import re


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

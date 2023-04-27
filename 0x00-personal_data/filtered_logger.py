#!/usr/bin/env python3
""" 0x05. Personal data

"""

import logging
import os
import re
import mysql.connector
from typing import List


PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: 
    str, separator: str) -> str:
    """ a function called filter_datum that returns the log message obfuscated:
        Args:
            fields: a list of strings representing all fields to obfuscate
            redaction: a string representing by what the field will be obfuscated
            message: a string representing the log line
            separator: a string representing by which character is separating all 
            fields in the log line (message) 
        Returns: message
    """
    for format in fields:
        message = re.sub(rf"{format}=(.*?)\{separator}",
                         f'{format}={redaction}{separator}', message)
    return message

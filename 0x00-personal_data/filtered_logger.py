#!/usr/bin/env python3
""" 0x05. Personal data
How to implement a log filter that will obfuscate PII fields
How to encrypt a password and check the validity
How to authenticate to a database using environment variables
"""
import os
import re
import mysql.connector
from typing import List
import logging

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """ a function called filter_datum that returns the log message
        Args:
            fields: a list of strings representing all fields
            redaction: a string representing by what the field 
            message: a string representing the log line
            separator: a string representing by which character is 
            separating all fields in the log line (message) 
        Returns: message
    """
    for format in fields:
        message = re.sub(rf"{format}=(.*?)\{separator}",
                         f'{format}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ Init """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ Format """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)
#!/usr/bin/env python3
"""defines a filter_datum function"""
import logging
import re
from typing import List


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """obfuscate log messages

    Args:
        fields (List): a list of strings representing all fields
        redaction (str): what feilds will be obfuscated
        message (str): the log line
        separtor (str): the charecter seperater in the log

    Returns:
        str: the log message obfuscated
    """
    for field in fields:
        pattern = fr'{field}=[^{separator}]*'
        message = re.sub(pattern, f'{field}={redaction}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]) -> None:
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """fomat record message
        """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.msg,
                                  self.SEPARATOR)
        return super(RedactingFormatter, self).format(record)


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def get_logger() -> logging.Logger:
    """returns a logger object"""
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handeler = logging.StreamHandler()
    formater = logging.Formatter(PII_FIELDS)

    stream_handeler.setFormatter(formater)
    logger.addHandler(stream_handeler)
    return logger

#!/usr/bin/env python3
"""defines a filter_datum function"""
import re
from typing import List


def filter_datum(fields: List,
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
    escape = map(re.escape, fields)
    fields_regex = '|'.join(escape)
    pattern = f'({fields_regex}=)[^{re.escape(separator)}]*'
    return re.sub(pattern, f'\\1{redaction}', message)

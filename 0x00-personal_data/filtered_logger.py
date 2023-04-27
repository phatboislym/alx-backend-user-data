#!/usr/bin/env python3

"""
contains:
    function `filter_datum`
"""


import re


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """
    args:   fields: list[str]
            redaction: str
            message: str
            separator: str
    return: redacted: str 
    """
    pattern = '|'.join('(?<={}=).*?(?={})'.format(field, separator)
                       for field in fields)
    redacted = re.sub(pattern, redaction, message)
    return (redacted)

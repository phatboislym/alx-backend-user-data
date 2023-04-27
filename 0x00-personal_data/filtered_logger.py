#!/usr/bin/env python3

"""
contains:
    function `filter_datum`
"""


import re


def filter_datum(fields: list[str], redaction: str, message: str,
                 separator: str) -> str:
    """ function scrubs selected PII data fields with regex"""
    return re.sub('|'.join('(?<={}=).*?(?={})'.format(field, separator)
                           for field in fields), redaction, message)

#!/usr/bin/env python3

"""
contains:
    function `hash_password`
"""

from bcrypt import gensalt, hashpw


def hash_password(password: str) -> bytes:
    """
    args:   password: str
    return: hashed: bytes
    """
    password_bytes: bytes = password.encode('utf-8')
    salt = gensalt()
    hashed: bytes = hashpw(password_bytes, salt)
    return (hashed)

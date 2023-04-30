#!/usr/bin/env python3

"""
contains:
    function `hash_password`
    function `is_valid`
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """
    args:   password: str
    return: hashed: bytes
    """
    password_bytes: bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(password_bytes, salt)
    return (hashed)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    args:   hashed_password: bytes
            password: str
    return: True | False: bool
    """
    password_bytes: bytes = password.encode('utf-8')
    if bcrypt.checkpw(password_bytes, hashed_password):
        return True
    return False

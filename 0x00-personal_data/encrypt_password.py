#!/usr/bin/env python3

"""
contains:
    function `hash_password`
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

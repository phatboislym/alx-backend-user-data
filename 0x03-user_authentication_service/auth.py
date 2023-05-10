#!/usr/bin/env python3

"""
module for auth
contains:
    function `_hash_password`
"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes
    args:   password: str
    return: bytes_string: bytes
    """
    password_bytes: bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(password_bytes, salt)
    return (hashed)

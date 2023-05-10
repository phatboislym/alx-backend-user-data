#!/usr/bin/env python3

"""
module for auth
contains:
    function `_hash_password`
    class `Auth`
"""

import bcrypt
from db import DB, NoResultFound
from user import User


def _hash_password(password: str) -> bytes:
    """
    takes in a password string arguments and returns bytes
    args:   password: str
    return: bytes_string: bytes
    """
    password_bytes: bytes = password.encode('utf-8')
    salt: bytes = bcrypt.gensalt()
    hashed: bytes = bcrypt.hashpw(password_bytes, salt)
    return (hashed)


class Auth:
    """
    Auth class to interact with the authentication database
    methods:    class constructor
                register_user
    """

    def __init__(self) -> None:
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register a new user
        args:   self
                email: str
                password: str
        return: user: User
        """
        try:
            user: User = self._db.find_user_by(email=email)
            raise ValueError(f"User {user.email} already exists")
        except NoResultFound:
            hashed_password: bytes = _hash_password(password)
            user: User = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return user

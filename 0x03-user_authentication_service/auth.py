#!/usr/bin/env python3

"""
module for auth
contains:
    function `_hash_password`
    function `_generate_uuid`
    class `Auth`
"""

import bcrypt
from db import DB, NoResultFound
from typing import Optional
from uuid import UUID, uuid4
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


def _generate_uuid() -> str:
    """
    generate and return a string representation of a new UUID
    private function only to be used within the auth module
    args:   None
    return: unique_id: str
    """
    _unique_id: UUID = uuid4()
    unique_id: str = str(_unique_id)
    return unique_id


class Auth:
    """
    Auth class to interact with the authentication database
    methods:    class constructor
                register_user
                valid_login
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

    def valid_login(self, email: str, password: str) -> bool:
        """
        locate the user by email
        if it exists, check the password with bcrypt.checkpw
        args:   self
                email: str
                password: str
        return: True | False: bool
        """
        try:
            user: User = self._db.find_user_by(email=email)
            password_bytes: bytes = password.encode('utf-8')
            valid: bool = bcrypt.checkpw(password_bytes, user.hashed_password)
            return valid
        except ValueError:
            return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> Optional[str]:
        """
        takes an email string argument and returns the session ID as a string
        args:   self
                email: str
        return: session_id, optional
        """
        try:
            user: User = self._db.find_user_by(email=email)
            session_id: str = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()

            return session_id
        except ValueError:
            return None
        except NoResultFound:
            return None

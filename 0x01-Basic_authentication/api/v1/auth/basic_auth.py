#!/usr/bin/env python3

"""
module to manage API authentication
contains:
    class `BasicAuth`
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from models.user import User
from typing import Optional, Tuple, TypeVar


User = TypeVar("User")


class BasicAuth(Auth):
    """
    class for API authentication
    inherits from class Auth
    methods:
        class constructor
        extract_base64_authorization_header
        decode_base64_authorization_header
    """

    def __init__(self) -> None:
        pass

    def extract_base64_authorization_header(
            self, authorization_header: str) -> Optional[str]:
        """
        returns the Base64 part of the Authorization header
        args:   self
                authorization_header: str
        return: Optional[str]
        """
        base64_header: Optional[str] = None
        auth_header = authorization_header
        if (auth_header is None) or (type(auth_header) != str):
            return (base64_header)
        elif authorization_header.startswith("Basic "):
            base64_header = authorization_header[6:]
            return (base64_header)
        else:
            return (base64_header)

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> Optional[str]:
        """
        returns the decoded value of a base64_authorization_header string
        args:   self
                base64_authorization_header
        return: Optional[str]
        """
        base64_value: Optional[str] = None
        base64_header = base64_authorization_header
        if (base64_header is None) or (type(base64_header) != str):
            return (base64_value)
        try:
            base64_bytes: bytes = base64.b64decode(base64_header)
            base64_value = base64_bytes.decode('utf-8')
            return (base64_value)
        except (binascii.Error, UnicodeDecodeError):
            return None

    def extract_user_credentials(
            self, decoded_base64_authorization_header: str) -> Tuple[str, str]:
        """
        returns the user email and password from the Base64 decoded value
        args:   self
                decoded_base64_authorization_header: str
        return: credentials: Tuple[str, str] | defualt: Tuple[None, None]
        """
        credentials: Tuple[str, str] = ("", "")
        default: tuple = (None, None)
        if (decoded_base64_authorization_header is None):
            return (default)
        elif (not isinstance(decoded_base64_authorization_header, str)):
            return (default)
        else:
            split = decoded_base64_authorization_header.split(":")
            if (len(split) != 2):
                return (default)
            elif (len(split) == 2):
                credentials = tuple(split)
            return (credentials)

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> Optional[User]:
        """
        returns the User instance based on his email and password
        args:   self
                user_email: str
                user_pwd: str
        return: user: User
        """
        if (user_email is None) or (not isinstance(user_email, str)):
            return None
        elif (user_pwd is None) or (not isinstance(user_pwd, str)):
            return None
        else:
            token: dict = {"email": user_email}
            try:
                users: list = User.search(token)
                if not users:
                    return None
                for user in users:
                    if user.is_valid_password(user_pwd):
                        return (user)
            except (AttributeError, TypeError):
                return None
        return None

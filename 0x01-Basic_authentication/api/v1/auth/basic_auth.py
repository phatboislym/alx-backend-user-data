#!/usr/bin/env python3

"""
module to manage API authentication
contains:
    class `BasicAuth`
"""
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import Optional


class BasicAuth(Auth):
    """
    class for API authentication
    inherits from class Auth
    methods:
        class constructor
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

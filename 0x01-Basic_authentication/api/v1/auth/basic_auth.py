#!/usr/bin/env python3

"""
module to manage API authentication
contains:
    class `BasicAuth`
"""
from api.v1.auth.auth import Auth
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

    def extract_base64_authorization_header(self, authorization_header: str) -> Optional[str]:
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

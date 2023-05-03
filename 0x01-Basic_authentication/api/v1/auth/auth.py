#!/usr/bin/env python3

"""
module to manage API authentication
contains:
    class `Auth`
"""

from flask import request
from typing import List, TypeVar


class Auth():
    """
    class for API authentication
    methods:
        class constructor
        require_auth
        authorization_header
        current_user
    """

    def __init__(self) -> None:
        pass

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        checks if authentication is required for a given path
        args:   path: str
                excluded_paths: List[str]
        return: True|False: bool
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        gets the value of the authorization header from a Flask request object
        args:   request: flask.Request, optional
        return: header: str|None
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        gets the current user from a Flask request object
        args:   request: flask.Request, optional
        return: User: TypeVar('User')
        """
        return None

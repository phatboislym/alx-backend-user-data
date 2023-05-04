#!/usr/bin/env python3

"""
module to manage API authentication
contains:
    class `Auth`
"""

from flask import request
from typing import List, Optional, TypeVar


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
        return: requires_auth: bool
        """
        requires_auth = True
        if ((path is None) or (excluded_paths is None)):
            return (requires_auth)
        elif (len(excluded_paths) == 0):
            return (requires_auth)
        else:
            excluded_paths_2: List[str] = [excluded_path.strip('/')
                                           for excluded_path in excluded_paths]
            if (path.strip('/') not in excluded_paths_2):
                return (requires_auth)
            else:
                for excluded_path in excluded_paths_2:
                    if path.startswith(excluded_path):
                        requires_auth = False
                        return (requires_auth)
        requires_auth = False
        return (requires_auth)

    def authorization_header(self, request=None) -> Optional[str]:
        """
        gets the value of the authorization header from a Flask request object
        args:   request: flask.Request, optional
        return: header: str|None
        """
        if (request is None):
            return None
        elif ('Authorization' not in request.headers):
            return None
        else:
            authorization: str = request.headers.get('Authorization')
            return (authorization)

    def current_user(self, request=None) -> TypeVar('User'):
        """
        gets the current user from a Flask request object
        args:   request: flask.Request, optional
        return: User: TypeVar('User')
        """
        return None

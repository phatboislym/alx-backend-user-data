#!/usr/bin/env python3

"""
module to manage API authentication
contains:
    class `Auth`
"""

# from flask import request
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
        return: requires_auth: bool
        """
        requires_auth = True
        if ((path is None) or (excluded_paths is None)):
            return (requires_auth)
        elif (len(excluded_paths) == 0):
            return (requires_auth)
        elif ((path not in excluded_paths) and
              (path.strip('/') not in excluded_paths)):
            return (requires_auth)
        else:
            for excluded_path in excluded_paths:
                if path.startswith(excluded_path):
                    requires_auth = False
                    return (requires_auth)
                else:
                    return (requires_auth)
        requires_auth = False
        return (requires_auth)

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


a = Auth()

print(a.require_auth(None, None))
print(a.require_auth(None, []))
print(a.require_auth("/api/v1/status/", []))
print(a.require_auth("/api/v1/status/", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/status", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/"]))
print(a.require_auth("/api/v1/users", ["/api/v1/status/", "/api/v1/stats"]))

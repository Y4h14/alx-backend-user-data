#!/usr/bin/env python3
"""define a python auth module"""
from flask import request
from typing import List, TypeVar
from models.user import User
from os import getenv


class Auth():
    """Authontication Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): the request path
            excluded_paths (List[str]):
            list of pathes that require authentication

        Returns:
            bool: returns True if the path is not
            in the list of strings excluded_paths
        """
        if path is None or excluded_paths is None or excluded_paths == []:
            return True

        if not path.endswith('/'):
            path = path + '/'

        if path in excluded_paths:
            return False
        else:
            return True

    def authorization_header(self, request=None) -> str:
        """checks if the request header contains Authorization

        Args:
            request (_type_, optional): icoming request Defaults to None.

        Returns:
            str: None - request will be the Flask request object
        """
        if request is None:
            return None

        if "Authorization" in request.headers:
            return request.headers.get('Authorization')
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """get current user
        """
        return None

    def session_cookie(self, request=None):
        """returns a cookie value form request"""
        if request:
            cookie_name = getenv('SESSION_NAME')
            return request.cookies.get(cookie_name)

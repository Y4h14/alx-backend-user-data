#!/usr/bin/env python3
"""define a python auth module"""
from flask import request
from typing import List, TypeVar
from models.user import User


class Auth():
    """Authontication Class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
            path (str): _description_
            excluded_paths (List[str]): _description_

        Returns:
            bool: False - path and excluded_paths
        """
        pass

    def authorization_header(self, request=None) -> str:
        """_summary_

        Args:
            request (_type_, optional): _description_. Defaults to None.

        Returns:
            str: None - request will be the Flask request object
        """
        pass

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        pass

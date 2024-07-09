#!/usr/bin/env python3
"""define basic authentication"""
from .auth import Auth


class BasicAuth(Auth):
    """class for Basic Authentication"""
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """_summary_

        Args:
            authorization_header (str): _description_

        Returns:
            str: retrun Base64 part of the Authentication header
        """
        if authorization_header is None:
            return None

        if not isinstance(authorization_header, str):
            return None

        if authorization_header.startswith('Basic '):
            result = authorization_header.split('Basic ', 1)
            return result[1]
        else:
            return None

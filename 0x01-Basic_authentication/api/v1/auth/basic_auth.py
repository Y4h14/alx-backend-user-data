#!/usr/bin/env python3
"""define basic authentication"""
from .auth import Auth
import base64
import binascii
from typing import Tuple, TypeVar
from models.user import User


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

    def decode_base64_authorization_header(
            self,
            base64_authorization_header: str) -> str:
        """_summary_

        Args:
            base64_authorization_header (str): _description_

        Returns:
            str: return the decoded value of base64 string
        """
        if base64_authorization_header:
            if isinstance(base64_authorization_header, str):
                try:
                    res = base64.b64decode(
                        base64_authorization_header,
                        validate=True
                    )
                    return res.decode('utf-8')
                except (binascii.Error, UnicodeDecodeError):
                    return None
        else:
            return None

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value.

        Args:
            str (_type_): _description_
        """
        if decoded_base64_authorization_header:
            if isinstance(decoded_base64_authorization_header, str):
                parts = decoded_base64_authorization_header.split(':', 1)
                if len(parts) != 2:
                    return None, None
                email, password = parts
                return email, password

        return None, None

    def user_object_from_credentials(
            self, user_email: str, user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password.
        """
        if user_email and user_pwd:
            if isinstance(user_email, str) and isinstance(user_pwd, str):
                try:
                    users = User.search({'email': user_email})
                except Exception:
                    return None

                if len(users) <= 0:
                    return None

                if users[0].is_valid_password(user_pwd):
                    return users[0]

        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """retrieves the User instance for a request
        """
        auth_header = self.authorization_header(request)
        base64_token = self.extract_base64_authorization_header(auth_header)
        utf8_token = self.decode_base64_authorization_header(base64_token)
        email, password = self.extract_user_credentials(utf8_token)
        return self.user_object_from_credentials(email, password)

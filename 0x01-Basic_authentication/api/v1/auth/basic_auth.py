#!/usr/bin/env python3
"""define basic authentication"""
from .auth import Auth
import base64
import binascii


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

    def decode_base64_authorization_header(self,
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

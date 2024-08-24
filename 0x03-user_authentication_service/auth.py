#!/usr/bin/python3
"""defines hash password method"""
from bcrypt import hashpw, gensalt
from db import DB
from user import User


def _hash_password(password: str) -> bytes:
    """hashes a password"""
    salt = gensalt()
    return hashpw(password=password.encode(), salt=salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a new user into the system"""

        if self._db.find_user_by(email=email):
            raise ValueError(f'User {email} already exitsts')
        hashed_pass = _hash_password(password=password)
        user = self._db.add_user(email=email, password=hashed_pass)
        return user

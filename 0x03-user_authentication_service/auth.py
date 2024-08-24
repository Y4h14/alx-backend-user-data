#!/usr/bin/env python3
"""defines hash password method"""
from bcrypt import hashpw, gensalt, checkpw
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

        try:
            self._db.find_user_by(email=email)
        except Exception:
            hashed_pass = _hash_password(password=password)
            user = self._db.add_user(email=email, hashed_password=hashed_pass)
            return user
        raise ValueError(f'User {email} already exitsts')

    def valid_login(self, email: str, password: str) -> bool:
        """locates a user by email and verify the password"""
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return checkpw(password.encode(), user.hashed_password)
        except Exception:
            return False
        return False

#!/usr/bin/env python3
"""defines an encryption function"""
import bcrypt
from typing import ByteString


def hash_password(password: str) -> ByteString:
    """hashes a apassword"""
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """checks if a password matches a hash value"""
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)

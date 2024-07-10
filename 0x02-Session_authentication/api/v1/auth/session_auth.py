#!/usr/bin/env python3
"""defines  a session authentication class"""
from .auth import Auth
import uuid


class SessionAuth(Auth):
    """class for session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates session ID for a user_id"""
        if user_id and isinstance(user_id, str):
            session_id = uuid.uuid4()
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

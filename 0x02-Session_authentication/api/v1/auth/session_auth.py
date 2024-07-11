#!/usr/bin/env python3
"""defines  a session authentication class"""
from .auth import Auth
import uuid
from models.user import User


class SessionAuth(Auth):
    """class for session authentication"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates session ID for a user_id"""
        if user_id and isinstance(user_id, str):
            session_id = str(uuid.uuid4())
            self.user_id_by_session_id[session_id] = user_id
            return session_id
        return None

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns a User ID based on session ID"""
        if session_id and isinstance(session_id, str):
            return self.user_id_by_session_id.get(session_id)
        return None

    def current_user(self, request=None):
        """returns a User instance based on cookie value"""
        session_id = self.session_cookie(request)
        user_id = self.user_id_by_session_id(session_id)
        return User.get(user_id)

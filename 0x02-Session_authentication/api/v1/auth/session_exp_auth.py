#!/usr/bin/env python3
"""define a class for expiring sessions"""
from .session_auth import SessionAuth
from os import getenv
import datetime


class SessionExpAuth(SessionAuth):
    """class for expiring Auth sessions"""

    def __init__(self) -> None:
        super().__init__()
        try:
            self.session_duration = int(getenv('SESSION_DURATION'))
        except Exception:
            session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """create a new time bound session"""
        session_id = super().create_session(user_id)
        if not session_id:
            return None
        self.user_id_by_session_id[session_id] = {
            'user_id': user_id, 
            'created_at': datetime.now()}

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """returns user id of the session"""
        if not session_id:
            return None
        if session_id not in self.user_id_by_session_id:
            return None

        session_dict = self.user_id_by_session_id[session_id]

        if self.session_duration <= 0:
            return session_dict['user_id']

        if 'created_at' not in session_dict:
            return None

        time_passed = datetime.timedelta(seconds=self.session_duration)
        expiry_time = session_dict['created_at'] + time_passed
        if expiry_time < datetime.now():
            return None
        return session_dict['user_id'] 

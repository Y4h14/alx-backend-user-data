#!/usr/bin/env python3
"""handling routes for the Session authentication"""
from flask import jsonify, request
from api.v1.views import app_views
from os import getenv
from models.user import User


@app_views.route('/auth_session/login', methods=['Post'],
                 strict_slashes=False)
def session_login():
    """handle login"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error":
                        "no user found for this email"}), 404
    if len(users) <= 0:
        return jsonify({"error":
                        "no user found for this email"}), 404

    if users[0].is_valid_password(password):
        from api.v1.app import auth
        session_id = auth.create_session(getattr(users[0], 'id'))
        res = jsonify(users[0].to_json())
        res.set_cookie(getenv('SESSION_NAME'), session_id)
        return res
    return jsonify({"error": "wrong password"}), 401

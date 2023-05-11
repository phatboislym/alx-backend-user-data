#!/usr/bin/env python3

"""
module for Flask app
"""
from auth import Auth
from flask import Flask, jsonify, request, Response
from typing import Optional, Tuple
from user import User

AUTH = Auth()
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def test_route() -> Response:
    """
    args:   None
    return: payload: Response
    """
    payload: Response = jsonify({"message": "Bienvenue"})
    return payload


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> Tuple[Response, Optional[int]]:
    """
    end-point to register a user
    args:   None
    return: payload: Response
    """
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    try:
        user: User = AUTH.register_user(email=email, password=password)
        user_created: Response = jsonify(
            {"email": "<registered email>", "message": "user created"})
        return user_created
    except ValueError:
        user_exists: Response = jsonify(
            {"message": "email already registered"})
        return (user_exists, 400)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

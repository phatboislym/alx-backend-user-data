#!/usr/bin/env python3

"""
module for Flask app
"""
from auth import Auth
from flask import abort, Flask, jsonify, make_response, request, Response
from typing import Optional, Tuple, Union
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


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> Union[Response, int]:
    """"""
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    if AUTH.valid_login(email, password):
        session_id: Union[str, None] = AUTH.create_session(email=email)
        response: Response = make_response(
            jsonify({"email": email, "message": "logged in"}))
        response.set_cookie('session_id', session_id)
        return response
    else:
        abort(401)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

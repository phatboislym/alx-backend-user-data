#!/usr/bin/env python3

"""
module for Flask app
"""
from user import User
from typing import Optional, Tuple, Union
from auth import Auth, NoResultFound
from flask import (abort, Flask, jsonify, make_response,
                   redirect, request, Response, url_for)


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
    """
    end-point to log a user in
    args:   None
    return: response: Response | 401 abort status code
    """
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


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout() -> Union[Response, int]:
    """
    end-point to log a user out
    args:   None
    return: response: Response | 403 abort status code
    """
    session_id: Union[str, None] = request.form.get('session_id')
    user: User = AUTH.get_user_from_session_id(session_id)
    if not user or not session_id:
        abort(403)
    else:
        user.session_id = None
        AUTH.destroy_session(user.id)
        response: Response = make_response(redirect('/'))
        response.set_cookie('session_id', "", expires=0)
        return response


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    end-point to find user profile
    args:   None
    return: payload: Response
            200: int
    """
    session_id: Union[str, None] = request.form.get('session_id')
    try:
        user: User = AUTH.get_user_from_session_id(session_id)
        payload: Response = jsonify({"email": "<user email>"})
        return (payload, 200)
    except (NoResultFound, ValueError):
        pass


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)

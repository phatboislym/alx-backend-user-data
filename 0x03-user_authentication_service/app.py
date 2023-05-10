#!/usr/bin/env python3

"""
module for Flask app
"""
from flask import Flask, jsonify, Response

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def test_route() -> Response:
    """
    args:   None
    return: payload: Response
    """
    payload: Response = jsonify({"message": "Bienvenue"})
    return payload


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

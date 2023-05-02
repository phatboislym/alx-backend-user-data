# 0x01. Basic authentication

## Mandatory Tasks

- [0.  Simple-basic-API](api/v1/app.py)
- [1.  Error handler: Unauthorized](api/v1/views/index.py)
- [2.  Error handler: Forbidden](api/v1/views/index.py)
- [3.  Auth class](api/v1/auth)
  - [init](api/v1/auth/__init__.py)
  - [auth](api/v1/auth/auth.py)
- [4.  Define which routes don't need authentication](api/v1/auth/auth.py)
- [5.  Request validation!](api/v1/auth/auth.py)
- [6.  Basic auth](api/v1/auth/basic_auth.py)
- [7.  Basic - Base64 part](api/v1/auth/basic_auth.py)
- [8.  Basic - Base64 decode](api/v1/auth/basic_auth.py)
- [9.  Basic - User credentials](api/v1/auth/basic_auth.py)
- [10. Basic - User object](api/v1/auth/basic_auth.py)
- [11. Basic - Overload current_user - and BOOM!](api/v1/auth/basic_auth.py)

## Simple API

Simple HTTP API for playing with `User` model.

### Files

#### `models/`

- `base.py`: base of all models of the API - handle serialization to file
- `user.py`: user model

#### `api/v1`

- `app.py`: entry point of the API
- `views/index.py`: basic endpoints of the API: `/status` and `/stats`
- `views/users.py`: all users endpoints

### Setup

```bash
pip3 install -r requirements.txt
```

### Run

```bash
API_HOST=0.0.0.0 API_PORT=5000 python3 -m api.v1.app
```

### Routes

- `GET /api/v1/status`: returns the status of the API
- `GET /api/v1/stats`: returns some stats of the API
- `GET /api/v1/users`: returns the list of users
- `GET /api/v1/users/:id`: returns an user based on the ID
- `DELETE /api/v1/users/:id`: deletes an user based on the ID
- `POST /api/v1/users`: creates a new user (JSON parameters: `email`, `password`, `last_name` (optional) and `first_name` (optional))
- `PUT /api/v1/users/:id`: updates an user based on the ID (JSON parameters: `last_name` and `first_name`)

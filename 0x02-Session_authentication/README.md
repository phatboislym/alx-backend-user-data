# 0x02. Session authentication

## Mandatory Tasks

- [0. Et moi et moi et moi!](api/v1/app.py)
  - [views](api/v1/views/users.py)
- [1.  Error handler: Unauthorized](api/v1/auth/session_auth.py)
  - [app](api/v1/app.py)
- [2. Create a session](api/v1/auth/session_auth.py)
- [3. User ID for Session ID](api/v1/auth/session_auth.py)
- [4. Session cookie](api/v1/auth/auth.py)
- [5. Before request](api/v1/app.py)
- [6. Use Session ID for identifying a User](api/v1/auth/session_auth.py)
- [7. New view for Session Authentication](api/v1/views/session_auth.py)
  - [init](api/v1/views/__init__.py)
- [8. Logout](api/v1/auth/session_auth.py)
  - [views](api/v1/views/session_auth.py)

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

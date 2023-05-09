#!/usr/bin/env python3

"""
module for SQLAlchemy model `User` for a database table named `users`
"""

from bcrypt import gensalt, hashpw
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from typing import Optional

Base = declarative_base()


class User(Base):
    """
    class for SQLAlchemy model `User`
    attributes:
        id, primary key: Column[int]
        email, a non-nullable string: Column[str]
        hashed_password, a non-nullable string: Column[str]
        session_id, a nullable string: Column[str], optional
        reset_token, a nullable string: Column[str], optional
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

    def __init__(self, email: str, hashed_password: str,
                 session_id: Optional[str] = None,
                 reset_token: Optional[str] = None) -> None:
        self.email = email
        self.hashed_password = hashed_password
        self.session_id = session_id
        self.reset_token = reset_token

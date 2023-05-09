#!/usr/bin/env python3

"""
DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.exc import InvalidRequestError, NoResultFound
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from user import Base, User


class DB:
    """
    DB class
    """

    def __init__(self) -> None:
        """
        initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db")
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """
        memoized session object
        args:   self
        return: self.__session: Session
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        adds a user to the database
        args:   self
                email: str
                hashed_password: str
        return: user: User
        """
        user = User(email=email, hashed_password=hashed_password)
        self._session.add(user)
        self._session.commit()
        return user

    def find_user_by(self, **kwargs) -> User:
        """
        finds the first user in the database that matches the given criteria
        args:   self
                **kwargs: arbitrary keyword arguments for filtering the query
        return: user: User
        """
        try:
            users = self._session.query(User)
            user: User = users.filter_by(**kwargs).one()
        except NoResultFound:
            raise
        except InvalidRequestError as e:
            raise InvalidRequestError(str(e))
        return user

import sqlalchemy as sq
from sqlalchemy import orm
from sqlalchemy.ext.mutable import MutableDict


class Base(orm.DeclarativeBase): pass

class User(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True, index=True)
    fullname = sq.Column(sq.String)
    username = sq.Column(sq.String)


class Game(Base):
    __tablename__ = 'games'

    id = sq.Column(sq.Integer, primary_key=True, autoincrement=True, index=True)
    chat_id = sq.Column(sq.Integer, index=True)
    players = sq.Column(MutableDict.as_mutable(sq.JSON))
    voting = sq.Column(MutableDict.as_mutable(sq.JSON))
    status = sq.Column(sq.BOOLEAN, default=True)
    word = sq.Column(sq.CHAR)

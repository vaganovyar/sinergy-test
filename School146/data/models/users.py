from flask_login import UserMixin
from sqlalchemy import Integer, Column, String
from sqlalchemy_serializer import SerializerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.ext.sqlalchemy import orm

from School146.data.db_session import SqlAlchemyBase


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String)
    name = Column(String)
    email = Column(String, index=True, unique=True)
    hashed_password = Column(String)
    theme = Column(String)

    timetable = orm.relation('Timetable', back_populates='user')

    homework = orm.relation('Homework', back_populates='user')


    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
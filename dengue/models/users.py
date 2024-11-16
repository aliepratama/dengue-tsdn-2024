from dengue.app import db
from sqlalchemy import Column, Integer, String, DateTime, Enum
import datetime


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'


class Place(Enum):
    Urban = 'Urban'
    Village = 'Village'


class Users(db.Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    full_name = Column(String(50), nullable=True)
    age = Column(Integer, nullable=True)
    gender = Column(Enum(Gender), nullable=True)
    address = Column(String(100), nullable=True)
    place = Column(Enum(Place), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<User {self.full_name}>'

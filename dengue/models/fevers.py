from dengue.app import db
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float
import datetime


class Fevers(db.Base):
    __tablename__ = 'fevers'

    id = Column(Integer, primary_key=True)
    dengue_days = Column(Integer, nullable=True)
    fever_temp = Column(Float, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<Fevers %r>' % self.id

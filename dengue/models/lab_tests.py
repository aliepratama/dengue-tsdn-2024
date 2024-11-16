from dengue.app import db
from sqlalchemy import Column, Integer, DateTime, ForeignKey, Float
import datetime


class LabTests(db.Base):
    __tablename__ = 'lab_tests'

    id = Column(Integer, primary_key=True)
    wbc = Column(Float, nullable=True)
    hemoglobin = Column(Float, nullable=True)
    platelets = Column(Integer, nullable=True)
    hematocrit = Column(Integer, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return '<LabTests %r>' % self.id

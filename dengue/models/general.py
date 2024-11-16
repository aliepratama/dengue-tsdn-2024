from dengue.app import db
from sqlalchemy import Column, Integer, Boolean, DateTime, ForeignKey
import datetime


class Generals(db.Base):
    __tablename__ = 'generals'

    id = Column(Integer, primary_key=True, autoincrement=True)
    severe_headche = Column(Boolean, nullable=True)
    pain_behind_the_eyes = Column(Boolean, nullable=True)
    joint_muscle_aches = Column(Boolean, nullable=True)
    metallic_taste_in_the_mouth = Column(Boolean, nullable=True)
    appetite_loss = Column(Boolean, nullable=True)
    addominal_pain = Column(Boolean, nullable=True)
    nausea_vomiting = Column(Boolean, nullable=True)
    diarrhoea = Column(Boolean, nullable=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return f'<General {self.id}>'

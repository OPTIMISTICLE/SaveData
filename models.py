import datetime

from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Data(Base):
    __tablename__ = 'donnees'
    id = Column(Integer, primary_key=True)
    valeur = Column(String(255), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False)
    heure = Column(DateTime(timezone=True), nullable=False)
    def __init__(self,  valeur, date=datetime.datetime.now(), heure=datetime.datetime.now()):
        self.valeur = valeur
        self.date = date
        self.heure = heure

    def __repr__(self):
        return '<Data %r>' % self.valeur


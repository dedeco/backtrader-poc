

from database import Base
from sqlalchemy import Column, Integer, String, Float, DateTime

class Marketdata(Base):
    __tablename__ = 'marketprices'

    id = Column(Integer(), primary_key = True,  autoincrement=True)
    quote = Column(String(6), nullable=False)
    date = Column(DateTime, nullable=False)
    price_first = Column(Float())
    price_max = Column(Float())
    price_min = Column(Float())
    price_last = Column(Float())
    volume = Column(Integer(), unique=True)

from sqlalchemy import Column, Date, Integer

from base import Base


class Dates1(Base):
    __tablename__ = 'dates1'

    id = Column(Integer, primary_key=True)
    dates1 = Column(Date)

    def __init__(self, dates1):
        self.dates1 = dates1


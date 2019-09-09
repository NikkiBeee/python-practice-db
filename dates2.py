from sqlalchemy import Column, Date, Integer

from base import Base


class Dates2(Base):
    __tablename__ = 'dates2'

    id = Column(Integer, primary_key=True)
    dates2 = Column(Date)

    def __init__(self, dates2):
        self.dates2 = dates2
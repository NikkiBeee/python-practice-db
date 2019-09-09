# coding=utf-8

# 1 - imports
from datetime import date

from base import Session, engine, Base
from dates1 import Dates1
from dates2 import Dates2


Base.metadata.create_all(engine)

session = Session()

date_first = Dates1(date(2002, 10, 11))
date_second = Dates1(date(2002, 10, 12))
date_third = Dates1(date(2002, 10, 13))
date_fourth = Dates1(date(2002, 10, 14))

session.add(date_first)
session.add(date_second)
session.add(date_third)
session.add(date_fourth)

date_first2 = Dates2(date(2002, 10, 11))
date_second2 = Dates2(date(2002, 10, 12))
date_third2 = Dates2(date(2002, 10, 13))
date_fourth2 = Dates2(date(2002, 10, 14))

session.add(date_first2)
session.add(date_second2)
session.add(date_third2)
session.add(date_fourth2)


# 10 - commit and close session
session.commit()
session.close()

from datetime import date, timedelta

from base import Session
from dates1 import Dates1
from dates2 import Dates2


session = Session()


dates_1 = session.query(Dates1).all()
dates_2 = session.query(Dates2).all()

days1 = []
days2 = []


for day in dates_1:
    days1.append(day.dates1)

    

for day in dates_2:
    days2.append(day.dates2)


def f_calc(list1, list2):
    print(list1)
    total = timedelta()

    for i, j in zip(list1, list2):

        dif = abs(i - j)
        total += dif

    
    print(total)
    return total

f_calc(days1,days2)


from datetime import datetime, date
import pytest

from func_calc import f_calc

@pytest.fixture()
def same_dates1():
    dates = [datetime.date(2002, 10, 11), datetime.date(2002, 10, 12), datetime.date(2002, 10, 13), datetime.date(2002, 10, 14)]
    return dates


@pytest.fixture()
def same_dates2():
    dates = [datetime.date(2002, 10, 11), datetime.date(2002, 10, 12), datetime.date(2002, 10, 13), datetime.date(2002, 10, 14)]
    return dates


def test_f_calc(same_dates1,same_dates2):
    assert f_calc(same_dates1,same_dates2) == 0
    
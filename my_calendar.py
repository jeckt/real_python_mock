#!/usr/bin/env python

import datetime
from unittest.mock import Mock

# Save a couple of test days
tuesday = datetime.datetime(2019, 1, 1)
saturday = datetime.datetime(2019, 1, 5)

def is_weekday():
    today = datetime.datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

# Test if today is a weekday
# NOTE(steve): problem with this test is that
# depending on the day of the week it currently
# is when you run the test it will either pass
# or fail. We would like to freeze the dates
# that the function uses when testing it
# so that when it is a weekday it returns True
# and when it is a weekend it return False
assert is_weekday()

# Mock datetime to control today's date
datetime = Mock()

# Mock .today() to return Tuesday
datetime.datetime.today.return_value = tuesday
# Test Tuesday is a weekday
assert is_weekday()
# Mock .today() to return Saturday
datetime.datetime.today.return_value = saturday
# Test Tuesday is a weekday
assert not is_weekday()

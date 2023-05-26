"""
Friday 13th or Black Friday is considered as unlucky day. Calculate how many unlucky days are in the given year.

Find the number of Friday 13th in the given year.

Input: Year as an integer.

Output: Number of Black Fridays in the year as an integer.

Precondition: 1000 < |year| < 3000
"""

from calendar import weekday, FRIDAY


def checkio(year):
    """
    calendar.weekday(year, month, day)
        Returns the day of the week
    """
    return sum(1 for i in range(1, 13) if weekday(year, i, 13) == FRIDAY)  # BETTER :)

    # This was my first iteration
    # c = 0
    # for i in range(1, 13):
    #     if weekday(year, i, 13) == FRIDAY:
    #         c += 1
    # return c


if __name__ == "__main__":
    assert checkio(2015) == 3, "First - 2015"
    assert checkio(1986) == 1, "Second - 1986"
    assert checkio(2689) == 2, "Third - 2689"
    assert checkio(2688) == 3, "Third - 2688"


from time import strptime


def checkio1(year):
    fridays = 0

    for month in range(1, 13):
        date = strptime("{:04}-{:02}-13".format(year, month), "%Y-%m-%d")
        if date.tm_wday == 4:
            fridays += 1

    return fridays


from calendar import day_name
import calendar


def checkio2(year):
    counter = 0
    for i in range(1, 13):
        if day_name[calendar.weekday(year, i, 13)] == "Friday":
            counter += 1
    return counter


from datetime import datetime


def checkio(year):
    count = 0
    for month in range(1, 13):
        date = datetime(year, month, 13)
        if date.weekday() == 4:
            count += 1
    return count

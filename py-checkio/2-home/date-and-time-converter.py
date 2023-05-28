"""
Computer date and time format consists only of numbers, for example: 21.05.2018 16:30.
Humans prefer to see something like this: 21 May 2018 year, 16 hours 30 minutes.
Your task is simple - convert the input date and time from computer format into a "human" format.

Input: Date and time as a string

Output: The same date and time, but in a more readable format as a string

How it is used: To improve the understanding between computers and humans.

Precondition :
0 < day <= 31
0 < month <= 12
1900 < year <= 3000
0 <= hours < 24
0 <= minutes < 60
"""
import calendar


def date_time(time: str) -> str:
    date, time = time.split(" ")
    day, month, year = date.split(".")
    hours, minutes = time.split(":")
    m = "s" if int(minutes) != 1 else ""
    h = "s" if int(hours) != 1 else ""
    return (
        f"{int(day)} {calendar.month_name[int(month)]} {year} year"
        f" {int(hours)} hour{h} {int(minutes)} minute{m}"
    )


print("Example:")
print(date_time("01.01.2000 00:00"))

assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes"
assert date_time("09.05.1945 06:07") == "9 May 1945 year 6 hours 7 minutes"
assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes"
assert date_time("09.07.1995 16:01") == "9 July 1995 year 16 hours 1 minute"
assert date_time("11.04.1812 01:01") == "11 April 1812 year 1 hour 1 minute"

print("The mission is done! Click 'Check Solution' to earn rewards!")

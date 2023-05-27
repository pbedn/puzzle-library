"""
You prefer a good old 12-hour time format. But the modern world we live in would rather use the 24-hour format and you see it everywhere. Your task is to convert the time from the 24-h format into 12-h format by following the next rules:
- the output format should be 'hh:mm a.m.' (for hours before midday) or 'hh:mm p.m.' (for hours after midday)
- if hours is less than 10 - don't write a '0' before it. For example: '9:05 a.m.'
Here you can find some useful information about the 12-hour format.

example

Input: Time in a 24-hour format (as a string).

Output: Time in a 12-hour format (as a string).

Precondition:
'00:00' <= time <= '23:59'
"""


def time_converter(time):
    #  replace this for solution
    if time == "24:00":
        time = "00:00"
    hour, minute = time.split(":")
    if hour[0] == "0":
        hour = hour[1:]
    text = "p" if int(hour) >= 12 else "a"
    hour = hour if 0 < int(hour) <= 12 else str(abs(int(hour) - 12))
    return "{}:{} {}.m.".format(hour, minute, text)


def time_converter2(time):
    time = time.replace("24:00", "00:00")
    h, m = map(int, time.split(":"))
    print("time", time, "result", f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m.")
    return f"{(h-1)%12+1}:{m:02d} {'ap'[h>11]}.m."


if __name__ == "__main__":
    # print("Example:")
    # print(time_converter('12:30'))

    #  These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter("12:30") == "12:30 p.m."
    assert time_converter("09:00") == "9:00 a.m."
    assert time_converter("23:15") == "11:15 p.m."
    assert time_converter("00:00") == "12:00 a.m."
    assert time_converter("00:01") == "12:01 a.m."
    assert time_converter("01:00") == "1:00 a.m."
    assert time_converter("01:01") == "1:01 a.m."
    assert time_converter("11:59") == "11:59 a.m."
    assert time_converter("12:00") == "12:00 p.m."
    assert time_converter("12:01") == "12:01 p.m."
    assert time_converter("13:00") == "1:00 p.m."
    assert time_converter("24:00") == "12:00 a.m."
    print("Coding complete? Click 'Check' to earn cool rewards!")

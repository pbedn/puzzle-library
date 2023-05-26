"""
Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from the nature around him. Programming won't help you with the fire and water, but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day. Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees. At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees. 6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM), your function should return - "I don't see the sun!".

Input: The time of the day.

Output: The angle of the sun, rounded to 2 decimal places.

Precondition:
00:00 <= time <= 23:59
"""


def sun_angle(time):
    hour, minute = int(time.split(":")[0]) - 6, int(time.split(":")[1])
    print("hour, minute", hour, minute)
    minutes = hour * 60 + minute
    print("minutes", minutes)
    if not 0 <= minutes <= 720:
        return "I don't see the sun!"
    print("angle", minutes * 0.25)
    return minutes * 0.25


def sun_angle(time):
    hour, minute = map(int, time.split(":"))
    # hour - 6 hours to star counting from zero
    minutes = (hour - 6) * 60 + minute
    if not 0 <= minutes <= 720:
        return "I don't see the sun!"
    # if 6 hours is 90 degrees: 6h = 90'
    # then 1 minute is 0.25 degree: 1m = x
    # x = (90' * 1m) / 60m = 0.25'
    return minutes * 0.25


if __name__ == "__main__":
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("5:59") == "I don't see the sun!"
    assert sun_angle("6:00") == 0
    assert sun_angle("6:01") == 0.25
    assert sun_angle("07:00") == 15
    assert sun_angle("12:00") == 90
    assert sun_angle("17:59") == 179.75
    assert sun_angle("18:00") == 180
    assert sun_angle("18:01") == "I don't see the sun!"
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")

#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""03.05.2015 - First Version"""


# 06.10.2016
# czytam ponownie..
# zaimplementowalem wlasna funkcję reurencyjną -> sum
# fajnie ale po co ;)
def checkio(array):
    """
    sums even-indexes elements and multiply at the last
    """
    if array == []:
        return 0

    def sum(array):
        if array == []:
            return 0
        else:
            return array[0] + sum(array[2:])

    return sum(array) * array[-1]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([1, 3]) == 3, "1*5=5"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"


# CLEAR
if len(array) == 0:
    return 0
return sum(array[0::2]) * array[-1]

# CLEAR?
checkio = lambda x: sum(x[::2]) * x[-1] if x else 0

# CREATIVE
checkio = lambda array: sum(array[::2]) * sum(array[-1:])


# SPEEDY
return array and sum(array[::2]) * array[-1] or 0

return sum(array[::2]) * array[-1] if array else 0

return sum(array[0::2]) * array[-1] if 0 < len(array) else 0

"""
You are given a list of integers. You should find the sum of the elements with even indexes (0th, 2nd, 4th...).
Then multiply this summed number and the final element of the list together. Don't forget that the first element has an index of 0.
For an empty list, the result will always be 0 (zero).

Input: List of integers.

Output: The number as an integer.

Examples:
assert checkio([0, 1, 2, 3, 4, 5]) == 30
assert checkio([1, 3, 5]) == 30
assert checkio([6]) == 36
assert checkio([]) == 0

How it is used: Indexes and slices are important elements of coding. This will come in handy down the road!

Preconditions: 0 ≤ len(array) ≤ 20
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""


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


# Clear
def checkio(array):
    """
    sums even-indexes elements and multiply at the last
    """
    if len(array) == 0:
        return 0
    return sum(array[0::2]) * array[-1]


# Creative
checkio = lambda array: sum(array[::2]) * sum(array[-1:])


# Speedy
def checkio(array):
    """
    sums even-indexes elements and multiply at the last
    """
    return sum(array[0::2]) * array[-1] if 0 < len(array) else 0


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert checkio([1, 3, 5]) == 30, "(1+5)*5=30"
    assert checkio([6]) == 36, "(6)*6=36"
    assert checkio([]) == 0, "An empty array = 0"

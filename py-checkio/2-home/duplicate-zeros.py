"""
You are given a list of integers. Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...)
all zeros (think about donuts ;-P)
and return the result as any Iterable. Let's look on the example:

[1, 0, 2, 0] -> [1, 0, 0, 2, 0, 0]

Input: A list of integers.

Output: A list on another Iterable (tuple, generator, iterator) of integers.

Examples:
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
    1,
    0,
    0,
    2,
    3,
    0,
    0,
    4,
    5,
    0,
    0,
]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]
"""
from collections.abc import Iterable

# First version
def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    l = list()
    for d in donuts:
        l.append(d)
        if not d:
            l.append(d)
    return l

# Generator version
def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
    for d in donuts:
        yield d
        if not d:
            yield d

print("Example:")
print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))

# These "asserts" are used for self-checking
assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [1, 0, 0, 2, 3, 0, 0, 4, 5, 0, 0]
assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]

print("The mission is done! Click 'Check Solution' to earn rewards!")

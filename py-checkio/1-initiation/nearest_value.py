"""
 Find the nearest value to the given one.

You are given a set of integers and a value for which you need to find the nearest one.

For example, we have the following sequence of numbers: 4, 7, 10, 11, 12, 17, and we need to find the nearest value to the number 9. If we sort this sequence in the ascending order, then to the left of number 9 will be number 7 and to the right - will be number 10. But 10 is closer than 7, which means that the correct answer is 10.

A few clarifications:

    If 2 numbers are at the same distance, you need to choose the smallest one;
    The sequence of numbers is always non-empty;
    The given value can be in this sequence, which means that it’s the answer;
    The sequence may contain both positive and negative numbers, but they are always integers;
    The sequence isn’t sorted and consists only unique numbers.

Input: Two arguments. A set of integers. The sought value as an integer.

Output: An integer.
"""
def nearest_value(values: set[int], one: int) -> int:
    values = sorted(values)
    for i, v in enumerate(values):
        if v >= one:
            prev = abs(values[i-1] - one)
            after = abs(values[i] - one)
            return values[i] if after < prev else values[i-1]
    return values[-1]


print("Example:")
print(nearest_value({4, 7, 10, 11, 12, 17}, 9))

assert nearest_value({17, 4, 7, 10, 11, 12}, 9) == 10
assert nearest_value({17, 4, 7, 10, 11, 12}, 8) == 7
assert nearest_value({17, 4, 8, 10, 11, 12}, 9) == 8
assert nearest_value({17, 4, 9, 10, 11, 12}, 9) == 9
assert nearest_value({17, 4, 7, 10, 11, 12}, 0) == 4
assert nearest_value({17, 4, 7, 10, 11, 12}, 100) == 17
assert nearest_value({100, 5, 8, 89, 10, 12}, 7) == 8
assert nearest_value({2, 3, -1}, 0) == -1
assert nearest_value({5}, 5) == 5
assert nearest_value({5}, 7) == 5

print("The mission is done! Click 'Check Solution' to earn rewards!")

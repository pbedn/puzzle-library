"""
 You are given a list of integers. Your task in this mission is to find,
 how many times the sorting direction was changed in the given list.
 If the elements are equal - the previous sorting direction remains the same,
 if the sequence starts from the same elements - look for the next different to determine the sorting direction.

 There are three sorting directions:

    on the chunk 1, 2, 2 - up (increasing);
    on the chunk 2, 1 - down (decreasing);
    and on the chunk 1, 2, 2 - up again.

So, you have two points of changing the sorting direction: #1 - from up to down,
and #2 - from down to up. That's the result your function should return.

Input: A list of integers.

Output: Integer.

Preconditions:
    the list is non-empty;
    the elements are positive integers.
"""


def changing_direction(elements: list[int]) -> int:
    change = 0
    direction = None
    first = elements[0]
    for i, second in enumerate(elements[1:]):
        if first == second:
            continue
        elif first < second:
            if direction == 1:
                change += 1
            direction = 0
        else:
            if direction == 0:
                change += 1
            direction = 1
        first = second
    return change


print("Example:")
print(changing_direction([1, 2, 3, 4, 5]))

# These "asserts" are used for self-checking
assert changing_direction([1, 2, 3, 4, 5]) == 0
assert changing_direction([1, 2, 3, 2, 1]) == 1
assert changing_direction([1, 2, 2, 1, 2, 2]) == 2
assert changing_direction([1, 2, 2, 1, 2, 1, 2]) == 4
assert changing_direction([1, 2, 3, 5, 4, 2, 5, 7, 8, 3, 2, 1]) == 3
assert changing_direction([0]) == 0
assert changing_direction([6, 6, 6, 4, 1, 2, 5, 9, 7, 8, 5, 9, 4, 2, 6]) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")

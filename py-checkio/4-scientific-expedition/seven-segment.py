"""
You have a device that uses a Seven-segment display to display 2 digit numbers. However, some of the segments aren't working and can't be displayed.

You will be given information on the lit and broken segments. You won't know whether the broken segment is lit or not. You have to count and return the total number that the device may be displaying.

The input is a set of lit segments (the first argument) and broken segments (the second argument).

Uppercase letters represent the segments of the first out two digit number.
Lowercase letters represent the segments of the second out two digit number.
topmost: 'A(a)', top right: 'B(b)', bottom right: 'C(c)', bottommost: 'D(d)', bottom left: 'E(e)', top left: 'F(f)', middle: 'G(g)'
example

example

Input: Two arguments. The first one contains the lit segments as a set of letters representing segments. The second one contains the broken segments as a set of letters representing segments.

Output: The total number that the device may be displaying.

Precondition:
all(re.match('[A-Ga-g]', s) for s in lit | broken)
len(lit & broken) == 0
"""

from string import ascii_lowercase

DIGIT_CODE = {
    "abcdef": 0,
    "bc": 1,
    "abdeg": 2,
    "abcdg": 3,
    "bcfg": 4,
    "acdfg": 5,
    "acdefg": 6,
    "abc": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def create_possible_digits(number_lit, number_total):
    tmp = []
    for code, digit in DIGIT_CODE.items():
        # if set.issubset(set(code), number_total):
        if set(code).issubset(set(number_total)):
            if number_lit.issubset(set(code)):
                tmp.append(digit)
    return tmp


def seven_segment(lit_seg, broken_seg):
    left_seg_lit = set(l.lower() for l in lit_seg if l not in ascii_lowercase)
    right_seg_lit = set(l for l in lit_seg if l in ascii_lowercase)

    segments = lit_seg.union(broken_seg)
    # segments = set.union(lit_seg, broken_seg)
    left_seg = set(l.lower() for l in segments if l not in ascii_lowercase)
    right_seg = set(l for l in segments if l in ascii_lowercase)

    possible_left_digit = create_possible_digits(left_seg_lit, left_seg)
    possible_right_digits = create_possible_digits(right_seg_lit, right_seg)

    possible_combinations = set()
    for l in possible_left_digit:
        for r in possible_right_digits:
            possible_combinations.add("{}{}".format(l, r))

    # print(len(possible_left_digit)*len(possible_right_digits))
    return len(possible_combinations)


if __name__ == "__main__":
    assert (
        seven_segment({"g", "b", "G", "B"}, {"a", "c", "d", "A", "C", "D"}) == 1
    ), "33"
    assert seven_segment({"B", "C", "b", "c"}, {"A"}) == 2, "11, 71"
    assert (
        seven_segment({"B", "C", "a", "f", "g", "c", "d"}, {"A", "G", "D", "e"}) == 6
    ), "15, 16, 35, 36, 75, 76"
    assert (
        seven_segment(
            {"B", "C", "a", "f", "g", "c", "d"}, {"A", "G", "D", "F", "b", "e"}
        )
        == 20
    ), "15...98"
    print('"Run" is good. How is "Check"?')


# ----------------------------------------------

NUMBERS = [
    "abcdef",
    "bc",
    "abdeg",
    "abcdg",
    "bcfg",
    "acdfg",
    "acdefg",
    "abc",
    "abcdefg",
    "abcdfg",
]


def seven_segment2(lit_seg, broken_seg):
    first, second = 0, 0
    for i in range(10):
        # First number(big letters).
        if all(symb.upper() in lit_seg | broken_seg for symb in NUMBERS[i]) and all(
            letter.lower() in NUMBERS[i] for letter in lit_seg if letter.isupper()
        ):
            first += 1
        # Second number(small letters).
        if all(symb in lit_seg | broken_seg for symb in NUMBERS[i]) and all(
            letter in NUMBERS[i] for letter in lit_seg if letter.islower()
        ):
            second += 1
    return first * second


# -----------------------------------------------

TENS = (
    "BC",
    "ABGED",
    "ABCDG",
    "FGBC",
    "AFGCD",
    "AFGECD",
    "ABC",
    "ABCDEFG",
    "ABFGCD",
    "ABCDEF",
)
UNITS = tuple(map(str.lower, TENS))


def seven_segment3(working, broken):
    def segment(obj):
        return set(filter(str.isupper, obj)), set(filter(str.islower, obj))

    tens, units = segment(working)
    first, second = segment(set.union(working, broken))

    len1 = len(
        list(filter(lambda x: set(x).issubset(first) and tens.issubset(set(x)), TENS))
    )
    len2 = len(
        list(
            filter(lambda x: set(x).issubset(second) and units.issubset(set(x)), UNITS)
        )
    )
    return len1 * len2


# -----------------------------------------------

import string

numbers = {
    0: ("a", "b", "c", "d", "e", "f"),
    1: ("b", "c"),
    2: ("a", "b", "d", "e", "g"),
    3: ("a", "b", "c", "d", "g"),
    4: ("b", "c", "f", "g"),
    5: ("a", "c", "d", "f", "g"),
    6: ("a", "c", "d", "e", "f", "g"),
    7: ("a", "b", "c"),
    8: ("a", "b", "c", "d", "e", "f", "g"),
    9: ("a", "b", "c", "d", "f", "g"),
}


def possible_numbers(lit_seq, broken_seq):
    count = 0

    for k, number_set in numbers.items():
        if lit_seq.issubset(set(number_set)):
            if set(number_set).issubset(set(lit_seq | broken_seq)):
                count += 1
    return count


def seven_segment4(lit_seg, broken_seg):
    lit_seg_upper = set(
        map(str.lower, filter(lambda c: c in string.ascii_uppercase, lit_seg))
    )
    lit_seg_lower = set(filter(lambda c: c in string.ascii_lowercase, lit_seg))

    broken_seg_upper = set(
        map(str.lower, filter(lambda c: c in string.ascii_uppercase, broken_seg))
    )
    broken_seg_lower = set(filter(lambda c: c in string.ascii_lowercase, broken_seg))

    possible_upper = possible_numbers(lit_seg_upper, broken_seg_upper)
    possible_lower = possible_numbers(lit_seg_lower, broken_seg_lower)

    return possible_upper * possible_lower


# -------------------------------------------------------------------------------

import itertools


def seven_segment5(lit_seg, broken_seg):
    digits = (
        "bc",
        "abdeg",
        "abcdg",
        "bcfg",
        "acdfg",
        "acdefg",
        "abc",
        "abcdefg",
        "abcdfg",
        "abcdef",
    )

    s0 = lit_seg & set("ABCDEFG")
    s1 = lit_seg & set("abcdefg")

    s0_count = s1_count = 0
    for digit in digits:
        if set(digit.upper()) - broken_seg == s0:
            s0_count += 1
        if set(digit) - broken_seg == s1:
            s1_count += 1

    return s0_count * s1_count


assert seven_segment5({"g", "b", "G", "B"}, {"a", "c", "d", "A", "C", "D"}) == 1, "33"
assert seven_segment5({"B", "C", "b", "c"}, {"A"}) == 2, "11, 71"
assert (
    seven_segment5({"B", "C", "a", "f", "g", "c", "d"}, {"A", "G", "D", "e"}) == 6
), "15, 16, 35, 36, 75, 76"
assert (
    seven_segment5({"B", "C", "a", "f", "g", "c", "d"}, {"A", "G", "D", "F", "b", "e"})
    == 20
), "15...98"
print('"Run" is good. How is "Check"?')
# --------------------------------------------------------------------------------

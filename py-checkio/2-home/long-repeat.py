def long_repeat(line):
    """
    length the longest substring that consists of the same char
    """
    if not line:
        return 0
    last = line[0]
    s = []
    ss = ""
    for l in line:
        if l != last:
            s.append([ss])
            ss = ""
            last = l
        ss += l
    # print(max([len(w[0]) for w in s]))
    if not s:
        return len(line)
    return max([len(w[0]) for w in s])


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat("") == 0
    assert long_repeat("sdsffffse") == 4, "First"
    assert long_repeat("ddvvrwwwrggg") == 3, "Second"
    assert long_repeat("aa") == 2
    print('"Run" is good. How is "Check"?')


"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).

This mission is the first one of the series. Here you should find the length of the longest substring that consists of the same letter. For example, line "aaabbcaaaa" contains four substrings with the same letters "aaa", "bb","c" and "aaaa". The last substring is the longest one which makes it an answer.

Input: String.

Output: Int.

Example:

long_repeat('sdsffffse') == 4
long_repeat('ddvvrwwwrggg') == 3
"""


# RANDOM
def long_repeat(line):
    """
    length the longest substring that consists of the same char
    """
    largest = 0
    ant_c = None
    actual_size = 0

    for c in line:
        if c == ant_c:
            actual_size += 1
            largest = max(actual_size, largest)
        else:
            actual_size = 1
            largest = max(actual_size, largest)
        ant_c = c

    return largest


# CLEAR ?
from itertools import groupby


def long_repeat(data):
    return max(list(map(lambda s: len(list(s[1])), groupby(data))) + [0])


from itertools import groupby


def long_repeat(line):
    return max((sum(1 for _ in g) for k, g in groupby(line)), default=0)

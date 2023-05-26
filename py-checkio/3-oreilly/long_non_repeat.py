def find_subs(line):
    subs = ""
    for letter in line:
        if letter not in subs:
            subs += letter
            continue
        else:
            break
    return subs


def non_repeat(line):
    """
    the longest substring without repeating chars
    """
    if set(line) == line:
        return line
    longest = ""
    for i in range(len(line)):
        subs = find_subs(line[i:])
        if len(subs) > len(longest):
            longest = subs
    return longest


# These "asserts" using only for self-checking and not necessary for auto-testing
assert non_repeat("aaaaa") == "a", "First"
assert non_repeat("abdjwawk") == "abdjw", "Second"
assert non_repeat("abcabcffab") == "abcf", "Third"
print('"Run" is good. How is "Check"?')

# assert non_repeat('') == '', "Empty"
# assert non_repeat('a') == 'a', "One letter"
# assert non_repeat('ab') == 'ab', "Two letters"
# assert non_repeat('qw') == 'qw', "Two letters reversed"
# assert non_repeat('wq') == 'wq', "Two letters reversed"

# From https://github.com/oduvan/checkio-mission-long-non-repeat/blob/master/verification/tests.py
EXTRA = [
    {"input": "ccccc", "answer": "c"},
    {"input": "afafafaf", "answer": "af"},
    {"input": "abcabcfabcabc", "answer": "abcf"},
    {"input": "", "answer": ""},
    {"input": "w", "answer": "w"},
    {"input": "wq", "answer": "wq"},
    {"input": "dfghj", "answer": "dfghj"},
    {"input": "fghfhy", "answer": "fgh"},
    {"input": "fghfrtyfgh", "answer": "ghfrty"},
    {"input": "abcbde", "answer": "cbde"},
]

for test in EXTRA:
    try:
        assert non_repeat(test["input"]) == test["answer"]
    except AssertionError:
        print("TEST FAILED:", test)
        print("My output", non_repeat(test["input"]))

"""
There are four substring missions that were born all in one day and you shouldn’t be needed more than one day to solve them. All of those mission can be simply solved by brute force, but is it always the best way to go? (you might not have access to all of those missions yet, but they are going to be available with more opened islands on the map).

A very similar to the first is the second mission of the series with only one distinction is that you should look in a completely different way. You need to find the first longest substring with all unique letters. For example, in substring "abca" we have two substrings with unique letters "abc" and "bca", but we should take the first one, so the answer is "abc".

Input: String.

Output: String.

Example:

non_repeat('aaaaa') == 'a'
non_repeat('abdjwawk') == 'abdjw'
non_repeat('abcabcffab') == 'abcf'
"""

# CLEAR
# 4 tasks and one solution


# The common boring part
def longest_substring(string, predicate):
    n = len(string)
    for length in range(n, -1, -1):
        for start in range(n - length + 1):
            substring = string[start : start + length]
            if predicate(substring):
                return substring


def repeat_inside(line):
    return longest_substring(line, lambda s: s in (s + s)[1:-1])


def non_repeat(line):
    return longest_substring(line, lambda s: len(s) == len(set(s)))


def long_repeat(line):
    return len(longest_substring(line, lambda s: len(set(s)) < 2))


def double_substring(line):
    return len(longest_substring(line, lambda s: line.count(s) > 1 or not s))


########################
# CLEAR
def non_repeat(line):
    """
    the longest substring without repeating chars
    """
    snake = ""
    longest_snake = ""
    for c in line:
        if c in snake:
            snake = snake[snake.find(c) + 1 :] + c
        else:
            snake += c
            if len(snake) > len(longest_snake):
                longest_snake = snake

    return longest_snake


########################
def non_repeat(line):
    """
    the longest substring without repeating chars
    """
    max_string = ""
    working_string = ""

    for i in range(len(line)):
        if line[i] not in working_string:
            working_string += line[i]
        else:
            char_idx = working_string.index(line[i])
            working_string = working_string[char_idx + 1 :] + line[i]

        if len(working_string) > len(max_string):
            max_string = working_string[:]

    return max_string


########################
# Simple recursion
def non_repeat(line):
    return (
        line
        if len(line) == len(set(line))
        else max(non_repeat(line[:-1]), non_repeat(line[1:]), key=len)
    )


########################
# KMP Inverted
def intervals(line):
    last = {}
    start = end = 0
    for i, letter in enumerate(line):
        end += 1
        if letter in last and start <= last[letter]:
            start = last[letter] + 1
        yield line[start:end]
        last[letter] = i


def non_repeat(line):
    return max(intervals(line), key=len, default="")

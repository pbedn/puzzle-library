"""
 Split the string into pairs of two characters. If the string contains an odd number of characters, then the missing second character of the final pair should be replaced with an underscore ('_').

Input: A string.

Output: A list or another Iterable of strings.

Example:
assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]

Precondition: 0 <= len(text) <= 100
"""
from typing import Iterable

def split_pairs(text: str) -> Iterable[str]:
    if len(text) % 2 != 0:
        text += "_"
    lst = list()
    for i in range(1, len(text)+1):
        if i % 2 == 0:
            lst.append(text[i-2: i])
    return lst


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")

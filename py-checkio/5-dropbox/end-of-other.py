"""
For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello", so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Precondition: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)
"""


def checkio(words_set):
    for word in words_set:
        tmp = words_set.copy()
        tmp.remove(word)
        if any(map(lambda w: word.endswith(w), tmp)):
            return True
    return False


if __name__ == "__main__":
    # assert checkio({"hello", "lo", "he"}) is True, "helLO"
    assert checkio({"hello", "la", "hellow", "cow"}) is False, "hellow la cow"
    assert checkio({"walk", "duckwalk"}) is True, "duck to walk"
    assert checkio({"one"}) is False, "Only One"
    assert checkio({"helicopter", "li", "he"}) is False, "Only end"
    assert checkio({"longest", "aa", "a"}) is True, "Longest"

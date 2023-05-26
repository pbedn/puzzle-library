"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.
"""

from collections import Counter


def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    c = Counter(data)
    previous = 0
    for k, v in c.items():
        print(k, v)
        if v > previous:
            most_frequent = k
        previous = v
    return most_frequent


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")

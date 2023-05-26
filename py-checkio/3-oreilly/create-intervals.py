def create_intervals(data):
    """
    Create a list of intervals out of set of ints.
    """
    data = sorted(data)
    list_of_intervals, interval = [], []
    for i in range(len(data)):
        try:
            if data[i] + 1 == data[i + 1]:
                interval.append(data[i])
                continue
        except IndexError:
            pass
        interval.append(data[i])
        list_of_intervals.append((min(interval), max(interval)))
        interval = []
    return list_of_intervals


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [
        (1, 5),
        (7, 8),
        (12, 12),
    ], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print("Almost done! The only thing left to do is to Check it!")


"""
From a set of ints you have to create a list of closed intervals as tuples, so the intervals are covering all the values found in the set.

A closed interval includes its endpoints! The interval 1..5, for example, includes each value x that satifies the condition 1 <= x <= 5.

Values can only be in the same interval if the difference between a value and the next smaller value in the set equals one, otherwise a new interval begins. Of course, the start value of an interval is excluded from this rule.
A single value, that does not fit into an existing interval becomes the start- and endpoint of a new interval.

Input: A set of ints.

Output: A list of tuples of two ints, indicating the endpoints of the interval. The Array should be sorted by start point of each interval

Examples:

create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)]
create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)]
"""


# CLEAR
def create_intervals2(data):
    """
    Create a list of intervals out of set of ints.
    """
    data = sorted(data)

    intervals = []
    beginval = endval = None

    for datum in data:
        if beginval is None:
            beginval = endval = datum
        elif endval + 1 == datum:
            endval = datum
        else:
            intervals.append((beginval, endval))
            beginval = endval = datum

    if beginval is not None:
        intervals.append((beginval, endval))

    return intervals


# NICE !!!
def create_intervals3(data):
    left = [x for x in data if x - 1 not in data]
    right = [x for x in data if x + 1 not in data]
    return list(zip(sorted(left), sorted(right)))


# assert create_intervals3({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
# assert create_intervals3({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"

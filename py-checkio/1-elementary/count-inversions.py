def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    lst = []
    count = 0
    for x in sequence:
        for y in lst:
            if y >= x:
                count += 1
        lst.append(x)
    return count


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
    assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
    assert count_inversion((99, -99)) == 1, "Two numbers"
    assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
    print("COUNT >>", count_inversion((5,3,2,1,0)))


## RECURSION
def count_inversion(sequence):
    head, *tail = sequence
    if tail:
        return sum(head > item for item in tail) + count_inversion(tail)
    else:
        return 0

## CLEAR
def count_inversion(sequence):
    return sum(sum(m<n for m in sequence[i+1:]) for i,n in enumerate(sequence))

##
import itertools as it
​
def count_inversion(sequence):
    return sum(x > y for x, y in it.combinations(sequence, 2))

##
def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    count = 0
    for i, x in enumerate(sequence[:-1]):
        for y in sequence[i+1:]:
            if x > y: count += 1
    return count

##
count_inversion = lambda s: sum(a > b for i, b in enumerate(s) for a in s[:i])
"""
 Try to find out how many zeros a given number has at the end.

Input: A positive integer.

Output: An integer.

Examples:
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
"""
def end_zeros(a: int) -> int:
    count = 0
    for i in reversed([i for i in str(a)]):
        if not int(i):
            count += 1
        else:
            break
    return count


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

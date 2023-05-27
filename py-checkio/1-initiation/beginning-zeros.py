"""
 You have a string that consist only of digits. You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consists of digits.

Output: A integer.

Examples:
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2

Precondition: 0-9
"""
def beginning_zeros(a: str) -> int:
    count = 0
    for i in [i for i in a]:
        if not int(i):
            count += 1
        else:
            break
    return count


print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")

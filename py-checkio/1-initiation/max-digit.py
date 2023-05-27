"""
 You have a number and you need to determine which digit in this number is the biggest.

Input: A positive integer.

Output: An integer (0-9).

Examples:
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
"""
def max_digit(value: int) -> int:
    return max(int(i) for i in str(value))


print("Example:")
print(max_digit(10))

# These "asserts" are used for self-checking
assert max_digit(0) == 0
assert max_digit(52) == 5
assert max_digit(634) == 6
assert max_digit(1) == 1
assert max_digit(10000) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")

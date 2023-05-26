"""
You are given the current stock prices. You have to find out which stocks cost more.

Input: The dictionary where the market identifier code is a key and the value is a stock price.

Output: A string and the market identifier code.

Example:

best_stock({
    'CAC': 10.0,
    'ATX': 390.2,
    'WIG': 1.2
}) == 'ATX'
best_stock({
    'CAC': 91.1,
    'ATX': 1.01,
    'TASI': 120.9
}) == 'TASI'

Preconditions: All the prices are unique.
"""


def best_stock(data):
    m = max(data.values())
    return [key for key in data if data[key] == m][0]


if __name__ == "__main__":
    print("Example:")
    print(best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert best_stock({"CAC": 10.0, "ATX": 390.2, "WIG": 1.2}) == "ATX", "First"
    assert best_stock({"CAC": 91.1, "ATX": 1.01, "TASI": 120.9}) == "TASI", "Second"
    print("Coding complete? Click 'Check' to earn cool rewards!")


# OTHER SOLUTIONS
def best_stock(data):
    # your code here
    return max(data.items(), key=lambda x: x[1])[0]

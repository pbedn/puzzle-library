def checkio(numbers_array):
    dct = {abs(t): t for t in numbers_array}
    s = sorted(dct.items(), key=lambda x: x[0])
    return [x[1] for x in s]


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":

    def check_it(array):
        if not isinstance(array, (list, tuple)):
            raise TypeError("The result should be a list or tuple.")
        return list(array)

    assert check_it(checkio((-20, -5, 10, 15))) == [
        -5,
        10,
        15,
        -20,
    ], "Example"  # or (-5, 10, 15, -20)
    assert check_it(checkio((1, 2, 3, 0))) == [0, 1, 2, 3], "Positive numbers"
    assert check_it(checkio((-1, -2, -3, 0))) == [0, -1, -2, -3], "Negative numbers"

"""HINT
First, read about sorted and abs.
abs(5) == abs(-5) == 5
sorted([1, 5, 2, -3]) == [-3, 1, 2, 5]
"""

"""
Let's try some sorting. Here is an array with the specific rules.

The array (a tuple) has various numbers. You should sort it, but sort it by absolute value in ascending order.
For example, the sequence (-20, -5, 10, 15) will be sorted like so: (-5, 10, 15, -20).
Your function should return the sorted list or tuple.

Precondition: The numbers in the array are unique by their absolute values.

Input: An array of numbers , a tuple..

Output: The list or tuple (but not a generator) sorted by absolute values in ascending order.

Addition: The results of your function will be shown as a list in the tests explanation panel.

How it is used: Sorting is a part of many tasks, so it will be useful to know how to use it.

Precondition: len(set(abs(x) for x in array)) == len(array)
0 < len(array) < 100
all(isinstance(x, int) for x in array)
all(-100 < x < 100 for x in array)
"""


# CLEAR
def checkio(numbers_array):
    """
    The magic of the key :)
    """
    return tuple(sorted(numbers_array, key=abs))


"""
Not only builtin function. Any callable can go there.
class BySign(int):
    def __lt__(self, other):
        x, y = map(int, (self, other))
        return 0 <= x < y or y < x < 0 or x < 0 < y

>>> sorted([5, -2, 3, -8, 1, 0, 3], key=BySign)
[-2, -8, 0, 1, 3, 3, 5]
Function “requires an explicit argument” only if you intend to call it. The same way a number “requires an explicit factor” only if you intend to multiply it. :-) It can stand on its own, and be passed to other functions, without any problem.
>>> id(abs), type(abs), repr(abs)
(3546784, <class 'builtin_function_or_method'>, '<built-in function abs>')

>>> *map(abs, [3, -5, -2, 0]),
(3, 5, 2, 0)
You can also
print(abs), dir(abs), hash(abs), help(abs)
or you can even get attributes:
abs.__name__, abs.__doc__, abs.__self__, abs.__text_signature__
Moreover, you can do that (or similar) with any object. The only thing callables are special about, is that they have an attribute __call__.
>>> hasattr(abs, '__call__')
True

>>> abs.__call__(-5)
5
"""
checkio = lambda n: sorted(n, key=abs)

from functools import partial as c

checkio = c(sorted, key=abs)

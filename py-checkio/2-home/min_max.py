def min(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        if key:
            return sorted(*args, key=key)[0]
        else:
            return sorted(*args)[0]
    else:
        if key:
            return sorted(args, key=key)[0]
        else:
            return sorted(args)[0]


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if len(args) == 1:
        if key:
            return sorted(*args, key=key, reverse=True)[0]
        else:
            return sorted(*args, reverse=True)[0]
    else:
        if key:
            return sorted(args, key=key, reverse=True)[0]
        else:
            return sorted(args, reverse=True)[0]


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert max(3, 2) == 3, "Simple case max"
    assert min(3, 2) == 2, "Simple case min"
    assert max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert min("hello") == "e", "From string"
    assert max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
In this mission you should write you own py3 implementation (but you can use py2 for this)
of the built-in functions min and max. Some builtin functions are closed here: import, eval, exec, globals.
Don't forget you should implement two functions in your code.

max(iterable, *[, key]) or min(iterable, *[, key])
max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])

Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.

If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned.
If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.

The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key
from each list element (for example, key=str.lower).

If multiple items are maximal (minimal), the function returns the first one encountered.

-- Python Documentation (Built-in Functions)

Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.

Output: The largest item for the "max" function and the smallest for the "min" function.

Example:

max(3, 2) == 3
min(3, 2) == 2
max([1, 2, 0, 3, 4]) == 4
min("hello") == "e"
max(2.2, 5.6, 5.9, key=int) == 5.6
min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]


How it is used: This task will help you understand how some of the built-in functions work on a more precise level.

Precondition: All test cases are correct and functions don't have to raise exceptions.

"""


# SIMPLE
def min(*args, **kwargs):
    key = kwargs.get("key", None)
    args = list(args[0] if len(args) is 1 else args)
    smallest = args[0]

    for a in args:
        if key:
            if key(a) < key(smallest):
                smallest = a
        elif a < smallest:
            smallest = a

    return smallest


def max(*args, **kwargs):
    key = kwargs.get("key", None)
    args = list(args[0] if len(args) is 1 else args)
    largest = args[0]

    for a in args:
        if key:
            if key(a) > key(largest):
                largest = a
        elif a > largest:
            largest = a

    return largest


# ----------------------------------------------


def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, key=None):
    return get_first_from_sorted(args, key, False)


def max(*args, key=None):
    return get_first_from_sorted(args, key, True)


# ----------------------------------------------

arguments = lambda args: args if len(args) > 1 else args[0]


def min(*args, **kwargs):
    key = kwargs.get("key")
    return sorted(arguments(args), key=key)[0]


def max(*args, **kwargs):
    key = kwargs.get("key")
    return sorted(arguments(args), key=key, reverse=True)[0]


# ----------------------------------------------


def min(*args, **kwargs):
    l = list(args)
    if len(l) == 1:
        l = list(*args)
    return sorted(l, **kwargs)[0]


def max(*args, **kwargs):
    l = list(args)
    if len(l) == 1:
        l = list(*args)
    kwargs.update({"reverse": True})
    return sorted(l, **kwargs)[0]


# ----------------------------------------------

min = lambda *a, **k: sorted(a if len(a) - 1 else a[0], **k)[0]
max = lambda *a, **k: min(*a, **dict(k, reverse=True))

# ----------------------------------------------


def min(*a, **kw):
    return minmax(*a, **kw)


def max(*a, **kw):
    kw["rev"] = True
    return minmax(*a, **kw)


def minmax(*a, **kw):
    if len(a) == 1:
        a = iter(a[0])
    return sorted(a, key=kw.get("key", None), reverse=kw.get("rev", False))[0]

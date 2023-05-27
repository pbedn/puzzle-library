def checkio(number):
    res = 1
    for x in str(number):
        if x == "0":
            continue
        res *= int(x)
    return res


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1


# CLEAR
def checkio(number):
    """
    Convert into the string and iterate.
    """
    res = 1
    for d in str(number):
        res *= int(d) if int(d) else 1
    return res


# CLEAR
def checkio(number):
    total = 1
    # for i in str(number).replace("0",""):
    for i in str(number).replace("0", "1"):
        total *= int(i)
    return total


# CREATIVE
checkio = lambda n: eval("*".join(i for i in str(n) if i != "0"))

# CREATIVE

from operator import mul
from functools import reduce

checkio = lambda n: reduce(mul, (int(d) or 1 for d in str(n)), 1)


# SPEEDY
def checkio(num):
    list_num = [n for n in str(num) if n != "0"]
    return eval("*".join(list_num))

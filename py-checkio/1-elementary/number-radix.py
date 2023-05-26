def checkio(str_number, radix):
    try:
        return int(str_number, radix)
    except ValueError:
        return -1


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio("1A", 9) == -1, "first"
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"
    assert 1 == 1


# CLEAR
def checkio(str_number, radix):
    wynik = 0
    k = len(str_number) - 1
    abc = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    error = False
    for i in str_number:
        if abc.find(i) != -1 and abc.find(i) < radix:
            liczba = abc.find(i)
            wynik += liczba * pow(radix, k)
            k -= 1
        else:
            error = True
    if error:
        wynik = -1
    return wynik


# CREATIVE
digits = "0123456789abcdefghijklmnopqrstuvwxyz"


def checkio(number, base):  # No try-except example
    if set(number.lower()) - set(digits[:base]):
        return -1
    return int(number, base)


def checkio(str_number, radix):
    value = 0
    for i, c in enumerate(reversed(str_number)):
        digit = ord(c) - (55 if c.isalpha() else 48)
        if digit >= radix:
            return -1
        value += radix**i * digit

    return value


def checkio(str_number, radix):
    glyphs = [x for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"]
    power = 0
    result = 0
    for digit in reversed(str_number):
        value = glyphs.index(digit)
        if value >= radix:
            return -1
        result += value * radix**power
        power += 1
    return result


"""
Do you remember the radix and Numeral systems from math class? Let's practice with it.

In the system with radix 13, for example, a string of digits such as 398 denotes the number 3 × 13^2 + 9 × 13^1 + 8 × 13^0.

You are given a positive number as a string along with the radix for it.
Your function should convert it into decimal form. The radix is less than 37 and greater than 1.
The task uses digits and the letters A-Z for the strings.

Watch out for cases when the number cannot be converted.
For example: "1A" cannot be converted with radix 9. For these cases your function should return -1.

Input: Two arguments. A number as string and a radix as an integer.

Output: The converted number as an integer.

How it is used: Here you will learn how to work with the various numeral systems and handle exceptions.

Precondition: 
re.match("\A[A-Z0-9]\Z", str_number)
0 < len(str_number) ≤ 10
2 ≤ radix ≤ 36
"""

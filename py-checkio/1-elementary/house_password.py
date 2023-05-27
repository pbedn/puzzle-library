from string import ascii_lowercase


def checkio(data):
    res, res2, res3 = False, False, False
    for d in data:
        if d in ascii_lowercase:
            res = True
        if d in ascii_lowercase.upper():
            res2 = True
        if d in "0123456789":
            res3 = True

    return len(data) >= 10 and res and res2 and res3


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("A1213pokl") == False, "1st example"
    assert checkio("bAse730onE4") == True, "2nd example"
    assert checkio("asasasasasasasaas") == False, "3rd example"
    assert checkio("QWERTYqwerty") == False, "4th example"
    assert checkio("123456123456") == False, "5th example"
    assert checkio("QwErTy911poqqqq") == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""
Stephan and Sophia forget about security and use simple passwords for everything.
Help Nikola develop a password security check module. The password will be considered strong enough
if its length is greater than or equal to 10 symbols, it has at least one digit, as well as containing
one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string (Unicode for python 2.7).

Output: Is the password safe or not as a boolean or any data type that can be converted and processed as a boolean.
In the results you will see the converted results.

Example:

checkio('A1213pokl') == False
checkio('bAse730onE') == True
checkio('asasasasasasasaas') == False
checkio('QWERTYqwerty') == False
checkio('123456123456') == False
checkio('QwErTy911poqqqq') == True


How it is used: If you are worried about the security of your app or service,
you can check your users' passwords for complexity. You can use these skills to
require that your users passwords meet more conditions (punctuations or unicode).

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64
"""

# CLEAR
import re

DIGIT_RE = re.compile("\d")
UPPER_CASE_RE = re.compile("[A-Z]")
LOWER_CASE_RE = re.compile("[a-z]")


def checkio(data):
    """
    Return True if password strong and False if not

    A password is strong if it contains at least 10 symbols,
    and one digit, one upper case and one lower case letter.
    """
    if len(data) < 10:
        return False

    if not DIGIT_RE.search(data):
        return False

    if not UPPER_CASE_RE.search(data):
        return False

    if not LOWER_CASE_RE.search(data):
        return False

    return True


def checkio(data):
    import re

    if len(data) < 10:
        return False
    if not re.search("[0-9]", data):
        return False
    if not re.search("[a-z]", data):
        return False
    if not re.search("[A-Z]", data):
        return False
    return True


def checkio(data):
    if len(data) < 10:
        return False
    if data.upper() == data:
        return False
    if data.lower() == data:
        return False
    return any(c.isdigit() for c in data)


def checkio(data):
    return all(
        re.search(regexp, data) for regexp in ("[a-z]", "[A-Z]", "[0-9]", ".{10,}")
    )

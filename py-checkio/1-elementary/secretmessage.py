import string


def find_message(text):
    """Find a secret message"""
    result = ""
    for l in text:
        if l.isupper():
            result += l
    return result


# print find_message("How are you? Eh, ok.")

if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
    assert find_message("hello world!") == "", "Nothing"
    assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"


# CLEAR
return "".join(c for c in text if c.isupper())

find_message = lambda text: "".join(filter(str.isupper, text))

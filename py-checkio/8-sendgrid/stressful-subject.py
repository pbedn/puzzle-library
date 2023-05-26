def is_stressful(subj):
    """
    recoognise stressful subject
    """
    if subj[-3:] == "!!!" or subj.isupper():
        return True

    words = ["help", "asap", "urgent"]
    sep = ["!", "-", "."]
    s = ""
    previous = None

    for char in subj:
        if not (char in sep or previous == char):
            s += char.lower()
        previous = char

    if any(word in s for word in words):
        return True
    return False


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful("Hi") == False, "First"
    assert is_stressful("I neeed HELP") == True, "Second"
    print("Done! Go Check it!")
    assert is_stressful("h!e!l!p") is True
    assert is_stressful("something is gona happen") is False
    assert is_stressful("We need you A.S.A.P.!!") is True
    assert is_stressful("where are you?!!!!") is True
    assert is_stressful("UUUURGGGEEEEENT here") is True
    assert is_stressful("Heeeeeey!!! I’m having so much fun!”") is False
    assert is_stressful("HI HOW ARE YOU?") is True
"""
The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help", "asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P", even in a very loooong way "HHHEEEEEEEEELLP"

Input: Subject line as a string.

Output: Boolean.

Precondition: Subject can be up to 100 letters
"""


def is_stressful2(subj):
    import itertools

    RED = ["help", "asap", "urgent"]

    if subj.isupper() or subj.endswith("!!!"):
        return True

    textOnly = "".join(
        l.lower() for l in subj if l.isalpha() or l.isspace()
    )  # keep only texte
    testFormat = "".join(
        ch for ch, _ in itertools.groupby(textOnly)
    )  # suppress duplicate characters

    return any([word for word in RED if word in testFormat])


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert is_stressful2("Hi") == False, "First"
    assert is_stressful2("I neeed HELP") == True, "Second"
    print("Done! Go Check it!")
    assert is_stressful2("h!e!l!p") is True
    assert is_stressful2("something is gona happen") is False
    assert is_stressful2("We need you A.S.A.P.!!") is True
    assert is_stressful2("where are you?!!!!") is True
    assert is_stressful2("UUUURGGGEEEEENT here") is True
    assert is_stressful2("Heeeeeey!!! I’m having so much fun!”") is False
    assert is_stressful2("HI HOW ARE YOU?") is True

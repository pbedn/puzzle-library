from string import punctuation

VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    count = 0
    for p in punctuation:
        text = text.replace(p, " ")
    striped_ = text.upper().split()
    for word in striped_:
        # if len(word) == 1:
        #     continue
        ok = True
        for i in range(len(word) - 1):
            if not (
                word[i] in CONSONANTS
                and word[i + 1] in VOWELS
                or word[i + 1] in CONSONANTS
                and word[i] in VOWELS
            ):
                ok = False
        if ok and len(word) > 1:
            count += 1
    return count


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == "__main__":
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"

"""
Our robots are always working to improve their linguistic skills. For this mission, they research the latin alphabet and its applications.

The alphabet contains both vowel and consonant letters (yes, we divide the letters).
Vowels -- A E I O U Y
Consonants -- B C D F G H J K L M N P Q R S T V W X Z

You are given a block of text with different words. These words are separated by white-spaces and punctuation marks. Numbers are not considered words in this mission (a mix of letters and digits is not a word either). You should count the number of words (striped words) where the vowels with consonants are alternating, that is; words that you count cannot have two consecutive vowels or consonants. The words consisting of a single letter are not striped -- do not count those. Casing is not significant for this mission.

Input: A text as a string (unicode)

Output: A quantity of striped words as an integer.

Example:

checkio("My name is ...") == 3
checkio("Hello world") == 0
checkio("A quantity of striped words.") == 1, "Only of"
checkio("Dog,cat,mouse,bird.Human.") == 3
How it is used: This idea in this task is a useful exercise for linguistic research and analysis. Text processing is one of the main tools used in the analysis of various books and languages and can help translate print text to a digital format.

Precondition:The text contains only ASCII symbols.
0 < len(text) < 105
"""

###############################
# Nice Algorithm but ugly solution
PUNCTUATION = ",.!?"


def checkio1(text):
    text = text.upper()
    for c in PUNCTUATION:
        text = text.replace(c, " ")
    for c in VOWELS:
        text = text.replace(c, "v")
    for c in CONSONANTS:
        text = text.replace(c, "c")

    words = text.split(" ")

    count = 0
    for word in words:
        if len(word) > 1 and word.isalpha():
            if word.find("cc") == -1 and word.find("vv") == -1:
                count += 1

    return count


###############################
# Much nore prettier


def striped(word):
    """Is a word (encoded with d,v,c,p) striped?"""
    for forbidden in "d", "v" * 2, "c" * 2:
        if forbidden in word:
            return False
    return len(word) > 1


def encode(text):
    """Generate kinds of letters for text (d,v,c,p)."""
    for char in text:
        if char.lower() in "aeiouy":
            yield "v"  # vowel
        elif char.isalpha():
            yield "c"  # consonant
        elif char.isdigit():
            yield "d"  # digit
        else:
            yield "p"  # punctuation (and space)


def checkio2(text):
    """Number of striped words."""
    encoded = "".join(encode(text))
    words = encoded.split("p")
    return sum(map(striped, words))


###############################
# Other nice solution
def checkio3(text):
    text = "".join(
        "V" if t in "AEIOUY" else "C" if t.isalpha() else "D" if t.isdigit() else " "
        for t in text.upper()
    )
    return sum(
        "VV" not in token and "CC" not in token and "D" not in token and len(token) > 1
        for token in text.split()
    )

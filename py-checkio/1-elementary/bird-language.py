"""
Stephan has a friend who happens to be a little mechbird. Recently, he was trying to teach it how to speak basic language. Today the bird spoke its first word: "hieeelalaooo". This sounds a lot like "hello", but with too many vowels. Stephan asked Nikola for help and he helped to examine how the bird changes words. With the information they discovered, we should help them to make a translation module.

The bird converts words by two rules:
- after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
- after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
Vowels letters == "aeiouy".

You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.

Input: A bird phrase as a string.

Output: The translation as a string.

Precondition: re.match("\A([a-z]+\ ?)+(?<!\ )\Z", phrase)
A phrase always has the translation.
"""


VOWELS = "aeiouy"


def translate(phrase):
    result = ""
    while True:
        try:
            letter = next(iter(phrase))
        except StopIteration:
            return result
        if letter == " ":
            phrase = phrase[1:]
        elif letter not in VOWELS:
            phrase = phrase[2:]
        else:
            phrase = phrase[3:]
        result += letter
        print(result, len(result), list(result))


import re


def translate(phrase):
    phrase = re.sub(r"([bcdfghjklmnpqrstvwxz])\w", r"\1", phrase)
    phrase = re.sub(r"([aeiouy]){3}", r"\1", phrase)
    return phrase


def translate(phrase):
    i, end, result = 0, len(phrase), []
    while i < end:
        letter = phrase[i]
        result.append(letter)
        if letter in VOWELS:
            i += 3
        elif letter == " ":  # space
            i += 1
        else:
            i += 2
    return "".join(result)


if __name__ == "__main__":
    assert translate("hieeelalaooo") == "hello", "Hi!"
    assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin", "Joey?"
    assert translate("aaa bo cy da eee fe") == "a b c d e f", "Alphabet"
    assert translate("sooooso aaaaaaaaa") == "sos aaa", "Mayday, mayday"

# https://py.checkio.org/mission/most-wanted-letter/

import string
from operator import itemgetter

A = string.ascii_lowercase


def checkio(text):
    if len(text) == 1:
        return text.lower()
    counter = {}
    single = True
    for l in text.lower():
        if l in A:
            try:
                counter[l] += 1
                single = False
            except KeyError:
                counter[l] = 1
    res = sorted(counter.items(), key=itemgetter(1), reverse=True)
    if single:
        x = sorted(res, key=lambda x: ord(x[0]))[0][0]
        return x[0][0].lower()
    rr = res[0]
    tmp = []
    for r in res:
        if r[1] == rr[1]:
            tmp.append(r)
    if len(tmp) > 1:
        x = sorted(tmp, key=lambda x: ord(x[0]))[0][0]
        return x[0][0].lower()
    return res[0][0].lower()


if __name__ == "__main__":
    assert checkio("Z") == "z", "1"
    assert checkio("ab") == "a", "2"
    assert checkio("abc") == "a", "3"
    assert checkio("aa") == "a", "4"
    assert checkio("aabb") == "a", "5"
    assert checkio("bbaa") == "a", "6"
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
    assert checkio("Lorem ipsum dolor sit amet") == "m", "Lorem test"
    assert (
        checkio("fn;lsfndasl;f naslkdnlkasdnfslahwemwjkrjkl;zcmk;lzcdkcslksdkseewme,")
        == "k"
    ), "Complex test"
    print("Additional tests are done")


"""
You are given a text, which contains different english letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.

If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

Input: A text for analysis as a string.

Output: The most frequent letter in lower case as a string.

Example:

checkio("Hello World!") == "l"
checkio("How do you do?") == "o"
checkio("One") == "e"
checkio("Oops!") == "o"
checkio("AAaooo!!!!") == "a"
checkio("abe") == "a"

How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear. This is interesting stuff for language experts!
"""

# CLEAR


def checkio(text):
    """
    We iterate through latyn alphabet and count each letter in the text.
    Then 'max' selects the most frequent letter.
    For the case when we have several equal letter,
    'max' selects the first from they.
    """
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)


from string import ascii_lowercase as letters

checkio = lambda text: max(letters, key=text.lower().count)


from collections import Counter


def checkio(text):
    count = Counter([x for x in text.lower() if x.isalpha()])
    m = max(count.values())
    return sorted([x for (x, y) in count.items() if y == m])[0]


def checkio(text):
    ltext = [ch for ch in text.lower() if ch.isalpha()]
    maxCh = ""
    maxN = 0
    for ch in sorted(ltext):
        if ltext.count(ch) > maxN:
            maxCh, maxN = ch, ltext.count(ch)
    return maxCh


def checkio(text):
    """Return most common letter."""
    normalized = text.lower()
    letters_set = set(normalized) & set(string.ascii_lowercase)
    return max(letters_set, key=lambda c: (normalized.count(c), -ord(c)))


## CREATIVE
checkio = lambda t: max("abcdefghijklmnopqrstuvwxyz", key=t.lower().count)


def checkio(text):
    l = [text.lower().count(chr(x)) for x in range(97, 123)]
    return chr(l.index(max(l)) + 97)


def checkio(text):
    return max([x for x in sorted(text.lower()) if x.isalpha()], key=text.lower().count)


## SPEEDY
checkio = lambda t: max(map(chr, range(97, 123)), key=t.lower().count)

import string
from collections import Counter


def checkio(text):
    # lower-case-ize text, then remove any non-letter characters
    text = [char for char in text.lower() if char in string.ascii_lowercase]

    # count occurrences of letters
    # returns a list of tuples [('letter', occurrences), (...)]
    most_common = Counter(text).most_common()

    # sort by number of occurrences (in descending order, hence -x[1]), then
    # sort by letter in ascending order
    most_common.sort(key=lambda x: (-x[1], x[0]))

    # thanks to the sorting, the desired result will be the letter in the first
    # element of the list
    return most_common[0][0]

"""
Hey, are you ready for a Scrabble game party?
You have a list of words and you have to find only one that is the most valuable among them.
Rules:
The worth of each word is equivalent to the sum of letters which it consists of.
The values of the letters are as follow:
e, a, i, o, n, r, t, l, s, u = 1
d, g = 2
b, c, m, p = 3
f, h, v, w, y = 4
k = 5
j, x = 8
q, z = 10
For example, the worth of the word 'dog' is 5, because 'd' = 2, 'o' = 1 and 'g' = 2.

example

Input: A list of words.

Output: The most valuable word.

Precondition:
2 <= words <= 10
Real words only
lowercase letters only
"""

VALUES = {
    "e": 1,
    "a": 1,
    "i": 1,
    "o": 1,
    "n": 1,
    "r": 1,
    "t": 1,
    "l": 1,
    "s": 1,
    "u": 1,
    "d": 2,
    "g": 2,
    "b": 3,
    "c": 3,
    "m": 3,
    "p": 3,
    "f": 4,
    "h": 4,
    "v": 4,
    "w": 4,
    "y": 4,
    "k": 5,
    "j": 8,
    "x": 8,
    "q": 10,
    "z": 10,
}


def worth_of_words(words):
    best_word = ""
    best_sum = 0
    print("--------------")
    for w in words:
        sum = 0
        for l in w:
            sum += VALUES[l]
        print(w, sum)
        if sum > best_sum:
            best_word = w
            best_sum = sum
    return best_word


def worth_of_words(words):
    return max(words, key=lambda word: sum(VALUES[i] for i in word))


if __name__ == "__main__":
    print("Example:")
    print(worth_of_words(["hi", "quiz", "bomb", "president"]))
    assert worth_of_words(["hi", "quiz", "bomb", "president"]) == "quiz"
    assert worth_of_words(["zero", "one", "two", "three", "four", "five"]) == "zero"
    assert worth_of_words(["i", "am", "happy", "to", "learn", "python"]) == "happy"
    print("Coding complete? Click 'Check' to earn cool rewards!")

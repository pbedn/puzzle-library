"""
 In a given string you should reverse every word, but the words should stay in their places.
Input: A string.
Output: A string.
Precondition: The line consists only from alphabetical symbols and spaces.
"""
def backward_string_by_word(text: str) -> str:
    new_text, new_word = "", ""
    word_end_idx = 0
    for t in text.split():
        spaces_count = text.count(" ", word_end_idx, text.find(t, word_end_idx))
        new_text += new_word + " " * spaces_count
        word_end_idx = text.find(t, word_end_idx) + len(t)
        new_word = t[::-1]
    new_text += new_word
    return new_text


print("Example:")
print(backward_string_by_word(""))

# These "asserts" are used for self-checking
assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"
assert backward_string_by_word('olleH Hello') == 'Hello olleH'
assert backward_string_by_word('ha ha ha   this is cool') == 'ah ah ah   siht si looc'

print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Your task is to decrypt the secret message using the Morse code.
The message will consist of words with 3 spaces between them and 1 space between each letter of each word.
If the decrypted text starts with a letter then you'll have to print this letter in uppercase.
 Input: The secret message (string).

Output: The decrypted text (string).

How it is used: For cryptography and spy work.

Precondition:
0 < len(message) < 100
The message will consist of numbers and English letters only.
"""
MORSE = {
    ".-": "a",
    "-...": "b",
    "-.-.": "c",
    "-..": "d",
    ".": "e",
    "..-.": "f",
    "--.": "g",
    "....": "h",
    "..": "i",
    ".---": "j",
    "-.-": "k",
    ".-..": "l",
    "--": "m",
    "-.": "n",
    "---": "o",
    ".--.": "p",
    "--.-": "q",
    ".-.": "r",
    "...": "s",
    "-": "t",
    "..-": "u",
    "...-": "v",
    ".--": "w",
    "-..-": "x",
    "-.--": "y",
    "--..": "z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
}


def morse_decoder(code: str) -> str:
    s, word = "", ""
    skip = -1
    for c in code:
        if c == " " and not word:
            skip += 1
            if skip:
                s += " "
                skip = -1
        elif c == " ":
            s += MORSE[word]
            word = ""
        else:
            word += c
    s += MORSE[word]
    return s.capitalize()


print("Example:")
print(morse_decoder("... --- -- .   - . -..- -"))

assert morse_decoder("... --- -- .   - . -..- -") == "Some text"
assert (
    morse_decoder("..   .-- .- ...   -... --- .-. -.   .. -.   .---- ----. ----. -----")
    == "I was born in 1990"
)
assert (
    morse_decoder(
        "...- ...-- .-. -.--   .---- ----- -. --.   ... - .-. .---- -. --.   .-- .----"
        " - ....   ... ----- -- ...--   -. ..- -- -... ...-- .-. ....."
    )
    == "V3ry 10ng str1ng w1th s0m3 numb3r5"
)

print("The mission is done! Click 'Check Solution' to earn rewards!")

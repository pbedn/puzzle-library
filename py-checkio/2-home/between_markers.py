"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:

The initial and final markers are always different.
If there is no initial marker, then the first character should be considered the beginning of a string.
If there is no final marker, then the last character should be considered the ending of a string.
If the initial and final markers are missing then simply return the whole string.
If the final marker comes before the initial marker, then return an empty string.
Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.

Output: A string.

Example:

between_markers('What is >apple<', '>', '>') == 'apple'
between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
1
2
How it is used: for parsing texts

Precondition: can't be more than one final marker and can't be more than one initial
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
    returns substring between two given markers
    """
    pos_end = text.find(end) if text.find(end) >= 0 else len(text)
    pos_begin = text.find(begin) + len(begin) if text.find(begin) >= 0 else 0
    return text[pos_begin:pos_end]


if __name__ == "__main__":
    assert between_markers("aaa>bbb", "<", ">") == "aaa", "2 No begin"
    assert between_markers("aaa<bbb", "<", ">") == "bbb", "2.5 No end"
    assert between_markers("What is <apple>", "<", ">") == "apple", "3 both markers"
    assert (
        between_markers(
            "<head><title>My new site</title></head>", "<title>", "</title>"
        )
        == "My new site"
    ), "4 HTML"
    assert between_markers("No[/b] hi", "[b]", "[/b]") == "No", "5 No opened"
    assert between_markers("No [b]hi", "[b]", "[/b]") == "hi", "6 No close"
    assert between_markers("No hi", "[b]", "[/b]") == "No hi", "7 No markers at all"
    assert between_markers("No >hi<", "<", ">") == "", "8 Wrong direction"
    print("Wow, you are doing pretty good. Time to check it!")
    assert (
        between_markers("Never send a human to do a machine's job.", "Never", "do")
        == " send a human to "
    ), "Bonus"

"""
I believe that many of you have dealt with such a problem. One day you are working in the text editor, saving the document and closing it. And the next day you are re-reading the text and realizing that one of the previous versions was better but there is no way to get it back. This thing can be easily handled by the version control system (for example, git), but it’s used mostly by the developers and not the ordinary people who work with texts. In this mission you’ll help the latter by creating a text editor prototype that supports the version control system, which will allow to save different versions of the text and restore any one of them.
Your task is to create 2 classes: Text and SavedText. The first will works with texts (adding, font changing, etc.), the second will control the versions and save them.

Class Text should have the next methods:
write(text) - adds (text) to the current text;
set_font(font name) - sets the chosen font. Font is applied to the whole text, even if it’s added after the font is set. The font is displayed in the square brackets before and after the text: "[Arial]...example...[Arial]". Font can be specified multiple times but only the last variant is displays;
show() - returns the current text and font (if is was set);
restore(SavedText.get_version(number)) - restores the text of the chosen version.

Class SavedText should have the next methods:
save_text(Text) - saves the current text and font. The first saved version has the number 0, the second - 1, and so on;
get_version(number) - this method works with the 'restore' method and is used for choosing the needed version of the text.

In this mission you can use the Memento design pattern.

Example:

text = Text()
saver = SavedText()

text.write("At the very beginning ")
saver.save_text(text)
text.set_font("Arial")
saver.save_text(text)
text.write("there was nothing.")
text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

text.restore(saver.get_version(0))
text.show() == "At the very beginning "

Input: information about the text and saved copies.

Output: the text after all of the commands.

How it is used: To save the object’s previous states with the ability to return to them, in case something goes wrong.

Precondition: No more than 10 saved copies.
"""

from copy import deepcopy


class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state


class Text:
    def __init__(self):
        self._text = ""
        self._font = ""

    def write(self, text):
        self._text += text

    def set_font(self, font):
        self._font = font

    def show(self):
        if self._font:
            return "[{font}]{text}[{font}]".format(font=self._font, text=self._text)
        return self._text

    def restore(self, text):
        """Restore text instance fields"""
        self._font = text._font
        self._text = text._text


class SavedText:
    def __init__(self):
        self.versions = []

    def save_text(self, text):
        """Save text instance"""
        self.versions.append(Memento(deepcopy(text)))

    def get_version(self, number):
        """Get text instance"""
        return self.versions[number].get_state()


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing

    text = Text()
    saver = SavedText()

    text.write("At the very beginning ")
    saver.save_text(text)
    text.set_font("Arial")
    saver.save_text(text)
    text.write("there was nothing.")

    assert text.show() == "[Arial]At the very beginning there was nothing.[Arial]"

    text.restore(saver.get_version(0))
    assert text.show() == "At the very beginning "

    print("Coding complete? Let's try tests!")

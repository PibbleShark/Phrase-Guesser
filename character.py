import re


class Character(str):
    """Character takes a character and stores it.  It can then check that a character is a single letter and stores
    guessed letters as correct or incorrect.  It also has a method for displaying a correctly guessed letter in the
    string of underscores created by the Phrase class"""
    correct_characters = []
    incorrect_characters = []

    def __init__(self, character):
        super().__init__()
        self.character = character

    def hide_character(self):
        self.character = " _ "

    def is_letter(self):
        letter = re.match(r'^[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+$', self.character)
        if not letter:
            raise ValueError("That is not a letter")
        else:
            return letter

    def correct_character(self):
        if self.character.lower() in self.correct_characters:
            self.character = True
        else:
            self.character = False

    def validate_character(self):
        if len(self.character) > 1:
            raise ValueError("Looking for a single letter")

        self.is_letter()
        if not self.is_letter():
            raise ValueError("That is not a letter")

        elif self.character in self.incorrect_characters:
            raise ValueError("That was not right the first time")

        elif self.character in self.correct_characters:
            raise ValueError("You have already guessed that letter")
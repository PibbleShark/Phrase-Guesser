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

    def replace_character(self, string, indices):
        lst1 = list(string)
        for index in indices:
            lst1[index] = self.character
        return ''.join(lst1)

    def search_phrase(self, string):
        match = [character.start() for character in re.finditer(self.character.lower(), string.lower())]
        return match

    def is_letter(self):
        if len(self.character) > 1:
            raise ValueError
        else:
            letter = re.match(r'^[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+$', self.character)
        if letter is None:
            return False
        else:
            return True

    def correct_characters_append(self):
        return self.correct_characters.append(self.character)

    def incorrect_characters_append(self):
        return self.incorrect_characters.append(self.character)

    def validate_input(self):
        if len(self.character) > 1:
            raise ValueError("Looking for a single letter")

        self.is_letter()
        if not self.is_letter():
            raise ValueError("That is not a letter")

        elif self.character in self.incorrect_characters:
            raise ValueError("That was not right the first time")

        elif self.character in self.correct_characters:
            raise ValueError("You have already guessed that letter")


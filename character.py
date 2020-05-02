import re


class Character:

    def __init__(self, character):
        self.character = character

    @staticmethod
    def display_letter_string(lst):
        return ','.join(lst).upper()

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
            raise ValueError
        return self.character

from character import Character


class Phrase:
    """Phrase takes a phrase, converts it into a set of Character objects and can turn it into a string of underscores
    to hide the letters it contains.
    It also is used to check for a correct answer in the phrase guessing game."""

    def __init__(self, phrase):
        self.phrase = [Character(letter) for letter in phrase]
        self.phrase_string = ''.join(self.phrase)
        self.phrase_letter_list = []
        for character in self.phrase:
            if character.is_letter:
                self.phrase_letter_list.append(character.lower())

    def display_phrase(self):
        for letter in self.phrase:
            if letter.is_letter:
                if not letter.correct_character:
                    letter.hide_character()
        return ''.join(self.phrase)

    def match_character(self, letter):
        for character in self.phrase:
            if character.lower() == letter.lower():
                Character.correct_characters.append(letter.lower)
            else:
                Character.incorrect_characters.append(letter.lower)

    def phrase_guess(self, guessed_phrase):
        self.phrase = [character for character in self.phrase]
        return all(list(guessed_phrase.capitalize()))

    def phrase_match(self):
        if self.phrase_letter_list == Character.correct_characters:
            return True
        else:
            return False

from character import Character


class Phrase:
    """Phrase takes a phrase, converts it into a set of Character objects and can display the characters.
    It has a method to see if a given character is present in the phrase.
    It also is used to check for a correct answer in the phrase guessing game."""

    def __init__(self, phrase):
        self.phrase = [Character(letter) for letter in phrase]

    def display_phrase(self):
        display_phrase = []
        for character in self.phrase:
            display_phrase.append(character.display_character())
        return ' '.join(display_phrase)

    def search_phrase(self, letter):
        for character in self.phrase:
            if str(character) == letter:
                character.add_correct()
                return True

    def phrase_guess(self, guessed_phrase):
        if guessed_phrase.lower() == ''.join(self.phrase).lower():
            return True
        else:
            return False

    def phrase_match(self):
        if self.display_phrase().lower() == ' '.join(self.phrase).lower():
            return True
        else:
            return False


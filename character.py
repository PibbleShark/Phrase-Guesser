

class Character(str):
    """Character takes a character and stores it. It works with the Phrase class to store correctly guessed letters.
    a character object will display as an _ until that character has been correctly guessed."""
    correct_characters = []

    def __init__(self, character):
        super().__init__()
        self.character = character.lower()

    def display_character(self, ):
        if self.character in self.correct_characters:
            return self.character.upper()
        elif self.character != ' ' and self.character not in self.correct_characters:
            return '_'
        elif self.character == ' ':
            return ' '

    def add_correct(self):
        return self.correct_characters.append(self.character.lower())

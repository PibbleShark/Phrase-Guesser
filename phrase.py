from character import Character


class Phrase(str):

    def __init__(self, phrase):
        super().__init__()
        self.phrase = phrase
        self.letters_guessed = []
        self.letters_guessed.append(Character)

    def display_length(self):
        split_phrase = self.phrase.split(' ')
        return ' '.join(['_' * len(word) for word in split_phrase])

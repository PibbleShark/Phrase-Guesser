from character import Character


class Phrase(str):

    def __init__(self, phrase):
        super().__init__()
        self.phrase = phrase
        self.phrase_finished = [Character(letter) for letter in phrase]

    def display_length(self):
        split_phrase = self.phrase.split(' ')
        return ' '.join(['_' * len(word) for word in split_phrase])


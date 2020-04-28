from phraselist import phrases_original
from phrase import PhraseGenerator


class Character(str):

    def __init__(self, string):
        super().__init__()
        self.string = string
        self.split_string = string.split(' ')

    def display_length(self):
        return ' '.join(['_' * len(word) for word in self.split_string])


char_string = Character(PhraseGenerator(phrases_original).rand_phrase())
print(char_string.display_length())

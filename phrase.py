from character import Character


class Phrase(str):

    def __init__(self, phrase):
        super().__init__()
        self.phrase = [Character(letter) for letter in phrase]
        self.string_phrase = ''.join(self.phrase)

    @property
    def display_length(self):
        phrase_ = []
        for letter in self.phrase:
            if letter.is_letter():
                phrase_.append('_')
            else:
                phrase_.append(' ')
        return ''.join(phrase_)
        
    def phrase_guesser(self):
        guessed_phrase = input('complete the phrase:   ')
        if guessed_phrase.upper() == self.string_phrase.upper():
            print('You win!')
            return True
        else:
            print('incorrect')
            return False

    def phrase_match(self, string):
        if self.string_phrase.upper() == string.upper():
            print('Your Win!')
            return True



class PhraseGenerator(str):
    import random

    def __init__(self, phrases):
        super().__init__()
        self.phrases = phrases

    def rand_phrase(self):
        return self.random.choice(self.phrases)

class PhraseGenerator:
    import random
    phrases = []

    def __init__(self, phrases=None):
        assert isinstance(phrases, list)  # pycharm suggested this as a debugging tool
        self.phrases = phrases

    def add_phrase(self, phrase):
        self.phrases.append(phrase)

    @property
    def phrase_selector(self):
        return self.random.choice(self.phrases)

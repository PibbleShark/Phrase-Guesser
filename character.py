
class Character:

    def __init__(self, string):
        self.string = string
        self.split_string = string.split(' ')

    def display_length(self):
        return ' '.join(['_' * len(word) for word in self.split_string])

    def replace_character(self, character, indices):
        lst1 = list(self.string)
        for index in indices:
            lst1[index] = character
        return ''.join(lst1)

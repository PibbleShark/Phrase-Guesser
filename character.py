

class Character:

    def __init__(self, string):
        self.split_string = string.split(' ')
        self.string = string

    def display_length(self):
        return ' '.join(['_'*len(word) for word in self.split_string])
        



        
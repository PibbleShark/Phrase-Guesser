import sys
import re
from phraselist import phrases_original
from character import Character
from phrase import PhraseGenerator


class Game:

    def __init__(self, phrase):
        self.phrase = phrase
        self.number_of_trys = 0
        heading = f"""
                {'~' * 40}
                PHRASE GUESSING GAME!
                {'/' * 40}
                """
        print(heading)
        input("Press Enter to continue")
        instructions = ("\n"
                        "Your job is to guess the phrase\n"
                        "You will be shown the length of the phrase with the letters hidden\n"
                        "Guess a letter: If your letter is in the phrase, you will be shown all the places that your "
                        "letter appears\n "
                        "               If your letter is not in the phrase, you will be given a strike\n"
                        "                If you guess the phrase incorrectly, you will be given a strike\n"
                        "                If you wish to guess the phrase, enter solve\n"
                        "                If your guessed phrase is incorrect, you will be given a strike\n"
                        "Guess the phrase correctly before you receive 5 strikes.  \n"
                        "If you do, You win!\n"
                        "if you don't, You're a loser!\n")
        print(instructions)
        input("Press Enter to continue")
        self.letter_guesser()

    @staticmethod
    def is_letter(test_string):
        letter = re.match(r'^[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+$', test_string)
        if letter is None:
            raise ValueError
        # adapted from Martin Thoma on stack overflow
        # https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python

    def search_phrase(self, string, letter):
        match = [self.phrase.start() for _ in re.finditer(letter, string)]
        return match

    def letter_guesser(self):
        letters_guessed = []
        display_phrase = f"""
        Your phrase is:
        {self.phrase} 
        """
        print(display_phrase)
        while True:
            letter_guessed = input('Guess a letter:  ')
            try:
                letter_guessed = self.is_letter(letter_guessed)
                if letter_guessed != 'SOLVE'.lower() and len(letter_guessed) > 1:
                    raise ValueError
            except ValueError:
                print("That is not a letter")
                continue

            # need to make sure that I accept letter or phrases

            if letter_guessed is not None:
                character_indices = self.search_phrase(self.phrase, letter_guessed)
                Character(self.phrase).replace_character(letter_guessed, character_indices)

            elif letter_guessed == "SOLVE".lower():
                self.phrase_guesser()

            elif letter_guessed is None:
                self.number_of_trys += 1
                letters_guessed.append(letter_guessed)
                letters_guessed = ' ,'.join([letter for letter in letters_guessed])
                print('Sorry, there is no {}'.format(letter_guessed))
                print('So far you have guessed {}'.format(' ,'.join(letters_guessed)))

            elif self.number_of_trys >= 5:
                print("You're a loser")
                self.play_again()

    def phrase_guesser(self):
        guessed_phrase = input('complete the phrase:   ')
        if guessed_phrase == self.phrase:
            print('You win!')
            self.play_again()

        else:
            print('incorrect')
            self.number_of_trys += 1

    @staticmethod
    def play_again():
        again = input('Would you like to play again? [y]es or [n]o.    ')
        if again == ('NO'.lower()) or again == ('N'.lower()):
            sys.exit('Good day')

        elif again == ('YES'.lower()) or again == ('Y'.lower()):
            Game.reset()

    @classmethod
    def reset(cls):
        pass


if __name__ == "__main__":
    Game(PhraseGenerator(phrases_original))

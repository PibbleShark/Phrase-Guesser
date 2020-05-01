import sys
import re
import copy
from phraselist import phrases_original
from character import Character
from phrase import PhraseGenerator


class Game:

    def __init__(self, phrase):
        self.phrase = phrase
        self.number_of_trys = 0
        heading = f"""
                {'~' * 41}
                {'<' * 9} PHRASE GUESSING GAME! {'>' * 9}
                {'~' * 41}
                """
        print(heading)
        input("Press Enter for instructions")
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
        if len(test_string) > 1:
            raise ValueError
        else:
            letter = re.match(r'^[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+$', test_string)
        if letter is None:
            raise ValueError
        return test_string
        # adapted from Martin Thoma on stack overflow
        # https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python

    @staticmethod
    def search_phrase(letter, string):
        match = [character.start() for character in re.finditer(letter.lower(), string.lower())]
        return match

    def letter_guesser(self):
        letters_guessed = []
        display_phrase = Character(self.phrase).display_length()
        new_display_phrase = copy.copy(display_phrase)

        while True:

            print(f"""
                    Your phrase is:
                    {new_display_phrase} 
                    """)

            letter_guessed = input('Guess a letter:  ')

            if letter_guessed == "SOLVE".lower():
                self.phrase_guesser()
                continue

            try:
                letter_guessed = self.is_letter(letter_guessed)
            except ValueError:
                print("That is not a letter")
                continue

            try:
                if letter_guessed in letters_guessed:
                    raise ValueError
            except ValueError:
                print("You have already guessed that letter")
                continue

            character_indices = self.search_phrase(letter_guessed, self.phrase)

            if not character_indices:
                self.number_of_trys += 1
                if self.number_of_trys == 5:
                    print("You're a loser")
                    self.play_again()
                else:
                    letters_guessed.append(letter_guessed)
                    print('Sorry, there is no {}'.format(letter_guessed.upper()))
                    print('Incorrect guessed letters: {}'.format(','.join(letters_guessed)))

            elif character_indices:
                print("Yes, {} is in your phrase".format(letter_guessed.upper()))
                print('Incorrect guessed letters: {}'.format(','.join(letters_guessed)))
                new_display_phrase = Character(new_display_phrase).replace_character(letter_guessed, character_indices)
                if new_display_phrase == self.phrase:
                    print('You win!')
                    self.play_again()
                else:
                    continue

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
        Game(PhraseGenerator(phrases_original).rand_phrase())


if __name__ == "__main__":
    Game(PhraseGenerator(phrases_original).rand_phrase())

import sys
import copy
from phraselist import phrases_original
from character import Character
from phrase import Phrase


class Game:
    import random

    def __init__(self, phrase_list):
        self.phrase = self.random.choice(phrase_list)
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

    def letter_guesser(self):
        incorrect_letters = []
        display_phrase = Phrase(self.phrase).display_length()
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
                letter_guessed = Character(letter_guessed).is_letter()
            except ValueError:
                print("That is not a letter")
                continue

            try:
                if letter_guessed in incorrect_letters:
                    raise ValueError
            except ValueError:
                print("That was not right the first time")
                continue

            try:
                if letter_guessed in new_display_phrase:
                    raise ValueError
            except ValueError:
                print("You have already guessed that letter")
                continue

            character_indices = Character(letter_guessed).search_phrase(self.phrase)
            Character(letter_guessed)
            # here I store the letter.  This is because the assignment asked me to store the letter.
            # the search function that I created doesn't require such a list.

            if not character_indices:
                incorrect_letters.append(letter_guessed)
                self.number_of_trys += 1
                if self.number_of_trys == 5:
                    print("You're a loser")
                    self.play_again()
                else:
                    print('Sorry, there is no {}'.format(letter_guessed.upper()))
                    print('Incorrect guessed letters: {}'.format(Character.display_letter_string(incorrect_letters)))

            elif character_indices:
                print("Yes, {} is in your phrase".format(letter_guessed).upper())
                new_display_phrase = Character(letter_guessed).replace_character(new_display_phrase, character_indices)
                if new_display_phrase == self.phrase.lower():
                    print('You win!')
                    self.play_again()
                else:
                    print('Incorrect guessed letters: {}'.format(Character.display_letter_string(incorrect_letters)))
                    continue

    def phrase_guesser(self):
        guessed_phrase = input('complete the phrase:   ')
        if guessed_phrase == self.phrase.lower():
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
        Game(phrases_original)


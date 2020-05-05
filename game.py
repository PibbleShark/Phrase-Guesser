import sys
from phraselist import phrases_original
from character import Character
from phrase import Phrase


# noinspection PyUnboundLocalVariable
class Game:
    import random

    def __init__(self, phrase_list):
        self.phrase = self.random.choice(phrase_list)
        self.number_of_tries = 5

    def begin_game(self):
        heading = f"""
                {'~' * 41}
                {'<' * 9} PHRASE GUESSING GAME! {'>' * 9}
                {'~' * 41}
                """
        print(heading)
        see_instructions = input("enter 'i' for instructions or press enter to continue").lower()

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

        if see_instructions == 'i':
            print(instructions)
            input("Press Enter to continue")
            self.letter_guesser()
        else:
            self.letter_guesser()

    def letter_guesser(self):

        loop_phrase = Phrase(self.phrase).display_length
        while True:

            already_guessed = 'guessed letters: '

            print(f"""
                    Your phrase is:
                    {loop_phrase.capitalize()} 
                    you have {self.number_of_tries} guesses remaining
                    {already_guessed}{', '.join(Character.incorrect_characters).upper()}
                    """)

            letter_guessed = input('Guess a letter:  ')

            if letter_guessed == "SOLVE".lower():
                answer = Phrase(self.phrase).phrase_guesser()
                if answer:
                    self.play_again()
                else:
                    self.number_of_tries -= 1
                    continue
            try:
                Character(letter_guessed).validate_input()
            except ValueError as err:
                print(err)
                continue

            else:
                character_indices = Character(letter_guessed).search_phrase(self.phrase)

            if not character_indices:
                Character(letter_guessed).incorrect_characters_append()
                self.number_of_tries -= 1
                if self.number_of_tries == 0:
                    print("You're a loser")
                    self.play_again()
                else:
                    print('Sorry, there is no {}'.format(letter_guessed.upper()))

            elif character_indices:
                Character(letter_guessed).correct_characters_append()
                print("Yes, {} is in your phrase".format(letter_guessed.upper()))
                loop_phrase = Character(letter_guessed).replace_character(loop_phrase, character_indices)
                if Phrase(self.phrase).phrase_match(loop_phrase):
                    self.play_again()

    def play_again(self):
        while True:

            again = input('Would you like to play again? [y]es or [n]o.    ').lower()
            if again == ('NO'.lower()) or again == ('N'.lower()):
                sys.exit('Good day')

            elif again == ('YES'.lower()) or again == ('Y'.lower()):
                self.reset()

            else:
                print('that is not a valid entry')

    @staticmethod
    def reset():
        new_game = Game(phrases_original)
        return new_game.begin_game()

    # play again or reset is not working properly

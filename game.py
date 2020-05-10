import sys
import random
from phraselist import phrases_original
from character import Character
from phrase import Phrase


class Game:
    """Game stores a list of phrases as Phrase objects.  It chooses a phrase at random to use in the running of the game.
    It handles taking an input, checking that it is an acceptable.  Once the other phrase class has checked the input
    for correctness, the game class either continues to loop though the game or it allows the phrase class to declare
    a win.  An option to play again either ends the program or performs a reset."""

    def __init__(self, phrases):
        self.phrases = [Phrase(phrase) for phrase in phrases]
        self.number_of_tries = 5
        self.selected_phrase = random.choice(self.phrases)

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
        incorrect_guesses = []
        while True:
            display_phrase = self.selected_phrase.display_phrase()

            print(f"""
                    Your phrase is:
                    {display_phrase} 
                    Attempts Remaining: {'X' * self.number_of_tries}
                    Guessed Letters: {', '.join(incorrect_guesses)}
                    """)

            letter_guessed = input('Guess a letter:  ')

            if letter_guessed.lower() == "SOLVE".lower():
                guessed_phrase = input('Guess the phrase:  ')
                answer = self.selected_phrase.phrase_guess(guessed_phrase)
                if answer:
                    print('You win')
                    self.play_again()
                else:
                    print('Incorrect')
                    self.number_of_tries -= 1
                    continue

            try:
                if len(letter_guessed) > 1:
                    raise ValueError("Looking for a single letter")

                elif not letter_guessed.isalpha():
                    raise ValueError("That is not a letter")

                elif letter_guessed.upper() in incorrect_guesses:
                    raise ValueError("That was not right the first time")

                elif letter_guessed in display_phrase:
                    raise ValueError("You have already guessed that letter")
            except ValueError as err:
                print(err)
                continue

            match = self.selected_phrase.search_phrase(letter_guessed)

            if match:
                print("Yes, {} is in your phrase".format(letter_guessed.upper()))
                phrase_match = self.selected_phrase.phrase_match()
                if phrase_match:
                    print('You completed the phrase and won!')
                    self.play_again()

            else:
                self.number_of_tries -= 1
                incorrect_guesses.append(letter_guessed.upper())
                if self.number_of_tries == 0:
                    print("You're a loser")
                    self.play_again()
                else:
                    print('Sorry, there is no {}'.format(letter_guessed.upper()))

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
        Character.correct_characters = []
        new_game = Game(phrases_original)
        return new_game.begin_game()

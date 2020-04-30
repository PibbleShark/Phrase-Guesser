import re
import phrase
from character import Character
import phraselist


class Game:

    def __init__(self, phrase):
        self.phrase = phrase
        self.number_of_trys = 0
        answer_not_solved = True
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
                        "Guess a letter: If your letter is in the phrase, you will be shown all the places that your letter appears\n"
                        "                if your letter is not in the phrase, you will be given a strike\n"
                        "                if you guess the phrase incorrectly, you will be given a strike"
                        "Guess the phrase correctly before you receive 5 strikes.  \n"
                        "If you do, You win!\n"
                        "if you don't, You're a loser!\n")
        print(instructions)
        input("Press Enter to continue")

    def is_letter(self, test_string):
        letter = re.match(r"^[abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]+$", test_string)
        return letter is not None
        # suggested by Martin Thoma on stack overflow
        # https://stackoverflow.com/questions/18667410/how-can-i-check-if-a-string-only-contains-letters-in-python

    def search_phrase(self, phrase, letter):
        match = [self.phrase.start() for _ in re.finditer(letter, phrase)]
        return match

    def run_game(self):
        global letter_guessed
        disp_phrase = f"""
        Your phrase is:
        {self.phrase} 
        """
        print(disp_phrase)
        while True:
            letter_guessed = input('Guess a letter:  ')
            try:

                letter_guessed = self.is_letter(letter_guessed)
            except ValueError:
                print("That is not a letter")
                continue

            # need to make sure that I accept letter or phrases

            if letter_guessed is not None:
                try:
                    #see if guess is correct
                    #else search and redisplay
                    #add a try
                Character(self.phrase).replace_character(letter_guessed,
                                                         self.search_phrase(self.phrase, letter_guessed))

# Unit-3
 Phrase guessing game
 
 phraselist.py is just a list of phrases that my program will use
    it can be changed if we would like to add or subtract phrases from the game
    
 phrase.py contains the class PhraseGenerator.  It takes a list and can choose a random string from it.  It's output is a string.
 
 caracter.py contains the class Character.  I can use it to display my phrase as a series of underscores that represent the length of the phrase.  It also has a method to take the class argument string and output a new string with its characters altered based on a list of indices.
 
 game.py contains the execution of the game in the class Game.  It primarily consists of a while loop that takes letters and determines if they are in the generated phrase.  It allows you to win by trying to solve the puzzle or by filling in all of the letters.  It contains a static method that checks if input is a single letter using a regex match.  It contains another static function that returns a list of indices representing the locations of any input letter in a string.  I have also created a method for solving the puzzle and a class method to reset the class and play again.     

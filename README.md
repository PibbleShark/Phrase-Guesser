# Unit-3
 Phrase guessing game
 
phraselist.py is just a list of phrases that my program will use it can be changed if we would like to add or 
subtract phrases from the game
    
phrase.py contains the class Phrase.  Phrase takes a phrase, converts it into a set of Character objects and can turn
it into a string of underscores to hide the letters it contains.
It also is used to check for a correct answer in the phrase guessing game.
 
character.py contains the class Character.  Character takes a character and stores it.  It can then check that a 
character is a single letter and stores guessed letters as correct or incorrect.  It also has a method for 
displaying a correctly guessed letter in the string of underscores created by the Phrase class

game.py contains the class Game.  Game takes the components of the Character and Phrase classes and runs through the
steps of the guessing game.  It also contains a function to reset the game to play again
  
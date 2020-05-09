# Unit-3
 Phrase guessing game
 
phraselist.py is just a list of phrases that my program will use it can be changed if we would like to add or 
subtract phrases from the game
    
phrase.py contains the class Phrase.  Phrase takes a phrase, converts it into a set of Character objects and can display
the characters.  It has a method to see if a given character is present in the phrase.
It also is used to check for a correct answer in the phrase guessing game.
 
character.py contains the class Character.  Character takes a character and stores it. It works with the Phrase class to
store correctly guessed letters.  A character object will display as an _ until that character has been correctly guessed.

game.py contains the class Game.  Game takes the components of the Character and Phrase classes and runs through the
steps of the guessing game.  It also contains a function to reset the game to play again
  
# Unit-3
 Phrase guessing game
 
 phraselist.py is just a list of phrases that my program will use
    it can be changed if we would like to add or subtract phrases from the game
    
 phrase.py contains the class Phrase.  It takes a phrase an converts it into a series of underscores that correspond to the letters in the phrase. 
 
character.py includes all of my logic dealing with the individual characters in the program.  It includes a method to check if a letter guessed is a letter.  It also has logic to iterate through a string and return indices in which a character is can be found.  

game.py contains the operation of the game which is mostly contained in one while loop.  Since my function returns indices of the location of a letter in the string, I use conditional statements to check if those indices are preset rather than using a boolean statement.  It keeps a running list of tries and failed guesses as well as updates my displayed string with the correctly guessed letters. It also include methods to guess the phrase and a method to restart the game.  
  
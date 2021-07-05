# Problem 1 - Is the Word Guessed
# 10.0/10.0 points (graded)
# Please read the Hangman Introduction before starting this problem. We'll start by writing 3 simple functions that will
# help us easily code the Hangman problem. First, implement the function isWordGuessed that takes in two parameters - a
# string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - True if secretWord has
# been guessed (ie, all the letters of secretWord are in lettersGuessed) and False otherwise.

#Example Usage:

#>>> secretWord = 'apple'
#>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
#>>> print(isWordGuessed(secretWord, lettersGuessed))
#False

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
lettersGuessed1 = ['a', 'l', 'p', 'l', 'e', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
            return False
            break
    return True

print(isWordGuessed(secretWord, lettersGuessed))
print(isWordGuessed(secretWord, lettersGuessed1))
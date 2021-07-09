# Exercise: guess my number
# In this problem, you'll create a program that guesses a secret number!
# The program works as follows: you (the user) thinks of an integer between 0 (inclusive) and 100 (not inclusive). The
# computer makes guesses, and you give it input - is its guess too high or too low? Using bisection search, the computer
# will guess the user's secret number!

# Here is a transcript of an example session:
# >> Please think of a number between 0 and 100!
# >> Is your secret number 50?
# >> Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I
#    guessed correctly. l
# >> Is your secret number 75?
# >> Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I
#    guessed correctly. l
# etc.

#while numGuesses > 0:
#    print("You have " + str(numGuesses) + " guesses left.")
#    print("Available Letters: " + getAvailableLetters(lettersGuessed))
#    l = input("Please guess a letter: ")

print("Please think of a number between 0 and 100!")
numGuess = 50
minGuess = 0
maxGuess = 100

userInput = ''
while userInput != 'c':
    print("Is your secret number " + str(numGuess) + "?")
    userInput = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. " +
                      "Enter 'c' to indicate I guessed correctly. ")


    if userInput == 'h':
        maxGuess = numGuess
        numGuess = int((numGuess + minGuess) / 2)
    elif userInput == 'l':
        minGuess = numGuess
        numGuess = int((numGuess + maxGuess) / 2)
    elif userInput == 'c':
        print("Game over. Your secret number was: " + str(numGuess))
    else:
        print("Sorry, I did not understand your input.")


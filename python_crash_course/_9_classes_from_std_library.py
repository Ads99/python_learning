from collections import OrderedDict
from random import randint

favourite_languages = OrderedDict()

favourite_languages['jen'] = 'python'
favourite_languages['sarah'] = 'c'
favourite_languages['edward'] = 'ruby'
favourite_languages['phil'] = 'python'

for name, language in favourite_languages.items():
	print(name.title() + "'s favourite language is " +
		language.title() + ".")

# Exercise 9.13 - OrderedDict Rewrite
# Start with Exercise 6-4, where you used a standard dictionary to represent a
# glossary. Rewrite the program using the OrderedDict class.
glossary = OrderedDict()

glossary['if'] = 'conditional keyword, used to validate an assumption'
glossary['elif'] = 'used within an "if" statement'
glossary['dunder'] = 'haven\'t learnt this one yet'

for word, meaning in glossary.items():
    print(word + ": " + meaning + ".")
print("\n")

# Exercise 9.14 - Dice
# The module 'random' contains functions that generate random numbers in a
# variety of ways. The function randint() returns an integer in the range you
# provide.
# 1) Make a class Die with one attribute called sides, which has a default
# value of 6.
# 2) Write a method called roll_die() that prints a random number between 1 and
# the number of sides the die has.
# 3) Make a 6-sided die and roll it 10 times.
# 4) Make a 10-sided die and a 20-sided die. Roll each die 10 times.

class Die():
    """A simple attempt to model a Die"""

    def __init__(self, sides=6):
        """Initialise the number of sides"""
        self.sides = sides

    def roll_die(self):
        print("The number rolled is : " + str(randint(1,self.sides)))


die1 = Die()
print("Testing a 6-sided die:")
for i in range(0,10):
    die1.roll_die()

print("\nTesting a 10-sided die:")
die2 = Die(10)
for i in range(0,10):
    die2.roll_die()

print("\nTesting a 20-sided die:")
die3 = Die(20)
for i in range(0,10):
    die3.roll_die()
file_path = '/Users/adambaker/Documents/GitHub/python_learning/' \
            'python_crash_course/_10_pi_digits.txt'

#with open('_10_pi_digits.txt') as file_object:
with open(file_path) as file_object:
    contents = file_object.read()
    print(type(contents))
    print(contents.rstrip())

# Looping through each line
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing the lines inside a list for later use
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

# Working with a File's contents
pi_string = ''
for line in lines:
    #pi_string += line.rstrip() # this doesn't work as it only stips whitespace from rhs
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# Reading 1M digits of pi
filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:52] + '...')
print(len(pi_string))

# Is Your Birthday Contained in Pi?
#birthday = input("Enter your birthday, in the form ddmmyy: ")
birthday = '040683'
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")

# Exercise 10.1 - Learning Python
print("Method A: reading the entire file:")
filename = '_10_learning_python.txt'
with open(filename) as file_object:
    contents = file_object.read()
    print("file_object contents is of type: " + str(type(contents)))
    print(contents.strip())

print("\nMethod B: looping over the file object:")
with open(filename) as file_object:
    for line in file_object:
        print(line.strip())

print("\nMethod C: storing lines in a list and working with these outside 'with':")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Exercise 10.2 - Learning C
# Use string replacement methods to change 'python' to 'C'
for line in lines:
    print(line.strip().replace('Python', 'C'))

# Exercise 10.3 - Guest
# Write a program that prompts the user for their name. When they respond,
# write their name to a file called guest.txt
#name = input("Please enter your name:\n")
name = 'Esme Wren'
file_name = '_10_name.txt'

with open(file_name, 'a') as file_object:
    file_object.write(name + ".\n")

# Exercise 10.4 - Guest Book
# Write a while loop that prompts the user for their name. When they enter their
# name, print a greeting to the screen and add a line recording their visit in a
# file called guest_book.txt. Make sure each entry appears on a new line
#print("\nGuess Book Exercise")
#prompt = "Enter your name for the guest book:\n"
#prompt += "Enter 'quit' to exit the program.\n"
#file_name = "_10_guest_book.txt"
#guest_name = ""

#while guest_name != 'quit':
#    guest_name = input(prompt)
#    with open(file_name, 'a') as file_object:
#        file_object.write(guest_name + "\n")

# Handling Exceptions with try/catch
print("")

# Exercise 10.6 - Addition
# Handling text but expecting numbers and getting a TypeError
# Write a program that prompts for two numbers, add them together and print the
# result. Catch the TypeError if either value is not a number.
print("Give me two numbers and I'll add them together.")
print("Enter 'q' to quit.")

"""while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except TypeError:
        print("You can only add numbers!")
    else:
        print(answer)"""

def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + " does not exist."
        print(msg)
    else:
        # Count approximate number of words in the file.
        words = contents.split()
        #print(words[0:10])
        num_words = len(words)
        print("The file " + filename + " has about " + str(num_words) +
            " words.")

filename = './_10_book_files/alice.txt'
count_words(filename)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for f in filenames:
    file_path = './_10_book_files/' + f
    count_words(file_path)

# Exercise 10.8 - Cats and Dogs
# Make two files, cats.txt and dogs.txt. Store at least three names of cats in
# the first file and three names of dogs in the second file. Write a program
# that tries to read these files and print the contents of the file to the
# screen. Wrap your code in a try-except block to catch the FileNotFound error
# and print a friendly message if a file is missing. Move one of the files to a
# different location on your system and make sure the code in the except block
# executes properly.
def list_animals(filename):
    """Print the animal names to the terminal."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = "Sorry, couldn't find the file: " + filename
        #print(msg)
        pass
    else:
        # Print the contents of the file
        print(contents)


filenames = ['_10_cats.txt', '_10_dogs.txt']
for f in filenames:
    list_animals(f)

# Exercise 10.10 - Common Words
# Use the count() method to find out how many times a word or phrase appears in 
# text from a book
def count_words(filename, phrase):
    """Count the number of times a given phrase appears in the text"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except:
        print("Couldn't open the file: " + filename)
    else:
        count = contents.lower().count(phrase)
        msg = "The file: '" + filename + "' contains the phrase '" + phrase
        msg += "' " + str(count) + " times"
        print(msg)

filename = './_10_book_files/moby_dick.txt'
phrase = 'moby dick'
count_words(filename, phrase)

# Using json.dump() and json.load()
import json

numbers = [2, 3, 5, 7, 11, 13]

filename = '_10_numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)

# Reading the json file back into memory
filename = '_10_numbers.json'
with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)
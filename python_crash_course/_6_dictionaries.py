# Playing around with dictionaries
alien_0 = {'color' : 'green', 'points' : 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# We can also start with an empty dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# Modifying values in a dictionary
alien_0 = {'color' : 'green'}
print("The alien is " + alien_0['color'] + ".")
alien_0 = {'color' : 'yellow'}
print("The alien is now " + alien_0['color'] + ".")

# a more interesting example
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right. 
# Determine how far the move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))

# Removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del(alien_0['points'])
print(alien_0)

favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("Sarah's favourite language is " +
    favourite_languages['sarah'].title() +
    ".")

# Exercise 6.1 - Person
# Use a dict to store information about a person you know including:
# first_name, last_name, age, city
esme = {'first_name': 'esme', 'last_name': 'baker', 'age':2, 'city':'leamington spa'}
for i in esme:
    print(i + ": " + str(esme[i]).title())

# Exercise 6.2 - Favourite Numbers
# Assign a favourite number to each person
numbers = {'adam': 4, 'lauren': 25, 'esme':6, 'lynn':1, 'craig':13}
for name in numbers:
    print(name + ": " + str(numbers[name]))

# Exercise 6.3 - Glossary
# Use 5 programming words as key, store their meanings as values
glossary = {'if': 'conditional keyword, used to validate an assumption',
            'elif': 'used within an "if" statement',
            'dunder': 'havent\'t learnt this one yet'
}
for word in glossary:
    print(word + ": " + "\n\t" + glossary[word])

# Another looping example - using a dictionary's 'items()' method
for key, value in glossary.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name, language in favourite_languages.items():
    print(name.title() + "'s favourite language is " + 
        language.title() + ".")

# Looping through keys of a dictionary:
for name in favourite_languages.keys():
    print(name.title())

print("\n")

# Equivalently, the default behaviour when looping through a dictionary is to
# loop through the keys
for name in favourite_languages:
    print(name.title())

print("\n")

friends = ['phil', 'sarah']
for name in favourite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
            ", I see your favourite language is " +
            favourite_languages[name].title() + "!")

if 'erin' not in favourite_languages.keys():
    print("Erin, please take our poll")

# Return the keys in order from a dictionary
for name in sorted(favourite_languages.keys()):
    print(name.title() + ", thank you for taking the poll")

# Looping through the values of a dictionary
print("The following languages have been mentioned:")
for language in favourite_languages.values():
    print(language.title())

# Notice the repetition above ('Python' is repeated)
# We can use a 'set' (similar to a list, except each item is unique)
for language in set(favourite_languages.values()):
    print(language.title())

print("\n")
# Exercise 6.5 - Rivers: Make a dict containing three major rivers and country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.
rivers = {'nile': 'egypt', 'amazon': 'brazil', 'thames': 'uk'}
for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title())
for river in rivers.keys():
    print(river.title())
for country in sorted(set(rivers.values())):
    print(country.title())

print("\n")
# Exercise 6.6 - Polling: 
# • Make a list of people who should take the favorite languages poll. Include
#   some names that are already in the dictionary and some that are not.
# • Loop through the list of people who should take the poll. If they have
#   already taken the poll, print a message thanking them for responding. If
#   they have not yet taken the poll, print a message inviting them to take poll
names = ['adam', 'phil', 'esme']
for name in names:
    if name in favourite_languages.keys():
        print(name.title() + ", thanks for taking the poll")
    else:
        print(name.title() + ", please take the poll")

# Nesting
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")
# Show how many aliens have been created:
print("Total number of aliens: " + str(len(aliens)))
print("\n")

# Exercise 6.7 - People:
#  Make two new dictionaries representing different people and store all three
#  dictionaries in a list called people. Loop through your list of people.
#  As you loop through the list, print everything you know about each person.
lauren = {'first_name': 'lauren', 'last_name': 'baker', 'age':35, 'city':'leamington spa'}
mum = {'first_name': 'lynn', 'last_name': 'baker', 'age':65, 'city':'barnard castle'}
people = [esme, lauren, mum]
for person in people:
    print(person)

# Exercise 6.8 - Pets:
#  Make several dictionaries, where the name of each dictionary is the name of a
#  pet. In each, include the kind of animal and the owner’s name. Store these
#  dictionaries in a list called pets. Next, loop through your list and as you
#  do print everything you know about each pet.
daisy = {"type": "cat", "owner": "Adam", "age": 9}
albie = {"type": "dog", "owner": "Alex", "age":8}
rory = {"type": "pig", "owner": "Mr Pig Man", "age":2}
pets = [daisy, albie, rory]
for pet in pets:
    for key, value in pet.items():
        print(key + ": " + str(value))
    print("\n")

# Exercise 6.9 - Favourite Places:
# Make dict 'favorite_places'. Use 3 names to use as keys and store one to three
# favorite places for each person. Loop and print each person’s name and their
# favorite places
favourite_places = {
    "adam": ["santa marta", "tayrona", "amalfi"],
    "lauren": ["leamington spa", "buenos aires"],
    "esme": ["gran canaria", "elounda"]
    }
for name, fav in favourite_places.items():
    print(name.title() + "'s favourite places are: ")
    for place in fav:
        print(place.title())
    print("\n")

# Exercise 6.10 - Favorite Numbers:
# Modify program from Exercise 6.2 so each person can have > 1 favorite number.
# Print each person’s name along with their favorite numbers
numbers['adam'] = [4, 3, 6]
numbers['lauren'] = [69, 82]
numbers['esme'] = [6, 5]
for name, numberList in numbers.items():
    print(name.title() + "'s favourite numbers: " + str(numbers[name]))
    # More convluted way of doing this
    #if type(numberList) == list:
    #    for n in numberList:
    #        print(str(n))
    #else:
    #    print(str(numberList))

# Exercise 6.11 - Cities:
# Make a dictionary called cities. Use the names of three cities as keys.
# Create a dictionary of information about each city, include country, population
# and one fact about that city. The keys for each city’s dictionary should be
# something like country, population, and fact. Print the name of each city
# and all of the information you have stored about it.
print("\n")
cities = {
    "london": {"country": "UK", "pop": 8000000, "fact": "largest in UK"},
    "leamington": {"country": "UK", "pop": 60000, "fact": "one of 3 spa towns"}
    }
for city, details in cities.items():
    print(city.title() + ": " + str(cities[city]))
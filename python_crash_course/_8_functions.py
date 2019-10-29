def greet_user(username):
	"""Display a simple greeting."""
	print("Hello, " + username.title() + "!")

greet_user("adam")

# Exercise 8.1 - Message
def display_message():
    print("You are learning about functions in this chapter.")

display_message()

# Exercise 8.2 - Favourite Book
def favourite_book(title):
    print("One of my favourite titles is: " + title.title())

favourite_book("alice in wonderland")

# Positional arguments
def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('cat', 'misty')

# However, order matters in positional arguments
describe_pet('misty', 'cat')

# Keyword arguments - resolve the above issue
describe_pet(animal_type='cat', pet_name='misty')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
    """Displays information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + '.')

describe_pet('jess')
describe_pet('joey', 'hamster')

# NOTE: when you have default values, any parameter with a default value needs
# to be listed after all the parameters that don't have default values. This
# allows Python to continue interpreting positional arguments correctly

# Exercise 8.3 - T-Shirt
# Write a function make_shirt() that accepts a size and the text of a message
# that should be printed on the shirt. The function should print a sentece
# summarizing the size of the shirt and the message printed on it
def make_shirt(size, message):
    print("Shirt size : " + str(size) + "\nMessage: " + str(message))

make_shirt("medium", "Beastie Boys: Paul's Boutique")
make_shirt(36, "Four Tet: Live at Roundhouse")

# Exercise 8.4 - Large Shirts
# Modify the above so that shirts are large by default, with a default message
def make_shirt(size='Large', message='I Love Python'):
    print("Shirt size : " + str(size) + "\nMessage: " + str(message))

make_shirt()
make_shirt("Medium")
make_shirt("Small", "I Love Dogs")

# Return Values - a simple example
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
# print(get_formatted_name('jimi', 'hendrix'))

# Making an argument optional
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
    
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# Returning a dictionary
def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)

# Using a Function with a while Loop
# NB. This is an infinite loop!
"""
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")
"""

# Exercise 8.6 - City Names
# Write a function called city_country() that takes the name of a city and its
# country. 
def city_country(city, country):
    ### Return a City, Country combination """
    full_location = city + ", " + country
    return full_location.title()

location = city_country('london', 'uk')
print(location)
location = city_country('santiago', 'chile')
print(location)

# Exercise 8.7 - Album
# Write a function make_album() that builds a dictionary describing a music 
# album. The function should take an artist name and album title, and return a
# dictionary containing these two pieces of info.
# Add an optional parameter that allows you to store the number of tracks
def make_album(artist, album, tracks = ''):
    album_details = {'artist': artist.title(), 'album': album.title()}
    if tracks:
        album_details['track_count'] = int(tracks)
    return album_details
a1 = make_album('prodigy', 'music for the jilted generation')
print(a1)
a2 = make_album('groove armada', 'lovebox', 22)
print(a2)

# Passing a List
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# Modifying a List in a Function
# Star with some designs that need to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each deign, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # Simulate creating a 3D print from the design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# We can reorganise the above by writing two functions, each of which does one
# specific job

# Function 1 : handle the printing of the designs
def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        # Simulate creating a 3D print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)

# Function 2 : summarize the prints that have been made
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a Function from Modifying a List (you may want to keep the original
# list)
print_models(unprinted_designs[:], completed_models)

# Exercise 8.9 - Magicians
# Make a list of magician's names. Pass the list to a function called
# show_magicians(), which prints the name of each magician in the list
magicians = ['paul daniels', 'david blaine']
def show_magicians(magicians):
    for magician in magicians:
        print(magician.title())
show_magicians(magicians)

# Exercise 8.10 - Great Magicians
# Based on 8.9, create function called make_great() that modifies the list of
# magicians by adding the phrase "the Great" to each name.
great_magicians = []
def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        magician = magician.title() + ", the Great!"
        great_magicians.append(magician)
make_great(magicians, great_magicians)
print(great_magicians)
print(magicians)

# Exercise 8.11 - Unchanged Magicians
# Call the same function with a copy of the list of magician's names so that the
# original list will remain unchanged, return the new list and store it in a
# separate list
magicians = ['paul daniels', 'david blaine']
great_magicians = []
make_great(magicians[:], great_magicians)
print(great_magicians)
print(magicians)

# Passing an Arbitrary Number of Arguments
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Mixing Positional and Arbitrary Arguments
# If you want a function to accept several different kinds of arguments, the 
# parameter that accepts an arbitrary number of args must be placed last
def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# Using Arbitrary Keyword Arguments
# You may not know ahead of time what kind of info will be passed to the
# function. You can define function to accept as many key-value pairs as the
# calling statement provides
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
    location='princeton', field='physics')
print(user_profile)
user_profile2 = build_profile('adam', 'baker', daughter='esme')
print(user_profile2)

# Exercise 8.12 - Sandwiches
# Write a function that accepts a list of items a person wants on a sandwich.
# The function should have one parameter that collects as many items as the
# function call provides, and it should print a summary of the sandwich that is 
# being ordered. Call the function 3 times, using different args each time
def show_sandwiches(ingredients):
    print("Sandwich contains: ")
    for i in ingredients:
        print(i)
show_sandwiches(['tuna', 'cucumber'])
show_sandwiches(['chicken', 'chorizo', 'cheese'])

# Exercise 8.13 - User Profile
# Build a user profile, using first and last names and three other key-val pairs
adam_profile= build_profile('adam', 'baker', daugher='esme', wife='lauren',
    cat='daisy')
print(adam_profile)

# Exercise 8-14 - Cars
# Write a function that stores information about a car in a dictionary. The
# function should always receive a manufacturer and a model name. It should then
# accept an arbitrary number of keyword arguments
def make_car(manufacturer, model, **car_details):
    # Build a dictionary containing every detail relating to the car
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_details.items():
        car[key] = value
    return car
car = make_car('subaru', 'impreza', colour='blue', year=1999)
print(car)
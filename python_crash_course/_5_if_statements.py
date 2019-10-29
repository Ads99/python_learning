# Checking whether a value is in a list
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('egg' in requested_toppings)

# Other times we need to check a value isn't in a list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(user.title() + ", you can post a response if you wish")

# Exercise 5-1: Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False")
print(car == 'audi')

# Exsercise 5-2: More Conditional Tests

# a) String tests for equality/inequality
my_string = 'pampelmousse'
print(my_string == 'pampelmousse')
print(my_string == 'oiseaux')
# b) testing title()
print(my_string.title() == 'Pampelmousse')
print(my_string == 'pampelmousse'.title())
# c) numerical tests involving ==, >, <, >=, <=
numero = 6517
print(numero == 6517)
print(numero > 5000)
print(numero < 2000)
print(numero >= 4500)
print(numero <= 6517)
# d) using 'and' and 'or' keywords
print(numero > 5000 and numero < 10000)
print(numero > 5000 or numero < 100)

# Exercise 5-3. Alien Colors #1:
# Imagine an alien was just shot down in a game . Create a variable called
# alien_color and assign it a value of 'green', 'yellow', or 'red'
# • Write an if statement to test whether the alien’s color is green. If it is,
#   print a message that the player just earned 5 points
# • Write one version of this program that passes the if test and another that
#   fails . (The version that fails will have no output)
alien_color = 'yellow'
if alien_color == 'green':
    print("You just earned 5 points!")
elif alien_color == 'yellow':
    print("You just earned 2 points!")

# Exercise 5-6: Stages of Life:
# Set a value for the variable age, and then:
# • If less than 2 years old, print a message that the person is a baby
# • If at least 2 years old but less than 4, print that the person is a toddler
# • If at least 4 years old but less than 13, print that the person is a kid
# • If at least 13 years old but less than 20, print that the person is a teenager
# • If at least 20 years old but less than 65, print that the person is an adult
# • If 65 or older, printthat the person is an elder
age = 68
if age < 2:
    age_category = "baby"
elif age >= 2 and age < 4:
    age_category = "todller"
elif age >= 4 and age < 13:
    age_category = "kid"
elif age >= 13 and age <20:
    age_category = "teenager"
elif age >= 20 and age < 65:
    age_category = "adult"
elif age >= 65:
    age_category = "elder"

print("The person is a: " + age_category)

# Checking whether a list is empty
# When the name of a list is used in an if statement, Python returns 'True' if
# the list is not empty
requested_toppings = []
if requested_toppings:
    for i in requested_toppings:
        print("Adding: " + i + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you'd like an empty pizza?")

# Comparing multiple lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding:" + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza!")

print("\n\n")

# Exercise 5-8: Hello Admin
user_names = ['rory', 'adam', 'elwood', 'admin']
if user_names:
    for user_name in user_names:
        if user_name == 'admin':
            print("Hello admin, would you like to see a special status report?")
        else:
            print("Hello, " + user_name + ", thank you for logging in again")
else:
    print("We need to find some users!")

# Delete all users from user_names list
del(user_names[:])
if user_names:
    print("Username list has values")
else:
    print("We need to find some users!")

# Exercise 5-10: Checking Usernames:
# • Make a list of five or more usernames called current_users
# • Make another list of five usernames called new_users. Make sure one or two
#   of the new usernames are also in the current_users list
# • Loop through the new_users list to see if each new username has already been
#   used. If it has, print a message that the person will need to enter a new
#   username . If a username has not been used, print a message saying that the
#   username is available
# • Make sure your comparison is case insensitive . If 'John' has been used,
#   'JOHN' should not be accepted
current_users = ['rory', 'adam', 'elwood', 'pinkerton', 'sally']
new_users = ['apple', 'fife dog', 'q-tip', 'sally', 'rory']
for new_user in new_users:
    if new_user in current_users:
        print("Username: " + new_user + " is unavailable")
    else:
        print("Username: " + new_user + " is available to use")

# Exercise 5-11: Ordinal Numbers:
# • Store the numbers 1-9 in a list
# • Loop through the list
# • Use an if-elif-else chain to print the ordinal ending
nList = [val for val in range(1,10)]
for n in nList:
    if n == 1:
        print("1st")
    elif n == 2:
        print("2nd")
    elif n == 3:
        print("3rd")
    else:
        print(str(n) + "th")
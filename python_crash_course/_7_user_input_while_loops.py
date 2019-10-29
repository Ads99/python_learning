message = input("Tell me something: ")
print(str(message))

prompt = "If you tell us who you are, we can pesonalise messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print("\nHello," + str(name) + "!")

# Letting the user choose when to quit
prompt = "\nTell me something, I will repeat:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    
    if message != 'quit':
    	print(message)

# Testing multiple conditions - using a flag
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)

# Use a 'break' statement to immediately exit a while loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Using continue in a Loop
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# Exercise 7.4 - Pizza Toppings
# Ask user to enter a series of pizza toppings until they enter a 'quit' value
# Print a message saying you'll add said topping to pizza
active = True
while active:
    topping = input("Please enter a topping: ")

    if topping == 'quit':
        active = False
    else:
        print("You have added " + str(topping) + " to your pizza")

# Exercise 7.5 - Movie Tickets
# A cinema charges a different price depending on customer's age. Write a loop
# which asks for a user's age and tell them the cost of their ticket
prompt = "How old are you? (type 'quit' to exit): "
message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        if int(message) < 3:
            price = "free"
        elif int(message) >= 3 and int(message) <= 12:
            price = "£10"
        elif int(message) > 12:
            price = "£15"

        print("Your ticket price is : " + price)

# Re-writing this to use a 'break' statement
prompt = "How old are you? (type 'quit' to exit): "
message = ""
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        break
    elif int(message) < 3:
        price = "free"
    elif int(message) >= 3 and int(message) <= 12:
        price = "£10"
    elif int(message) > 12:
        price = "£15"

    print ("Your ticket price is : " + price)


# Using a while Loop with Lists and Dictionaries
# Moving Items from One List to Another

unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into a list of confirmed users
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Removing all instances of specific values from a List
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
print(pets)


# Filling a dictionary with user input
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


# Exercise 7.8 - Deli
# Make a list called sandwich_orders and fill with names of various sandwiches
# Then make a list called finished_sandwiches. Loop through the first list and
# print a message for each order. As each is made, move to the finished list. 
# After all have been made, print a list indicating each sandwich which was made
sandwich_orders = ['BLT', 'club', 'ploughmans', 'prawn mayonnaise']
made_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("I made your " + current_sandwich.title() + " sandwich.")

    made_sandwiches.append(current_sandwich)

print("The following sandwiches have been made: ")
for sandwich in made_sandwiches:
    print(sandwich.title())

# Exercise 7.9 - No Pastrami
# Make sure 'pastrami' appears at least 3 times. Add code to print a message
# saying that the deli has run out of pastrami, then use a while loop to remove
# all occurrences of pastrami from sandwich_orders. 
sandwich_orders = ['BLT', 'pastrami', 'club', 'pastrami', 'ploughmans', 'pastrami', 'prawn mayonnaise']
made_sandwiches = []

if 'pastrami' in sandwich_orders:
    print("We've ran out of pastrami!")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    made_sandwiches.append(current_sandwich)

print("The following sandwiches have been made: ")
for sandwich in made_sandwiches:
    print(sandwich.title())
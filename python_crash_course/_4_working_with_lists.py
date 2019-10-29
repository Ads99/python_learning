pizzas = ['hawaiian', 'marinara', 'pepperoni']
for pizza in pizzas:
    print("I love " + pizza + " pizza")
print("I really, really love pizza")

numbers = range(1,6)
print(type(numbers))
print(numbers)
numbers = list(numbers)
print(type(numbers))
print(numbers)

squares = []
for i in range(1,11):
    i = i**2
    squares.append(i)
print(squares)

# or more concisely
squares = []
for i in range(1,11):
    squares.append(i**2)
print(squares)

# Some statistics work only with a list of numbers
print("Min square number: " + str(min(squares)))
print("Max square number: " + str(max(squares)))
print("Total of square numbers: " + str(sum(squares)))

# List Comprehensions: even more concise way of creating lists
# A LC combines the 'for' loop and the creation of new elements into a single line
squares = [value**2 for value in range(1,11)]
print(squares)

# Exercise 4.3 - count to 20
print([value for value in range(1,21)])

# Exercise 4.4 - list of numbers from 1 to 1M
mil = [value for value in range(1,1000001)]
#print(mil)

# Exercise 4.5 - using min/max/sum to verify list is correct
print(min(mil))
print(max(mil))
print(sum(mil))

# Exercise 4.6 - Odd Numbers from 1 to 20
odd = [value for value in range(1, 21, 2)]
for i in odd:
    print(i)

# Exercise 4.7 - Threes - make a list of multiples of 3 from 3 to 30
threes = [value*3 for value in range(3,31)]
print(threes)

# Exercise 4.8 - Cubes - make a list of first 10 cubes
cubes = [value**3 for value in range(1,11)]
for i in cubes:
    print(i)

# List Slicing
# to slice a list specify the first and last indexes of the list 
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[1:4])

# If you omit the first index, slice starts at start of list
print(players[:4])

# Similarly, omitting the last index assume you want from first index to end of list
print(players[2:])

# Negative index works backwards from end of list
print(players[-3:])

# Can use for list to loop through slices
print("Here are the first 3 players on my team: ")
for i in players[:3]:
    print(i.title())

# Copying a List - you'll often want to make a new list based on an existing one
# To copy a list you can make a slice that includes the entire original list by
# omitting the first and last indexes ([:])
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods
print("My favourite foods are: " + str(my_foods))
print("My friends favourite foods are: " + str(friend_foods))
my_foods.pop()
print(my_foods)
print(friend_foods)
# You can see from the above that these both reference the same underlying object
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]
del(my_foods[0])
print(my_foods)
print(friend_foods)
# Now, these refer to difference objects

# 4-10. Slices:
# • Print the message, "The first three items in the list are: ". Then use a slice to print the first three items from that program’s list
# • Print the message, "Three items from the middle of the list are: ". Use a slice to print three items from the middle of the list
# • Print the message, "The last three items in the list are: ". Use a slice to print the last three items in the list
foods = ['pizza', 'falafel', 'carrot cake', 'ice cream', 'walnuts']

print("The first three items in the list are: " + str(foods[:3]))
print("Three items from the middle of the list are: " + str(foods[1:-1]))
print("The last three items in the list are: " + str(foods[-3:]))

# 4-13. Tuples:
# A buffet-style restaurant offers only five basic foods . Think of five simple foods, and store them in a tuple
# • Use a for loop to print each food the restaurant offers
# • Try to modify one of the items, and make sure that Python rejects the change
# • The restaurant changes its menu, replacing two of the items with different foods
#   Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu

foods = ('chilli', 'bangers & mash', 'burrito', 'sandwich')

for f in foods:
    print(f)

#foods[1] = 'salsa'
#print(foods)

foods = ('chilli', 'fish', 'burrito', 'sandwich')
for f in foods:
    print(f)
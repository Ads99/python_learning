class Dog():
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialise name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")

my_dog = Dog('Jess', 13)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Albie', 8)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

# Exercise 9.1 - Restaurant
# Make a class called 'Restaurant'. It should be initialised using a
# restaurant_name and a cuisine_type. Make a method called describe_restaurant()

class Restaurant():
    """A simple attempt to model a Restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise both attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print("The restaurant's name is: " + self.restaurant_name.title() + ".")
        print("It has a cuisine type of: " + self.cuisine_type.title())

    def open_restaurant(self):
        print("The restaurant is now open!")

    def get_number_served(self):
        print("The restaurant has served " + str(self.number_served) + " people")

print("")
restA = Restaurant("bella donna", "italian")
restA.describe_restaurant()
restA.open_restaurant()
restA.get_number_served()
restA.number_served = 10
restA.get_number_served()

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialise attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage > self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


print("")
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
# Changing an attribute's value (odometer reading):
# Method 1: directly through the instance
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# Method 2: through a Class method
my_new_car.update_odometer(13)
my_new_car.read_odometer()

# Method 3: incrementing an attribute's value through a method
print("")
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())
my_used_car.update_odometer(23500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

# Inheritance
# When you create a child class, the parent class must be part of the current
# file. The name of the parent class must be included in parentheses in the
# definition of the child class
print("")
class ElectricCar(Car):
    """Represents aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def fill_gas_tank():
        """Electric cars don't have gas tanks"""
        print("This car doesn't need a gas tank!")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# Instances as Attributes
# Part of one class can be re-written as another class (you may want to do this
# when your Classes are getting too large and can be split off)
class Battery():
    """A simple attempt to model an electric car battery"""
    def __init__(self, battery_size=70):
        """Initialise the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approximately " + str(range)
        message += " miles on a full charge"
        print(message)

    def upgrade_battery(self):
        """Upgrade the battery to 85 if it isn't already"""
        if self.battery_size < 85:
            self.battery_size = 85

class ElectricCarNew(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_other_tesla = ElectricCarNew('tesla', 'model s', 2019)
print("")
print(my_other_tesla.get_descriptive_name())
my_other_tesla.battery.describe_battery()
my_other_tesla.battery.get_range()

# Exercise 9.6 - Ice Cream Stand
# Write a class IceCreamStand that inherits from the Restaurant class.
# Add an attribute called flavors that stores a list of ice cream flavors.
# Write a method that displays these flavors.
class IceCreamStand(Restaurant):
    """Inherits from Restaurant."""
    def __init__(self, restaurant_name, cuisine_type, flavours):
        """
        Initialise attributes of the parent class.
        Then initialise attributes specific to an Ice Cream Stand
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = flavours

    def describe_flavours(self):
        print("The ice cream flavours available are: ")
        for i in self.flavours:
            print(i)

my_ice_cream_stand = IceCreamStand('Adam"s Ice Creams', 'Ice Cream',
    ['chocolate', 'vanilla'])
print("")
my_ice_cream_stand.describe_flavours()

# Exercise 9.7 - Admin
# An administrator is a special kind of user. Write a class 'Admin' that
# inherits from the User class. Add an attribute privileges that stores a list
# of strings like "can add post", "can delete post", "can ban user". Include a
# method show_prileges()
class User():
    """A simple attempt to model a User"""
    def __init__(self, first_name, last_name):
        """Initialise both attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.created = '2019-01-01'
        self.last_login = '2019-07-01'
        self.country = 'United Kingdom'

    def describe_user(self):
        print("The user's name is: " + self.first_name.title() + " " +
            self.last_name.title())
        print("The user was created on " + self.created + ", last logged in: "
            + self.last_login)
        print("The user country is " + self.country)

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " +
            self.last_name.title())

user_lauren = User('lauren', 'baker')
user_lauren.describe_user()

class Admin(User):
    """Admin user inherits from User class"""
    def __init__(self, first_name, last_name):
        """
        Initialise attrbiutes of the parent class.
        Then initialise attributes specific to an Admin user.
        """
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        self.describe_user
        print("The user also has the following privileges: ")
        for p in self.privileges:
            print("\t" + p)

user_adam = Admin('adam', 'baker')
user_adam.show_privileges()

# Exercise 9.8 - Privileges
# Write a separate Privileges class. The class should have one attribute:
# privileges that stores a list of strings. Also create a show_privileges()
# method
class Privileges():
    """A simple attempt to model user privileges"""
    def __init__(self, privileges):
        """Initialise the Prilege's attributes."""
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("The user has the following privileges: ")
        for p in self.privileges:
            print("\t" + p)

class AdminNew(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges(['x', 'y', 'z'])

user_lynn = AdminNew('lynn', 'baker')
user_lynn.privileges.show_privileges()

# Exercise 9.9 - Battery Upgrade
# Use the final version of electric_car.py. Add a method to the Battery class
# called upgrade_battery(). This method should check the battery size and set
# the capacity to 85 if it isn't already. Make an electric car with a default
# battery size, call get_range() once, and then call get_range() a second time
# after upgrading the battery.

# see from rows 166 for upgrade_battery() method
my_new_jag = ElectricCarNew('jaguar', 'e-type', 2019)
print("")
print(my_new_jag.get_descriptive_name())
my_new_jag.battery.describe_battery()
my_new_jag.battery.get_range()
my_new_jag.battery.upgrade_battery()
my_new_jag.battery.describe_battery()
my_new_jag.battery.get_range()

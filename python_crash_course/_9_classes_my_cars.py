from _9_classes_car import Car, ElectricCar
# Alternatively - import an eniter module
import _9_classes_car

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())

# Using the 'import _9_classes_car' - we can use dot notation

my_other_beetle = _9_classes_car.Car('volswagen', 'beetle', 2017)
print(my_other_beetle.get_descriptive_name())
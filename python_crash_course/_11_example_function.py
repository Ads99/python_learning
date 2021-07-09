# The following would fail the unit test
#def get_formatted_name(first, middle, last):
def get_formatted_name(first, last, middle=''):
	"""Generate a neatly formatted full name."""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()

# Exercise 11.1 - City, Country
# Write a function that accepts two params: city, county. The function should 
# return a single string of the form City, Country
def get_formatted_location(city, country, population=0):
	"""Generate a neatly formatted location"""
	if population:
		location = city + ', ' + country + ' - population ' + str(population)
	else:
		location = city + ', ' + country
	return location.title()